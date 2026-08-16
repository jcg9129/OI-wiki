## Definition

Some [bitmask DP](./state.md) problems require us to record connectivity information of the state; this kind of problem is generally vividly called plug DP or connectivity bitmask DP. Examples include counting Hamiltonian paths on a grid graph, counting the black-white colorings of a board such that cells of the same color form a single connected component, and counting the spanning trees of a specific graph, and so on. These problems usually require us to encode the connectivity of the state and discuss the changes of connectivity during the state transition.

## Introduction

### Domino tiling and contour-line DP

To review the old and learn the new, before starting to learn plug DP, let us first review a classic problem.

???+ note "Example [「HDU 1400」Mondriaan's Dream](https://acm.hdu.edu.cn/showproblem.php?pid=1400)"
    Problem summary: fill an $N\times M$ board completely with $1\times 2$ or $2\times 1$ dominoes, and count the number of ways.

When $n$ or $m$ is not large, this kind of problem can be solved with [bitmask DP](./state.md). Dividing the stages row by row, let $dp(i,s)$ be the number of ways when the first $i$ rows have been considered and the state of the $i$-th row is $s$. Here each bit of the state $s$ can indicate whether this position has been covered by the previous row.

![domino](./images/domino.svg)

Another way of dividing the stages is cell-by-cell DP, or contour-line DP. $dp(i,j,s)$ is the number of ways when we have considered up to row $i$, column $j$, and the state on the current contour line is $s$.

Although in cell-by-cell DP our state gains one more dimension, the time complexity of the transition is reduced to $O(1)$, so the time complexity is unchanged. We use $f_0$ to denote the state of the current stage and $f_1$ to denote the state of the next stage, and $u = f_0(s)$ to denote the current enumerated function value; then we have the following state-transition equation:

```cpp
if (s >> j & 1) {       // if already covered
  f1[s ^ 1 << j] += u;  // do not place
} else {                // if not covered
  if (j != m - 1 && (!(s >> j + 1 & 1))) f1[s ^ 1 << j + 1] += u;  // place horizontally
  f1[s ^ 1 << j] += u;                                             // place vertically
}
```

We observe that here the equations for not placing and placing vertically can be merged.

??? note "Implementation"
    ```cpp
    #include <algorithm>
    #include <iostream>
    using namespace std;
    constexpr int N = 11;
    long long f[2][1 << N], *f0, *f1;
    int n, m;
    
    int main() {
      while (cin >> n >> m && n) {
        f0 = f[0];
        f1 = f[1];
        fill(f1, f1 + (1 << m), 0);
        f1[0] = 1;
        for (int i = 0; i < n; ++i) {
          for (int j = 0; j < m; ++j) {
            swap(f0, f1);
            fill(f1, f1 + (1 << m), 0);
    #define u f0[s]
            for (int s = 0; s < 1 << m; ++s)
              if (u) {
                if (j != m - 1 && (!(s >> j & 3))) f1[s ^ 1 << j + 1] += u;  // place horizontally
                f1[s ^ 1 << j] += u;  // place vertically or do not place
              }
          }
        }
        cout << f1[0] << endl;
      }
    }
    ```

??? note "Exercise [「SRM 671. Div 1 900」BearDestroys](https://archive.topcoder.com/ProblemStatement/pm/14069)"
    Problem summary: given an $n\times m$ matrix, each cell has `E` or `S`.
    For a matrix there is a scoring scheme. Scan each cell in row-major order; if this cell was already occupied by a domino before, then skip.
    Otherwise try to place a domino. If the direction of placing the domino is outside the matrix or occupied by another domino, then the placement fails, and switch to the other scheme or skip.
    If it is `E`, prefer to place a $1\times 2$ domino;
    if it is `S`, prefer to place a $2\times 1$ domino.
    The score of a matrix is the number of dominoes finally placed.
    Ask the sum of the scores over all $2^{nm}$ matrices.

### Terminology

Stage: the order in which dynamic programming executes; the result of a later stage is only related to the results of earlier stages (no aftereffect). Many DP problems can have multiple ways of dividing the stages. For example, in the knapsack problem, we can usually divide the stages either by items or by knapsack capacity (which the outer loop enumerates first). And in the domino problem, we can divide the stages by row, column, cell, diagonal, and other features.

Contour line: the boundary between decided states and undecided states.

![contour line](./images/contour_line.svg)

Plug: the existence of a plug in a certain direction of a cell means that this cell is connected to the adjacent cell in this direction.

![plug](./images/plug.svg)

## The path model

### Multiple cycles

#### Example

???+ note "Example [「HDU 1693」Eat the Trees](https://acm.hdu.edu.cn/showproblem.php?pid=1693)"
    Problem summary: count the number of ways to cover an $N\times M$ board with several cycles, where some positions have obstacles.

Strictly speaking, the multiple-cycle problem does not belong to plug DP, because we only need to, as with the domino-tiling problem above, record whether plugs exist and then merge and generate plugs in pairs.

