author: hyp1231, 383494

## Introduction

The inversion transformation applies to situations where there are tangency relations among multiple circles/lines in a problem. Using the properties of the inversion transformation, solving the problem in the inversion space can greatly simplify the computation.

## Definition

Given the inversion center point $O$ and the inversion radius $R$. If points $P$ and $P'$ in the plane satisfy:

-   Point $P'$ is on the ray $\overrightarrow{OP}$
-   $|OP| \cdot |OP'| = R^2$

then points $P$ and $P'$ are said to be inversion points of each other.

## Explanation

The figure below shows the inversion of a point $P$ in the plane:

![Inv1](./images/inverse1.png)

## Properties

1.  The inversion point of a point outside circle $O$ is inside circle $O$, and vice versa; the inversion point of a point on circle $O$ is itself.

2.  For a circle $A$ not passing through point $O$, its inversion figure is also a circle not passing through point $O$.

    ![Inv2](./images/inverse2.png)

    -   Denote the radius of circle $A$ as $r_1$, and the radius of its inversion figure circle $B$ as $r_2$; then:

        $$
        r_2 = \frac{1}{2}\left(\frac{1}{|OA| - r_1} - \frac{1}{|OA| + r_1}\right) R^2
        $$

    ???+ note "Proof"
        ![Inv3](./images/inverse3.png)
        
        By the definition of the inversion transformation:
        
        $$
        \begin{aligned}
        |OC|\cdot|OC'| &= (|OA|+r_1)\cdot(|OB|-r_2) = R^2 \\
        |OD|\cdot|OD'| &= (|OA|-r_1)\cdot(|OB|+r_2) = R^2
        \end{aligned}
        $$
        
        Eliminate $|OB|$ and solve the equation.

    -   Denote the coordinates of point $O$ as $(x_0, y_0)$, the coordinates of point $A$ as $x_1, y_1$, and the coordinates of point $B$ as $x_2, y_2$; then:

        $$
        \begin{aligned}
        x_2 &= x_0 + \frac{|OB|}{|OA|} (x_1 - x_0) \\
        y_2 &= y_0 + \frac{|OB|}{|OA|} (y_1 - y_0)
        \end{aligned}
        $$

        where $|OB|$ can be computed in the above process of finding $r_2$.

3.  For a circle $A$ passing through point $O$, its inversion figure is a line not passing through point $O$. Because a point on circle $A$ infinitely close to point $O$ has its inversion point infinitely far from point $O$.

    ![Inv4](./images/inverse4.png)

4.  If two figures are tangent and there exists a tangent point that is not point $O$, then their inversion figures are also tangent.

## Example problem

### [「ICPC 2013 Hangzhou Regional」Problem of Apollonius](https://acm.hdu.edu.cn/showproblem.php?pid=4773)

#### Problem summary

Find all circles that pass through a point outside two circles and are tangent to both circles.

#### Solution

First consider the analytic-geometry solution; it seems very hard to solve.

Consider performing inversion with the point that needs to be passed through as the inversion center (the inversion radius is arbitrary); the inversion figure of the sought circle is a line (applying property $3$), and is tangent (property $4$) to the inversion figures (property $2$) of the two circles given in the problem.

So after the inversion transformation, the problem transforms into: find all common tangents of two circles.

After finding the common tangents, just invert back to the original plane.

