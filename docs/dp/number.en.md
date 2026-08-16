This page briefly introduces digit DP.

## Introduction

"Digits" means splitting a number apart digit by digit into ones, tens, hundreds, thousands, and so on, focusing on the digit at each position. If we split a decimal number, then each digit is 0–9; other bases are analogous to decimal.

Digit DP: used to solve a specific class of problems. This kind of problem is relatively easy to recognize; it generally has these characteristics:

1.  It requires counting the number of numbers satisfying a certain condition (i.e. the ultimate goal is counting);

2.  These conditions, after transformation, can be understood and judged using the idea of "digits";

3.  The input provides a numeric interval (sometimes only an upper bound) as the counting constraint;

4.  The upper bound is very large (e.g. $10^{18}$), and brute-force enumeration and verification would time out.

The basic principle of digit DP:

Consider the way humans count; the most naive counting is to start from small and add one in turn. But we find that for numbers with many digits, this process has many repeated parts. For example, the processes of counting from 7000 to 7999, from 8000 to 8999, and from 9000 to 9999 are very similar: they all go from 000 to 999 in the last three digits, and the only difference is the thousands digit; so we can merge these processes and store the counting answers produced during these processes in a common array. This array sets its states according to the specific requirements of the problem, and performs state transitions via recurrence or DP.

Digit DP usually uses conventional counting-problem techniques, such as splitting the answer within an interval into a subtraction of two parts (i.e. $\mathit{ans}_{[l, r]} = \mathit{ans}_{[0, r]}-\mathit{ans}_{[0, l - 1]}$).

Then, with the common answer array, the next step is to count the answer. Counting the answer can use either memoized search or loop-iteration recurrence. To count all answers not exceeding the upper bound without repetition or omission, we enumerate each digit from high to low, then consider which digits each position can be filled with, and finally use the common answer array to count the answer.

Next let's look at a few specific problems.

## Example 1

???+ note "Example 1 [Luogu P2602 Digit Counting](https://www.luogu.com.cn/problem/P2602)"
    Problem summary: given two positive integers $a,b$, find how many times each digit occurs among all integers in $[a,b]$.

### Method one

#### Explanation

We find that for numbers with a full $\mathit{i}$ digits, the number of occurrences of all digits is the same, so let the array $\mathit{dp}_i$ be the number of occurrences of each digit among numbers with a full $i$ digits, temporarily not handling leading zeros. Then $\mathit{dp}_i=10 \times \mathit{dp}_{i−1}+10^{i−1}$; of these two parts, the former comes from the contribution of the first $i-1$ digits, and the latter comes from the contribution of the $i$-th digit.

With the $\mathit{dp}$ array, let's consider how to count the answer. Split the upper bound digit by digit, enumerating from high to low; when not sticking to the upper bound, the following digits can take any value. When sticking to the upper bound, the following digits can only take $0$ to the upper bound, and we compute the contributions of the two parts separately. Finally, consider leading zeros: when the $i$-th digit is a leading $0$, digits $1$ to $\mathit{i-1}$ are also all $0$, meaning we over-counted the answer of filling $i-1$ digits full, which needs to be subtracted off.

#### Implementation

???+ note "Reference code"
    ```cpp
    #include <cstdio>
    using namespace std;
    constexpr int N = 15;
    using ll = long long;
    ll l, r, dp[N], mi[N];
    ll ans1[N], ans2[N];
    int a[N];
    
    void solve(ll n, ll *ans) {
      ll tmp = n;
      int len = 0;
      while (n) a[++len] = n % 10, n /= 10;
      for (int i = len; i >= 1; --i) {
        for (int j = 0; j < 10; j++) ans[j] += dp[i - 1] * a[i];
        for (int j = 0; j < a[i]; j++) ans[j] += mi[i - 1];
        tmp -= mi[i - 1] * a[i], ans[a[i]] += tmp + 1;
        ans[0] -= mi[i - 1];
      }
    }
    
    int main() {
      scanf("%lld%lld", &l, &r);
      mi[0] = 1ll;
      for (int i = 1; i <= 13; ++i) {
        dp[i] = dp[i - 1] * 10 + mi[i - 1];
        mi[i] = 10ll * mi[i - 1];
      }
      solve(r, ans1), solve(l - 1, ans2);
      for (int i = 0; i < 10; ++i) printf("%lld ", ans1[i] - ans2[i]);
      return 0;
    }
    ```

