author: Marcythm, zyf0726, hsfzLZH1, MingqiHuang, Ir1d, greyqz, billchenchina, Chrogeek, StudyingFather, NFLSCode, c-forrest

Quadrangle-inequality optimization exploits the decision monotonicity in the state-transition equation; it is also often called **decision-monotonicity optimization of DP**.

## Basics

Consider the simplest case, where we want to solve the following series of optimization problems:

$$
f(i) = \min_{1 \leq j \leq i} w(j,i) \qquad \left(1 \leq i \leq n\right) \tag{1}
$$

Here we assume the cost function $w(j,i)$ can be computed in $O(1)$ time.

???+ info "Convention"
    The state-transition equation of dynamic programming can often be written in the form of a series of optimization problems. Taking equation (1) as an example, these problems contain a parameter $i$, and the problem's objective function and feasible region can both depend on $i$. Each problem, given the parameter $i$, selects some feasible solution $j$ to minimize the value of the objective function. For convenience of description, below we abbreviate the optimization problem with parameter $i$ as "problem $i$", the feasible solution $j$ of this optimization problem as "decision $j$", and the value the objective function attains at the optimal solution as "state $f(i)$". At the same time, denote the smallest optimal decision point corresponding to problem $i$ as $\operatorname{opt}(i)$.

In the general case, the total time complexity of these problems is $O(n^2)$. This is because for problem $i$ we need to consider all possible decisions $j$. And when decision monotonicity holds, we can effectively shrink the decision space and optimize the total complexity.

-   **Decision monotonicity**: for any $i_1 < i_2$, $\operatorname{opt}(i_1) \leq \operatorname{opt}(i_2)$ necessarily holds.

??? note "Remark"
    For problem $i$, the set of optimal decisions is not necessarily an interval. Decision monotonicity can actually be defined on the set of optimal decisions. For sets $A$ and $B$, we can define $A \leq B$ if and only if for any $a\in A$ and $b\in B$, $\min\{a,b\}\in A$ and $\max\{a,b\}\in B$ hold. This implies the monotonicity of the smallest (largest) optimal decision point, which is the definition adopted here. The conclusions stated in this article about the smallest optimal decision point also apply to the largest optimal decision point. However, there are cases where the smallest optimal decision of some larger problem is strictly smaller than the largest optimal decision of another smaller problem, i.e. it is possible that for some $i_1 < i_2$, $\mathop{\mathrm{optmax}}(i_1) > \mathop{\mathrm{optmin}}(i_2)$ holds, so when writing code you should ensure that you always compute the smallest or the largest optimal decision point.
    
    On the other hand, the problems that have the same smallest optimal decision form an interval. This interval, as a function of the smallest optimal decision, should be strictly increasing. That is, given $j_1 = \operatorname{opt}(i_1)$, $j_2 = \operatorname{opt}(i_2)$, if $j_1 < j_2$, then necessarily $i_1 < i_2$. In other words, if the intervals of problems for which decisions $j_1 < j_2$ can be the smallest optimal decision are $[l_{j_1},r_{j_1}]$ and $[l_{j_2},r_{j_2}]$ respectively, then necessarily $r_{j_1} < l_{j_2}$.

The most common way to judge decision monotonicity is via the quadrangle inequality. In different contexts, this property is also often called the Monge property (used to describe a matrix $A_{j,i}$) or submodularity (used to describe a function $f([j,i])$ with an interval as its variable).

-   **Quadrangle inequality**: if for any $a\leq b\leq c\leq d$,

    $$
    w(a,c)+w(b,d) \leq w(a,d)+w(b,c),
    $$

    holds, then the function $w$ is said to satisfy the quadrangle inequality (abbreviated as "crossing is less than containing"). If equality always holds, then the function $w$ is said to satisfy the **quadrangle identity**.

Unless otherwise specified, below we always guarantee $a\leq b\leq c\leq d$. The quadrangle inequality gives a sufficient but not necessary condition for decision monotonicity.

???+ note "Theorem 1"
    If $w$ satisfies the quadrangle inequality, then problem (1) satisfies decision monotonicity.

??? note "Proof"
    To prove this, use proof by contradiction. Suppose for some $c < d$, $a = \operatorname{opt}(d) < \operatorname{opt}(c) = b$ holds. Then $a < b \leq c < d$. By the optimality conditions, $w(a,d) \leq w(b,d)$ and $w(b,c) < w(a,c)$, so $w(a,d) - w(b,d) \leq 0 < w(a,c) - w(b,c)$, contradicting the quadrangle inequality.

The quadrangle inequality can be understood, within a reasonable domain, as the second-order mixed difference $\Delta_i\Delta_jw(j,i)$ of $w$ being non-positive.

Using decision monotonicity, many common algorithms can optimize the complexity to $O(n\log n)$. These algorithms differ in scope of application, implementation difficulty, and running efficiency, and one needs to choose the appropriate algorithm according to the actual scenario. This mainly depends on the properties of $w(j,i)$. Unless otherwise stated, this article by default assumes $w(i,j)$ supports **random access**, i.e. $w(j,i)$ can be queried or computed in $O(1)$ time. However, not in all problems is $w(j,i)$ so easy to compute. Therefore, besides the basic case, this article also discusses methods of optimizing DP with decision monotonicity when $w(j,i)$ only has the following properties:

-   **Moving access**: $w(j,i)$ can be transitioned from $w(j\pm 1,i)$ or $w(j,i\pm 1)$ in $O(1)$ time. (Similar to the situation in [Mo's algorithm](../../misc/mo-algo.md).)
-   **Dynamic computation**: the computation of $w(j,i)$ depends on $\{f(j'):j' < j\}$. This means $f$ and $w$ can only be computed sequentially. The interval-partition problem without a restriction on the number of intervals introduced below belongs to this case.

These two properties are not mutually exclusive; there may be cases where $w(j,i)$ both needs dynamic computation and only supports moving access.

### Divide and conquer

To solve all states, we only need to solve all optimal decision points. To solve $\operatorname{opt}(i)$ for all $1 \leq i \leq n$, first compute $\operatorname{opt}(n/2)$, and then separately compute $\operatorname{opt}(i)$ on $1 \leq i < n/2$ and $n/2 < i \leq n$; note that at this point the known $\operatorname{opt}(i)$ of the first half must lie between $1$ and $\operatorname{opt}(n/2)$ (inclusive), and the $\operatorname{opt}(i)$ of the second half must lie between $\operatorname{opt}(n/2)$ and $n$ (inclusive). We handle the two subintervals similarly, until the optimal decision of every problem is computed. By recording the upper and lower search bounds during the divide-and-conquer process, we can guarantee the algorithm complexity is controlled at $O(n\log n)$. The number of levels of the recursion tree is $O(\log n)$, and in each level a single decision point is computed at most twice, so the total number of computations is $O(n\log n)$.

???+ example "Reference implementation"
    ```cpp
    --8<-- "docs/dp/code/opt/quadrangle/quadrangle-divide-conquer.cpp:core"
    ```

Besides the basic case of random access, the divide-and-conquer algorithm can also be applied to the case where $w(j,i)$ only supports moving access. We only need to maintain a cursor $(j,i)$ and the corresponding function value $w(j,i)$ during computation, and when a new value needs to be queried, brute-force move the cursor to the current position and update the function value. The time complexity of doing this is still $O(n\log n)$. For a more detailed discussion of this, refer to the [Simplified LARSCH algorithm](#simplified-larsch-algorithm) section below. However, the divide-and-conquer algorithm cannot solve the case where $w(j,i)$ needs dynamic computation, because the divide-and-conquer algorithm has no way to compute the smallest optimal decision $\operatorname{opt}(n/2)$ at the interval midpoint while the left-half interval's problems are not yet solved.

### Binary-search queue

Note that for each decision point $j$, the problems $i$ for which it can be the smallest optimal decision point necessarily form an interval. We can use a monotonic queue to record the interval of problems each decision point can solve so far; this way, the optimal solution of a problem can naturally be computed from the decision points recorded in the queue.

Specifically, the algorithm needs to traverse the decision points sequentially. When traversing to decision point $k$, the queue needs to record, for each feasible decision point $j$ so far, the **triple** formed by $j$ and the left and right endpoints $l_j$ and $r_j$ of the interval of problems it can solve. For a problem in the given interval $[l_j,r_j]$, $j$ should be the smallest optimal among the decision points considered so far (i.e. the decision points in the interval $[1,k]$). At every moment, the decisions stored in the queue are not necessarily contiguous, but the unsolved problems $[j,n]$ should be the disjoint union of the problem intervals stored in the queue.

To show that during the queue update, the problems $i$ for which decision point $j$ is the smallest optimal decision always form a contiguous interval, we need to appropriately strengthen the earlier conclusion:

???+ note "Corollary 1"
    Let $\operatorname{opt}_k(i)$ be the smallest optimal decision of problem $i$ when only the decisions in $[1,k]$ are considered. If $w$ satisfies the quadrangle inequality, then for any $i_1 < i_2$, $\operatorname{opt}_k(i_1) \leq \operatorname{opt}_k(i_2)$ necessarily holds.

??? note "Proof"
    Let $M$ be a sufficiently large positive real number. The function $w'(j,i) = w(j,i) + M[j > k]$ still satisfies the quadrangle inequality, where $[\cdot]$ is the Iverson bracket. Consider the auxiliary DP with $w'$ as the cost function. In the auxiliary DP, for any problem $i$, a decision $j > k$ can never be the smallest optimal, i.e. $\operatorname{opt}'(i) = \operatorname{opt}'_k(i) = \operatorname{opt}_k(i)$. Applying Theorem 1 to the auxiliary DP gives this corollary.

The algorithm process is as follows:[^cmp-min-opt]

-   Initially, the queue is empty. Similar to a monotonic queue, each time we consider the next decision $j$, we need to perform dequeue and enqueue operations.
-   **Dequeue**: first remove the previous problem $j-1$ from the queue. If the right endpoint of the problems the front decision can solve is exactly $j-1$, directly pop the front; otherwise, update the left endpoint of the problems the front decision can solve to $j$.
-   **Enqueue**: to enqueue decision $j$, first compare it with the tail decision $j'$.
    -   If, for problem $l_{j'}$, the decision $j$ to be enqueued is strictly better than the existing decision $j'$, i.e. $w(j,l_{j'}) < w(j',l_{j'})$, then pop the tail decision $j'$. This operation continues until the queue is empty or the tail decision $j'$ is better than $j$ for problem $l_{j'}$.
    -   If the queue is already empty, enqueue $(j,j,n)$, i.e. consider decision $j$ the optimal solution of all unsolved problems.
    -   If the tail decision $j'$ is also no worse than the decision $j$ to be enqueued for problem $r_{j'}$, then when $r_{j'} < n$, enqueue $(j,r_{j'}+1,n)$, indicating $j$ is the smallest optimal decision of problems $[r_{j'}+1,n]$; otherwise, there is no need to enqueue $j$, because it is not better than the existing decision.
    -   The last case is that the tail decision $j'$ is strictly better than the decision $j$ to be enqueued for problem $l_{j'}$, but strictly worse for problem $r_{j'}$. This means there exists a problem $i\in(l_{j'},r_{j'}]$ such that the smallest optimal decision of problems $[l_{j'},i-1]$ is $j'$ and the smallest optimal decision of problems $[i,r_{j'}]$ is $j$. Therefore, we need to find, via **binary search**, the smallest $i\in[l_{j'},r_{j'}]$ such that $w(j,i) < w(j',i)$, then modify the tail's right endpoint $r_{j'}$ to $i-1$ and enqueue $(j,i,n)$.
-   After handling decision $j$, we have handled all decisions up to $j$. At this point, the front decision is the smallest optimal decision of problem $j$, and we can record the corresponding optimal solution.

???+ example "Reference implementation"
    ```cpp
    --8<-- "docs/dp/code/opt/quadrangle/quadrangle-monotone-queue.cpp:core"
    ```

Similar to a monotonic queue, each decision point is enqueued at most once and dequeued at most once. Dequeuing is $O(1)$, while enqueuing is $O(\log n)$ (a binary search may be needed), so the total time complexity is $O(n\log n)$.

Since the binary-search-queue algorithm sequentially considers all problems and decision points, it can be applied to the case where $w(j,i)$ needs dynamic computation. This is its advantage over the divide-and-conquer algorithm. But because the binary-search step in the algorithm relies on random access to $w(j,i)$, it cannot be applied to the case where $w(j,i)$ only supports moving access.

???+ example "Example 1: ["POI2011" Lightning Conductor](https://loj.ac/problem/2157)"
    Given a sequence $a_1,a_2,\cdots,a_n$ of length $n$, for each $1 \leq i \leq n$ find the smallest non-negative integer $f_i$ satisfying
    
    $$
    \forall j\in\left[1,n\right]:a_j \leq a_i + f_i - \sqrt{|i-j|}.
    $$

??? note "Idea"
    Clearly, by transforming the inequality, we can obtain the integer to be found $f_i = \max_{j}\{a_j+\sqrt{|i-j|}-a_i\}$. Consider the case $j \leq i$ first (the other case is similar); then we can obtain the state-transition equation:
    
    $$
    f_i = -\min_{j\le i}\{-a_j-\sqrt{i-j}+a_i\}.
    $$
    
    By the convexity of $-\sqrt{x}$, we easily conclude (described in detail later) that the function $w(l, r) = -a_l - \sqrt{r-l} + a_r$ satisfies the quadrangle inequality, so applying the above algorithm solves this problem in $O(n\log n)$ time.

??? note "Implementation"
    ```cpp
    --8<-- "docs/dp/code/opt/quadrangle/quadrangle_1.cpp"
    ```

### Simplified LARSCH algorithm

Neither of the previous two algorithms can handle the case where $w(j,i)$ both needs dynamic computation and only supports moving access. This section introduces an algorithm that can overcome both difficulties at once. It is a simplified version of the LARSCH algorithm[^larsch] proposed by Larmore and Schieber in 1991, hence called the **simplified LARSCH algorithm**. The original version of this algorithm can solve decision-monotonicity DP problems in $O(n)$ time, but its implementation is more complex and is not introduced in this article.

We still consider solving with divide and conquer. When solving the problems in the interval $(l,r]$, assume the following information is known:

-   the smallest optimal decision $\operatorname{opt}(i)$ and optimal value of problem $i$ in the interval $[1,l]$, and
-   the smallest optimal decision $\operatorname{opt}_l(r)$ and optimal value of problem $r$ considering only the decisions in the interval $[1,l]$.

When solving the problems in the interval $(l,r]$ is finished, we need to obtain the smallest optimal decision and optimal value of the problems in the interval $(l,r]$.

Let $\textit{mid}$ be the midpoint of the interval $(l,r]$. The solving process is as follows:

1.  Traverse decisions $i\in[\operatorname{opt}(l),\operatorname{opt}_l(r)]$, updating the smallest optimal decision and optimal value of problem $\textit{mid}$.
2.  Recursively solve the problems in the interval $(l,\textit{mid}]$.
3.  Traverse decisions $i\in(l,\textit{mid}]$, updating the smallest optimal decision and optimal value of problem $r$.
4.  Recursively solve the problems in the interval $(\textit{mid},r]$.

Before executing the recursion on the whole interval $[1,n]$, we first need to update problems $i\in\{1,n\}$ with decision $j=1$. The algorithm terminates when the recursion reaches $l=r$.

???+ example "Reference implementation"
    ```cpp
    --8<-- "docs/dp/code/opt/quadrangle/quadrangle-simplified-larsch.cpp:core"
    ```

First, we can show the correctness of this algorithm. To this end, we only need to check that the preconditions given above are satisfied before each recursive-solving step (i.e. steps 2 and 4). By Corollary 1 from the previous section, $\operatorname{opt}(l)=\operatorname{opt}_l(l)\le\operatorname{opt}_l(\textit{mid})\le\operatorname{opt}_l(r)$, so after step 1, $\operatorname{opt}_l(\textit{mid})$ is known, and thus the precondition for recursively solving the problems in the interval $(l,\textit{mid}]$ before executing step 2 holds. Since $\{\operatorname{opt}(i):i\in[1,l]\}$ was known before, and step 2 also obtained the values of $\{\operatorname{opt}(i):i\in(l,\textit{mid}]\}$, afterward $\{\operatorname{opt}(i):i\in[1,\textit{mid}]\}$ are all known; at the same time, since $\operatorname{opt}_l(r)$ was known before, after step 3 $\operatorname{opt}_\textit{mid}(r)$ is also known. Therefore, the precondition for recursively solving the problems in the interval $(\textit{mid},r]$ before executing step 4 also holds.

Then, we need to show that the complexity of this algorithm is still $O(n\log n)$. The number of levels of the recursion tree is $O(\log n)$. For each node in the same level of the recursion tree, we traverse the decisions in the intervals $[\operatorname{opt}(l),\operatorname{opt}_l(r)]$ and $(l,\textit{mid}]$ respectively. Because $\operatorname{opt}(l)\le\operatorname{opt}_l(r)\le\operatorname{opt}(r)$, in the same level, each decision point is traversed only $O(1)$ times. Hence, the total number of traversals in each level of the recursion tree is $O(n)$. Assuming the complexity of a single access to or computation of $w(j,i)$ is $O(1)$, the time complexity of the algorithm is $O(n\log n)$.

For some cases where $w(j,i)$ only supports moving access, the complexity of this algorithm is still $O(n\log n)$. In this case, we need to maintain a cursor $(j,i)$ and the current value of $w(j,i)$ for steps 1 and 3 of the algorithm respectively. Each time a new value needs to be accessed, we need to brute-force update the cursor $(j,i)$ from its position at the last access to the current position, and transition the function value $w(j,i)$. It is easy to verify that when traversing the recursion tree, the total number of these brute-force updates is $O(n\log n)$. So the time complexity of the algorithm is still $O(n\log n)$.

??? note "Complexity proof for non-random access"
    We only need to prove that the total number of cursor moves is $O(n\log n)$. Let $A$ and $B$ be the cursors corresponding to steps 1 and 3 respectively. In fact we can guarantee: before solving the problems in the interval $(l,r]$, cursor $A$ is at position $(\operatorname{opt}(l),l)$ and cursor $B$ is at position $(l,l)$; and afterward, cursor $A$ is at position $(\operatorname{opt}(r),r)$ and cursor $B$ is at position $(r,r)$.
    
    Consider constructing the following cursor-movement rules. In step 1, we can let cursor $A$ move along the path
    
    $$
    (\operatorname{opt}(l),l)\to(\operatorname{opt}(l),\textit{mid})\to(\operatorname{opt}_l(r),\textit{mid})\to(\operatorname{opt}(l),\textit{mid})\to(\operatorname{opt}(l),l)
    $$
    
    At this point, cursors $A$ and $B$ are both at the prescribed positions before solving the problems in the interval $(l,\textit{mid}]$. In step 2, as prescribed, cursor $A$ will move to $(\operatorname{opt}(\textit{mid}),\textit{mid})$ and cursor $B$ will move to $(\textit{mid},\textit{mid})$. In step 3, we can let cursor $B$ move along the path
    
    $$
    (\textit{mid},\textit{mid}) \to (l,\textit{mid}) \to (l, r) \to (\textit{mid},r) \to (\textit{mid},\textit{mid})
    $$
    
    At this point, cursors $A$ and $B$ are both at the prescribed positions before solving the problems in the interval $(\textit{mid},r]$. In step 4, as prescribed, cursor $A$ will move to $(\operatorname{opt}(r),r)$ and cursor $B$ will move to $(r,r)$. Both cursors are at the prescribed positions upon finishing solving the problems in the interval $(l,r]$. Therefore, this movement rule conforms to the above prescriptions. Moreover, this movement rule suffices to complete all computations in steps 1 and 3. Directly computing the number of cursor moves in this rule shows that step 1 needs
    
    $$
    2(\operatorname{opt}_l(r) - \operatorname{opt}(l)) + 2(\textit{mid} - l)
    $$
    
    moves, and step 3 needs
    
    $$
    2(\textit{mid}-l)+2(r-\textit{mid}) = 2(r-l)
    $$
    
    moves. Summing these move counts over all nodes in the recursion tree, and using the property that all $[l,r]$ and $[\operatorname{opt}(l),\operatorname{opt}_l(r)]$ in the same level overlap at most at their endpoints, we can show that the total number of moves is $O(n\log n)$.
    
    Since the above movement rule sets more waypoints than the cursor movement during the actual computation, the actual number of cursor moves does not exceed the estimate of the number of moves under this rule. Therefore, the actual number of cursor moves is also $O(n\log n)$.

Since this algorithm has computed the optimal solutions $f(i)$ in the interval $[1,l]$ before solving the problems in the interval $(l,r]$, this algorithm can also be applied to the case where $w(j,i)$ needs dynamic computation.

## Interval-partition problem

Consider the problem of splitting some interval into several subintervals. Formally, split the given interval $[1,n]$ into $[a_1,b_1],\cdots,[a_k,b_k]$, where $a_1=1$, $b_k=n$, and $b_{i}+1=a_{i+1}$ holds for any $i < k$. For a given split, the cost is $\sum_{i=1}^kw(a_i,b_i)$. The problem asks to minimize this cost. We can write the following 1D1D state-transition equation.

$$
f(i) = \min_{1\leq j\leq i} f(j-1)+w(j,i) \qquad (1\leq i\leq n)
$$

Here $f(0)=0$. Note that as long as $w(j,i)$ satisfies the quadrangle inequality, $f(j-1)+w(j,i)$ necessarily satisfies the quadrangle inequality, because the first term does not include a cross term of $j$ and $i$ and cancels out in the mixed difference. But since the cost function depends on the previous subproblems, this transition can only be computed sequentially, so the first divide-and-conquer algorithm described earlier cannot be applied; usually only the binary-search-queue algorithm or the simplified LARSCH algorithm is suitable. The algorithm complexity is $O(n\log n)$.

### The case with a restricted number of intervals

The above problem can be strengthened to the case with a restricted number of intervals, i.e. the problem specifies splitting the interval into $m$ subintervals. In this case, we need to take the number of intervals after splitting as one dimension of the transition state. Correspondingly, we have the following 2D1D state-transition equation.

$$
f(k,i) = \min_{1\leq j\leq i} f(k-1,j-1)+w(j,i) \qquad (1\leq k\leq m,\ 1\leq i\leq n) \tag{2}
$$

Here $f(0,0)=0$, and $f(0,i)=f(k,0)=\infty$ holds for any $1\leq k\leq m$ and $1\leq i\leq n$. By the same reasoning as above, here $f(k-1,j-1)+w(j,i)$ necessarily satisfies the quadrangle inequality. At this point, the computation of layer $i$ no longer depends on the results of that layer, so for each layer, we can compute it via any algorithm described in the previous section, and the algorithm complexity is $O(mn\log n)$.

For this problem, using decision monotonicity, there are actually other optimization algorithms. The second optimization idea relies on the following result. This optimization algorithm is very similar to the Knuth optimization algorithm described in detail below.

???+ note "Theorem 2"
    If $w$ satisfies the quadrangle inequality, then for problem (2), $\operatorname{opt}(k-1,i) \leq \operatorname{opt}(k,i) \leq \operatorname{opt}(k,i+1)$ holds.

??? note "Proof"
    The second inequality is just the decision monotonicity of layer $k$. The key is the first inequality.
    
    Below we prove $\operatorname{opt}(k,i) \leq \operatorname{opt}(k+1,i)$. Suppose we have the following two partitions of the interval $[1,i]$ (labeled in reverse order): $[a_{k},d_{k}],\cdots,[a_1,d_1]$ and $[b_{k+1},c_{k+1}],\cdots,[b_1,c_1]$. Here, the left endpoint of each interval is the smallest optimal decision of the problem corresponding to its right endpoint; likewise, considering all possible partitions from right to left, the right endpoint is also the smallest optimal decision of the problem corresponding to the left endpoint. For example, $d_j$ and $c_j$ are respectively the smallest optimal decisions of the right endpoint of the first interval from the left when $[a_j,i]$ and $[b_j,i]$ are split into $j$ segments. By decision monotonicity, if $a_{j-1} > b_{j-1}$, i.e. $d_j > c_j$, then necessarily $a_j > b_j$. Hence, if the claim does not hold, then $a_1 > b_1$. Further, we can inductively prove $a_{k} > b_{k}$. This clearly contradicts the assumption. This completes the proof.
    
    The first inequality can be proven alternatively as follows. Again consider the two partitions in the above proof. If the claim does not hold, then $a_1 > b_1$, but since $a_{k} < b_{k}$, we can find the smallest $j>1$ such that $a_j \leq b_j$. Further, at this point $a_{j-1} > b_{j-1}$, so $d_j>c_j$. We have found a group of intervals satisfying $a_j \leq b_j \leq c_j < d_j$. Consider the result of recombining these two partitions. Consider the partition $[b_{k+1},c_{k+1}],\cdots,[b_{j+1},c_{j+1}],[b_j,d_j],[a_{j-1},d_{j-1}],\cdots,[a_1,d_1]$, with $(k+1)$ segments in total, so by the assumed optimality we deduce
    
    $$
    \begin{aligned}
    &w(b_{k+1},c_{k+1})+\cdots+w(b_{j+1},c_{j+1})+w(b_j,c_j)+w(b_{j-1},c_{j-1})+\cdots+w(b_1,c_1) \\
    &\qquad \leq w(b_{k+1},c_{k+1})+\cdots+w(b_{j+1},c_{j+1})+w(b_j,d_j)+w(a_{j-1},d_{j-1})+\cdots+w(a_1,d_1).
    \end{aligned}
    $$
    
    Similarly, consider the partition $[a_{k},d_{k}],\cdots,[a_{j+1},d_{j+1}],[a_j,c_j],[b_{j-1},c_{j-1}],\cdots,[b_1,c_1]$, with $k$ segments in total; then
    
    $$
    \begin{aligned}
    &w(a_{k},d_{k})+\cdots+w(a_{j+1},d_{j+1})+w(a_j,d_j)+w(a_{j-1},d_{j-1})+\cdots+w(a_1,d_1) \\
    &\qquad < w(a_{k},d_{k})+\cdots+w(a_{j+1},d_{j+1})+w(a_j,c_j)+w(b_{j-1},c_{j-1})+\cdots+w(b_1,c_1).
    \end{aligned}
    $$
    
    Here, the inequality is strict, because $a_1 > b_1$, but by assumption $a_1$ is the smallest optimal among the left endpoints of the last segment of all $k$-segment partitions. Adding the two inequality conditions gives $w(b_j,c_j) + w(a_j,d_j) < w(b_j,d_j) + w(a_j,c_j)$, which contradicts the quadrangle inequality. Hence the original conclusion is proven.

Using this result, we can restrict the search range of decision $j$. In implementation, traverse $k$ forward and $i$ backward, and brute-force search $j$ within the previously determined upper and lower bounds to guarantee an algorithm complexity of $O(n(n+m))$.

??? warning "Note"
    The algorithm complexity here is not $O(nm)$. The correct complexity computation needs to consider the $n\times m$ state matrix. Because for problem $(i,k)$ we only need to consider the decisions in $\operatorname{opt}(k-1,i) \leq j \leq \operatorname{opt}(k,i+1)$, the total number of decisions to traverse for the problems on each anti-diagonal (i.e. where $i-k$ is a fixed value) is $O(n)$. There are $(n+m)$ such diagonals in total, so the total time complexity is $O(n(n+m))$.

The last optimization method comes from the following observation.

???+ note "Theorem 3"
    If $w$ satisfies the quadrangle inequality, then the optimal solution $g(k):=f(n,k)$ of problem (2) is a convex function of $k$.

??? note "Proof"
    Below we prove $g(k-1) + g(k+1) \ge 2g(k)$. To this end, consider the optimal partitions of length $(k-1)$ segments and $(k+1)$ segments, which are $[a_1,d_1],\cdots,[a_{k-1},d_{k-1}]$ and $[b_1,c_1],\cdots,[b_{k+1},c_{k+1}]$ respectively. Take the smallest $1 \leq j \leq k-1$ such that $c_{j+1} \leq d_j$; its existence can be deduced from $c_{k} < n = d_{k-1}$. By its minimality, $b_{j+1} > a_j$. So $a_j < b_{j+1} \leq c_{j+1} \leq d_j$. Similar to above, swapping the second halves of the two existing partitions, we can obtain the following two interval partitions:
    
    $$
    \begin{aligned}
    & [a_1,d_1],\cdots,[a_{j-1},d_{j-1}],[a_j,c_{j+1}],[b_{j+2},c_{j+2}],\cdots,[b_{k+1},c_{k+1}], \\
    & [b_1,c_1],\cdots,[b_j,c_j],[b_{j+1},d_j],[a_{j+1},d_{j+1}],\cdots,[a_{k-1},d_{k-1}].
    \end{aligned}
    $$
    
    Both resulting intervals have $k$ segments, so by the optimality condition
    
    $$
    \begin{aligned}
    2g(k) &\le w(a_1,d_1) + \cdots + w(a_{j-1},d_{j-1}) + w(a_j,c_{j+1}) + w(b_{j+2},c_{j+2}) + \cdots + w(b_{k+1},c_{k+1}) \\
    &\quad + w(b_1,c_1) + \cdots + w(b_j,c_j) + w(b_{j+1},d_j) + w(a_{j+1},d_{j+1}) + \cdots + w(a_{k-1},d_{k-1}) \\
    &\le w(a_1,d_1) + \cdots + w(a_{j-1},d_{j-1}) + w(a_j,d_j) + w(a_{j+1},d_{j+1}) + \cdots + w(a_{k-1},d_{k-1}) \\
    &\quad + w(b_1,c_1) + \cdots + w(b_j,c_j) + w(b_{j+1},c_{j+1}) + w(b_{j+2},c_{j+2}) + \cdots + w(b_{k+1},c_{k+1}) \\
    &= g(k-1) + g(k+1).
    \end{aligned}
    $$
    
    Here the second inequality is exactly the quadrangle inequality. The desired convexity is thus proven.

This conclusion guarantees that this problem can be solved via the WQS binary search method (called the Aliens Trick abroad). Specifically, consider the parameterized cost function $w_c(j,i):=w(j,i)+c$, solve the problem without a restriction on the number of intervals, and obtain its optimal solution $f_c(n)$. As the real number $c$ increases, the number of intervals in the corresponding optimal partition monotonically decreases, so we can find, via binary search, the parameter $c$ that makes the optimal number of intervals exactly equal to $m$; then the optimal solution of the original problem is $f(n,m) = f_c(n)-cm$. Here the real number $c$ can be seen as the Lagrange multiplier of the interval-count restriction. The implementation of this algorithm has many details; refer to the [WQS binary search](./wqs-binary-search.md) page. The time complexity of this algorithm is $O(n\log n\log C)$, where $C$ is some constant.

For the three algorithms of the interval-partition problem with a restricted number of intervals, their performance has different pros and cons at different data ranges, and one needs to choose the appropriate algorithm according to the specific problem.

???+ example "Example 3: [P4767 \[IOI2000\] Post Office, enhanced](https://www.luogu.com.cn/problem/P4767) [P6246 \[IOI2000\] Post Office, enhanced enhanced](https://www.luogu.com.cn/problem/P6246)"
    There are some villages beside a highway. The highway is represented as the integer axis, and the position of each village is identified by a single integer coordinate. No two villages are in the same place. The distance between two positions is the absolute value of the difference of their integer coordinates.
    
    Post offices will be built in some, but not necessarily all, of the villages. To build the post offices, you should choose the positions where they are built to minimize the total sum of distances between each village and its nearest post office.
    
    You are to write a program that, given the positions of the villages and the number of post offices, computes the minimum possible total sum of all distances between each village and its nearest post office.

??? note "Idea"
    Each village has its nearest post office, so each post office also has the villages it governs, which is easily seen to be an interval.
    
    Consider dividing these $n$ villages into $m$ intervals, and then determining a post office in each interval.
    
    By mathematical knowledge, for the interval $[i,j]$, the post office should be built at the $\left\lfloor\dfrac{i+j}2\right\rfloor$-th village. Using prefix sums, $w(i,j)$ is easy to compute.
    
    The problem reduces to the interval-partition problem with a restricted number of intervals. It can be proven that the $w$ function satisfies the quadrangle inequality. Just directly apply the above optimization method.

??? note "Implementation 1, the second optimization above, complexity $O(n(n+m))$"
    ```cpp
    --8<-- "docs/dp/code/opt/quadrangle/quadrangle_2.cpp"
    ```

??? note "Implementation 2, WQS binary search, complexity $O(n\log n\log C)$"
    ```cpp
    --8<-- "docs/dp/code/opt/quadrangle/quadrangle_3.cpp"
    ```

## Interval-merging problem

Another class of dynamic-programming problems that can be optimized via the quadrangle inequality is the interval-merging problem, i.e. merging $n$ length-one intervals $[i,i]$ pairwise until obtaining the interval $[1,n]$. Each time $[j,k]$ and $[k+1,i]$ are merged, a cost $w(j,i)$ must be paid. The problem asks to find the lowest-cost way of merging. For this kind of problem, we have the following 2D1D state-transition equation:

$$
f(j,i) = \min_{j \leq k < i} f(j,k) + f(k+1,i) + w(j,i) \qquad (1\le j< i\le n) \tag{3}
$$

where the initial cost $f(i,i)=0$. The total complexity of the brute-force algorithm is $O(n^3)$, and when decision monotonicity exists, it can be optimized to an algorithm complexity of $O(n^2)$. This algorithm was first proposed by Knuth in solving the optimal binary search tree problem, and further studied and summarized by F. Frances Yao; it is called Knuth's optimization or the Knuth-Yao speedup abroad.

Besides the quadrangle inequality, the decision monotonicity of the interval-merging problem also requires the cost function to satisfy interval-inclusion monotonicity.

-   **Interval-inclusion monotonicity**: if for any $a \leq b \leq c \leq d$,

    $$
    w(b,c) \leq w(a,d),
    $$

    holds, then the function $w$ is said to be monotone with respect to interval inclusion.

This is essentially the first-order condition of the cost function, i.e. $w(j,i)$ decreases in $j$ and increases in $i$.

???+ note "Lemma 1"
    If $w$ satisfies interval-inclusion monotonicity and the quadrangle inequality, then the state $f(j,i)$ satisfies the quadrangle inequality.

??? note "Proof"
    Suppose $a \leq b \leq c \leq d$. Below we prove $f(a,d) + f(b,c) \geq f(a,c) + f(b,d)$. Consider induction on $d-a$. When $a=b$ or $c=d$, the desired result is an identity. For the general case, do a case analysis based on the position of $d'=\operatorname{opt}(a,d)$.
    
    First case, $c \leq d'$ or $d' < b$, i.e. $[b,c]$ is contained in $[a,d']$ or $[d'+1,d]$.
    
    Suppose $c \leq d'$; the other case is similar. Then
    
    $$
    \begin{aligned}
    f(a,d) + f(b,c)
    & = f(a,d') + f(d'+1,d) + w(a,d) + f(b,c) \\
    & \geq f(a,c) + f(b,d') + f(d'+1,d) + w(a,d) \\
    & \geq f(a,c) + f(b,d') + f(d'+1,d) + w(b,d) \\
    & \geq f(a,c) + f(b,d).
    \end{aligned}
    $$
    
    Here, the first inequality comes from the inductive hypothesis $f(a,c) + f(b,d') \leq f(a,d') + f(b,c)$, the second comes from interval-inclusion monotonicity $w(b,d) \leq w(a,d)$, and the third comes from the optimality condition $f(b,d) \leq f(b,d') + f(d'+1,d) + w(b,d)$.
    
    Second case, $b \leq d' < c$, i.e. $d'$ lies within $[b,c]$. In this case, consider the position of $c'=\operatorname{opt}(b,c)$.
    
    Suppose $c' \leq d'$, i.e. $[b,c']$ is contained in $[a,d']$; the other case is similar. Then
    
    $$
    \begin{aligned}
    f(a,d) + f(b,c)
    & = f(a,d') + f(d'+1,d) + w(a,d) + f(b,c') + f(c'+1,c) + w(b,c) \\
    & \geq f(a,c') + f(c'+1,c) + w(b,c) + f(b,d') + f(d'+1,d) + w(a,d) \\
    & \geq f(a,c') + f(c'+1,c) + w(a,c) + f(b,d') + f(d'+1,d) + w(b,d) \\
    & \geq f(a,c) + f(b,d).
    \end{aligned}
    $$
    
    Here, the first inequality comes from the inductive hypothesis $f(a,c') + f(b,d') \leq f(a,d') + f(b,c')$, the second comes from the quadrangle inequality $w(a,c) + w(b,d) \leq w(a,d) + w(b,c)$, and the third comes from the optimality conditions of $f(a,c)$ and $f(b,d)$.

???+ note "Theorem 4"
    If $w$ satisfies interval-inclusion monotonicity and the quadrangle inequality, then the smallest optimal decision $\operatorname{opt}(j,i)$ in problem (3) satisfies
    
    $$
    \operatorname{opt}(j,i-1) \leq \operatorname{opt}(j,i) \leq \operatorname{opt}(j+1,i). \qquad (j + 1 < i)
    $$

??? note "Proof"
    Lemma 1 already proved that $f(j,i)$ satisfies the quadrangle inequality, so the objective function $f(j,k) + f(k+1,i) + w(j,i)$, for a given $j$ as a function of $(k,i)$, satisfies the quadrangle inequality, so by Theorem 1, $\operatorname{opt}(j,i-1) \leq \operatorname{opt}(j,i)$. Note that terms not simultaneously containing $(k,i)$ do not affect the quadrangle inequality holding. Similarly, for a given $i$ as a function of $(k,j)$ it also satisfies the quadrangle inequality, so $\operatorname{opt}(j,i) \leq \operatorname{opt}(j+1,i)$. This gives the claim.

Using this conclusion, we can likewise restrict the search range of decision point $k$. Here, traverse the interval length $i-j+1$ in increasing order, then traverse all intervals $[j,i]$ of the same length, brute-force searching all $k$ between $\operatorname{opt}(j,i-1)$ and $\operatorname{opt}(j+1,i)$ to obtain the optimal solution $f(j,i)$ and record the smallest optimal decision $\operatorname{opt}(j,i)$. For all intervals of the same length, the total length of the decision space in this algorithm is $O(n)$, and the number of possible interval lengths is likewise $O(n)$, so the total algorithm complexity is $O(n^2)$.

???+ example "Reference implementation"
    ```cpp
    --8<-- "docs/dp/code/opt/quadrangle/quadrangle-knuth-optimization.cpp:core"
    ```

## Classes of functions satisfying the quadrangle inequality

To more conveniently prove that a function satisfies the quadrangle inequality, we have the following properties:

**Property 1**: if functions $w_1(j,i)$ and $w_2(j,i)$ both satisfy the quadrangle inequality (or interval-inclusion monotonicity), then for any $c_1,c_2\geq 0$, the function $c_1w_1+c_2w_2$ also satisfies the quadrangle inequality (or interval-inclusion monotonicity).

**Property 2**: if there exist functions $f(x)$ and $g(x)$ such that $w(j,i) = f(j)-g(i)$, then the function $w$ satisfies the quadrangle identity. When the functions $f$ and $g$ are monotonically increasing, the function $w$ additionally satisfies interval-inclusion monotonicity.

**Property 3**: let $h(x)$ be a monotonically increasing convex function; if the function $w(j,i)$ satisfies the quadrangle inequality and is monotone with respect to interval inclusion, then the composite function $h(w(j,i))$ also satisfies the quadrangle inequality and interval-inclusion monotonicity.

**Property 4**: let $h(x)$ be a convex function; if the function $w(j,i)$ satisfies the quadrangle identity and is monotone with respect to interval inclusion, then the composite function $h(w(j,i))$ also satisfies the quadrangle inequality.

First we need to clarify one point: the definition of a convex function has divergence in domestic textbooks; the convex function here refers to a lower-convex function, i.e. (when differentiable) a function whose first derivative is monotonically increasing.

??? note "Proof"
    The first two properties are easy to prove by definition; below we prove the third property, and the proof of Property 4 is similar. Since $h(x)$ is monotone, $h(w(j,i))$ naturally preserves monotonicity with respect to interval inclusion. The key is the proof of the quadrangle inequality.
    
    To this end, below we consider the second-order mixed difference on $a \leq j \leq b \leq c \leq i \leq d$.
    
    $$
    \begin{aligned}
    \Delta_i\Delta_j h\left(w(j,i)\right)
    &= h\left(w(b,d)\right) - h\left(w(a,c) + \Delta_jw(j,c) + \Delta_iw(a,i)\right) \\
    &\quad + h\left(w(a,c) + \Delta_jw(j,c) + \Delta_iw(a,i)\right) - h\left(w(a,c) + \Delta_jw(j,c)\right) \\
    &\quad - h\left(w(a,c) + \Delta_iw(a,i)\right) + h\left(w(a,c)\right).
    \end{aligned}
    $$
    
    Here, by interval monotonicity, $\Delta_iw(a,i) := w(a,d) - w(a,c) \geq 0$ and $\Delta_jw(j,c) := w(b,c) - w(a,c) \leq 0$. Since $h(x)$ is convex, for $t_1,t_2\geq 0$, $h(x + t_1 - t_2) - h(x + t_1) \leq h(x - t_2) - h(x)$ holds, so the last two lines are necessarily non-positive. At the same time, by the quadrangle inequality, $w(b,d) \leq w(a,c) + \Delta_jw(j,c) + \Delta_iw(a,i) = w(b,c) + w(a,d) - w(a,c)$, so the difference in the first line, given $h(x)$ monotonically increasing, is also necessarily non-positive. So the total second-order mixed difference is non-positive. This is exactly the quadrangle inequality.
    
    This proof is actually the discrete version of the following derivative proof.
    
    $$
    \frac{\partial^2}{\partial x\partial y}h(w(x,y)) = h''(w(x,y))\frac{\partial }{\partial x}w(x,y)\frac{\partial}{\partial y}w(x,y) + h'(w(x,y))\frac{\partial^2}{\partial x\partial y}w(x,y) \leq 0.
    $$
    
    This clearly holds under the conditions $h' \geq 0$, $h'' \geq 0$, $w_x \leq 0$, $w_y \geq 0$, and $w_{xy} \leq 0$. Here, interval-inclusion monotonicity gives the first-order condition of $w$, and the quadrangle inequality gives its second-order condition.

## Exercises

-   [Codeforces - Ciel and Gondolas](https://codeforces.com/contest/321/problem/E) (Be careful with I/O!)
-   [SPOJ - LARMY](https://www.spoj.com/problems/LARMY/)
-   [Codechef - CHEFAOR](https://www.codechef.com/problems/CHEFAOR)
-   [Hackerrank - Guardians of the Lunatics](https://www.hackerrank.com/contests/ioi-2014-practice-contest-2/challenges/guardians-lunatics-ioi14)
-   [ACM ICPC World Finals 2017 - Money](https://open.kattis.com/problems/money)

## References and notes

-   [Quora Answer by Michael Levin](https://www.quora.com/What-is-divide-and-conquer-optimization-in-dynamic-programming)
-   [Video Tutorial by "Sothe" the Algorithm Wolf](https://www.youtube.com/watch?v=wLXEWuDWnzI)
-   [Divide and Conquer DP](https://cp-algorithms.com/dynamic_programming/divide-and-conquer-dp.html)
-   [Knuth's Optimization](https://cp-algorithms.com/dynamic_programming/knuth-optimization.html)
-   [Quadrangle Inequality Properties](https://codeforces.com/blog/entry/86306)
-   [Wang Qinshi, "An Analysis of a Class of Binary-Search Methods"](https://github.com/hzwer/shareOI/blob/master/%E5%9F%BA%E7%A1%80%E7%AE%97%E6%B3%95/%E6%B5%85%E6%9E%90%E4%B8%80%E7%B1%BB%E4%BA%8C%E5%88%86%E6%96%B9%E6%B3%95_%E7%8E%8B%E9%92%A6%E7%9F%B3.pdf)
-   [Simplified LARSCH Algorithm by noshi91](https://noshi91.hatenablog.com/entry/2023/02/18/005856)
-   [Quadrangle Inequality and Decision Monotonicity by b6e0\_ - Luogu column](https://www.luogu.com.cn/article/h81hh5lk)
-   [A Poor-Man's LARSCH Algorithm for Online Decision Monotonicity by Register\_int - Luogu column](https://www.luogu.com.cn/article/vqf42hah)

[^cmp-min-opt]: The "worse" and "better" mentioned in the algorithm description should both be regarded as describing the lexicographic order of first comparing function values and then comparing decision points. Under this lexicographic order, "better" means either the function value is smaller, or the function value is the same but the decision point is smaller.

[^larsch]: Larmore, Lawrence L., and Baruch Schieber. "On-line dynamic programming with applications to the prediction of RNA secondary structure." Journal of Algorithms 12, no. 3 (1991): 490-515.
