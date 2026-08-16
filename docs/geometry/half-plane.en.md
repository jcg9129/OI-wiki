author: wjy-yy, Ir1d, Xeonacid

## Definition

### Half-plane

A line and one side of the line. A half-plane is a point set, so it is the point set constituted by a line and one side of the line. When the line is included, it is called a closed half-plane; when the line is not included, it is called an open half-plane.

The analytic expression is generally $Ax+By+C\ge 0$.

In computational geometry it is represented by a vector; the whole problem uniformly takes the left or right side of the vector as the half-plane.

![Half-plane](./images/hpi1.svg)

### Half-plane intersection

The half-plane intersection refers to the intersection of multiple half-planes. Because a half-plane is a point set, the intersection of point sets is still a point set. It encloses a region in the Cartesian coordinate plane.

This is very much like an ordinary linear programming problem; the obtained half-plane intersection is the feasible region in linear programming. Generally, the half-plane intersection is finite, and problems such as area are often examined.

It can be understood as the intersection of the right side of each vector in the vector set, or the solution of the following system of equations.

$$
\begin{cases}
A_1x+B_1y+C\ge 0\\
A_2x+B_2y+C\ge 0\\
\cdots
\end{cases}
$$

### Kernel of a polygon

If the line connecting a point in a point set with any point on a polygon has no other intersection points with the polygon, then this point set is called the kernel of the polygon.

Regarding each edge of the polygon as a head-to-tail connected vector, then the half-plane intersection of these vectors in the direction of the polygon's interior is the kernel of the polygon.

## Solution - S&I algorithm

### Polar-angle sorting

The C language has a library function called `atan2(double y,double x)`, which can return $\theta\in (-\pi,\pi]$, $\theta =\arctan \frac{y}{x}$.

Directly taking the vector as the argument, call this function, and sort with the return value as the key, obtaining a new edge (vector) set.

When sorting, if collinear vectors are encountered (and in the same direction), take the one closer to the feasible region. For example, if the polar angles of two vectors are the same, and what we want is the left half-plane of the vector, then we only need to keep the left vector. The judgment method is to take the start or end point of one of the vectors and compare it with the other, checking whether it is on the left or the right.

### Maintaining a monotonic queue

Because the half-plane intersection is a convex polygon, a convex hull needs to be maintained. Because a later-added edge can only possibly affect the earliest-added or last-added edge (at which point the convex hull is connected), we only need to delete the elements at the front and back of the queue, so a monotonic queue is needed.

We traverse the sorted vectors and maintain another intersection-point array. When there are more than 2 elements in the monotonic queue, intersection points are produced between them.

For the current vector, if the previous intersection point is on the **opposite side** of the half-plane represented by this vector, then the previous edge is meaningless.

![Monotonic queue](./images/hpi2.svg)

As in the figure above, suppose we take the left half-plane of a vector. After polar-angle sorting, the traversal order should be $\vec a\to\vec b\to\vec c$. When $\vec a$ and $\vec b$ are enqueued, a point $D$ is produced in the intersection-point array (the intersection-point array stores the intersection of the vector at the same index in the queue with the previous vector).

Next, when enumerating to $\vec c$, we find that $D$ is on the right side of $\vec c$. And because **the polar angle of the vector producing $D$ must be smaller than that of $\vec c$**, the vector producing $D$ (referring to $\vec b$) has no effect on the half-plane intersection.

There is another possible situation, which is that when it is about to end, a newly-added vector will cause effects starting from the front of the queue.

![Front-of-queue effect](./images/hpi7.svg)

Still suppose we take the left half-plane of a vector. After adding vector $\vec f$, the first intersection point $G$ is on the right side of $\vec f$; reversing the judgment criterion above, we know that at this point we should delete vector $\vec a$, i.e. the **front-of-queue** vector.

Finally, use the front-of-queue vector to exclude the redundant vectors at the back of the queue. Because the front-of-queue vector will be constrained by the later ones, while the back-of-queue vector will not. At this point they enclose a ring, so the front-of-queue vector can constrain the back-of-queue vector.

### Obtaining the half-plane intersection

