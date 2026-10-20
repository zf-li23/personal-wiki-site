---
title: Debugging and Testing
description: Kinds of program errors and compiler warnings; the debugging process of reproduce, diagnose, fix and reflect; print debugging; breakpoints, conditional breakpoints, single stepping, watching variables and the call stack in a debugger (GDB, VS Code, pdb); AddressSanitizer and UBSan; test cases, boundary conditions and off-by-one errors, unit testing and differential testing; defensive programming and assertions.
source_hash: 4cbb2bb50db5
---

More than half of the time spent writing programs often goes into finding errors. *Debugging* is the process of finding and correcting program errors, and testing is the process of finding errors by running the program: testing answers "is there an error?", and debugging answers "where is it?". This chapter introduces the methods and current tools for both: it first explains the kinds of errors and the general debugging process, then introduces debuggers, compiler warnings and runtime checking tools, and finally discusses how to design tests and how to use assertions to expose errors early. The examples in this chapter use the loops, functions and arrays of the first four chapters; the causes of memory errors such as out-of-bounds array access and dangling pointers are in [4.1.8](/4.1.8); the systematic approach to testing in software engineering (test frameworks, continuous integration, coverage) is in [4.14](/4.14); when AI tools are used to assist debugging, the results must likewise be verified with the testing methods of this chapter ([4.2.14](/4.2.14)).

## 5.1. Kinds of Errors and the Debugging Process

### 5.1.1. Letting the Compiler Help

[4.1.1](/4.1.1) divided program errors into compile errors, runtime errors and logic errors. Of the three, the earlier an error is found, the easier it is to fix, so the first principle is to let errors show up at compile time as far as possible. Always compile with warnings turned on:

```bash
g++ -std=c++20 -Wall -Wextra -g prog.cpp -o prog
```

Warnings are not hints that can be ignored; many warnings point directly at logic errors. For example:

```cpp
int sum = 0;
for (int i = 1; i <= 10; ++i);    // stray semicolon: the loop body is empty
    sum += i;                     // error: i is not declared here
if (sum = 0) { /* ... */ }        // assignment instead of comparison
```

For the second line GCC reports "`'for' clause does not guard...` [-Wmisleading-indentation]" (if the reference to `i` in the third line is removed, the program compiles, but the loop does nothing), and for `if (sum = 0)` it reports "suggest parentheses around assignment used as truth value [-Wparentheses]". One can also add `-Werror` to treat warnings as errors, forcing oneself to deal with every warning.

Messy formatting can also hide errors. If a `return 0;` is mistakenly written inside the loop body, or the check that prints "no solution" is mistakenly written inside the loop, tidying the indentation with an automatic formatter (clang-format) often makes the problem obvious at a glance. When reading compile error messages, start from the first one, which gives the file name, line number and cause; the later errors are often a chain reaction caused by the first.

### 5.1.2. The General Debugging Process

When a program runs but the result is wrong, debugging is an experimental process:

