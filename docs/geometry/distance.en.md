author: Chrogeek, frank-xjh, ChungZH, hsfzLZH1, Marcythm, Planet6174, partychicken, i-Yirannn

## Euclidean distance

### Two-dimensional space

#### Definition

The Euclidean distance, generally also called the Euclidean distance. In the Cartesian coordinate plane, let the coordinates of points $A,B$ be $A(x_1,y_1),B(x_2,y_2)$ respectively; then the Euclidean distance between the two points is:

$$
\left | AB \right | = \sqrt{\left ( x_2 - x_1 \right )^2 + \left ( y_2 - y_1 \right )^2}
$$

#### Explanation

For example, if in the Cartesian coordinate plane there are two points $A(6,5),B(2,2)$, then through the formula, we easily obtain the Euclidean distance between the two points $A,B$:

$$
\left | AB \right | = \sqrt{\left ( 2 - 6 \right )^2 + \left ( 2 - 5 \right )^2} = \sqrt{4^2+3^2} = 5
$$

In addition, the Euclidean distance from $P(x,y)$ to the origin can be expressed by the formula:

$$
|P| = \sqrt{x^2+y^2}
$$

### n-dimensional space

#### Introduction

So, what about the Euclidean distance formula for two points in three-dimensional space? Let's observe the figure below.

![dis-3-dimensional](./images/distance-0.png)

We easily find that in $\triangle ADC$, $\angle ADC = 90^\circ$; in $\triangle ACB$, $\angle ACB = 90^\circ$.

$$
\begin{aligned}
\therefore ~ |AB| &= \sqrt{|AC|^2+|BC|^2} \\
&= \sqrt{|AD|^2+|CD|^2+|BC|^2}
\end{aligned}
$$

#### Definition

From this we can obtain that the distance formula for the Euclidean distance in three-dimensional space is:

$$
\begin{gathered}
\left | AB \right | = \sqrt{\left ( x_2 - x_1 \right )^2 + \left ( y_2 - y_1 \right )^2 + \left ( z_2 - z_1 \right )^2} \\
|P| = \sqrt{x^2+y^2+z^2}
\end{gathered}
$$

#### Explanation