### Method two

#### Explanation

This problem can also use memoized search. $\mathit{dp}_i$ denotes the answer for $i$ digits when not sticking to the upper bound and with no leading zeros.

See the code comments for details.

#### Process

???+ note "Reference code"
    ```cpp
    #include <cstdio>
    #include <cstring>
    #include <iostream>
    using namespace std;
    using ll = long long;
    constexpr int N = 50005;
    ll a, b;
    ll f[15], ksm[15], p[15], now[15];
    
    ll dfs(int u, int x, bool f0,
           bool lim) {  // u is the number of digits, f0 whether there are leading zeros, lim whether all stick to the upper bound
      if (!u) {
        if (f0) f0 = false;
        return 0;
      }
      if (!lim && !f0 && (~f[u])) return f[u];
      ll cnt = 0;
      int lst = lim ? p[u] : 9;
      for (int i = 0; i <= lst; i++) {  // enumerate the digit to fill in this position
        if (f0 && i == 0)
          cnt += dfs(u - 1, x, 1, lim && i == lst);  // handle leading zeros
        else if (i == x && lim && i == lst)
          cnt += now[u - 1] + 1 +
                 dfs(u - 1, x, 0,
                     lim && i == lst);  // here the enumerated leading digits all stick to the given upper bound.
        else if (i == x)
          cnt += ksm[u - 1] + dfs(u - 1, x, 0, lim && i == lst);
        else
          cnt += dfs(u - 1, x, 0, lim && i == lst);
      }
      if ((!lim) && (!f0)) f[u] = cnt;  // only memoize when not sticking to the upper bound and no leading zeros
      return cnt;
    }
    
    ll gans(ll d, int dig) {
      int len = 0;
      memset(f, -1, sizeof(f));
      while (d) {
        p[++len] = d % 10;
        d /= 10;
        now[len] = now[len - 1] + p[len] * ksm[len - 1];
      }
      return dfs(len, dig, 1, 1);
    }
    
    int main() {
      scanf("%lld%lld", &a, &b);
      ksm[0] = 1;
      for (int i = 1; i <= 12; i++) ksm[i] = ksm[i - 1] * 10ll;
      for (int i = 0; i < 9; i++) printf("%lld ", gans(b, i) - gans(a - 1, i));
      printf("%lld\n", gans(b, 9) - gans(a - 1, 9));
      return 0;
    }
    ```

## Example 2

???+ note "Example 2 [HDU 2089 No 62](https://acm.hdu.edu.cn/showproblem.php?pid=2089)"
    Problem summary: count how many numbers in an interval have digits that contain neither a 4 nor a consecutive 62.

### Explanation

For the "no 4" condition, we just check during enumeration; not enumerating 4 guarantees the state is valid, so this constraint has no need for memoization. As for 62, it involves two digits, and the counts differ between the two cases where the previous digit is 6 or is not 6, so we need a state to record the different scheme counts. $\mathit{dp}_{\mathit{pos},\mathit{sta}}$ denotes the state at the current $\mathit{pos}$-th digit and whether the previous digit is 6; here $\mathit{sta}$ only needs to take the two states 0 and 1, and the cases where it is not 6 can be regarded as the same kind without affecting the count.

### Implementation

