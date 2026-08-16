author: countercurrent-time, StudyingFather

Interactive problems already appeared in the IOI of the last century. Although interactive problems have not appeared in contests below the provincial-selection level in recent years, in 2019 two interactive problems—*P5208 [WC2019] I-kun's Shop* and *P5473 [NOI2019] I-kun's Exploration*—appeared consecutively in the NOI series, which may indicate that interactive problems are returning to the NOI series.

Interactive problems do not have very high prerequisite algorithm requirements, and generally do not have strict time limits; how good a program is often depends only on the query-count limit. So when learning interactive problems, it is recommended to progress gradually by difficulty. If you want to train your algorithmic thinking rather than just learn algorithms, then doing interactive problems is a very good method. Although interactive problems usually place relatively low requirements on the algorithms a contestant has mastered, it is still recommended to master some advanced and provincial-selection-level algorithms before attempting interactive problems, because by then your algorithmic-thinking level and knowledge breadth have reached a certain level. For a basic introduction to interactive problems, refer to **OI Wiki**'s [Problem-type introduction - Interactive problems](./problems.md#interactive-problems).

Special errors of interactive problems:

-   The contestant needs to flush the buffer after each output, otherwise it causes an Idleness limit exceeded error. In addition, if the problem contains multiple datasets and the program can know the answer before reading in all the data, it must still read in all the data, otherwise it will likewise cause ILE due to jumbled input (you can issue multiple queries at once and receive the answers to all queries at once). At the same time, try not to use fast input.
-   If the program makes too many queries, Codeforces gives a Wrong Answer judging result (though the judging system will explain the reason for the Wrong Answer), while UVa gives a Protocol Limit Exceeded (PLE) judging result.
-   If the program's interaction format is wrong, UVa gives a Protocol Violation (PV) judging result.

Since the input/output of interactive problems is rather tedious, it is recommended to encapsulate the input and output functions separately.

During a contest, if the problem setter provides a grader header file (for debugging grader interactive problems) or a checker program (for debugging stdio interactive problems), then debugging the interactive problem is relatively simple, because diff-testing an interactive problem is much harder than diff-testing an ordinary problem. Without `testlib.h`, the stdio interaction library for a problem with many interaction details generally has about 3k of code, plus a 3k-long diff-tester, requiring at least an hour to implement. However, regardless of whether there is a debugging program, debugging the code of an interactive problem often requires the contestant to simulate the interaction process with the program, so interactive problems require the contestant to design a high-quality program, to get it right on the first try as much as possible, and to have strong static error-checking ability.

Examples:

-   [CF679A Bear and Prime 100](https://codeforces.com/problemset/problem/679/A)
-   [CF843B Interactive LowerBound](https://codeforces.com/problemset/problem/843/B)
-   [UOJ206 \[APIO2016\] Gap](http://uoj.ac/problem/206)
-   [CF750F New Year and Finding Roots](https://codeforces.com/problemset/problem/750/F)
-   [UVa12731 Mysterious Space Station](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=823&page=show_problem&problem=4584)

## CF679A Bear and Prime 100

Every prime has exactly two factors, so directly enumerate the factors of the number to guess. Since the limit is at most 20 queries, and for a larger number (such as 92), when trying to factorize we find we need to enumerate primes up to at most $\lfloor\frac{n}{2}\rfloor$. So we first sieve the primes within 50 and query all of them each time.

Since diff-testing this problem is relatively easy, we can directly try every number in the value range. We will find that the program cannot effectively handle the squares of primes. So we must put in the squares of 2, 3, 5, 7—namely 4, 9, 25, 49—for a total of 19 numbers, which fits the problem.

??? note "Reference code"
    ```cpp
    #include <cstdio>
    constexpr int prime[] = {2,  3,  4,  5,  7,  9,  11, 13, 17, 19,
                             23, 25, 29, 31, 37, 41, 43, 47, 49};
    int cnt = 0;
    char res[5];
    
    int main() {
      for (int i : prime) {
        printf("%d\n", i);
        fflush(stdout);
        scanf("%s", res);
        if (res[0] == 'y' && ++cnt == 2) return printf("composite"), 0;
      }
      printf("prime");
      return 0;
    }
    ```

## CF843B Interactive LowerBound

The linked list has at most $5 \times 10 ^ 4$ elements, but we can only query $1999$ times, and can only obtain the successor of an element, so the ordinary method of traversing the whole linked list is unusable. There is only one way to directly approach the position of the target element: random sampling.

For the case $n < 2000$ we enumerate directly; when $n \ge 2000$ we scatter 1000 points, and then the expected distance between these points is very small, so we can directly traverse forward from the largest value smaller than $x$; it can be proven that we obtain the answer before reaching the next point. During the traversal, once we find an element greater than or equal to $x$, we can directly deduce it.

Although the overall idea is simple, in practice, if one has not learned imperfect random algorithms such as simulated annealing, thinking through it may be somewhat difficult.

Also, since Codeforces has a hack mechanism, many people will deliberately hack code that does not initialize the random seed, so before the `random_shuffle()` function one needs `srand((size_t)new char)`.

??? note "Reference code"
    ```cpp
    #include <algorithm>
    #include <cstdio>
    #include <cstdlib>
    constexpr int N = 50005;
    int n, start, x;
    int a[N];
    
    int main() {
      scanf("%d%d%d", &n, &start, &x);
      if (n < 2000) {
        int ans = 2e9;
        for (int i = 1; i <= n; i++) {
          printf("? %d\n", i), fflush(stdout);
          int val, next;
          scanf("%d%d", &val, &next);
          if (val >= x) ans = std::min(ans, val);
        }
        if (ans == 2e9) ans = -1;
        printf("! %d", ans), fflush(stdout);
      } else {
        srand((size_t) new char);
        int p = start, ans = 0;
        for (int i = 1; i <= n; i++) a[i] = i;
        std::random_shuffle(a + 1, a + n + 1);
        for (int i = 1; i <= 1000; i++) {
          printf("? %d\n", a[i]), fflush(stdout);
          int val, next;
          scanf("%d%d", &val, &next);
          if (val < x && val > ans) p = a[i], ans = val;
        }
        while (p != -1 && ans < x) {
          printf("? %d\n", p), fflush(stdout);
          int val, next;
          scanf("%d%d", &val, &next);
          ans = val;
          p = next;
        }
        if (ans < x) ans = -1;
        printf("! %d", ans), fflush(stdout);
      }
      return 0;
    }
    ```

## UOJ206 [APIO2016] Gap

Discuss two subtasks:

1.  Query-count limit.

    Consider the first query. Because we do not know any number at the start, we need to query the range $[1, 10 ^ {18}]$ to obtain the maximum and minimum values.

    Since the query-count limit is exactly $\frac{N + 1}{2}$, consider how to obtain a value not previously obtained each time, so that we can obtain all numbers in the sequence roughly within the count limit. The method is also simple: after each query of $[s, t]$, let the obtained values be $mn, mx$; then the next query is $[mn + 1, mx - 1]$.

2.  Query-interval-size limit.

    Since the problem requires that the sum of the counts of numbers in the queried intervals not exceed $3N$, consider minimizing the query intervals. The above method is no longer usable, because the sum of the counts of numbers in its query intervals is of scale $O(N ^ 2)$. We can consider binary-searching the value range, but this method is not reliable and can be adversarially made $O(N ^ 2)$ in the worst case. So we need a more effective way to partition the value range, avoiding repeatedly querying points within a query interval and wasting opportunities.

    Considering that the answer is not smaller than $\lfloor\frac{a_n - a_1}{N - 1}\rfloor$, we can consider partitioning the value range by this value: let $i$ initially be 0 and $ans$ initially be the above value, each time query $[i, i + ans]$ and update $ans$, and then increase $i$ with step $ans$.

    However, this method also does not adapt well to subtask 1, because in the worst case many queries may have no number in their value range.

??? note "Reference code"
    ```cpp
    #include <algorithm>
    #include <cstdio>
    
    #include "gap.h"
    
    long long findGap(int T, int N) {
      static long long a[100005] = {}, ans = 0;
      long long s = 0, t = 1e18, s1, t1;
      if (T == 1) {
        int l = 1, r = N;
        while (l <= r) {
          MinMax(s, t, &s1, &t1);
          a[l++] = s1, a[r--] = t1;
          s = s1 + 1, t = t1 - 1;
        }
        for (int i = 2; i <= N; i++) ans = std::max(ans, a[i] - a[i - 1]);
      } else if (T == 2) {
        MinMax(s, t, &s1, &t1);
        ans = (t1 - s1) / (N - 1);
        long long l = s1 + 1, r = t1, last = s1;
        for (long long i = l; i <= r;) {
          MinMax(i, i + ans, &s1, &t1);
          i += ans + 1;
          if (s1 != -1) ans = std::max(ans, s1 - last), last = t1;
        }
      }
      return ans;
    }
    ```

## CF750F New Year and Finding Roots

Seeing the strict requirements $h \le 7$ and query count $\le 16$, we need to very strictly maximize the use of the information obtained from visits.

When $h \le 4$ we can directly brute-force enumerate. However, when $h > 4$ we need a very efficient traversal algorithm.

Random sampling is not a good method, because random sampling cannot determine whether we are close enough to the root, and with pure random sampling, the probability of hitting the root at least once is $1 - (\frac{2 ^ h - 2}{2 ^ h - 1})$; even after excluding repeated samples, the probability of hitting the root is still very small.

Since $1 \le k \le 3$ and we do not know which side is closer to the root, we consider the worst case, i.e. if $k = 3$, the first two of our traversal directions are away from the root and the third is toward the root. So we must traverse in all three directions.

Consider the two traversal methods, bfs and dfs. Since the bfs search tree may be very large, we prioritize dfs. Of course, if we know the current depth and the current depth is small enough that the size of the search tree within the depth range is at most the remaining count, we can directly bfs.

Knowing the current node's depth and the current traversal direction gives a big advantage. However, knowing whether we are traversing toward the root or toward the leaves is very difficult. With dfs, we only know the current direction when we traverse to the root ($k = 2$) or a leaf ($k = 1$). So we need to know the current node's depth as much as possible, and cannot use a method like iterative-deepening search that stops midway through the traversal.

Consider randomizing an initial node; starting from the initial node, we may encounter the worst case above.

If $k = 1$, we can directly know the current node's depth.

If $k = 2$, the current node is the root.

If $k = 3$, we directly consider dfs in all three directions. Considering that two of the directions go directly toward the leaves, with the same traversal path length; the other direction goes toward the root, but may accidentally go toward the leaves midway, so its traversal path length is larger. At this point we can compute the current node's depth.

When $k = 1$ or $k = 3$, we need to consider the longer traversal path. We can know the point on the path with the smallest depth (necessarily smaller than the initial node's depth). If we mark visited nodes and no longer traverse them, then starting from that node there is only one traversal path. Although this path may still go toward the leaves, there must likewise be a node on this path with a smaller depth than the starting point, from which we can continue to repeat the above steps.

Of course, when we consider the worst case for $h = 7$ (each time going only one step toward the root, then directly going toward the leaves), we find that with dfs alone, in the worst case we need $\frac{(1 + 7) \times 7}{2} = 28$ queries. However, we already know the initial node's depth, so we can compute the depth of all traversed nodes, and according to our earlier discussion of bfs, determine whether we can directly bfs from the node with the smallest depth.

At this point, we can compute that the worst case needs 17 times. So we consider removing one node from the search tree (given the property that dfs can only traverse blindly, we consider bfs): that is, when doing a bfs of depth $k$, the search tree has at most $2 ^ k - 1$ nodes, and it may take $2 ^ k - 1$ queries to determine which node has exactly 2 neighbors. However, if we have queried $2 ^ k - 2$ of the nodes, we know the last node must be the root.

At this point the optimal solution in the worst case is: when $h = 7$, dfs from a leaf, each time going only one step toward the root, then directly going toward the leaves; after 10 queries, the currently-known node with the smallest depth has depth 4, and since its parent is known, we directly bfs from its parent (search tree depth 3, node count $2 ^ 3 - 1 = 7$). During the bfs, after $2 ^ 3 - 2 = 6$ queries, we determine that the last node on the bfs search tree is the root.

At this point our algorithm can hit exactly 16 times in the worst case.

??? note "Reference code"
    ```cpp
    #include <algorithm>
    #include <cstdio>
    #include <queue>
    #include <vector>
    using namespace std;
    constexpr int N = 256 + 5;
    int T, h, chance;
    bool ok;
    vector<int> to[N], path;
    
    bool read(int x) {
      if (to[x].empty()) {
        printf("? %d\n", x), fflush(stdout);
        int k, t;
        scanf("%d", &k);
        if (k == 0) exit(0);
        for (int i = 0; i < k; i++) {
          scanf("%d", &t);
          to[x].push_back(t);
        }
        if (k == 2) {
          printf("! %d\n", x), fflush(stdout);
          return ok = true;
        }
        chance--;
      }
      return false;
    }
    
    bool dfs(int x) {
      if (to[x].empty()) path.push_back(x);
      if (read(x)) return true;
      for (int i : to[x])
        if (to[i].empty()) return dfs(i);
      return false;
    }
    
    void bfs(int s, int k) {
      queue<int> q;
      for (int i : to[s])
        if (to[i].empty()) q.push(i);
      for (int i = 1; i < k; i++) {
        int x = q.front();
        q.pop();
        if (read(x)) return;
        for (int j : to[x])
          if (to[j].empty()) q.push(j);
      }
      for (int i = 1; i < k; i++) {
        int x = q.front();
        q.pop();
        if (read(x)) return;
      }
      printf("! %d\n", q.front()), fflush(stdout);
    }
    
    int main() {
      for (scanf("%d", &T); T--;) {
        ok = false;
        for (int i = 0; i < N; i++) to[i].clear();
        chance = 16;
        scanf("%d", &h);
        if (h == 0) exit(0);
        vector<int> long_path;
        if (read(1)) continue;
        int root, dep;
        if (to[1].size() == 1)
          root = 1, dep = h;
        else {
          for (int i : to[1]) {
            path.clear();
            if (dfs(i)) break;
            if (path.size() > long_path.size()) swap(path, long_path);
          }
          if (ok) continue;
          dep = h - (path.size() + long_path.size()) / 2;
          root = long_path.at((long_path.size() - (h - dep)) - 1);
        }
        while ((1 << (dep - 1)) - 2 > chance) {
          path.clear();
          if (dfs(root)) break;
          dep = h - (h - dep + path.size()) / 2;
          root = path.at((path.size() - (h - dep)) - 1);
        }
        if (!ok) bfs(root, 1 << (dep - 2));
      }
      return 0;
    }
    ```

## UVa12731 Mysterious Space Station

Since the only feedback is whether you hit a wall when moving, we should consider walking as close to the wall as possible while the robot does not get lost; this has several benefits:

-   When walking close to the wall, it is easy to know whether you will hit a wall, obtaining as much information as possible.
-   The cells along the wall never have portals, which avoids the robot getting lost.

So, if we know the robot may be at some position along the wall, to determine whether the robot is really at this position, we can use the ["one-hand-on-the-wall method"](https://en.wikipedia.org/wiki/Maze_solving_algorithm) to determine whether we are really at this position. By the topological principle, in a maze with walls on both sides, if you enter from the entrance and always keep one hand on the same wall, you are guaranteed to find the exit. Since the walls in this problem are closed, you only need to walk along the path beside the wall to be guaranteed to return to the origin without hitting a wall. In addition, since the path beside the wall is the maximal closed loop on the map, the actual code does not need to deliberately hit walls to ensure the robot is beside the wall; you can use a mark to indicate the wall-side path on the map. And once you hit a wall, you need to quickly return along the original path, which reduces the number of steps while avoiding the robot getting lost.

From the above, we can deduce the trial-and-error method for determining whether the robot is in a specific cell: move the robot to the wall-side path without stepping onto an unknown cell or a known portal, then walk one loop around the wall-side path. If no wall is hit during this process, we can determine that the robot is indeed in the specific cell.

We can use the above method: first mark all unknown cells on the map, then from top to bottom and left to right, determine one by one whether each unknown cell is a portal. We can first walk above the unknown cell, then walk down and left. Then use the above method to determine whether the robot is to the left of the unknown cell. If not, it means the robot is not where it should be, i.e. the unknown cell is a portal.

After finding the unknown cells, we need to determine the pairing relationship of the 2k unknown cells; the actual method is also simple: just brute-force pair them. Since $k \le 5$, at most $9 + 7 + 5 + 3$ trials of the trial-and-error method are needed. By comparison, determining the situation of all unknown cells on the map needs at most $121 - 40$ trials of the trial-and-error method.

Since the following code can currently only pass UOJ's mirror problem [#247. 【Rujia Liu's Present 7】Mysterious Space Station](http://uoj.ac/problem/247) but cannot pass the original UVa problem—and after modifying Rujia Liu's reference solution on UOJ it still cannot pass, and Rujia Liu cannot be contacted for now—the following code is based on UOJ.

That said, Rujia Liu's reference solution is still of much higher quality than the following code; you can view the [reference solution that passed the UOJ mirror problem](http://uoj.ac/submission/105789) on UOJ. Under the same data, the reference solution uses far fewer moves.

??? note "Reference code"
    ```cpp
    #include <algorithm>
    #include <cstdio>
    #include <cstring>
    #include <iostream>
    #include <queue>
    #include <stack>
    
    #define Wall 0
    #define Unknown 1
    #define Space 2
    #define Gate 3
    #define Path 4
    
    const int N = 20;
    const int dir[8][2] = {{0, 1},  {1, 0}, {0, -1}, {-1, 0},
                           {-1, 1}, {1, 1}, {1, -1}, {-1, -1}};
    const char dirs[5] = "ESWN";
    int n, m, k;
    int a[N][N], id[N][N];
    
    struct point {
      int x, y;
    
      point(int x = 0, int y = 0) : x(x), y(y) {}
    
      bool operator==(const point& tmp) const { return x == tmp.x && y == tmp.y; }
    
      bool operator!=(const point& tmp) const { return !(*this == tmp); }
    
      point side(int d) const { return point(x + dir[d][0], y + dir[d][1]); }
    
      int check(int d) { return a[x + dir[d][0]][y + dir[d][1]]; }
    
      int id() { return ::id[x][y]; }
    } start;
    
    std::vector<std::pair<point, int>> path;
    std::pair<point, point> ans[N];
    std::pair<point, bool> vis[N];
    
    bool walk(int d) {
      printf("MoveRobot %c\n", dirs[d]);
      fflush(stdout);
      int ret;
      scanf("%d", &ret);
      return ret;
    }
    
    bool walk(int d, std::stack<int>& st) {
      if (walk(d)) {
        st.push(d);
        return true;
      }
      return false;
    }
    
    bool read() {
      if (scanf("%d%d%d", &n, &m, &k) != 3) return false;
      if (n == 0) return false;
      memset(a, 0, sizeof(a));
      for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) {
          char c;
          std::cin >> c;
          if (c == 'S') start = point(i, j);
          if (c == '*')
            a[i][j] = Wall;
          else
            a[i][j] = Unknown;
        }
      return true;
    }
    
    void answer() {
      for (int i = 0; i < k; i++)
        printf("Answer %d %d\n", ans[i].first.id(), ans[i].second.id());
      fflush(stdout);
    }
    
    // One-hand-on-the-wall method: since the Path beside the wall is a maximal closed loop,
    // it suffices that no obstacle is hit while walking along the Path
    void wall_follower_init(point x, int last, int wallside, point s) {
      if (x == s && !path.empty()) return;
      if (x.check(wallside) == Path) {
        path.push_back(std::make_pair(x, wallside));
        wall_follower_init(x.side(wallside), wallside, last ^ 2, s);
      } else if (x.check(last) == Wall) {
        for (int i = 0; i < 4; i++)
          if (i != (last ^ 2) && x.check(i) != Wall) {
            path.push_back(std::make_pair(x, i));
            wall_follower_init(x.side(i), i, last, s);
            return;
          }
      } else {
        path.push_back(std::make_pair(x, last));
        wall_follower_init(x.side(last), last, wallside, s);
      }
    }
    
    void init() {
      int cnt = 1;
      for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) {
          if (a[i][j] == Unknown) {
            id[i][j] = cnt++;
            for (int k = 0; k < 8; k++)
              if (point(i, j).check(k) == Wall) {
                a[i][j] = Path;
                break;
              }
          } else
            id[i][j] = 0;
        }
      path.clear();
      int wallside = 0, last = 0;
      for (int i = 0; i < 4; i++)
        if (start.check(i) == Wall) {
          wallside = i;
          break;
        }
      for (int i = 0; i < 4; i++)
        if (start.check(i) == Path && i != (wallside ^ 2)) {
          last = i;
          break;
        }
      wall_follower_init(start, last, wallside, start);
    }
    
    void undo(std::stack<int>& st) {
      while (!st.empty()) walk(st.top() ^ 2), st.pop();
    }
    
    bool wall_follower(point x) {
      std::stack<int> st;
      bool ok = true;
      int i = 0;
      while (i < path.size() && path[i].first != x) i++;
      for (int j = i; ok && j < path.size(); j++) {
        if (walk(path[j].second))
          st.push(path[j].second);
        else
          ok = false;
      }
      for (int j = 0; ok && j < i; j++) {
        if (walk(path[j].second))
          st.push(path[j].second);
        else
          ok = false;
      }
      if (!ok) undo(st);
      return ok;
    }
    
    // Determine that you are currently at x, using the "crossing the river by feeling the stones"
    // method: just walk to a Path along a direction that avoids obstacles, unknown cells, and portals.
    // Used when finding portals and pairing portals
    void bfs(point s, point t, std::vector<int>& v) {
      static int map[N][N] = {};
      memset(map, -1, sizeof(map));
      std::queue<point> q;
      map[s.x][s.y] = 4;
      q.push(s);
      while (!q.empty()) {
        point x = q.front();
        q.pop();
        if (x == t) break;
        for (int i = 0; i < 4; i++) {
          point y = x.side(i);
          if ((x.check(i) == Path || x.check(i) == Space) && map[y.x][y.y] == -1) {
            map[y.x][y.y] = i;
            q.push(y);
          }
        }
      }
      for (point x = t; x != s; x = x.side(map[x.x][x.y] ^ 2)) {
        v.push_back(map[x.x][x.y]);
      }
      std::reverse(v.begin(), v.end());
    }
    
    bool move(point s, point t, std::stack<int>& st) {  // used when close to a portal
      static std::vector<int> v;
      v.clear();
      bfs(s, t, v);
      for (int i : v)
        if (!walk(i, st)) return false;
      return true;
    }
    
    // Move toward the wall as fast as possible
    bool make_sure(point x, int last) {
      if (a[x.x][x.y] == Path) return wall_follower(x);
      for (int i = 0; i < 4; i++)
        if ((x.check(i) == Path || x.check(i) == Space) && i != (last ^ 2)) {
          if (!walk(i)) return false;
          bool ret = make_sure(x.side(i), i);
          walk(i ^ 2);
          return ret;
        }
      return false;
    }
    
    void find_gate() {
      int cnt = 0;
      std::stack<int> st;
      for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
          if (cnt == k * 2 && a[i][j] == Unknown)
            a[i][j] = Space;
          else if (a[i][j] == Unknown) {
            bool ok = true;
            if (!move(start, point(i - 1, j), st))
              ok = false;
            else if (!walk(1, st))
              ok = false;
            else if (!walk(2, st))
              ok = false;
            else if (!make_sure(point(i, j - 1), -1))
              ok = false;
            if (!ok) {
              vis[cnt++] = std::make_pair(point(i, j), false);
              a[i][j] = Gate;
              for (int k = 0; k < 8; k++) {
                point y = point(i, j).side(k);
                if (point(i, j).check(k) == Unknown) a[y.x][y.y] = Space;
              }
            } else
              a[i][j] = Space;
            undo(st);
          }
    }
    
    void make_gate_pair() {
      int cnt = 0;
      std::stack<int> st;
      for (int i = 0; i < k * 2; i++)
        if (!vis[i].second)
          for (int j = 0; !vis[i].second && j < k * 2; j++)
            if (j != i && !vis[j].second) {
              bool ok = true;
              if (!move(start, vis[i].first.side(2), st))
                ok = false;
              else if (!walk(0, st))
                ok = false;
              else if (!make_sure(vis[j].first.side(0), -1))
                ok = false;
              if (ok) {
                ans[cnt++] = std::make_pair(vis[i].first, vis[j].first);
                vis[i].second = vis[j].second = true;
              }
              undo(st);
            }
    }
    
    int main() {
      while (read()) {
        init();
        find_gate();
        make_gate_pair();
        answer();
      }
      return 0;
    }
    ```

## Exercises

-   [Rujia Liu's Present 7, a special interactive-problem contest, is of very high quality and recommended.](https://onlinejudge.org/contests/328-9976a2e2/)
-   [P5473 \[NOI2019\] I-kun's Exploration](https://www.luogu.com.cn/problem/P5473)
-   [P5208 \[WC2019\] I-kun's Shop](https://www.luogu.com.cn/problem/P5208)

## References and further reading

-   [Implementing the interactive-problem feature of an online judge with Linux pipes](https://www.cnblogs.com/tsreaper/p/pipe-interactive.html)
