---
title: Strings, Streams and Regular Expressions
description: Common operations of std::string, string_view and UTF-8; the hierarchy of input and output streams, stream operators, manipulators and std::format (and std::print in C++23); file streams and string streams; the syntax of regular expressions and matching, searching and replacing; Python's str, f-strings, files and the re module.
source_hash: 451f0876e5c1
---

A large part of the data that programs process is text: configuration files, logs, user input, web pages. This chapter covers three tools C++ offers for handling text: the variable-length string `std::string`; streams, which read data in and write data out, together with the new-style formatting `std::format` and `std::print` brought by C++20/23; and regular expressions, which describe a "class of strings" by a short pattern. C-style strings and character arrays were discussed in [4.1.7](/4.1.7), and the internal structure of `std::string` is similar to that of the `vector` of Chapter 10; string-matching algorithms (KMP and others) are in [4.3.13](/4.3.13), and the formal definition of regular expressions and finite automata are in [4.8 Formal Languages and Automata](/4.8).

## 11.1. std::string

### 11.1.1. Common Operations

`std::string` is a dynamic array of `char` that manages its own memory and can be copied, compared and concatenated with `+` like a built-in type. Most implementations also have the "small string optimization": strings of up to a dozen or so characters are stored directly inside the object, without heap allocation.

```cpp tab
#include <format>
#include <iostream>
#include <string>

int main() {
    std::string s = "Hello, World";
    std::cout << std::format("{} [{}]\n", s.size(), s.substr(7, 5));    // substr(pos, count)

    if (auto pos = s.find("World"); pos != std::string::npos)
        s.replace(pos, 5, "C++");                          // replace(pos, count, str)
    s += "!";
    std::cout << std::format("{}\n", s);
    std::cout << std::format("{} {} {}\n", s.starts_with("Hello"), s.contains("C++"),
                 s.find('z') == std::string::npos);

    int n = std::stoi("42");                               // string -> number
    double d = std::stod("2.5");
    std::string t = std::to_string(n * d);                 // number -> string
    std::cout << std::format("{}\n", t);
}
```

```python tab
s = "Hello, World"
print(len(s), f"[{s[7:12]}]")                  # slicing

if (pos := s.find("World")) != -1:
    s = s[:pos] + "C++" + s[pos + 5:]          # str is immutable: build a new one
s += "!"
print(s)
print(s.startswith("Hello"), "C++" in s, s.find("z") == -1)

n = int("42")
d = float("2.5")
t = str(n * d)
print(t)
```

| Operation | C++ `std::string` | Python `str` |
|---|---|---|
| Length | `s.size()` | `len(s)` |
| Substring | `s.substr(pos, count)` | `s[pos:pos + count]` |
| Search | `s.find(x)`, returns `std::string::npos` if not found | `s.find(x)`, returns `-1` if not found; `x in s` |
| Prefix, suffix | `starts_with`, `ends_with` (C++20) | `startswith`, `endswith` |
| Modification | `replace`, `insert`, `erase`, `+=`, modifying in place | Immutable; `replace` and others return new strings |
| Conversion to and from numbers | `std::stoi`, `std::stod`, `std::to_string`, `std::from_chars` | `int(s)`, `float(s)`, `str(x)` |

### 11.1.2. string_view and Character Encoding

The C++17 `std::string_view` is a read-only "view" of a sequence of characters: it stores only a starting pointer and a length, does not own the characters, and copying it does not copy the characters. When a function only needs to read a string, declaring the parameter as `std::string_view` accepts `std::string`, string literals and character arrays alike, without making a copy. The price is that, like an **iterator**, it can dangle: once the string a `string_view` refers to is destroyed or modified, the view becomes invalid, so one should not use it to store data or return it from a function pointing into a local string.

`std::string` stores bytes and knows nothing about character encoding. Nearly all text today is encoded in UTF-8, in which a non-ASCII character occupies 2 to 4 bytes, so `size()` returns the number of bytes, not characters: `std::string("café").size()` is 5, whereas Python's `len("café")` is 4, because a Python `str` is a sequence of Unicode code points. A byte sequence is a different type, `bytes`, and the two are converted into each other with `encode` and `decode` using a specified encoding. The support of the C++ standard library for Unicode text is still limited, and processing multilingual text by "characters" usually requires a dedicated library.

