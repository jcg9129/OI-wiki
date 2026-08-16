Prerequisites: [bit operations](./bit.md#bit-operations), [integers and bit sequences](./bit.md#integers-and-bit-sequences).

The binary representation of a number can be regarded as a set ($0$ means not in the set, $1$ means in the set). For example, the set $\{1,3,4,8\}$ can be represented as $(100011010)_2$. And the corresponding bit operations can be regarded as operations performed on sets.

| Operation | Set notation | Bit-operation notation |
| ------ | :-------------: | :-------------------------: |
| Intersection | $a \cap b$ | $a \operatorname{AND} b$ |
| Union | $a \cup b$ | $a \operatorname{OR} b$ |
| Complement | $\bar{a}$ | $\operatorname{NOT} a$ (the universal set is all 1s in binary) |
| Difference | $a \setminus b$ | $a \operatorname{AND} \operatorname{NOT} b$ |
| Symmetric difference | $a\triangle b$ | $a \operatorname{XOR} b$ |

Before further introducing the operation of traversing the subsets of a set, let us first look at some example applications related to bit operations.

### Modulo a power of 2

Taking a number modulo a non-negative integer power of $2$ is equivalent to taking the last several bits of a number in binary, which is equivalent to performing an AND operation with $mod-1$.

=== "C++"
    ```cpp
    int modPowerOfTwo(int x, int mod) { return x & (mod - 1); }
    ```

=== "Python"
    ```python
    def modPowerOfTwo(x, mod):
        return x & (mod - 1)
    ```

Thus one can see that a non-negative integer power of $2$ taken modulo itself gives $0$; that is, if $n$ is a non-negative integer power of $2$, then the AND operation of $n$ and $n-1$ results in $0$.

In fact, for a positive integer $n$, $n-1$ zeros out the lowest $1$ bit of $n$ and sets all the subsequent bits to $1$. Therefore, the AND operation of $n$ and $n-1$ is equivalent to removing the lowest $1$ bit of $n$.

By this one can determine whether a number is a non-negative integer power of $2$. $n$ is a non-negative integer power of $2$ if and only if the binary representation of $n$ has only one $1$.

=== "C++"
    ```cpp
    bool isPowerOfTwo(int n) { return n > 0 && (n & (n - 1)) == 0; }
    ```

=== "Python"
    ```python
    def isPowerOfTwo(n):
        return n > 0 and (n & (n - 1)) == 0
    ```

### Subset traversal

Traversing all subsets of a set represented by a binary number is equivalent to enumerating all submasks of the mask corresponding to the binary number.

A mask is a string of binary code, used to perform an AND operation with a source code, obtaining a new operand after masking out several input bits of the source code.

A mask can play a masking role for the source code: a $1$ bit in the mask means the corresponding bit of the source code is retained, and a $0$ bit in the mask means the corresponding bit of the source code is set to $0$. Changing some $1$ bits of the mask to $0$ bits yields a submask of the mask; the mask itself is also a submask of itself.

Given a mask $m$, if one wishes to efficiently iterate over all submasks $s$ of $m$, one can consider an implementation based on bit-operation tricks.

```cpp
// Traverse the non-empty subsets of m in descending order
int s = m;
while (s > 0) {
  // s is a non-empty subset of m
  s = (s - 1) & m;
}
```

Or use the more compact for statement:

```cpp
// Traverse the non-empty subsets of m in descending order
for (int s = m; s; s = (s - 1) & m)
// s is a non-empty subset of m
```

Neither of these two pieces of code handles the submask equal to $0$; to handle the submask equal to $0$, one can use other methods, for example:

```cpp
// Traverse the subsets of m in descending order
for (int s = m;; s = (s - 1) & m) {
  // s is a subset of m
  if (s == 0) break;
}
```

Next we prove that the above code visits all submasks of $m$, without repetition, and in descending order.

Suppose we have a current bitmask $s$ and want to continue to visit the next bitmask. Subtracting $1$ from the mask $s$ is equivalent to removing the rightmost set bit of the mask $s$ and turning all the bits to its right into $1$.

To make $s-1$ become a new submask, one needs to remove all the extra $1$ bits not contained in the mask $m$; one can use the bit operation `(s - 1) & m` to perform this removal.

These two operations are equivalent to cutting the mask $s-1$ down to determine the largest value arithmetically attainable, i.e. the next submask after $s$ in descending order.

Therefore, this algorithm generates all submasks of the mask in descending order, performing only two operations per iteration.

The special case is $s=0$. After performing $s-1$, one obtains $-1$, in which all bits are $1$. After the `(s - 1) & m` operation, one obtains the new $s$ equal to $m$. Therefore, if the loop does not end at $s=0$, the algorithm's loop will fail to terminate.

Using $\text{popcount}(m)$ to denote the number of $1$s in the binary representation of $m$, this method can traverse the subsets of the set $m$ in $O(2^{\text{popcount}(m)})$ time complexity.

### Traversing the submasks of all masks

In problems using bitmask DP, one sometimes wishes, for each mask, to traverse all submasks of the mask:

```cpp
for (int m = 0; m < (1 << n); ++m)
  // Traverse the non-empty subsets of m in descending order
  for (int s = m; s; s = (s - 1) & m)
// s is a non-empty subset of m
```

Doing this traverses the subsets of each subset of a set of size $n$.

Next we prove that the time complexity of this operation is $O(3^n)$, where $n$ is the total number of bits of the mask, i.e. the total number of elements in the set.

Consider the $i$-th bit, i.e. the $i$-th element in the set; there are three cases:

- It is $0$ in the mask $m$, and therefore $0$ in the submask $s$, i.e. the element is in neither the large nor the small subset.
- It is $1$ in $m$ but $0$ in $s$, i.e. the element is only in the large subset, not in the small subset.
- It is $1$ in both $m$ and $s$, i.e. the element is in both the large and small subsets.

There are $n$ bits in total, so there are $3^n$ different combinations.

There is another proof method:

If the mask $m$ has $k$ $1$s, then it has $2^k$ submasks. For a given $k$, there are correspondingly $\dbinom{n}{k}$ masks $m$, so the total number over all masks is:

$$
\sum_{k=0}^n \dbinom{n}{k} 2^k
$$

The above sum equals the expansion of $(1+2)^n$ using the binomial theorem, so there are $3^n$ different combinations.

### References

**This page is mainly translated from the blog post [Перебор всех подмасок данной маски](http://e-maxx.ru/algo/all_submasks) and its English translation [Submask Enumeration](https://cp-algorithms.com/algebra/all-submasks.html). The Russian version is under the Public Domain + Leave a Link license; the English version is under the CC-BY-SA 4.0 license.**

### Exercises

- [Atcoder - Close Group](https://atcoder.jp/contests/abc187/tasks/abc187_f)
- [Codeforces - Nuclear Fusion](http://codeforces.com/problemset/problem/71/E)
- [Codeforces - Sandy and Nuts](http://codeforces.com/problemset/problem/599/E)
- [UVa 1439 - Exclusive Access 2](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=4185)
- [UVa 11825 - Hackers' Crackdown](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2925)
