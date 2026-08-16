???+ note "Tip"
    This article is under editing and discussion; you are welcome to add further learning roadmaps or share your ideas in the comments section!

This article introduces a learning roadmap for competitive programming.

This roadmap is both a guide for beginners learning competitive-programming knowledge and a review checklist.

## 1 C++ language basics

Start by learning C++ syntax, step by step.

### 1.1 Hello, World!

Begin your competitive-programming journey with a single `Hello, World!`

At the same time, get a rough idea of what the general framework of a C++ source program looks like.

-   [Hello, World!](../lang/helloworld.md)
-   [C++ syntax basics](../lang/basic.md)

### 1.2 Variables and operations

The original purpose of the computer was computation. So let's first learn how to complete some simple computational tasks.

-   [Variables](../lang/var.md)
-   [Operations](../lang/op.md)

### 1.3 Control flow

#### 1.3.1 Branch structures

Sometimes we need to choose to execute different statements under different conditions, and then we need to rely on branch statements.

-   [Branches](../lang/branch.md)

Branch statements include the following kinds:

-   the if statement
-   the if-else statement
-   the if-elif-else statement
-   the switch statement

#### 1.3.2 Loop structures

To execute several statements repeatedly many times, we need loop statements.

-   [Loops](../lang/loop.md)

Loop statements include the following kinds:

-   the for statement
-   the while statement
-   the do-while statement

### 1.4 Arrays and structs

Arrays are used to store large amounts of data of the same type. Structs, on the other hand, can bundle several variables together.

-   [Arrays](../lang/array.md)
-   [Structs](../lang/struct.md)

### 1.5 Functions and recursion

Use functions to make programs modular and reduce implementation cost.

Recursion, on the other hand, is a hurdle for beginners; "calling oneself" does not sound so easy to understand, but if you dig into the essence, you will find there is no fundamental difference between "calling oneself" and "calling someone else".

-   [Functions](../lang/func.md)
-   [Recursion & divide and conquer](../basic/divide-and-conquer.md)

## 2 CSP-J entry level

### 2.1 Enumeration and simulation

From now on, you can already use the C++ language to complete some simple tasks, but this is far from enough.

To correctly solve some simple problems, you need to learn to implement code by enumerating or simulating the logic in your mind. This does not look very efficient, but it is sometimes very useful.

-   [Enumeration](../basic/enumerate.md)
-   [Simulation](../basic/simulate.md)

### 2.2 Recursion and divide and conquer

Recursion refers to a method in which a function definition continually calls itself; divide and conquer is the operation of continually decomposing a problem into several subproblems, solving them, and merging.

-   [Recursion & divide and conquer](../basic/divide-and-conquer.md)

### 2.3 Strings

When doing informatics problems, a data type you often encounter is the string; you need to learn some STL functions for manipulating strings. Of course, simulation is also a good way to solve string problems.

-   [String basics](../string/basic.md)
-   [STL functions](../string/lib-func.md)

### 2.4 Sorting

When you have a group of data, how to turn it from unordered to ordered is also a very important problem. When you have no idea, you might as well consider sorting the array. This is also the foundation of many algorithms to come.

There are quite a few sorting methods, but they are not hard to remember once understood.

-   [Introduction to sorting](../basic/sort-intro.md)
-   [Selection sort](../basic/selection-sort.md)
-   [Bubble sort](../basic/bubble-sort.md)
-   [Insertion sort](../basic/insertion-sort.md)
-   [Counting sort](../basic/counting-sort.md)
-   [Radix sort](../basic/radix-sort.md)
-   [Quicksort](../basic/quick-sort.md)
-   [Merge sort](../basic/merge-sort.md)
-   [Heapsort](../basic/heap-sort.md)
-   [Bucket sort](../basic/bucket-sort.md)
-   [Sorting-related STL](../basic/stl-sort.md)

In the NOI syllabus, the entry level only requires learning selection, bubble, and insertion sort—three sorting algorithms in total—but the rest are not very hard either and may be involved in the preliminary round, so they are listed together.

### 2.5 Binary search and binary lifting

Binary search essentially applies the idea of divide and conquer, continually reducing the size of the search range until the answer is found. But note that this search method must be applied to an ordered data structure.

-   [Binary search](../basic/binary.md)

Binary lifting is different: it continually doubles, turning processing in the linear domain into logarithmic, greatly optimizing time complexity. (This topic requires a bit of mathematical foundation; it is not a big problem to skip it for now.)

-   [Binary lifting](../basic/binary-lifting.md)

### 2.6 Search

In the entry group, search problems often appear in maze-type problems, which generally have map-type data; in addition, search is also very commonly used to efficiently enumerate and construct valid solutions, and can also be used to grind out partial credit.

