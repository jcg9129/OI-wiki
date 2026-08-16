author: hydingsy, Link-cute, Ir1d, greyqz, LuoshuiTianyi, odeinjul, xyf007, GoodCoder666, paigeman, shenshuaijie, oldoldtea

Prerequisite: [Introduction to the dynamic programming part](./index.md).

## Introduction

Before specifically explaining what "knapsack DP" is, let's look at the following example:

???+ note "["USACO07 DEC" Charm Bracelet](https://www.luogu.com.cn/problem/P2871)"
    Problem summary: there are $n$ items and a knapsack of capacity $W$; each item has two attributes, weight $w_{i}$ and value $v_{i}$. You are required to select some items to put into the knapsack so that the total value of the items in the knapsack is maximized and the total weight of the items in the knapsack does not exceed the knapsack's capacity.

In the example above, since each object has only two possible states (taken or not taken), corresponding to $0$ and $1$ in binary, this kind of problem is called the "0-1 knapsack problem".

## 0-1 knapsack

### Explanation

In the example, the known conditions are the weight $w_{i}$ and value $v_{i}$ of the $i$-th item, as well as the total capacity $W$ of the knapsack.

Let the DP state $f_{i,j}$ be the maximum total value a knapsack of capacity $j$ can achieve when only the first $i$ items can be placed.

Consider the transition. Suppose all states of the first $i-1$ items have already been processed; then for the $i$-th item, when it is not put into the knapsack, the knapsack's remaining capacity is unchanged and the total value of the items in the knapsack is unchanged, so the maximum value in this case is $f_{i-1,j}$; when it is put into the knapsack, the knapsack's remaining capacity decreases by $w_{i}$ and the total value of the items in the knapsack increases by $v_{i}$, so the maximum value in this case is $f_{i-1,j-w_{i}}+v_{i}$.

From this we can derive the state-transition equation:

$$
f_{i,j}=\max(f_{i-1,j},f_{i-1,j-w_{i}}+v_{i})
$$

If we directly use a two-dimensional array to record the states, MLE will occur. We can consider switching to a rolling-array form for optimization.

Since only $f_{i-1}$ affects $f_i$, we can remove the first dimension and directly use $f_{i}$ to denote the maximum value when the knapsack capacity is $i$ upon processing the current item, giving the following equation:

$$
f_j=\max \left(f_j,f_{j-w_i}+v_i\right)
$$

**Be sure to firmly remember and understand this transition equation, because the transition equations of most knapsack problems are derived on this basis.**

### Implementation

One more thing to note is that it is easy to write the following **wrong core code**:

=== "C++"
    ```cpp
    for (int i = 1; i <= n; i++)
      for (int l = 0; l <= W - w[i]; l++)
        f[l + w[i]] = max(f[l] + v[i], f[l + w[i]]);
    // simplified from f[i][l + w[i]] = max(max(f[i - 1][l + w[i]], f[i - 1][l] + v[i]),
    // f[i][l + w[i]]);
    ```

=== "Python"
    ```python
    for i in range(1, n + 1):
        for l in range(0, W - w[i] + 1):
            f[l + w[i]] = max(f[l] + v[i], f[l + w[i]])
    # simplified from f[i][l + w[i]] = max(max(f[i - 1][l + w[i]], f[i - 1][l] + v[i]),
    # f[i][l + w[i]])
    ```

Where is this code wrong? The enumeration order is wrong.

Examining the code carefully, we can find that for the item $i$ currently being processed and the current state $f_{i,j}$, when $j\geqslant w_{i}$, $f_{i,j}$ is affected by $f_{i,j-w_{i}}$. This is equivalent to item $i$ being able to be put into the knapsack multiple times, which does not match the problem. (In fact, this is exactly the solution to the complete knapsack problem.)

To prevent this from happening, we can change the enumeration order, enumerating from $W$ down to $w_{i}$; this way the above error does not occur, because $f_{i,j}$ is always updated before $f_{i,j-w_{i}}$.

