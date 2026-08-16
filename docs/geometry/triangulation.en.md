author: xehoth

In geometry, triangulation refers to subdividing a planar object into triangles, and by extension subdividing a higher-dimensional geometric object into simplices.
For a given point set, there are many kinds of triangulations, such as:

![Three triangulations](./images/triangulation-0.svg)

Triangulation in OI mainly refers to the perfect triangulation in two-dimensional geometry (two-dimensional Delaunay triangulation, abbreviated DT).

## Delaunay triangulation

### Definition

In mathematics and computational geometry, for a given discrete point set $P$ in the plane, its Delaunay triangulation DT($P$) satisfies:

1.  Empty-circle property: DT($P$) is **unique** (no four points can be concyclic); in DT($P$), the circumscribed circle of **any** triangle contains no other point within its range.
2.  Maximizing the minimum angle: among the triangulations that point set $P$ can possibly form, the minimum angle of the triangles formed by DT($P$) is the maximum. In this sense, DT($P$) is the triangulation **closest to being regular**. Specifically, for the diagonal of the convex quadrilateral formed by two adjacent triangles, after they are swapped, the minimum of the two interior angles no longer increases.

![A Delaunay triangulation showing circumscribed circles](./images/triangulation-1.png)

### Properties

1.  Closest: form triangles from the closest three points, and all line segments (edges of triangles) do not intersect.
2.  Uniqueness: no matter from where in the region the construction begins, the final result is consistent (no four points in the point set can be concyclic).
3.  Optimality: if the diagonals of the convex quadrilateral formed by any two adjacent triangles can be swapped, then the minimum angle among the six interior angles of the two triangles does not change.
4.  Most regular: if the minimum angles of each triangle in a triangulation are arranged in ascending order, then the values obtained by the arrangement of the Delaunay triangulation are the largest.
5.  Regionality: adding, deleting, or moving a certain vertex only affects nearby triangles.
6.  Has a convex hull: the outermost boundary of the triangulation forms a convex polygon hull.

## Divide-and-conquer algorithm for constructing DT

DT has many construction algorithms; among the $O(n \log n)$ construction algorithms, the divide-and-conquer algorithm is the easiest to understand and implement.

The first step of divide-and-conquer construction of DT is to arrange the given point set in **ascending** order by $x$ coordinate; the figure below shows a sorted point set of size $10$.

![A sorted point set of size 10](./images/triangulation-2.svg)

Once the point set is ordered, we can continually divide it into two parts (divide-and-conquer), until the sub-point-set size does not exceed $3$. Then these sub-point-sets can be immediately triangulated into a triangle or a line segment.

![Divided into point sets containing 2 or 3 points](./images/triangulation-3.svg)

Then during the divide-and-conquer backtracking process, the already-triangulated left and right sub-point-sets can be merged in turn. The merged triangulation contains LL-edges (edges of the left sub-point-set), RR-edges (edges of the right sub-point-set), and LR-edges (new edges produced by connecting the left and right triangulations); as in the figure, LL-edges (gray), RR-edges (red), LR-edges (blue). For the merged triangulation, to maintain the DT property, we **may** need to delete some LL-edges and RR-edges, but we **will not** add LL-edges and RR-edges during merging.

![edge](./images/triangulation-4.svg)

The first step of merging the left and right triangulations is inserting the base LR-edge; the base LR-edge is the **bottommost** LR-edge that does not intersect **any** LL-edge or RR-edge.

![Merging the left and right triangulations](./images/triangulation-5.svg)

Then, we need to determine the next LR-edge **immediately** above the base LR-edge. For example, for the right point set, the possible endpoints (right endpoints) of the next LR-edge are the other endpoints ($6, 7, 9$) of the RR-edges connected to the right endpoint of the base LR-edge, and the left endpoint is point $2$.

![The next LR-edge](./images/triangulation-6.svg)

For a possible endpoint, we need to test it by the following two criteria:

1.  The angle between its corresponding RR-edge and the base LR-edge is less than $180$ degrees.
2.  The circle formed by the two endpoints of the base LR-edge and this possible point contains no other **possible point**.

![Testing possible points](./images/triangulation-7.svg)

As in the figure above, the green circle corresponding to possible point $6$ contains possible point $9$, while the purple circle corresponding to possible point $7$ contains no other possible point, so point $7$ is the right endpoint of the next LR-edge.

For the left point set, we just do mirror processing.

![Testing left-side possible points](./images/triangulation-8.svg)

