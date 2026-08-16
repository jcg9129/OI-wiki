## Two-dimensional convex hull

### Definition

#### Convex polygon

A convex polygon is a **simple polygon** all of whose interior angles are in the range $[0,\pi]$.

#### Convex hull

The smallest convex polygon in the plane that can contain all given points is called the convex hull.

Its definition is: for a given set $X$, the intersection $S$ of all convex sets containing $X$ is called the **convex hull** of $X$.

It can actually be understood as the shape of using a rubber band to enclose all given points.

The convex hull encloses all given points with the minimum perimeter. If a concave polygon encloses all the points, its perimeter must not be the smallest, as shown in the figure below. By the triangle inequality, a convex polygon must be optimal in terms of perimeter.

![](./images/ch.png)

### Andrew's algorithm for the convex hull

Commonly-used methods include Graham's scan and Andrew's algorithm; here we mainly introduce Andrew's algorithm.

#### Properties

The time complexity of this algorithm is $O(n\log n)$, where $n$ is the size of the point set for which the convex hull is to be found; the complexity bottleneck lies in the two-key sorting of all point coordinates.

#### Process

First sort all points with the x-coordinate as the first key and the y-coordinate as the second key.

Obviously, after sorting, the smallest element and the largest element must be on the convex hull. And because it is a convex polygon, if we start from a point and walk counterclockwise, the trajectory is always "turning left"; once a right turn appears, it means this segment is not on the convex hull. Therefore we can use a monotonic stack to maintain the upper and lower hulls.

Because looking from left to right, the upper and lower hulls rotate in different directions, in order to make the monotonic stack work, we first **enumerate in ascending order** to find the lower hull, then **in descending order** find the upper hull.

When finding the hull, once we find that the direction of travel of the point about to be pushed ($P$) and the top two points of the stack ($S_1,S_2$, where $S_1$ is the top of the stack) rotates to the right, i.e. the cross product is less than $0$: $\overrightarrow{S_2S_1}\times \overrightarrow{S_1P}<0$, then pop the top of the stack, go back to the previous step, and continue checking, until $\overrightarrow{S_2S_1}\times \overrightarrow{S_1P}\ge 0$ or only one element remains in the stack.

Usually there is no need to retain points located on the edges of the convex hull, so the "$<$" in the condition $\overrightarrow{S_2S_1}\times \overrightarrow{S_1P}<0$ in the paragraph above can be changed to $\le$ as appropriate, and the latter condition should be changed to $>$.

![Andrew](./images/andrew.svg)

#### Implementation

???+ note "Code implementation"
    === "C++"
        ```cpp
        // stk[] is integer-typed, storing indices
        // p[] stores vectors or points
        tp = 0;                       // initialize the stack
        std::sort(p + 1, p + 1 + n);  // sort the points
        stk[++tp] = 1;
        // add the first element to the stack, and do not update used, so that 1 also updates the monotonic stack when finally closing the convex hull
        for (int i = 2; i <= n; ++i) {
          while (tp >= 2  // the * operator in the next line is overloaded as cross product
                 && (p[stk[tp]] - p[stk[tp - 1]]) * (p[i] - p[stk[tp]]) <= 0)
            used[stk[tp--]] = 0;
          used[i] = 1;  // used means on the hull
          stk[++tp] = i;
        }
        int tmp = tp;  // tmp is the size of the lower hull
        for (int i = n - 1; i > 0; --i)
          if (!used[i]) {
            // ↓finding the upper hull does not affect the lower hull
            while (tp > tmp && (p[stk[tp]] - p[stk[tp - 1]]) * (p[i] - p[stk[tp]]) <= 0)
              used[stk[tp--]] = 0;
            used[i] = 1;
            stk[++tp] = i;
          }
        for (int i = 1; i <= tp; ++i)  // copy into the new array
          h[i] = p[stk[i]];
        int ans = tp - 1;
        ```
    
    === "Python"
        ```python
        stk = []  # integer-typed, storing indices
        p = []  # stores vectors or points
        tp = 0  # initialize the stack
        p.sort()  # sort the points
        tp = tp + 1
        stk[tp] = 1
        # add the first element to the stack, and do not update used, so that 1 also updates the monotonic stack when finally closing the convex hull
        for i in range(2, n + 1):
            while tp >= 2 and (p[stk[tp]] - p[stk[tp - 1]]) * (p[i] - p[stk[tp]]) <= 0:
                # the * operator in the next line is overloaded as cross product
                used[stk[tp]] = 0
                tp = tp - 1
            used[i] = 1  # used means on the hull
            tp = tp + 1
            stk[tp] = i
        tmp = tp  # tmp is the size of the lower hull
        for i in range(n - 1, 0, -1):
            if used[i] == False:
                #      ↓finding the upper hull does not affect the lower hull
                while tp > tmp and (p[stk[tp]] - p[stk[tp - 1]]) * (p[i] - p[stk[tp]]) <= 0:
                    used[stk[tp]] = 0
                    tp = tp - 1
                used[i] = 1
                tp = tp + 1
                stk[tp] = i
        for i in range(1, tp + 1):
            h[i] = p[stk[i]]
        ans = tp - 1
        ```

