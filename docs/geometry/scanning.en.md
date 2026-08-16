## Introduction

The scan line is generally applied to figures; it is very similar to its literal meaning, i.e. a line scanning back and forth across the whole figure; it is generally used to solve problems such as the area and perimeter of figures, and two-dimensional point counting.

## Two-dimensional rectangle area union problem

In a two-dimensional coordinate system, given the bottom-left and top-right coordinates of multiple rectangles, find the area of the figure composed of all rectangles.

### Process

From the figure, we can see that the total area can be found directly by brute force; but what if the data becomes large? At this point we need to talk about the **scan line** algorithm.

Now suppose we have a line, scanning from bottom to top:

![](./images/scanning.svg)

As shown, divide the whole rectangle into small rectangles of different colors as in the figure; the height of a small rectangle is the distance scanned, however the horizontal width of the rectangle keeps changing.

Mark the top and bottom edges of each rectangle; mark the bottom edge as 1 and the top edge as -1. Each time a horizontal edge is encountered, add the mark of this edge to the weight of this edge (on its projection interval on the horizontal axis).

???+ note "Note"
    This operation is similar to traversing a bracket sequence: an open bracket adds 1, a close bracket subtracts 1; the "weight" corresponds to the depth at the current position, and whether the "weight" is greater than 0 corresponds to whether we are currently inside brackets, i.e. whether this interval is counted into the width of the small rectangle.

The width of the small rectangles (not necessarily only one) is the total length of the intervals on the whole number axis where the weight is greater than 0.

### Implementation

Use a segment tree to maintain the length of the rectangles, i.e. the points on the whole number axis whose covering count is greater than 0. The requirements are listed as follows:

-   Add 1 or subtract 1 to the weight of an interval.
-   Count, on the whole number axis, the "sum of interval lengths" where the interval weight is greater than 0.

If you try to implement it directly with an ordinary segment tree template, you may encounter some frustration. Specifically, since during interval add, even if the modification interval and the interval managed by the node overlap, we still cannot know in constant time how the covering count changes. This is because we cannot directly know: how long an interval within the managed range will change from 1 to 0 (or from 0 to 1).

This problem can be implemented with only naive divide-and-conquer: maintain, for the interval managed by each node, two pieces of information: "the number of times the interval is completely covered `v[]`" (similar to a lazy tag that need not be pushed down) and "the covered length `w[]`".

[Discretization](../misc/discrete.md) is needed.

??? note "[Luogu P5490 【Template】Scan Line & Rectangle Area Union](https://www.luogu.com.cn/problem/P5490) reference code"
    ```cpp
    --8<-- "docs/geometry/code/scanning/scanning_1.cpp"
    ```

??? note "[「POJ 1151」Atlantis](http://poj.org/problem?id=1151) reference code"
    ```cpp
    --8<-- "docs/geometry/code/scanning/scanning_2.cpp"
    ```

### Practice

