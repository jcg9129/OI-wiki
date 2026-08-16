This page mainly introduces rotating calipers.

## Introduction

The Rotating Calipers algorithm, on the basis of the convex hull algorithm, by enumerating a certain edge on the convex hull while maintaining other needed points, can solve, in linear time, problems related to convex hull properties such as the convex hull diameter and minimum rectangle covering.

???+ note "Chinese name of the algorithm"
    A relatively common Chinese name for this algorithm is "旋转卡壳" (rotating and getting stuck). It can be understood as: according to the edge we enumerate, we can draw a line either parallel or perpendicular from each maintained point; to ensure optimality for the currently enumerated edge, our task is to make these lines exactly "clamp" the convex hull. And edges are usually enumerated in the order of rotating toward a certain direction, so the whole process is edges "rotating" and edges "getting stuck".
    
    The literal translation of its English name "rotating calipers" should be "旋转卡尺", where "calipers" means "卡尺" (calipers). The original meaning of the paper[^ref1] that first proposed this term is: after clamping the convex hull with a dynamically-adjustable "caliper", "rotate" this "caliper" around the convex hull.

## Finding the convex hull diameter

???+ note "Example problem 1: [Luogu P1452 Beauty Contest G](https://www.luogu.com.cn/problem/P1452)"
    Given $n$ points in the plane, find the longest distance among all pairs of points. ($2\leq n \leq 50000,|x|,|y| \leq 10^4$)

### Process

First use any convex hull algorithm to find the convex hull of all given points; the pair of points with the longest distance must be on the convex hull. And because of the shape of the convex hull, we find that traversing the edges of the convex hull counterclockwise, and finding for each edge the point farthest from this edge, then as the edge rotates, the corresponding farthest point also rotates counterclockwise, with no reversal, which means we can, while enumerating the edges of the convex hull counterclockwise, record and maintain a current farthest point, and continually compute and update the answer.

The array after finding the convex hull is naturally arranged in counterclockwise order, but remember to append node 1 at the bottom-left in advance to the end of the array, so that when enumerating edges $(i,i+1)$ one by one, all edges can be enumerated.

![](images/rotating-calipers1.png)

During enumeration, for each edge, check whether the distance from $j+1$ to edge $(i,i+1)$ is greater than that of $j$; if so, increment $j$ by one; otherwise it means $j$ is the optimal point for this edge. When judging the distance from a point to an edge, one can use the cross product to compute the areas of two triangles separately (as in the figure, the areas of the two triangles, yellow and blue, with the same base) and compare directly.

### Implementation

???+ note "Core code"
    === "C++"
        ```cpp
        int sta[N], top;  // store the node numbers on the convex hull in a stack; the first and last node numbers are the same

        ll pf(ll x) { return x * x; }

        ll dis(int p, int q) { return pf(a[p].x - a[q].x) + pf(a[p].y - a[q].y); }

        ll sqr(int p, int q, int y) { return abs((a[q] - a[p]) * (a[y] - a[q])); }

        ll mx;

        void get_longest() {  // find the convex hull diameter
          int j = 3;
          if (top < 4) {
            mx = dis(sta[1], sta[2]);
            return;
          }
          for (int i = 1; i < top; ++i) {
            while (sqr(sta[i], sta[i + 1], sta[j]) <=
                   sqr(sta[i], sta[i + 1], sta[j % top + 1]))
              j = j % top + 1;
            mx = max(mx, max(dis(sta[i + 1], sta[j]), dis(sta[i], sta[j])));
          }
        }
        ```
    
    === "Python"
        ```python
        sta = [0] * N
        top = 0  # store the node numbers on the convex hull in a stack; the first and last node numbers are the same
        
        
        def pf(x):
            return x * x
        
        
        def dis(p, q):
            return pf(a[p].x - a[q].x) + pf(a[p].y - a[q].y)
        
        
        def sqr(p, q, y):
            return abs((a[q] - a[p]) * (a[y] - a[q]))
        
        
        def get_longest():  # find the convex hull diameter
            j = 3
            if top < 4:
                mx = dis(sta[1], sta[2])
                return
            for i in range(1, top):
                while sqr(sta[i], sta[i + 1], sta[j]) <= sqr(
                    sta[i], sta[i + 1], sta[j % top + 1]
                ):
                    j = j % top + 1
                mx = max(mx, max(dis(sta[i + 1], sta[j]), dis(sta[i], sta[j])))
        ```

## Finding the minimum rectangle covering

