## Definition

Memoized search is a search implementation that avoids repeatedly traversing the same state by recording the information of states already traversed.

Because memoized search ensures each state is visited only once, it is also a common way to implement dynamic programming.

## Introduction

???+ note "[\[NOIP2005\] Herb Gathering](https://www.luogu.com.cn/problem/P1048)"
    In a cave there are $M$ different herbs; gathering each takes some time $t_i$, and each also has its own value $v_i$. Given a length of time $T$, within this time you can gather some herbs. Maximize the total value of the gathered herbs.
    
    $1 \leq T \leq 10^3$, $1 \leq t_i,v_i,M \leq 100$

### The naive [DFS](../search/dfs.md) approach

It is easy to implement a naive search approach: during the search, record the three parameters of which item is currently to be selected, how much time remains, and how much value has been obtained; then enumerate whether the current item is selected and transition to the corresponding state.

???+ note "Implementation"
    === "C++"
        ```cpp
        int n, t;
        int tcost[103], mget[103];
        int ans = 0;
        
        void dfs(int pos, int tleft, int tans) {
          if (tleft < 0) return;
          if (pos == n + 1) {
            ans = max(ans, tans);
            return;
          }
          dfs(pos + 1, tleft, tans);
          dfs(pos + 1, tleft - tcost[pos], tans + mget[pos]);
        }
        
        int main() {
          cin >> t >> n;
          for (int i = 1; i <= n; i++) cin >> tcost[i] >> mget[i];
          dfs(1, t, 0);
          cout << ans << endl;
          return 0;
        }
        ```
    
    === "Python"
        ```python
        tcost = [0] * 103
        mget = [0] * 103
        ans = 0
        
        
        def dfs(pos, tleft, tans):
            global ans
            if tleft < 0:
                return
            if pos == n + 1:
                ans = max(ans, tans)
                return
            dfs(pos + 1, tleft, tans)
            dfs(pos + 1, tleft - tcost[pos], tans + mget[pos])
        
        
        t, n = map(lambda x: int(x), input().split())
        for i in range(1, n + 1):
            tcost[i], mget[i] = map(lambda x: int(x), input().split())
        dfs(1, t, 0)
        print(ans)
        ```

The time complexity of this approach is exponential and cannot pass this problem.

### Optimization

Why is the above approach inefficient? Because the same state is visited many times.

If, after querying a state, we store the state's information, then when we need to visit this state again we can directly use the previously computed information, thereby avoiding recomputation. This fully exploits the characteristic that many problems in dynamic programming have a large number of overlapping subproblems; it belongs to the "memoization" idea of trading space for time.

Concretely for this problem, on top of the naive DFS, we add an array `mem` to record the return value of each `dfs(pos,tleft)`. At first, set every value in `mem` to `-1` (meaning not solved yet). Each time we need to visit a state, if the value of the corresponding state in `mem` is `-1`, we recursively visit the state. Otherwise we directly use the value already stored in `mem`.

Through this handling, we ensure that each state is visited only once, so the time complexity of this algorithm is $O(TM)$.

