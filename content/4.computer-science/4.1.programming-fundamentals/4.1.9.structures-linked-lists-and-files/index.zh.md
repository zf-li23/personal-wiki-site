---
title: 结构体、链表与文件
description: 用结构体把相关数据打包、结构体数组与平行数组；用指针把结构体串成链表，单链表与循环链表的建立、遍历与删除，约瑟夫问题；文本文件与二进制文件、文件流的读写与常见陷阱；以词频统计为例的逐步求精。
---

到目前为止，程序处理的数据要么是单个变量，要么是同类元素组成的数组，而且程序一结束数据就消失了。本章解决两个问题。第一，怎样表示"由几项不同类型的信息组成的一个整体"，例如一个学生的姓名、学号和成绩：这就是结构体；把结构体和上一章的指针结合起来，就得到可以随时插入、删除节点的链表。第二，怎样让数据在程序结束后保存下来、在下次运行时读回：这就是文件。本章最后以词频统计为例，示范怎样用**逐步求精**的方法把一个问题从粗略的思路一步步细化成可靠的程序。结构体是 [4.2](/4.2) 中类的前身，链表在 [4.3.3](/4.3.3) 中作为一种数据结构系统讨论，流与格式化输出在 [4.2.11](/4.2.11) 中展开。

## 9.1. 结构体

### 9.1.1. 定义与使用

**定义 9.1.1（结构体）** 把若干个可能类型不同的数据成员组合成一个新的类型，这样的用户自定义类型称为**结构体**。C++ 中用 `struct` 声明结构体类型，用"变量名.成员名"访问成员；通过**指针** `p` 访问时写 `p->成员名`，它是 `(*p).成员名` 的简写。

```cpp
#include <iostream>
#include <string>

struct Student {
    std::string name;
    int id = 0;
    double score = 0.0;  // default member initializers
};

int main() {
    Student a{"Alice", 2023001, 92.5};             // aggregate initialization
    Student b{.name = "Bob", .id = 2023002};       // designated initializers (C++20)
    Student* p = &b;
    p->score = 88.0;                               // same as (*p).score = 88.0
    std::cout << a.name << ' ' << b.name << ' ' << b.score << '\n';
}
```

结构体变量之间可以整体赋值（逐个成员复制），可以作为函数的参数和返回值。较大的结构体作参数时按常量**引用传递**（`const Student&`），避免复制；函数需要修改它时按引用传递。默认情况下两个结构体不能用 `==` 或 `<` 比较：编译器不知道"两个学生谁大"该怎样定义。排序时要么提供一个比较函数，要么为结构体定义比较运算符（[4.2.5](/4.2.5)）：

```cpp
#include <algorithm>
#include <vector>

// Higher score first; ties broken by smaller id.
bool before(const Student& x, const Student& y) {
    if (x.score != y.score) return x.score > y.score;
    return x.id < y.id;
}

void rank(std::vector<Student>& students) {
    std::sort(students.begin(), students.end(), before);
}
```

### 9.1.2. 结构体数组与平行数组

在没有结构体时，描述一批对象常用几个下标对应的数组，称为平行数组：`std::string name[100]; int id[100]; double score[100];`。它的缺点是同一个对象的信息分散在几处：排序时必须同步交换所有数组，漏掉一个数据就错位了。用结构体数组 `std::vector<Student>` 时，一个元素就是一个完整的对象，交换、传参、增删都以对象为单位。这是"程序 = 数据结构 + 算法"的一个具体体现：选对了数据的组织方式，算法就变得简单。后面各章的问题求解（如 [4.1.12](/4.1.12) 的跳马问题）也会用结构体把一个"状态"或"走法"打包。

Python 中与结构体对应的是数据类（`dataclasses.dataclass`），它自动生成构造、打印和比较方法：

```python
from dataclasses import dataclass

@dataclass
class Student:
    name: str
    id: int = 0
    score: float = 0.0

students = [Student("Alice", 2023001, 92.5), Student("Bob", 2023002, 88.0)]
students.sort(key=lambda s: (-s.score, s.id))  # higher score first, then smaller id
print(students[0])  # Student(name='Alice', id=2023001, score=92.5)
```

## 9.2. 链表

