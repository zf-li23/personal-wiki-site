---
title: 字符串、流与正则表达式
description: std::string 的常用操作、string_view 与 UTF-8；输入输出流的层次、流运算符、流操纵算子与 std::format（及 C++23 的 std::print）；文件流与字符串流；正则表达式的语法与匹配、搜索、替换；Python 的 str、f-string、文件与 re 模块。
---

程序处理的数据很大一部分是文本：配置文件、日志、用户输入、网页。本章讲 C++ 处理文本的三件工具：变长字符串 `std::string`；把各种数据读进来、写出去的流，以及 C++20/23 带来的新式格式化 `std::format` 与 `std::print`；用一个简短的模式描述"一类字符串"的正则表达式。C 风格字符串与字符数组已在 [4.1.7](/4.1.7) 讨论，`std::string` 的内部结构与第 10 章的 `vector` 相似；串匹配算法（KMP 等）见 [4.3.13](/4.3.13)，正则表达式的形式定义与有限自动机见 [4.8 形式语言与自动机](/4.8)。

## 11.1. std::string

### 11.1.1. 常用操作

`std::string` 是存放 `char` 的动态数组，自己管理内存，可以像内置类型一样复制、比较和用 `+` 连接。多数实现还有"短字符串优化"：十几个字符以内的字符串直接存放在对象内部，不分配堆内存。

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

| 操作 | C++ `std::string` | Python `str` |
|---|---|---|
| 长度 | `s.size()` | `len(s)` |
| 子串 | `s.substr(pos, count)` | `s[pos:pos + count]` |
| 查找 | `s.find(x)`，找不到返回 `std::string::npos` | `s.find(x)`，找不到返回 `-1`；`x in s` |
| 前缀、后缀 | `starts_with`、`ends_with`（C++20） | `startswith`、`endswith` |
| 修改 | `replace`、`insert`、`erase`、`+=`，原地修改 | 不可变，`replace` 等返回新字符串 |
| 与数值互转 | `std::stoi`、`std::stod`、`std::to_string`、`std::from_chars` | `int(s)`、`float(s)`、`str(x)` |

### 11.1.2. string_view 与字符编码

C++17 的 `std::string_view` 是对一段字符的只读"视图"：只保存起始指针和长度，不拥有字符，复制它不复制字符。函数只需要读字符串时，参数写成 `std::string_view` 可以同时接受 `std::string`、字符串字面量和字符数组，且不产生复制。代价是它和**迭代器**一样可能悬垂：`string_view` 所指的字符串被销毁或修改后，视图就失效了，因此不要用它保存数据或作为函数返回值指向局部字符串。

`std::string` 存放的是字节，不知道字符编码。今天的文本几乎都用 UTF-8 编码，一个非 ASCII 字符占 2–4 个字节，所以 `size()` 返回的是字节数而不是字符数：`std::string("café").size()` 是 5，而 Python 的 `len("café")` 是 4，因为 Python 的 `str` 是 Unicode 码位的序列，字节序列是另一个类型 `bytes`，二者用 `encode` 与 `decode` 按指定的编码互相转换。C++ 标准库对 Unicode 文本的支持仍然有限，按"字符"处理多语言文本时通常需要专门的库。

## 11.2. 流

### 11.2.1. 流的层次与流运算符

C++ 的输入输出建立在流（stream）之上：流是字节序列的抽象，程序只管往里写或从中读，不关心另一端是终端、文件还是内存中的字符串。

| 类 | 方向 | 另一端 | 头文件 |
|---|---|---|---|
| `istream`、`ostream`、`iostream` | 输入、输出、双向 | 抽象 | `<iostream>` |
| `ifstream`、`ofstream`、`fstream` | 同上 | 文件 | `<fstream>` |
| `istringstream`、`ostringstream`、`stringstream` | 同上 | `std::string` | `<sstream>` |

文件流和字符串流都派生自 `istream` 或 `ostream`（`iostream` 同时继承二者，见 [4.2.7](/4.2.7) 的**虚继承**），所以一个接受 `std::ostream&` 的函数既能写终端，也能写文件和字符串，这正是第 8 章的子类型多态。标准对象 `std::cin`、`std::cout`、`std::cerr` 分别连接标准输入、标准输出和标准错误。

为自定义类型重载 `operator<<`（**运算符重载**，[4.2.5](/4.2.5)）后，它就能输出到任何输出流。函数返回流的引用，使 `os << a << b` 可以连写；流对象不能复制（拷贝构造函数被删除，复制一个"连接到终端的通道"没有意义），所以总是按引用传递。

### 11.2.2. 格式化输出

传统的 `<iostream>` 用流操纵算子（manipulator）控制格式：`std::setw(n)` 设置下一项的宽度，`std::fixed` 与 `std::setprecision(n)` 设置小数位数，`std::hex` 改为十六进制。除 `setw` 外，它们的效果会一直保持，容易影响后面的输出。`std::endl` 输出换行并刷新缓冲区，频繁刷新会显著拖慢大量输出的程序，一般写 `'\n'` 即可。

