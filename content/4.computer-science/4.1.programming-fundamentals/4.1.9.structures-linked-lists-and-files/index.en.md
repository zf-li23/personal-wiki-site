---
title: Structures, Linked Lists, and Files
description: Packing related data with structures, arrays of structures versus parallel arrays; chaining structures into linked lists with pointers, building, traversing, and deleting in singly linked and circular lists, the Josephus problem; text and binary files, reading and writing with file streams and common pitfalls; stepwise refinement illustrated by word-frequency counting.
source_hash: ac5284a673ac
---

So far, the data our programs handle has been either single variables or arrays of elements of one type, and the data disappears when the program ends. This chapter addresses two problems. First, how do we represent "a whole made of several pieces of information of different types", such as a student's name, ID, and score? This is the structure; combining structures with the pointers of the previous chapter yields linked lists, in which nodes can be inserted and deleted at any time. Second, how do we keep data after the program ends and read it back in the next run? This is the file. At the end of the chapter we use word-frequency counting to show how **stepwise refinement** turns a rough idea into a reliable program, one step at a time. The structure is the predecessor of the class in [4.2](/4.2), linked lists are discussed systematically as a data structure in [4.3.3](/4.3.3), and streams and formatted output are developed in [4.2.11](/4.2.11).

## 9.1. Structures

### 9.1.1. Definition and Use

**Definition 9.1.1 (Structure)** A user-defined type that combines several data members, possibly of different types, into a new type is called a **structure**. In C++, a structure type is declared with `struct` and its members are accessed as "variable name.member name"; when accessing through a **pointer** `p`, we write `p->member`, which is shorthand for `(*p).member`.

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

Structure variables can be assigned as a whole (member by member) and can be passed to and returned from functions. A large structure is passed to a function by constant reference (`const Student&`), which is **pass by reference** and avoids copying; pass by non-const reference when the function must modify it. By default two structures cannot be compared with `==` or `<`: the compiler does not know how to define which of two students is "greater". To sort, either supply a comparison function or define comparison operators for the structure ([4.2.5](/4.2.5)):

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

### 9.1.2. Arrays of Structures and Parallel Arrays

