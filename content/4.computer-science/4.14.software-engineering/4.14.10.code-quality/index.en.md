---
title: Code Quality
description: "Writing code that other people can read, change and trust: defensive programming and its trade-offs; layout and coding standards, with formatters; naming conventions and bad names; self-documenting code; comments that explain why; code smells, cyclomatic complexity and the ABC metric, linters and type checkers with real output; refactoring as a sequence of behavior-preserving steps, with a worked example under tests; design smells, design patterns and the SOLID principles; and code quality when AI agents write the code."
---

A program is read far more often than it is written: by reviewers, by colleagues who extend it, by the maintainer who fixes it years later, and by the author, who after a few months is a stranger to it as well. Code quality is the property of code that keeps this reading cheap and safe. This chapter belongs to the "good code" line of the course ([4.14.1](/4.14.1)): it starts with defensive programming, which keeps code from failing when its assumptions are violated (10.1); then turns to the presentation of code, its layout (10.2), names (10.3), structure (10.4) and comments (10.5). Section 10.6 shows how to detect bad code by its smells, by metrics and by static analysis tools; 10.7 explains how to improve it safely by refactoring; and 10.8 lifts the discussion from functions to classes, where code smells become design smells and the remedies are **design patterns** and the SOLID principles ([4.2.13](/4.2.13)). The tests that make refactoring safe are the subject of the next two chapters ([4.14.11](/4.14.11), [4.14.12](/4.14.12)). Examples are in Python and were run with Python 3.14, ruff 0.17, radon 6.0, mypy 2.4 and pytest 9.1; the C fragments illustrate layout only.

## 10.1. Defensive Programming

### 10.1.1. Assume Nothing

Murphy's law states: "If anything can go wrong, it will." Its original form is more precise: if there is more than one way to do a job, and one of those ways will result in disaster, then somebody will do it that way. For code, it reads: if your code can be used incorrectly, it will be. Inputs will be empty, too long, malformed or hostile; functions will be called in the wrong order; files will be missing; the network will time out; and code written for one context will be reused in another.

**Defensive programming** ([4.1.5](/4.1.5)) is the discipline of writing each piece of code so that it continues to behave sensibly when such things happen. Its first rule is to *assume nothing*: unwritten assumptions are a constant source of faults, and they multiply as code grows and changes hands. A classic example is a function that crashes on an input longer than 1000 characters, written by a programmer who thought that nobody would ever enter such a long input; an attacker will, and a buffer overflow is the result.

The failure of Ariane 5 (Example 1.1.1) shows how unwritten assumptions combine. Several decisions, each reasonable in its context, had to coincide:

- In the inertial reference software of Ariane 4, the conversion of a 64-bit floating-point value (the horizontal bias, related to horizontal velocity) to a 16-bit signed integer was left unprotected, to keep the processor load low; an analysis had shown that on the Ariane 4 trajectory the value could not overflow.
- The software was reused unchanged in Ariane 5, whose trajectory produces much larger horizontal velocities early in flight. The assumption that justified the missing protection was recorded in the Ariane 4 analysis, not in a form that anybody re-checked against the new trajectory.
- The alignment function containing the conversion was useful only before lift-off, but it kept running for about 40 seconds after lift-off, a requirement inherited from Ariane 4 to allow a quick restart after a hold in the countdown.

The overflow raised an exception that shut down both inertial units. Each of these decisions rested on an assumption that was true for Ariane 4 and false for Ariane 5; a single check of the conversion's range, or a re-examination of the assumptions, would have prevented the loss.

### 10.1.2. Handling Bad Input

A program can respond to bad input in several ways, from worst to best:

| Response | Name | Example |
|---|---|---|
| Process it and produce wrong results | garbage in, garbage out | a negative quantity yields a negative invoice |
| Accept it and do nothing | garbage in, nothing out | the form silently discards the order |
| Reject it with a clear message | garbage in, error message out | "quantity must be a positive integer" |
| Make bad input impossible | no garbage allowed in | a number field with a minimum of 1, a type that cannot hold invalid values |

Defensive programming aims for the last two rows. The practical rules are to check the values of all data from external sources (files, network requests, users, environment variables); to check the values of all input parameters of a function, at least at the boundaries of a module; and to decide deliberately how to handle bad input. The decision depends on who is at fault:

- Bad input from outside the program is an expected event. It is reported to the caller as an error, typically by raising an exception with a precise message, or by returning an error value, and the program continues.
- A violated internal assumption is a bug in the program. It is checked with an **assertion** ([4.1.5](/4.1.5)), which stops the program at the point where the bug becomes visible instead of letting a corrupted state propagate. Assertions are not a means of validating input: Python removes `assert` statements when run with `-O`.

```python
from dataclasses import dataclass

MAX_QUANTITY = 1000


@dataclass(frozen=True)
class OrderLine:
    sku: str
    quantity: int

    def __post_init__(self) -> None:
        # Validate at construction, so that no invalid OrderLine can exist.
        if not self.sku:
            raise ValueError("sku must not be empty")
        if not 1 <= self.quantity <= MAX_QUANTITY:
            raise ValueError(f"quantity must be in 1..{MAX_QUANTITY}, got {self.quantity}")


def parse_line(text: str) -> OrderLine:
    """Parse 'SKU,QUANTITY' from an uploaded file."""
    sku, sep, qty = text.partition(",")
    if not sep or not qty.strip().isdigit():
        raise ValueError(f"malformed order line: {text!r}")
    return OrderLine(sku.strip(), int(qty))
```

The class validates itself in its constructor, so that every function receiving an `OrderLine` can rely on its invariants without checking them again; this is the "no garbage allowed in" strategy realized with types. Checking at the boundary and trusting inside is the usual compromise between safety and duplication.

