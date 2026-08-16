author: Marcythm, hsfzLZH1, abc1763613206, greyqz, Ir1d, billchenchina, Chrogeek, Enter-tainer, StudyingFather, MrFoodinChina, luoguyuntianming, sshwy, wood3

## Introductory example

???+ note "["HNOI2008" Packing Toys](https://loj.ac/problem/10188)"
    There are $n$ toys arranged in a row; the $i$-th toy has value $c_i$. You are required to divide these $n$ toys into several segments. For a segment $[l,r]$, its cost is $(r-l+\sum_{i=l}^r c_i-L)^2$, where $L$ is a constant. Find the minimum cost of the segmentation.
    
    $1\le n\le 5\times 10^4, 1\le L, c_i\le 10^7$.

### The naive DP approach

Let $f_i$ denote the minimum cost of dividing the first $i$ items into several segments.

State-transition equation: $f_i=\min_{j<i}\{f_j+(i-(j+1)+pre_i-pre_j-L)^2\}=\min_{j<i}\{f_j+(pre_i-pre_j+i-j-1-L)^2\}$.

where $pre_i$ denotes the sum of the first $i$ numbers, i.e. $\sum_{j=1}^i c_j$.

The time complexity of this approach is $O(n^2)$, which cannot solve this problem.

### Optimization

Consider simplifying the state-transition equation above: let $s_i=pre_i+i,L'=L+1$; then $f_i=\min_{j<i}\{f_j+(s_i-s_j-L')^2\}$.

Moving the parts unrelated to $j$ outside, we get

$$
f_i - (s_i-L')^2=\min_{j<i}\{f_j+s_j^2 + 2s_j(L'-s_i) \} 
$$

Consider the slope-intercept form of a linear function $y=kx+b$; rearranging gives $b=y-kx$. We express the information related to $j$ in the form of $y$, express the information related to both $i$ and $j$ as $kx$, and express the information to be minimized (the information related to $i$) as $b$, i.e. the intercept. Specifically, let