1. Reproduce: find an input that triggers the error reliably and is as simple as possible. An error that cannot be reproduced can hardly be fixed.
2. Diagnose: form a hypothesis from the symptoms ("perhaps this term is computed wrongly"), design an experiment to confirm or refute it (print the value of this term), and gradually narrow down the range where the error lies until the cause is found.
3. Fix: correct the error, confirm with the original input that it is gone, and confirm with other inputs that no new error has been introduced.
4. Reflect: why this kind of error happened and how to avoid it in the future; add this input to the tests ([5.4](#sec-5.4)).

**Example 5.1.1** A program should compute $1 + \frac{1}{2 \cdot 2 + 1} = 1.2$ but prints `1`:

```cpp
double x = 1 + 1 / (2 * 2 + 1);
std::cout << x << '\n';            // prints 1
```

Observation: the output is exactly the first term, so we hypothesize that "the value of the second term is $0$". Experiment: print `1 / (2 * 2 + 1)` alone, and it is indeed `0`; the denominator `2 * 2 + 1` is `5`, which is not wrong; print `1 / 5` and it is still `0`. Conclusion: dividing two integers is integer division ([4.1.2](/4.1.2)), and changing `1` to `1.0` fixes it. Reflection: for every expression containing a division, think about the types of the operands.

The idea most often used in diagnosis is bisection: check an intermediate result in the middle of the program; if it is already wrong, the error is in the first half, otherwise in the second half, halving the suspect range each time.

### 5.1.3. Print Debugging

The simplest diagnostic tool is to insert output statements into the program that print the values of variables or "execution reached here":

```cpp tab
#include <iostream>

int main() {
    int total = 0;
    for (int i = 1; i <= 5; ++i) {
        total += i * i;
        std::cerr << "[debug] line " << __LINE__ << ": i=" << i
                  << " total=" << total << '\n';   // goes to standard error
    }
    std::cout << total << '\n';
    return 0;
}
```

```python tab
total = 0
for i in range(1, 6):
    total += i * i
    print(f"[debug] {i=} {total=}")   # the = specifier prints the name and the value
print(total)
```

Debugging messages are written to standard error `std::cerr` (in Python, `print(..., file=sys.stderr)`), which is separate from standard output, so it does not get mixed into the formal output of the program, and an **online judge** does not check it. `__LINE__` is the current line number (C++20 also has `std::source_location`). The drawback of print debugging is that the program must be modified and recompiled repeatedly and the statements must be deleted afterwards; for more complex programs a debugger is more effective. Formal programs use logging (the Python standard library `logging`) in place of scattered output statements, which can be turned on or off by level.

## 5.2. Debuggers

### 5.2.1. Breakpoints, Single Stepping and Watching

**Definition 5.2.1 (Debugger)** A **debugger** is a program that controls the execution of another program, makes it pause at specified positions, and inspects and modifies its state (the values of variables, memory, the **call stack**) while it is paused.

The basic operations of a debugger:

- *Breakpoint*: the program pauses before executing this line. A conditional breakpoint pauses only when a specified condition holds, such as `k >= 30`, which suits the case where a loop runs many times and fails only in one of them.
- Single stepping: after pausing, execute one line at a time. "Step over" executes the function calls in the current line completely; "step into" goes inside the called function; "step out" finishes the current function and returns to the caller.
- Continue: run to the next breakpoint or the end of the program.
- Watching: view the current values of variables and expressions; a *watchpoint* pauses when a variable is modified, to find out "who changed this variable".
- Call stack: see how the program called its way down to the current position ([4.1.4](/4.1.4)), and switch to a particular level to view its **local variables**.

A C++ program must be compiled with `-g` for the executable to contain the information about source line numbers and variable names; it is also best to turn off optimization with `-O0`, otherwise code reordered or removed by the compiler makes single stepping appear to jump around.

| Operation | GDB | VS Code | pdb |
|---|---|---|---|
| Start | `gdb ./prog`, `run` | F5 | `python -m pdb prog.py` |
| Set a breakpoint | `break 9`, `break f` | Click left of the line number, or F9 | `b 9`, `b f`; write `breakpoint()` in code |
| Conditional breakpoint | `break 9 if k >= 30` | Right-click the breakpoint, edit the condition | `b 9, k >= 30` |
| Step over / into / out | `next` / `step` / `finish` | F10 / F11 / Shift+F11 | `n` / `s` / `r` |
| Continue | `continue` | F5 | `c` |
| View a value | `print k` | Variables panel, hover, watch panel | `p k` |
| Call stack | `backtrace` | Call stack panel | `w` |

The Clang toolchain on macOS uses LLDB, whose commands are similar to those of GDB (`b`, `r`, `n`, `s`, `bt`).

### 5.2.2. Example: Finding an Array Out-of-Bounds Error

**Example 5.2.1** The following program uses the sieve ([4.1.6](/4.1.6)) to find the primes up to $30$, but when run it may print incomplete output, fall into an infinite loop or crash, with behavior varying with the compile options:

```cpp
#include <iostream>

int main() {
    const int N = 30;
    int composite[N] = {};              // composite[i] == 1 if i is composite
    for (int i = 2; i < N; ++i) {
        if (composite[i] == 0) {
            for (int k = 2 * i; k <= N; k += i)   // bug: k == N is out of bounds
                composite[k] = 1;
            std::cout << i << ' ';
        }
    }
    std::cout << '\n';
    return 0;
}
```

The array `composite` has only the indices $0 \sim 29$, but the inner loop writes `composite[30]`. An out-of-bounds write is **undefined behavior**: it may overwrite some other variable (such as `i`) that happens to lie right after the array, making the behavior of the program look entirely unrelated to the source code, which is exactly why errors of this kind are hard to find. Use GDB to set a conditional breakpoint and stop before the out-of-bounds write happens:

```text
$ g++ -std=c++20 -g -O0 sieve.cpp -o sieve
$ gdb ./sieve
(gdb) break 9 if k >= 30
Breakpoint 1 at ...: file sieve.cpp, line 9.
(gdb) run
Breakpoint 1, main () at sieve.cpp:9
9                       composite[k] = 1;
(gdb) print k
$1 = 30
(gdb) print i
$2 = 2
```

The program stops at `i = 2`, `k = 30`, just about to write index $30$. The cause is that the loop condition `k <= N` should be `k < N`. In VS Code the procedure is the same: set a breakpoint on line 9 with the condition `k >= 30`, press F5 to start debugging, and when it stops look at `k` and `i` in the variables panel. The debugger can also show addresses such as `&composite[30]` and `&i`, to verify which variable the out-of-bounds write overwrote ([4.1.8](/4.1.8)).

### 5.2.3. Debugging in VS Code

VS Code supports debugging through extensions: C++ uses Microsoft's C/C++ extension (which calls GDB or LLDB underneath) or the CodeLLDB extension, and Python uses the Python extension (which is built on debugpy). The debug configuration is written in the project's `.vscode/launch.json`, for example:

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Debug C++",
      "type": "cppdbg",
      "request": "launch",
      "program": "${workspaceFolder}/sieve",
      "args": ["30"],
      "cwd": "${workspaceFolder}",
      "MIMode": "gdb"
    },
    {
      "name": "Debug Python",
      "type": "debugpy",
      "request": "launch",
      "program": "${file}",
      "args": ["30"],
      "console": "integratedTerminal"
    }
  ]
}
```

`args` gives the command-line arguments ([5.5](#sec-5.5)); when the program reads data from standard input, it can be typed in the terminal, or redirected with `"<", "input.txt"` in `args` (depending on the debugger). A C++ program must first be compiled with `-g`; one can also configure a `preLaunchTask` to compile automatically before debugging starts.

### 5.2.4. Python's pdb

The debugger of the Python standard library is pdb. Write a line `breakpoint()` where the program should pause, and when execution reaches it the interactive pdb interface is entered; one can also start debugging from the beginning with `python -m pdb prog.py`. When the program terminates because of an exception, `python -m pdb -c continue prog.py` stops at the point of the error so that you can inspect the variables at that moment, which is called *post-mortem debugging*. In pdb one can also enter any Python expression directly to evaluate it. Since Python 3.14 one can also attach to a running Python process with `python -m pdb -p <process id>`.

The traceback that Python prints on an error is itself important debugging information: it lists each level of the call stack from the outside in (file, line number, function name), and the last line gives the type and description of the exception, such as `IndexError: list index out of range`. Read from the last line and look upward for the first place that belongs to your own code.

## 5.3. Runtime Checking Tools

Undefined behavior in C++ ([4.1.2](/4.1.2)) does not necessarily cause a crash immediately; the error may show up much later and far away. The checking tools provided by compilers (sanitizers) check for such errors while the program runs and report them at the moment they occur:

- AddressSanitizer (`-fsanitize=address`): checks memory errors such as out-of-bounds array access, use of freed memory and memory leaks;
- UndefinedBehaviorSanitizer (`-fsanitize=undefined`): checks signed **integer overflow**, division by zero, illegal shifts and so on.

Compile the program of Example 5.2.1 with `-fsanitize=address,undefined -g` and run it; the program stops immediately at the out-of-bounds write, and the report begins with:

```text
==7870==ERROR: AddressSanitizer: stack-buffer-overflow on address 0x7c016d600098 ...
WRITE of size 4 at 0x7c016d600098 thread T0
    #0 ... in main sieve.cpp:9
  This frame has 1 object(s):
    [32, 152) 'composite' (line 5) <== Memory access at offset 152 overflows this variable