### 10.1.3. Costs and Benefits

| Against | For |
|---|---|
| Checks cost some run time | Checks save hours of debugging, because a failure is reported where it starts |
| Each check is extra code to write, test and read | Working code that is slightly slower is far superior to code that works most of the time and occasionally fails spectacularly |
| Too many checks obscure the main logic | Checks document the assumptions that would otherwise remain unwritten |

The cost argument is rarely decisive: a range check costs nanoseconds, a crash in production costs hours or more. The readability argument is real, and it is answered by placing checks at module boundaries and in constructors, as above, rather than repeating them in every function.

## 10.2. Layout and Presentation

### 10.2.1. Code Is Written for People

Source code has three audiences. The compiler or interpreter needs only correct syntax. The author understands the logic at the moment of writing, which is why code written only for oneself confuses its author during later maintenance. The third audience matters most and is considered least: other programmers, the colleagues and future maintainers, including the future self, who need to read, modify and extend the code. Write for their benefit.

Presentation has a real effect on quality, because programmers read meaning into code from its layout. Good presentation reveals the structure of the code; bad presentation misleads and can hide bugs. In C, the indentation of the following lines suggests that both are guarded by the `if`, but only the first is:

```c
if (user_is_admin)
    grant_access();
    log_access();       // runs for everyone, despite the indentation
```

The same class of mistake caused Apple's "goto fail" vulnerability in 2014: a duplicated `goto fail;` line, indented as if it belonged to an `if`, skipped the final step of TLS certificate verification. Python avoids this particular trap by making indentation part of the syntax; compilers such as GCC and Clang warn about it (`-Wmisleading-indentation`).

### 10.2.2. Layout Styles

A good layout is *consistent* (one style across the whole project: indentation, braces, spacing, line length), *conventional* (one of the major styles in use in the industry rather than a private invention) and *concise* (easy to learn and follow). The classical brace styles of C-like languages differ only in where the braces go:

```c
int kr_style(void) {              /* K&R, also used by Java and most C++ guides */
    int a = 0, b = 0;
    while (a != 10) {
        b++;
        a++;
    }
    return b;
}

int allman_style(void)            /* Allman: braces on their own lines */
{
    int a = 0, b = 0;
    while (a != 10)
    {
        b++;
        a++;
    }
    return b;
}

int gnu_style (void)              /* GNU: braces indented by half a level */
{
  int a = 0, b = 0;
  while (a != 10)
    {
      b++;
      a++;
    }
  return b;
}
```

There are others (Whitesmiths indents the braces together with the body). None is objectively best; what matters is that a project chooses one. Layout rules cover more than braces: the indentation of control structures, the form of individual statements (one statement per line, spaces around operators), the layout of functions and classes (blank lines between them, order of members) and of comments.

### 10.2.3. Coding Standards and Formatters

A *coding standard* is a documented set of rules for the layout, naming and use of language features in a project. Some well-known ones, each with its own focus:

| Standard | Focus |
|---|---|
| Indian Hill C Style and Coding Standards (AT&T Bell Labs) | readability and team collaboration |
| GNU Coding Standards | portability and the conventions of free software |
| MISRA C and MISRA C++ (Motor Industry Software Reliability Association) | safety and reliability of embedded, safety-critical systems; the 1998 edition had 127 rules, current editions (MISRA C:2023, MISRA C++:2023) well over a hundred guidelines, checked by dedicated tools |
| SEI CERT C, C++ and Java Coding Standards | security: rules that prevent vulnerabilities |
| PEP 8 (Python), Google style guides (C++, Java, Python, TypeScript and others), C++ Core Guidelines | the community conventions of a language |

Pick a single good style and stick to it. Today, the layout part of a standard is best enforced by a *formatter*, a tool that rewrites code into the canonical style automatically: `ruff format` or Black for Python, clang-format for C and C++, Prettier for JavaScript and TypeScript, `gofmt` and `rustfmt`, whose output is the de facto standard of their languages. A formatter ends arguments about style, removes style comments from **code review**, and keeps diffs small because nobody reformats other people's lines. Here `ruff format` is applied to a carelessly written function:

```python
import os, sys
import json
def load_orders(path,default=[]):
    try:
        f=open(path)
        data=json.load(f)
    except:
        return default
    result = [ ]
    for o in data :
        if o['status']=='paid' or o['status']=='shipped' : result.append( o )
    if result == None: return default
    return result
```

```text
$ ruff format --diff messy.py
--- messy.py
+++ messy.py
@@ -1,13 +1,17 @@
 import os, sys
 import json
-def load_orders(path,default=[]):
+
+
+def load_orders(path, default=[]):
     try:
-        f=open(path)
-        data=json.load(f)
+        f = open(path)
+        data = json.load(f)
     except:
         return default
-    result = [ ]
-    for o in data :
-        if o['status']=='paid' or o['status']=='shipped' : result.append( o )
-    if result == None: return default
+    result = []
+    for o in data:
+        if o["status"] == "paid" or o["status"] == "shipped":
+            result.append(o)
+    if result == None:
+        return default
     return result

1 file would be reformatted
```

The formatter changes only the layout; the much more serious problems of this function (the bare `except`, the mutable default argument, the file that is never closed) are found by a linter in 10.6.3.

Good programmers know how layout affects readability and strive for the clearest code; they adopt the house style even when it contradicts their personal preference. Bad programmers are convinced that their own view is the only right one, have no consistent style, and trample over other people's code in their own style.

## 10.3. Naming

### 10.3.1. What a Name Says

People read the meaning of a thing from its name. A good name describes the identity of a thing (what it is), its behavior (its role, relationships and interactions) and makes it recognizable: naming a concept turns a vague idea into a well-defined part of the design. Programmers name variables, constants, functions, types (classes, enumerations, structures, type aliases), modules and packages, **namespaces**, macros, subsystems and source files.