-   [「POJ1177」Picture](http://poj.org/problem?id=1177)
-   [「POJ3832」Posters](http://poj.org/problem?id=3832)
-   [Luogu P1856 \[IOI1998\] \[USACO5.5\] Rectangle Perimeter Picture](https://www.luogu.com.cn/problem/P1856)
    -   The contribution of a horizontal edge is the change in the covered length.
    -   Computing once in each of the two directions can avoid the discussion of vertical edges.
    -   When sorting operations, note to consider the case where the edges of two rectangles coincide.
    -   The data range allows not using a segment tree, and directly simulating in quadratic time.

## B-dimensional orthogonal range

A B-dimensional orthogonal range refers to, in a B-dimensional Cartesian coordinate system, the point set inside where the $i$-th dimension coordinate is within an integer range $[l_i,r_i]$.

Generally, a one-dimensional orthogonal range is abbreviated as an interval, a two-dimensional orthogonal range is abbreviated as a rectangle, and a three-dimensional orthogonal range is abbreviated as a cube (what we commonly call two-dimensional point counting is a two-dimensional orthogonal range).

For a static two-dimensional problem, we can use a scan line to scan one dimension and a data structure to maintain the other dimension.
During the process of the scan line scanning from left to right, some modifications and queries are produced on the dimension maintained by the data structure.
If the queried information can be differenced, then directly use differencing, otherwise divide-and-conquer is needed. Differencing is generally maintained with a Fenwick tree or a segment tree, but because the Fenwick tree is easy to write and has a small constant factor, most people choose to use a Fenwick tree for maintenance. Divide-and-conquer is generally CDQ divide-and-conquer (but divide-and-conquer is not involved here).

Another perspective on the problem that is relatively easy to understand is to stand from the sequence perspective, rather than the two-dimensional plane perspective. If we view the problem this way, then the scan line actually enumerates the right endpoint $r=1\cdots n$, maintains a data structure supporting querying, for the current $r$, given a value $l$, what the answer from $l$ to $r$ is. That is, the scan line scans the right endpoint of queries, and the data structure maintains the answer for all left endpoints, or in other words, traverse one dimension, and the data structure maintains the other dimension.

The complexity is generally $O((n+m)\log n)$.

## Two-dimensional point counting

Given a sequence of length $n$, there are $m$ queries; each query asks the number of elements in the interval $[l,r]$ whose value is within $[x,y]$.

This problem is called two-dimensional point counting. We can find it is equivalent to querying the count of points inside a rectangle on a two-dimensional plane. Here we discuss the simplest handling method for this problem, scan line + Fenwick tree.

Obviously, this problem is a static two-dimensional problem; through the scan line we can convert the static two-dimensional problem into a dynamic one-dimensional problem. To maintain the dynamic one-dimensional problem, use a data structure to maintain a sequence; here a Fenwick tree can be used.

First discretize all queries, and use a Fenwick tree to maintain the weights; for the $l$ and $r$ of each query, when we enumerate to $l-1$ we count the number $a$ of numbers currently within the interval $[x,y]$; continuing to enumerate backward, when we enumerate to $r$ we count the number $b$ of numbers currently within the interval $[x,y]$; $b-a$ is the answer of this query.

### Example problems

???+ note "[Luogu P2163 \[SHOI2007\] The Gardener's Trouble](https://www.luogu.com.cn/problem/P2163)"
    First discretize. Let a rectangle with bottom-left corner $(0, 0)$ and top-right corner $(x, y)$ contain $ans_{x, y}$ points. Then the answer of a query can be differenced as $ans_{c, d} - ans_{a - 1, d} - ans_{c, b - 1} + ans_{a - 1, b - 1}$.
    
    ??? note "Code"
        ```cpp
        --8<-- "docs/geometry/code/scanning/scanning_3.cpp"
        ```

???+ note "[Luogu P1908 Inversions](https://www.luogu.com.cn/problem/P1908)"
    That's right, inversions can also be done using the scan-line idea. Consider converting counting the number of inversions into enumerating each position $i$ from back to front, and finding the number of points in the interval $[i+1,n]$ whose size is within the interval $[0,a_i]$. The data range in the problem is $10^9$, so obviously discretization must be done first; we can consider traversing the array from back to front, updating the Fenwick tree (segment tree) each time we traverse to a number, and then counting how many numbers are currently smaller than the currently enumerated number; because we traverse from back to front, the number of numbers smaller than the current value is the number of its inversions, which can be done with single-point modification and interval query using a Fenwick tree or segment tree.
    
    ??? note "Code"
        ```cpp
        --8<-- "docs/geometry/code/scanning/scanning_4.cpp"
        ```

???+ note "[Luogu P1972 \[SDOI2009\] HH's Necklace](https://www.luogu.com.cn/problem/P1972)"
    Brief problem meaning: given a sequence, query multiple times how many different kinds of numbers there are in the interval $[l,r]$.
    
    For this kind of problem we can consider deriving properties, and then use the scan line to enumerate all right endpoints while the data structure maintains the answer for each left endpoint; we can also convert the problem to a two-dimensional plane, turning it into a rectangle-query-information problem.
    
    In this problem, we let the previous occurrence position of $a_i$ in the sequence be $pre_i$; if $a_i$ has not appeared, then $pre_i = 0$. According to the problem, if a kind of number appears multiple times in the interval, it only produces one contribution. We may as well consider that the position where each kind of number produces a contribution is the first occurrence position in the interval; at this point we can find that the total contribution produced is the number of $pre_x \le l - 1$, easily proved by contradiction.
    
    Now the problem is: given a sequence $pre$, query multiple times how many $pre_i \le l - 1$ there are in the interval $[l,r]$.
    
    We can regard $pre_i$ as a point on the two-dimensional plane: $i$ is the x-coordinate, $pre_i$ is the y-coordinate, and the problem is transformed into a two-dimensional point counting problem: each query asks how many points there are in the rectangle with bottom-left corner $(l,0)$ and top-right corner $(r,l - 1)$.
    
    Note that this query can be differenced; we can difference the query into how many points there are in the rectangle with bottom-left corner $(0,0)$ and top-right corner $(r,l - 1)$ minus the rectangle with bottom-left corner $(0,0)$ and top-right corner $(l - 1,l - 1)$, which conveniently lets us use the scan-line idea.
    
    The complexity of a single operation is $O(\log n)$; there are $n$ add-point operations and $2m$ query operations in total, and the total time complexity is $O((n + m) \log n)$.
    
    ??? note "Code"
        ```cpp
        --8<-- "docs/geometry/code/scanning/scanning_5.cpp"
        ```

### Practice

-   [Luogu P8593 「KDOI-02」Throwing a Bomb](https://www.luogu.com.cn/problem/P8593) an application of inversions.
-   [AcWing 4709. Triples](https://www.acwing.com/problem/content/4712/) a weakened version of the above problem, likewise an application of inversions.
-   [Luogu P8773 \[Lanqiao Cup 2022 Provincial A\] Choosing Numbers XOR](https://www.luogu.com.cn/problem/P8773) a modified version of HH's Necklace.
-   [Luogu P8844 \[Chuanzhi Cup #4 Preliminary\] Little Ka and Falling Leaves](https://www.luogu.com.cn/problem/P8844) converting a tree problem into a sequence problem and then performing two-dimensional point counting.

In summary, the main idea of two-dimensional point counting is to use a data structure to maintain one dimension, and then enumerate the other dimension.

## References

-   [cnblogs/Yang1208: Scan line explanation, dynamically-allocated segment tree](https://www.cnblogs.com/yangsongyi/p/8378629.html)
-   [csdn/riba2534: POJ1151 Atlantis solution](https://blog.csdn.net/riba2534/article/details/76851233)
-   [csdn/Daodaogou 0102: POJ1151 Atlantis solution](https://blog.csdn.net/winddreams/article/details/38495093)
-   [A brief discussion of the scan line](https://www.luogu.com.cn/article/f8q5bmnz)
