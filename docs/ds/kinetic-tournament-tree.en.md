author: Jerry3128

Prerequisite: [segment tree](./seg.md)

## Problem statement

Given a sequence of single-variable linear functions $F=\{f_1,\dots,f_n\}$: $f_i: \mathbf{R} \rightarrow \mathbf{R}$, where $f_i(x)=k_ix+b_i$ and $k_i,b_i \in \mathbf{R}$. We need to maintain the following operations:

-   $\operatorname{QueryMax}(l,r)$: given $l$ and $r$, return $\max_{i=l}^r{f_i(0)}$.
-   $\operatorname{TranslateLeft}(l,r,\delta)$: given $l$, $r$, and $\delta$, for all $i\in[l,r]$, perform the operation $f_i(x) \leftarrow f_i(x+\delta)$; this operation is equivalent to performing $b_i\leftarrow b_i+k_i\delta$, where $\delta > 0$.

For convenience, we assume all functions are pairwise distinct.

The essence of a left translation of linear functions over an interval is $b_i \leftarrow k_i\cdot \delta$, i.e. for the constant term $b_i$, adding to it the slope $k_i$ times the translation amount of the abscissa $\delta$; this operation is equivalent to the "position-coefficient-weighted interval add" we encounter in many data-structure problems: i.e. for each index $i$ in the interval $[l, r]$, adding to its value a fixed number $\delta$ times the coefficient $k_i$ specific to that position. Therefore, the interval translation of linear functions is essentially the so-called position-coefficient-weighted interval addition.

To showcase the unique binary-tree divide-and-conquer structure of KTT, we will start directly from interval translation.

## Kinetic Data Structures

Kinetic Data Structures, or KDS, are used to maintain the attributes of a system of geometric objects during continuous motion.

### Event queue

We assume each point has a known motion plan; this plan can provide its complete or partial motion information—for example, the curve or line formed by the function $f_i(x)$ describes the trajectory of the moving point $i$ well. The motion plan may change at any time, possibly due to collisions or environmental interactions; we call the cause of a motion-plan change an event. The event queue gives events in chronological order.

A key aspect of KDS is that we need events that are easy to maintain, i.e. the event types in the event queue correspond to possible combinatorial changes involving a constant and usually small number of objects. For example, in the maintenance of this problem, one event type we use is "the magnitude relationship between function $f_i(0)$ and function $f_{j}(0)$ changes".

The event queue can be maintained implicitly.

### Certificates

These events should be equivalent to being guaranteed by the intersection of a series of low-degree algebraic conditions, each involving a finite number of objects. We call these conditions the certificates of the KDS. For example, $[f_i(0) > f_j(0)]$.

## Kinetic Tournament Tree

### Introduction