```

It points out the line of the error (line 9), the operation (writing 4 bytes) and the variable that was overrun (`composite` defined in line 5, 120 bytes, that is 30 `int`s). Without the check, compiled with `-O2`, the same program behaves on this machine as `*** stack smashing detected ***: terminated`, from which we only know that the stack was corrupted, not where.

Compile with sanitizers during development and testing and remove them for release (they slow the program down by about a factor of 2 and use more memory). When an online judge reports "runtime error" or the results are sometimes right and sometimes wrong, first run the test data locally with sanitizers. Valgrind on Linux can also check memory errors without recompiling, but is much slower. In Python an out-of-bounds access raises `IndexError` and integers do not overflow, so there is no corresponding problem, at the price of a checking overhead on every access.

## 5.4. Testing

### 5.4.1. Test Cases and Boundary Conditions

**Definition 5.4.1 (Test Case)** A **test case** consists of a set of inputs of a program and the corresponding expected output. Run the program and compare the actual output with the expected output; a mismatch shows that the program has an error.

Testing can show that errors exist but cannot show that there are none (Dijkstra). The possible inputs are usually infinite, so test cases must be chosen representatively:

- Equivalence classes: divide the inputs into several classes, such that inputs in the same class are expected to be handled by the program in the same way, and choose one representative from each class. For example, for the leap-year test: not divisible by 4, divisible by 4 but not by 100, divisible by 100 but not by 400, divisible by 400; choose one year from each of the four classes.
- Boundary values: errors most often occur at boundaries. Take the boundary of each class and the values on both sides of it: empty input, a single element, the minimum and maximum, exactly equal to a threshold, just overflowing.
- Special cases: repeated elements, negative numbers and zero, all elements equal, already sorted or in reverse order.

The most common boundary error is the *off-by-one error*: a loop executing once too many or too few times, an index one too large or too small, confusing `<` and `<=`. Array indices run from $0$ to $n-1$, an interval $[a, b)$ of length $n$ contains $b - a$ integers and $[a, b]$ contains $b - a + 1$; all of this must be thought through when writing loops.

**Example 5.4.1** Decide whether a string is a palindrome (reads the same forwards and backwards). The following implementation has errors:

```cpp
bool is_palindrome(const std::string& s) {
    int n = s.size();
    for (int i = 0; i <= n / 2; ++i)
        if (s[i] != s[n - i]) return false;   // bug: should be s[n - 1 - i]
    return true;
}
```

Check by hand with a simple example: for "aba" the length is $n = 3$, and for $i = 0$ it compares `s[0]` with `s[3]`, while the index of the last character is $2$. The correct symmetric position is $n - 1 - i$. Now look at the loop range: the pairs to compare are $(0, n-1), (1, n-2), \dots$, altogether $\lfloor n/2 \rfloor$ pairs, so the condition should be `i < n / 2`; written as `<=`, $n = 4$ makes one extra comparison of `s[2]` with `s[1]` (the result is still correct, but it shows that the author did not think the range through). The corrected version and its tests are in the next section. A good set of test cases should include `""`, `"a"`, `"ab"`, `"aa"`, `"aba"`, `"abba"` and `"abca"`: lengths 0, 1, even and odd, with both true and false results.

### 5.4.2. Unit Testing and Differential Testing

*Unit testing* tests each function in a program separately. Writing the tests as code and rerunning all tests after each modification of the program immediately shows whether the modification broke existing functionality (a regression). The simplest form is a test function that calls the function under test and checks the result with assertions ([5.5](#sec-5.5)):

```cpp tab
#include <cassert>
#include <iostream>
#include <string>