### 9.2.1. 从数组到链表

数组的元素在内存中连续存放，按下标访问只需一次地址计算；但在中间插入或删除一个元素，要把其后的所有元素整体移动。如果把每个元素和"下一个元素在哪里"打包成一个节点，节点就可以分散在内存各处，插入和删除只需修改几个指针。

**定义 9.2.1（链表）** 由若干节点组成、每个节点除数据外还保存指向下一个节点的指针的线性结构称为**链表**。第一个节点称为头节点，最后一个节点的指针为空；若最后一个节点的指针指回头节点，则称为**循环链表**。

```cpp
struct Node {
    int value;
    Node* next;  // a struct may contain a pointer to its own type
};
```

结构体不能包含自己类型的成员（那样大小将是无穷大），但可以包含指向自己类型的指针，因为指针的大小是固定的。

| 操作 | 数组 | 链表 |
|---|---|---|
| 访问第 $i$ 个元素 | 一步 | 从头开始走 $i$ 步 |
| 已知位置处插入、删除 | 移动其后的所有元素 | 修改常数个指针 |
| 额外空间 | 无 | 每个节点一个指针 |
| 内存分布 | 连续，对缓存友好 | 分散 |

各种操作的代价怎样随规模增长，即复杂度分析，在 [4.3.1](/4.3.1) 中讨论；[4.3.3](/4.3.3) 实现完整的列表结构。标准库提供了双向链表 `std::list` 和单向链表 `std::forward_list`；不过由于现代处理器的缓存机制，在多数实际场合中 `std::vector` 反而更快，只有在需要频繁在中间插入删除、并且已经持有位置时，链表才有优势。

### 9.2.2. 链表的基本操作

建立链表时，每读入一个数据就 `new` 一个节点，把它挂到当前尾节点的后面，再让尾指针前移。遍历时从头指针出发，沿 `next` 走到**空指针**为止。删除节点 `q` 时，要先让它的前驱跳过它（`prev->next = q->next`），再释放它；顺序反过来就会访问已释放的内存。程序结束前要逐个释放所有节点，否则就是**内存泄漏**（[4.1.8](/4.1.8)）。

```cpp
#include <iostream>

struct Node {
    int value;
    Node* next;
};

int main() {
    Node* head = nullptr;
    Node* tail = nullptr;
    for (int i = 1; i <= 5; ++i) {             // build 1 -> 2 -> 3 -> 4 -> 5
        Node* p = new Node{i, nullptr};
        if (head == nullptr) head = p;
        else tail->next = p;
        tail = p;
    }
    for (Node* p = head; p != nullptr; p = p->next)  // traverse
        std::cout << p->value << ' ';
    std::cout << '\n';
    while (head != nullptr) {                  // free every node
        Node* next = head->next;
        delete head;
        head = next;
    }
}
```

### 9.2.3. 例：约瑟夫问题

**例 9.2.1（约瑟夫问题）** $n$ 只猴子围成一圈，按顺时针方向编号 $1, \dots, n$。从 1 号开始依次报数 $1, 2, \dots, m$，报到 $m$ 的猴子出圈，下一只从 1 重新报数，如此反复，最后剩下的一只是猴王。按出圈顺序输出编号，并输出猴王。例如 $n = 8$、$m = 3$ 时，出圈顺序为 3 6 1 5 2 8 4，猴王是 7。

"围成一圈"正好对应循环链表：报数就是沿链表走 $m - 1$ 步，出圈就是删除节点。用数组模拟时，出圈要么移动元素，要么做标记并在报数时跳过已出圈者；用循环链表，删除只需修改一个指针。实现时始终保持指向"当前报数者的前驱"的指针 `prev`，因为删除一个节点需要它的前驱：

```cpp tab
#include <iostream>

struct Monkey {
    int id;
    Monkey* next;
};

int main() {
    int n = 8, m = 3;
    // Build a circular list 1 -> 2 -> ... -> n -> 1.
    Monkey* head = new Monkey{1, nullptr};
    Monkey* tail = head;
    for (int i = 2; i <= n; ++i) {
        tail->next = new Monkey{i, nullptr};
        tail = tail->next;
    }
    tail->next = head;

    Monkey* prev = tail;               // predecessor of the monkey who says "1"
    while (prev->next != prev) {       // more than one monkey left
        for (int k = 1; k < m; ++k) prev = prev->next;
        Monkey* out = prev->next;      // this monkey says m
        std::cout << out->id << ' ';
        prev->next = out->next;        // unlink it first ...
        delete out;                    // ... then release it
    }
    std::cout << "\nking: " << prev->id << '\n';
    delete prev;
}
```

