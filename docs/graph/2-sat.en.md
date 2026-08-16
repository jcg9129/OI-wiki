author: chu-yuehan

SAT is the abbreviation for the Satisfiability problem. Its general form is the k-satisfiability problem, abbreviated k-SAT. And when $k>2$ this problem is NP-complete. So we only study the case $k=2$.

## Definition

2-SAT, simply put, is: given $n$ boolean equations, where each equation is related to two variables, such as $a \vee b$, meaning variables $a, b$ satisfy at least one. Then judge whether a feasible scheme exists; obviously there may be multiple choice schemes, and generally a problem only requires finding one. In addition, $\neg a$ denotes the negation of $a$.

## Solution idea

???+ example "[Luogu P4782 「Template」2-SAT](https://www.luogu.com.cn/problem/P4782)"
    There are $n$ boolean variables $x_1\sim x_n$, and there are also $m$ conditions to be satisfied; each condition is of the form "$x_i$ is `true`/`false` or $x_j$ is `true`/`false`". For example "$x_1$ is true or $x_3$ is false", "$x_7$ is false or $x_2$ is false".
    
    The goal of the 2-SAT problem is to assign a value to each variable so that all conditions are satisfied.

Use boolean equations to represent the above problem. Let $a$ denote that $x_a$ is true ($\neg a$ then denotes that $x_a$ is false). If someone's requirements are $a$ and $b$ respectively, i.e. $(a \vee b)$ (variables $a, b$ satisfy at least one). Build a directed graph for these variable relations; then represent $a$ holding or not holding with points in the graph, $\neg a\to b$, $\neg b\to a$, meaning if $a$ **does not hold** then $b$ **must hold**; similarly, if $b$ **does not hold** then $a$ **must hold**. After building the graph, we can use the contraction algorithm to solve the 2-SAT problem.

| Original expression | Graph construction |
| :----------------: | :-----------------------------: |
|   $\neg a \vee b$  | $a \to b$ and $\neg b \to \neg a$ |
|     $a \vee b$     | $\neg a \to b$ and $\neg b \to a$ |
| $\neg a\vee\neg b$ | $a \to \neg b$ and $b \to \neg a$ |

Many 2-SAT problems need to find relations such as if $a$ **does not hold**, then $b$ **holds**.

## Solving

Think about what it means if two points are in the same strongly connected component. From the logical meaning of the edges above, we know: if two points are in the same strongly connected component, then the conditions represented by these two points are **either both satisfied, or both not satisfied**.

After building the graph, we use [Tarjan's algorithm to find SCCs](./scc.md) to judge, for any boolean variable $a$, whether the point representing $a$ holding and the point representing $a$ not holding are in the same SCC (the same condition cannot be both satisfied and not satisfied, or both not satisfied and not-not-satisfied); if so, output no solution, otherwise there is a solution.

When outputting the scheme, the value of a variable can be determined by its topological order in the graph. If the topological order of variable $x$ is after $\neg x$, then take the value of $x$ as true. Applied to the contraction of Tarjan's algorithm, i.e. when the SCC number where $x$ is located is before that of $\neg x$, take $x$ as true. Because Tarjan's algorithm uses a stack when finding strongly connected components, if the topological order presented after running Tarjan's contraction is larger, it is traversed later in Tarjan, and it will be popped from the stack and contracted earlier, so its component number will be smaller; therefore the SCC number found by Tarjan is equivalent to the **reverse topological order**.

The algorithm traverses the whole graph once; since $n$ and $m$ of this graph are of the same order, the complexity of computing the answer is $O(n)$, so the total complexity is $O(n)$.

??? note "Code implementation"
    ```cpp
    --8<-- "docs/graph/code/2-sat/2-sat_3.cpp"
    ```

## Example problems

### Example problem 1

???+ example "[HDU3062 Party](https://acm.hdu.edu.cn/showproblem.php?pid=3062)"
    There are $n$ couples invited to a party; because of the venue problem, only one person of each couple may attend. Among the $2n$ people, there are big conflicts between some people (of course there is no conflict between a couple); two people with a conflict will not appear at the party at the same time. Is it possible for $n$ people to attend at the same time?

According to the analysis above, if the husband in $a_1$ and the wife in $a_2$ do not get along, then we connect an edge between the husband in $a_1$ and the husband in $a_2$, and connect an edge between the wife in $a_2$ and the wife in $a_1$, then contract, color, and judge.

??? note "Reference code"
    ```cpp
    --8<-- "docs/graph/code/2-sat/2-sat_1.cpp"
    ```

### Example problem 2

???+ example "[2018-2019 ACM-ICPC Asia Seoul Regional K TV Show Game](https://codeforces.com/gym/101987/problem/K)"
    There are $k$ lamps, each lamp is red or blue, but initially the color of the lamp is unknown. There are $n$ people, and each person chooses three lamps and guesses the colors of the lamps. A person who guesses the colors of two or more lamps correctly can win a prize. Judge whether there exists a coloring scheme of the lamps such that everyone can get a prize; if so, output a coloring scheme of the lamps.

According to [Wu Yu - "Solving 2-SAT problems by symmetry"](https://github.com/OI-wiki/libs/blob/master/%E9%9B%86%E8%AE%AD%E9%98%9F%E5%8E%86%E5%B9%B4%E8%AE%BA%E6%96%87/%E5%9B%BD%E5%AE%B6%E9%9B%86%E8%AE%AD%E9%98%9F2003%E8%AE%BA%E6%96%87%E9%9B%86/%E4%BC%8D%E6%98%B1--%E7%94%B1%E5%AF%B9%E7%A7%B0%E6%80%A7%E8%A7%A32-SAT%E9%97%AE%E9%A2%98/%E4%BC%8D%E6%98%B1.ppt), we can conclude: if we want to output a feasible solution to a 2-SAT problem, we only need to perform selection and deletion from bottom to top on the DAG obtained after tarjan contraction.

In the specific implementation, this can be achieved by constructing the reverse graph of the DAG and then performing topological sorting on the reverse graph; it can also be achieved, according to the property that after tarjan contraction, the smaller the number of the connected component a node belongs to, the closer the node is to a leaf node, by preferentially selecting nodes whose belonging connected component has a smaller number.

The code for the second implementation method is given below.

??? note "Reference code"
    ```cpp
    --8<-- "docs/graph/code/2-sat/2-sat_2.cpp"
    ```

## Exercises

-   [Luogu P5782 Peace Committee](https://www.luogu.com.cn/problem/P5782)
-   [POJ3683 Priest John's Busiest Day](http://poj.org/problem?id=3683)