Therefore the actual core code is

=== "C++"
    ```cpp
    for (int i = 1; i <= n; i++)
      for (int l = W; l >= w[i]; l--) f[l] = max(f[l], f[l - w[i]] + v[i]);
    ```

=== "Python"
    ```python
    for i in range(1, n + 1):
        for l in range(W, w[i] - 1, -1):
            f[l] = max(f[l], f[l - w[i]] + v[i])
    ```

??? note "Example code"
    ```cpp
    --8<-- "docs/dp/code/knapsack/knapsack_1.cpp"
    ```

## Complete knapsack

### Explanation

The complete knapsack model is similar to the 0-1 knapsack; the only difference from the 0-1 knapsack is that an item can be selected an unlimited number of times, rather than only once.

We can borrow the idea of the 0-1 knapsack to define the state: let $f_{i,j}$ be the maximum value a knapsack of capacity $j$ can achieve when only the first $i$ items can be selected.

Note that although the definition is similar to the 0-1 knapsack, its state-transition equation is not the same as the 0-1 knapsack's.

### Process

Consider a naive approach: for the $i$-th item, enumerate how many of it are selected to transition. The time complexity of doing this is $O(n^3)$.

The state-transition equation is as follows:

$$
f_{i,j}=\max_{k=0}^{+\infty}(f_{i-1,j-k\times w_i}+v_i\times k)
$$

Consider a simple optimization. We can find that for $f_{i,j}$, it suffices to transition through $f_{i,j-w_i}$. So the state-transition equation is:

$$
f_{i,j}=\max(f_{i-1,j},f_{i,j-w_i}+v_i)
$$

The reason is that when we transition this way, $f_{i,j-w_i}$ has already been updated by $f_{i,j-2\times w_i}$, so $f_{i,j-w_i}$ is the optimal result obtained after fully considering the number of times the $i$-th item is selected. In other words, we reuse the previous enumeration process through the property of local optimal substructure, optimizing the complexity of enumeration.

As with the 0-1 knapsack, we can remove the first dimension to optimize the space complexity. If you understood the optimization method of the 0-1 knapsack, it is not hard to see that the compressed loop is forward (that is, the wrong optimization mentioned above).

??? note "["Luogu P1616" Crazy Herb Gathering](https://www.luogu.com.cn/problem/P1616)"
    Problem summary: there are $n$ kinds of items and a knapsack of capacity $W$; each kind of item has two attributes, weight $w_{i}$ and value $v_{i}$. You are required to select some items to put into the knapsack so that the total value of the items in the knapsack is maximized and the total weight of the items in the knapsack does not exceed the knapsack's capacity.

??? note "Example code"
    ```cpp
    --8<-- "docs/dp/code/knapsack/knapsack_2.cpp"
    ```

## Multiple knapsack

The multiple knapsack is also a variant of the 0-1 knapsack. The difference from the 0-1 knapsack is that each kind of item has $k_i$ copies rather than one.

A very naive idea is to equivalently convert "select item of each kind $k_i$ times" into "there are $k_i$ identical items, each selected once". This converts it into a 0-1 knapsack model, which can be solved by applying the method described above. The state-transition equation is as follows:

$$
f_{i,j}=\max_{k=0}^{k_i}(f_{i-1,j-k\times w_i}+v_i\times k)
$$

Time complexity $O(W\sum_{i=1}^nk_i)$.

??? note "Core code"
    ```cpp
    for (int i = 1; i <= n; i++) {
      for (int weight = W; weight >= w[i]; weight--) {
        // traverse one more level for the item count
        for (int k = 1; k * w[i] <= weight && k <= cnt[i]; k++) {
          dp[weight] = max(dp[weight], dp[weight - k * w[i]] + k * v[i]);
        }
      }
    }
    ```

### Binary-grouping optimization