Without structures, a collection of objects is often described by several arrays that correspond by index, called parallel arrays: `std::string name[100]; int id[100]; double score[100];`. Their drawback is that the information about one object is scattered over several places: sorting must swap all the arrays in step, and missing one misaligns the data. With an array of structures, `std::vector<Student>`, one element is a complete object, and swapping, passing, inserting, and deleting all work on whole objects. This is a concrete instance of "program = data structures + algorithms": once the data is organized the right way, the algorithm becomes simple. Problem solving in later chapters (such as the knight's tour problem in [4.1.12](/4.1.12)) also uses structures to package a "state" or a "move".

The Python counterpart of a structure is the data class (`dataclasses.dataclass`), which automatically generates the constructor, printing, and comparison methods:

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

## 9.2. Linked Lists

### 9.2.1. From Arrays to Linked Lists

The elements of an array are stored contiguously in memory, so access by index takes a single address computation; but inserting or deleting an element in the middle requires shifting all the elements after it. If each element is packaged together with "where the next element is" into a node, the nodes can be scattered anywhere in memory, and insertion and deletion only require changing a few pointers.

**Definition 9.2.1 (Linked List)** A linear structure consisting of nodes, each of which stores, besides its data, a pointer to the next node, is called a **linked list**. The first node is called the head, and the pointer of the last node is null; if the pointer of the last node points back to the head, the list is called a **circular linked list**.

```cpp
struct Node {
    int value;
    Node* next;  // a struct may contain a pointer to its own type
};
```

A structure cannot contain a member of its own type (its size would be infinite), but it can contain a pointer to its own type, because the size of a pointer is fixed.

| Operation | Array | Linked list |
|---|---|---|
| Access the $i$-th element | one step | walk $i$ steps from the head |
| Insert or delete at a known position | shift all later elements | change a constant number of pointers |
| Extra space | none | one pointer per node |
| Memory layout | contiguous, cache-friendly | scattered |

How the cost of each operation grows with problem size, that is, complexity analysis, is discussed in [4.3.1](/4.3.1); [4.3.3](/4.3.3) implements a complete list structure. The standard library provides the doubly linked list `std::list` and the singly linked list `std::forward_list`; however, because of the caching mechanisms of modern processors, `std::vector` is in fact faster in most practical situations, and linked lists have an advantage only when elements must be inserted or deleted frequently in the middle and the position is already in hand.

### 9.2.2. Basic Operations on Linked Lists

To build a linked list, we `new` a node for each data item read, attach it after the current tail node, and advance the tail pointer. To traverse, we start from the head pointer and follow `next` until we reach the **null pointer**. To delete a node `q`, we first let its predecessor skip over it (`prev->next = q->next`) and then release it; in the reverse order we would access released memory. Before the program ends, all nodes must be released one by one; otherwise there is a **memory leak** ([4.1.8](/4.1.8)).

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

### 9.2.3. Example: The Josephus Problem

**Example 9.2.1 (Josephus Problem)** $n$ monkeys stand in a circle, numbered $1, \dots, n$ clockwise. Starting from monkey 1, they count off $1, 2, \dots, m$ in turn; the monkey that counts $m$ leaves the circle, and the next monkey restarts the count from 1. This repeats until one monkey remains, who becomes the king. Output the numbers in the order in which monkeys leave, and then the king. For example, for $n = 8$ and $m = 3$, the order of leaving is 3 6 1 5 2 8 4 and the king is 7.

"Standing in a circle" corresponds exactly to a circular linked list: counting off means walking $m - 1$ steps along the list, and leaving the circle means deleting a node. When simulating with an array, leaving requires either shifting elements or marking and skipping the departed monkeys while counting; with a circular linked list, deletion only changes one pointer. In the implementation we always keep a pointer `prev` to the predecessor of the monkey currently counting, because deleting a node requires its predecessor:

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

The structure of the Python version is exactly the same as the C++ one: Python's "references" play the role of pointers here, except that deleted nodes need not be released by hand. In Python, simulating with a list and `pop` (`i = (i + m - 1) % len(a); a.pop(i)`) is shorter still, which is precisely "the same problem, a different organization of data". If only the king's number is required, there is an even faster recurrence: let $J(n)$ be the king's position (numbered from 0) with $n$ monkeys; then $J(1) = 0$ and $J(n) = (J(n-1) + m) \bmod n$, because after the first monkey leaves, the remaining $n - 1$ monkeys, renumbered starting from the one after the departed, form the same problem of size $n - 1$. This idea of "reducing to the same problem of smaller size" is the subject of [4.1.10](/4.1.10).

## 9.3. Files

### 9.3.1. The Concept of a File

**Definition 9.3.1 (File)** A named sequence of bytes stored in external storage (hard disk, solid-state drive, and so on) is called a **file**. Files are organized by the file system into a directory tree and located by paths (such as `/home/user/data.txt` or `C:\data\scores.txt`); a file persists after the program ends or the power is cut.

All files are, in essence, sequences of bytes; they differ in how the bytes are interpreted:

| | Text file | Binary file |
|---|---|---|
| Contents | encoded characters (ASCII, UTF-8, etc.), organized in lines | raw bytes of data as in memory, or some agreed format |
| Examples | source code, CSV, configuration files, logs | images, audio, executables, databases |
| Opened in a text editor | readable | garbled |
| The number `12345` | 5 characters `'1'…'5'` | the 4 bytes of an `int` |
| Advantages | human-readable and editable, portable | compact, fast to read and write, no parsing |

Modern programs always use UTF-8 for text files; a Chinese character occupies 3 bytes in UTF-8, so the "number of characters" and the "number of bytes" differ ([4.1.7](/4.1.7)).

Files are used for much more than saving results: putting the variable parts of a program (the colors and fonts of an interface, the so-called "skin", or the parameters of an algorithm) into a configuration file changes the program's behavior without changing the code or recompiling; writing the intermediate state of a program to a file and reading it back at the next start gives the program a "memory".

### 9.3.2. Reading and Writing Text Files

C++ reads and writes files through file streams: `std::ifstream` for reading and `std::ofstream` for writing, used just like `std::cin` and `std::cout`. A stream object closes its file automatically when it leaves scope, so calling `close()` by hand is generally unnecessary. Opening a file may fail (the file does not exist, no permission), so the result must be checked after opening; this is a basic requirement of **defensive programming** ([4.1.5](/4.1.5)).

The following program implements an "accumulator with memory": each run reads a number, adds it to the sum saved last time, and writes the new sum back to the file.

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

The most common mistake when reading a file is to control the loop with `eof()`:

```cpp
std::string word;
while (!in.eof()) {   // WRONG
    in >> word;       // the last read fails, but word is still processed once more
    process(word);
}
```

`eof()` returns true only after some read has already failed because the end of the file was reached. After the last word is read, the stream does not know that nothing follows (a newline may still follow), so `eof()` is still false; the next `in >> word` fails, yet the loop body still treats it as a success, and the last word is counted twice. The correct way is to use the read operation itself as the loop condition; when the read fails, the stream converts to false:

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

Python opens files with the `with` statement, which closes the file automatically when the block is left, even if an error occurs midway (context managers, see [4.2.4](/4.2.4)). In text mode, the encoding should be stated explicitly; otherwise the platform's default encoding is used. A file object can itself be iterated line by line:

```python
with open("article.txt", encoding="utf-8") as f:
    for line in f:          # iterates line by line; no eof test is needed
        print(line.rstrip("\n"))
```

### 9.3.3. Binary Files

A binary file stores the bytes of memory directly. C++ opens the file in `std::ios::binary` mode and reads and writes blocks of bytes with `write` and `read`:

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

This is simple and fast, but the resulting file depends on the platform: a structure may contain padding bytes inserted by the compiler, and the byte order of integers in memory (endianness; little-endian on most platforms) varies from machine to machine, so files written by different compilers or platforms may not be readable by one another. Only simple structures with no indirect members such as pointers or `std::string` can be written out as a block this way: writing a pointer writes only an address, which is meaningless in the next run.

A standard binary format specifies the offset, length, and byte order of every field. For example, a WAV audio file begins with a 44-byte header that records, in order, the format tag, the number of channels, the sample rate, the bits per sample, and the length of the data, followed by the sample data. Reading it by defining a structure according to the format and checking its fields makes it possible to concatenate several recordings into a new audio clip, which is exactly the principle of the simplest concatenative speech synthesis. When data must be exchanged across platforms, self-describing text formats (CSV, JSON) or binary formats with a clear specification are more common. Python's standard `struct` module packs and parses bytes according to a given format (in `struct.pack("<id", step, value)`, the `<` specifies little-endian).

## 9.4. Stepwise Refinement: Word-Frequency Counting

**Example 9.4.1 (Word-Frequency Counting)** Read an English article and output each word, in order of first appearance, together with its number of occurrences; punctuation following a word is not counted as part of the word.

Faced with a problem for which the code cannot be written at a glance, we can first write the roughest possible steps and then refine each step until every one can be written directly as code. This is the top-down method of **stepwise refinement** from [4.1.4](/4.1.4). The first-level idea of word-frequency counting takes only three sentences:

1. Read each word in turn.
2. For each word: if it has been recorded, add 1 to its count; otherwise add it to the records with count 1.
3. Output all the records.

First we decide on the data structure: each record must store both the spelling and the count, so we use a structure `WordCount`; there are many records, so we use an array of structures. Step 2 is refined into "sequentially search the array for the word". After writing the first version and testing it on a sample, we find that `emacs,` and `emacs` are treated as two different words, so we add a step 4, "strip trailing punctuation from the word". A good practice is to write this step as a separate small function rather than testing for commas and periods directly in the main loop: the main loop then expresses only the task "clean the word", and which characters count as punctuation and what the words are stored in is left to lower-level functions, so that later changes touch only one place. Finally, we write the loop condition as `while (in >> word)`, avoiding the error of §9.3.2 in which the last word is counted twice.

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

## Summary

- A structure packs the data describing one object into a single type; use an array of structures instead of parallel arrays.
- A linked list strings scattered nodes together with pointers. Insertion and deletion only change pointers, but there is no **random access**; a circular linked list suits problems where things "stand in a ring". Before deleting a node, update its predecessor's pointer, and free the nodes one by one when done.
- Files keep data outside the program. Check that opening succeeded; let the read operation itself control the loop instead of `eof()`; state the encoding of text files; binary files that write whole structures depend on the platform.
- Stepwise refinement: write the rough steps in a few sentences first and refine them level by level; hide the details that may change in lower-level functions.