$$
\begin{aligned}
x_j&=s_j\\
y_j&=f_j+s_j^2\\
k_i&=-2(L'-s_i)\\
b_i&=f_i-(s_i-L')^2\\
\end{aligned}
$$

Then the transition equation is written as $b_i = \min_{j<i}\{ y_j-k_ix_j \}$. We regard $(x_j,y_j)$ as points on a two-dimensional plane; then $k_i$ denotes the slope of a line and $b_i$ denotes the intercept of a line with slope $k_i$ passing through $(x_j,y_j)$. The problem turns into: choose an appropriate $j$ ($1\le j<i$) to minimize the intercept of the line.

![slope\_optimization](../images/optimization.svg)

As shown in the figure, we translate this line with slope $k_i$ from bottom to top until a point $(x_p,y_p)$ is on this line; then $b_i=y_p-k_ix_p$, and at this point $b_i$ attains its minimum. After computing $f_i$, we add the point $(x_i,y_i)$ into the point set as a new DP decision. So how should we maintain the point set?

It is easy to see that the point that may make $b_i$ attain its minimum must be on the lower convex hull. So when looking for $p$, we do not need to enumerate all $i-1$ points, only consider the points on the convex hull. And in this problem $k_i$ increases with $i$, so we can maintain the convex hull with a monotonic queue.

Specifically, let $K(a,b)$ denote the slope of the line through $(x_a,y_a)$ and $(x_b,y_b)$. Consider the queue $q_l,q_{l+1},\ldots,q_r$, which maintains the points on the lower convex hull. That is, for $l<i<r$, $K(q_{i-1},q_i) < K(q_i,q_{i+1})$ always holds.

We maintain a pointer $e$ to compute the minimum of $b_i$. We need to find an $e$ with $K(q_{e-1},q_e)\le k_i< K(q_e,q_{e+1})$ (in particular, we must handle $e=l$ or $e=r$ specially); then $p=q_e$, i.e. $q_e$ is the optimal decision point for $i$. Since $k_i$ is monotonically increasing, the number of moves of $e$ is amortized $O(1)$.

When inserting a point $(x_i,y_i)$, we must check whether $K(q_{r-1},q_r)<K(q_r,i)$; if the inequality does not hold, pop $q_r$ until it holds. Then insert $i$ at the tail of $q$.

This way we optimize the DP complexity to $O(n)$.

To summarize the algorithm of the above slope-optimization template problem:

1.  Enqueue the initial state.
2.  Each time, use a line $f(i)$ related to $i$ to cut the maintained convex hull, find the optimal decision, and update $dp_i$.
3.  Add the state $dp_i$. If a state (i.e. a point on the convex hull) is no longer on the convex hull after $dp_i$ is added, it needs to be removed before $dp_i$ is added.

Next we introduce advanced applications of slope optimization, combining slope optimization with binary search / divide and conquer / data structures, etc., to maintain DP equations with less nice properties (lacking some monotonicity properties).

## Optimizing DP with binary search, CDQ, or balanced trees

When we look for the optimal decision at point $i$, we use a line $f(i)$ related to $i$ to cut the maintained convex hull. The point cut is the optimal decision.

In the above example, the slope of the line changes monotonically with $i$, but for some problems the slope is not monotonic. Then we need to maintain every node on the convex hull, and each time use the current line to cut this convex hull. This process can be solved with binary search, because the slopes of two adjacent points on the convex hull have monotonicity.

???+ note "Packing Toys, revised"
    There are $n$ toys arranged in a row; the $i$-th toy has value $c_i$. You are required to divide these $n$ toys into several segments. For a segment $[l,r]$, its cost is $(r-l+\sum_{i=l}^r c_i-L)^2$, where $L$ is a constant. Find the minimum cost of the segmentation.
    
    $1\le n\le 5\times 10^4,1\le L\le 10^7,-10^7\le c_i\le 10^7$.

The only difference between this problem and the "Packing Toys" problem is that the value of a toy can be negative. Continuing the previous approach, let $f_i$ denote the minimum cost of dividing the first $i$ items into several segments.

State-transition equation: $f_i=\min_{j<i}\{f_j+(pre_i-pre_j+i-j-1-L)^2\}$.

where $pre_i = \sum_{j=1}^i c_j$.

Making the same transformation of the equation,

$$
f_i - (s_i-L')^2=\min_{j<i}\{f_j+s_j^2 + 2s_j(L'-s_i) \} 
$$

However, now two conditions no longer hold:

1.  The slope of the line is no longer monotonic;
2.  The x-coordinate of each newly added decision point is no longer monotonic.

We still consider maintaining the convex hull.

When looking for the optimal decision point, i.e. cutting the convex hull with a line, we change finding the front of the monotonic queue to: binary search on the convex hull. We binary-search for the convex-hull edge whose slope is closest to the line's slope, and thereby find the optimal decision.

When adding a decision point, i.e. adding a point to the convex hull, we have two ways to maintain it.

The first method is to directly maintain the convex hull with a balanced tree. Then the binary-search operation for finding the decision point turns into binary search on the balanced tree, and inserting a decision point turns into inserting a node into the balanced tree and deleting several points kicked out of the convex hull. This method is concise in idea but tedious to implement.

Below we introduce an approach based on [CDQ divide and conquer](../../misc/cdq-divide.md).

Let $\text{CDQ}(l,r)$ denote computing $f_i,i\in [l,r]$. Consider $\text{CDQ}(1,n)$:

-   We first call $\text{CDQ}(1,mid)$ to compute $f_i,i\in[1,mid]$. Then we build a convex hull for the decision points in the interval $[1,mid]$, and use this convex hull to update $f_i,i\in [mid+1,n]$. At this point our decision-point set is fixed, unlike before where we add decision points while computing DP values, so we can first sort the $f_i$ for $i \in [mid+1,n]$ by the line's slope $k_i$, and then use a monotonic queue to compute the DP values. Of course, we can also binary-search on the static convex hull to compute the DP values.

-   For each point in $[mid+1,n]$, if the position of its optimal decision is in the interval $[1,mid]$, it will be updated to its optimal answer in this step. When this step is done, we find that all points in $[1,mid]$ have played their full role, and whether they exist in the convex hull no longer affects subsequent answer updates. Therefore we can directly discard the decision points of this interval, and use $\text{CDQ}(mid+1,n)$ to solve the remaining problem of the right interval.

Time complexity $O(n\log^2 n)$.

Comparing "Packing Toys" and "Packing Toys, revised", we can summarize the following two points:

-   Binary search / CDQ / balanced trees, etc., can optimize the computation of the DP equation and reduce the complexity to a certain extent, but they cannot change the equation itself.
-   The properties of a DP equation depend on the characteristics of the data, but the DP equation itself depends on the mathematical model in the problem.

## Summary

Slope-optimization DP requires flexible application; its purpose is to turn an optimization problem into an intercept-extremum problem related to the convex hull on a two-dimensional plane. When encountering equations with less nice properties, sometimes we need to supplement it with data structures; in that case, please analyze case by case.

## Exercises

-   ["SDOI2016" The Journey](https://loj.ac/problem/2035)
-   ["ZJOI2007" Warehouse Construction](https://loj.ac/problem/10189)
-   ["APIO2010" Special Task Force](https://loj.ac/problem/10190)
-   ["JSOI2011" Lemon](https://www.luogu.com.cn/problem/P5504)
-   ["Codeforces 311B" Cats Transport](http://codeforces.com/problemset/problem/311/B)
-   ["NOI2007" Currency Exchange](https://loj.ac/problem/2353)
-   ["NOI2019" The Way Home](https://loj.ac/problem/3156)
-   ["NOI2016" The King Drinks Water](https://uoj.ac/problem/223)
-   ["NOI2014" Ticket Buying](https://uoj.ac/problem/7)