[NOIP2017 Senior Group Cheese](https://uoj.ac/problem/332) uses this knowledge and can serve as an example problem for the Euclidean distance.

By analogy, we obtain the distance formula for the Euclidean distance in $n$-dimensional space: for $\vec A(x_{11}, x_{12}, \cdots,x_{1n}) ,~ \vec B(x_{21}, x_{22}, \cdots,x_{2n})$, we have

$$
\begin{aligned}
\lVert\overrightarrow{AB}\rVert &= \sqrt{\left ( x_{11} - x_{21} \right )^2 + \left ( x_{12} - x_{22} \right )^2 + \cdot \cdot \cdot +\left ( x_{1n} - x_{2n} \right )^2}\\
&= \sqrt{\sum_{i = 1}^{n}(x_{1i} - x_{2i})^2}
\end{aligned}
$$

Although the Euclidean distance is very useful, it also has an obvious drawback. When computing the Euclidean distance of two integer points, the answer is often a floating-point type, and there is a certain error.

## Manhattan distance

### Definition

In two-dimensional space, the Manhattan distance between two points is the sum of the absolute value of the difference of their x-coordinates and the absolute value of the difference of their y-coordinates. Let points $A(x_1,y_1),B(x_2,y_2)$; then the Manhattan distance between $A,B$ can be expressed by the formula:

$$
d(A,B) = |x_1 - x_2| + |y_1 - y_2|
$$

### Explanation

Observe the figure below:

![manhattan-dis-diff](./images/distance-1.png)

Between $A,B$, the yellow line and orange line both represent the Manhattan distance, the red line and blue line represent equivalent Manhattan distances, and the green line represents the Euclidean distance.

For the same example, in the figure below the coordinates of $A,B$ are $A(25,20),B(10,10)$ respectively.

![manhattan-dis](./images/distance-2.svg)

Through the formula, we easily obtain the Manhattan distance between the two points $A,B$:

$$
d(A,B) = |20 - 10| + |25 - 10| = 10 + 15 = 25
$$

After derivation, we obtain the Manhattan distance formula for $n$-dimensional space:

$$
\begin{aligned}
d(A,B) &= |x_1 - y_1| + |x_2 - y_2| + \cdot \cdot \cdot + |x_n - y_n|\\
&= \sum_{i = 1}^{n}|x_i - y_i|
\end{aligned}
$$

### Properties

Besides the formula, the Manhattan distance also has the following mathematical properties:

-   Non-negativity: the Manhattan distance is a non-negative number, i.e. $d(i,j)\geq 0$.
-   Uniformity: the Manhattan distance from a point to itself is $0$, i.e. $d(i,i) = 0$.
-   Symmetry: the Manhattan distance from $A$ to $B$ and from $B$ to $A$ are equal, i.e. $d(i,j) = d(j,i)$.
-   Triangle inequality: the direct distance from point $i$ to $j$ is not greater than the distance passing through any other point $k$, i.e. $d(i,j)\leq d(i,k)+d(k,j)$.

### Example problem

[P5098 「USACO04OPEN」Cave Cows 3](https://www.luogu.com.cn/problem/P5098)

According to the problem, for the expression $|x_1-x_2|+|y_1-y_2|$, we can assume $x_1 - x_2 \geq 0$, and divide into two cases according to the sign of $y_1 - y_2$:

-   $(y_1 - y_2 \geq 0)\rightarrow |x_1-x_2|+|y_1-y_2|=x_1 + y_1 - (x_2 + y_2)$

-   $(y_1 - y_2 < 0)\rightarrow |x_1-x_2|+|y_1-y_2|=x_1 - y_1 - (x_2 - y_2)$

Just find the maximum and minimum of $x+y, x-y$ respectively to obtain the answer.

??? note "Reference code"
    === "C++"
        ```cpp
        #include <algorithm>
        #include <cstdio>
        using namespace std;
        
        int main() {
          int n, x, y, minx = 0x7fffffff, maxx = 0, miny = 0x7fffffff, maxy = 0;
          scanf("%d", &n);
          for (int i = 1; i <= n; i++) {
            scanf("%d%d", &x, &y);
            minx = min(minx, x + y), maxx = max(maxx, x + y);
            miny = min(miny, x - y), maxy = max(maxy, x - y);
          }
          printf("%d\n", max(maxx - minx, maxy - miny));
          return 0;
        }
        ```
    
    === "Python"
        ```python
        minx = 0x7FFFFFFF
        maxx = 0
        miny = 0x7FFFFFFF
        maxy = 0
        n = int(input())
        for i in range(1, n + 1):
            x, y = map(lambda x: int(x), input().split())
            minx = min(minx, x + y)
            maxx = max(maxx, x + y)
            miny = min(miny, x - y)
            maxy = max(maxy, x - y)
        print(max(maxx - minx, maxy - miny))
        ```

Actually there is a second approach, which is to convert the Manhattan distance into the Chebyshev distance for solving; this will be discussed in the last part.

## Chebyshev distance

### Definition

The Chebyshev distance is a metric in vector space; the distance between two points is defined as the maximum of the difference of their coordinate values. [^ref1]

In two-dimensional space, the Chebyshev distance between two points is the maximum of the absolute value of the difference of their x-coordinates and the absolute value of the difference of their y-coordinates. Let points $A(x_1,y_1),B(x_2,y_2)$; then the Chebyshev distance between $A,B$ can be expressed by the formula:

$$
d(A,B) = \max(|x_1 - x_2|, |y_1 - y_2|)
$$

The distance formula for the Chebyshev distance in $n$-dimensional space can be expressed as:

$$
\begin{aligned}
d(x,y) &= \max\begin{Bmatrix} |x_1 - y_1|,|x_2 - y_2|,\cdot \cdot \cdot,|x_n - y_n|\end{Bmatrix} \\
&= \max\begin{Bmatrix} |x_i - y_i|\end{Bmatrix}(i \in [1, n])\end{aligned}
$$

### Explanation

Still this example, in the figure below the coordinates of $A,B$ are $A(25,20),B(10,10)$ respectively.

![Chebyshev-dis](./images/distance-2.svg)

$$
d(A,B) = \max(|20 - 10|, |25 - 10|) = \max(10, 15) = 15
$$

## Mutual conversion between Manhattan distance and Chebyshev distance

### Process

First, we consider drawing all points on the Cartesian coordinate plane whose Manhattan distance to the origin is $1$.

Through the formula, we easily obtain the equation $|x| + |y| = 1$.

Expanding the absolute values, we obtain $4$ linear functions, namely:

$$
\begin{aligned}
&y = -x + 1 &(x \geq 0, y \geq 0) \\
&y = x + 1 &(x \leq 0, y \geq 0) \\
&y = x - 1  &(x \geq 0, y \leq 0)  \\
&y = -x - 1  &(x \leq 0, y \leq 0) \\
\end{aligned}
$$

Drawing these $4$ functions on the Cartesian coordinate plane, we obtain a square with side length $\sqrt{2}$, as shown in the figure below:

![dis-diff-square-1](./images/distance-3.svg)

The Manhattan distance from all points on the boundary of the square to the origin is $1$.

Similarly, we consider drawing all points on the Cartesian coordinate plane whose Chebyshev distance to the origin is $1$.

Through the formula, we know $\max(|x|,|y|)=1$.

Expanding the expression, we can likewise obtain $4$ line segments, namely:

$$
\begin{aligned}
&y = 1&(-1\leq x \leq 1) \\
&y = -1&(-1\leq x \leq 1) \\
&x = 1,&(-1\leq y \leq 1) \\
&x = -1,&(-1\leq y \leq 1) \\
\end{aligned}
$$

Drawing on the Cartesian coordinate plane, we can obtain a square with side length $2$, as shown in the figure below:

![dis-diff-square-2](./images/distance-4.svg)

The Chebyshev distance from all points on the boundary of the square to the origin is $1$.

Comparing these two figures, we amazingly find:

These $2$ squares are similar figures.

### Proof

So, is there a connection between the Manhattan distance and the Chebyshev distance?

Next let's briefly prove it:

Suppose $A(x_1,y_1),B(x_2,y_2)$,

We expand the absolute values in the Manhattan distance and can obtain four values; the maximum of these four values is the sum of two non-negative numbers, i.e. the Manhattan distance. Then the Manhattan distance between the two points $A,B$ is:

$$
\begin{aligned}
d(A,B)&=|x_1 - x_2| + |y_1 - y_2|\\
&=\max\begin{Bmatrix} x_1 - x_2 + y_1 - y_2, x_1 - x_2 + y_2 - y_1,x_2 - x_1 + y_1 - y_2, x_2 - x_1 + y_2 - y_1\end{Bmatrix}\\
&= \max(|(x_1 + y_1) - (x_2 + y_2)|, |(x_1 - y_1) - (x_2 - y_2)|)
\end{aligned}
$$

We easily find that this is exactly the Chebyshev distance between the two points $(x_1 + y_1,x_1 - y_1), (x_2 + y_2,x_2 - y_2)$.

So converting each point $(x,y)$ into $(x + y, x - y)$, the Chebyshev distance in the new coordinate system is the Manhattan distance in the original coordinate system.

Similarly, the Chebyshev distance between the two points $A,B$ is:

$$
\begin{aligned}
d(A,B)&=\max\begin{Bmatrix} |x_1 - x_2|,|y_1 - y_2|\end{Bmatrix}\\
&=\max\begin{Bmatrix} \left|\dfrac{x_1 + y_1}{2}-\dfrac{x_2 + y_2}{2}\right|+\left|\dfrac{x_1 - y_1}{2}-\dfrac{x_2 - y_2}{2}\right|\end{Bmatrix}
\end{aligned}
$$

And this is exactly the Manhattan distance between the two points $(\dfrac{x_1 + y_1}{2},\dfrac{x_1 - y_1}{2}), (\dfrac{x_2 + y_2}{2},\dfrac{x_2 - y_2}{2})$.

So converting each point $(x,y)$ into $(\dfrac{x + y}{2},\dfrac{x - y}{2})$, the Manhattan distance in the new coordinate system is the Chebyshev distance in the original coordinate system.

### Conclusion

-   The Manhattan coordinate system is obtained by rotating the Chebyshev coordinate system by $45^\circ$ and then shrinking it to half of the original.
-   After changing the coordinates of a point $(x,y)$ to $(x + y, x - y)$, the Manhattan distance in the original coordinate system equals the Chebyshev distance in the new coordinate system.
-   After changing the coordinates of a point $(x,y)$ to $(\dfrac{x + y}{2},\dfrac{x - y}{2})$, the Chebyshev distance in the original coordinate system equals the Manhattan distance in the new coordinate system.

When encountering problems asking for the Chebyshev distance or Manhattan distance, we can often convert between them to solve. The two distances have different advantages and disadvantages in different problems, and should be used flexibly.

### Example problems

[P4648 「IOI2007」pairs](https://www.luogu.com.cn/problem/P4648) (Manhattan distance to Chebyshev distance)

[P3964 「TJOI2013」Squirrel Gathering](https://www.luogu.com.cn/problem/P3964) (Chebyshev distance to Manhattan distance)

Finally, we give the second solution to [P5098 「USACO04OPEN」Cave Cows 3](https://www.luogu.com.cn/problem/P5098):

We consider converting the Manhattan distance asked in the problem into the Chebyshev distance, i.e. changing the coordinates $(x,y)$ of each point into $(x + y, x - y)$.

The asked answer then becomes $\max\limits_{i,j\in n}\begin{Bmatrix} \max\begin{Bmatrix} |x_i - x_j|,|y_i - y_j|\end{Bmatrix}\end{Bmatrix}$.

Now to maximize the difference of x-coordinates and the difference of y-coordinates, just preprocess the maximum and minimum of $x,y$.

??? note "Reference code"
    === "C++"
        ```cpp
        #include <algorithm>
        #include <cstdio>
        using namespace std;
        
        int main() {
          int n, x, y, a, b, minx = 0x7fffffff, maxx = 0, miny = 0x7fffffff, maxy = 0;
          scanf("%d", &n);
          for (int i = 1; i <= n; i++) {
            scanf("%d%d", &a, &b);
            x = a + b, y = a - b;
            minx = min(minx, x), maxx = max(maxx, x);
            miny = min(miny, y), maxy = max(maxy, y);
          }
          printf("%d\n", max(maxx - minx, maxy - miny));
          return 0;
        }
        ```
    
    === "Python"
        ```python
        minx = 0x7FFFFFFF
        maxx = 0
        miny = 0x7FFFFFFF
        maxy = 0
        n = int(input())
        for i in range(1, n + 1):
            a, b = map(lambda x: int(x), input().split())
            x = a + b
            y = a - b
            minx = min(minx, x)
            maxx = max(maxx, x)
            miny = min(miny, y)
            maxy = max(maxy, y)
        print(max(maxx - minx, maxy - miny))
        ```

Comparing the two pieces of code, we can again find that two different lines of thought produce completely equivalent code. Isn't that amazing? Of course, more profound things need everyone to research separately.

## Minkowski distance

We define the Minkowski distance between two points $X(x_1, x_2, \dots, x_n)$, $Y(y_1, y_2, \dots, y_n)$ in $n$-dimensional space as:

$$
D(X, Y) = \left(\sum_{i=1}^n \left\vert x_i - y_i \right\vert ^p\right)^{\frac{1}{p}}.
$$

In particular:

1.  when $p=1$, $D(X, Y) = \sum_{i=1}^n \left\vert x_i - y_i \right\vert$ is the Manhattan distance;
2.  when $p=2$, $D(X, Y) = \left(\sum_{i=1}^n (x_i - y_i)^2\right)^{1/2}$ is the Euclidean distance;
3.  when $p \to \infty$, $D(X, Y) = \lim_{p \to \infty}\left(\sum_{i=1}^n \left\vert x_i - y_i \right\vert ^p\right) ^{1/p} = \max\limits_{i=1}^n \left\vert x_i - y_i \right\vert$ is the Chebyshev distance.

Note: only when $p \ge 1$ is the Minkowski distance a metric; for the specific proof see [Minkowski distance - Wikipedia](https://en.wikipedia.org/wiki/Minkowski_distance).

## References and links

1.  [A brief discussion of three common distance algorithms](https://www.luogu.com.cn/blog/xuxing/Distance-Algorithm), thanks to the author xuxing for the authorization.

[^ref1]: [Chebyshev distance - Wikipedia, the free encyclopedia](https://zh.wikipedia.org/wiki/%E5%88%87%E6%AF%94%E9%9B%AA%E5%A4%AB%E8%B7%9D%E7%A6%BB)
