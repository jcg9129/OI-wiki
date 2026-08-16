author: Ir1d, CBW2007, ChungZH, xhn16729, Xeonacid, tptpp, hsfzLZH1, ouuan, Marcythm, HeRaNO, greyqz, Chrogeek, partychicken, zhb2000, xyf007, Persdre, XiaoSuan250, hhc0001, ZhangZhanhaoxiang, Taoran\_01

This page mainly introduces the basic idea of dynamic programming, as well as the design approach for states and state-transition equations in dynamic programming, to help beginners get a preliminary understanding of dynamic programming.

The other pages in this part introduce methods for building dynamic-programming models in various types of problems, as well as some dynamic-programming optimization techniques.

## Introduction

???+ note "[\[IOI1994\] The Triangle](https://www.luogu.com.cn/problem/P1216)"
    Given a number triangle with $r$ rows ($r \leq 1000$), you need to find a path from the topmost point ending anywhere at the bottom that maximizes the sum of the numbers the path passes through. Each step you can move to the point at the lower-left or lower-right of the current point.
    
    ```plain
            7 
          3   8 
        8   1   0 
      2   7   4   4 
    4   5   2   6   5 
    ```
    
    In the example above, the optimal path is $7 \to 3 \to 8 \to 7 \to 5$.

The simplest and crudest idea is to try all paths. Because the number of paths is on the order of $O(2^r)$, this approach is unacceptable.

Note the following fact: for an optimal path, every step of its decisions is optimal.

Take the optimal path mentioned in the example. Considering only the first four steps $7 \to 3 \to 8 \to 7$, there is no path from the top to the 2nd number of row $4$ with a larger weight.

For each point, its next decision has only two options: go to the lower-left or the lower-right (if they exist). Therefore we only need to record the maximum weight of the current point, and use this maximum weight to make the next decision, updating the maximum weight of subsequent points.

Doing this has another benefit: we have successfully reduced the size of the problem, splitting one problem into several smaller problems. To obtain the optimal scheme from the top to row $r$, we only need to know the information of the optimal scheme from the top to row $r-1$.

At this point there is still a problem: the overlapping parts between subproblems are numerous, the same subproblem may be visited repeatedly, and efficiency is still not high. The way to solve this problem is to store the solution of each subproblem, restricting the visiting order via memoization to ensure each subproblem is visited only once.

The above are some basic ideas of dynamic programming. Below we introduce the idea of dynamic programming more systematically.

## The principles of dynamic programming

A problem that can be solved with dynamic programming needs to satisfy three conditions: optimal substructure, no aftereffect (the Markov property), and overlapping subproblems.

### Optimal substructure

Having optimal substructure may also mean the problem is suitable for a greedy method.

Be sure to ensure that we have examined all the subproblems used in the optimal solution.

1.  Prove that the first component of the problem's optimal solution is making a choice;
2.  For a given problem, assume among its possible first choices that you already know which choice yields the optimal solution. You do not care for now how this choice is specifically obtained, only assume it is already known;
3.  Given the choice for obtaining the optimal solution, determine which subproblems this choice produces and how best to characterize the subproblem space;
4.  Prove that, as a component that constitutes the original problem's optimal solution, each subproblem's solution is its own optimal solution. The method is proof by contradiction: consider that a certain subproblem's solution is not its own optimal solution; then you could replace the current non-optimal solution in the original problem's solution with that subproblem's optimal solution, obtaining a better solution to the original problem, contradicting the assumption that it is the original problem's optimal solution.

Keep the subproblem space as simple as possible, expanding it only when necessary.

The differences in optimal substructure manifest in two aspects:

1.  How many subproblems the original problem's optimal solution involves;
2.  How many choices need to be examined when determining which subproblems the optimal solution uses.

Each vertex in the subproblem graph corresponds to a subproblem, and the choices to be examined correspond to the edges incident to the subproblem vertices.

### No aftereffect

An already-solved subproblem will not be affected by subsequent decisions.

### Overlapping subproblems

If there are a large number of overlapping subproblems, we can use space to store the solutions of these subproblems, avoiding repeatedly solving the same subproblem, thereby improving efficiency.

### Basic approach

For a problem that can be solved with dynamic programming, we generally use the following approach:

1.  Divide the original problem into several **stages**; each stage corresponds to several subproblems, and extract the features of these subproblems (called the **state**);
2.  Find the possible **decisions** for each state, or the ways of transitioning between states (described in mathematical language as the **state-transition equation**).
3.  Solve each stage's problem in order.

Understood with graph-theory ideas, we build a [directed acyclic graph](../graph/dag.md), where each state corresponds to a node in the graph and decisions correspond to edges between nodes. Then the problem turns into a problem of finding the longest (shortest) path on a DAG (see: [DP on a DAG](./dag.md)).

## Longest common subsequence

???+ note "The longest common subsequence problem"
    Given a sequence $A$ of length $n$ and a sequence $B$ of length $m$ ($n,m \leq 5000$), find a longest sequence that is both a subsequence of $A$ and a subsequence of $B$.

For the definition of a subsequence, refer to [subsequence](../string/basic.md). A brief example: the common subsequences of the strings `abcde` and `acde` are `a`, `c`, `d`, `e`, `ac`, `ad`, `ae`, `cd`, `ce`, `de`, `acd`, `ade`, `ace`, `cde`, `acde`, and the length of the longest common subsequence is 4.

Let $f(i,j)$ denote the length of the longest common subsequence when considering only the first $i$ elements of $A$ and the first $j$ elements of $B$; finding this length is the **subproblem**. $f(i,j)$ is what we call the **state**, and $f(n,m)$ is the final state to reach, i.e. the desired result.