#### 2.6.1 Depth-first search (DFS)

Depth-first search refers to an algorithm that conveniently implements brute-force enumeration using recursive functions; it has some similarities with the DFS algorithm in graph theory, but is not entirely the same.

-   [DFS (search)](../search/dfs.md)

#### 2.6.2 Breadth-first search (BFS)

By designing each state as a vertex in a graph, one can carry out a carpet-style search.

-   [BFS (search)](../search/bfs.md)

#### 2.6.3 Search optimization

Many problems can be solved with DFS, but the complexity of this algorithm obviously cannot pass. Therefore, some optimizations are needed to make it run faster. Such optimizations, which reduce attempts that cannot possibly succeed, are called "pruning". Optimizations related to BFS are more flexible, but the basic idea is the same as here.

-   [DFS pruning optimization](../search/opt.md)

### 2.7 Introduction to data structures

#### 2.7.1 Linear data structures

Arrays, linked lists, queues, and stacks are all linear structures. Cleverly using these structures can accomplish quite a few convenient things.

-   [Stack](../ds/stack.md)
-   [Queue](../ds/queue.md)
-   [Linked list](../ds/linked-list.md)

#### 2.7.2 Complex data structures

-   [Trees and binary trees](../graph/tree-basic.md)
-   [Concept of graphs](../graph/concept.md)
-   [Storing graphs](../graph/save.md)

### 2.8 Introduction to dynamic programming

Dynamic programming (DP) is a method for solving complex problems by decomposing the original problem into relatively simple subproblems.

Since dynamic programming is not a specific algorithm but a method for solving particular problems, it appears in all kinds of data structures, and the types of problems related to it are also more varied.

-   [Introduction to dynamic programming](../dp/index.md)

#### 2.8.1 The knapsack problem

That is, given a knapsack with limited capacity, choose to put in several items with capacities and values, and solve for how to place them so that the total value is maximized. This is the first hurdle that blocks many OIers; from here, algorithms become somewhat hard to understand.

-   [Knapsack DP](../dp/knapsack.md)

#### 2.8.2 Linear dynamic programming

In dynamic programming, one of the hardest parts is designing the state, which requires construction-related techniques. Once you have written the state and the state-transition equation, completing a dynamic-programming problem is not hard.

-   [Construction](../basic/construction.md)
-   [Dynamic programming basics](../dp/basic.md)

Memoized search is a search implementation that avoids repeatedly traversing the same state by recording the information of states already traversed. Some problems can also use memoized search to reduce the difficulty of thinking.

Because memoized search ensures each state is visited only once, it is also a common way to implement dynamic programming.

-   [Memoized search](../dp/memo.md)

#### 2.8.3 Complex dynamic programming

Interval dynamic programming is an extension of linear dynamic programming; when it divides the problem in stages, it has a lot to do with the order in which elements appear within a stage and which elements from the previous stage they are merged from.

-   [Interval DP](../dp/interval.md)

### 2.9 Mathematics

#### 2.9.1 Big-number algorithms

What if even long long (or int64) is not enough? Use big-number algorithms. Essentially it just simulates the four arithmetic operations.

-   [Big-number computation](../math/bignum.md)

#### 2.9.2 Base conversion

In computers, besides binary, octal and hexadecimal are also relatively commonly used. Sometimes learning to use the right base is a great help in solving problems.

-   [Number bases](../math/numeral-sys/base.md)

#### 2.9.3 Bit operations

Bit operations are operations based on the binary representation of integers. Since computers internally store data in binary, bit operations are quite fast.

There are 6 basic bit operations in total: bitwise AND, bitwise OR, bitwise XOR, bitwise NOT, left shift, and right shift.

-   [Bit operations](../math/bit.md)

#### 2.9.4 Number theory

-   [Number-theory basics](../math/number-theory/basic.md)
-   [Primes](../math/number-theory/prime.md)
-   [Sieve methods](../math/number-theory/sieve.md)
-   [Greatest common divisor](../math/number-theory/gcd.md)
-   [Euler's totient function](../math/number-theory/euler-totient.md)
-   [Prime factorization](../math/number-theory/pollard-rho.md)

#### 2.9.5 Combinatorial counting

-   [Permutations and combinations](../math/combinatorics/combination.md)
-   [Pigeonhole principle](../math/combinatorics/drawer-principle.md)
-   [Inclusion–exclusion principle](../math/combinatorics/inclusion-exclusion-principle.md)

***

At this point, you have finished learning all the algorithms within the scope of the entry group; but to master them, you need to keep doing a sufficient number of problems to consolidate the knowledge you have learned.