???+ note "Reference code"
    ```cpp
    #include <cstdio>
    #include <cstring>
    #include <iostream>
    using namespace std;
    int x, y, dp[15][3], p[50];
    
    void pre() {
      memset(dp, 0, sizeof(dp));
      dp[0][0] = 1;
      for (int i = 1; i <= 10; i++) {
        dp[i][0] = dp[i - 1][0] * 9 - dp[i - 1][1];
        dp[i][1] = dp[i - 1][0];
        dp[i][2] = dp[i - 1][2] * 10 + dp[i - 1][1] + dp[i - 1][0];
      }
    }
    
    int cal(int x) {
      int cnt = 0, ans = 0, tmp = x;
      while (x) {
        p[++cnt] = x % 10;
        x /= 10;
      }
      bool flag = false;
      p[cnt + 1] = 0;
      for (int i = cnt; i; i--) {  // enumerate the digits from high to low
        ans += p[i] * dp[i - 1][2];
        if (flag)
          ans += p[i] * dp[i - 1][0];
        else {
          if (p[i] > 4) ans += dp[i - 1][0];
          if (p[i] > 6) ans += dp[i - 1][1];
          if (p[i] > 2 && p[i + 1] == 6) ans += dp[i][1];
          if (p[i] == 4 || (p[i] == 2 && p[i + 1] == 6)) flag = true;
        }
      }
      return tmp - ans;
    }
    
    int main() {
      pre();
      while (~scanf("%d%d", &x, &y)) {
        if (!x && !y) break;
        if (x > y) swap(x, y);
        printf("%d\n", cal(y + 1) - cal(x));
      }
      return 0;
    }
    ```

## Example 3

???+ note "Example 3 [SCOI2009 Windy Numbers](https://loj.ac/problem/10165)"
    Problem summary: given an interval $[l,r]$, find the number of numbers in it satisfying the condition **no leading $0$ and any two adjacent digits differ by at least $2$**.

### Explanation

First we transform the problem into a simpler form. Let $\mathit{ans}_i$ denote the number of numbers satisfying the condition in the interval $[1,i]$; then the desired answer is $\mathit{ans}_r-\mathit{ans}_{l-1}$.

For a number smaller than $n$, from high to low there must be some digit where the value at this digit is smaller than the corresponding value at this digit of $n$, while all previous digits equal the digits of $n$.

With this property, we can define $f(i,st,op)$ as the number of numbers when the digit currently to be considered is the $i$-th from high to low, the state of the current prefix is $st$, and the magnitude relationship between the prefix and the number currently being solved is $op$ ($op=1$ means equal, $op=0$ means less than). In this problem, this prefix state is the value of the previous digit, because which digits the digit currently to be determined cannot take is only related to the previous digit. In other problems, this value could be: the digit sum of the prefix, the $\gcd$ of all digits of the prefix, the remainder of the prefix modulo some number, and there are also cases where two or more are combined.

Write the **state-transition equation**: $f(i,st,op)=\sum_{k=1}^{\mathit{maxx}} f(i+1,k,op=1~ \operatorname{and}~ k=\mathit{maxx} )\quad (|\mathit{st}-k|\ge 2)$

Here $k$ is the value of the next digit currently being enumerated, and $\mathit{maxx}$ is the highest value currently attainable. Because if $\mathit{op}=1$, then the value you take at this digit certainly cannot be greater than the value at this digit of the number being solved; otherwise there is no restriction.

We find that even though the prefix chooses different states, if the three parameters of $f$ are the same, the answer is the same. To prevent this answer from being computed multiple times, we can implement it using [memoized search](./memo.md).

### Implementation

???+ note "Reference code"
    ```cpp
    int dfs(int x, int st, int op)  // op=1 =; op=0 <
    {
      if (!x) return 1;
      if (!op && ~f[x][st]) return f[x][st];
      int maxx = op ? dim[x] : 9, ret = 0;
      for (int i = 0; i <= maxx; i++) {
        if (abs(st - i) < 2) continue;
        if (st == 11 && i == 0)
          ret += dfs(x - 1, 11, op & (i == maxx));
        else
          ret += dfs(x - 1, i, op & (i == maxx));
      }
      if (!op) f[x][st] = ret;
      return ret;
    }
    
    int solve(int x) {
      memset(f, -1, sizeof f);
      dim.clear();
      dim.push_back(-1);
      int t = x;
      while (x) {
        dim.push_back(x % 10);
        x /= 10;
      }
      return dfs(dim.size() - 1, 11, 1);
    }
    ```

