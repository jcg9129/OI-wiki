author: DanJoshua, opsiff, yzy-1, yingqi-z20

## Definition

Since the definition of **source and sink points** is removed, we need to redefine the concept of a **cut**.

(Actually the definition of a cut in the network-flow part does not agree with Wikipedia; it is just that since the cut usually encountered is the "minimum cut problem with source and sink", this concept became conventional.)

### Cut

The edge set whose removal of all edges can make a network-flow graph no longer connected (i.e. divide it into two subgraphs) is called a cut of the graph.

That is: in an undirected graph $G = (V, E)$, let $C$ be a set of some arcs in graph $G$; if deleting all arcs in $C$ from $G$ can make graph $G$ not a connected graph, then $C$ is called a cut of graph $G$.

### Minimum cut problem with source and sink

Same as the definition in [minimum cut](./flow/min-cut.md).

### Minimum cut problem without source and sink

The cut with the minimum sum of weights of the contained arcs. Also called the global minimum cut.

Obviously, directly running network flow is complexity-wise infeasible.

***

## Stoer–Wagner algorithm

### Introduction

The Stoer–Wagner algorithm was proposed in 1995 by *Mechthild Stoer* and *Frank Wagner*; it is an algorithm that solves the global minimum cut problem on an **undirected positive-weight graph** through **recursion**.

### Properties

The algorithm complexity $O(|V||E| + |V|^{2}\log|V|)$ can generally be approximately regarded as $O(|V|^3)$.

Its implementation is based on the following basic fact: let there be any two points $S, T$ in graph $G$. Then any cut $C$ of graph $G$ either has $S, T$ in the same connected block, or has $C$ being an ${S-T}$ cut.

### Procedure

1.  Arbitrarily designate two points $s, t$ in graph $G$, and taking these two points as source and sink, find the $S-T$ minimum cut of graph $G$ (defined as the *cut of phase*), and update the current answer.
2.  "Merge" points $s, t$; if $|V|$ in graph $G$ is greater than $1$, then return to the first step.
3.  Output the minimum value of all *cut of phase*.

Merging two points $s, t$: delete the edge $(s, t)$ between $s, t$; for any point $k$ in $G \setminus \{s, t\}$, delete $(t, k)$, and add its edge weight $d(t, k)$ to $d(s, k)$.

Explanation: if $s, t$ are in the same connected block, for a point $k$ in $G \setminus \{s, t\}$, if $(k, s) \in C_{\min}$, then $(k, t) \in C_{\min}$ must also hold, otherwise because $s, t$ are connected and $k, t$ are connected, it causes $s, k$ to be in the same connected block, and at this time $C = C_{\min} \setminus \{(t, k)\}$ would be better than $C_{\min}$. And vice versa. So $s, t$ can be regarded as the same point.

Step 1 considers the case where $s,t$ are not in the same connected block, and step 2 considers the remaining case. Since each execution of step 2 decreases $|V|$ by $1$, the algorithm will end after $|V| - 1$ steps.

### Method for finding the S-T minimum cut

(Obviously not network flow.)

Assume that after several merges, the current graph is $G'=(V', E')$, and execute step 1.

We construct a set $A$, initially letting $A = \varnothing$.

Each time we add to set $A$ the node among all points in $V'$ that satisfies $i \notin A$ and has the maximum weight function $w(A, i)$, until $|A| = |V'|$.

The definition of the weight function:

$w(A, i) = \sum_{j \in A} d(i, j)$

(if $(i, j) \notin E'$, then $d(i, j) = 0$).

It is easy to know that the order in which all points are added to $A$ is fixed; let $\operatorname{ord}(i)$ denote the $i$-th point added to $A$, $t = \operatorname{ord}(|V'|)$; $\operatorname{pos}(v)$ denotes the size of $|A|$ after $v$ is added to $A$, i.e. the order in which $v$ is added.

Then for any point $s$, a cut from $s$ to $t$ is $w(t)$.

### Proof

Define a point $v$ as activated if and only if, when $v$ is added to $A$, we find that the last point $u$ in $A$ at this time was added to the set earlier than $v$, and in the graph $G'' = (V', E'/C)$, $u$ and $v$ are not in the same connected block.

![Stoer-Wagner1](./images/Stoer-Wagner1.png)

As shown in the figure, the blue region and the yellow region are two different connected blocks, and the numbers in square brackets are the order of being added to $A$. Gray nodes are active nodes, while white nodes are not active nodes.

Define $A_v = \{u \mid \operatorname{pos}(u) < \operatorname{pos}(v)\}$, that is, the points added to $A$ strictly earlier than $v$; let $E_v$ be the edge set of the induced subgraph of $E'$ (with point set $A_v \cup\{v\}$). (Note that it includes point $v$.)

Define the induced cut $C_v$ as $C \cap E_v$. $w(C_v) = \sum_{(i,j) \in C_v} d(i, j)$.

???+ note "Lemma 1"
    For any activated point $v$, $w(A_v, v) \le w(C_v)$.
    
    Proof: Use mathematical induction.
    
    For the first activated point $v_0$, by definition we know $w(A_{v_0}, v_0) = w(C_{v_0})$.
    
    For two subsequent activated points $u, v$, assuming $\operatorname{pos}(v) < \operatorname{pos}(u)$, we have:
    
    $w(A_u, u) = w(A_v, u) + w(A_u - A_v, u)$
    
    Also, it is known that:
    
    $w(A_v, u) \le w(A_v, v)$ and $w(A_v, v) \le w(C_v)$; combining them gives:
    
    $w(A_u, u) \le w(C_v) + w(A_u - A_v, u)$
    
    Since $w(A_u - A_v, u)$ contributes to $w(C_u)$ but not to $w(C_v)$, in the case where all edges are positive-weight, we can derive:
    
    $w(A_u,u) \le w(C_u)$
    
    Proved by induction.

Since $\operatorname{pos}(s) < \operatorname{pos}(t)$ and $s, t$ are not in the same connected block, $t$ will be activated, from which we can conclude $w(A_t, t) \le w(C_t) = w(C)$.

??? note "[P5632 [Template] Stoer–Wagner algorithm](https://www.luogu.com.cn/problem/P5632)"
    ```cpp
    --8<-- "docs/graph/code/stoer-wagner/stoer-wagner_1.cpp"
    ```

***

### Complexity analysis and optimization

The complexity of the *contract* operation is $O(|E| + |V|\log|V|)$.

A total of $O(|V|)$ *contract*s are performed, with total complexity $O(|E||V| + |V|^2\log|V|)$.

According to the experience of [shortest path](./shortest-path.md), the algorithm bottleneck lies in finding the point with the maximum weight.

In one *contract*, we need to find the heap top $|V|$ times, and incrementally modify the weight $|E|$ times.

The Fibonacci heap can handle finding the heap top in $O(\log|V|)$ and incrementally modifying the weight in $O(1)$; the theoretical complexity can reach $O(|E| + |V|\log|V|)$, but since the Fibonacci heap has too large a constant factor and a high amount of code, its practical application value is relatively low.

(In actual testing, even with O2 enabled, we still need to fight against judge fluctuations to pass.)
