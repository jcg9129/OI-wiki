## Definition

A DAG is a [directed acyclic graph](../graph/dag.md); the binary relations in some practical problems can all be modeled with a DAG, thereby turning these problems into longest (shortest) path problems on a DAG.

## Explanation

Take this problem as an example to analyze the process of DAG modeling.

???+ note "Example [UVa 437 The Tower of Babylon](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=378)"
    There are $n (n\leqslant 30)$ kinds of blocks; the lengths of their three edges are known, and there are infinitely many of each kind. You are required to select some cuboids and stack them into a column as high as possible (each block may choose one of its edges as its height), such that the length and width of each block's base are strictly smaller than the length and width of the base of the block below it. Find the maximum height of the tower.

## Process

### Building the DAG

Since the length and width of each block's base are strictly smaller than the length and width of the base of the block below it, it is not hard to use such a relationship as the basis for building the graph, and this problem thus turns into a longest-path problem.

That is, if block $j$ can be placed on block $i$, then there is an edge $(i, j)$ between $i$ and $j$, and the edge weight is the height chosen for block $j$.

Another issue in this problem is that each block's height has three choices; how is it more appropriate to build the graph?

We might as well decompose each block into three stacking ways, i.e. decompose one block into three blocks, each decomposed block choosing a different height.

The initial starting point is the ground; the ground's base is infinitely large, so the ground can reach any block—of course, we do not need to specifically write infinity when writing the program.

Suppose there are two blocks with edges $31, 41, 59$ and $33, 83, 27$ respectively; then the whole DAG should be as shown in the figure below.

![](./images/dag-babylon.png)

The blue solid-line boxes in the figure represent a group of blocks obtained by decomposing one block; the reason $\{\}$ is used to denote the base edge lengths is that once a block chooses its height, its base edge lengths are unordered.

The yellow dashed-line boxes in the figure represent the repeatedly-computed part, which can be avoided using [memoized search](./memo.md).

### Transition

The problem asks for the maximum height of the tower, which has been turned into a longest-path problem; its starting point was noted above as the ground, so what about the endpoint? Clearly the endpoint is naturally determined: it is when no other block can be placed on a certain block.

Below we begin considering the transition equation.

Let $d(i,r)$ denote the maximum height when the $i$-th block is at the bottom and the $r$-th stacking way is used. Then we have the following transition equation:

$$
d(i, r) = \max\left\{d(j, r') + h\right\}
$$

where $j$ is all those blocks that can be placed on top when block $i$ is stacked in way $r$, $r'$ corresponds to $j$'s placement way at that time, and $h$ corresponds to the height when block $i$ uses the $r$-th stacking way.

??? note "Implementation"
    ```cpp
    --8<-- "docs/dp/code/dag/dag_1.cpp"
    ```
