author: Persdre

Prerequisite knowledge: [clique](./concept.md)

## Introduction

In computer science, the clique problem refers to the computational problem of finding cliques (subsets of vertices that are all pairwise adjacent, also called complete subgraphs) in a given graph.

The clique problem also manifests in real life. For example, consider a social network, where the points of the graph represent users, and an edge of the graph represents that the two users it connects know each other. Then, when we find a clique, we find a group of people who all know each other.

If we want to find the largest group of people who all know each other in this social network, then we need to use a maximum clique search algorithm.

We have already introduced the concept of a [maximal clique](./concept.md); a maximum clique refers to the maximal clique with the most vertices.

## Explanation

The idea is to use recursion and backtracking, using a list to store vertices; each time a vertex is added in, check whether these vertices are still in one clique. If after adding this vertex it can no longer be a clique, then backtrack to a position that satisfies the condition, and add other vertices again.

The reason for adopting the backtracking strategy is that we do not know whether a certain vertex $v$ is **ultimately** a member of the maximum clique. If the recursive algorithm chooses $v$ as a member of the maximum clique but does not find the maximum clique, then it should backtrack, and look for a solution of the maximum clique without $v$.

## Procedure

The **Bron–Kerbosch** algorithm optimizes the implementation of this idea. Its basic form recursively searches by giving three sets: $R$, $P$, $X$. The steps are as follows:

1.  Initialize the sets $R,X$ to be empty respectively, and the set $P$ to be the set of all points in the graph.
2.  Each time take a vertex $v$ from the set $P$; when there is no vertex in the set, there are two cases:
    1.  The set $R$ is a maximal clique, at which point the set $X$ is empty
    2.  There is no maximal clique, at which point backtrack
3.  For each vertex $v$ taken from the set $P$, there is the following handling:
    1.  Add vertex $v$ to the set $R$, then recurse on the sets $R,P,X$
    2.  Delete vertex $v$ from the set $P$, and add vertex $v$ to the set $X$
    3.  If the sets $P,X$ are both empty, then the set $R$ is a maximal clique

This method can also be further optimized. In order to save time and let the algorithm backtrack faster, we can search by setting a pivot vertex. Another optimization idea is to sort all points at the beginning, and enumerate in index order to prevent duplication.

## Implementation

### Pseudocode

```text
R := {}
P := node set of G 
X := {}

BronKerbosch1(R, P, X):
    if P and X are both empty:
        report R as a maximal clique
    for each vertex v in P:
        BronKerbosch1(R ⋃ {v}, P ⋂ N(v), X ⋂ N(v))
        P := P \ {v}
        X := X ⋃ {v}
```

### C++ implementation

??? note "Implementation code"
    ```cpp
    --8<-- "docs/graph/code/max-clique/max-clique_1.cpp"
    ```

## Example problems

???+ note "[POJ 2989: All Friends](http://poj.org/problem?id=2989)"
    Problem summary: Given $n$ people, among whom there are $m$ pairs of friends, find the number of maximal cliques.

Idea: A template problem, requiring the Bron–Kerbosch algorithm.

Pseudocode:

```text
 BronKerbosch(All, Some, None):  
     if Some and None are both empty:  
         report All as a maximal clique // all points have been selected, and there are no points that cannot be selected, so accumulate the answer  
     for each vertex v in Some: // enumerate every element in Some  
         BronKerbosch1(All ⋃ {v}, Some ⋂ N(v), None ⋂ N(v))   
         // add v to All; obviously only people who are friends with v can be candidates, and in None only those who are friends with v will affect what follows  
         Some := Some - {v} // already searched, delete from Some, add to None  
         None := None ⋃ {v} 
```

In order to save time and let the algorithm backtrack faster, we can optimize by setting a pivot vertex $v$.

We know that in the above algorithm there must be many processes of repeatedly computing previously-computed maximal cliques and then backtracking.

Taking the three sets $R$, $P$, $X$ mentioned earlier as an example:

We consider the following problem. Take a point $u$ in the set $P\cup X$; to form a maximal clique with the set $R$, the point taken must be a point in $P\cap N(u)$ ($N(u)$ represents the points adjacent to $u$).

If after taking $u$ we then take a point $v$ adjacent to $u$ which can also be added to the maximal clique, then we only need to take $u$. Doing so can reduce the repeated computation of $v$ afterward. Afterward, we only need to take points not adjacent to $u$.

The C++ code implementation after adding the optimization:

??? note "Implementation code"
    ```cpp
    --8<-- "docs/graph/code/max-clique/max-clique_2.cpp"
    ```

## Exercises

-   [ZOJ 1492 Maximum Clique](https://pintia.cn/problem-sets/91827364500/exam/problems/type/7?page=4&problemSetProblemId=91827364991)
-   [POJ 1419 Undirected graph maximum clique](http://poj.org/problem?id=1419)
-   [POJ 1129 Broadcast station](http://poj.org/problem?id=1129)

## References

-   [Clique problem - Wikipedia](https://en.wikipedia.org/wiki/Clique_problem)
-   [Maximal cliques and maximum cliques of undirected graphs (Bron–Kerbosch algorithm)](https://blog.csdn.net/yo_bc/article/details/77453478)
-   [The maximum clique problem——Bron–Kerbosch algorithm](https://hallelujahjeff.github.io/2018/04/12/34/)
-   [The maximum clique problem](https://www.cnblogs.com/zhj5chengfeng/archive/2013/07/29/3224092.html)