```python tab
class Monkey:
    def __init__(self, id: int):
        self.id = id
        self.next: "Monkey | None" = None

n, m = 8, 3
# Build a circular list 1 -> 2 -> ... -> n -> 1.
head = tail = Monkey(1)
for i in range(2, n + 1):
    tail.next = Monkey(i)
    tail = tail.next
tail.next = head

prev = tail                      # predecessor of the monkey who says "1"
order = []
while prev.next is not prev:     # more than one monkey left
    for _ in range(m - 1):
        prev = prev.next
    out = prev.next              # this monkey says m
    order.append(out.id)
    prev.next = out.next         # unlink; the garbage collector frees it
print(*order)                    # 3 6 1 5 2 8 4
print("king:", prev.id)          # 7
```

Python 版本的结构与 C++ 一模一样：Python 的"引用"在这里扮演了指针的角色，只是删除节点后不必手工释放。在 Python 中用列表 `pop` 模拟（`i = (i + m - 1) % len(a); a.pop(i)`）更简短，这正是"同一个问题、不同的数据组织"。若只要求猴王的编号，还有更快的递推：设 $J(n)$ 是 $n$ 只猴子时猴王的位置（从 0 编号），则 $J(1) = 0$，$J(n) = (J(n-1) + m) \bmod n$，因为第一只出圈后，剩下的 $n - 1$ 只从出圈者的下一只重新编号，就是规模为 $n - 1$ 的同一问题。这种"化为规模更小的同一问题"的思路是 [4.1.10](/4.1.10) 的主题。

## 9.3. 文件

### 9.3.1. 文件的概念

**定义 9.3.1（文件）** 存储在外存（硬盘、固态硬盘等）上、有名字的一段字节序列称为**文件**。文件由文件系统按目录树组织，用路径（如 `/home/user/data.txt` 或 `C:\data\scores.txt`）定位；程序结束、断电之后文件仍然存在。

所有文件本质上都是字节序列，区别在于如何解释这些字节：

| | 文本文件 | 二进制文件 |
|---|---|---|
| 内容 | 字符的编码（ASCII、UTF-8 等），按行组织 | 数据在内存中的原始字节，或某种约定格式 |
| 例子 | 源代码、CSV、配置文件、日志 | 图像、音频、可执行程序、数据库 |
| 用文本编辑器打开 | 可读 | 乱码 |
| 数值 `12345` | 5 个字符 `'1'…'5'` | 一个 `int` 的 4 个字节 |
| 优点 | 人可读、可编辑，跨平台 | 紧凑，读写快，无需解析 |

现代程序的文本文件一律用 UTF-8 编码；汉字在 UTF-8 中占 3 个字节，所以"字符数"和"字节数"不同（[4.1.7](/4.1.7)）。

文件的用途远不止保存结果：把程序的可变部分（界面的颜色、字体，即所谓"皮肤"，或算法的参数）放进配置文件，不改代码、不重新编译就能改变程序的行为；把程序的中间状态写进文件，下次启动时读回，程序就有了"记忆"。

### 9.3.2. 文本文件的读写

C++ 通过文件流读写文件：`std::ifstream` 用于读，`std::ofstream` 用于写，用法与 `std::cin`、`std::cout` 相同。流对象在离开作用域时自动关闭文件，一般不必手工调用 `close()`。打开文件可能失败（文件不存在、没有权限），因此打开后必须检查，这是**防御性编程**的基本要求（[4.1.5](/4.1.5)）。

下面的程序实现一个"有记忆的累加器"：每次运行读入一个数，加到上次保存的总和上，再把新的总和写回文件。