A good name is:

- *descriptive*: `user_age`, `calculate_order_total`, not `x` or `do_it`;
- *technically correct*: valid in the language, with no spaces, and with characters (underscores, Unicode, case) the language and tools handle reliably;
- *idiomatic*: following the naming convention of the language;
- *appropriate*: long enough to be clear (prefer clarity over brevity), and serious in tone; `foo`, `bar` and jokes do not belong in production code.

### 10.3.2. Conventions by Kind

- Variables are nouns or noun phrases: `order_form`, `count`; Boolean variables read as predicates: `is_valid`, `has_children`.
- Functions are verbs or verb phrases: `count_apples()`, `send_invoice()`. A function is named from the viewpoint of its caller, for what it does, hiding how it does it: `find_customer`, not `loop_over_customer_table`.
- Types are nouns: `Invoice`, `Window`. Interfaces often name a capability: `Serializable`, `Comparable`. Avoid redundant words (`InvoiceClass`, `InvoiceData`, `InvoiceObject` say nothing that `Invoice` does not).
- Namespaces and packages group names to avoid collisions; their names should reflect the logical relationships of their contents. Java's package names, for example, are nested like reversed Internet domain names (`org.apache.commons.lang3`).

Case conventions distinguish kinds of names, and they differ between languages:

| Kind | Python (PEP 8) | Java | C# | C++ (common) | JavaScript / TypeScript |
|---|---|---|---|---|---|
| local variable, parameter | `snake_case` | `camelCase` | `camelCase` | `snake_case` or `camelCase` | `camelCase` |
| function, method | `snake_case` | `camelCase` | `PascalCase` | `snake_case` or `camelCase` | `camelCase` |
| class, type | `PascalCase` | `PascalCase` | `PascalCase` | `PascalCase` | `PascalCase` |
| constant | `UPPER_CASE` | `UPPER_CASE` | `PascalCase` | `kPascalCase` (Google) or `UPPER_CASE` | `UPPER_CASE` or `camelCase` |
| package, module | `lowercase` | `lowercase` | `PascalCase` | `snake_case` | `kebab-case` files |

Case can carry meaning within one convention: in Python, `Window` is a type and `window` an instance of it; in C#, a local `count` and a public property `Count`.

### 10.3.3. Bad Names

| Defect | Example | Better |
|---|---|---|
| Cryptic: random abbreviations, single letters outside tiny scopes | `nmbr_aps`, `t2`, `proc_dt` | `apple_count`, `retry_timeout`, `processing_date` |
| Verbose | `the_number_of_apples_before_i_started_eating` | `initial_apple_count` |
| Inaccurate or misleading | `customer_list` holding a dictionary; `get_size()` that also resizes | `customers_by_id`; split into two functions |
| Ambiguous or vague | `data`, `value`, `info`, `manager`, `temp` | a name that says what the value represents |
| Differing only in case or one character | `user` and `User` in the same scope; `item1`, `iteml` | names that differ in meaning |
| Shadowing an outer name | a local `list` or `id` in Python | `items`, `user_id` |

A name that says the opposite of what the code does is worse than a meaningless one:

```c
void checkForContinue(bool weShouldContinue)
{
    if (weShouldContinue) abort();
}
```

The function does not check anything, and it aborts exactly when told to continue. Good programmers treat names with respect: they think about the name of everything they create, balance length against clarity and context, and keep names consistent across a project. Bad programmers produce write-once code, ignore the idioms of the language, and name things inconsistently because they do not consider how their piece fits into the whole.

## 10.4. Self-Documenting Code

The traditional answer to unreadable code was documentation: long documents about the code and long comments in it. Separate documents are expensive to write and to read, fall out of step with the code at the first change, and are hard to find, so important information in them is easily missed. The only document that describes code completely and correctly is the code itself. *Self-documenting code* is code whose names, types and structure make its intent clear without further explanation: write code to be read by humans, easily; the compiler will cope.

Compare two implementations of the same function:

```c
int fval(int i) {
    int ret = 2;
    for (int n1 = 1, n2 = 1, i2 = i - 3; i2 >= 0; --i2) {
        n1 = n2; n2 = ret; ret = n2 + n1;
    }
    return (i < 2) ? 1 : ret;
}
```

```c
int fibonacci(int position) {
    if (position < 2) {
        return 1;
    }
    int previous_but_one = 1;
    int previous = 1;
    int answer = 2;
    for (int n = 2; n < position; ++n) {
        previous_but_one = previous;
        previous = answer;
        answer = previous + previous_but_one;
    }
    return answer;
}
```

Both compute the Fibonacci numbers $1, 1, 2, 3, 5, \dots$ indexed from $0$. The first is short, but the reader must simulate it to discover what it does; the second explains itself. Even the smallest and most elegant functions need maintenance later, and the cost of that maintenance is the cost of understanding them.

The techniques of self-documenting code:

- Make the normal path obvious. Order `if`–`else` chains consistently, for example always the normal case first and the error case second, or always errors first as *guard clauses* that return early.
- Avoid deep nesting. The second `fibonacci` returns early for small positions; a version with a single exit point would have to nest the whole loop inside `if (position >= 2)`. Structured programming once insisted on a single entry and a single exit; today the usual balance is to accept several early exits in exchange for flat code.
- Do not optimize at the expense of clarity. Never optimize code unless you have shown that it is a bottleneck for acceptable performance (profiling is treated in [4.4.7](/4.4.7)); keep the clear version as the reference and the test oracle.
- Decompose into atomic functions: one function, one action, short, with no surprising **side effects**.
- Make important code stand out, and group related information using the language's features (a class, a data class, a module) rather than relying on proximity.
- Choose meaningful names (10.3) and descriptive types: an `OrderLine` or an enumeration says more than a tuple or a string, and a type checker can verify it.
- Name constants. A *magic number* is an unexplained literal in code, such as `if total >= 199`; a named constant `FREE_SHIPPING_THRESHOLD = 199` explains the meaning, and a change to it is made in one place.

