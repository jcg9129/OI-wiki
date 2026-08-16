## Introduction

Given $n$ points on the two-dimensional plane, find a pair of points with the closest Euclidean distance.

Below we introduce a divide-and-conquer algorithm with time complexity $O(n\log n)$ to solve this problem. This algorithm was proposed in 1975 by [Franco P. Preparata](https://en.wikipedia.org/wiki/Franco_P._Preparata); Preparata and [Michael Ian Shamos](https://en.wikipedia.org/wiki/Michael_Ian_Shamos) proved that this algorithm is optimal under the decision-tree model.

## Process

As with a conventional divide-and-conquer algorithm, we split this set of $n$ points into two equal-sized sets $S_1, S_2$, and continually recurse down. But we encounter a difficulty: how to merge? That is, how to find the closest pair of points where one point is in $S_1$ and the other is in $S_2$? Here we first assume the time complexity of the merge operation is $O(n)$, and we can know the total complexity of the algorithm is $T(n) = 2T(\frac{n}{2}) + O(n) = O(n\log n)$.

We first sort all points with $x_i$ as the first key and $y_i$ as the second key, and use the point $p_m (m = \lfloor \frac{n}{2} \rfloor)$ as the boundary point to split the point set into $A_1,A_2$:

$$
\begin{aligned}
A_1 &= \{p_i \ \big | \ i = 0 \ldots m \}\\
A_2 &= \{p_i \ \big | \ i = m + 1 \ldots n-1 \}
\end{aligned}
$$

and recurse down to find the closest pairs of points within each of the two point sets, letting the distances be $h_1,h_2$, and take the smaller value as $h$.

Now it is time to merge! We try to find such a pair of points, one belonging to $A_1$, the other belonging to $A_2$, with a distance between them less than $h$. Therefore we put all points whose x-coordinate differs from $x_m$ by less than $h$ into the set $B$:

$$
B = \{ p_i \ \big | \ \lvert x_i - x_m \rvert < h \}
$$

Combining with the figure, the line $m$ divides the points into two parts. The left of $m$ is the point set $A_1$, and the right is the point set $A_2$.

Then by the rule $B = \{ p_i \ \big | \ \lvert x_i - x_m \rvert < h \}$, we obtain the point set $B$ composed of the green points. ![nearest-points1](./images/nearest-points1.png)

For each point $p_i$ in $B$, our current goal is to find a point that is also in $B$ and whose distance to it is less than $h$. To avoid considering two points with respect to each other, we only consider those points whose y-coordinate is smaller than $y_i$. Obviously, for a valid point $p_j$, $y_i - y_j$ must be less than $h$. So we obtain a set $C(p_i)$:

$$
C(p_i) = \{ p_j\ \big |\ p_j \in B,\ y_i - h < y_j \le y_i \}
$$

Choosing a point $p_i$ in the point set $B$, by the rule $C(p_i) = \{ p_j\ \big |\ p_j \in B,\ y_i - h < y_j \le y_i \}$, we obtain the point set $C$ composed of the yellow points inside the red box.

![nearest-points2](./images/nearest-points2.png)

If we sort the points in $B$ by $y_i$, $C(p_i)$ will be easily obtained, i.e. the several consecutive points immediately adjacent to $p_i$.

From this we obtain the merge steps:

1.  Construct the set $B$.
2.  Sort the points in $B$ by $y_i$. The usual approach is $O(n\log n)$, but we can change the strategy to optimize to $O(n)$ (explained below).
3.  For each $p_i \in B$, consider $p_j \in C(p_i)$; for each pair $(p_i,p_j)$, compute the distance and update the answer (the closest pair of points in the current set).

Note that we mentioned two sorts above; because the point coordinates do not change throughout, the first sort can be performed only once before the divide-and-conquer begins. We let each recursion return the current point set sorted by $y_i$; for the second sort, the upper level directly merges the two separately-sorted point sets from the lower level.

It seems this algorithm is still not optimal; $|C(p_i)|$ will be on the order of $O(n)$, causing the total complexity to be incorrect. Actually this is not so; its maximum size is $7$, and we give its proof:

## Complexity proof

We already know that the y-coordinates of all points in $C(p_i)$ are within the range $(y_i-h,y_i]$; and the x-coordinates of all points in $C(p_i)$, and $p_i$ itself, are within the range $(x_m-h,x_m+h)$. This constitutes a $2h \times h$ rectangle.

We then split this rectangle into two $h \times h$ squares; not considering $p_i$, the points in one of the squares are $C(p_i) \cap A_1$, and the other is $C(p_i) \cap A_2$, and the distance between any two points within the two squares is greater than $h$. (because they come from the same lower-level recursion)

We split an $h \times h$ square into four $\frac{h}{2} \times \frac{h}{2}$ small squares. We can find that each small square has at most $1$ point: because the maximum distance between any two points in that small square is the length of the diagonal, i.e. $\frac{h}{\sqrt 2}$, which is less than $h$.

![nearest-points3](./images/nearest-points3.png)

From this, each square has at most $4$ points, and the rectangle has at most $8$ points; removing $p_i$ itself, $\max(C(p_i))=7$.

???+ example "Reference implementation"
    ```cpp
    --8<-- "docs/geometry/code/nearest-points/nearest-points_1.cpp"
    ```

## Generalization: minimum-perimeter triangle in the plane

The above algorithm interestingly generalizes to this problem: among a given set of points, choose three points such that the sum of their pairwise distances is minimized.

The algorithm remains largely unchanged; each time we try to find a triangle with a perimeter smaller than the current answer $d$, put all points whose x-coordinate differs from $x_m$ by less than $\frac{d}{2}$ into the set $B$, and try to update the answer. (the longest side of a triangle with perimeter $d$ is less than $\frac{d}{2}$)

## Non-divide-and-conquer algorithm

Actually, besides the divide-and-conquer algorithm mentioned above, there is another non-divide-and-conquer algorithm whose time complexity is likewise $O(n \log n)$.

We can consider a common idea for statistical sequences: for each element, add the contribution of it and all elements to its left into the answer. The planar closest-pair problem can likewise use this idea.

Specifically, we sort all points with $x_i$ as the first key and $y_i$ as the second key, and establish a multiset keyed on $y_i$. For each position $i$, we perform the following operations:

1.  Delete all points satisfying $x_i - x_j \ge d$ from the set. They will no longer contribute to the answer.
2.  For all points in the set satisfying $\lvert y_i - y_j \rvert < d$, count their distance from $p_i$.
3.  Insert $p_i$ into the set.

Since each point is inserted and deleted at most once, the time complexity of inserting and deleting points is $O(n \log n)$, and the time-complexity proof of the answer-counting part is similar to the time-complexity proof of the divide-and-conquer algorithm; the reader may as well try it.

??? example "Reference implementation"
    ```cpp
    --8<-- "docs/geometry/code/nearest-points/nearest-points_2.cpp"
    ```

## Expected-linear approach

Actually, besides the approach with time complexity $O(n \log n)$ mentioned above, there is another algorithm with **expected** complexity $O(n)$.

First [randomly shuffle](../misc/random.md#shuffle) the pairs of points; we will maintain the answer for prefix point sets. Consider deriving the answer for the $i$-th point from the first $i - 1$ points.

Denote the closest-pair distance of the first $i - 1$ points as $s$; we divide the plane into several grids with side length $s$, and store the points in each grid (using a [hash table](../ds/hash.md)), then check all points in the surrounding nine grids of the grid where the $i$-th point lies, and update the answer. Note that the number of points to check is $O(1)$, because the closest-pair distance of the first $i - 1$ points is $s$, so each grid has no more than $4$ points.

If during this process the answer is updated, we rebuild the grid graph, otherwise not. Among the first $i$ points, the probability that the closest pair contains $i$ is $O\left(\frac{1}{i}\right)$, and the cost of rebuilding the grid is $O(i)$, so the expected cost of the $i$-th point is $O(1)$. So for $n$ points, this algorithm is expected $O(n)$.

## Exercises

-   [UVa 10245 "The Closest Pair Problem" \[Difficulty: low\]](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1186)
-   [SPOJ #8725 CLOPPAIR "Closest Point Pair" \[Difficulty: low\]](https://www.spoj.com/problems/CLOPPAIR/)
-   [CODEFORCES Team Olympiad Saratov - 2011 "Minimum amount" \[Difficulty: medium\]](http://codeforces.com/contest/120/problem/J)
-   [SPOJ #7029 CLOSEST "Closest Triple" \[Difficulty: medium\]](https://www.spoj.com/problems/CLOSEST/)
-   [Google Code Jam 2009 Final "Min Perimeter" \[Difficulty: medium\]](https://github.com/google/coding-competitions-archive/blob/main/codejam/2009/world_finals/min_perimeter/statement.pdf)

## References and further reading

**The divide-and-conquer algorithm part of this page is mainly translated from the blog post [Нахождение пары ближайших точек](http://e-maxx.ru/algo/nearest_points) and its English translation [Finding the nearest pair of points](https://github.com/e-maxx-eng/e-maxx-eng/blob/master/src/geometry/nearest_points.md). The Russian version's copyright license is Public Domain + Leave a Link; the English version's copyright license is CC-BY-SA 4.0.**

[Zhihu column: Computational Geometry - The Closest Pair Problem](https://zhuanlan.zhihu.com/p/74905629)