```cpp tab
#include <fstream>
#include <iostream>

int main() {
    const char* path = "total.txt";
    long long total = 0;
    if (std::ifstream in{path}; in) {   // the file may not exist on the first run
        in >> total;
    }
    long long x;
    std::cin >> x;
    total += x;
    std::ofstream out{path};             // truncates and rewrites the file
    if (!out) {
        std::cerr << "cannot write " << path << '\n';
        return 1;
    }
    out << total << '\n';
    std::cout << "total = " << total << '\n';
}
```

```python tab
from pathlib import Path

path = Path("total.txt")
total = int(path.read_text()) if path.exists() else 0  # absent on the first run
total += int(input())
path.write_text(f"{total}\n")
print("total =", total)
```

读文件时最常见的错误是用 `eof()` 控制循环：

```cpp
std::string word;
while (!in.eof()) {   // WRONG
    in >> word;       // the last read fails, but word is still processed once more
    process(word);
}
```

`eof()` 只有在某次读取已经因为到达文件末尾而失败之后才返回真。读完最后一个单词时，流并不知道后面已经没有内容了（后面可能还有换行符），`eof()` 仍为假；下一次 `in >> word` 失败，而循环体仍按成功处理，于是最后一个单词被统计两次。正确的写法是把读取操作本身作为循环条件，读取失败时流转换为假：

```cpp
std::string word;
while (in >> word) {   // the loop body runs only after a successful read
    process(word);
}
std::string line;
while (std::getline(in, line)) {   // the same idiom, line by line
    process(line);
}
```

Python 用 `with` 语句打开文件，离开代码块时自动关闭，即使中途出错也一样（上下文管理器，见 [4.2.4](/4.2.4)）。文本模式下应当显式写明编码，否则会使用平台的默认编码；文件对象本身可以逐行迭代：

```python
with open("article.txt", encoding="utf-8") as f:
    for line in f:          # iterates line by line; no eof test is needed
        print(line.rstrip("\n"))
```

### 9.3.3. 二进制文件

二进制文件直接保存内存中的字节。C++ 以 `std::ios::binary` 模式打开文件，用 `write` 和 `read` 按字节块读写：

```cpp
#include <fstream>

struct State {
    int step;
    double value;
};

int main() {
    State s{42, 3.14};
    {
        std::ofstream out{"state.bin", std::ios::binary};
        out.write(reinterpret_cast<const char*>(&s), sizeof s);  // raw bytes of s
    }
    State t{};
    std::ifstream in{"state.bin", std::ios::binary};
    in.read(reinterpret_cast<char*>(&t), sizeof t);
    return t.step == 42 ? 0 : 1;
}
```

这样做简单快速，但写出的文件依赖于平台：结构体中可能有编译器插入的填充字节，整数在内存中的字节顺序（字节序，大多数平台为小端序）也因机器而异，不同编译器或平台写出的文件不一定能互相读取。只有不含指针、`std::string` 等间接成员的简单结构体才能这样整块写出：写出一个指针只是写出了一个地址，下次运行时它毫无意义。

标准的二进制格式会规定每个字段的偏移、长度和字节序。例如 WAV 音频文件以一个 44 字节的文件头开始，依次记录格式标记、声道数、采样率、每个样本的位数和数据长度，其后是采样数据。读取时按格式定义一个结构体并检查各字段，就能把多段录音拼接成新的音频，这正是最简单的拼接式语音合成的原理。需要跨平台交换数据时，更常用的是自描述的文本格式（CSV、JSON）或带有明确规范的二进制格式。Python 的标准库 `struct` 模块按给定格式打包和解析字节（`struct.pack("<id", step, value)` 中的 `<` 指定小端序）。

## 9.4. 逐步求精：词频统计

**例 9.4.1（词频统计）** 读入一篇英文文章，按单词首次出现的顺序输出每个单词及其出现次数，单词后面的标点不计入单词。

面对一个不能一眼写出代码的问题，可以先写出最粗略的步骤，再逐个细化每一步，直到每一步都能直接写成代码。这就是 [4.1.4](/4.1.4) 中自顶向下、**逐步求精**的方法。词频统计的第一层思路只有三句话：

1. 依次读入每个单词；
2. 对每个单词：若已记录过，次数加 1；否则把它加入记录，次数为 1；
3. 输出所有记录。

