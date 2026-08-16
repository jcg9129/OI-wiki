## Building a block array

A block array divides an array into several blocks, storing the block information as a whole; if a query encounters an incomplete block on either side, it queries it directly by brute force. In general, the block length is $O(\sqrt{n})$. For a detailed analysis, you can read Xu Mingkuan's "A Preliminary Exploration of Non-Conventional-Size Block Algorithms" in the 2017 National Training Team papers.

Below is directly given a piece of code for building a block array.

???+ note "Implementation"
    ```cpp
    num = sqrt(n);
    for (int i = 1; i <= num; i++)
      st[i] = n / num * (i - 1) + 1, ed[i] = n / num * i;
    ed[num] = n;
    for (int i = 1; i <= num; i++) {
      for (int j = st[i]; j <= ed[i]; j++) {
        belong[j] = i;
      }
      size[i] = ed[i] - st[i] + 1;
    }
    ```

Here `st[i]` and `ed[i]` are the start and end of a block, and `size[i]` is the size of the block.

## Storing and modifying block information

### Example 1: [The Guru's Magic](https://www.luogu.com.cn/problem/P2801)

Two operations:

1.  Add $z$ to each number in the interval $[x,y]$;
2.  Query the number of numbers greater than or equal to $z$ in the interval $[x,y]$.

We want to query the number of numbers in a block greater than or equal to a given number, so we need a `t` array to sort within the block, where `a` is the original (unsorted) array. For modifying a whole block, we use a method similar to permanent tagging, using the `delta` array to record the value currently added to the whole block. Let $q$ be the total number of query and modification operations; then the time complexity is $O(q\sqrt{n}\log n)$.

Use the `delta` array to record the whole-block assignment of each block.

???+ note "Implementation"
    ```cpp
    void Sort(int k) {
      for (int i = st[k]; i <= ed[k]; i++) t[i] = a[i];
      sort(t + st[k], t + ed[k] + 1);
    }
    
    void Modify(int l, int r, int c) {
      int x = belong[l], y = belong[r];
      if (x == y)  // if the interval is within one block, modify directly
      {
        for (int i = l; i <= r; i++) a[i] += c;
        Sort(x);
        return;
      }
      for (int i = l; i <= ed[x]; i++) a[i] += c;     // directly modify the starting part
      for (int i = st[y]; i <= r; i++) a[i] += c;     // directly modify the ending part
      for (int i = x + 1; i < y; i++) delta[i] += c;  // tag the whole middle blocks
      Sort(x);
      Sort(y);
    }
    
    int Answer(int l, int r, int c) {
      int ans = 0, x = belong[l], y = belong[r];
      if (x == y) {
        for (int i = l; i <= r; i++)
          if (a[i] + delta[x] >= c) ans++;
        return ans;
      }
      for (int i = l; i <= ed[x]; i++)
        if (a[i] + delta[x] >= c) ans++;
      for (int i = st[y]; i <= r; i++)
        if (a[i] + delta[y] >= c) ans++;
      for (int i = x + 1; i <= y - 1; i++)
        ans +=
            ed[i] - (lower_bound(t + st[i], t + ed[i] + 1, c - delta[i]) - t) + 1;
      // use lower_bound to find, in each whole middle block, the position of the first number greater than or equal to c
      return ans;
    }
    ```

### Example 2: Ark in the Cold Night

Two operations:

1.  Change each number in the interval $[x,y]$ to $z$;
2.  Query the number of numbers less than or equal to $z$ in the interval $[x,y]$.

Use the `delta` array to record the value the whole block is currently assigned to. When the block has not been assigned as a whole, use a special value (such as `0x3f3f3f3f3f3f3f3fll`) to indicate this. For the corner blocks, `pushdown` before querying to push down the information stored for the block onto each number. Remember to re-`sort` after assignment. Other aspects are the same as the previous problem.

???+ note "Implementation"
    ```cpp
    void Sort(int k) {
      for (int i = st[k]; i <= ed[k]; i++) t[i] = a[i];
      sort(t + st[k], t + ed[k] + 1);
    }
    
    void PushDown(int x) {
      if (delta[x] != 0x3f3f3f3f3f3f3f3fll)  // use this value to mark that the block has not been assigned as a whole
        for (int i = st[x]; i <= ed[x]; i++) a[i] = t[i] = delta[x];
      delta[x] = 0x3f3f3f3f3f3f3f3fll;
    }
    
    void Modify(int l, int r, int c) {
      int x = belong[l], y = belong[r];
      PushDown(x);
      if (x == y) {
        for (int i = l; i <= r; i++) a[i] = c;
        Sort(x);
        return;
      }
      PushDown(y);
      for (int i = l; i <= ed[x]; i++) a[i] = c;
      for (int i = st[y]; i <= r; i++) a[i] = c;
      Sort(x);
      Sort(y);
      for (int i = x + 1; i < y; i++) delta[i] = c;
    }
    
    int Binary_Search(int l, int r, int c) {
      int ans = l - 1, mid;
      while (l <= r) {
        mid = (l + r) / 2;
        if (t[mid] <= c)
          ans = mid, l = mid + 1;
        else
          r = mid - 1;
      }
      return ans;
    }
    
    int Answer(int l, int r, int c) {
      int ans = 0, x = belong[l], y = belong[r];
      PushDown(x);
      if (x == y) {
        for (int i = l; i <= r; i++)
          if (a[i] <= c) ans++;
        return ans;
      }
      PushDown(y);
      for (int i = l; i <= ed[x]; i++)
        if (a[i] <= c) ans++;
      for (int i = st[y]; i <= r; i++)
        if (a[i] <= c) ans++;
      for (int i = x + 1; i <= y - 1; i++) {
        if (0x3f3f3f3f3f3f3f3fll == delta[i])
          ans += Binary_Search(st[i], ed[i], c) - st[i] + 1;
        else if (delta[i] <= c)
          ans += size[i];
      }
      return ans;
    }
    ```

## Exercises

1.  [Single-point modification, interval query](https://loj.ac/problem/130)
2.  [Interval modification, interval query](https://loj.ac/problem/132)
3.  [【Template】Segment Tree 2](https://www.luogu.com.cn/problem/P3373)
4.  [「Ynoi2019 Mock Contest」Yuno loves sqrt technology III](https://www.luogu.com.cn/problem/P5048)
5.  [「Violet」Dandelion](https://www.luogu.com.cn/problem/P4168)
6.  [Composing Poetry](https://www.luogu.com.cn/problem/P4135)