Consider optimizing. We still consider converting the multiple knapsack into a 0-1 knapsack model to solve.

### Explanation

Clearly, the $O(nW)$ part of the complexity cannot be optimized further; we can only work on the $O(\sum k_i)$ part. For convenience of description, we use $A_{i,j}$ to represent the $j$-th item split from the $i$-th kind of item.

In the naive approach, $\forall j\le k_i$, $A_{i,j}$ all represent the same item. Then the reason for our low efficiency is mainly that we did a lot of repetitive work. For example, we considered the two completely equivalent cases "select $A_{i,1},A_{i,2}$ together" and "select $A_{i,2},A_{i,3}$ together". We did such repetitive work many times. So optimizing the splitting method becomes the breakthrough for solving the problem.

### Process

We can make the splitting method more elegant via "binary grouping".

Specifically, let $A_{i,j}\left(j\in\left[0,\lfloor \log_2(k_i+1)\rfloor-1\right]\right)$ each represent a big item "bundled" from $2^{j}$ single items. In particular, if $k_i+1$ is not an integer power of $2$, we need to add at the end a big item "bundled" from $k_i-2^{\lfloor \log_2(k_i+1)\rfloor-1}$ single items to make up the difference.

A few examples:

-   $6=1+2+3$
-   $8=1+2+4+1$
-   $18=1+2+4+8+3$
-   $31=1+2+4+8+16$

Clearly, through the above splitting method, any equivalent selection of $\le k_i$ items can be represented. After splitting each kind of item as above, just solve using the 0-1 knapsack method.

Time complexity $O(W\sum_{i=1}^n\log_2k_i)$.

### Implementation

??? note "Binary-grouping code"
    === "C++"
        ```cpp
        index = 0;
        for (int i = 1; i <= m; i++) {
          int c = 1, p, h, k;
          cin >> p >> h >> k;
          while (k > c) {
            k -= c;
            list[++index].w = c * p;
            list[index].v = c * h;
            c *= 2;
          }
          list[++index].w = p * k;
          list[index].v = h * k;
        }
        ```
    
    === "Python"
        ```python
        index = 0
        for i in range(1, m + 1):
            c = 1
            p, h, k = map(int, input().split())
            while k > c:
                k -= c
                index += 1
                list[index].w = c * p
                list[index].v = c * h
                c *= 2
            index += 1
            list[index].w = p * k
            list[index].v = h * k
        ```

### Monotonic-queue optimization

See [Monotonic-queue / monotonic-stack optimization](./opt/monotonic-queue-stack.md).