The Kinetic Tournament Tree (KTT), which belongs to Kinetic Data Structures, first appeared in the 1999 [Data Structures for Mobile Data](https://www.sciencedirect.com/science/article/pii/S0196677498909889), used to maintain continuously changing data. More generally, every structure adopting the following kinetization strategy can be called a Kinetic Tournament:

-   Generate correctness certificates for the key operations (such as comparisons) in a static algorithm, and associate each certificate with a global event queue, recording the time point at which that certificate may become invalid.
-   When some certificate becomes invalid, we can efficiently update the algorithm output and maintain the certificate set.

In the competitive-programming community, it rose to prominence with the 2020 National Training Team paper "[A Brief Discussion of the Dynamic Maintenance of Function Extrema](https://github.com/OI-wiki/libs/blob/master/%E9%9B%86%E8%AE%AD%E9%98%9F%E5%8E%86%E5%B9%B4%E8%AE%BA%E6%96%87/IOI2020%E4%B8%AD%E5%9B%BD%E5%9B%BD%E5%AE%B6%E5%80%99%E9%80%89%E9%98%9F%E8%AE%BA%E6%96%87%E9%9B%86%20%E9%9D%9E%E6%AD%A3%E5%BC%8F%E7%89%88.pdf)". The academic KTT and the competitive-programming KTT differ in application area and implementation, so we will introduce the KTT with some optimizations made for the competitive-programming community.

### Basic structure

First we consider designing a data structure similar to a segment tree to maintain the static maximum. We build the segment-tree structure; for each non-leaf node, its weight is the larger weight of its two children. After performing $O(n)$ comparisons, the weight we obtain at the root is the global maximum. Now, the weights begin to change. As long as KTT can detect each change of the source of the maximum at a tree node, we can maintain the global maximum.

To let KTT detect each change of the source of the maximum on the tree, for a tree node $x$ and the functions $f_L$ and $f_R$ provided by its left and right children, we define the certificate as "the magnitude relationship between $f_L$ and $f_R$ remains unchanged". When the certificate becomes invalid, we need to walk along the tree path to the node where the current certificate is invalid to update its information. To maintain the invalidation time of each certificate, we find that the moment a certificate becomes invalid is exactly the moment the two functions have equal values, so the problem becomes finding the abscissa of the intersection of two linear functions, which can be solved in $O(1)$ time.

For each tree node, we maintain the function that attains the maximum at $0$, as well as the current certificate's invalidation time and the earliest invalidation time of a certificate within the whole subtree; then at the moment each node's certificate becomes invalid, we can find it at this moment and update its information. This information is used to record the information of the functions themselves. Next we consider maintaining the interval-translation operation; because it can be simply accumulated, we can use a lazy tag to handle the interval-translation operation.

We define the lazy tag $\Delta_v$ to mean that all other nodes' functions within the subtree of node $v$ should be translated left by $\Delta_v$ units. At this point, for a tree node $v$, a new operation is to translate all functions within its subtree left by $\delta$ over the interval, i.e. $f(x)\leftarrow f(x+\delta)$. We need to update the lazy tag: $\Delta_v\leftarrow \Delta_v + \delta$, i.e. accumulate the offsets of all other nodes within the subtree. At the same time, a left translation also means a change in the function value at the $0$ point. We can find that if a certificate's invalidation abscissa is $t$, then after translation the invalidation abscissa should be $t-\delta$; at this point, if $t-\delta$ crosses the $0$ point, it means the certificate is invalid, and we need to recurse down to find the node where the current certificate is, update the current node, and update the new information upward to the root. This process can be done together with the modification.

Thus we can obtain a simple implementation.

???+ example "Reference implementation"
    ```cpp
    --8<-- "docs/ds/code/ktt/ktt_1.cpp:core"
    ```

### Complexity analysis

Proving the time complexity of KTT requires potential analysis.

Let $d(x)$ be the depth of node $x$ on the segment tree, with the root having depth $1$. Define the potential of node $x$ on the segment tree as:

$$
\alpha(x) = \begin{cases}
d(x) & \text{if the lower slope function has larger value}  \\
0    & \text{otherwise}\\
\end{cases}
$$

That is, among the two functions compared at $x$, if the function with the smaller slope has a larger value at the $0$ point, then the current node's potential is $d(x)$, otherwise it is $0$.

Define the potential of the whole KTT as the sum of all nodes' potentials:

$$
\Phi = \sum_x \alpha(x)
$$

Consider a certain update, for node $x$ and its parent $p$, with actual update cost $c=1$, and potentials $\Phi$ and $\Phi'$ before and after the update. We compute the amortized update cost of updating node $x$. Since the current node $x$ is updated, its potential at that moment must drop from $d(x)$ to $0$. And for $p$, in the worst case its potential may rise from $0$ to $d(p)$:

$$
\begin{aligned}
\hat{c} &= 1 + \Phi' - \Phi\\
    &= 1 + (\alpha'(p) + \alpha'(x)) - (\alpha(p) + \alpha(x))\\
    &= 1 + (\alpha'(p) - \alpha(p)) + (\alpha'(x) - \alpha(x))\\
    &\leq 1 + d(p) - d(x)\\
    &= 0
\end{aligned}
$$

Summing the actual costs and defining the initial potential $\Phi_s$ and final potential $\Phi_t$:

$$
\begin{aligned}
\sum c  &= \sum \hat{c} + \Phi_{s} - \Phi_{t}\\
    &\leq \Phi_{s} - \Phi_{t}\\
    &=O(n\log n)
\end{aligned}
$$

This part is the number of times KTT finishes updating all invalid certificates in the case where only global modifications exist.

Additionally, consider the effect of interval translation on the potential. For a certain interval translation, the nodes we need to consider are those whose subtree contains but does not entirely consist of tree nodes that the interval-translation operation is executed on. Such nodes are exactly the nodes we pass on the tree when performing the modification operation, and their number does not exceed $O(\log n)$; in the worst case, each node's potential rises by $d(x)\le \log n$, so each operation raises the potential by $O(\log^2 n)$.

To maintain interval translation, the certificate-update operation will be executed $O(n\log n + m\log^2 n)$ times. Each time we update a certificate, we need to walk along the path on the tree to the node where the certificate is invalid, which is $O(\log n)$. Therefore the total time complexity is $O(n\log^2 n+ m\log^3 n)$.

The excellence of this method is that it has already reached the lower bound of the problem's time complexity, $O(\lambda_{s}(n)\log^2 n)$. $\lambda_{s}(n)$ denotes the length of the longest $(n, s)$ Davenport–Schinzel sequence, where linear functions correspond to $s=1$ with $\lambda_1(n)=n$. This part belongs to computational geometry and is not belabored here.

### The higher-degree case

If what we maintain is not linear functions but polynomial functions, or more complex functions, how do we cope? Two complex functions may have multiple intersection points. Given a sequence of continuous, fully defined single-variable functions $F=\{f_1,\dots,f_n\}$: $f_i: \mathbf{R} \rightarrow \mathbf{R}$, where each pair of functions' graphs intersect at most $s$ points. Representatively, the set of degree-$s$ polynomial functions meets this requirement.

For the same problem, we use potential analysis.

$d(x)$ is the depth of node $x$ on the segment tree, with the root having depth $1$. Define $I(x)$ as the number of intersection points, after the $0$ point, of the two functions compared at node $x$. Define the potential of node $x$ on the segment tree as:

$$
\alpha(x)=d(x)^{\log_2(s+1)}I(x)
$$

Define the potential of the whole KTT as the sum of all nodes' potentials:

$$
\Phi = \sum_x \alpha(x)
$$

Consider a certain update, for node $x$ and its parent $p$, with actual update cost $c=1$, and potentials $\Phi$ and $\Phi'$ before and after the update. We compute the amortized update cost of updating node $x$. Since the current node $x$ is updated, its potential at that moment must drop from $d(x)^{\log_2(s+1)}I(x)$ to $d(x)^{\log_2(s+1)}(I(x)-1)$. And for $p$, in the worst case its potential may rise from $0$ to $d(p)^{\log_2(s+1)}$:

$$
\begin{aligned}
        \hat{c} &= 1 + \Phi' - \Phi\\
                &= 1 + (\alpha'(x) - \alpha(x)) + (\alpha'(p) - \alpha(p))\\
                &\leq 1 - d(x)^{\log_2{(s+1)}} + s(d(x)-1)^{\log_2{(s+1)}}\\
                &\leq 0
    \end{aligned}
$$

From the third line to the fourth line we used the restriction that $d(x)$ is a positive integer.

Summing the actual costs and defining the initial potential $\Phi_s$ and final potential $\Phi_t$:

$$
\begin{aligned}
    \sum c  &= \sum \hat{c} - \Phi_t + \Phi_s\\
            &\leq \Phi_s - \Phi_t\\
            &= O(ns (\log n)^{\log_2{(s+1)}})
\end{aligned}
$$

We obtain the upper bound on the complexity $O(ns (\log n)^{1+\log_2{(s+1)}} + ms (\log n)^{2+\log_2{(s+1)}})$. [^ref1]

### The approximate case

Given a sequence of continuous, fully defined single-variable functions $F=\{f_1,\dots,f_n\}$, define $\mathfrak U_F(x)$, $\mathfrak L_F(x)$, and $\mathfrak E_F(x)$ as the upper envelope, lower envelope, and extent respectively.

$$
\begin{aligned}
    \mathfrak U_F(x) & = \max\{f_i(x) \mid f_i \in F\} \\
    \mathfrak L_F(x) & = \min\{f_i(x) \mid f_i \in F\} \\
    \mathfrak E_F(x) & = \mathfrak U_F(x) - \mathfrak L_F(x)
\end{aligned}
$$

We only require the program to return $\tilde{\mathfrak U}_F(x)$ satisfying

$$
\mathfrak U_F(x) \geq \tilde{\mathfrak U}_F(x) \geq \mathfrak U_F(x) - \epsilon \mathfrak E_F(x)
$$

Then in the complex case we can achieve $O((1/\epsilon^2)n\log^3 n)$, independent of the polynomial degree, and we allow functions to simultaneously perform interval left-shift or right-shift.

## References and notes

[^ref1]: Note that this only gives an upper bound; the lower bound of the complexity should be $O(\lambda_{s}(n)\log n)$. The author conjectures that the potential-analysis construction here should refer to the general-term formula of $\lambda_{s}(n)$ corresponding to Davenport–Schinzel sequences to obtain a tighter upper bound.

-   P. K. Agarwal, S. Har-Peled, and K. R. Varadarajan. Approximating extent measures of points. J. ACM, 51(4):606–635, July 2004.
-   J. Basch, L. J. Guibas, and J. Hershberger. Data structures for mobile data. Journal of Algorithms, 31(1):1–28, 1999.
-   G. Alexandron, H. Kaplan, and M. Sharir. Kinetic and dynamic data structures for convex hulls and upper envelopes. Computational Geometry, 36(2):144–158, 2007.