According to the code above, in the end there are $\textit{ans}$ elements on the convex hull (point number $1$ is additionally stored, so there are $\textit{ans}+1$ elements in the $h$ array), sorted in counterclockwise order. The perimeter is

$$
\sum_{i=1}^{\textit{ans}}\left|\overrightarrow{h_ih_{i+1}}\right|
$$

### Graham's scan

#### Properties

Same as Andrew's algorithm, the time complexity of Graham's scan is $O(n\log n)$, and the complexity bottleneck is also in sorting all points.

#### Process

First find, among all points, the one with the smallest y-coordinate, $P$. By the definition of the convex hull, we know this point must be on the convex hull. Then sort all points with the polar angle relative to point P as the key.

![](./images/ch1.svg)

Similar to Andrew's algorithm, we consider starting from point $P$ and walking counterclockwise on the convex hull; then all nodes we pass must be "turning left". Formally, for any three consecutively passed points $P_1, P_2, P_3$ in the counterclockwise direction of the convex hull, it must satisfy $\overrightarrow{P_1 P_2} \times \overrightarrow{P_2 P_3} \ge 0$.

Create a new stack to store the information of the convex hull, first push $P$ onto the stack, then try to add each point in turn in polar-angle order. If the direction of travel of the pushed point $P_0$ and the top two points of the stack $P_1, P_2$ (where $P_1$ is the top of the stack) "turns right", then pop the top of the stack $P_1$, continually repeat the above process until the pushed point and the top two points of the stack satisfy the condition, or only one element remains in the stack, then push $P_0$ onto the stack.

![](./images/ch2.svg)

![](./images/ch3.svg)

???+ note "Code implementation"
    ```cpp
    struct Point {
      double x, y, ang;
    
      Point operator-(const Point& p) const { return {x - p.x, y - p.y, 0}; }
    } p[MAXN];
    
    double dis(Point p1, Point p2) {
      return sqrt((p1.x - p2.x) * (p1.x - p2.x) + (p1.y - p2.y) * (p1.y - p2.y));
    }
    
    bool cmp(Point p1, Point p2) {
      if (p1.ang == p2.ang) {
        return dis(p1, p[1]) < dis(p2, p[1]);
      }
      return p1.ang < p2.ang;
    }
    
    double cross(Point p1, Point p2) { return p1.x * p2.y - p1.y * p2.x; }
    
    int main() {
      for (int i = 2; i <= n; ++i) {
        if (p[i].y < p[1].y || (p[i].y == p[1].y && p[i].x < p[1].x)) {
          std::swap(p[1], p[i]);
        }
      }
      for (int i = 2; i <= n; ++i) {
        p[i].ang = atan2(p[i].y - p[1].y, p[i].x - p[1].x);
      }
      std::sort(p + 2, p + n + 1, cmp);
      sta[++top] = 1;
      for (int i = 2; i <= n; ++i) {
        while (top >= 2 &&
               cross(p[sta[top]] - p[sta[top - 1]], p[i] - p[sta[top]]) < 0) {
          top--;
        }
        sta[++top] = i;
      }
      return 0;
    }
    ```

## Minkowski sum

### Definition

The Minkowski sum $P+Q$ of point set $P$ and point set $Q$ is defined as $P+Q=\{a+b|a\in P,b\in Q\}$, i.e. regard each point in point set $Q$ as a vector, translate each point in point set $P$ along these vectors, and the set of the final results is the point set $P+Q$. Here we only discuss the Minkowski sum of **convex hulls**.

For example: for point set $P=\{(0,0),(-3,3),(2,1)\}$ and point set $Q=\{(0,0),(-1,3),(1,4),(2,2)\}$,

![](./images/convex-hull1.svg)

Translate $P$ along each vector of $Q$:

![](./images/convex-hull2.svg)

It is not hard to find that the new figure is also a **convex hull**:

![](./images/convex-hull3.svg)

### Properties

1.  If point sets $P$, $Q$ are convex sets, then their Minkowski sum $P+Q$ is also a convex set.

    ??? note "Proof"
        Let $e,f\in P+Q$; there exist $a,b \in P$, $c,d\in Q$ with $e=a+c,f=b+d$; then for any $t\in[0,1]$:
        
        $$
        \begin{aligned}
        te + (1-t)f &= t(a+c)+(1-t)(b+d)\\
        &=(ta+(1-t)b)+(tc+(1-t)d)\\
        &\in P+Q.
        \end{aligned}
        $$
        
        Q.E.D.