Good programmers write clear, self-documenting code and the least documentation necessary, thinking of the programmers who will maintain it. Bad programmers either write no documentation at all or let it rot, think that what was hard to write should be hard to understand, and are proud of unfathomable *spaghetti code*: code whose control flow is so tangled that it cannot be followed.

## 10.5. Comments

Comments should be written in sufficient number, and no more. They are easier to write badly than well, and a bad comment can do more harm than none, because readers believe it. What matters is the quality of comments, not their quantity. Three kinds can be told apart in the following Java fragments:

```java
// sum from 1 to num                         <- wrong: the loop adds 1, not i,
sum = 0;                                     //    and stops before num
for (int i = 1; i < num; i++) {
    sum = sum + 1;
}

// set product to "base"                     <- repeats the code
product = base;
// loop from 2 to "num-1"
for (int i = 2; i < num; i++) {
    // multiply "base" by "product"
    product = product * base;
}

// compute the square root of num using the Newton-Raphson approximation
r = num / 2;                                 // <- explains the intent
while (Math.abs(r - (num / r)) > TOLERANCE) {
    r = 0.5 * (r + (num / r));
}
```

The rules for good comments:

- Explain why, not how. The code says how; the comment says why it is done this way, what it is for, or what would go wrong otherwise.
- Do not describe the code. A comment that repeats the code doubles the reading and goes wrong as soon as one of them changes.
- Document the unexpected: workarounds, non-obvious performance tricks, constraints imposed from outside.
- Tell the truth, and keep comments worthwhile and clear.

Two comments that earn their place:

```java
// Use a right shift to divide by two: replacing the division
// cut the loop time by 75% (profiled on the production data set).
elementList[element] = elementList[element] >> 1;

/* Work around an error in writeData() that appears only when the third
   parameter equals 500. '500' has been replaced with a named constant. */
if (blockSize == WRITEDATA_BROKEN_SIZE) {
    blockSize = WRITEDATA_WORKAROUND_SIZE;
}
writeData(file, data, blockSize);
```

Often a comment is a sign that the code should be improved instead. Improving code and comments in turn:

| Step | Code | Assessment |
|---|---|---|
| 1 | `// if account flag is zero` `if (accountFlag == 0)` | the comment repeats the code |
| 2 | `// if establishing a new account` `if (accountFlag == 0)` | better comment: it states the intent |
| 3 | `if (accountType == AccountType.NEW_ACCOUNT)` | better code: the intent is in the code, the comment is unnecessary |
| 4 | `// Establish a new account` `if (accountType == AccountType.NEW_ACCOUNT) { … }` | a comment that summarizes the whole block |

Further guidance:

- Choose a low-maintenance style. Boxes of asterisks with a right border, and column-aligned tables of variables in comments, must be re-aligned after every edit and soon decay; plain block comments do not.
- A file header comment describes the purpose and contents of the file, and carries a legal notice where required. It should not list every function, class and global variable of the file (such a list is out of date immediately), nor the version and modification history, which the **version control system** records ([4.14.3](/4.14.3)).
- Interface documentation is a comment of a special kind: docstrings in Python, Javadoc, Doxygen. It documents the contract of a function (what it does, its parameters, return value, errors, preconditions) for callers who do not read its body, and it is extracted into reference documentation by tools.

Good programmers write a few really good comments that explain why, and concentrate on writing good code rather than a plethora of comments. Bad programmers cannot tell good comments from bad ones, explain how, write comments that make sense only to themselves, bolster bad code with many comments, and fill files with redundant information.

## 10.6. Detecting Bad Code

### 10.6.1. Code Smells

**Definition 10.6.1 (Code Smell)** A **code smell** is a surface characteristic of code that usually indicates a deeper problem in its design: not a bug, since the code works, but a sign that the code will be hard to understand or change. The term is due to Kent Beck and was popularized by Martin Fowler's book *Refactoring* (1999; 2nd edition 2018), which pairs each smell with the refactorings that remove it.

Fowler's catalog names more than twenty smells; the most common, with the names of the 2nd edition (1st-edition names in parentheses):

| Smell | Symptom |
|---|---|
| Mysterious Name | the name does not say what the thing does (10.3) |
| Duplicated Code | the same structure in several places; a fix must be repeated in each |
| Long Function (Long Method) | a function too long to understand at a glance |
| Large Class | a class with too many fields and methods, doing several jobs |
| Long Parameter List | many parameters, hard to call and to test |
| Data Clumps | the same group of values travels together through many functions |
| Primitive Obsession | strings and numbers where a small type (money, date range, phone number) belongs |
| Repeated Switches (Switch Statements) | the same `switch` or `if` chain on a type code in several places |
| Divergent Change | one module is changed for many unrelated reasons |
| Shotgun Surgery | one change requires small edits in many modules |
| Feature Envy | a function uses the data of another class more than its own |
| Message Chains | `a.get_b().get_c().get_d()`: the caller depends on the whole navigation path |
| Middle Man | a class that only delegates to another |
| Insider Trading (Inappropriate Intimacy) | classes that know each other's internals |
| Speculative Generality | hooks and abstractions for cases that never occur |
| Temporary Field | a field that is set only in some situations |
| Lazy Element (Lazy Class) | a class or function that does too little to justify itself |
| Data Class | a class with only fields and accessors, whose behavior lives elsewhere |
| Refused Bequest | a subclass that does not want what it inherits |
| Comments | comments used as deodorant for unclear code (10.5) |