For each $f(i,j)$, there are three decisions: if $A_i=B_j$, it can be appended to the end of the common subsequence; the other two decisions are to skip $A_i$ or $B_j$. The state-transition equation is as follows:

$$
f(i,j)=\begin{cases}f(i-1,j-1)+1&A_i=B_j\\\max(f(i-1,j),f(i,j-1))&A_i\ne B_j\end{cases}
$$

You can refer to [SourceForge's LCS interactive web page](http://lcs-demo.sourceforge.net/) to better understand the implementation process of LCS.

???+ example "Reference implementation"
    === "C++"
        ```cpp
        --8<-- "docs/dp/code/basic/lcs.cpp:core"
        ```
    
    === "Python"
        ```cpp
        --8<-- "docs/dp/code/basic/lcs.py:core"
        ```

The time complexity of this approach is $O(nm)$.

In addition, this problem has an $O\left(\dfrac{nm}{w}\right)$ algorithm[^ref1]. Interested students can explore it on their own.

## Longest non-decreasing subsequence

???+ note "The longest non-decreasing subsequence problem"
    Given a sequence $a$ of length $n$ ($n \leq 5000$), find a longest subsequence of $a$ such that each element of the subsequence is not smaller than the previous one.

### Algorithm one

Let $f(i)$ denote the length of the longest non-decreasing subsequence ending at $a_i$; then the desired answer is $\max_{1 \leq i \leq n} f(i)$.

When computing $f(i)$, try appending $a_i$ to other longest non-decreasing subsequences to update the answer. So we can write the following state-transition equation: $f(i)=\max_{1 \leq j < i,~a_j \leq a_i} (f(j)+1)$.

???+ example "Reference implementation"
    === "C++"
        ```cpp
        --8<-- "docs/dp/code/basic/lis-1.cpp:core"
        ```
    
    === "Python"
        ```python
        --8<-- "docs/dp/code/basic/lis-1.py:core"
        ```

It is easy to see that the time complexity of this algorithm is $O(n^2)$.

### Algorithm two

When the range of $n$ is expanded to $n \leq 10^5$, the first approach is not fast enough; below we give an $O(n \log n)$ approach.

Consider the previously defined state $(i, l)$, indicating that the longest non-decreasing subsequence ending at the $i$-th element of the sequence has length $l$. Unlike the previous method of processing states for a fixed $i$, here we directly determine whether $(i, l)$ is valid:

-   The initial state $(1,1)$ must be valid.
-   For any $(i, l)$, if there exists $j < i$ with $(j, l-1)$ valid and $a_j \le a_i$, then $(i, l)$ is valid.

Finally, we only need to find the valid state $(i,l)$ with the largest $l$ to obtain the length of the longest non-decreasing subsequence.

Let the original sequence be $a_1, \cdots, a_n$, and define an array $d$, whose $x$-th position denotes the minimum of the last elements of non-decreasing subsequences of length $x$. Initially the sequence is empty. Let $i$ go from $1$ to $n$, computing in turn the length of the longest non-decreasing subsequence of the first $i$ elements. For the current element $a_i$:

-   If $a_i$ is greater than or equal to the last element of the sequence $d$, directly insert the element $a_i$ at the end of the sequence $d$.
    -   Explanation: if $a_i$ is greater than or equal to the last element of the current longest subsequence, it means there is a non-decreasing subsequence that can be extended by $a_i$. Not inserting it would break optimality.
-   If $a_i$ is strictly smaller than the last element of $d$, find the **first** element greater than it and replace it with $a_i$.
    -   Explanation: inserting directly at the end would break the monotonicity of $d$; the replacement operation ensures that the last element of each length is as small as possible, thereby leaving more possibilities for subsequent elements.
    -   Optimization: because $d$ is monotonically non-decreasing, binary search can be used to directly find the insertion position of the element, reducing the overall complexity to $O(n\log n)$ instead of the brute-force $O(n^2)$.

If you also need to output the specific longest non-decreasing subsequence, you can additionally maintain an array $d'_x$, denoting the position of the minimum last element in a non-decreasing subsequence of length $x$ (if there are several, any one can be chosen). Specifically, when inserting element $a_i$ into $d_x$, simultaneously update $d'_x$ to $i$. At the same time, you need to record $i$'s optimal predecessor $p_i$ as $d'_{x-1}$. Finally, starting from any maximum-length state and backtracking along the predecessors $p_i$, you obtain the complete subsequence.

???+ example "Reference implementation"
    === "C++"
        ```cpp
        --8<-- "docs/dp/code/basic/lis-2.cpp:core"
        ```
    
    === "Python"
        ```python
        --8<-- "docs/dp/code/basic/lis-2.py:core"
        ```

The time complexity of this algorithm is $O(n\log n)$. The time complexity of outputting the answer is $O(\textit{ans})$.

???+ tip "Note"
    For the longest **strictly increasing** subsequence problem, similarly, we can let $d_i$ denote the minimum of the last elements of all longest strictly increasing subsequences of length $i$.
    
    Note that in step 2, if $a_i \leq d_{len}$, since adjacent elements in a longest strictly increasing subsequence cannot be equal, we need to find the **first** element in the $d$ sequence that is **not smaller than** $a_i$ and replace it with $a_i$.
    
    In implementation (taking C++ as an example), the `upper_bound` function needs to be changed to `lower_bound`.

## References and notes

-   [Detailed explanation of the nlogn algorithm for the longest non-decreasing subsequence - lvmememe - cnblogs](https://www.cnblogs.com/itlqs/p/5743114.html)

[^ref1]: [Computing the longest common subsequence with bit operations - -Wallace- - cnblogs](https://www.cnblogs.com/-Wallace-/p/bit-lcs.html)