## 11.2. Streams

### 11.2.1. The Stream Hierarchy and Stream Operators

C++ input and output are built on *streams*: a stream is an abstraction of a sequence of bytes, and the program just writes into it or reads from it without caring whether the other end is a terminal, a file or a string in memory.

| Class | Direction | The other end | Header |
|---|---|---|---|
| `istream`, `ostream`, `iostream` | Input, output, both | Abstract | `<iostream>` |
| `ifstream`, `ofstream`, `fstream` | Same | A file | `<fstream>` |
| `istringstream`, `ostringstream`, `stringstream` | Same | A `std::string` | `<sstream>` |

File streams and string streams derive from `istream` or `ostream` (`iostream` inherits from both, see the **virtual inheritance** of [4.2.7](/4.2.7)), so a function that takes a `std::ostream&` can write to the terminal, to a file and to a string alike; this is exactly the subtype polymorphism of Chapter 8. The standard objects `std::cin`, `std::cout` and `std::cerr` are connected to standard input, standard output and standard error, respectively.

Once `operator<<` is overloaded for a user-defined type (**operator overloading**, [4.2.5](/4.2.5)), the type can be written to any output stream. The function returns a reference to the stream so that `os << a << b` can be chained. Stream objects cannot be copied (the copy constructor is deleted, since copying a "channel connected to a terminal" makes no sense), so they are always passed by reference.

### 11.2.2. Formatted Output

The traditional `<iostream>` controls formatting with manipulators: `std::setw(n)` sets the width of the next item, `std::fixed` and `std::setprecision(n)` set the number of decimal places, and `std::hex` switches to hexadecimal. Except for `setw`, their effects persist and easily affect later output. `std::endl` outputs a newline and flushes the buffer; frequent flushing can slow down programs with large output considerably, and `'\n'` is generally enough.

The C++20 `std::format` uses the same format specification language as Python: `{}` is a placeholder, and after the colon comes the format specification `[[fill]align][width][.precision][type]`. It returns a formatted `std::string`, which is then passed to `std::cout`. Compared with a chain of `<<` and manipulators, it is type safe (a mismatch between format and argument types is a compile-time error), faster and more readable, and does not change the state of the stream, so it is the recommended formatting method in modern C++. C++23 further provides `std::print` and `std::println` (header `<print>`), which combine formatting and output in one step: `std::println("{:.2f}", x)` is equivalent to `std::cout << std::format("{:.2f}\n", x)`. `<print>` is available only from GCC 14; so that the code also compiles with GCC 13, which is still widely used (for example the default compiler of Ubuntu 24.04), the examples in this book are uniformly written as `std::cout << std::format(…)`.

```cpp
#include <format>
#include <iomanip>
#include <iostream>
#include <string>

struct Point { double x, y; };

std::ostream& operator<<(std::ostream& os, const Point& p) {   // for streams
    return os << '(' << p.x << ", " << p.y << ')';
}

template <>
struct std::formatter<Point> {                                  // for std::format/print
    constexpr auto parse(std::format_parse_context& ctx) { return ctx.begin(); }
    auto format(const Point& p, std::format_context& ctx) const {
        return std::format_to(ctx.out(), "({}, {})", p.x, p.y);
    }
};

int main() {
    std::cout << std::setw(8) << std::fixed << std::setprecision(2) << 3.14159
              << '|' << std::hex << 255 << '|' << Point{1, 2} << '\n';

    std::cout << std::format("{:>8.2f}|{:x}|{:08b}|{:<5}|{:^7}|\n", 3.14159, 255, 5, "ab", "mid");
    std::cout << std::format("{1} {0} {1}\n", "a", "b");  // explicit argument index
    std::string s = std::format("{}", Point{1.5, -2});
    std::cout << std::format("{} has {} chars\n", s, s.size());
}
```

```text
    3.14|ff|(1.00, 2.00)
    3.14|ff|00000101|ab   |  mid  |
b a b
(1.5, -2) has 9 chars
```

Note that in the first line the coordinates of `Point` are also printed as `1.00`: the `std::fixed` and `setprecision(2)` set earlier are still in effect, a surprise brought by the "sticky" state of streams.

### 11.2.3. File Streams

