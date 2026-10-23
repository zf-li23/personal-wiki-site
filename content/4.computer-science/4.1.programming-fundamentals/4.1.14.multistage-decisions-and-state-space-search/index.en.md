---
title: Multistage Decisions and State-Space Search
description: Mathematical models of multistage decision problems (states, decisions, and state transitions); digitizing the states of the people-and-ghosts river-crossing problem; the state space and state graph; depth-first search with visited marks and breadth-first search for the fewest steps; a summary of problem-solving strategies and search in artificial intelligence.
source_hash: bc46d823be83
---

In the problems of the previous chapters (going downstairs, the knight's path, book assignment, eight queens), every step moves the problem toward its goal: the stairs decrease, the knight moves rightward, the number of people with books grows. Many problems are not like this. In crossing a river, the boat carries some people across and must also carry some back; in a maze one meets forks and dead ends; in jigsaw puzzles, Rubik's cubes, and board games, the same position can recur through different sequences of moves. This chapter discusses a general modeling method for such multistage decision problems: abstract the situation of the problem at each moment into a "state" and each operation into a "transition" between states, so that solving the problem becomes finding a path from the initial state to the goal state in the space of all states. Using the people-and-ghosts river-crossing problem as an example, we explain in turn how to digitize a game, how to avoid going in circles with depth-first search with visited marks, and how to find the plan with the fewest steps by breadth-first search. State-space search is one of the basic methods of artificial intelligence; [4.5 Introduction to Artificial Intelligence](/4.5) builds on it to discuss heuristic search and game-tree search, and graph traversal algorithms themselves are discussed systematically in [4.3.10](/4.3.10). At the end of the chapter we summarize the problem-solving strategies met since [4.1.10](/4.1.10).

## 14.1. Modeling Multistage Decision Problems

### 14.1.1. Example: People and Ghosts Crossing the River

**Example 14.1.1 (People and Ghosts Crossing the River)** Three people and three ghosts are on the east bank of a river and must all be ferried to the west bank by a small boat. The boat carries at most 2 passengers (two people, two ghosts, or one of each), and at least 1 must row. On either bank, whenever the ghosts outnumber the people (and there are people on that bank), the people are eaten. When the boat lands, its passengers count as being on the bank. Find a safe plan for crossing, with as few crossings as possible.

This problem is a version of the classic "missionaries and cannibals" problem. Unlike the problems of the earlier chapters, it has no obvious "same problem of smaller size": the boat must go back and forth, and sometimes people who have already crossed must be taken back. To have a computer solve it, we first have to find which quantities change during the process and how to represent them by numbers.

### 14.1.2. Digitizing States and Decisions

Observing the crossing process, the changing quantities are the numbers of people and ghosts on the east bank, on the west bank, and in the boat, and the position of the boat. Some are redundant: the numbers of people on the two banks sum to 3, and so do the numbers of ghosts, so the east bank alone suffices; passengers in the boat count as being on the bank once it lands, so they need not be recorded separately. The situation at a given moment can be completely described by the triple

$$
S = (r, g, b):
$$

there are $r$ people and $g$ ghosts on the east bank, and $b = 0$ means the boat is on the east bank, $b = 1$ that it is on the west bank. The initial state is $(3, 3, 0)$ and the goal state is $(0, 0, 1)$.

The decision of one crossing is how many people and how many ghosts the boat carries, denoted $d = (u, v)$. There are only 5 decisions satisfying the boat's capacity:

$$
D = \{(2, 0),\ (1, 0),\ (1, 1),\ (0, 1),\ (0, 2)\}.
$$

When the boat goes from the east bank to the west bank, the people and ghosts on the east bank decrease; when it returns from west to east, they increase. So the state transition for the $k$-th crossing ($k = 1, 2, \dots$) is

$$
(r_k, g_k) = (r_{k-1}, g_{k-1}) + (-1)^k (u_k, v_k), \qquad b_k = 1 - b_{k-1},
$$

with the boat going east to west for odd $k$ and west to east for even $k$. The new state is valid if $0 \leq r, g \leq 3$ (no more people or ghosts can be carried away than are on the bank) and both banks are safe: on the east bank $r = 0$ or $r \geq g$, and on the west bank $3 - r = 0$ or $3 - r \geq 3 - g$. For the case of 3 people and 3 ghosts, the two conditions together amount to

$$
r = 0 \quad\text{or}\quad r = 3 \quad\text{or}\quad r = g.
$$

Putting the boat position $b$ into the state is necessary: with the same 2 people and 2 ghosts on the east bank, the available decisions are entirely different when the boat is on the east bank and when it is on the west bank, so these must be regarded as two states.

### 14.1.3. The State Space

Abstracting this modeling method gives a general framework for solving multistage decision problems.

**Definition 14.1.1 (State Space)** A set of variables describing the situation of a problem at some moment is called a **state**; a state becoming another state under one operation is called a state transition. The model consisting of all possible states, all valid transitions, the initial state, and the goal states is called the **state space** of the problem. Solving the problem means finding, in the state space, a sequence of transitions from the initial state to some goal state.

Drawing states as nodes and valid transitions as directed edges, the state space is a directed graph (the state graph); in the people-and-ghosts problem, every crossing can be reversed exactly, so edges come in pairs. In the state space of this problem, only 16 valid states are reachable from the initial state. This graph contains cycles: $(3, 3, 0) \to (2, 2, 1) \to (3, 3, 0)$ is "one person and one ghost cross, then return together". The decision trees of the previous chapters have no cycles because every step changes some quantity monotonically; once cycles exist, blind recursion may go in circles forever.

| Element | People and ghosts | Knight's path ([4.1.12](/4.1.12)) | Eight queens |
|---|---|---|---|
| State | $(r, g, b)$ | knight's coordinates $(x, y)$ | positions of the queens in the first $k$ rows |
| Operation | 5 ways of loading | 4 kinds of jumps | the 8 columns of row $k + 1$ |
| Validity condition | people not outnumbered by ghosts | stay on the board | no mutual attacks |
| Initial / goal | $(3,3,0)$ / $(0,0,1)$ | $(0,0)$ / $(8,4)$ | empty board / 8 rows filled |
| Does the state graph have cycles? | yes | no (jumps only rightward) | no (placement row by row) |

## 14.2. Depth-First Search

### 14.2.1. Avoiding Going in Circles with Visited Marks

The people-and-ghosts problem can be regarded as a special kind of "knight's path": the board is the state space and the jumps are the 5 decisions. Following the recursive enumeration of [4.1.12](/4.1.12), we try each decision in turn from the current state and recurse on each valid new state. The only addition needed is this: because the state graph contains cycles, we must record which states have been visited and not enter a visited state again. This is **depth-first search** on the state graph.

```cpp tab
#include <array>
#include <iostream>
#include <vector>

struct State { int r, g, b; };              // people and ghosts on the east bank; boat side

constexpr std::array<std::array<int, 2>, 5> kLoads = {{{2, 0}, {1, 0}, {1, 1}, {0, 1}, {0, 2}}};
bool visited[4][4][2] = {};
std::vector<State> path;

bool safe(int r, int g) {
    return 0 <= r && r <= 3 && 0 <= g && g <= 3 && (r == 0 || r == 3 || r == g);
}

bool dfs(State s) {
    if (s.r == 0 && s.g == 0 && s.b == 1) return true;   // everyone is on the west bank
    int sign = (s.b == 0) ? -1 : +1;                     // east -> west removes people
    for (auto [u, v] : kLoads) {
        State t{s.r + sign * u, s.g + sign * v, 1 - s.b};
        if (!safe(t.r, t.g) || visited[t.r][t.g][t.b]) continue;
        visited[t.r][t.g][t.b] = true;                   // never enter a state twice
        path.push_back(t);
        if (dfs(t)) return true;                         // stop at the first solution
        path.pop_back();
    }
    return false;
}

int main() {
    State start{3, 3, 0};
    visited[3][3][0] = true;
    path.push_back(start);
    if (dfs(start)) {
        for (auto [r, g, b] : path) std::cout << '(' << r << ',' << g << ',' << b << ") ";
        std::cout << '\n' << path.size() - 1 << " crossings\n";
    }
}
```

```python tab
LOADS = [(2, 0), (1, 0), (1, 1), (0, 1), (0, 2)]
State = tuple[int, int, int]        # people and ghosts on the east bank; boat side

def safe(r: int, g: int) -> bool:
    return 0 <= r <= 3 and 0 <= g <= 3 and (r in (0, 3) or r == g)

def dfs(s: State, path: list[State], visited: set[State]) -> bool:
    r, g, b = s
    if (r, g, b) == (0, 0, 1):                       # everyone is on the west bank
        return True
    sign = -1 if b == 0 else +1                      # east -> west removes people
    for u, v in LOADS:
        t = (r + sign * u, g + sign * v, 1 - b)
        if not safe(t[0], t[1]) or t in visited:
            continue
        visited.add(t)                               # never enter a state twice
        path.append(t)
        if dfs(t, path, visited):                    # stop at the first solution
            return True
        path.pop()
    return False

start = (3, 3, 0)
path = [start]
if dfs(start, path, {start}):
    print(*path)
    print(len(path) - 1, "crossings")
```

Unlike the **backtracking** of [4.1.12](/4.1.12), here the visited marks are not undone on retreat: if no solution can be found from some state, none will be found when it is reached again later by another path, so there is no need to try again. Visited marks are essentially a kind of memo ([4.1.10](/4.1.10)), except that what they remember is not the value of a subproblem but "this state has already been explored". Each state is entered at most once, so the amount of search does not exceed the number of states times the number of decisions.

With the order of decisions above, depth-first search happens to find a plan with 11 crossings. But this is a coincidence: depth-first search guarantees only that it finds some path, not that it is shortest; with a different order of trying the decisions, the plan found might be longer.

### 14.2.2. Iterative Implementation

Depth-first search can also be done without recursion: put the "states waiting to be explored" on a stack, each time take the state on top, and push its unvisited successors onto the stack. This replaces the **call stack** by an explicit stack ([4.3.4](/4.3.4)). When the state space is large and the search deep, the iterative version avoids **stack overflow** and Python's recursion depth limit.

## 14.3. Breadth-First Search

To require the fewest crossings, we must change the order of search: first find all states reachable in 1 step, then all states reachable in 2 steps, and so on, expanding outward layer by layer. The first time the goal state is reached, the number of steps used is necessarily minimal. This is **breadth-first search**. It is implemented with a queue: states that enter the queue first are expanded first, so states are processed in increasing order of "number of steps from the initial state". To output the plan, we also record for each state the state it was reached from (its predecessor), and after reaching the goal we trace back along the predecessors to the initial state.

```cpp tab
#include <algorithm>
#include <array>
#include <iostream>
#include <map>
#include <queue>
#include <vector>

using State = std::array<int, 3>;           // {people east, ghosts east, boat side}

bool safe(int r, int g) {
    return 0 <= r && r <= 3 && 0 <= g && g <= 3 && (r == 0 || r == 3 || r == g);
}

int main() {
    constexpr std::array<std::array<int, 2>, 5> loads = {{{2, 0}, {1, 0}, {1, 1}, {0, 1}, {0, 2}}};
    const State start{3, 3, 0}, goal{0, 0, 1};
    std::map<State, State> parent{{start, start}};   // also serves as the visited set
    std::queue<State> frontier;
    frontier.push(start);
    while (!frontier.empty()) {
        State s = frontier.front();
        frontier.pop();
        if (s == goal) break;
        int sign = (s[2] == 0) ? -1 : +1;
        for (auto [u, v] : loads) {
            State t{s[0] + sign * u, s[1] + sign * v, 1 - s[2]};
            if (!safe(t[0], t[1]) || parent.contains(t)) continue;
            parent[t] = s;                           // reached for the first time
            frontier.push(t);
        }
    }
    std::vector<State> path;
    for (State s = goal; s != start; s = parent[s]) path.push_back(s);
    path.push_back(start);
    std::reverse(path.begin(), path.end());
    for (auto [r, g, b] : path) std::cout << '(' << r << ',' << g << ',' << b << ") ";
    std::cout << '\n' << path.size() - 1 << " crossings\n";  // 11
}
```

```python tab
from collections import deque

LOADS = [(2, 0), (1, 0), (1, 1), (0, 1), (0, 2)]

def safe(r: int, g: int) -> bool:
    return 0 <= r <= 3 and 0 <= g <= 3 and (r in (0, 3) or r == g)

start, goal = (3, 3, 0), (0, 0, 1)
parent = {start: None}               # also serves as the visited set
frontier = deque([start])
while frontier:
    s = frontier.popleft()
    if s == goal:
        break
    r, g, b = s
    sign = -1 if b == 0 else +1
    for u, v in LOADS:
        t = (r + sign * u, g + sign * v, 1 - b)
        if safe(t[0], t[1]) and t not in parent:
            parent[t] = s            # reached for the first time
            frontier.append(t)

path = []
s = goal
while s is not None:
    path.append(s)
    s = parent[s]
path.reverse()
print(*path)
print(len(path) - 1, "crossings")    # 11
```

At least 11 crossings are needed. Writing $(r, g)$ for the numbers of people and ghosts on the east bank, an optimal plan is as follows (the labels on the arrows are the numbers of people and ghosts in the boat; odd-numbered crossings go west, even-numbered ones east):

```mermaid
flowchart LR
    s0["(3,3) boat on east bank"] -->|"1 person, 1 ghost →"| s1["(2,2)"]
    s1 -->|"← 1 person"| s2["(3,2)"]
    s2 -->|"2 ghosts →"| s3["(3,0)"]
    s3 -->|"← 1 ghost"| s4["(3,1)"]
    s4 -->|"2 people →"| s5["(1,1)"]
    s5 -->|"← 1 person, 1 ghost"| s6["(2,2)"]
    s6 -->|"2 people →"| s7["(0,2)"]
    s7 -->|"← 1 ghost"| s8["(0,3)"]
    s8 -->|"2 ghosts →"| s9["(0,1)"]
    s9 -->|"← 1 person"| s10["(1,1)"]
    s10 -->|"1 person, 1 ghost →"| s11["(0,0) boat on west bank"]
```

Note that step 6 takes one person and one ghost back to the east bank, and the state $(2, 2)$ appears once more, only with the boat on the other side. It is precisely this "step backward" that makes the problem difficult, and it also explains why the boat position must be part of the state.

The two searches compare as follows:

| | Depth-first search | Breadth-first search |
|---|---|---|
| Order of expansion | go to the end of one path, then backtrack | expand layer by layer by the number of steps from the start |
| Data structure | stack (or the recursion call stack) | queue |
| Solution found | some solution, not necessarily shortest | solution with the fewest steps |
| Memory | proportional to the search depth | proportional to the number of states in one layer, possibly large |
| Suited to | finding all solutions (with backtracking), deciding whether a solution exists | finding the fewest steps |

## 14.4. Generalizing State-Space Search

The state space of the people-and-ghosts problem has only a dozen or so states, and any search method finishes instantly. The state spaces of real problems are often far larger: the 15-puzzle has about $10^{13}$ states, the Rubik's cube about $4.3 \times 10^{19}$, and chess and Go are too large to enumerate. There are then several directions:

- **Pruning** and symmetry: as in eight queens, exclude infeasible states as early as possible and use symmetry to merge equivalent states.
- Heuristic search: guided by an estimate of "how far from the goal", expand the more promising states first; the representative algorithm is A\* search. With a suitable estimate, it both guarantees finding the shortest path and explores only a small part of the state space.
- Weighted shortest paths: if each step has a different cost (distance, time), breadth-first search generalizes to Dijkstra's algorithm ([4.3.11](/4.3.11)).
- Game-tree search: games in which two opponents decide in turn (board games) require considering the opponent's best replies, using minimax search and α-β pruning.

These methods are the content of [4.5 Introduction to Artificial Intelligence](/4.5). The significance of this chapter lies in modeling: once a problem is represented as a state space, a whole set of general search algorithms can be applied, without designing a separate solution for each problem.

## Summary

This chapter models multistage decision problems as a state space (Definition 14.1.1): the states are digitized as a set of variables, decisions cause state transitions, and the problem becomes finding a path from the initial state to a goal state in the state graph. Depth-first search with visited marks avoids going around in circles in a state graph with cycles and finds one solution; breadth-first search expands the states level by level, so the first time it reaches a goal it gives a solution with the fewest steps.

### Problem-Solving Strategies

The strategies from [4.1.10](/4.1.10) to this chapter all start from the idea of "reducing the problem to a smaller or closer problem"; they differ in the relation between subproblems:

| Strategy | Structure of subproblems | Typical examples | Chapter |
|---|---|---|---|
| Decrease and conquer | one smaller subproblem | factorial, binary search, Tower of Hanoi | [4.1.10](/4.1.10) |
| Divide and conquer | several independent subproblems whose results are merged | merge sort, quicksort | [4.1.11](/4.1.11) |
| Enumeration and backtracking | all choices at each step form a decision tree | staircase, book assignment, eight queens | [4.1.12](/4.1.12) |
| Dynamic programming | overlapping subproblems with optimal substructure | rod cutting, matrix chain | [4.1.13](/4.1.13) |
| State-space search | a state graph, possibly with cycles | people and ghosts crossing | this chapter |

Given a problem, we can ask ourselves in turn: can the situation of the problem at a given moment be described by a set of variables (the state)? What choices are there at each step (the decisions)? How does the state change after a choice (the transition)? Which states are valid and which are goals? Do we want all solutions, any solution, or an optimal solution? Can different paths reach the same state? Once these questions are answered, which strategy to choose and which data structures to use are also clear.