2.  If point sets $P$, $Q$ are convex sets, then the edge set of their Minkowski sum $P+Q$ is the result of connecting the edges of convex sets $P$, $Q$ after sorting by polar angle.

    ??? note "Proof"
        We may as well assume that the slope of any edge in convex set $P$ is different from the slope of any edge in $Q$. Rotate the coordinate system so that an edge $XY$ on $P$ is parallel to the $x$-axis and at the bottom.
        
        Let the lowest point $U$ in $Q$ at this time, and the **lowest** and **leftmost** point $A$ of $P+Q$.
        
        We know $\vec{A} = \vec{X} + \vec{U}$, so $A$ must be on the boundary of $P+Q$.
        
        Similarly, the **lowest** and **rightmost** point $B$ in $P+Q$ has $\vec{B} = \vec{Y} + \vec{U}$, and must also be on the boundary of $P+Q$.
        
        Therefore, $\vec{AB} = \vec{XY} + \vec{U}$.
        
        If we rotate in order, then the result continuously constitutes each edge in $P+Q$.
        
        Q.E.D.

### Implementation

By property 2, we can sort the convex sets $P,Q$ by polar angle to obtain their order of appearance on $P+Q$, regard $P_1+Q_1$ as the starting point of $P+Q$, and then place the edges in turn using a method similar to **merging**.

Time complexity: $O(n+m)$

???+ note "Implementation"
    ```cpp
    template <class T>
    struct Point {
      T x, y;
    
      Point(T x = 0, T y = 0) : x(x), y(y) {}
    
      friend Point operator+(const Point &a, const Point &b) {
        return {a.x + b.x, a.y + b.y};
      }
    
      friend Point operator-(const Point &a, const Point &b) {
        return {a.x - b.x, a.y - b.y};
      }
    
      // dot product
      friend T operator*(const Point &a, const Point &b) {
        return a.x * b.x + a.y * b.y;
      }
    
      // cross product
      friend T operator^(const Point &a, const Point &b) {
        return a.x * b.y - a.y * b.x;
      }
    };
    
    template <class T>
    vector<Point<T>> minkowski_sum(vector<Point<T>> a, vector<Point<T>> b) {
      vector<Point<T>> c{a[0] + b[0]};
      for (usz i = 0; i + 1 < a.size(); ++i) a[i] = a[i + 1] - a[i];
      for (usz i = 0; i + 1 < b.size(); ++i) b[i] = b[i + 1] - b[i];
      a.pop_back(), b.pop_back();
      c.resize(a.size() + b.size() + 1);
      merge(a.begin(), a.end(), b.begin(), b.end(), c.begin() + 1,
            [](const Point<T> &a, const Point<T> &b) { return (a ^ b) < 0; });
      for (usz i = 1; i < c.size(); ++i) c[i] = c[i] + c[i - 1];
      return c;
    }
    ```

### Example problem

???+ note "[Example problem \[JSOI2018\] War](https://loj.ac/p/2549)"
    There are two convex hulls $P,Q$; translate $Q$ $q$ times, and ask whether there is an intersection point after each move. $1\le n,m\le 10^5,1\le q\le 10^5$.

??? note "Implementation"
    ```cpp
    --8<-- "docs/geometry/code/convex-hull/convex-hull_1.cpp"
    ```

## Three-dimensional convex hull

### Basic knowledge

> Inversion of a circle: the inversion center is $O$, the inversion radius is $R$; if a line through $O$ passes through $P$, $P'$, and $OP\times OP'=R^{2}$, then $P$, $P'$ are said to be inverses of each other with respect to $O$.

### Process

The process of finding the convex hull is as follows:

-   First perform a tiny perturbation on it to avoid the case of four coplanar points.
-   For a known convex hull, add a new point $P$; regard $P$ as a point light source and cast rays toward the convex hull; we can know that the visible faces and invisible faces of the light must be separated by several edges.
-   Delete the visible faces of the light, and add the planes constituted by their separating edges and $P$.
    Just repeat this process; by [Pick's theorem](./pick.md), Euler's formula (in a convex polyhedron, its number of vertices $V$, number of edges $E$, and number of faces $F$ satisfy $V−E+F=2$), and inversion of a circle, the complexity is $O(n^2)$. [^3d-v]

### Template problem

[P4724 【Template】Three-Dimensional Convex Hull](https://www.luogu.com.cn/problem/P4724)

Just repeat the above process to obtain the answer.

???+ note "Code implementation"
    ```cpp
    --8<-- "docs/geometry/code/3d/3d_1.cpp"
    ```

## Practice

-   [UVa11626 Convex Hull](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=78&page=show_problem&problem=2673)

-   [「USACO5.1」Fencing the Cows](https://www.luogu.com.cn/problem/P2742)

-   [POJ1873 The Fortified Forest](http://poj.org/problem?id=1873)

-   [POJ1113 Wall](http://poj.org/problem?id=1113)

-   [USACO22JAN Multiple Choice Test P](https://www.luogu.com.cn/problem/P8101)

-   [「SHOI2012」Credit Card Convex Hull](https://www.luogu.com.cn/problem/P3829)

## References and notes

[^3d-v]: [A brief note on learning the three-dimensional convex hull](https://www.cnblogs.com/xzyxzy/p/10225804.html)