A file stream object opens the file on construction and closes it automatically on destruction, a typical application of **resource acquisition is initialization** (RAII; [4.2.4](/4.2.4)). A failed open does not throw an exception but leaves the stream in a failed state, which should be checked. When reading, the read operation itself serves as the loop condition: `while (std::getline(in, line))` and `while (in >> word)` become false at the end of the file or on a format error, and the loop ends.

```cpp tab
#include <format>
#include <fstream>
#include <iostream>
#include <map>
#include <sstream>
#include <string>

int main() {
    {
        std::ofstream out("notes.txt");
        if (!out) {
            std::cerr << "cannot open notes.txt\n";
            return 1;
        }
        out << "the quick brown fox\njumps over the lazy dog\nthe end\n";
    }                                            // out is closed here (RAII)

    std::ifstream in("notes.txt");
    std::map<std::string, int> freq;
    std::string line;
    int lines = 0;
    while (std::getline(in, line)) {             // false at end of file
        ++lines;
        std::istringstream words(line);          // split the line into words
        std::string w;
        while (words >> w) ++freq[w];
    }
    std::cout << std::format("{} lines, 'the' x {}\n", lines, freq["the"]);
}
```

```python tab
from collections import Counter

with open("notes.txt", "w", encoding="utf-8") as out:
    out.write("the quick brown fox\njumps over the lazy dog\nthe end\n")
# the file is closed when the with block ends

freq: Counter[str] = Counter()
lines = 0
with open("notes.txt", encoding="utf-8") as f:
    for line in f:                               # a file object iterates over lines
        lines += 1
        freq.update(line.split())
print(f"{lines} lines, 'the' x {freq['the']}")
```

```text
3 lines, 'the' x 3
```

For binary reading and writing, open with `std::ios::binary` and use `read` and `write` to transfer bytes. The word-frequency part of the example above (reading line by line, splitting, counting) is the standard-library version of the stepwise-refinement example of [4.1.9](/4.1.9).

### 11.2.4. String Streams

A string stream treats a `std::string` as the other end of the stream: `istringstream` reads formatted data from a string (the example above uses it to split a line into words), and `ostringstream` writes values formatted into a string, which is finally retrieved with `str()`. With it one can write a generic type-conversion function template; in modern C++, conversion between numbers and strings is better done with `std::format` and the C++17 `std::from_chars`, which allocates no memory, is unaffected by the locale, and reports errors explicitly.

```cpp
#include <charconv>
#include <format>
#include <iostream>
#include <sstream>
#include <string>
#include <system_error>

template <typename To, typename From>
To convert(const From& x) {                      // works for any streamable types
    std::stringstream ss;
    ss << x;
    To y{};
    ss >> y;
    return y;
}

int main() {
    std::cout << std::format("{} {}\n", convert<int>("123") + 1, convert<std::string>(3.5));

    const std::string text = "2048 apples";
    int value = 0;
    auto [ptr, ec] = std::from_chars(text.data(), text.data() + text.size(), value);
    if (ec == std::errc{})
        std::cout << std::format("parsed {}, rest: [{}]\n", value, std::string(ptr, text.data() + text.size()));
}
```

```text
124 3.5
parsed 2048, rest: [ apples]
```

C's `scanf` and `printf` can be mixed with C++ streams, but by default they must be synchronized with each other, which makes `cin` and `cout` slower than `scanf`; when only streams are used, calling `std::ios::sync_with_stdio(false)` at the start of the program removes this overhead.

## 11.3. Regular Expressions

### 11.3.1. Motivation and Syntax

Suppose that registering a user name requires that it contain only lowercase letters, digits and underscores, with a length of 3 to 15. Writing the check by hand needs a loop and a series of conditions, which must be rewritten whenever the rule changes. With a regular expression the rule is a single line, `^[a-z0-9_]{3,15}$`.

**Definition 11.3.1 (Regular Expression)** A pattern composed of ordinary characters and metacharacters with special meanings, used to describe a set of strings, is called a **regular expression**. A string matches a regular expression if it belongs to the set that the pattern describes.

In theory, a regular expression is built from single characters by three operations, concatenation, union (`|`) and closure (`*`), and the set it describes is exactly a regular language, which a finite automaton can recognize ([4.8](/4.8)). Practical regular expressions add many convenient notations on top of this:

| Notation | Meaning | Example |
|---|---|---|
| `abc` | Ordinary characters match themselves | `cat` matches cat |
| `.` | Any single character except newline | `c.t` matches cat, cut |
| `[abc]`, `[a-z]`, `[^0-9]` | Character class: one character from the set; `^` means complement | `[A-Za-z_]` |
| `\d`, `\w`, `\s` | Digit, word character (letter, digit, underscore), whitespace; the uppercase `\D`, `\W`, `\S` are complements | `\d\d` matches two digits |
| `^`, `$`, `\b` | Beginning, end, word boundary (consume no characters) | `^\d+$` the whole string is digits |
| `*`, `+`, `?` | Previous item repeated 0 or more, 1 or more, 0 or 1 times | `colou?r` |
| `{m}`, `{m,n}`, `{m,}` | Repeated exactly m times, m to n times, at least m times | `\d{4}` |
| `*?`, `+?` | Non-greedy: repeat as few times as possible | `<.+?>` matches just one tag |
| `x\|y` | Or | `cat\|dog` |
| `(…)` | Group and capture; can be back-referenced with `\1` | `(\w)\1` matches two identical consecutive characters |
| `(?:…)` | Group only, no capture | `(?:ab)+` |
| `\.`, `\\` | Escape metacharacters | `\d+\.\d+` matches a decimal |

Regular expressions contain many backslashes, which must be escaped once more in an ordinary string literal (`"\\d+"`). In the C++11 raw string literal `R"(\d+)"` and in Python's `r"\d+"`, backslashes are not escaped, and these should be used when writing regular expressions.

### 11.3.2. Matching, Searching and Replacing

A regular expression has three basic uses: matching (whether the whole string conforms to the pattern), searching (finding the substrings that conform to the pattern), and replacing (replacing the substrings that conform to the pattern with something else). The C++ `<regex>` and the Python `re` module correspond one to one:

| Use | C++ `<regex>` | Python `re` |
|---|---|---|
| Match the whole string | `std::regex_match` | `re.fullmatch` |
| Search for the first occurrence | `std::regex_search` | `re.search` |
| Iterate over all | `std::sregex_iterator` | `re.finditer`, `re.findall` |
| Replace | `std::regex_replace`, `$1` refers to a group | `re.sub`, `\1` or `\g<name>` refers to a group |
| Get a group | `std::smatch m; m[1].str()` | `m.group(1)`, `m[1]`, `m["name"]` |

```cpp tab
#include <format>
#include <iostream>
#include <regex>
#include <string>

int main() {
    const std::regex username(R"([a-z0-9_]{3,15})");  // regex_match checks the whole string
    for (std::string name : {"john_123", "John_123", "jo", "@john"})
        std::cout << std::format("{:<9} {}\n", name, std::regex_match(name, username));

    const std::string text = "q123e456w";
    const std::regex number(R"(\d+)");
    for (std::sregex_iterator it(text.begin(), text.end(), number), end; it != end; ++it)
        std::cout << std::format("{} ", it->str());  // search: all matches
    std::cout << '\n';
    std::cout << std::format("{}\n", std::regex_replace(text, number, "(number)"));

    const std::regex date(R"((\d{4})-(\d{2})-(\d{2}))");     // three capturing groups
    const std::string log = "released 2026-10-20, patched 2026-11-02";
    if (std::smatch m; std::regex_search(log, m, date))
        std::cout << std::format("year {}, month {}, day {}\n", m[1].str(), m[2].str(), m[3].str());
    std::cout << std::format("{}\n", std::regex_replace(log, date, "$3/$2/$1"));
}
```

```python tab
import re

username = re.compile(r"[a-z0-9_]{3,15}")                    # compile once, reuse
for name in ["john_123", "John_123", "jo", "@john"]:
    print(f"{name:<9} {username.fullmatch(name) is not None}")

text = "q123e456w"
print(*re.findall(r"\d+", text))                              # search: all matches
print(re.sub(r"\d+", "(number)", text))

date = re.compile(r"(?P<y>\d{4})-(?P<m>\d{2})-(?P<d>\d{2})")  # named groups
log = "released 2026-10-20, patched 2026-11-02"
if m := date.search(log):
    print(f"year {m['y']}, month {m['m']}, day {m['d']}")
print(date.sub(r"\g<d>/\g<m>/\g<y>", log))
```