[Luogu P3187 Minimum Rectangle Covering](https://www.luogu.com.cn/problem/P3187)

Given the coordinates of some points, find the minimum-area rectangle that can cover all the points. ($3\leq n \leq 50000$)

### Process

With the previous problem as a foundation, a relatively intuitive idea for this problem is still to use the rotating calipers method, but this time what is asked is the area; maintaining only one optimal point as in the previous problem can only find a pair of parallel lines with the minimum distance, and we also need to determine the left and right boundaries of the rectangle. So this time we need to maintain three points: one point opposite the enumerated line, and two points on different sides. The optimal point opposite is still compared using the cross product to compute the area; at this point comparing the area is comparing one side length of this rectangle. The optimal points on the sides are compared using the dot product, because comparing the dot product is comparing the length of the projection, and adding the left and right projection lengths can represent the other side length of this rectangle. The optimality of these two side lengths is mutually independent, so finding the positions of the three optimal points determines the minimum area of the rectangle that can cover all points when one edge of the rectangle is on the line where the current edge lies.

![](images/rotating-calipers2.png)

Finally when counting the answer, if the problem does not require finding all four vertices, there is actually a relatively clever way to directly compute the area of the rectangle using the cross product and dot product. Let twice the area of the purple part be $S$; then the final area is

$$
S\times (|\overrightarrow{AD}\cdot \overrightarrow{AB}|+|\overrightarrow{BC}\cdot \overrightarrow{BA}|-|\overrightarrow{AB}\cdot \overrightarrow{BA}|)/|\overrightarrow{AB}\cdot \overrightarrow{BA}|
$$

### Implementation

The necessary convex-hull-finding process is omitted; here we paste the core code of this problem:

???+ note "Core code"
    === "C++"
        ```cpp
        void get_biggest() {
          int j = 3, l = 2, r = 2;
          double t1, t2, t3, ans = 2e10;
          for (int i = 1; i < top; ++i) {
            while (sqr(sta[i], sta[i + 1], sta[j]) <=
                   sqr(sta[i], sta[i + 1], sta[j % top + 1]))
              j = j % top + 1;
            while (dot(sta[i + 1], sta[r % top + 1], sta[i]) >=
                   dot(sta[i + 1], sta[r], sta[i]))
              r = r % top + 1;
            if (i == 1) l = r;
            while (dot(sta[i + 1], sta[l % top + 1], sta[i]) <=
                   dot(sta[i + 1], sta[l], sta[i]))
              l = l % top + 1;
            t1 = sqr(sta[i], sta[i + 1], sta[j]);
            t2 = dot(sta[i + 1], sta[r], sta[i]) + dot(sta[i + 1], sta[l], sta[i]);
            t3 = dot(sta[i + 1], sta[i + 1], sta[i]);
            ans = min(ans, t1 * t2 / t3);
          }
        }
        ```
    
    === "Python"
        ```python
        def get_biggest():
            j = 3
            l = 2
            r = 2
            ans = 2e10
            for i in range(1, top):
                while sqr(sta[i], sta[i + 1], sta[j]) <= sqr(
                    sta[i], sta[i + 1], sta[j % top + 1]
                ):
                    j = j % top + 1
                while dot(sta[i + 1], sta[r % top + 1], sta[i]) >= dot(
                    sta[i + 1], sta[r], sta[i]
                ):
                    r = r % top + 1
                if i == 1:
                    l = r
                while dot(sta[i + 1], sta[l % top + 1], sta[i]) <= dot(
                    sta[i + 1], sta[l], sta[i]
                ):
                    l = l % top + 1
                t1 = sqr(sta[i], sta[i + 1], sta[j])
                t2 = dot(sta[i + 1], sta[r], sta[i]) + dot(sta[i + 1], sta[l], sta[i])
                t3 = dot(sta[i + 1], sta[i + 1], sta[i])
                ans = min(ans, t1 * t2 / t3)
        ```

## Practice

-   [POJ 3608. Bridge Across Islands](http://poj.org/problem?id=3608)
-   [2011 ACM-ICPC World Finals, Problem K. Trash Removal](https://codeforces.com/gym/101175)
-   [ICPC WF Moscow Invitational Contest - Online Mirror, Problem F. Framing Pictures](https://codeforces.com/contest/1578/problem/F)

## References and notes

[^ref1]: Toussaint, Godfried T. (1983). "Solving geometric problems with the rotating calipers". Proc. MELECON '83, Athens. CiteSeerX 10.1.1.155.5671

-   <https://en.wikipedia.org/wiki/Rotating_calipers>

-   <http://www-cgrl.cs.mcgill.ca/~godfried/research/calipers.html>

-   Shamos, Michael (1978). "Computational Geometry" (PDF). Yale University. pp. 76–81.