Divergent change and shotgun surgery are the two faces of bad modularity: the first is weak **cohesion**, the second strong **coupling** (Definition 5.5.2). The Long Parameter List smell deserves a closer look because it is so common. A function with many parameters is hard to cover by tests, since the number of combinations grows quickly, and hard to replace by a test double in the tests of its callers. A Boolean parameter is a warning sign: if a function behaves differently depending on its value, it should probably be two functions. And if the same arguments travel in a pack through many functions, they form a data clump that should become a class of its own (the refactoring Introduce Parameter Object).

### 10.6.2. Complexity Metrics

Smells are judged by people; metrics are computed by tools. Two metrics of the complexity of a function are in common use.

**Definition 10.6.2 (Cyclomatic Complexity)** The **cyclomatic complexity** of a program, introduced by Thomas McCabe (1976), is the number of linearly independent paths through its control-flow graph. For a control-flow graph $G$ with $E$ edges, $N$ nodes and $P$ connected components (one per function),
$$
V(G) = E - N + 2P.
$$

For a single function ($P = 1$) with structured control flow, three ways of computing it agree:

- $V(G) = E - N + 2$;
- $V(G)$ = the number of decisions $+ 1$, where each `if`, `elif`, loop (`for`, `while`), `case` and `except` counts as one decision;
- $V(G)$ = the number of regions into which the graph, drawn in the plane, divides the plane, counting the outer region.

A sequence of statements has $V = 1$; an `if`–`then`–`else`, a `while` loop and a repeat–until loop each have $V = 2$. The number $V(G)$ is also the size of a basis of paths, from which every path can be combined, and therefore the number of test cases needed in basis path testing ([4.14.11](/4.14.11)).

The following function computes a shipping cost:

```python
def shipping_cost(order):
    cost = 0.0
    if order.weight <= 1:
        cost = 5.0
    elif order.weight <= 5:
        cost = 8.0
    else:
        cost = 8.0 + (order.weight - 5) * 1.5
    if order.express:
        cost *= 2
    if order.country != "CN":
        if order.country in ("JP", "KR"):
            cost += 20
        else:
            cost += 45
    for item in order.items:
        if item.fragile:
            cost += 3
    if order.total >= 199 and not order.express:
        cost = 0.0
    return cost
```

It contains eight decisions (`if`, `elif`, `if`, `if`, nested `if`, `for`, `if`, `if`), so $V = 9$. Two tools report:

```text
$ ruff check --select C901 --config 'lint.mccabe.max-complexity = 5' shipping.py
shipping.py:1:5: C901 `shipping_cost` is too complex (9 > 5)
Found 1 error.
$ radon cc -s shipping.py
shipping.py
    F 1:0 shipping_cost - B (10)
```

Ruff implements McCabe's count; radon also counts the Boolean operator `and` in the last condition as a decision, since `order.total >= 199 and not order.express` hides two conditions (this variant is sometimes called extended cyclomatic complexity). Radon's letter grade A means 1–5, B means 6–10.

**Definition 10.6.3 (ABC Metric)** The **ABC metric** (Jerry Fitzpatrick, 1997) measures the size of a function by three counts: $A$, the number of assignments (`=`, `+=`, `-=`, `*=`, `++` and similar operators that store a value); $B$, the number of branches in the sense of transfers of control to other code, chiefly function and method calls; and $C$, the number of conditions (comparisons such as `<`, `==`, `!=` and the keywords `else`, `case`, `default`, and the `?` of a conditional expression). The ABC score is the length of the vector $(A, B, C)$:
$$
|ABC| = \sqrt{A^2 + B^2 + C^2}.
$$

Commonly used thresholds are a cyclomatic complexity of at most 10 per function, the limit recommended by the NIST report on structured testing (SP 500-235, 1996, which allows up to 15 in justified cases), and an ABC score of about 20 per method, a rule of thumb from the Ruby community, where tools such as Flog and RuboCop compute it. Metrics should be taken with a grain of salt. Like test coverage, they are better at pointing out where improvement is needed than at certifying that code is good: a function with complexity 3 can still be unreadable. The most useful targets are *hotspots*, places where several metrics raise flags at once, especially when the version history shows that they also change often.

### 10.6.3. Static Analysis Tools

**Definition 10.6.4 (Static Analysis)** **Static analysis** is the examination of a program without executing it, to find defects, violations of coding rules and other quality problems. A tool that performs lightweight static analysis of source code for likely errors and violations of a coding standard is called a **linter**, after the Unix program `lint` (Stephen Johnson, 1978), which checked C programs.

Linters find the problems that a formatter leaves alone. Applied to the function of 10.2.3:

```text
$ ruff check --select E,F,B,SIM messy.py --output-format concise
messy.py:1:1: E401 [*] Multiple imports on one line
messy.py:1:8: F401 [*] `os` imported but unused
messy.py:1:12: F401 [*] `sys` imported but unused
messy.py:3:30: B006 Do not use mutable data structures for argument defaults
messy.py:5:11: SIM115 Use a context manager for opening files
messy.py:7:5: E722 Do not use bare `except`
messy.py:11:58: E701 Multiple statements on one line (colon)
messy.py:12:18: E711 Comparison to `None` should be `cond is None`
messy.py:12:22: E701 Multiple statements on one line (colon)
Found 9 errors.
[*] 3 fixable with `--fix` (2 unsafe fixes available with `--fix --unsafe-fixes`).
```