```text
john_123  true
John_123  false
jo        false
@john     false
123 456
q(number)e(number)w
year 2026, month 10, day 20
released 20/10/2026, patched 02/11/2026
```

(The Python version prints `true` and `false` as `True` and `False`.) `regex_match` and `fullmatch` themselves require the whole string to match, so `^` and `$` need not be written in the pattern; when checking a format with `regex_search` or `re.search`, they must be written, otherwise the substring `john_123` in `"@john_123"` would also be found.

### 11.3.3. Practical Advice

- Compile first, then reuse: constructing a `std::regex` object compiles the pattern into an internal matcher, which is not cheap, so do not construct it repeatedly in a loop; Python's `re` caches recently used patterns, but an explicit `re.compile` is clearer.
- Mind performance: the `std::regex` of all mainstream implementations is rather slow and may become a bottleneck in bulk text processing. Mainstream regular-expression engines use backtracking, and patterns with nested repetition such as `(a+)+$` may take exponential time on non-matching input (catastrophic backtracking), so special care is needed with untrusted input.
- Know the limits: regular expressions can describe only regular languages and cannot match parentheses nested to arbitrary depth, so they should not be used to parse HTML, JSON or program source code; such tasks require dedicated parsers (the context-free grammars of [4.8](/4.8)).
- Readability: complex patterns are hard to read, and should be split into several parts, commented (Python's `re.VERBOSE` allows line breaks and comments inside a pattern), and covered by tests.

## 11.4. Python Comparison

### 11.4.1. str and bytes

Python's `str` is immutable: `s.replace(…)`, `s.upper()` and slicing all return new strings and leave the original unchanged. Accumulating a long string with `+=` in a loop can therefore degrade to quadratic complexity; instead, put the pieces in a list and join them once at the end with `"".join(parts)`. Common methods include `split`, `strip`, `join`, `startswith`, `partition` and `count`. When dealing with files and networks, one obtains bytes, `bytes`, which must be converted to `str` with `b.decode("utf-8")`.

### 11.4.2. f-strings and Formatting

The f-string `f"{x:>8.2f}"` uses the same format specification language as C++'s `std::format` (which was modeled on Python's). `f"{x=}"` prints both the expression and its value, which is convenient for debugging. The `__str__` of a user-defined class determines the output of `print` and `str()`, corresponding to overloading `operator<<` in C++; `__repr__` gives a programmer-oriented, as unambiguous as possible representation; `__format__` handles format specifications, corresponding to specializing `std::formatter`.

### 11.4.3. Files and io.StringIO

`with open(path, mode, encoding="utf-8") as f:` guarantees that the file is closed on leaving the `with` block, corresponding to the RAII of C++ file streams (the **context manager** of [4.2.4](/4.2.4)). In text mode one should always state the `encoding`; otherwise the default encoding of the platform is used, and results may differ between systems. A file object can be iterated line by line; `pathlib.Path` provides object-oriented path operations, and `Path("a.txt").read_text(encoding="utf-8")` reads a whole file at once. `io.StringIO` is a text file in memory, corresponding to C++'s `stringstream`.

### 11.4.4. The re Module

The `re` module was compared with C++ in §11.3.2. Besides the functions in the table, `re.split` splits a string by a pattern, the replacement argument of `re.sub` can be a function (called for each match and returning the replacement text), and the flags `re.IGNORECASE`, `re.MULTILINE` and `re.VERBOSE` ignore case, make `^` and `$` match at the beginning and end of each line, and allow whitespace and comments in the pattern, respectively.

## Summary

- `std::string` is a byte sequence that manages its own memory; use `std::string_view` for read-only parameters, noting that it may dangle; in UTF-8 text the number of bytes is not the number of characters.
- Streams abstract the sources and destinations of data into a uniform interface, with file streams and string streams as derived classes; overloading `operator<<` lets user-defined types be output.
- In new code, use `std::format` for formatted output (`std::print` directly in C++23) and `std::from_chars` to parse numbers.
- Regular expressions describe sets of strings and have three uses, matching, searching and replacing; write them with raw string literals, compile once and reuse, and do not use them to parse nested structures.
- Python's `str` is an immutable Unicode string, f-strings and `std::format` share the same format specification, `with open` corresponds to RAII, and `re` corresponds one to one with `<regex>`.