Note that for a board of width $m$, the width of the contour line is $m+1$, because it contains $m$ up-plugs and $1$ left-plug. Note that when a row's iteration is complete, the rightmost left-plug is usually an invalid state, and at the same time we need to add the first left-plug of the next row; this requires us to adjust the state of the current contour line, usually by left-shifting all states, an operation we call rolling, `roll()`.

??? note "Example code"
    ```cpp
    --8<-- "docs/dp/code/plug/plug_1.cpp"
    ```

#### Exercise

??? note "Exercise [「ZOJ 3466」The Hive II](https://pintia.cn/problem-sets/91827364500/exam/problems/type/7?problemSetProblemId=91827368730)"
    Problem summary: same as the previous problem, but the cells become hexagonal.

### One cycle

#### Example

???+ note "Example [「Andrew Stankevich Contest 16 - Problem F」Pipe Layout](https://codeforces.com/gym/100220)"
    Problem summary: count the number of ways to cover an $N\times M$ board with one cycle.

In the state representation above, each time we merge a group of connected plugs, an independent cycle is generated; therefore in this problem we also need to distinguish the connectivity between plugs (here it appears!). This requires us to additionally encode the state.

#### State encoding

The usual encoding schemes are the bracket representation and the minimum representation; here we focus on the more general-purpose minimum representation. We use an integer array of length $m+1$ to record the state of each plug on the contour line, where $0$ means there is no plug, and we agree that connected plugs are marked with the same number.

Then the following two encodings represent the same state:

-   `0 3 1 0 1 3`
-   `0 1 2 0 2 1`

We map all identical states to the lexicographically smallest representation; for example, `0 1 2 0 2 1` in the above example is a minimum representation.

We use the `b[]` array to denote the state of the plugs on the contour line. `bb[]` denotes the smallest number each number is mapped to in the process of the minimum-representation encoding. Note that $0$ means the plug does not exist and cannot be mapped to another value.

??? note "Implementation"
    ```cpp
    int b[M + 1], bb[M + 1];
    
    int encode() {
      int s = 0;
      memset(bb, -1, sizeof(bb));
      int bn = 1;
      bb[0] = 0;
      for (int i = m; i >= 0; --i) {
    #define bi bb[b[i]]
        if (!~bi) bi = bn++;
        s <<= offset;
        s |= bi;
      }
      return s;
    }
    
    void decode(int s) {
      REP(i, m + 1) {
        b[i] = s & mask;
        s >>= offset;
      }
    }
    ```

We note that plugs always appear in pairs and disappear in pairs. Therefore a state like `0 1 2 0 1 2` is invalid. Valid states form a bracket sequence; in practice valid states may be very sparse.

#### Hand-written hash