Several of these are real bugs: the mutable **default argument** `[]` is shared between calls, so a caller who appends to the returned default changes it for everybody ([4.4.1](/4.4.1)); the bare `except` also catches `KeyboardInterrupt` and hides programming errors such as a misspelled name; and the file is never closed. The rule codes name their origin: `E` and `F` come from pycodestyle and Pyflakes, `B` from flake8-bugbear, `SIM` from flake8-simplify, all reimplemented in ruff. Rules are selected in the project configuration, so that every developer and the CI pipeline apply the same ones:

```toml
# pyproject.toml
[tool.ruff]
line-length = 100

[tool.ruff.lint]
select = ["E", "F", "B", "SIM", "UP", "I", "C901"]   # I: import sorting
mccabe.max-complexity = 10
```

A **type checker** is a static analyzer for **type annotations** ([4.4.1](/4.4.1)). It finds errors that would otherwise appear only when an unusual path is executed:

```python
def average(values: list[float]) -> float:
    return sum(values) / len(values)


def report(scores: dict[str, list[float]]) -> str:
    best = max(scores, key=lambda name: average(scores[name]))
    return "best: " + best + " with " + average(scores[best])
```

```text
$ mypy typed.py
typed.py:7: error: Unsupported operand types for + ("str" and "float")  [operator]
Found 1 error in 1 file (checked 1 source file)
```

The main static analysis tools by language:

| Language | Formatter | Linter | Type checker or deeper analysis |
|---|---|---|---|
| Python | ruff format, Black | ruff, Pylint | mypy, Pyright |
| JavaScript / TypeScript | Prettier | ESLint, Biome | the TypeScript compiler (`tsc`) |
| C / C++ | clang-format | clang-tidy, cppcheck | compiler warnings, sanitizers at run time, Coverity |
| Java | google-java-format | Checkstyle, PMD | SpotBugs, Error Prone |
| multi-language | | | SonarQube, CodeQL, Semgrep |

Static analysis is most effective when it runs continuously: in the editor as one types, in a pre-commit hook before each commit, and in the CI pipeline as a quality gate on every pull request ([4.14.3](/4.14.3)). Continuous inspection services such as SonarQube track the health of a code base over time: duplicated code, violations of coding standards, complexity, comments, likely bugs and security vulnerabilities. When a team adopts a linter on an existing code base, it usually enables the rules for new code first, or records the existing violations as a baseline, so that the number of warnings can only fall.

## 10.7. Refactoring

### 10.7.1. Definition

**Definition 10.7.1 (Refactoring)** **Refactoring** is a disciplined technique for restructuring an existing body of code, altering its internal structure without changing its external behavior. Its heart is a series of small behavior-preserving transformations, each of which is itself called a refactoring; the system is kept fully working after each step.

Refactoring improves non-functional qualities of code, chiefly simplicity, flexibility and understandability, and sometimes performance. Two conditions make it safe. The steps are small, so that a mistake is found immediately and is easy to undo; and there are automated tests that are run after each step, because "without changing its external behavior" is a claim that must be checked, not assumed. Where a piece of legacy code has no tests, the first step is to write *characterization tests*, tests that record what the code currently does, before changing it. Refactoring is not a separate project phase but part of everyday work: in test-driven development ([4.14.12](/4.14.12)) it is the third step of every cycle, and a common rule is to refactor the code one is about to change so that the change becomes easy.

Fowler's catalog gives each refactoring a name, a motivation and mechanical steps. Two small inverse pairs show the idea. Inline Function replaces a call by the body of the function when the body is as clear as the name; Extract Function does the opposite:

```java
// before: the helper adds nothing to the body
int getRating() { return moreThanFiveLateDeliveries() ? 2 : 1; }
boolean moreThanFiveLateDeliveries() { return numberOfLateDeliveries > 5; }

// after Inline Function
int getRating() { return (numberOfLateDeliveries > 5) ? 2 : 1; }
```

Inline Variable removes a temporary variable that only names an expression which is already clear: `double basePrice = anOrder.basePrice(); return basePrice > 100;` becomes `return anOrder.basePrice() > 100;`.

The smells of 10.6.1 map to refactorings:

| Smell | Refactorings |
|---|---|
| Large Class | Extract Class, Extract Subclass, Extract Superclass, Move Function to a new module |
| Long Function | Extract Function, Decompose Conditional, Replace Temp with Query, Replace Loop with Pipeline, Replace Function with Command |
| Long Parameter List, Data Clumps | Introduce Parameter Object, Preserve Whole Object, Replace Parameter with Query |
| Shotgun Surgery, Insider Trading | Move Function, Move Field, Combine Functions into Class: collect related items in one place |
| Comments | Extract Function (with a name that replaces the comment), Introduce Assertion |
| Duplicated Code | Extract Function, Extract Class, Pull Up Method, Form Template Method |
| Repeated Switches | Replace Conditional with Polymorphism, Replace Type Code with Subclasses |

Most of these are automated by IDEs (rename, extract, inline, move), which perform them correctly across a whole code base.

### 10.7.2. A Worked Example

The function `shipping_cost` of 10.6.2 has a long function body, magic numbers, and a rule (free shipping) that is stated last although it overrides everything before it. Before changing it, we pin down its behavior with a parameterized test that covers each decision:

```python
from dataclasses import dataclass, field

import pytest

from shipping import shipping_cost


@dataclass
class Item:
    fragile: bool = False


@dataclass
class Order:
    weight: float
    country: str = "CN"
    express: bool = False
    total: float = 50
    items: list = field(default_factory=list)


@pytest.mark.parametrize(
    ("order", "expected"),
    [
        (Order(weight=1), 5.0),
        (Order(weight=5), 8.0),
        (Order(weight=7), 11.0),
        (Order(weight=1, express=True), 10.0),
        (Order(weight=1, country="JP"), 25.0),
        (Order(weight=1, country="US"), 50.0),
        (Order(weight=1, items=[Item(fragile=True), Item()]), 8.0),
        (Order(weight=1, total=199), 0.0),
        (Order(weight=1, total=199, express=True), 10.0),
    ],
)
def test_shipping_cost(order, expected):
    assert shipping_cost(order) == pytest.approx(expected)
```