## Example 4

???+ note "Example 4. [SPOJ MYQ10](https://www.spoj.com/problems/MYQ10/en/)"
    Problem summary: if you handwrite all integers in $[n,m]$, how many numbers look exactly the same as they look in a mirror? ($n,m<10^{44}, T<10^5$)

### Explanation

Note: since the mirroring considered here means only the mirror images of $0,1,8$ are themselves, the "exactly the same" here is not a palindrome in the traditional sense, but a palindrome containing only $0,1,8$.

First, in the digit DP process, clearly only $0,1,8$ can be selected.

Second, since the values exceed the range of long long, $[n,m]=[1,m]-[1,n-1]$ no longer applies (big-number comparison is rather tedious); instead we need to judge whether $n$ is valid, giving: $[n,m]=[1,m]-[1,n]+\mathrm{check}(n)$.

The mirroring is solved; how to judge palindromes?

We need a small array to record the previous values. When not past half the length, it suffices not to exceed the upper bound; when past half the length, we also need to judge whether it equals the digit "mirror-symmetric" to it.

Note additionally that the memoization part of this problem cannot use `memset`, otherwise it causes a timeout.

### Implementation

???+ note "Reference code"
    ```cpp
    int check(char cc[]) {  // special check for n
      int strc = strlen(cc);
      for (int i = 0; i < strc; ++i) {
        if (!(cc[i] == cc[strc - i - 1] &&
              (cc[i] == '1' || cc[i] == '8' || cc[i] == '0')))
          return 0ll;
      }
      return 1ll;
    }
    
    // now: current digit, eff: effective digits, fulc: whether all stick to the top, ful0: whether all 0
    int dfs(int now, int eff, bool ful0, bool fulc) {
      if (now == 0) return 1ll;
      if (!fulc && f[now][eff][ful0] != -1)  // memoization
        return f[now][eff][ful0];
    
      int res = 0, maxk = fulc ? dig[now] : 9;
      for (int i = 0; i <= maxk; ++i) {
        if (i != 0 && i != 1 && i != 8) continue;
        b[now] = i;
        if (ful0 && i == 0)  // all leading 0
          res += dfs(now - 1, eff - 1, 1, 0);
        else if (now > eff / 2)                                  // not past halfway
          res += dfs(now - 1, eff, 0, fulc && (dig[now] == i));  // past halfway
        else if (b[now] == b[eff - now + 1])
          res += dfs(now - 1, eff, 0, fulc && (dig[now] == i));
      }
      if (!fulc) f[now][eff][ful0] = res;
      return res;
    }
    
    char cc1[100], cc2[100];
    int strc, ansm, ansn;
    
    int get(char cc[]) {  // processing wrapper
      strc = strlen(cc);
      for (int i = 0; i < strc; ++i) dig[strc - i] = cc[i] - '0';
      return dfs(strc, strc, 1, 1);
    }
    
    scanf("%s%s", cc1, cc2);
    printf("%lld\n", get(cc2) - get(cc1) + check(cc1));
    ```

## Example 5

???+ note "Example 5. [P3311 Counting Numbers](https://www.luogu.com.cn/problem/P3311)"
    Problem statement: we call a positive integer $x$ a lucky number if and only if its decimal representation does not contain any element of the digit-string set $S$ as a substring. For example, when $S = \{22, 333, 0233\}$, $233233$ is a lucky number, while $23332333$, $2023320233$, $32233223$ are not. Given $n$ and $S$, count the number of lucky numbers not greater than $n$. The answer is taken modulo $10^9 + 7$.
    
    $1 \leq n<10^{1201}$, $1 \leq m \leq 100$, $1 \leq \sum_{i = 1}^m |s_i| \leq 1500$, $\min_{i = 1}^m |s_i| \geq 1$, where $|s_i|$ denotes the length of the string $s_i$. $n$ has no leading $0$, but $s_i$ may have leading $0$s.