If the half-plane intersection is a convex $n$-gon, then in the end we obtain $n$ points in the intersection-point array. We connect them head-to-tail, and it is a $n$-gon with a uniform direction (clockwise or counterclockwise).

At this point we can use triangulation to find the area. (Finding the area is the most basic examination method)

Occasionally, cases where the half-plane intersection does not exist or the area is 0 appear; note to consider the boundary.

### Notes

When a vector appears that can pop out all points in the queue (i.e. all points in the queue are on the right side of this vector), then we **must** handle the back of the queue first, then the front of the queue. Therefore in the loop, we first enumerate the `--r;` part, then enumerate the `++l;` part, so as not to make a mistake. The reason is as follows.

![](./images/hpi4.svg)

Generally, when we add an edge (vector $\vec w$) after the queue (queue order $\left\{\vec{u},\vec{v}\right\}$), an intersection point $N$ is produced, shrinking the range behind $\vec{v}$.

![](./images/hpi5.svg)

But after all, every operation is general, so there may be a case where point $M$ is "squeezed out".

![](./images/hpi6.svg)

If at this point a vector $\vec a$ appears such that $M$ is on the right side of $\vec a$, then $M$ should leave the queue. At this point, if we enumerate `++l` from the front of the queue, we obviously expand the range. In fact, point $M$ is jointly constituted by $\vec u$ and $\vec v$, so we need to consider whether it is $\vec u$ or $\vec v$ that affects the existing process. And because after polar-angle sorting, the vectors are in counterclockwise order, the effect of $\vec v$ is greater.

Just as in the figure above, if $M$ is confirmed to be on the right side of $\vec a$, then at this point the effect of $\vec v$ will definitely not make any contribution to the answer of the half-plane intersection.

And the reason we exclude the front of the queue is that **the constraint of the current vector is greater than that of the front-of-queue vector**; the premise of this condition is that there are more than two segments (vectors) in the queue, otherwise the above situation will occur.

So we must exclude the back of the queue first and then the front of the queue.

???+ note "Code - comparison part"
    ```cpp
    friend bool operator<(seg x, seg y) {
      db t1 = atan2((x.b - x.a).y, (x.b - x.a).x);
      db t2 = atan2((y.b - y.a).y, (y.b - y.a).x);  // find the polar angle
      if (fabs(t1 - t2) > eps)                      // if the polar angles are unequal
        return t1 < t2;
      return (y.a - x.a) * (y.b - x.a) >
             eps;  // judge which side of y vector x is on, letting the leftmost be arranged at the far left
    }
    ```

???+ note "Code - increment part"
    ```cpp
    // pnt its(seg a,seg b) means finding the intersection point of segments a, b
    // s[] is the vectors after polar-angle sorting
    // q[] is the vector queue
    // t[i] is the intersection of s[i-1] and s[i]
    // 【coding style】the range of the queue is (l,r]
    // finding the half-plane on the left side of the vectors
    int l = 0, r = 0;
    for (int i = 1; i <= n; ++i)
      if (s[i] != s[i - 1]) {
        // note to check the back of the queue first
        while (r - l > 1 && (s[i].b - t[r]) * (s[i].a - t[r]) >
                                eps)  // if the previous intersection point is on the right side of the vector, pop the back of the queue
          --r;
        while (r - l > 1 && (s[i].b - t[l + 2]) * (s[i].a - t[l + 2]) >
                                eps)  // if the first intersection point is on the right side of the vector, pop the front of the queue
          ++l;
        q[++r] = s[i];
        if (r - l > 1) t[r] = its(q[r], q[r - 1]);  // find the new intersection point
      }
    while (r - l > 1 &&
           (q[l + 1].b - t[r]) * (q[l + 1].a - t[r]) > eps)  // note to delete redundant elements
      --r;
    t[r + 1] = its(q[l + 1], q[r]);  // then find the new intersection point
    ++r;
    // note that here we cannot ++r inside t……
    ```

## Practice

[POJ 2451 Uyuw's Concert](http://poj.org/problem?id=2451) note the boundary

[POJ 1279 Art Gallery](http://poj.org/problem?id=1279) find the kernel of a polygon

[「CQOI2006」Convex Polygon](https://www.luogu.com.cn/problem/P4196)