先决定数据结构：每条记录要同时保存拼写和次数，用结构体 `WordCount`；记录有很多条，用结构体数组。第 2 步细化为"在数组中顺序查找该单词"。第一版程序写好后用样例测试，发现 `emacs,` 和 `emacs` 被当成两个单词；于是加入第 4 步"去掉单词末尾的标点"。好的做法是把这一步写成独立的小函数，而不是在主循环里直接判断逗号和句号：主循环只表达"清洗单词"这件事，至于哪些字符算标点、单词存在什么里，交给下层函数，以后修改也只改一处。最后，把循环条件写成 `while (in >> word)`，避免 §9.3.2 中最后一个单词被统计两次的错误。

```cpp tab
#include <cctype>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

struct WordCount {
    std::string word;
    int count;
};

// Remove trailing punctuation such as "," "." "!" from a word.
std::string strip_punctuation(std::string w) {
    while (!w.empty() && std::ispunct(static_cast<unsigned char>(w.back())))
        w.pop_back();
    return w;
}

// Return the index of w in table, or -1 if absent (sequential search).
int find_word(const std::vector<WordCount>& table, const std::string& w) {
    for (int i = 0; i < static_cast<int>(table.size()); ++i)
        if (table[i].word == w) return i;
    return -1;
}

int main(int argc, char* argv[]) {
    if (argc < 2) {
        std::cerr << "usage: wordfreq FILE\n";
        return 1;
    }
    std::ifstream in{argv[1]};
    if (!in) {
        std::cerr << "cannot open " << argv[1] << '\n';
        return 1;
    }
    std::vector<WordCount> table;
    std::string raw;
    while (in >> raw) {                        // step 1: read each word
        std::string w = strip_punctuation(raw); // step 4: clean it
        if (w.empty()) continue;
        if (int i = find_word(table, w); i >= 0)
            ++table[i].count;                  // step 2: seen before
        else
            table.push_back({w, 1});           //         new word
    }
    for (const auto& [word, count] : table)    // step 3: report
        std::cout << word << ' ' << count << '\n';
}
```

```python tab
import string
import sys

def strip_punctuation(w: str) -> str:
    """Remove trailing punctuation such as ',' '.' '!' from a word."""
    return w.rstrip(string.punctuation)

def main() -> None:
    if len(sys.argv) < 2:
        sys.exit("usage: wordfreq FILE")
    counts: dict[str, int] = {}           # dicts keep insertion order
    with open(sys.argv[1], encoding="utf-8") as f:
        for line in f:                    # step 1: read each word
            for raw in line.split():
                w = strip_punctuation(raw)  # step 4: clean it
                if w:
                    counts[w] = counts.get(w, 0) + 1  # step 2
    for word, count in counts.items():    # step 3: report
        print(word, count)

if __name__ == "__main__":
    main()
```

两个版本的结构相同，差别在于"查找单词"这一步：C++ 版本在数组中顺序查找，文章有 $n$ 个单词、$k$ 个不同单词时，总的比较次数可达 $nk$ 量级；Python 的字典用散列表实现，每次查找平均只需常数时间。C++ 中对应的容器是 `std::unordered_map`（散列表）和 `std::map`（有序，基于平衡搜索树），见 [4.2.10](/4.2.10)，原理见 [4.3.9](/4.3.9) 与 [4.3.6](/4.3.6)。逐步求精的好处在这里也看得出来：替换数据结构只需重写 `find_word` 这一层，主循环不变。Python 标准库的 `collections.Counter` 把整个统计压缩成一行，`Counter(words).most_common(10)` 还能直接给出最高频的 10 个单词。

## 小结

- 结构体把描述同一对象的数据打包成一个类型；用结构体数组代替平行数组。
- 链表用指针把分散的节点串起来，插入、删除只改指针，但不能**随机访问**；循环链表适合"围成一圈"的问题。删除节点前先修改前驱的指针，用完逐个释放。
- 文件把数据保存在程序之外。打开后检查是否成功；用读取操作本身控制循环，不用 `eof()`；文本文件写明编码；整块写出结构体的二进制文件依赖平台。
- 逐步求精：先写出几句话的粗略步骤，逐层细化；把可能变化的细节封装成下层函数。