```text
$ pytest -q test_shipping.py
.........                                                                [100%]
9 passed in 0.01s
```

Then we apply, one at a time and running the tests after each, Replace Magic Literal (named constants), Extract Function for each rule, Decompose Conditional, Replace Loop with Pipeline (the fragile-item loop becomes a `sum`), and finally Slide Statements to move the free-shipping rule to the front as a guard clause, which is behavior-preserving because the rule overrode every earlier result:

```python
FREE_SHIPPING_THRESHOLD = 199
EXPRESS_FACTOR = 2
FRAGILE_SURCHARGE = 3
NEARBY_COUNTRIES = {"JP": 20, "KR": 20}
OTHER_COUNTRY_SURCHARGE = 45


def shipping_cost(order):
    if qualifies_for_free_shipping(order):
        return 0.0
    cost = base_cost(order.weight)
    if order.express:
        cost *= EXPRESS_FACTOR
    cost += international_surcharge(order.country)
    cost += handling_surcharge(order.items)
    return cost


def qualifies_for_free_shipping(order):
    return order.total >= FREE_SHIPPING_THRESHOLD and not order.express


def base_cost(weight):
    if weight <= 1:
        return 5.0
    if weight <= 5:
        return 8.0
    return 8.0 + (weight - 5) * 1.5


def international_surcharge(country):
    if country == "CN":
        return 0
    return NEARBY_COUNTRIES.get(country, OTHER_COUNTRY_SURCHARGE)


def handling_surcharge(items):
    return FRAGILE_SURCHARGE * sum(1 for item in items if item.fragile)
```

```text
$ pytest -q test_shipping.py
.........                                                                [100%]
9 passed in 0.01s
$ radon cc -s shipping.py
shipping.py
    F 8:0 shipping_cost - A (3)
    F 21:0 base_cost - A (3)
    F 35:0 handling_surcharge - A (3)
    F 17:0 qualifies_for_free_shipping - A (2)
    F 29:0 international_surcharge - A (2)
```

The behavior is unchanged, as the same nine tests confirm. The total complexity is about the same, since the decisions are inherent in the business rules, but it is now spread over five functions, each of which can be read, named, tested and changed on its own; `shipping_cost` itself reads as a summary of the pricing policy, and a change to the surcharges for one country touches only a table.

## 10.8. From Code Smells to Design Smells

### 10.8.1. Design Patterns and Antipatterns

The ideas of 10.6 and 10.7 apply within a function or a class. At the level of the relationships between classes, the corresponding notions are design smells and design patterns. The architect Christopher Alexander described a pattern as a problem that occurs over and over again, together with the core of a tried solution to it; his book *A Pattern Language* (1977) contains 253 patterns of building and planning, from the distribution of towns to the details of a roof, organized into a *pattern language* in which larger patterns are completed by smaller ones. The 23 **design patterns** of the "Gang of Four" (Gamma, Helm, Johnson and Vlissides, 1994) carry the idea to object-oriented software, in three categories ([4.2.13](/4.2.13)):

| Creational | Structural | Behavioral |
|---|---|---|
| Factory Method, Abstract Factory, Builder, Prototype, Singleton | Adapter, Bridge, Composite, Decorator, Facade, Flyweight, Proxy | Chain of Responsibility, Command, Interpreter, Iterator, Mediator, Memento, Observer, State, Strategy, Template Method, Visitor |

A pattern describes communicating objects and classes that solve a general design problem in a particular context; it captures a common and successful solution to a category of related problems and is customized for each concrete one. A pattern is neither a class or library (such as a list or a hash table) nor a complete design: it is closer to a blueprint for part of a design. Patterns are a reuse of design rather than of code, and their common theme is to separate what changes from what stays the same: program to an interface, not an implementation; prefer **composition** over **inheritance**; delegate.

An *antipattern* is the opposite: a commonly occurring structure that looks like a solution but has more bad consequences than good ones, such as a God class that knows and does everything, or code that clearly ought to follow some pattern but does not. Antipatterns are often the result of accumulated *technical debt*: the future cost of rework that a team incurs by choosing an expedient solution now instead of a better one that would take longer. Like financial debt, technical debt is sometimes worth taking on deliberately, to meet a deadline; it then accrues interest, in the form of slower and riskier changes, until it is repaid by refactoring.

The two levels compare as follows:

| | Methods within a class | Relationships among classes |
|---|---|---|
| Bad signs | code smells | design smells |
| Catalogs | code smells and refactorings | design smells and design patterns |
| Metrics | ABC score, cyclomatic complexity | lack of cohesion of methods (LCOM), coupling between objects |
| Typical refactorings | extract functions, move code within a class | extract classes, move code between classes |
| Guidelines | SOFA: methods are Short, do One thing, have Few arguments, stay at a single level of Abstraction | SOLID principles |

### 10.8.2. The SOLID Principles

The SOLID principles, collected by Robert C. Martin around 2000 and named by Michael Feathers, aim to minimize the cost of change in object-oriented designs. They were introduced with the patterns in [4.2.13](/4.2.13); here we look at each from the maintenance side: the symptom that reveals a violation and the refactorings or patterns that repair it.

