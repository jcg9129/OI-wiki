author: Ir1d, TianyiQ

## Introduction

The randomized incremental algorithm is an important algorithm of computational geometry; it has low requirements on theoretical knowledge, low algorithmic time complexity, and a wide application scope.

The idea of the Incremental Algorithm is similar to the first mathematical induction; its essence is to reduce a problem to a subproblem exactly one level smaller. After solving the subproblem, add the current object. Written as a recurrence:

$$
T(n)=T(n-1)+g(n)
$$

The incremental method is concise in form and can be applied to many geometry problems.

The incremental method is often combined with randomization, which can avoid the occurrence of the worst case.

## Minimum circle covering problem

### Problem description

There are $n$ points in a plane; find a circle with the smallest radius that can cover all the points.

### Process

Suppose circle $O$ is the minimum covering circle of the first $i-1$ points; add the $i$-th point; if it is inside the circle or on the boundary, do nothing. Otherwise, the newly obtained minimum covering circle must pass through the $i$-th point.

Then based on the $i$-th point (radius $0$), repeat the above process to add the $j$-th point in turn; if the $j$-th point is outside the circle, then the minimum covering circle must pass through the $j$-th point.

Repeat the above steps. (Because at most three points are needed to determine this minimum covering circle, repeat three times)

After traversing all points, the obtained circle is the smallest circle covering all points.

### Properties

**Time complexity** $O(n)$; for the proof see the references.

**Space complexity** $O(n)$

### Implementation

??? note "Code implementation"
    ```cpp
    #include <cmath>
    #include <cstdio>
    #include <cstdlib>
    #include <cstring>
    #include <iostream>
    
    using namespace std;
    
    int n;
    double r;
    
    struct point {
      double x, y;
    } p[100005], o;
    
    double sqr(double x) { return x * x; }
    
    double dis(point a, point b) { return sqrt(sqr(a.x - b.x) + sqr(a.y - b.y)); }
    
    bool cmp(double a, double b) { return fabs(a - b) < 1e-8; }
    
    point geto(point a, point b, point c) {
      double a1, a2, b1, b2, c1, c2;
      point ans;
      a1 = 2 * (b.x - a.x), b1 = 2 * (b.y - a.y),
      c1 = sqr(b.x) - sqr(a.x) + sqr(b.y) - sqr(a.y);
      a2 = 2 * (c.x - a.x), b2 = 2 * (c.y - a.y),
      c2 = sqr(c.x) - sqr(a.x) + sqr(c.y) - sqr(a.y);
      if (cmp(a1, 0)) {
        ans.y = c1 / b1;
        ans.x = (c2 - ans.y * b2) / a2;
      } else if (cmp(b1, 0)) {
        ans.x = c1 / a1;
        ans.y = (c2 - ans.x * a2) / b2;
      } else {
        ans.x = (c2 * b1 - c1 * b2) / (a2 * b1 - a1 * b2);
        ans.y = (c2 * a1 - c1 * a2) / (b2 * a1 - b1 * a2);
      }
      return ans;
    }
    
    int main() {
      scanf("%d", &n);
      for (int i = 1; i <= n; i++) scanf("%lf%lf", &p[i].x, &p[i].y);
      for (int i = 1; i <= n; i++) swap(p[rand() % n + 1], p[rand() % n + 1]);
      o = p[1];
      for (int i = 1; i <= n; i++) {
        if (dis(o, p[i]) < r || cmp(dis(o, p[i]), r)) continue;
        o.x = (p[i].x + p[1].x) / 2;
        o.y = (p[i].y + p[1].y) / 2;
        r = dis(p[i], p[1]) / 2;
        for (int j = 2; j < i; j++) {
          if (dis(o, p[j]) < r || cmp(dis(o, p[j]), r)) continue;
          o.x = (p[i].x + p[j].x) / 2;
          o.y = (p[i].y + p[j].y) / 2;
          r = dis(p[i], p[j]) / 2;
          for (int k = 1; k < j; k++) {
            if (dis(o, p[k]) < r || cmp(dis(o, p[k]), r)) continue;
            o = geto(p[i], p[j], p[k]);
            r = dis(o, p[i]);
          }
        }
      }
      printf("%.10lf\n%.10lf %.10lf", r, o.x, o.y);
      return 0;
    }
    ```

## Practice

[Minimum Circle Covering](https://www.luogu.com.cn/problem/P1742)

[「HNOI2012」Archery](https://www.luogu.com.cn/problem/P3222)

[CodeForces 442E](https://codeforces.com/problemset/problem/442/E)

## References and further reading

[Randomized incremental algorithm - Xie Yilun](https://github.com/hzwer/shareOI/blob/master/%E8%AE%A1%E7%AE%97%E5%87%A0%E4%BD%95/%E9%9A%8F%E6%9C%BA%E5%A2%9E%E9%87%8F%E7%AE%97%E6%B3%95_%E8%A7%A3%E8%BD%B6%E4%BC%A6.pdf)

<https://www.cnblogs.com/aininot260/p/9635757.html>

<https://www.cise.ufl.edu/~sitharam/COURSES/CG/kreveldnbhd.pdf>

<https://blog.csdn.net/u014609452/article/details/62039612>