C++20 的 `std::format` 采用了与 Python 相同的格式说明语言：`{}` 是占位符，冒号后是格式说明 `[[填充]对齐][宽度][.精度][类型]`。它返回格式化好的 `std::string`，再交给 `std::cout` 输出。与一连串 `<<` 和流操纵算子相比，它类型安全（格式与参数类型不匹配时编译报错）、更快、更易读，也不会改变流的状态，是现代 C++ 推荐的格式化方式。C++23 进一步提供了 `std::print` 与 `std::println`（头文件 `<print>`），把格式化与输出合为一步：`std::println("{:.2f}", x)` 相当于 `std::cout << std::format("{:.2f}\n", x)`。`<print>` 从 GCC 14 起才提供，为了让代码在仍然广泛使用的 GCC 13（如 Ubuntu 24.04 的默认编译器）上也能编译，本站的示例统一写成 `std::cout << std::format(…)`。

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

注意第一行中 `Point` 的坐标也被印成了 `1.00`：前面设置的 `std::fixed` 与 `setprecision(2)` 仍然有效，这就是流状态"粘滞"带来的意外。

### 11.2.3. 文件流

文件流对象在构造时打开文件，析构时自动关闭，这是 **RAII**（[4.2.4](/4.2.4)）的典型应用。打开失败不会抛出异常，而是让流处于失败状态，应当检查。读取时把读操作本身作为循环条件：`while (std::getline(in, line))`、`while (in >> word)` 在读到文件末尾或格式错误时为假，循环结束。

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

以二进制方式读写时用 `std::ios::binary` 打开，并用 `read`、`write` 按字节读写。上例中统计词频的部分（逐行读取、拆分、计数）是 [4.1.9](/4.1.9) 逐步求精例子的标准库写法。

### 11.2.4. 字符串流

字符串流把一个 `std::string` 当作流的另一端：`istringstream` 从字符串中按格式读取（上例用它把一行拆成单词），`ostringstream` 把各种值格式化地写进字符串，最后用 `str()` 取出。借助它可以写出一个通用的类型转换函数模板；现代 C++ 中，数值与字符串的互转更推荐用 `std::format` 和 C++17 的 `std::from_chars`：后者不分配内存、不受区域设置影响，并明确报告错误。

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

C 的 `scanf`、`printf` 与 C++ 的流可以混用，但默认要相互同步，这使 `cin`、`cout` 比 `scanf` 慢；只用流时，在程序开头调用 `std::ios::sync_with_stdio(false)` 可以去掉这一开销。

## 11.3. 正则表达式

### 11.3.1. 动机与语法

注册用户名时要求：只能包含小写字母、数字和下划线，长度 3 到 15。手写检查需要一个循环和一串条件，规则一改就要重写。用正则表达式，这条规则就是一行 `^[a-z0-9_]{3,15}$`。

**定义 11.3.1（正则表达式）** 由普通字符和具有特殊含义的元字符组成、用来描述一个字符串集合的模式，称为**正则表达式**（regular expression）。一个字符串与正则表达式匹配，指它属于该模式描述的集合。

从理论上看，正则表达式由单个字符经过连接、并（`|`）和闭包（`*`）三种运算构造，它描述的集合恰好是有限自动机能识别的正则语言（[4.8](/4.8)）。实用的正则表达式在此之上加了许多便利写法：

| 写法 | 含义 | 例子 |
|---|---|---|
| `abc` | 普通字符匹配自身 | `cat` 匹配 cat |
| `.` | 除换行外的任意一个字符 | `c.t` 匹配 cat、cut |
| `[abc]`、`[a-z]`、`[^0-9]` | 字符类：集合中的一个字符；`^` 表示取补 | `[A-Za-z_]` |
| `\d`、`\w`、`\s` | 数字、单词字符（字母数字下划线）、空白；大写 `\D`、`\W`、`\S` 取补 | `\d\d` 匹配两位数字 |
| `^`、`$`、`\b` | 开头、结尾、单词边界（不消耗字符） | `^\d+$` 整个串都是数字 |
| `*`、`+`、`?` | 前一项重复 0 次以上、1 次以上、0 或 1 次 | `colou?r` |
| `{m}`、`{m,n}`、`{m,}` | 重复恰好 m 次、m 到 n 次、至少 m 次 | `\d{4}` |
| `*?`、`+?` | 非贪婪：尽量少地重复 | `<.+?>` 只匹配一个标签 |
| `x\|y` | 或 | `cat\|dog` |
| `(…)` | 分组并捕获，可用 `\1` 反向引用 | `(\w)\1` 匹配连续两个相同字符 |
| `(?:…)` | 只分组、不捕获 | `(?:ab)+` |
| `\.`、`\\` | 转义元字符 | `\d+\.\d+` 匹配小数 |

正则表达式中有大量反斜杠，写在普通字符串字面量中要再转义一次（`"\\d+"`）。C++11 的原生字符串字面量 `R"(\d+)"` 与 Python 的 `r"\d+"` 中反斜杠不转义，写正则表达式时应当使用。

### 11.3.2. 匹配、搜索与替换

