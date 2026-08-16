author: Backl1ght

The AHU algorithm is used to determine whether two rooted trees are isomorphic.

Besides determining tree isomorphism, another common approach is [tree hashing](tree-hash.md).

Prerequisite knowledge: [tree basics](tree-basic.md), [center of gravity of a tree](tree-centroid.md)

It is recommended to read it together with the examples given in the references.

## Definition of tree isomorphism

### Rooted tree isomorphism

For two rooted trees $T_1(V_1,E_1,r_1)$ and $T_2(V_2,E_2,r_2)$, if there exists a bijection $\varphi: V_1 \rightarrow V_2$ such that

$$
\forall u,v \in V_1,(u,v) \in E_1 \iff (\varphi(u),\varphi(v))  \in E_2
$$

**and** $\varphi(r_1)=r_2$ holds, then the rooted trees $T_1(V_1,E_1,r_1)$ and $T_2(V_2,E_2,r_2)$ are said to be isomorphic.

### Unrooted tree isomorphism

For two unrooted trees $T_1(V_1,E_1)$ and $T_2(V_2,E_2)$, if there exists a bijection $\varphi: V_1 \rightarrow V_2$ such that

$$
\forall u,v \in V_1,(u,v) \in E_1 \iff (\varphi(u),\varphi(v))  \in E_2
$$

holds, then the unrooted trees $T_1(V_1,E_1)$ and $T_2(V_2,E_2)$ are said to be isomorphic.

Simply put, if we can, by re-labeling all nodes of tree $T_1$, make tree $T_1$ and tree $T_2$ **completely identical**, then these two trees are said to be isomorphic.

## Transformation of the problem

The unrooted tree isomorphism problem can be transformed into the rooted tree isomorphism problem. The specific method is as follows:

For unrooted trees $T_1(V_1, E_1)$ and $T_2(V_2,E_2)$, first find **all** their centers of gravity respectively.

