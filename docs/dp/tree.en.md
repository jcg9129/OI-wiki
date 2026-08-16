author: aaron20100919

Tree DP is DP performed on a tree. Because of the inherent recursive nature of trees, tree DP is generally performed recursively.

## Basics

Take the following problem as an example to introduce the general process of tree DP.

???+ note "Example [Luogu P1352 Ball Without the Boss](https://www.luogu.com.cn/problem/P1352)"
    A university has $n$ employees numbered $1 \sim N$. There are subordinate relationships among them, that is, their relationships are like a tree rooted at the president, where the parent node is the direct superior of the child node. Now there is an anniversary banquet; every time an employee is invited to the banquet, it increases a certain happiness index $a_i$, but if some employee's direct superior comes to the ball, then this employee will absolutely not come to the ball. So please write a program to compute which employees to invite to maximize the happiness index, and find the maximum happiness index.

We let $f(i,0/1)$ denote the optimal solution of the subtree rooted at $i$ (a value of 0 in the second dimension means $i$ does not attend the ball, and 1 means $i$ attends the ball).

For each state, there are two decisions (where $x$ below is a child of $i$):

-   when the superior does not attend the ball, the subordinate may attend or not; in this case $f(i,0) = \sum\max \{f(x,1),f(x,0)\}$;
-   when the superior attends the ball, the subordinates all do not attend; in this case $f(i,1) = \sum{f(x,0)} + a_i$.

We can update the optimal solution of the current node when returning to the previous level via DFS.

```cpp
--8<-- "docs/dp/code/tree/tree_1.cpp"
```

Usually, the tree-DP state is generally the optimal solution of the current node. First DFS to traverse all optimal solutions of the subtrees, then pass them up to the parent node of the subtrees to transition; finally the value of the root node is the desired optimal solution.

### Exercises

-   [HDU 2196 Computer](https://acm.hdu.edu.cn/showproblem.php?pid=2196)

-   [POJ 1463 Strategic game](http://poj.org/problem?id=1463)

-   [\[POI2014\] FAR-FarmCraft](https://www.luogu.com.cn/problem/P3574)

## Knapsack on a tree

The knapsack problem on a tree, simply put, is the combination of the knapsack problem and tree DP.

???+ note "Example [Luogu P2014 CTSC1997 Course Selection](https://www.luogu.com.cn/problem/P2014)"
    There are $n$ courses; the $i$-th course is worth $a_i$ credits, and each course has zero or one prerequisite; a course with a prerequisite requires finishing its prerequisite before it can be studied.
    
    A student wants to study $m$ courses; find the maximum number of credits they can obtain.
    
    $n,m \leq 300$

The characteristic that each course has at most one prerequisite is similar to the characteristic that a node in a rooted tree has at most one parent node.

Therefore we can think of building a tree based on this property, so that all courses form a forest structure. For convenience, we can add a new course worth $0$ credits (let this course's number be $0$) as the prerequisite of all courses with no prerequisite, thereby turning the forest into a tree rooted at course $0$.

We let $f(u,i,j)$ denote the maximum credits in the subtree rooted at node $u$ when the first $i$ subtrees of node $u$ have been traversed and $j$ courses have been selected.

The transition process combines the characteristics of tree DP and [knapsack DP](./knapsack.md): we enumerate each child $v$ of node $u$, simultaneously enumerate how many courses are selected in the subtree rooted at $v$, and merge the subtree's result into $u$.

Let the number of children of node $x$ be $s_x$ and the size of the subtree rooted at $x$ be $\textit{siz}_x$; we can write the following state-transition equation:

$$
f(u,i,j)=\max_{v,k \leq j,k \leq \textit{siz}_v} f(u,i-1,j-k)+f(v,s_v,k)
$$

Note the several restriction conditions in the above state-transition equation; these restriction conditions ensure that some meaningless states are not visited.

The second dimension of $f$ can be easily omitted with a rolling array; note that in this case $j$ must be enumerated in reverse order.

It can be proven that the time complexity of this approach is $O(nm)$[^note1].

??? note "Reference code"
    ```cpp
    --8<-- "docs/dp/code/tree/tree_2.cpp"
    ```

### Exercises

-   [「CTSC1997」Course Selection](https://www.luogu.com.cn/problem/P2014)

-   [「JSOI2018」Infiltration Operation](https://loj.ac/problem/2546)

-   [「SDOI2017」Apple Tree](https://loj.ac/problem/2268)

-   [「Codeforces Round 875 Div. 1」Problem D. Mex Tree](https://codeforces.com/contest/1830/problem/D)

## Rerooting DP

The rerooting DP problem in tree DP is also called the two-pass scan; it usually does not specify the root node, and the change of the root node affects some values, such as the sum of child-node depths, the sum of vertex weights, etc.

Two DFS passes are usually needed: the first DFS preprocesses information such as depth and vertex-weight sum, and the second DFS starts running the rerooting dynamic programming.

Next we use some examples to familiarize you with this content.

???+ note "Example [\[POI2008\] STA-Station](https://www.luogu.com.cn/problem/P3478)"
    Given a tree with $n$ nodes, find a node such that when this node is the root, the sum of the depths of all nodes is maximized.

Let $u$ be the current node and $v$ be a child of the current node. First we need to use $s_i$ to denote the number of nodes in the subtree rooted at $i$, and $s_u=1+\sum s_v$. Clearly we need one DFS to compute all $s_i$; this DFS is the preprocessing, and we obtain the total number of nodes in a node's subtree when that node is the root.

Consider the state transition; this is where "rerooting" is embodied. Let $f_u$ be the sum of the depths of all nodes when $u$ is the root.

$f_v\leftarrow f_u$ can embody rerooting, i.e. transitioning from $u$ as the root to $v$ as the root. Clearly, during the rerooting transition, taking $v$ as the root or $u$ as the root causes the depths of the nodes in the subtree to change. Specifically:

-   the depths of all nodes in $v$'s subtree decrease by one, so the total depth sum decreases by $s_v$;

-   the depths of all nodes not in $v$'s subtree increase by one, so the total depth sum increases by $n-s_v$;

From these two conditions we can derive the state-transition equation $f_v = f_u - s_v + n - s_v=f_u + n - 2 \times s_v$.

So in the second DFS traversing the whole tree and transitioning $f_v=f_u + n - 2 \times s_v$, we can find the depth sum when each node is the root. Finally we only need to traverse all root nodes' depth sums once to find the answer.

??? note "Reference code"
    ```cpp
    --8<-- "docs/dp/code/tree/tree_3.cpp"
    ```

### Exercises

-   [Atcoder Educational DP Contest, Problem V, Subtree](https://atcoder.jp/contests/dp/tasks/dp_v)

-   [Educational Codeforces Round 67, Problem E, Tree Painting](https://codeforces.com/contest/1187/problem/E)

-   [POJ 3585 Accumulation Degree](http://poj.org/problem?id=3585)

-   [\[USACO10MAR\] Great Cow Gathering G](https://www.luogu.com.cn/problem/P2986)

-   [CodeForce 708C Centroids](http://codeforces.com/problemset/problem/708/C)

## References and notes

[^note1]: [Complexity Proof of Subtree-Merging Knapsack-Type DP - LYD729's CSDN blog](https://blog.csdn.net/lyd_7_29/article/details/79854245)