正则表达式有三种基本用法：匹配（整个字符串是否符合模式）、搜索（找出符合模式的子串）、替换（把符合模式的子串换成别的内容）。C++ 的 `<regex>` 与 Python 的 `re` 模块一一对应：

| 用法 | C++ `<regex>` | Python `re` |
|---|---|---|
| 匹配整个串 | `std::regex_match` | `re.fullmatch` |
| 搜索第一处 | `std::regex_search` | `re.search` |
| 遍历全部 | `std::sregex_iterator` | `re.finditer`、`re.findall` |
| 替换 | `std::regex_replace`，`$1` 引用分组 | `re.sub`，`\1` 或 `\g<name>` 引用分组 |
| 取分组 | `std::smatch m; m[1].str()` | `m.group(1)`、`m[1]`、`m["name"]` |

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

（Python 版把 `true`、`false` 印成 `True`、`False`。）`regex_match` 与 `fullmatch` 本身就要求匹配整个字符串，所以模式中不必再写 `^` 和 `$`；用 `regex_search` 或 `re.search` 检查格式时则必须写上，否则 `"@john_123"` 中的子串 `john_123` 也会被找到。

### 11.3.3. 使用建议

- 先编译、再复用：构造 `std::regex` 对象要把模式编译成内部的匹配器，代价不小，不要在循环里反复构造；Python 的 `re` 会缓存最近用过的模式，但显式 `re.compile` 更清楚。
- 注意性能：各主流实现的 `std::regex` 都比较慢，大量文本处理时可能成为瓶颈。主流的正则引擎采用回溯算法，`(a+)+$` 这类嵌套重复的模式在不匹配的输入上可能耗费指数时间（灾难性回溯），对不可信的输入要格外小心。
- 知道边界：正则表达式只能描述正则语言，不能匹配任意深度嵌套的括号，因此不应用它解析 HTML、JSON 或程序源代码，这些任务要用专门的解析器（[4.8](/4.8) 的上下文无关文法）。
- 可读性：复杂的模式难以阅读，应当拆成几段、加注释（Python 的 `re.VERBOSE` 允许在模式中换行和写注释），并为它写测试。

## 11.4. Python 对照

### 11.4.1. str 与 bytes

Python 的 `str` 不可变：`s.replace(…)`、`s.upper()`、切片都返回新字符串，原字符串不变；因此在循环中用 `+=` 累积长字符串可能退化为平方复杂度，应把片段放进列表，最后用 `"".join(parts)` 一次连接。常用方法有 `split`、`strip`、`join`、`startswith`、`partition`、`count`。与文件、网络打交道时得到的是字节 `bytes`，要用 `b.decode("utf-8")` 转成 `str`。

### 11.4.2. f-string 与格式化

f-string `f"{x:>8.2f}"` 与 C++ 的 `std::format` 用同一套格式说明语言（后者正是参照 Python 设计的）。`f"{x=}"` 会同时印出表达式和值，便于调试。自定义类的 `__str__` 决定 `print` 和 `str()` 的输出，相当于 C++ 中重载 `operator<<`；`__repr__` 给出面向程序员、尽量无歧义的表示；`__format__` 处理格式说明，相当于特化 `std::formatter`。

### 11.4.3. 文件与 io.StringIO

`with open(path, mode, encoding="utf-8") as f:` 保证文件在离开 `with` 块时关闭，对应 C++ 文件流的 RAII（[4.2.4](/4.2.4) 的**上下文管理器**）。文本模式应当总是写明 `encoding`，否则使用平台的默认编码，在不同系统上结果可能不同。文件对象可以逐行迭代；`pathlib.Path` 提供面向对象的路径操作，`Path("a.txt").read_text(encoding="utf-8")` 一次读入整个文件。`io.StringIO` 是内存中的文本文件，对应 C++ 的 `stringstream`。

### 11.4.4. re 模块

`re` 模块已在 §11.3.2 与 C++ 对照。除表中的函数外，`re.split` 按模式拆分字符串，`re.sub` 的替换参数可以是一个函数（对每个匹配调用，返回替换文本），标志 `re.IGNORECASE`、`re.MULTILINE`、`re.VERBOSE` 分别忽略大小写、让 `^`、`$` 匹配每一行的首尾、允许在模式中写空白与注释。

## 小结

- `std::string` 是自管理内存的字节序列；只读参数用 `std::string_view`，注意它可能悬垂；UTF-8 文本中字节数不等于字符数。
- 流把数据的来源与去向抽象成统一的接口，文件流与字符串流都是它的派生类；重载 `operator<<` 让自定义类型可以输出。
- 新代码用 `std::format` 格式化输出（C++23 可直接用 `std::print`），用 `std::from_chars` 解析数值。
- 正则表达式描述字符串的集合，有匹配、搜索、替换三种用法；用原生字符串字面量书写，编译一次反复使用，不用它解析嵌套结构。
- Python 的 `str` 是不可变的 Unicode 字符串，f-string 与 `std::format` 格式说明相同，`with open` 对应 RAII，`re` 与 `<regex>` 一一对应。