-   If these two unrooted trees have different numbers of centers of gravity, then these two trees are not isomorphic.
-   If both of these unrooted trees have $1$ center of gravity, denoted as $c_1$ and $c_2$ respectively, then if the rooted tree $T_1(V_1,E_1,c_1)$ and the rooted tree $T_2(V_2,E_2,c_2)$ are isomorphic, then the unrooted trees $T_1(V_1, E_1)$ and $T_2(V_2,E_2)$ are isomorphic, and otherwise not isomorphic.
-   If both of these unrooted trees have $2$ centers of gravity, denoted as $c_1,c'_1$ and $c_2,c'_2$ respectively, then if the rooted tree $T_1(V_1,E_1,c_1)$ and the rooted tree $T_2(V_2,E_2,c_2)$ are isomorphic **or** the rooted tree $T_1(V_1,E_1,c'_1)$ and $T_2(V_2,E_2,c_2)$ are isomorphic, then the unrooted trees $T_1(V_1, E_1)$ and $T_2(V_2,E_2)$ are isomorphic, and otherwise not isomorphic.

So, as long as we solve the rooted tree isomorphism problem, we can transform the unrooted tree isomorphism problem into a rooted tree isomorphism problem according to the above method, and thereby solve the unrooted tree isomorphism problem.

Assuming there is an algorithm that can solve the rooted tree isomorphism problem in $O(\left|V\right|)$, then according to the above method we can also solve the unrooted tree isomorphism problem in $O(\left|V\right|)$ time.

## Naive AHU algorithm

The naive AHU algorithm is based on the bracket sequence.

### Principle 1

We know that a valid bracket sequence corresponds uniquely to a rooted tree, and the bracket sequence of a tree is formed by concatenating the bracket sequences of its subtrees. If we change the concatenation order of the subtree bracket sequences, thereby obtaining a new bracket sequence, then the tree corresponding to the new bracket sequence is isomorphic to the tree corresponding to the original bracket sequence.

### Principle 2

The isomorphism relation of trees is transitive. That is, if $T_1$ and $T_2$ are isomorphic, and $T_2$ and $T_3$ are isomorphic, then $T_1$ and $T_3$ are isomorphic.

### Corollary

Consider the recursive algorithm for finding the bracket sequence of a tree; we concatenate the bracket sequences of subtrees when backtracking. If, during concatenation, we concatenate the lexicographically smaller sequence first, and record the final result as $NAME$.

Taking the $NAME$ of the subtree rooted at node $r$ as the $NAME$ of node $r$, denoted $NAME(r)$, then for rooted trees $T_1(V_1,E_1,r_1)$ and $T_2(V_2,E_2,r_2)$, if $NAME(r_1)=NAME(r_2)$, then $T_1$ and $T_2$ are isomorphic.

### Naming algorithm

???+ note "Implementation"
    $$
    \begin{array}{ll}
    1 & \textbf{Input. } \text{A rooted tree }T\\
    2 & \textbf{Output. } \text{The name of rooted tree }T\\
    3 & \text{ASSIGN-NAME(u)}\\
    4 & \qquad \text{if  } u \text{  is a leaf}\\
    5 & \qquad \qquad \text{NAME(} u \text{) = (0)}\\
    6 & \qquad \text{else }\\
    7 & \qquad \qquad \text{for all child } v \text{ of } u\\
    8 & \qquad \qquad \qquad \text{ASSIGN-NAME(}v\text{)}\\
    9 & \qquad \text{sort the names of the children of }u\\
    10 & \qquad \text{concatenate the names of all children }u\text{ to temp}\\
    11 & \qquad \text{NAME(} u \text{) = (temp)}
    \end{array}
    $$

### AHU algorithm

???+ note "Implementation"
    $$
    \begin{array}{ll}
    1 & \textbf{Input. } \text{Two rooted trees }T_1(V_1,E_1,r_1)\text{ and }T_2(V_2,E_2,r_2) \\
    2 & \textbf{Output. } \text{Whether these two trees are isomorphic}\\
    3 & \text{AHU}(T_1(V_1,E_1,r_1), T_2(V_2,E_2,r_2))\\
    4 & \qquad \text{ASSIGN-NAME(}r_1\text{)}\\
    5 & \qquad \text{ASSIGN-NAME(}r_2\text{)}\\
    6 & \qquad \text{if  NAME}(r_1) = \text{NAME}(r_2)\\
    7 & \qquad \qquad \text{return true}\\
    8 & \qquad \text{else}\\
    10 & \qquad \qquad \text{return false}
    \end{array}
    $$

### Complexity proof

For a rooted tree with $n$ nodes, assuming it is chain-shaped, then the node name length can be at most $n$, so the complexity of the ASSIGN-NAME algorithm is a constant multiple of $1+2+\cdots+n$, i.e. $\Theta(n^2)$. From this, the complexity of the naive AHU algorithm is $O(n^2)$.

## Optimized AHU algorithm

The disadvantage of the naive AHU algorithm is that the length of the tree's $NAME$ may be too long; we can make some optimizations targeting this.

### Principle 1

Divide the tree into levels; the shortest distance from a node at level $i$ to the root is $i$. The $NAME$ of a node at level $i$ can be obtained by concatenating **only** the $NAME$s of the nodes at level $i+1$.

### Principle 2

Within the same level, the $NAME$ of a node can be uniquely identified by its rank within the level.

**Note** that the rank here is with respect to both trees; assuming node $u$ is at level $i$, then the rank of node $u$ equals the number of nodes among all nodes at level $i$ of $T_1$ and $T_2$ whose $NAME$ is smaller than $NAME(u)$.

### Corollary

We can replace a node's original $NAME$ with its rank within the level, and then replace the original concatenation of node $NAME$s with adding elements to an array.

Using integers and arrays to replace strings this way neither affects the correctness of the algorithm nor greatly reduces the complexity of the algorithm.

### Complexity proof

First, note that the total length of the $NAME$s obtained by concatenation at level $i$ is the sum of the degrees of the nodes at level $i$, i.e. the total number of nodes at level $i+1$, denoted below by $L_i$. The next step of the algorithm regards these $NAME$s as strings (arrays) and sorts them, then replaces them with their rank within the level (i.e. re-maps them to a number). The following lemma shows the complexity of sorting $m$ strings with total length $L$:

1.  We can use radix sort to complete the sorting in $O(L+|\Sigma|)$ time, where $|\Sigma|$ is the size of the character set. (There are some implementation details; see the references.)
2.  We can use quicksort to complete the sorting in $O(L \log m)$ time. The general idea of the proof is that the height of the quicksort recursion tree is $O(\log m)$, and the complexity of brute-force comparing two strings of length $\ell_1$ and $\ell_2$ is $O(\min\{\ell_1,\ell_2\})$.

In the AHU algorithm, the character set size of the strings at level $i$ is at most the number of nodes at level $i+1$, i.e. $L_i$, so the complexity of radix sort is linear. According to $\sum_i L_i=O(n)$, and after summing the complexity of each level, we can see that if we use radix sort of strings, then the total complexity of the algorithm is $T(n)=O(n)$. Similarly, if we use quicksort to sort the strings, then $T(n)=O(n \log n)$.

## Example problem

[SPOJ-TREEISO](https://www.spoj.com/problems/TREEISO/en/)

Problem translation: Given two unrooted trees, determine whether the two trees are isomorphic.

???+ note "Reference code"
    ```cpp
    --8<-- "docs/graph/code/tree-ahu/tree-ahu_1.cpp"
    ```

## References

Most of the content of this article is translated from [Paper](http://wwwmayr.in.tum.de/konferenzen/Jass08/courses/1/smal/Smal_Paper.pdf) and [Slide](https://logic.pdmi.ras.ru/~smal/files/smal_jass08_slides.pdf). The proofs in the references are more comprehensive and rigorous; this article has made certain simplifications.

For the complexity analysis of the AHU algorithm, and the linear-time radix sort algorithm for strings, see Section 3.2 Radix sorting of The Design and Analysis of Computer Algorithms, and Example 3.2 therein.
