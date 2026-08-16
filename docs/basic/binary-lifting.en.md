author: Ir1d, ShadowsEpic, Fomalhauthmj, siger-young, MingqiHuang, Xeonacid, hsfzLZH1, orzAtalod, NachtgeistW

This page briefly introduces binary lifting.

## Definition

Binary lifting, as the name suggests, means "growing by doubling". When performing a recurrence, if the state space is very large and an ordinary linear recurrence cannot meet the time and space complexity requirements, we can grow by doubling, computing only the values at positions that are integer powers of $k$ in the state space as representatives. When we need values at other positions, we use the property that "any integer can be expressed as a sum of several power-of-$k$ terms" to assemble the needed value from the previously computed representative values. So using binary lifting also requires that the state space of the problem being recurred is divisible with respect to powers of $k$. Usually $k$ is taken to be $2$. [^ref1]

This method is used in many algorithms, the most common of which are the RMQ problem and finding the [LCA (lowest common ancestor)](../graph/lca.md).

## Applications

### The RMQ problem

See: [RMQ topic](../topic/rmq.md)

RMQ stands for Range Maximum/Minimum Query. The method that uses the binary-lifting idea to solve the RMQ problem is the [sparse table (ST table)](../ds/sparse-table.md).

### Finding LCA with binary lifting on a tree

See: [Lowest common ancestor](../graph/lca.md)

## Example problems

### Problem 1

???+ note "Example"
    How can we weigh out every weight in $[0,31]$ using as few weights as possible? (Weights may be placed on only one side of the balance.)

??? note "Solution idea"
    The answer is to use the five weights 1 2 4 8 16, which can weigh out every weight in $[0,31]$. Likewise, to weigh out every weight in $[0,127]$, we can use the seven weights 1 2 4 8 16 32 64. By always choosing an integer power of 2 as the weight, we can measure any weight we need using very few weights.

    Why "very few"? Because to measure every weight in $[0,1023]$ we need only 10 weights, and to measure every weight in $[0,1048575]$ we need only 20. When the target weight doubles, the number of weights increases by only 1. This is called "logarithmic" growth, because the number of weights needed is proportional to the logarithm of the range of target weights.

### Problem 2

???+ note "Example"
    Given a cycle of length $n$ and a constant $k$, each step jumps from the $i$-th point to the $(i+k)\bmod n+1$-th point, for a total of $m$ jumps. Each point has a value, denoted $a_i$. Find the sum of the values of the starting points of the $m$ jumps, modulo $10^9+7$.

    Data range: $1\leq n\leq 10^6$, $1\leq m\leq 10^{18}$, $1\leq k\leq n$, $0\le a_i\le 10^9$.

??? note "Solution idea"
    Here we obviously cannot brute-force simulate $m$ jumps, because $m$ can be as large as $10^{18}$; brute-force simulation would not fit within the time limit.

    So we need some preprocessing to consolidate information in advance, so that we can produce the result more quickly at query time. Recording the result of every possible number of jumps would be unbearable in both time and space.

    So how should we preprocess? Look back at the first example. Any ideas?

    Back to this problem. We want to preprocess some information and then use it to assemble the answer as quickly as possible, while not preprocessing too much information. So we can preprocess information in units of integer powers of 2; this way we only need to handle a small amount of information during preprocessing, and we do not need to go to great lengths when assembling.

    For this problem, we preprocess the result of jumping 1, 2, 4, 8, etc. steps from each point (the resulting point and the sum of point values), and then to jump 13 steps we only need to jump 1+4+8 steps. That is, we first jump 1 step from the start, then jump 4 steps from the endpoint we reached, then jump another 8 steps, accumulating the preprocessed sums of point values along the way, so we know the sum of point values for 13 steps.

    For the $2^i$ steps starting from each point, record `go[i][x]` for the endpoint after point $x$ jumps $2^i$ steps, and `sum[i][x]` for the sum of point values obtained after point $x$ jumps $2^i$ steps. During preprocessing, use two nested loops; for the information about jumping $2^i$ steps, we can regard it as first jumping $2^{i-1}$ steps and then $2^{i-1}$ steps, since clearly $2^{i-1}+2^{i-1}=2^i$. That is, we have `sum[i][x] = sum[i-1][x]+sum[i-1][go[i-1][x]]` and `go[i][x] = go[i-1][go[i-1][x]]`.

    There are of course some implementation details to note. To ensure the counting has no omissions or duplicates, we generally preprocess "left-closed, right-open" sums of point values. That is, for jumping 1 step we record only that point's value; for jumping 2 steps we record only that point and its next point's values. This amounts to never counting the endpoint's value into `sum`. This way, during preprocessing, we only need to add the two parts' sums directly, without worrying that the endpoint of the first segment and the start of the second segment are double-counted.

    Although $m\leq 10^{18}$ in this problem seems daunting, in fact we only need to preprocess $i$ up to $65$ to solve it easily, which is much faster than brute-force enumeration. In technical terms, this approach has a [time complexity](./complexity.md) of $\Theta(n\log m)$ for preprocessing and $\Theta(\log m)$ per query.

??? note "Reference code"
    ```cpp
    #include <cstdio>
    using namespace std;
    
    constexpr int mod = 1000000007;
    
    int modadd(int a, int b) {
      if (a + b >= mod) return a + b - mod;  // subtraction instead of modulo, to speed up computation
      return a + b;
    }
    
    int vi[1000005];
    
    int go[75][1000005];  // make the array slightly larger to avoid overflow; put the smaller dimension first
    int sum[75][1000005];
    
    int main() {
      int n, k;
      scanf("%d%d", &n, &k);
      for (int i = 1; i <= n; ++i) {
        scanf("%d", vi + i);
      }
    
      for (int i = 1; i <= n; ++i) {
        go[0][i] = (i + k) % n + 1;
        sum[0][i] = vi[i];
      }
    
      int logn = 31 - __builtin_clz(n);  // a quick way to take a logarithm
      for (int i = 1; i <= logn; ++i) {
        for (int j = 1; j <= n; ++j) {
          go[i][j] = go[i - 1][go[i - 1][j]];
          sum[i][j] = modadd(sum[i - 1][j], sum[i - 1][go[i - 1][j]]);
        }
      }
    
      long long m;
      scanf("%lld", &m);
    
      int ans = 0;
      int curx = 1;
      for (int i = 0; m; ++i) {
        if (m & (1ll << i)) {  // see the material on bitwise operations; means whether bit i of m is 1
          ans = modadd(ans, sum[i][curx]);
          curx = go[i][curx];
          m ^= 1ll << i;  // clear bit i
        }
      }
    
      printf("%d\n", ans);
    }
    ```

[^ref1]: Quoted from Li Yudong, *Advanced Guide to Algorithm Competition*, section 0x06 "Binary Lifting".