When neither the left nor the right point set contains any possible point meeting the criteria, the merge is complete. When a possible point meets the criteria, an LR-edge needs to be added; for the LL-edges and RR-edges intersecting the LR-edge to be added, delete them.

When both the left and right point sets have possible points, judge whether the circle corresponding to the left point contains the right point; if it does, it does not meet the criteria; the same judgment is made for the right point. Generally only one possible point meets the criteria (unless four points are concyclic).

![The next LR-edge](./images/triangulation-9.svg)

After this LR-edge is added, take it as the base LR-edge and repeat the above steps to continue adding the next one, until the merge is complete.

![Merging](./images/triangulation-10.svg)

## Code

??? note "Implementation"
    ```cpp
    #include <algorithm>
    #include <cmath>
    #include <cstring>
    #include <list>
    #include <utility>
    #include <vector>
    
    constexpr double EPS = 1e-8;
    constexpr int MAXV = 10000;
    
    struct Point {
      double x, y;
      int id;
    
      Point(double a = 0, double b = 0, int c = -1) : x(a), y(b), id(c) {}
    
      bool operator<(const Point &a) const {
        return x < a.x || (fabs(x - a.x) < EPS && y < a.y);
      }
    
      bool operator==(const Point &a) const {
        return fabs(x - a.x) < EPS && fabs(y - a.y) < EPS;
      }
    
      double dist2(const Point &b) {
        return (x - b.x) * (x - b.x) + (y - b.y) * (y - b.y);
      }
    };
    
    struct Point3D {
      double x, y, z;
    
      Point3D(double a = 0, double b = 0, double c = 0) : x(a), y(b), z(c) {}
    
      Point3D(const Point &p) { x = p.x, y = p.y, z = p.x * p.x + p.y * p.y; }
    
      Point3D operator-(const Point3D &a) const {
        return Point3D(x - a.x, y - a.y, z - a.z);
      }
    
      double dot(const Point3D &a) { return x * a.x + y * a.y + z * a.z; }
    };
    
    struct Edge {
      int id;
      std::list<Edge>::iterator c;
    
      Edge(int id = 0) { this->id = id; }
    };
    
    int cmp(double v) { return fabs(v) > EPS ? (v > 0 ? 1 : -1) : 0; }
    
    double cross(const Point &o, const Point &a, const Point &b) {
      return (a.x - o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x);
    }
    
    Point3D cross(const Point3D &a, const Point3D &b) {
      return Point3D(a.y * b.z - a.z * b.y, -a.x * b.z + a.z * b.x,
                     a.x * b.y - a.y * b.x);
    }
    
    int inCircle(const Point &a, Point b, Point c, const Point &p) {
      if (cross(a, b, c) < 0) std::swap(b, c);
      Point3D a3(a), b3(b), c3(c), p3(p);
      b3 = b3 - a3, c3 = c3 - a3, p3 = p3 - a3;
      Point3D f = cross(b3, c3);
      return cmp(p3.dot(f));  // check same direction, in: < 0, on: = 0, out: > 0
    }
    
    int intersection(const Point &a, const Point &b, const Point &c,
                     const Point &d) {  // seg(a, b) and seg(c, d)
      return cmp(cross(a, c, b)) * cmp(cross(a, b, d)) > 0 &&
             cmp(cross(c, a, d)) * cmp(cross(c, d, b)) > 0;
    }
    
    class Delaunay {
     public:
      std::list<Edge> head[MAXV];  // graph
      Point p[MAXV];
      int n, rename[MAXV];
    
      void init(int n, Point p[]) {
        memcpy(this->p, p, sizeof(Point) * n);
        std::sort(this->p, this->p + n);
        for (int i = 0; i < n; i++) rename[p[i].id] = i;
        this->n = n;
        divide(0, n - 1);
      }
    
      void addEdge(int u, int v) {
        head[u].push_front(Edge(v));
        head[v].push_front(Edge(u));
        head[u].begin()->c = head[v].begin();
        head[v].begin()->c = head[u].begin();
      }
    
      void divide(int l, int r) {
        if (r - l <= 2) {  // #point <= 3
          for (int i = l; i <= r; i++)
            for (int j = i + 1; j <= r; j++) addEdge(i, j);
          return;
        }
        int mid = (l + r) / 2;
        divide(l, mid);
        divide(mid + 1, r);
    
        std::list<Edge>::iterator it;
        int nowl = l, nowr = r;
    
        for (int update = 1; update;) {
          // find left and right convex, lower common tangent
          update = 0;
          Point ptL = p[nowl], ptR = p[nowr];
          for (it = head[nowl].begin(); it != head[nowl].end(); it++) {
            Point t = p[it->id];
            double v = cross(ptR, ptL, t);
            if (cmp(v) > 0 || (cmp(v) == 0 && ptR.dist2(t) < ptR.dist2(ptL))) {
              nowl = it->id, update = 1;
              break;
            }
          }
          if (update) continue;
          for (it = head[nowr].begin(); it != head[nowr].end(); it++) {
            Point t = p[it->id];
            double v = cross(ptL, ptR, t);
            if (cmp(v) < 0 || (cmp(v) == 0 && ptL.dist2(t) < ptL.dist2(ptR))) {
              nowr = it->id, update = 1;
              break;
            }
          }
        }
    
        addEdge(nowl, nowr);  // add tangent
    
        for (int update = 1; true;) {
          update = 0;
          Point ptL = p[nowl], ptR = p[nowr];
          int ch = -1, side = 0;
          for (it = head[nowl].begin(); it != head[nowl].end(); it++) {
            if (cmp(cross(ptL, ptR, p[it->id])) > 0 &&
                (ch == -1 || inCircle(ptL, ptR, p[ch], p[it->id]) < 0)) {
              ch = it->id, side = -1;
            }
          }
          for (it = head[nowr].begin(); it != head[nowr].end(); it++) {
            if (cmp(cross(ptR, p[it->id], ptL)) > 0 &&
                (ch == -1 || inCircle(ptL, ptR, p[ch], p[it->id]) < 0)) {
              ch = it->id, side = 1;
            }
          }
          if (ch == -1) break;  // upper common tangent
          if (side == -1) {
            for (it = head[nowl].begin(); it != head[nowl].end();) {
              if (intersection(ptL, p[it->id], ptR, p[ch])) {
                head[it->id].erase(it->c);
                head[nowl].erase(it++);
              } else {
                it++;
              }
            }
            nowl = ch;
            addEdge(nowl, nowr);
          } else {
            for (it = head[nowr].begin(); it != head[nowr].end();) {
              if (intersection(ptR, p[it->id], ptL, p[ch])) {
                head[it->id].erase(it->c);
                head[nowr].erase(it++);
              } else {
                it++;
              }
            }
            nowr = ch;
            addEdge(nowl, nowr);
          }
        }
      }
    
      std::vector<std::pair<int, int>> getEdge() {
        std::vector<std::pair<int, int>> ret;
        ret.reserve(n);
        std::list<Edge>::iterator it;
        for (int i = 0; i < n; i++) {
          for (it = head[i].begin(); it != head[i].end(); it++) {
            if (it->id < i) continue;
            ret.push_back(std::make_pair(p[i].id, p[it->id].id));
          }
        }
        return ret;
      }
    };
    ```