### Explanation

Reading the statement, we find that if we regard numbers as strings, then this requires performing multi-pattern matching, which naturally makes us think of the Aho–Corasick automaton. In ordinary digit DP, we first enumerate the digits from high to low, then enumerate what each digit is filled with; in this problem, we naturally turn this into enumerating the number of digits already filled, then enumerating which node we currently stop at on the AC automaton, and then transitioning from the current node to its child node on the AC automaton.

Let $f(i,j,0/1)$ denote that we have currently filled $i$ digits from high to low (i.e. walked $i$ edges on the AC automaton), currently stop at the node labeled $j$, and whether we currently exactly stick to the upper bound.

As for the "does not contain" condition in the problem, just mark the ending node of each pattern string on the AC automaton, and skip these ending nodes whenever encountered during the DP.

The transition is easy to think of; see the main-function part of the code for details.

### Implementation

???+ note "Reference code"
    ```cpp
    #include <cstdio>
    #include <cstring>
    #include <queue>
    using namespace std;
    using ll = long long;
    constexpr int N = 1505;
    constexpr int mod = 1000000007;
    int n, m;
    char s[N], c[N];
    int ch[N][10], fail[N], ed[N], tot, len;
    
    void insert() {
      int now = 0;
      int L = strlen(s);
      for (int i = 0; i < L; ++i) {
        if (!ch[now][s[i] - '0']) ch[now][s[i] - '0'] = ++tot;
        now = ch[now][s[i] - '0'];
      }
      ed[now] = 1;
    }
    
    queue<int> q;
    
    void build() {
      for (int i = 0; i < 10; ++i)
        if (ch[0][i]) q.push(ch[0][i]);
      while (!q.empty()) {
        int u = q.front();
        q.pop();
        for (int i = 0; i < 10; ++i) {
          if (ch[u][i]) {
            fail[ch[u][i]] = ch[fail[u]][i], q.push(ch[u][i]),
            ed[ch[u][i]] |= ed[fail[ch[u][i]]];
          } else
            ch[u][i] = ch[fail[u]][i];
        }
      }
      ch[0][0] = 0;
    }
    
    ll f[N][N][2], ans;
    
    void add(ll &x, ll y) { x = (x + y) % mod; }
    
    int main() {
      scanf("%s", c);
      n = strlen(c);
      scanf("%d", &m);
      for (int i = 1; i <= m; ++i) scanf("%s", s), insert();
      build();
      f[0][0][1] = 1;
      for (int i = 0; i < n; ++i) {
        for (int j = 0; j <= tot; ++j) {
          if (ed[j]) continue;
          for (int k = 0; k < 10; ++k) {
            if (ed[ch[j][k]]) continue;
            add(f[i + 1][ch[j][k]][0], f[i][j][0]);
            if (k < c[i] - '0') add(f[i + 1][ch[j][k]][0], f[i][j][1]);
            if (k == c[i] - '0') add(f[i + 1][ch[j][k]][1], f[i][j][1]);
          }
        }
      }
      for (int j = 0; j <= tot; ++j) {
        if (ed[j]) continue;
        add(ans, f[n][j][0]);
        add(ans, f[n][j][1]);
      }
      printf("%lld\n", ans - 1);
      return 0;
    }
    ```

This problem can well help in understanding the principle of digit DP.

## Exercises

[Ahoi2009 self Same-Type Distribution](https://www.luogu.com.cn/problem/P4127)

[Luogu P3413 SAC#1 - Cute Numbers](https://www.luogu.com.cn/problem/P3413)

[HDU 6148 Valley Number](https://acm.hdu.edu.cn/showproblem.php?pid=6148)

[CF55D Beautiful numbers](http://codeforces.com/problemset/problem/55/D)

[CF628D Magic Numbers](http://codeforces.com/problemset/problem/628/D)