??? note "Example code"
    ```cpp
    #include <algorithm>
    #include <cmath>
    #include <cstdio>
    #include <cstring>
    #include <iostream>
    #include <vector>
    using namespace std;
    
    constexpr double EPS = 1e-8;   // precision coefficient
    const double PI = acos(-1.0);  // π
    constexpr int N = 4;
    
    // definition of a point
    struct Point {
      double x, y;
    
      Point(double x = 0, double y = 0) : x(x), y(y) {}
    
      bool operator<(Point A) const { return x == A.x ? y < A.y : x < A.x; }
    };
    
    // definition of a vector
    using Vector = Point;
    
    // vector addition
    Vector operator+(Vector A, Vector B) { return Vector(A.x + B.x, A.y + B.y); }
    
    // vector subtraction
    Vector operator-(Vector A, Vector B) { return Vector(A.x - B.x, A.y - B.y); }
    
    // vector scalar multiplication
    Vector operator*(Vector A, double p) { return Vector(A.x * p, A.y * p); }
    
    // vector scalar division
    Vector operator/(Vector A, double p) { return Vector(A.x / p, A.y / p); }
    
    // relation with 0
    int dcmp(double x) {
      if (fabs(x) < EPS) return 0;
      return x < 0 ? -1 : 1;
    }
    
    // vector dot product
    double Dot(Vector A, Vector B) { return A.x * B.x + A.y * B.y; }
    
    // vector length
    double Length(Vector A) { return sqrt(Dot(A, A)); }
    
    // vector cross product
    double Cross(Vector A, Vector B) { return A.x * B.y - A.y * B.x; }
    
    // projection of a point onto a line
    Point GetLineProjection(Point P, Point A, Point B) {
      Vector v = B - A;
      return A + v * (Dot(v, P - A) / Dot(v, v));
    }
    
    // circle
    struct Circle {
      Point c;
      double r;
    
      Circle() : c(Point(0, 0)), r(0) {}
    
      Circle(Point c, double r = 0) : c(c), r(r) {}
    
      // input the polar angle, return the point coordinates
      Point point(double a) { return Point(c.x + cos(a) * r, c.y + sin(a) * r); }
    };
    
    // common tangents of two circles; returns the number of tangents, -1 means infinitely many tangents
    // a[i] and b[i] are the tangent points of the i-th tangent on circle A and circle B respectively
    int getTangents(Circle A, Circle B, Point* a, Point* b) {
      int cnt = 0;
      if (A.r < B.r) {
        swap(A, B);
        swap(a, b);
      }
      double d2 =
          (A.c.x - B.c.x) * (A.c.x - B.c.x) + (A.c.y - B.c.y) * (A.c.y - B.c.y);
      double rdiff = A.r - B.r;
      double rsum = A.r + B.r;
      if (dcmp(d2 - rdiff * rdiff) < 0) return 0;  // internally contained
    
      double base = atan2(B.c.y - A.c.y, B.c.x - A.c.x);
      if (dcmp(d2) == 0 && dcmp(A.r - B.r) == 0) return -1;  // infinitely many tangents
      if (dcmp(d2 - rdiff * rdiff) == 0) {  // internally tangent, one tangent
        a[cnt] = A.point(base);
        b[cnt] = B.point(base);
        ++cnt;
        return 1;
      }
      // has external common tangents
      double ang = acos(rdiff / sqrt(d2));
      a[cnt] = A.point(base + ang);
      b[cnt] = B.point(base + ang);
      ++cnt;
      a[cnt] = A.point(base - ang);
      b[cnt] = B.point(base - ang);
      ++cnt;
      if (dcmp(d2 - rsum * rsum) == 0) {  // one internal common tangent
        a[cnt] = A.point(base);
        b[cnt] = B.point(PI + base);
        ++cnt;
      } else if (dcmp(d2 - rsum * rsum) > 0) {  // two internal common tangents
        double ang = acos(rsum / sqrt(d2));
        a[cnt] = A.point(base + ang);
        b[cnt] = B.point(PI + base + ang);
        ++cnt;
        a[cnt] = A.point(base - ang);
        b[cnt] = B.point(PI + base - ang);
        ++cnt;
      }
      return cnt;
    }
    
    // point O is outside circle A, find the inversion circle B of circle A, R is the inversion radius
    Circle Inversion_C2C(Point O, double R, Circle A) {
      double OA = Length(A.c - O);
      double RB = 0.5 * ((1 / (OA - A.r)) - (1 / (OA + A.r))) * R * R;
      double OB = OA * RB / A.r;
      double Bx = O.x + (A.c.x - O.x) * OB / OA;
      double By = O.y + (A.c.y - O.y) * OB / OA;
      return Circle(Point(Bx, By), RB);
    }
    
    // a line inverts into a circle B passing through point O, R is the inversion radius
    Circle Inversion_L2C(Point O, double R, Point A, Vector v) {
      Point P = GetLineProjection(O, A, A + v);
      double d = Length(O - P);
      double RB = R * R / (2 * d);
      Vector VB = (P - O) / d * RB;
      return Circle(O + VB, RB);
    }
    
    // returns true if points A and B are on the same side of the line
    bool theSameSideOfLine(Point A, Point B, Point S, Vector v) {
      return dcmp(Cross(A - S, v)) * dcmp(Cross(B - S, v)) > 0;
    }
    
    int main() {
      int T;
      scanf("%d", &T);
      while (T--) {
        Circle A, B;
        Point P;
        scanf("%lf%lf%lf", &A.c.x, &A.c.y, &A.r);
        scanf("%lf%lf%lf", &B.c.x, &B.c.y, &B.r);
        scanf("%lf%lf", &P.x, &P.y);
        Circle NA = Inversion_C2C(P, 10, A);
        Circle NB = Inversion_C2C(P, 10, B);
        Point LA[N], LB[N];
        Circle ansC[N];
        int q = getTangents(NA, NB, LA, LB), ans = 0;
        for (int i = 0; i < q; ++i)
          if (theSameSideOfLine(NA.c, NB.c, LA[i], LB[i] - LA[i])) {
            if (!theSameSideOfLine(P, NA.c, LA[i], LB[i] - LA[i])) continue;
            ansC[ans++] = Inversion_L2C(P, 10, LA[i], LB[i] - LA[i]);
          }
        printf("%d\n", ans);
        for (int i = 0; i < ans; ++i) {
          printf("%.8f %.8f %.8f\n", ansC[i].c.x, ansC[i].c.y, ansC[i].r);
        }
      }
    
      return 0;
    }
    ```

## Practice

[「ICPC 2017 Nanning Regional Online」Finding the Radius for an Inserted Circle](https://vjudge.net/problem/%E8%AE%A1%E8%92%9C%E5%AE%A2-A1283)

[「CCPC 2017 Online」The Designer](https://acm.hdu.edu.cn/showproblem.php?pid=6158)

## References and further reading

-   [Inversive geometry - Wikipedia](https://en.wikipedia.org/wiki/Inversive_geometry)

-   [Inversion transformation of a circle - ACdreamers' blog](https://blog.csdn.net/acdreamers/article/details/16966369)