Exercise: ["Luogu P1776" Treasure Screening \_NOI Guide 2010 Advanced (02)](https://www.luogu.com.cn/problem/P1776)

## Mixed knapsack

The mixed knapsack mixes the previous three knapsack problems together: some can be taken only once, some an unlimited number of times, and some only $k$ times.

This kind of problem looks scary, but as long as you grasp the central idea of the previous kinds of knapsacks and merge them together, it is fine. Below is pseudocode:

```plain
for (loop over item kinds) {
  if (it is a 0-1 knapsack)
    apply the 0-1 knapsack code;
  else if (it is a complete knapsack)
    apply the complete knapsack code;
  else if (it is a multiple knapsack)
    apply the multiple knapsack code;
}
```

### Example

???+ note "["Luogu P1833" Cherry Blossoms](https://www.luogu.com.cn/problem/P1833)"
    There are $n$ kinds of cherry-blossom trees and a length of time $T$; some cherry-blossom trees can be viewed only once, some at most $A_{i}$ times, and some an unlimited number of times. Each cherry-blossom tree has an aesthetic value $C_{i}$; find which cherry-blossom trees to view within time $T$ to maximize the aesthetic value.

??? note "Core code"
    ```cpp
    for (int i = 1; i <= n; i++) {
      if (cnt[i] == 0) {  // if the count is unlimited, use the complete-knapsack core code
        for (int weight = w[i]; weight <= W; weight++) {
          dp[weight] = max(dp[weight], dp[weight - w[i]] + v[i]);
        }
      } else {  // if the item is limited, use the multiple-knapsack core code, which can also handle the 0-1 knapsack problem
        for (int weight = W; weight >= w[i]; weight--) {
          for (int k = 1; k * w[i] <= weight && k <= cnt[i]; k++) {
            dp[weight] = max(dp[weight], dp[weight - k * w[i]] + k * v[i]);
          }
        }
      }
    }
    ```

Exercise: [HDU 5410 CRB and His Birthday](https://acm.hdu.edu.cn/showproblem.php?pid=5410)

## Two-dimensional-cost knapsack

???+ note "["Luogu P1855" Squeezing kkksc03](https://www.luogu.com.cn/problem/P1855)"
    There are $n$ tasks to complete; completing the $i$-th task costs $t_i$ minutes and incurs an expense of $c_i$ yuan.
    
    Now you have $T$ minutes and $W$ yuan to handle these tasks; find the maximum number of tasks that can be completed.

This is very obviously a 0-1 knapsack problem, but the difference is that selecting an item consumes two kinds of value (money, time); just add one dimension to the state to store the second kind of value.

At this point you must note that adding another dimension to store the item number is inappropriate, because it easily MLEs.

### Implementation

=== "C++"
    ```cpp
    for (int k = 1; k <= n; k++)
      for (int i = m; i >= mi; i--)    // one level of enumeration over money
        for (int j = t; j >= ti; j--)  // one level of enumeration over time
          dp[i][j] = max(dp[i][j], dp[i - mi][j - ti] + 1);
    ```

=== "Python"
    ```python
    for k in range(1, n + 1):
        for i in range(m, mi - 1, -1):  # one level of enumeration over money
            for j in range(t, ti - 1, -1):  # one level of enumeration over time
                dp[i][j] = max(dp[i][j], dp[i - mi][j - ti] + 1)
    ```

## Grouped knapsack

???+ note "["Luogu P1757" Tongtian Grouped Knapsack](https://www.luogu.com.cn/problem/P1757)"
    There are $n$ items and a knapsack of size $m$; the $i$-th item has value $w_i$ and volume $v_i$. At the same time, each item belongs to a group, and at most one item can be selected within the same group. Find the maximum total value of items the knapsack can hold.

How should we think about this kind of problem? Actually it changes from "select one out of all items" to "select one from the current group", so just do one 0-1 knapsack for each group.

Let's also talk about how to store it. We can use $t_{k,i}$ to denote the number of the $i$-th item of the $k$-th group, and use $\mathit{cnt}_k$ to denote how many items the $k$-th group has.

### Implementation

=== "C++"
    ```cpp
    for (int k = 1; k <= ts; k++)          // loop over each group
      for (int i = m; i >= 0; i--)         // loop over the knapsack capacity
        for (int j = 1; j <= cnt[k]; j++)  // loop over each item of this group
          if (i >= w[t[k][j]])             // knapsack capacity is sufficient
            dp[i] = max(dp[i],
                        dp[i - w[t[k][j]]] + c[t[k][j]]);  // transition like a 0-1 knapsack
    ```

=== "Python"
    ```python
    for k in range(1, ts + 1):  # loop over each group
        for i in range(m, -1, -1):  # loop over the knapsack capacity
            for j in range(1, cnt[k] + 1):  # loop over each item of this group
                if i >= w[t[k][j]]:  # knapsack capacity is sufficient
                    dp[i] = max(
                        dp[i], dp[i - w[t[k][j]]] + c[t[k][j]]
                    )  # transition like a 0-1 knapsack
    ```

Note here: **you must not get the loop order wrong**; only this way is correctness guaranteed.

## Knapsack with dependencies

???+ note "["Luogu P1064" Jinming's Budget Plan](https://www.luogu.com.cn/problem/P1064)"
    Jinming has $n$ yuan and wants to buy $m$ items; the $i$-th item has price $v_i$ and importance $p_i$. Some items are accessories subordinate to a certain main item; to buy such an item, you must buy its main item.
    
    The goal is to maximize the sum of $v_i \times p_i$ over all purchased items.

Consider case analysis. For a main item and its several accessories, there are the following possibilities: buy only the main item, or buy the main item + certain accessories. Because only one of these possibilities can be chosen, this can be viewed as a grouped knapsack.

If it is a collection of a multiway tree, compute the collections of the child nodes first, and the collection of the parent node last.

## Generalized-item knapsack

This kind of knapsack has no fixed cost and value; its value is determined by the cost allocated to it. In a knapsack problem with knapsack capacity $V$, when the cost allocated to it is $v_i$, the value obtainable is $h\left(v_i\right)$. In this case, just replace the fixed value with a reference to a function.

## Miscellaneous

### Small optimizations

By the greedy principle, when the cost is the same, keep only the one with the highest value; when the value is fixed, keep only the one with the lowest cost; when there are two items $i,j$ where $i$'s value is greater than $j$'s and $i$'s cost is smaller than $j$'s, keep only $i$.

### Variants of the knapsack problem

#### Outputting the scheme

Outputting the scheme is actually recording how a certain state in the knapsack was derived. We can use $g_{i,v}$ to indicate whether the $i$-th item was selected when it occupied space $v$. Then, during the transition, record which strategy (select or not) was used. Pseudocode when outputting:

```cpp
int v = V;  // record the current storage space

// because the last item stores the final state, loop from the last item
for (loop from the last item to the first) {
  if (g[i][v]) {
    selected item i;
    v -= the weight of item i;
  } else {
    did not select item i;
  }
}
```

#### Counting schemes

For a problem with a given knapsack capacity, item costs, other relations, etc., find the total number of schemes that fill up to a certain capacity.

For this kind of problem, just change finding the maximum to summing.

For example, the transition equation of the 0-1 knapsack problem becomes:

$$
\mathit{dp}_j \leftarrow \mathit{dp}_j + \mathit{dp}_{j-c_i} \qquad (j \ge c_i)
$$

Initial condition: $\mathit{dp}_0=1$

Because when the capacity is $0$ there is also one scheme, namely putting nothing in.

#### Counting optimal schemes

To count the optimal schemes, we slightly modify the definition of the $\mathit{dp}$ array in the 0-1 knapsack: the DP state $f_{i,j}$ is the maximum total value achievable when a knapsack of capacity $j$ is "exactly filled" using only the first $i$ items.

After this modification, each DP state can use a $g_{i,j}$ to represent the number of schemes.

$f_{i,j}$ denotes the maximum value when the knapsack volume is "exactly" $j$ considering only the first $i$ items.

$g_{i,j}$ denotes the number of schemes when the knapsack volume is "exactly" $j$ considering only the first $i$ items.

Transition equations:

If $f_{i,j} = f_{i-1,j}$ and $f_{i,j} \neq f_{i-1,j-v}+w$, it means not putting the item into the knapsack is better here, and the scheme count is transitioned from $g_{i-1,j}$;

If $f_{i,j} \neq f_{i-1,j}$ and $f_{i,j} = f_{i-1,j-v}+w$, it means putting the item into the knapsack is better here, and the scheme count is transitioned from $g_{i-1,j-v}$;

If $f_{i,j} = f_{i-1,j}$ and $f_{i,j} = f_{i-1,j-v}+w$, it means putting it in or not both achieve the optimal solution, and the scheme count is transitioned from both $g_{i-1,j}$ and $g_{i-1,j-v}$.

Initial conditions:

```cpp
memset(f, 0xcf, sizeof(f));
// because we are finding the maximum, initialize to negative infinity to avoid transitioning without being filled
// if finding the minimum, initialize to positive infinity 0x3f
f[0] = 0;
g[0] = 1;  // putting nothing in is one scheme
```

Because the maximum knapsack volume may not be filled, the optimal solution is not necessarily $f_{m}$.

Finally, by finding the value of the optimal solution, we just add up all the scheme counts in the array $g_{j}$ that achieve the optimal solution.

???+ note "Implementation"
    ```cpp
    for (int i = 0; i < N; i++) {
      for (int j = V; j >= v[i]; j--) {
        int tmp = std::max(dp[j], dp[j - v[i]] + w[i]);
        int c = 0;
        if (tmp == dp[j]) c += cnt[j];                       // if transitioned from dp[j]
        if (tmp == dp[j - v[i]] + w[i]) c += cnt[j - v[i]];  // if transitioned from dp[j-v[i]]
        dp[j] = tmp;
        cnt[j] = c;
      }
    }
    int max = 0;  // find the optimal solution
    for (int i = 0; i <= V; i++) {
      max = std::max(max, dp[i]);
    }
    int res = 0;
    for (int i = 0; i <= V; i++) {
      if (dp[i] == max) {
        res += cnt[i];  // sum the scheme counts of the optimal solution
      }
    }
    ```

#### The k-th best solution of the knapsack

The ordinary 0-1 knapsack finds the optimal solution; by slightly modifying the ordinary knapsack DP method and adding one dimension to record the top-k best solutions of the current state, we obtain an algorithm for finding the $k$-th best solution of the 0-1 knapsack.
Specifically: $\mathit{dp_{i,j,k}}$ records the $k$-th largest total value achievable when the total volume of items selected among the first $i$ items is $j$. This state can be understood as extending the $\mathit{dp_{i,j}}$ of the ordinary 0-1 knapsack, which records only one datum, into recording an ordered sequence of best solutions. When transitioning, the ordinary knapsack computes the optimal solution via $\mathit{dp_{i,j}}=\max(\mathit{dp_{i-1,j}},\mathit{dp_{i-1,j-v_{i}}}+w_{i})$; now we instead merge the two size-$k$ decreasing sequences $\mathit{dp_{i-1,j}}$ and $\mathit{dp_{i-1,j-v_{i}}}+w_{i}$, and keep the top $k$ largest values after merging, recorded in $\mathit{dp_{i,j}}$; this step uses the two-pointer method with complexity $O(k)$, and the overall time complexity is $O(nmk)$. In terms of space, this method, like the ordinary knapsack, can compress away the first dimension, with complexity $O(mk)$.

??? note "Example [HDU 2639 Bone Collector II](https://acm.hdu.edu.cn/showproblem.php?pid=2639)"
    Find the strict $k$-th best solution of the 0-1 knapsack. $n \leq 100,v \leq 1000,k \leq 30$

??? note "Implementation"
    ```cpp
    memset(dp, 0, sizeof(dp));
    int i, j, p, x, y, z;
    scanf("%d%d%d", &n, &m, &K);
    for (i = 0; i < n; i++) scanf("%d", &w[i]);
    for (i = 0; i < n; i++) scanf("%d", &c[i]);
    for (i = 0; i < n; i++) {
      for (j = m; j >= c[i]; j--) {
        for (p = 1; p <= K; p++) {
          a[p] = dp[j - c[i]][p] + w[i];
          b[p] = dp[j][p];
        }
        a[p] = b[p] = -1;
        x = y = z = 1;
        while (z <= K && (a[x] != -1 || b[y] != -1)) {
          if (a[x] > b[y])
            dp[j][z] = a[x++];
          else
            dp[j][z] = b[y++];
          if (dp[j][z] != dp[j][z - 1]) z++;
        }
      }
    }
    printf("%d\n", dp[m][K]);
    ```

## References and notes

-   [The Nine Lectures on the Knapsack Problem - Cui Tianyi](https://github.com/tianyicui/pack).
