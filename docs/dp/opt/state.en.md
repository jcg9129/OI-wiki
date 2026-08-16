author: Marcythm, partychicken, Xeonacid, hhc0001

## Overview

When optimizing DP, we can not only start from the transition process to speed up the transition. Sometimes we can also start from the state definition, achieving a complexity optimization by changing the way the state is designed.

What is rather troublesome is that most of these optimizations are not general, i.e. they cannot be applied to many problems in a routine manner. Therefore, the following starts from specific examples, striving to provide inspiration on approach, hopefully of some help to the reader.

## Example 1

???+ note "Statement"
    Given two strings $A,B$ of lengths $n,m$ respectively consisting only of lowercase letters, find the longest common subsequence of $A,B$. ($n\le 10^6,m\le 10^3$)

### The naive solution

You solve it at a glance—isn't this a template?

Define the state $f_{i,j}$ as the longest common subsequence of the first $i$ characters of $A$ and the first $j$ characters of $B$; then

$$
f_{i,j}=
\begin{cases}
\max(f_{i-1,j},f_{i,j-1}) & ,A_i \neq B_j \\
f_{i-1,j-1}+1 & ,A_i = B_j 
\end{cases}
$$

The time complexity of the above approach is $O(nm)$, which cannot pass this problem.

### A better solution

Thinking carefully, we discover a property: the final answer will not exceed $m$.

Thinking carefully again, we find that LCS satisfies a greedy property.

Change the state definition: let $f_{i,j}$ be the shortest prefix length of $A$ whose longest common subsequence with the first $i$ characters of $B$ has length $j$ (that is, swap the answer of the naive approach with the first-dimension state).

By preprocessing the next occurrence position of each of $a,b,\cdots,z$ for each position of $A$, we can perform $O(1)$ forward transitions.

Complexity $O(m^2+26n)$, which can pass this problem.

## Example 2

???+ note "Statement"
    Given an unweighted directed graph with $n$ vertices, determine whether the graph has a Hamiltonian cycle. ($2\le n\le 20$)

### The naive solution

Seeing the data range, we consider bitmask DP.

Let $f_{s,i}$ denote whether, starting from vertex $1$ and passing only through vertices in the vertex set $s$, we can reach vertex $i$. Let $g$ be the adjacency matrix of the original graph. Then

$$
f_{s, i} = \bigvee_{j\in s, j\neq i}f_{s \setminus \{i\}, j}\wedge g_{j, i} \left(i\in s\right)
$$

Time complexity $O(n^2 \times 2^n)$; written nicely it might pass, but it is not elegant.

### A better solution

In the above state design, each $dp$ value represents only a `bool`, which makes us feel it is a bit wasteful.

We can consider, for each state $s$, compressing $f_{s,1},f_{s,2},\dots,f_{s,n}$ into a single `int`, and we find that we can likewise compress the adjacency matrix and perform an $O(1)$ transition.

Time complexity $O(n^2/w\times 2^n)$, which can pass this problem, where $w$ is the number of bits of an `int`.

## Example 3

???+ note "Statement"
    A conventional knapsack problem. $n$ is the number of items, $m$ is the knapsack capacity, $v_i, w_i$ are the volume and value of the $i$-th item, $1 \le n \le 10^3$, $1 \le m, v_i \le \color{red}{10^{18}}$, $1 \le \sum w_i \le 10^3$.

### The naive solution

This is a template knapsack problem.

Define the state $f_{i, j}$ as the maximum total value after selecting the first $i$ items with $j$ capacity currently packed in the knapsack.

We easily get $f_{i, j} = \max(f_{i - 1, j}, f_{i - 1, j - v_i} + w_i)$.

$v_i \le 10^{18}$, so this cannot pass the problem.

### A better solution

Swap the answer and the second dimension of the state: let $f_{i, j}$ be the minimum total volume after selecting the first $i$ items with the items currently in the knapsack **having value $j$**.

Again, we easily get $f_{i, j} = \min(f_{i - 1, j}, f_{i - 1, j - w_i} + v_i)$.

Note that after changing the second dimension of the state, the transition must change accordingly.

Time complexity $O(n \sum w_i)$, which can pass this problem.