| Principle | Statement | Symptom of violation | Remedies |
|---|---|---|---|
| **Single-responsibility principle** | a class has one and only one reason to change | a very large class; several unrelated groups of methods; one cannot state its responsibility in 25 words | Extract Class |
| **Open–closed principle** | adding functionality should require adding code, not modifying existing code | `switch` or `if` chains on the type of an object or on a property that never changes after creation | Replace Conditional with Polymorphism; Strategy, Template Method, Decorator, Abstract Factory |
| **Liskov substitution principle** | an instance of a subtype can always be substituted for an instance of its supertype | Refused Bequest: a subclass has no meaningful way to implement an inherited operation | replace inheritance by composition and explicit delegation |
| **Interface segregation principle** | clients should not depend on methods they do not use | "fat" interfaces whose implementers leave many methods empty or raising errors | split the interface into role interfaces |
| **Dependency inversion principle** | high-level modules depend on abstractions, not on low-level modules | one cannot add a variant of a dependency, or test a class in isolation, without modifying it | introduce an interface between the two; inject the dependency; Adapter |

A model with many sets of behaviors is the typical violator of single responsibility: a `User` class that is at once a customer, an authentication principal and a member of a social network has three axes of change. A metric detects such classes. In LCOM4 (Hitz and Montazeri, 1995), the methods of a class are the vertices of a graph, and two methods are joined by an edge if one calls the other or both use the same field; LCOM4 is the number of connected components of this graph. A cohesive class has LCOM4 $= 1$; a value of 2 or more suggests that the class consists of several "cliques" of methods that could be separate classes (Extract Class).

The dependency inversion principle is usually realized by *dependency injection*: a class receives the objects it depends on, through its constructor or parameters, instead of creating them itself. This one change makes the class both extensible and testable:

```python
from datetime import datetime
from typing import Protocol


class Clock(Protocol):
    def now(self) -> datetime: ...


class Mailer(Protocol):
    def send(self, to: str, body: str) -> None: ...


class DailyReport:
    def __init__(self, clock: Clock, mailer: Mailer) -> None:
        self.clock = clock          # injected: a real clock in production,
        self.mailer = mailer        # a fixed clock and a fake mailer in tests

    def send_to(self, manager: str) -> None:
        today = self.clock.now().date()
        self.mailer.send(manager, f"Sales report for {today}")
```

`DailyReport` depends only on the two protocols; the tests of [4.14.12](/4.14.12) pass it test doubles. Some courses, following Fox and Patterson's *Engineering Software as a Service*, read the I of SOLID as "injection of dependencies" and the D as "Demeter"; in the standard formulation these are the dependency inversion principle and an independent principle, the **law of Demeter**. It says: talk to your friends (the object's own fields, its parameters and the objects it creates), not to strangers reached through them. Its typical symptom is a message chain such as `order.customer.address.city.postal_code`, which couples the caller to the whole navigation path and, in tests, forces the construction of a chain of mock objects (a "mock train wreck"). The remedy is to delegate the behavior to the object that has the data (`order.shipping_postal_code()`), or to use the Visitor pattern to separate a traversal from the computation, or the Observer pattern to be notified of relevant events instead of reaching for them.

Patterns and principles are tools, not goals. Introducing abstractions for changes that have not happened makes code more complex (Speculative Generality); the usual advice is to write the simplest code that works and refactor toward a pattern when the change it supports actually arrives.

## 10.9. Code Quality When Agents Write Code

When a **coding agent** ([4.2.14](/4.2.14)) writes much of the code, the readers of code change, but the need for readable code does not: people still review every change and own the system, and the agent itself is a reader, which understands a code base through its names, structure and comments. Clear names and small functions help agents as much as people, and a misleading name misleads both. Three practices of this chapter become more important.

- Make the conventions executable. A rule that exists only in a style document is applied inconsistently by people and unreliably by agents; a rule in the formatter, linter and type checker configuration is applied every time. A pre-commit hook and a CI quality gate that run `ruff format --check`, `ruff check` and a type checker turn the coding standard into a check that the agent can run after each change and fix by itself, before anyone reviews it.
- Watch for the smells that agents tend to produce. Generated code often duplicates an existing helper instead of finding it, adds defensive checks and comments that repeat the code, catches exceptions broadly to make an error disappear, and adds speculative options that nobody asked for. Duplicate-code detectors, complexity limits and rules against bare `except` catch part of this; the rest is found in review, which should read the diff and not only the agent's summary.
- Refactor under tests, in small steps. Agents are good at mechanical refactorings across many files, and they also make plausible-looking changes that alter behavior. The safeguard is the one of 10.7: characterization tests first, one refactoring per commit, all tests after each step, and an explicit instruction not to change the tests while refactoring.

The project instructions an agent reads (10.2.3's coding standard, the naming conventions, the commands that check them) are themselves documentation that must be kept true; [4.14.14](/4.14.14) discusses how to write and maintain them.

## Summary

- Defensive programming assumes nothing: it validates external data and parameters at module boundaries, reports bad input with clear errors, uses assertions only for internal assumptions, and makes invalid states unrepresentable where possible.
- Code is written for people. Layout should be consistent, conventional and concise; adopt a standard (PEP 8, a Google style guide, MISRA for safety-critical C) and enforce its layout with a formatter.
- Names are descriptive, correct, idiomatic and appropriate; avoid cryptic, verbose, misleading and vague names, and follow the case conventions of the language.
- Self-documenting code makes the normal path obvious, avoids deep nesting, uses small functions, descriptive types and named constants. Comments explain why, not how, and document the unexpected.
- Code smells signal design problems; cyclomatic complexity ($V = E - N + 2$ = decisions $+1$, at most about 10) and the ABC score quantify complexity; linters and type checkers find defects without running the code.
- Refactoring changes structure without changing behavior, in small steps verified by tests; each smell has standard refactorings.
- At the level of classes, design smells are repaired with design patterns and the SOLID principles; dependency injection makes classes extensible and testable, and the law of Demeter avoids message chains.
