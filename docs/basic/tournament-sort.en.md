This page briefly introduces tournament sort.

## Definition

Tournament sort, also called tree selection sort, is an optimized version of [selection sort](./selection-sort.md) and a variant of [heapsort](./heap-sort.md) (both use a complete binary tree). On top of selection sort, it uses a priority queue to find the next element to select.

## Introduction

The name of tournament sort comes from the single-elimination form of competition. In this format, many players participate in the competition; they compare pairwise, and the winner advances to the next round. This elimination method can determine the best player, but the player eliminated in the final round is not necessarily the second best—they may be worse than a player eliminated earlier.

## Process

Take the **minimum tournament sort tree** as an example:

![tournament-sort1](./images/tournament-sort1.png)

The elements to be sorted are the elements displayed at the leaf nodes. The red edges show the winning path of the smaller element in each round of comparison. Clearly, completing one "tournament" can select the smallest one from a group of elements.

After each round of comparing $n$ elements, $\frac{n}{2}$ "winners" are obtained, with the smaller element of each pair advancing to the next round of comparison. If a pair of elements cannot be formed, then that element advances directly to the next round of comparison.

![tournament-sort2](./images/tournament-sort2.png)

After completing one "tournament", the selected element needs to be removed. Simply set it to $\infty$ (this operation is similar to [heapsort](./heap-sort.md)), then hold the "tournament" again to select the second-smallest element.

Then repeat this operation until all elements are sorted.

## Properties

### Stability

Tournament sort is an unstable sorting algorithm.

### Time complexity

The best-case, average-case, and worst-case time complexities of tournament sort are all $O(n\log n)$. It uses $O(n)$ time to initialize the "tournament", and then $O(\log n)$ time to select one element from the $n$ elements.

### Space complexity

The space complexity of tournament sort is $O(n)$.

## Implementation

=== "C++"
    ```cpp
    int n, a[MAXN], tmp[MAXN << 1];
    
    int winner(int pos1, int pos2) {
      int u = pos1 >= n ? pos1 : tmp[pos1];
      int v = pos2 >= n ? pos2 : tmp[pos2];
      if (tmp[u] <= tmp[v]) return u;
      return v;
    }
    
    void creat_tree(int &value) {
      for (int i = 0; i < n; i++) tmp[n + i] = a[i];
      for (int i = 2 * n - 1; i > 1; i -= 2) {
        int k = i / 2;
        int j = i - 1;
        tmp[k] = winner(i, j);
      }
      value = tmp[tmp[1]];
      tmp[tmp[1]] = INF;
    }
    
    void recreat(int &value) {
      int i = tmp[1];
      while (i > 1) {
        int j, k = i / 2;
        if (i % 2 == 0)
          j = i + 1;
        else
          j = i - 1;
        tmp[k] = winner(i, j);
        i = k;
      }
      value = tmp[tmp[1]];
      tmp[tmp[1]] = INF;
    }
    
    void tournament_sort() {
      int value;
      creat_tree(value);
      for (int i = 0; i < n; i++) {
        a[i] = value;
        recreat(value);
      }
    }
    ```

=== "Python"
    ```python
    n = 0
    a = [0] * MAXN
    tmp = [0] * MAXN * 2
    
    
    def winner(pos1, pos2):
        u = pos1 if pos1 >= n else tmp[pos1]
        v = pos2 if pos2 >= n else tmp[pos2]
        if tmp[u] <= tmp[v]:
            return u
        return v
    
    
    def creat_tree():
        for i in range(0, n):
            tmp[n + i] = a[i]
        for i in range(2 * n - 1, 1, -2):
            k = int(i / 2)
            j = i - 1
            tmp[k] = winner(i, j)
        value = tmp[tmp[1]]
        tmp[tmp[1]] = INF
        return value
    
    
    def recreat():
        i = tmp[1]
        while i > 1:
            j = k = int(i / 2)
            if i % 2 == 0:
                j = i + 1
            else:
                j = i - 1
            tmp[k] = winner(i, j)
            i = k
        value = tmp[tmp[1]]
        tmp[tmp[1]] = INF
        return value
    
    
    def tournament_sort():
        value = creat_tree()
        for i in range(0, n):
            a[i] = value
            value = recreat()
    ```

## External links

-   [Tournament sort - Wikipedia](https://en.wikipedia.org/wiki/Tournament_sort)