bool is_palindrome(const std::string& s) {
    int n = static_cast<int>(s.size());
    for (int i = 0; i < n / 2; ++i)
        if (s[i] != s[n - 1 - i]) return false;
    return true;
}

void test_is_palindrome() {
    assert(is_palindrome(""));          // empty string
    assert(is_palindrome("a"));         // one character
    assert(!is_palindrome("ab"));       // even length, false
    assert(is_palindrome("aa"));        // even length, true
    assert(is_palindrome("aba"));       // odd length, true
    assert(is_palindrome("abba"));
    assert(!is_palindrome("abca"));
}

int main() {
    test_is_palindrome();
    std::cout << "all tests passed\n";
    return 0;
}
```

```python tab
import unittest


def is_palindrome(s: str) -> bool:
    n = len(s)
    return all(s[i] == s[n - 1 - i] for i in range(n // 2))


class TestIsPalindrome(unittest.TestCase):
    def test_short(self):
        self.assertTrue(is_palindrome(""))       # empty string
        self.assertTrue(is_palindrome("a"))      # one character
        self.assertFalse(is_palindrome("ab"))    # even length, false

    def test_longer(self):
        for s in ["aa", "aba", "abba"]:
            self.assertTrue(is_palindrome(s), s)
        self.assertFalse(is_palindrome("abca"))


if __name__ == "__main__":
    unittest.main()
```

Real projects use a test framework, which discovers and runs all tests and reports which ones fail: C++ commonly uses GoogleTest and Catch2, the Python standard library has `unittest`, and the most commonly used in the community is the third-party pytest (tests are written as functions using plain `assert`). Test frameworks, coverage and continuous integration are in [4.14](/4.14).

Another effective method is *differential testing*: write a simple reference implementation that is obviously correct but perhaps slow, run both implementations on a large number of randomly generated inputs, and compare whether the results agree. The reference implementation for palindromes is "reverse the string and compare it with the original":

```python
import random

for _ in range(10_000):
    s = "".join(random.choices("ab", k=random.randint(0, 8)))   # random short strings
    assert is_palindrome(s) == (s == s[::-1]), s                # compare with the reference
```

Random strings over just two letters with short lengths run into all kinds of boundary cases efficiently. As soon as random testing finds a disagreement, the input it prints is a minimal example that reproduces the error. In online-judge training, differential testing is the most common means of finding out "why only partial credit": write a reference solution by exhaustive search and compare it with the optimized solution.

## 5.5. Defensive Programming and Assertions

The input to a program does not always meet expectations: the user may enter letters instead of numbers, may omit a command-line argument, or the file may not exist. The principle of *defensive programming* is to handle possible unexpected situations in advance: check whether the input is valid and give clear messages on errors, instead of crashing or printing wrong results.

**Example 5.5.1** A program reads two integers from the command line and prints their sum (`./add 3 4` prints `7`). The two parameters of `main` give the command-line arguments: `argc` is the number of arguments (including the program name itself), and `argv[i]` is the string of the $i$-th argument. If `argv[1]` is accessed without checking `argc`, the program crashes when the user supplies too few arguments.

```cpp tab
#include <exception>
#include <iostream>
#include <string>

int main(int argc, char* argv[]) {
    if (argc != 3) {                                   // check the number of arguments
        std::cerr << "usage: " << argv[0] << " a b\n";
        return 1;                                      // nonzero exit status: failure
    }
    try {
        int a = std::stoi(argv[1]), b = std::stoi(argv[2]);
        std::cout << a + b << '\n';
    } catch (const std::exception& e) {                // not an integer, or out of range
        std::cerr << "invalid integer: " << e.what() << '\n';
        return 1;
    }
    return 0;
}
```

```python tab
import sys


def main() -> int:
    if len(sys.argv) != 3:                             # check the number of arguments
        print(f"usage: {sys.argv[0]} a b", file=sys.stderr)
        return 1                                       # nonzero exit status: failure
    try:
        a, b = int(sys.argv[1]), int(sys.argv[2])
    except ValueError as e:                            # not an integer
        print(f"invalid integer: {e}", file=sys.stderr)
        return 1
    print(a + b)
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

`std::stoi` and the Python `int` throw an exception when the string is not a valid integer, and `try … catch` (in Python `try … except`) catches and handles the exception; the exception mechanism is discussed in detail in the relevant chapters of [4.2](/4.2).

For external input, check and report errors; for conditions inside the program that "must hold in principle", use assertions.

**Definition 5.5.1 (Assertion)** An **assertion** is a condition that the programmer writes at some point in a program and believes must hold there. When execution reaches the assertion, the condition is checked: if it holds, execution continues; if not, the program itself has an error, and it terminates immediately and reports the file, line number and condition of the assertion.

```cpp
#include <cassert>

int days_in_month(int y, int m) {
    assert(1 <= m && m <= 12);           // precondition: the caller must pass a valid month
    /* ... */
    return 31;
}

static_assert(sizeof(int) == 4, "this program assumes a 32-bit int");   // checked at compile time
```

Assertions are often used to check the preconditions of a function (conditions the caller should guarantee), postconditions (results the function should guarantee) and **loop invariants** ([4.1.3](/4.1.3)). They turn a "wrong state" into an "immediate failure with location information", so that the error is exposed at the place closest to its cause rather than appearing far away as a strange result. `assert` works only during debugging: when the macro `NDEBUG` is defined in C++ (the compile options of release builds often contain `-DNDEBUG`), or when Python is run with `python -O`, all assertions are removed. Therefore:

- Assertions are for finding the programmer's errors and cannot be used to check user input or file contents, which must be tested with `if` and reported as errors;
- The expression in an assertion must have no **side effects**, as in `assert(++count < 10)`, otherwise the behavior of the program changes once the assertions are removed.

`static_assert` checks conditions that depend only on constants at compile time; if not satisfied, compilation fails, and there is no run-time overhead.

## Summary

- Turn on compiler warnings (`-Wall -Wextra`) and deal with them seriously; tidy the indentation with a formatter to make structural errors visible.
- Debugging is an experimental process of reproduce, diagnose, fix and reflect, narrowing the suspect range by bisection; print debugging writes to standard error.
- A debugger pauses the program at breakpoints (including conditional breakpoints), single-steps and watches variables and the call stack; compile C++ with `-g -O0`, and in Python use `breakpoint()` or pdb.
- AddressSanitizer and UBSan report an error at the moment an out-of-bounds access, overflow or other undefined behavior occurs and should be turned on during development.
- Testing can only show that errors exist: design test cases by equivalence classes and boundary values, beware of off-by-one errors; write tests as code to run repeatedly, and compare with a reference implementation on random inputs by differential testing.
- Use defensive checks for external input and assertions for conditions that must hold internally; assertions must have no side effects and cannot replace input checks.