## Voronoi diagram

The Voronoi diagram is composed of a set of continuous polygons composed of the perpendicular bisectors of the lines connecting two adjacent points; according to $n$ non-coinciding seed points in the plane, it divides the plane into $n$ regions, such that the distance from a point in each region to the seed point of the region it is in is closer than the distance to the seed points of other regions.

The Voronoi diagram is the dual graph of the Delaunay triangulation; one can use the divide-and-conquer algorithm for constructing the Delaunay triangulation to find the triangular mesh, then use the leftmost-turn-line algorithm to find its dual graph, achieving the construction of the Voronoi diagram in $O(n \log n)$ time complexity.

## Problems

[SGU 383 Caravans](https://codeforces.com/problemsets/acmsguru/problem/99999/383) triangulation + binary lifting

[ContestHunter. Endless Destruction](http://noi-test.zzstep.com/contest/Beta%20Round%20%EF%BC%832%20%28%E6%96%B0%E7%96%86%E7%9C%81%E9%98%9F%E4%BA%92%E6%B5%8BWeek1-Day2%29/%E6%97%A0%E5%B0%BD%E7%9A%84%E6%AF%81%E7%81%AD) triangulation to find the dual graph and build a Voronoi diagram

[Codeforces Gym 103485M. Constellation collection](https://codeforces.com/gym/103485/problem/M) build a graph after triangulation and perform floodfill

## References and further reading

1.  [Wikipedia - Triangulation (geometry)](https://en.wikipedia.org/wiki/Triangulation_%28geometry%29)
2.  [Wikipedia - Delaunay triangulation](https://en.wikipedia.org/wiki/Delaunay_triangulation)
3.  Samuel Peterson -[Computing Constrained Delaunay Triangulations in 2-D (1997-98)](http://www.geom.uiuc.edu/~samuelp/del_project.html)