In some [bitmask DP](./state.md) problems, the valid states may be sparse (such as this problem); to optimize time and space complexity, we can use a hash table to store the valid DP states. For C++ competitors, we can use [std::unordered\_map](http://www.cplusplus.com/reference/unordered_map/unordered_map/), or of course write it by hand directly, which lets us flexibly encapsulate the state-transition function within it as well.

???+ note "Implementation"
    ```cpp
    constexpr int MaxSZ = 16796, Prime = 9973;
    
    struct hashTable {
      int head[Prime], next[MaxSZ], sz;
      int state[MaxSZ];
      long long key[MaxSZ];
    
      void clear() {
        sz = 0;
        memset(head, -1, sizeof(head));
      }
    
      void push(int s) {
        int x = s % Prime;
        for (int i = head[x]; ~i; i = next[i]) {
          if (state[i] == s) {
            key[i] += d;
            return;
          }
        }
        state[sz] = s, key[sz] = d;
        next[sz] = head[x];
        head[x] = sz++;
      }
    
      void roll() { REP(i, sz) state[i] <<= offset; }
    } H[2], *H0, *H1;
    ```

In the code above:

-   `MaxSZ` denotes the upper bound of valid states, which can be estimated or precomputed to a relatively precise value.
-   `Prime` is a large prime smaller than `MaxSZ`.
-   `head[]` are the pointers to the head nodes of the lists.
-   `next[]` are the pointers to subsequent states.
-   `state[]` are the states of the nodes.
-   `key[]` are the keys of the nodes, which in this problem is the number of ways.
-   `clear()` is the initialization function; similar to a hand-written adjacency list, we only need to initialize the pointers to the head nodes.
-   `push()` is the state-transition function, where `d` is a global variable (out of laziness) denoting the increment brought by each state transition. If found, `+=`; otherwise create a new node with state `s` and key `d`.
-   `roll()`: after iterating a whole row, roll the contour line.

For the complexity analysis of hash tables, and the difference between open and closed hashing, see the relevant chapters on hash tables in [*Introduction to Algorithms*](../contest/resources.md#books).

#### State transition

???+ note "Implementation"
    ```cpp
    REP(ii, H0->sz) {
      decode(H0->state[ii]);                  // take out the state and decode it
      d = H0->key[ii];                        // get the increment delta
      int lt = b[j], up = b[j + 1];           // left plug, up plug
      bool dn = i != n - 1, rt = j != m - 1;  // down plug, right plug
      if (lt && up) {                         // if both the left and up have plugs
        if (lt == up) {                       // from the same connected component
          if (i == n - 1 &&
              j == m - 1) {  // only at the last cell can we merge and close the cycle.
            push(j, 0, 0);
          }
        } else {  // otherwise, we must merge these two connected components, because this problem requires cycle cover
          REP(i, m + 1) if (b[i] == lt) b[i] = up;
          push(j, 0, 0);
        }
      } else if (lt || up) {  // if one of the left, up has a plug
        int t = lt | up;      // get this plug
        if (dn) {             // if we can extend downward
          push(j, t, 0);
        }
        if (rt) {  // if we can extend rightward
          push(j, 0, t);
        }
      } else {           // if neither the left nor up has a plug
        if (dn && rt) {  // generate a new pair of plugs
          push(j, m, m);
        }
      }
    }
    ```

??? note "Example code"
    ```cpp
    --8<-- "docs/dp/code/plug/plug_2.cpp"
    ```

#### Exercises

??? note "Exercise [「Ural 1519」Formula 1](https://acm.timus.ru/problem.aspx?space=1&num=1519)"
    Problem summary: count the number of ways to cover an $N\times M$ board with one cycle, where some positions have obstacles.

??? note "Exercise [「USACO 5.4.4」Betsy's Tours](https://hydro.ac/d/USACO/p/USACO544)"
    Problem summary: an $N\times N$ square matrix ($N\le 7$); count the total number of paths from the top-left corner to the bottom-left corner passing through every cell. Although it is one path, because the start and end are fixed, it can be turned into a one-cycle problem.

??? note "Exercise [「POJ 1739」Tony's Tour](http://poj.org/problem?id=1739)"
    Problem summary: an $N\times M$ board; count the total number of paths from the bottom-left corner to the bottom-right corner passing through every cell, where some positions have obstacles.

??? note "Exercise [「USACO 6.1.1」Postal Vans](https://vjudge.net/problem/UVALive-2738)"
    Problem summary: count the number of ways to cover a $4\times N$ board with one directed cycle; big-number arithmetic is needed.

??? note "Exercise [「HNOI 2007」Magic Amusement Park](https://www.luogu.com.cn/problem/P3190)"
    Problem summary: given an $n\times m$ grid graph where each cell has a weight, find any one cycle maximizing the sum of the weights passed through.

??? note "Exercise [「ProjectEuler 393」Migrating ants](https://projecteuler.net/problem=393)"
    Problem summary: cover an $n\times n$ square matrix with several cycles; a scheme with $m$ cycles contributes $2^m$ to the answer; find the sum of the contributions of all schemes.

### One path

#### Example

???+ note "Example [「ZOJ 3213」Beautiful Meadow](https://pintia.cn/problem-sets/91827364500/exam/problems/type/7?page=22&problemSetProblemId=91827367895)"
    Problem summary: an $N\times M$ square matrix ($N,M\le 8$) where each cell has a weight; find a path maximizing the sum of the weights of the cells the path covers.

This is a standard one-path problem. In a one-path problem, the encoded state will also have unpaired independent plugs. In the state-transition function, we need to additionally discuss the cases of generation, merging, and disappearance of independent plugs. The generation and disappearance of an independent plug correspond to an end of the path, so this kind of event will not happen more than twice (one generation and one disappearance, or two generations and one merge); otherwise the final result will necessarily have multiple connected components.

We need to additionally record the total number of times this kind of event happens in the state. We can encode this information into the state (note that this kind of extra information does not need to roll along when adjusting the contour line), or of course add a dimension outside the `hashTable` array. In the following example program we choose the latter.

#### State transition

???+ note "Implementation"
    ```cpp
    REP(i, n) {
      REP(j, m) {
        checkMax(ans, A[i][j]);  // need to handle the single-cell case separately
        if (!A[i][j]) continue;  // if there is an obstacle, skip; note the state array does not need to roll here
        swap(H0, H1);
        REP(c, 3)
        H1[c].clear();  // c denotes the total number of generation and disappearance events, at most 2
        REP(c, 3) REP(ii, H0[c].sz) {
          decode(H0[c].state[ii]);
          d = H0[c].key[ii] + A[i][j];
          int lt = b[j], up = b[j + 1];
          bool dn = A[i + 1][j], rt = A[i][j + 1];
          if (lt && up) {
            if (lt == up) {  // in a one-path problem, we cannot merge identical plugs.
              // Cannot deploy here...
            } else {  // the two possibly participating in the merge may include an independent plug, but the same code snippet can handle it
              REP(i, m + 1) if (b[i] == lt) b[i] = up;
              push(c, j, 0, 0);
            }
          } else if (lt || up) {
            int t = lt | up;
            if (dn) {
              push(c, j, t, 0);
            }
            if (rt) {
              push(c, j, 0, t);
            }
            // the case of a plug disappearing: if it is an independent plug it means disappearance, if it is a paired plug it amounts to generating an independent plug,
            // whichever kind of event, we need to do c + 1.
            if (c < 2) {
              push(c + 1, j, 0, 0);
            }
          } else {
            d -= A[i][j];
            H1[c].push(H0[c].state[ii]);
            d += A[i][j];    // skip plug generation; this problem does not require full coverage
            if (dn && rt) {  // generate a pair of plugs
              push(c, j, m, m);
            }
            if (c < 2) {  // generate an independent plug
              if (dn) {
                push(c + 1, j, m, 0);
              }
              if (rt) {
                push(c + 1, j, 0, m);
              }
            }
          }
        }
      }
      REP(c, 3) H1[c].roll();  // a row ends, adjust the contour line
    }
    ```

??? note "Example code"
    ```cpp
    --8<-- "docs/dp/code/plug/plug_3.cpp"
    ```

#### Exercises

??? note "Exercise [「BZOJ 2310」ParkII](https://hydro.ac/p/bzoj-P2310)"
    Problem summary: an $m\times n$ board where each cell has a weight; find a path cover maximizing the sum of the weights of the cells the path passes through.

??? note "Exercise [「NOI 2010 Day2」Travel Route](https://www.luogu.com.cn/problem/P1933)"
    Problem summary: an $n\times m$ board where each cell has a 0/1 weight T\[x]\[y]; find a path cover satisfying:
    
    -   the $i$-th visited cell (x, y) satisfies T\[x]\[y]= L\[i]
    -   one end of the path is on the boundary of the board
    
    Find the number of feasible schemes.

## The coloring model

Besides the path model, there is another common model that requires us to color the board, where adjacent same-color nodes are regarded as connected. In path-type problems, during the state transition we enumerate the direction of the current path, while in coloring-type problems we enumerate what color the current node is colored. In the coloring model, there may be more than two nodes in the same connectivity in a state. But overall it is still much the same. Let us look at a classic example.

### Example: "UVa 10572" Black & White

???+ note "Example [「UVa 10572」Black & White](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=1513)"
    Problem summary: in an $N\times M$ board, color the uncolored cells black or white, requiring that all black regions and all white regions are connected, and that the colors within any $2\times 2$ subrectangle are not all the same (for example, the situation in the figure below is invalid); count the number of valid schemes and construct one valid scheme.
    
    ![black\_and\_white1](./images/black_and_white1.svg)

### State encoding

Let us first consider the state encoding. Ignoring connectivity, this is [SGU 197. Nice Patterns Strike Back](https://codeforces.com/problemsets/acmsguru/problem/99999/197), which is not hard to solve directly with [bitmask DP](./state.md). Now we need to reflect both color and connectivity information in the state. Examine the state of each position on the contour line: every `Offset` bits of the binary describe one position on the contour line; because there are only two colors, black and white, we use the parity of the lowest bit to indicate the color and the rest to indicate connectivity.

Consider the nodes above the first row and the nodes to the left of the first column; to avoid special cases, we can consider introducing a third color to distinguish them. Here we observe that the connectivity information of these boundary states is always 0, so there is no need to additionally encode the third color.

In the path problem, our contour line is composed of $m$ up-plugs and $1$ left-plug. In this problem, because we also need to judge whether the $2\times 2$ subrectangle with the current cell as its bottom-right corner is valid, we need to record the color of the top-left cell, so the length of the contour line is still $m+1$.

This encoding scheme still retains a lot of redundant information (connected regions always have the same color, and the top-left cell only needs color information, not connectivity), but because we already use a hash table and the minimum representation, the impact on time complexity is small; to reduce programming pressure, we do not refine it further.

In the maximum case (such as the first row alternating black and white), the connectivity information of every plug is different, so we need $4$ binary bits to record connectivity, plus the color information, so the `Offset` of this problem is $5$ bits.

???+ note "Implementation"
    ```cpp
    constexpr int Offset = 5, Mask = (1 << Offset) - 1;
    int c[N + 2];
    int b[N + 2], bb[N + 3];
    
    T_state encode() {
      T_state s = 0;
      memset(bb, -1, sizeof(bb));
      int bn = 1;
      bb[0] = 0;
      for (int i = m; i >= 0; --i) {
    #define bi bb[b[i]]
        if (!~bi) bi = bn++;
        s <<= Offset;
        s |= (bi << 1) | c[i];
      }
      return s;
    }
    
    void decode(T_state s) {
      REP(i, m + 1) {
        b[i] = s & Mask;
        c[i] = b[i] & 1;
        b[i] >>= 1;
        s >>= Offset;
      }
    }
    ```

### Hand-written hash

Because we need to construct any one scheme, here our hash table needs to add a field `pre[]` to record any one predecessor of each state in the previous stage.

???+ note "Implementation"
    ```cpp
    constexpr int Prime = 9979, MaxSZ = 1 << 20;
    
    template <class T_state, class T_key>
    struct hashTable {
      int head[Prime];
      int next[MaxSZ], sz;
      T_state state[MaxSZ];
      T_key key[MaxSZ];
      int pre[MaxSZ];
    
      void clear() {
        sz = 0;
        memset(head, -1, sizeof(head));
      }
    
      void push(T_state s, T_key d, T_state u) {
        int x = s % Prime;
        for (int i = head[x]; ~i; i = next[i]) {
          if (state[i] == s) {
            key[i] += d;
            return;
          }
        }
        state[sz] = s, key[sz] = d, pre[sz] = u;
        next[sz] = head[x], head[x] = sz++;
      }
    
      void roll() { REP(ii, sz) state[ii] <<= Offset; }
    };
    
    hashTable<T_state, T_key> _H, H[N][N], *H0, *H1;
    ```

### Constructing the scheme

With the above information, we can easily construct the scheme. First traverse the states in the current hash table; if the number of connected components does not exceed $2$, then count it into the number of ways. If the number of ways is not $0$, we construct the scheme in reverse order using the `pre` array; note that at the end of each row, because we executed the `Roll()` operation, the color needs to take `c[j+1]`.

???+ note "Implementation"
    ```cpp
    void print() {
      T_key z = 0;
      int u;
      REP(i, H1->sz) {
        decode(H1->state[i]);
        if (*max_element(b + 1, b + m + 1) <= 2) {
          z += H1->key[i];
          u = i;
        }
      }
      cout << z << endl;
      if (z) {
        DWN(i, n, 0) {
          B[i][m] = 0;
          DWN(j, m, 0) {
            decode(H[i][j].state[u]);
            int cc = j == m - 1 ? c[j + 1] : c[j];
            B[i][j] = cc ? 'o' : '#';
            u = H[i][j].pre[u];
          }
        }
        REP(i, n) puts(B[i]);
      }
      puts("");
    }
    ```

### State transition

We denote:

-   `cc` the color of the cell currently being colored
-   `lf` the color of the left cell
-   `up` the color of the upper cell
-   `lu` the color of the top-left cell

We use $-1$ to indicate that the color does not exist. Next we discuss the state transition; there are three cases in total: merging, inheriting, and generating:

???+ note "State transition - code"
    ```cpp
    void trans(int i, int j, int u, int cc) {
      decode(H0->state[u]);
      int lf = j ? c[j - 1] : -1, lu = b[j] ? c[j] : -1,
          up = b[j + 1] ? c[j + 1] : -1;  // no color is also a kind of color!
      if (lf == cc && up == cc) {         // merge
        if (lu == cc) return;             // the case of an identical 2x2 subrectangle
        int lf_b = b[j - 1], up_b = b[j + 1];
        REP(i, m + 1) if (b[i] == up_b) { b[i] = lf_b; }
        b[j] = lf_b;
      } else if (lf == cc || up == cc) {  // inherit
        if (lf == cc)
          b[j] = b[j - 1];
        else
          b[j] = b[j + 1];
      } else {                                             // generate
        if (i == n - 1 && j == m - 1 && lu == cc) return;  // special case
        b[j] = m + 2;
      }
      c[j] = cc;
      if (!ok(i, j, cc)) return;  // judge whether generating a closed connected component would make it invalid
      H1->push(encode(), H0->key[u], u);
    }
    ```

For the last case, note that if a closed connected region has already been generated, then we cannot color with its color again, otherwise this color would have two connected components. It seems we need to additionally record this kind of event; we can refer to the approach in [「ZOJ 3213」Beautiful Meadow](#example_2) and add a dimension to record this event. However, using the special nature of this problem, we can also handle it with a special case.

???+ note "Special case - code"
    ```cpp
    bool ok(int i, int j, int cc) {
      if (cc == c[j + 1]) return true;
      int up = b[j + 1];
      if (!up) return true;
      int c1 = 0, c2 = 0;
      REP(i, m + 1) if (i != j + 1) {
        if (b[i] == b[j + 1]) {  // same connectivity means the color must be the same
          assert(c[i] == c[j + 1]);
        }
        if (c[i] == c[j + 1] && b[i] == b[j + 1]) ++c1;
        if (c[i] == c[j + 1]) ++c2;
      }
      if (!c1) {               // if a new closed connected component would be generated
        if (c2) return false;  // if there is still the same color on the contour line
        if (i < n - 1 || j < m - 2) return false;
      }
      return true;
    }
    ```

Let us further discuss the case of a connected component disappearing. Each time after we color a cell, if no other cell is connected to the cell above it, then a closed connected component is formed. This event can only happen at the last two columns of the last row; otherwise, so as not to create a $2\times 2$ same-color connected component later, this color must appear again, except for the following case:

    2 2
    o#
    #o

We handle this case specially, so that in this problem we can be lazy and not record whether a closed connected component has already been generated before.

??? note "Example code"
    ```cpp
    --8<-- "docs/dp/code/plug/plug_4.cpp"
    ```

### Exercises

??? note "Exercise [「Topcoder SRM 312. Div1 Hard」CheapestIsland](https://archive.topcoder.com/ProblemStatement/pm/6482)"
    Problem summary: given a board graph where each cell has a weight, find the connected component with the minimum sum of weights.

??? note "Exercise [「JLOI 2009」Mysterious Creature](https://www.luogu.com.cn/problem/P3886)"
    Problem summary: given a board graph where each cell has a weight, find the connected component with the maximum sum of weights.

??? note "Exercise [「AtCoder Beginner Contest 211. Problem E」Red Polyomino](https://atcoder.jp/contests/abc211/tasks/abc211_e)"
    Problem summary: given an $N\times N$ board graph where each cell is initially black or white, you can pick exactly $K$ of the white cells and color them red; ask how many colorings make the red cells form a single connected component.

## The graph-theory model

???+ note "Example [「NOI 2007 Day2」Counting Spanning Trees](https://www.luogu.com.cn/problem/P2109)"
    Problem summary: counting the spanning trees of a special class of graph, where each node has edges exactly to its previous $k$ nodes.

???+ note "Example [「2015 ACM-ICPC Asia Shenyang Regional Contest - Problem E」Efficient Tree](https://acm.hdu.edu.cn/showproblem.php?pid=5513)"
    Problem summary: given an $N\times M$ grid graph and the edge weights between adjacent 4-connected cells.
    For a spanning tree, the score of each node is 1+\[there is an edge going up]+\[there is an edge going left].
    The score of the spanning tree is the product of the scores of all nodes.
    
    You need to find: the sum of the edge weights of the minimum spanning tree, and the sum of the scores of all minimum spanning trees.
    ($n\le 800,m\le 7$)

## Practical section

### Example

???+ note "Example [「HDU 4113」Construct the Great Wall](https://acm.hdu.edu.cn/showproblem.php?pid=4113)"
    Problem summary: in an $N\times M$ board, construct a set of cycles that separate all the `x`s and `o`s.

There is a class of plug DP problems that require us to construct a set of walls on the board to separate certain elements on the board. We may as well call it the wall-building problem; this kind of problem can be viewed either as a coloring model or as a path model.

![greatwall](./images/greatwall.svg)

In this problem, if viewed as a coloring model, we not only need to additionally discuss the perimeter of the colored region, but also judge the invalid case of touching at a corner (figure 2). In addition, unlike [「UVa 10572」Black & White](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=1513), this problem requires the wall to be a simple polygon, so the following 回-shaped case is invalid in this problem.

    3 3
    ooo
    oxo
    ooo

Therefore we use the path model and turn it into [one cycle](#one-cycle) to handle.

We do DP along the intersection points of the board (so the length and width need to increase by $1$); each time we transition, we need to ensure all `x`s are outside the cycle and all `o`s are inside the cycle. So we also need to maintain whether the current position is inside the cycle. For this information we can add a dimension, or directly count the parity of the number of down-plugs appearing before this position on the contour line (ray-casting method).

??? note "Example code"
    ```cpp
    #include <cstring>
    #include <iostream>
    using namespace std;
    #define REP(i, n) for (int i = 0; i < n; ++i)
    
    template <class T>
    bool checkMin(T &a, const T b) {
      return b < a ? a = b, true : false;
    }
    
    constexpr int N = 10, M = N;
    constexpr int offset = 3, mask = (1 << offset) - 1;
    int n, m;
    int d;
    constexpr int INF = 0x3f3f3f3f;
    int b[M + 1], bb[M + 1];
    
    int encode() {
      int s = 0;
      memset(bb, -1, sizeof(bb));
      int bn = 1;
      bb[0] = 0;
      for (int i = m; i >= 0; --i) {
    #define bi bb[b[i]]
        if (!~bi) bi = bn++;
        s <<= offset;
        s |= bi;
      }
      return s;
    }
    
    void decode(int s) {
      REP(i, m + 1) {
        b[i] = s & mask;
        s >>= offset;
      }
    }
    
    constexpr int MaxSZ = 16796, Prime = 9973;
    
    struct hashTable {
      int head[Prime], next[MaxSZ], sz;
      int state[MaxSZ];
      int key[MaxSZ];
    
      void clear() {
        sz = 0;
        memset(head, -1, sizeof(head));
      }
    
      void push(int s) {
        int x = s % Prime;
        for (int i = head[x]; ~i; i = next[i]) {
          if (state[i] == s) {
            checkMin(key[i], d);
            return;
          }
        }
        state[sz] = s, key[sz] = d;
        next[sz] = head[x];
        head[x] = sz++;
      }
    
      void roll() { REP(i, sz) state[i] <<= offset; }
    } H[2], *H0, *H1;
    
    char A[N + 1][M + 1];
    
    void push(int i, int j, int dn, int rt) {
      b[j] = dn;
      b[j + 1] = rt;
      if (A[i][j] != '.') {
        bool bad = A[i][j] == 'o';
        REP(jj, j + 1) if (b[jj]) bad ^= 1;
        if (bad) return;
      }
      H1->push(encode());
    }
    
    int solve() {
      cin >> n >> m;
      int ti, tj;
      REP(i, n) {
        scanf("%s", A[i]);
        REP(j, m) if (A[i][j] == 'o') ti = i, tj = j;
        A[i][m] = '.';
      }
      REP(j, m + 1) A[n][j] = '.';
      ++n, ++m, ++ti, ++tj;
      H0 = H, H1 = H + 1;
      H1->clear();
      d = 0;
      H1->push(0);
      int z = INF;
      REP(i, n) {
        REP(j, m) {
          swap(H0, H1);
          H1->clear();
          REP(ii, H0->sz) {
            decode(H0->state[ii]);
            d = H0->key[ii] + 1;
            int lt = b[j], up = b[j + 1];
            bool dn = i != n - 1, rt = j != m - 1;
            if (lt && up) {
              if (lt == up) {
                int cnt = 0;
                REP(i, m + 1) if (b[i])++ cnt;
                if (cnt == 2 && i == ti && j == tj) {
                  checkMin(z, d);
                }
              } else {
                REP(i, m + 1) if (b[i] == lt) b[i] = up;
                push(i, j, 0, 0);
              }
            } else if (lt || up) {
              int t = lt | up;
              if (dn) {
                push(i, j, t, 0);
              }
              if (rt) {
                push(i, j, 0, t);
              }
            } else {
              --d;
              push(i, j, 0, 0);
              ++d;
              if (dn && rt) {
                push(i, j, m, m);
              }
            }
          }
        }
        H1->roll();
      }
      if (z == INF) z = -1;
      return z;
    }
    
    int main() {
      int T;
      cin >> T;
      for (int Case = 1; Case <= T; ++Case) {
        printf("Case #%d: %d\n", Case, solve());
      }
    }
    ```

### Exercises

??? note "Exercise [「SCOI 2011」Floor](https://www.luogu.com.cn/problem/P3272)"
    Problem summary: an $r\times c$ board with obstacles at some positions; ask how many ways there are to tile all non-obstacle cells with L-shaped tiles.

??? note "Exercise [「HDU 4796」Winter's Coming](https://acm.hdu.edu.cn/showproblem.php?pid=4796)"
    Problem summary: in an $N\times M$ board, color the uncolored cells black, white, or gray, requiring that all black regions and white regions are connected, that the black region and white region are respectively connected to the top and bottom boundaries of the board, and that the black region and white region cannot be adjacent. Each cell has a corresponding cost; find a coloring scheme minimizing the cost of the gray region.
    
    ![4796](./images/4796.jpg)

??? note "Exercise [「ZOJ 2125」Rocket Mania](https://pintia.cn/problem-sets/91827364500/exam/problems/type/7?page=11&problemSetProblemId=91827365624)"
    Problem summary: on a $9\times6$ map, each cell has a kind of pipe (`-`, `T`, `L`, `+` type, or none), which can be rotated 0°, 90°, 180°, 270°; ask the maximum number of rows whose right boundary can be connected to the left boundary of row X through pipes.

??? note "Exercise [「ZOJ 2126」Rocket Mania Plus](https://pintia.cn/problem-sets/91827364500/exam/problems/type/7?page=11&problemSetProblemId=91827365625)"
    Problem summary: on a $9\times6$ map, each cell has a kind of pipe (`-`, `T`, `L`, `+` type, or none), which can be rotated 0°, 90°, 180°, 270°; ask the maximum number of rows whose right boundary can be connected to the left boundary through pipes.

??? note "Exercise [「World Finals 2009/2010 Harbin」Channel](https://qoj.ac/problem/13134)"
    Problem summary: on a grid map where `.` denotes empty space and `#` denotes rock, find the longest path satisfying:
    
    1.  the start is at the top-left corner and the end is at the bottom-right corner.
    2.  it cannot pass through rock.
    3.  the path itself cannot form a cycle in the sense of 8-connectivity. (i.e. it cannot even touch at corners)

??? note "Exercise [「HDU 3958」Tower Defence](https://acm.hdu.edu.cn/showproblem.php?pid=3958)"
    Problem summary: can be turned into solving for the longest non-touching path from $\mathit{S}$ to $\mathit{T}$, where corners are allowed to touch.

??? note "Exercise [「UVa 10531」Maze Statistics](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=1472)"
    Problem summary: there is an $N\times M$ graph where each cell independently becomes an obstacle with probability $\mathit{p}$. You need to walk from the top-left corner of the maze to the bottom-right corner. Find the probability that each cell is an obstacle in a **solvable maze (i.e. the start and end are 4-connected)**. ($N \le 5$, $M \le 6$)

??? note "Exercise [「Aizu 2452」Pipeline Plans](https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=2452)"
    Problem summary: there are 12 kinds of patterned tiles in total, with a given quantity of each kind. They are required to tile a rectangular floor viewable as an $R\times C$ grid graph, one tile per cell, such that the center of the top-left cell is connected to the center of the bottom-right cell through the lines on the tile patterns. ($2 \le R \times C \le 15$)
    
    ![plug2](./images/plug2.png)

??? note "Exercise [「SDOI 2014」Circuit Board](https://www.luogu.com.cn/problem/P3314)"
    Problem summary: an $N\times M$ circuit board where some positions are obstacles that wires cannot pass; given $K$ pairs of cells, each pair is required to be connected by a wire, and the wires must not intersect each other (one circuit line is allowed to enter the current cell from the top boundary and leave from the left boundary, while another circuit line can enter the cell from the bottom boundary and exit from the right boundary). Treating wires as undirected edges, find the shortest total wire length satisfying the requirement and the number of schemes.

??? note "Exercise [「SPOJ CAKE3」Delicious Cake](https://www.spoj.com/problems/CAKE3)"
    Problem summary: a cake viewable as an $N\times M$ grid is cut along the grid lines into several pieces; ask how many different ways of cutting there are. Two cuttings are the same if and only if every piece cut has the same shape and is at the same position. ($\min(N,M) \le 5, \max(N,M) \le 130$)

## Chapter notes

Plug DP problems are usually rather hard to encode and complex to discuss, and thus belong to a relatively [niche field](https://github.com/OI-wiki/libs/blob/master/topic/7-%E7%8E%8B%E5%A4%A9%E6%87%BF-%E8%AE%BA%E5%81%8F%E9%A2%98%E7%9A%84%E5%8D%B1%E5%AE%B3.ppt) in OI/ACM. The most classic material in this area is the 2008 National Training Team paper by [Danqi Chen](https://www.cs.princeton.edu/~danqic/)—[Dynamic Programming Problems Based on Connectivity Bitmasking](https://github.com/AngelKitty/review_the_national_post-graduate_entrance_examination/tree/master/books_and_notes/professional_courses/data_structures_and_algorithms/sources/%E5%9B%BD%E5%AE%B6%E9%9B%86%E8%AE%AD%E9%98%9F%E8%AE%BA%E6%96%87/%E5%9B%BD%E5%AE%B6%E9%9B%86%E8%AE%AD%E9%98%9F2008%E8%AE%BA%E6%96%87%E9%9B%86/%E9%99%88%E4%B8%B9%E7%90%A6%E3%80%8A%E5%9F%BA%E4%BA%8E%E8%BF%9E%E9%80%9A%E6%80%A7%E7%8A%B6%E6%80%81%E5%8E%8B%E7%BC%A9%E7%9A%84%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92%E9%97%AE%E9%A2%98%E3%80%8B). Second, notonlysuccess of HDU once wrote two consecutive, from-shallow-to-deep special topics on his blog in 2011, which are also rare good material, though you now need to dig them up in the Web Archive.

-   [notonlysuccess, 【Album】Plug DP](https://web.archive.org/web/20110815044829/http://www.notonlysuccess.com/?p=625)
-   [notonlysuccess, 【Full Version】Plug DP](https://web.archive.org/web/20111007185146/http://www.notonlysuccess.com/?p=931)

### Domino tiling

[「HDU 1400」Mondriaan's Dream](https://acm.hdu.edu.cn/showproblem.php?pid=1400) also appears in [*Classic Introduction to Algorithm Competitions - Training Guide*](../contest/resources.md#books), as an example in the "Dynamic Programming on Contour Lines" section. [Domino tiling](https://en.wikipedia.org/wiki/Domino_tiling) is a set of very classic mathematical problems; slightly modifying its data range gives subproblems of different difficulties requiring different algorithms to solve.

When restricted to $m=2$, domino tiling is equivalent to the Fibonacci sequence. [*Concrete Mathematics*](https://www.csie.ntu.edu.tw/~r97002/temp/Concrete%20Mathematics%202e.pdf) uses this problem to introduce the Fibonacci sequence and uses various methods to obtain its analytic solution.

When $m\le 10,n\le 10^9$, we can preprocess the transition equation into matrix form and use [matrix multiplication for speedup](http://www.matrix67.com/blog/archives/276).

![domino\_v2\_transform\_matrix](./images/domino_v2_transform_matrix.svg)

When $n,m\le 100$, we can use the [FKT Algorithm](https://en.wikipedia.org/wiki/FKT_algorithm) to compute the number of perfect matchings of the corresponding planar graph.

-   [「51nod 1031」Domino Tiling](https://www.51nod.com/Html/Challenge/Problem.html#problemId=1031)
-   [「51nod 1033」Domino Tiling V2](https://www.51nod.com/Html/Challenge/Problem.html#problemId=1033) | [「Vijos 1194」Domino](https://vijos.org/p/1194)
-   [「51nod 1034」Domino Tiling V3](https://www.51nod.com/Html/Challenge/Problem.html#problemId=1034) | [「Ural 1594」Aztec Treasure](https://acm.timus.ru/problem.aspx?space=1&num=1594)
-   [Wolfram MathWorld, Chebyshev Polynomial of the Second Kind](https://mathworld.wolfram.com/ChebyshevPolynomialoftheSecondKind.html)

### One path

"One path" is a special case of the [Hamiltonian path](https://en.wikipedia.org/wiki/Hamiltonian_path) problem in a [grid graph](https://mathworld.wolfram.com/GridGraph.html). The decision version of the Hamiltonian path is an important member of the [NP-complete](https://en.wikipedia.org/wiki/NP-completeness) family.