???+ note "Implementation"
    === "C++"
        ```cpp
        int n, t;
        int tcost[103], mget[103];
        int mem[103][1003];
        
        int dfs(int pos, int tleft) {
          if (mem[pos][tleft] != -1)
            return mem[pos][tleft];  // for an already-visited state, directly return the previously recorded value
          if (pos == n + 1) return mem[pos][tleft] = 0;
          int dfs1, dfs2 = -INF;
          dfs1 = dfs(pos + 1, tleft);
          if (tleft >= tcost[pos])
            dfs2 = dfs(pos + 1, tleft - tcost[pos]) + mget[pos];  // state transition
          return mem[pos][tleft] = max(dfs1, dfs2);  // finally store the value of the current state
        }
        
        int main() {
          memset(mem, -1, sizeof(mem));
          cin >> t >> n;
          for (int i = 1; i <= n; i++) cin >> tcost[i] >> mget[i];
          cout << dfs(1, t) << endl;
          return 0;
        }
        ```
    
    === "Python"
        ```python
        tcost = [0] * 103
        mget = [0] * 103
        mem = [[-1 for i in range(1003)] for j in range(103)]
        
        
        def dfs(pos, tleft):
            if mem[pos][tleft] != -1:
                return mem[pos][tleft]
            if pos == n + 1:
                mem[pos][tleft] = 0
                return mem[pos][tleft]
            dfs1 = dfs2 = -INF
            dfs1 = dfs(pos + 1, tleft)
            if tleft >= tcost[pos]:
                dfs2 = dfs(pos + 1, tleft - tcost[pos]) + mget[pos]
            mem[pos][tleft] = max(dfs1, dfs2)
            return mem[pos][tleft]
        
        
        t, n = map(lambda x: int(x), input().split())
        for i in range(1, n + 1):
            tcost[i], mget[i] = map(lambda x: int(x), input().split())
        print(dfs(1, t))
        ```

## Connection and difference with recurrence

When solving dynamic-programming problems, the code for memoized search and recurrence is highly similar in form. This is because they use the same state representation and similar state transitions. For this very reason, generally the time complexity of the two implementations is the same.

Below is the recurrence-implementation code (to make comparison convenient, no rolling-array optimization is added); by comparing, you can see the similarity in form between the two.

```cpp
int n, t, w[105], v[105], f[105][1005];

int main() {
  cin >> n >> t;
  for (int i = 1; i <= n; i++) cin >> w[i] >> v[i];
  for (int i = 1; i <= n; i++)
    for (int j = 0; j <= t; j++) {
      f[i][j] = f[i - 1][j];
      if (j >= w[i])
        f[i][j] = max(f[i][j], f[i - 1][j - w[i]] + v[i]);  // state-transition equation
    }
  cout << f[n][t];
  return 0;
}
```

When solving dynamic-programming problems, both memoized search and recurrence ensure that the same state is solved at most once. The ways they achieve this are slightly different: recurrence avoids repeated visits by setting an explicit visiting order, while memoized search, though it does not explicitly specify a visiting order, achieves the same goal by marking states that have been visited.

Compared with recurrence, memoized search, because it does not need to explicitly specify a visiting order, is sometimes lower in implementation difficulty than recurrence, and can handle boundary cases relatively conveniently—this is a major advantage of memoized search. But at the same time, memoized search is hard to optimize with techniques such as rolling arrays, and because of the recursion, its running efficiency is lower than recurrence. Therefore you should choose the more suitable implementation depending on the problem.

## How to write memoized search

### Method one

1.  Write out the DP state and equation of this problem
2.  Write the dfs function based on them
3.  Add the memoization array

Example:

$dp_{i} = \max\{dp_{j}+1\}\quad (1 \leq j < i \land a_{j}<a_{i})$ (longest increasing subsequence)

turns into

=== "C++"
    ```cpp
    int dfs(int i) {
      if (mem[i] != -1) return mem[i];
      int ret = 1;
      for (int j = 1; j < i; j++)
        if (a[j] < a[i]) ret = max(ret, dfs(j) + 1);
      return mem[i] = ret;
    }
    
    int main() {
      memset(mem, -1, sizeof(mem));
      // reading part omitted
      int ret = 0;
      for (int j = 1; j <= n; j++) {
        ret = max(ret, dfs(j));
      }
      cout << ret << endl;
    }
    ```

=== "Python"
    ```python
    def dfs(i):
        if mem[i] != -1:
            return mem[i]
        ret = 1
        for j in range(1, i):
            if a[j] < a[i]:
                ret = max(ret, dfs(j) + 1)
        mem[i] = ret
        return mem[i]
    ```

### Method two

1.  Write the brute-force search program of this problem (preferably [dfs](../search/dfs.md))
2.  Change this dfs into a dfs that "needs no external variables"
3.  Add the memoization array

Example: the "Herb Gathering" example in this article.
