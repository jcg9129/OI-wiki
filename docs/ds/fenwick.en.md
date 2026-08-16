author: HeRaNO, Zhoier, Ir1d, Xeonacid, wangdehu, ouuan, ranwen, ananbaobeichicun, Ycrpro, dbxxx-oi, HowieHz, y-kx-b

## Introduction

A Fenwick tree (binary indexed tree) is a data structure with a small amount of code that supports **single-point modification** and **range query**.

??? note "What are 'single-point modification' and 'range query'?"
    Suppose there is such a problem:
    
    Given a sequence $a$, you need to perform the following two operations:
    
    -   Given $x, y$, increment $a[x]$ by $y$.
    -   Given $l, r$, compute the sum of $a[l \ldots r]$.
    
    The first kind of operation is "single-point modification", and the second is "range query".
    
    Similarly, there are also "range modification" and "single-point query". One example of each is as follows:
    
    -   Range modification: given $l, r, x$, increment each number in $a[l \ldots r]$ by $x$;
    -   Single-point query: given $x$, compute the value of $a[x]$.
    
    Note that the range problem is generally strictly stronger than the single-point problem, because an operation on a single point is equivalent to an operation on an interval of length $1$.

The information and operations an ordinary Fenwick tree maintains must satisfy **associativity** and be **differenceable**, such as addition (sum), multiplication (product), XOR, etc.

-   Associativity: $(x \circ y) \circ z = x \circ (y \circ z)$, where $\circ$ is a binary operator.
-   Differenceable: an operation with an inverse, i.e. knowing $x \circ y$ and $x$ one can find $y$.

Note that:

-   For multiplication under a modulus to be differenceable, each number must have an inverse (which always exists when the modulus is prime);
-   Information such as $\gcd$ and $\max$ is not differenceable, so an ordinary Fenwick tree cannot handle it, but:
    -   Using two Fenwick trees, one can handle range extrema; see [Efficient Range Minimum Queries using Binary Indexed Trees](http://history.ioinformatics.org/oi/files/volume9.pdf#page=41).
    -   This page also introduces an extended Fenwick tree with $\Theta(\log^2n)$ time complexity that supports querying non-differenceable information.

In fact, the problems a Fenwick tree can solve are a subset of those a segment tree can solve: what a Fenwick tree can do, a segment tree can certainly do; what a segment tree can do, a Fenwick tree may not be able to. However, the code of a Fenwick tree is far shorter than that of a segment tree, and its time-efficiency constant factor is also smaller, so it is still worth learning.

Sometimes, with the help of a difference array and auxiliary arrays, a Fenwick tree can also solve the stronger **range-add single-point-value** and **range-add range-sum** problems.

## Fenwick tree

### Initial feel

Let's give an example first: we want to know the prefix sum of $a[1 \ldots 7]$; how do we do it?

One way is: $a_1 + a_2 + a_3 + a_4 + a_5 + a_6 + a_7$, requiring the sum of $7$ numbers.

But if we know three numbers $A$, $B$, $C$, where $A =$ the sum of $a[1 \ldots 4]$, $B =$ the total of $a[5 \ldots 6]$, and $C =$ the total of $a[7 \ldots 7]$ (which is $a[7]$ itself). How would you compute it? You would certainly answer: $A + B + C$, requiring the sum of only $3$ numbers.

This is why a Fenwick tree can quickly compute information: we can always split a prefix $[1, n]$ into **no more than $\boldsymbol{\log n}$ intervals** such that the information of these $\log n$ intervals is **known**.

So we only need to merge the information of these $\log n$ intervals to get the answer. Compared with directly merging the original $n$ pieces of information, the efficiency is greatly improved.

It is not hard to see that the information must satisfy associativity, otherwise it could not be merged as above.

The figure below shows how a Fenwick tree works:

![](./images/fenwick.svg)

The eight blocks at the bottom represent the original data array $a$. The jagged blocks above (which are the same array as the eight blocks at the very top) represent the superior of array $a$—the $c$ array.

The $c$ array is used to store the sum of some interval of the original array $a$, i.e. the information of these intervals is known, and our goal is to split the query prefix into these small intervals.

For example, from the figure we can see:

-   $c_2$ governs $a[1 \ldots 2]$;
-   $c_4$ governs $a[1 \ldots 4]$;
-   $c_6$ governs $a[5 \ldots 6]$;
-   $c_8$ governs $a[1 \ldots 8]$;
-   the remaining $c[x]$ all govern $a[x]$ itself (which can be seen as the length-$1$ small interval $a[x \ldots x]$).

It is not hard to see that $c[x]$ always governs the total information of an interval whose right boundary is $x$. Let's not worry about the left boundary for now and first get a feel for how a Fenwick tree queries.

Example: compute the sum of $a[1 \ldots 7]$.

Process: starting from $c_{7}$ and jumping backward, we find that $c_{7}$ governs only the element $a_{7}$; then we look at $c_{6}$ and find that $c_{6}$ governs $a[5 \ldots 6]$, then jump to $c_{4}$ and find that $c_{4}$ governs the elements $a[1 \ldots 4]$, then try to jump to $c_0$, but in fact $c_0$ does not exist, so we stop.

The $c$ we just found are $c_7, c_6, c_4$; in fact these are exactly the three small intervals $a[1 \ldots 7]$ is split into, and merging them gives the answer $c_7 + c_6 + c_4$.

Example: compute the sum of $a[4 \ldots 7]$.

We still start from $c_7$ and jump, to $c_6$ then to $c_4$. At this point we find it manages the sum of $a[1 \ldots 4]$, but we do not want the part $a[1 \ldots 3]$; what do we do? Very simple: just subtract the sum of $a[1 \ldots 3]$.

So we may as well, at the very start, transform the query for the sum of $a[4 \ldots 7]$ into the query for the sum of $a[1 \ldots 7]$ and the query for the sum of $a[1 \ldots 3]$, and finally take the difference of the two results.

![](images/fenwick-query.svg)

### Governed interval

So the question arises: exactly how far left does the interval governed by $c[x](x \ge 1)$ extend? That is, what is the interval length?

In a Fenwick tree, the length of the interval governed by $c[x]$ is stipulated to be $2^{k}$, where:

-   let the lowest binary bit be bit $0$; then $k$ is exactly the bit position of the lowest `1` in the binary representation of $x$;
-   $2^k$ (the length of the interval $c[x]$ governs) is exactly the number formed by the lowest `1` in the binary representation of $x$ together with all the `0`s after it.

For example, which interval does $c_{88}$ govern?

Because $88_{(10)}=01011000_{(2)}$, the binary formed by the lowest `1` and the `0`s after it is `1000`, i.e. $8$, so $c_{88}$ governs $8$ elements of the $a$ array.

Therefore, $c_{88}$ represents the interval information of $a[81 \ldots 88]$.

We denote the number formed by the lowest `1` of $x$ and the `0`s after it as $\operatorname{lowbit}(x)$; then the interval $c[x]$ governs is $[x-\operatorname{lowbit}(x)+1, x]$.

???+ warning "Note"
    $\operatorname{lowbit}$ is not the bit position $k$ of the lowest `1`, but the $2^k$ formed by this `1` and all the `0`s after it.

How to compute `lowbit`? By bit-operation knowledge, we get `lowbit(x) = x & -x`.

??? note "The principle of lowbit"
    Inverting all bits of the binary of `x` and then adding 1 gives the binary encoding of `-x`. For example, the binary encoding of $6$ is `110`; inverting all bits gives `001`, and adding `1` gives `010`.
    
    Let the original binary encoding of `x` be `(...)10...00`; inverting all bits gives `[...]01...11`, and adding `1` gives `[...]10...00`, which is the binary encoding of `-x`. Here the first `1` in the binary representation of `x` is the lowest `1` of `x`.
    
    Each bit in the ellipses of `(...)` and `[...]` is respectively opposite, so `x & -x = (...)10...00 & [...]10...00 = 10...00`, and the result obtained is the `lowbit`.

???+ note "Implementation"
    === "C++"
        ```cpp
        int lowbit(int x) {
          // the number formed by the lowest 1 in the binary of x and all the 0s after it.
          // lowbit(0b01011000) == 0b00001000
          //          ~~~~^~~~
          // lowbit(0b01110010) == 0b00000010
          //          ~~~~~~^~
          return x & -x;
        }
        ```
    
    === "Python"
        ```python
        def lowbit(x):
            """
            the number formed by the lowest 1 in the binary of x and all the 0s after it.
            lowbit(0b01011000) == 0b00001000
                    ~~~~~^~~
            lowbit(0b01110010) == 0b00000010
                    ~~~~~~~^~
            """
            return x & -x
        ```

### Range query

Next let's look at the specific operation implementations of a Fenwick tree, starting with range query.

Recall the process of querying $a[4 \ldots 7]$; we transformed it into two subprocesses: query $a[1 \ldots 7]$ and query the sum of $a[1 \ldots 3]$, and finally take the difference.

In fact, any range query can be done this way: querying the sum of $a[l \ldots r]$ is the sum of $a[1 \ldots r]$ minus the sum of $a[1 \ldots l - 1]$, thereby transforming the range problem into a prefix problem, which is more convenient to handle.

In fact, transforming a range query about $l \ldots r$ into prefix queries about $1 \ldots r$ and $1 \ldots l - 1$ and then taking the difference is a very commonly used technique in contests.

So how do we do a prefix query? Recall the process of querying $a[1 \ldots 7]$:

> Starting from $c_{7}$ and jumping backward, we find that $c_{7}$ governs only the element $a_{7}$; then we look at $c_{6}$ and find that $c_{6}$ governs $a[5 \ldots 6]$, then jump to $c_{4}$ and find that $c_{4}$ governs the elements $a[1 \ldots 4]$, then try to jump to $c_0$, but in fact $c_0$ does not exist, so we stop.
>
> The $c$ we just found are $c_7, c_6, c_4$; in fact these are exactly the three small intervals $a[1 \ldots 7]$ is split into, and merging them, the answer is $c_7 + c_6 + c_4$.

Observing the above process, each jump backward always jumps to the position just left of the current interval's left endpoint, as the new interval's right endpoint, so that the prefix is split without overlap or omission. For example, now $c_6$ manages $a[5 \ldots 6]$, and the next jump goes to $5 - 1 = 4$, i.e. accessing $c_4$.

We can write out the process of querying $a[1 \ldots x]$:

-   Starting from $c[x]$ and jumping backward, $c[x]$ governs $a[x-\operatorname{lowbit}(x)+1 \ldots x]$;
-   Let $x \gets x - \operatorname{lowbit}(x)$; if $x = 0$ it means we have jumped to the end, so terminate the loop; otherwise return to the first step.
-   Merge the $c$ jumped to.

In implementation, we do not necessarily need to first jump out all the $c$ and then merge them together; we can merge while jumping.

For example, if the information we maintain is the sum, directly let the initial $\mathrm{ans} = 0$, and each time we jump to a $c[x]$, do $\mathrm{ans} \gets \mathrm{ans} + c[x]$; finally $\mathrm{ans}$ is the result of all the merges.

???+ note "Implementation"
    === "C++"
        ```cpp
        int getsum(int x) {  // the sum of a[1]..a[x]
          int ans = 0;
          while (x > 0) {
            ans = ans + c[x];
            x = x - lowbit(x);
          }
          return ans;
        }
        ```
    
    === "Python"
        ```python
        def getsum(x):  # the sum of a[1]..a[x]
            ans = 0
            while x > 0:
                ans = ans + c[x]
                x = x - lowbit(x)
            return ans
        ```

### Properties of the Fenwick tree and its tree structure

Before explaining single-point modification, let's explain some basic properties of the Fenwick tree and where its tree structure comes from; this helps in better understanding the Fenwick tree's single-point modification.

We agree:

-   $l(x) = x - \operatorname{lowbit}(x) + 1$. That is, $l(x)$ is the left endpoint of the range $c[x]$ governs.
-   For any positive integer $x$, one can always represent $x$ in the form $s \times 2^{k + 1} + 2^k$, where $\operatorname{lowbit}(x) = 2^k$.
-   Below, "$c[x]$ and $c[y]$ are disjoint" means the range $c[x]$ governs and the range $c[y]$ governs are disjoint, i.e. $[l(x), x]$ and $[l(y), y]$ are disjoint. Expressions such as "$c[x]$ is contained in $c[y]$" are analogous.

**Property $\boldsymbol{1}$: for $\boldsymbol{x \le y}$, either $\boldsymbol{c[x]}$ and $\boldsymbol{c[y]}$ are disjoint, or $\boldsymbol{c[x]}$ is contained in $\boldsymbol{c[y]}$.**

??? note "Proof"
    Proof: suppose $c[x]$ and $c[y]$ intersect, i.e. $[l(x), x]$ and $[l(y), y]$ intersect; then there must be $l(y) \le x \le y$.
    
    Represent $y$ as $s \times 2^{k +1} + 2^k$; then $l(y) = s \times 2^{k + 1} + 1$. So $x$ can be represented as $s \times 2^{k +1} + b$, where $1 \le b \le 2^k$.
    
    It is not hard to see that $\operatorname{lowbit}(x) = \operatorname{lowbit}(b)$. And because $b - \operatorname{lowbit}(b) \ge 0$,
    
    so $l(x) = x - \operatorname{lowbit}(x) + 1 = s \times 2^{k +1} + b - \operatorname{lowbit}(b) +1 \ge s \times 2^{k +1} + 1 = l(y)$, i.e. $l(y) \le l(x) \le x \le y$.
    
    So if $c[x]$ and $c[y]$ intersect, then the range $c[x]$ governs is completely contained in $c[y]$.

**Property $\boldsymbol{2}$: $\boldsymbol{c[x]}$ is properly contained in $\boldsymbol{c[x + \operatorname{lowbit}(x)]}$.**

??? note "Proof"
    Proof: let $y = x + \operatorname{lowbit}(x)$, $x = s \times 2^{k + 1} + 2^k$; then $y = (s + 1) \times 2^{k +1}$, $l(x) = s \times 2^{k + 1} + 1$.
    
    It is not hard to see that $\operatorname{lowbit}(y) \ge 2^{k + 1}$, so $l(y) = (s + 1) \times 2^{k + 1} - \operatorname{lowbit}(y) + 1 \le s \times 2^{k +1} + 1= l(x)$, i.e. $l(y) \le l(x) \le x < y$.
    
    So $c[x]$ is properly contained in $c[x + \operatorname{lowbit}(x)]$.

**Property $3$: for any $\boldsymbol{x < y < x + \operatorname{lowbit}(x)}$, $\boldsymbol{c[x]}$ and $\boldsymbol{c[y]}$ are disjoint.**

??? note "Proof"
    Proof: let $x = s \times 2^{k + 1} + 2^k$; then $y = x + b = s \times 2^{k + 1} + 2^k + b$, where $1 \le b < 2^k$.
    
    It is not hard to see that $\operatorname{lowbit}(y) = \operatorname{lowbit}(b)$. And because $b - \operatorname{lowbit}(b) \ge 0$,
    
    therefore $l(y) = y - \operatorname{lowbit}(y) + 1 = x + b - \operatorname{lowbit}(b) + 1 > x$, i.e. $l(x) \le x < l(y) \le y$.
    
    So $c[x]$ and $c[y]$ are disjoint.

With these three properties as a foundation, let's next look at the tree structure of the Fenwick tree (please ignore the edges from $a$ to $c$).

![](./images/fenwick.svg)

In fact, the tree structure of the Fenwick tree is the graph obtained by connecting an edge from $x$ to $x + \operatorname{lowbit}(x)$, where $x + \operatorname{lowbit}(x)$ is the parent of $x$.

Note that when considering the tree structure of the Fenwick tree, we do not consider the influence of the Fenwick tree's size, i.e. we consider this an infinitely large tree for convenience of analysis. In actual implementation, we only need the $c[x]$ with $x \le n$, where $n$ is the length of the original array.

This tree naturally satisfies many nice properties, several of which are listed below (let $fa[u]$ denote the direct parent of $u$):

-   $u < fa[u]$.
-   $u$ is greater than any descendant of $u$ and less than any ancestor of $u$.
-   The $\operatorname{lowbit}$ of point $u$ is strictly less than the $\operatorname{lowbit}$ of $fa[u]$.

??? note "Proof"
    Let $y = x + \operatorname{lowbit}(x)$, $x = s \times 2^{k + 1} + 2^k$; then $y = (s + 1) \times 2^{k +1}$, and it is not hard to see that $\operatorname{lowbit}(y) \ge 2^{k + 1} > \operatorname{lowbit}(x)$. Q.E.D.

-   The height of point $x$ is $\log_2\operatorname{lowbit}(x)$, i.e. the bit position of the lowest `1` in the binary of $x$.

??? note "Definition of height"
    The height $h(x)$ of point $x$ satisfies: if $x \bmod 2 = 1$, then $h(x) = 0$, otherwise $h(x) = \max(h(y)) + 1$, where $y$ denotes all children of $x$ (in this case $x$ has at least one child $x - 1$).
    
    That is, the height of a point is exactly $1$ higher than its highest child. If a point has no children, its height is $0$.
    
    We introduce the concept of height here for the convenience of explaining the complexity later.

-   $c[u]$ is properly contained in $c[fa[u]]$ (Property $2$).
-   $c[u]$ is properly contained in $c[v]$, where $v$ is any ancestor of $u$ (induction on the previous property).
-   $c[u]$ properly contains $c[v]$, where $v$ is any descendant of $u$ (the previous property with $u$, $v$ swapped).
-   For any $v' > u$, if $v'$ is not an ancestor of $u$, then $c[u]$ and $c[v']$ are disjoint.

??? note "Proof"
    Among $u$ and $u$'s ancestors, there must exist a point $v$ such that $v < v' < fa[v]$; by Property $3$, $c[v']$ is disjoint from $c[v]$, and $c[v]$ contains $c[u]$, so $c[v']$ is disjoint from $c[u]$.

-   For any $v < u$, if $v$ is not in $u$'s subtree, then $c[u]$ and $c[v]$ are disjoint (the previous property with $u$, $v'$ swapped).
-   For any $v > u$, $c[u]$ is properly contained in $c[v]$ if and only if $v$ is an ancestor of $u$ (a summary of the previous properties). This is the core principle of Fenwick-tree single-point modification.
-   Let $u = s \times 2^{k + 1} + 2^k$; then its number of children is $k = \log_2\operatorname{lowbit}(u)$, with numbers $u - 2^t(0 \le t < k)$.
    -   Example: suppose $k = 3$ and the binary number of $u$ is `...1000`; then $u$ has three children, with binary numbers `...0111`, `...0110`, `...0100`.

??? note "Proof"
    Subtracting $2^t$ from a number $x$ flips bit $t$ of $x$'s binary, while the lower bits stay unchanged.
    
    Consider a child $v$ of $u$; we have $v + \operatorname{lowbit}(v) = u$, i.e. $v = u - 2^t$ and $\operatorname{lowbit}(v) = 2^t$. Let $u = s \times 2^{k + 1} + 2^k$.
    
    **Consider $\boldsymbol{0 \le t < k}$**: bit $t$ of $u$ and below are all $0$, so bit $t$ of $v = u - 2^t$ becomes $1$ with the bits after it still $0$, which **satisfies** $\operatorname{lowbit}(v) = 2^t$.
    
    **Consider $\boldsymbol{t = k}$**: then $v = u - 2^k$, and bit $k$ of $v$ becomes $0$, which **does not satisfy** $\operatorname{lowbit}(v) = 2^t$.
    
    **Consider $\boldsymbol{t > k}$**: then $v = u - 2^t$, and bit $k$ of $v$ is $1$, so $\operatorname{lowbit}(v) = 2^k$, which **does not satisfy** $\operatorname{lowbit}(v) = 2^t$.

-   The ranges $c$ governed by all children of $u$ exactly piece together into $[l(u), u - 1]$.
    -   Example: suppose $k = 3$ and the binary number of $u$ is `...1000`; then $u$ has three children, with binary numbers `...0111`, `...0110`, `...0100`.
    -   `c[...0100]` represents `a[...0001 ~ ...0100]`.
    -   `c[...0110]` represents `a[...0101 ~ ...0110]`.
    -   `c[...0111]` represents `a[...0111 ~ ...0111]`.
    -   It is not hard to see that the union of the above three governed ranges is exactly `a[...0001 ~ ...0111]`, i.e. $[l(u), u - 1]$.

??? note "Proof"
    A child of $u$ can always be represented as $u - 2^t(0 \le t < k)$; it is not hard to see that the smaller $t$ is, the larger $u - 2^t$ is, and the more to the right the interval it represents. Let $f(t) = u - 2^t$; then $f(k - 1), f(k - 2), \ldots, f(0)$ are respectively the children of $u$ from left to right.
    
    It is not hard to see that $\operatorname{lowbit}(f(t)) = 2^t$, so $l(f(t)) = u - 2^t - 2^t + 1 = u - 2^{t + 1} + 1$.
    
    Consider two adjacent children $f(t + 1)$ and $f(t)$. The right endpoint of the former's governed interval is $f(t + 1) = u - 2^{t + 1}$, and the left endpoint of the latter's governed interval is $l(f(t)) = u - 2^{t + 1} + 1$, which connect exactly.
    
    Consider the leftmost child $f(k - 1)$; its governed left boundary $l(f(k - 1)) = u - 2^k + 1$ is exactly $l(u)$.
    
    Consider the rightmost child $f(0)$; its governed right boundary is exactly $u - 1$.
    
    Therefore, these children's governed intervals can piece together exactly into $[l(u), u - 1]$.

### Single-point modification

Now let's consider how to single-point-modify $a[x]$.

Our goal is to quickly and correctly maintain the $c$ array. To guarantee efficiency, we only need to traverse and modify all $c[y]$ that govern $a[x]$, because the other $c$ clearly do not change.

The $c[y]$ that governs $a[x]$ must contain $c[x]$ (by Property $1$), so $y$ is an ancestor of $x$ in the Fenwick tree's tree structure. Therefore we start from $x$ and keep jumping to parents until we jump beyond the length of the original array.

Let $n$ denote the size of $a$; it is not hard to write out the process of single-point-modifying $a[x]$:

-   Initially let $x' = x$.
-   Modify $c[x']$.
-   Let $x' \gets x' + \operatorname{lowbit}(x')$; if $x' > n$ it means we have jumped to the end, so terminate the loop; otherwise return to the second step.

The kind of interval information and the kind of single-point modification together determine how $c[x']$ is modified. Below are a few examples:

-   If $c[x']$ maintains the interval sum and the modification kind is adding $p$ to $a[x]$, then the modification is to also add $p$ to all $c[x']$.
-   If $c[x']$ maintains the interval product and the modification kind is multiplying $a[x]$ by $p$, then the modification is to also multiply all $c[x']$ by $p$.

However, the freedom of single-point modification makes the kind of modification and the maintained information not necessarily the same operation; for example, if $c[x']$ maintains the interval sum and the modification kind is assigning $a[x]$ the value $p$, one can consider transforming it into adding $p - a[x]$ to $a[x]$. If it is multiplying $a[x]$ by $p$, consider transforming it into adding $a[x] \times p - a[x]$ to $a[x]$.

Below we give an implementation taking maintaining the interval sum with single-point add as an example.

???+ note "Implementation"
    === "C++"
        ```cpp
        void add(int x, int k) {
          while (x <= n) {  // must not go out of bounds
            c[x] = c[x] + k;
            x = x + lowbit(x);
          }
        }
        ```
    
    === "Python"
        ```python
        def add(x, k):
            while x <= n:  # must not go out of bounds
                c[x] = c[x] + k
                x = x + lowbit(x)
        ```

### Tree building

That is, building the Fenwick tree from the initially given sequence (preprocessing all $c$).

Generally one can directly transform it into $n$ single-point modifications, with time complexity $\Theta(n \log n)$ (complexity analysis later).

For example, given the sequence $a = (5, 1, 4)$ and asked to build the tree, just treat it as single-point-adding $5$ to $a[1]$, $1$ to $a[2]$, and $4$ to $a[3]$.

There is also a $\Theta(n)$ tree-building method; see the [$\Theta(n)$ tree building](#thetan-tree-building) section on this page.

### Complexity analysis

The space complexity is obviously $\Theta(n)$.

Time complexity:

-   For the range-query operation: the whole iteration process $x \gets x - \operatorname{lowbit}(x)$ can be seen as the process of gradually changing all the $1$s in the binary of $x$ to $0$ from low to high bits, and the number of intervals split out equals the number of $1$s in the binary of $x$ (i.e. $\operatorname{popcount}(x)$). Therefore, a single query has time complexity $\Theta(\log n)$;
-   For the single-point-modification operation: when jumping to parents, the height accessed keeps strictly increasing, and always $x \le n$. Since the height of point $x$ is $\log_2\operatorname{lowbit}(x)$, the height jumped to does not exceed $\log_2n$, so the number of $c$ accessed is on the order of $\log n$. Therefore, a single single-point modification has complexity $\Theta(\log n)$.

## Range-add range-sum

Prerequisite: [prefix sum & difference](../basic/prefix-sum.md).

This problem can be solved by using two Fenwick trees to maintain the difference array.

Consider the difference array $d$ of the sequence $a$, where $d[i] = a[i] - a[i - 1]$. Since the prefix sum of the difference array is the original array, $a_i=\sum_{j=1}^i d_j$.

Likewise, we consider transforming a range-sum query into a prefix-sum query via difference. So consider querying the sum of $a[1 \ldots r]$, i.e. $\sum_{i=1}^{r} a_i$, and derive:

$$
\begin{aligned}
&\sum_{i=1}^{r} a_i\\=&\sum_{i=1}^r\sum_{j=1}^i d_j
\end{aligned}
$$

Observing this expression, it is not hard to see that each $d_j$ is added $r - j + 1$ times in total. Continue deriving:

$$
\begin{aligned}
&\sum_{i=1}^r\sum_{j=1}^i d_j\\=&\sum_{i=1}^r d_i\times(r-i+1)
\\=&\sum_{i=1}^r d_i\times (r+1)-\sum_{i=1}^r d_i\times i
\end{aligned}
$$

$\sum_{i=1}^r d_i$ cannot yield the value of $\sum_{i=1}^r d_i \times i$, so we must use two Fenwick trees to maintain the sum information of $d_i$ and $d_i \times i$ respectively.

So how do we do range add? Consider the effect on $d$ of range-adding $x$ to the original array $a[l \ldots r]$.

Because the difference is $d[i] = a[i] - a[i - 1]$,

-   $a[l]$ increases by $v$ while $a[l - 1]$ is unchanged, so the value of $d[l]$ increases by $v$.
-   $a[r + 1]$ is unchanged while $a[r]$ increases by $v$, so the value of $d[r + 1]$ decreases by $v$.
-   For any $i$ not equal to $l$ and not equal to $r+1$, $a[i]$ and $a[i - 1]$ either both did not change or both increased by $v$, and $a[i] + v - (a[i - 1] + v)$ is still $a[i] - a[i - 1]$, so the other $d[i]$ are all unchanged.

Then the maintenance is not hard to think of: for the Fenwick tree maintaining $d_i$, single-point-add $v$ at $l$ and $-v$ at $r + 1$; for the Fenwick tree maintaining $d_i \times i$, single-point-add $v \times l$ at $l$ and $-v \times (r + 1)$ at $r + 1$.

For the weaker problem, "range-add single-point-value", we only need a Fenwick tree maintaining a difference array $d_i$. To query the single-point value of $a[x]$, just compute the sum of $d[1 \ldots x]$.

Here we directly give the code for "range-add range-sum":

???+ note "Implementation"
    === "C++"
        ```cpp
        int t1[MAXN], t2[MAXN], n;
        
        int lowbit(int x) { return x & (-x); }
        
        void add(int k, int v) {
          int v1 = k * v;
          while (k <= n) {
            t1[k] += v, t2[k] += v1;
            // note: do not write t2[k] += k * v, because the value of k is no longer the index of the original array
            k += lowbit(k);
          }
        }
        
        int getsum(int *t, int k) {
          int ret = 0;
          while (k) {
            ret += t[k];
            k -= lowbit(k);
          }
          return ret;
        }
        
        void add1(int l, int r, int v) {
          add(l, v), add(r + 1, -v);  // difference the range add into two prefix adds
        }
        
        long long getsum1(int l, int r) {
          return (r + 1ll) * getsum(t1, r) - 1ll * l * getsum(t1, l - 1) -
                 (getsum(t2, r) - getsum(t2, l - 1));
        }
        ```
    
    === "Python"
        ```python
        t1 = [0] * MAXN
        t2 = [0] * MAXN
        n = 0
        
        
        def lowbit(x):
            return x & (-x)
        
        
        def add(k, v):
            v1 = k * v
            while k <= n:
                t1[k] = t1[k] + v
                t2[k] = t2[k] + v1
                k = k + lowbit(k)
        
        
        def getsum(t, k):
            ret = 0
            while k:
                ret = ret + t[k]
                k = k - lowbit(k)
            return ret
        
        
        def add1(l, r, v):
            add(l, v)
            add(r + 1, -v)
        
        
        def getsum1(l, r):
            return (
                (r) * getsum(t1, r)
                - l * getsum(t1, l - 1)
                - (getsum(t2, r) - getsum(t2, l - 1))
            )
        ```

By this principle, one should be able to implement "range-multiply range-product", "range-XOR a number, query range-XOR value", etc., as long as the maintained information and the range operation are the same operation; interested readers can try it themselves.

## Two-dimensional Fenwick tree

### Single-point modification, submatrix query

A two-dimensional Fenwick tree, also called a Fenwick tree nested inside a Fenwick tree, is used to maintain single-point modification and prefix-information problems on a two-dimensional array.

Similar to a one-dimensional Fenwick tree, we use $c(x, y)$ to denote the total information of the matrix $a(x - \operatorname{lowbit}(x) + 1, y - \operatorname{lowbit}(y) + 1) \ldots a(x, y)$, i.e. the total information of a matrix with $a(x, y)$ as the bottom-right corner, height $\operatorname{lowbit}(x)$, and width $\operatorname{lowbit}(y)$.

For single-point modification, let:

$$
f(x, i) = \begin{cases}x &i = 0\\f(x, i - 1) + \operatorname{lowbit}(f(x, i - 1)) & i > 0\\\end{cases}
$$

i.e. $f(x, i)$ is the $i$-th-level ancestor of $x$ in the Fenwick tree's tree structure (the 0th-level ancestor is itself).

Then only the elements in $c(f(x, i), f(y, j))$ govern $a(x, y)$, so when modifying $a(x, y)$ we only need to modify all $c(f(x, i), f(y, j))$ with $f(x, i) \le n$ and $f(y, j) \le m$.

??? note "Correctness proof"
    $c(p, q)$ governs $a(x, y)$; find the range of $p$ and $q$.
    
    Consider a one-dimensional Fenwick tree $c_1$ of size $n$ (corresponding to the original array $a_1$) and a one-dimensional Fenwick tree $c_2$ of size $m$ (corresponding to the original array $a_2$).
    
    Then the proposition is equivalent to: the condition that $c_1(p)$ governs $a_1[x]$ and $c_2(q)$ governs $a_2[y]$.
    
    That is, in the Fenwick tree's tree structure, $p$ is a point among $x$ and its ancestors, and $q$ is a point among $y$ and its ancestors.
    
    So $p = f(x, i)$, $q = f(y, j)$.

For the query, we let:

$$
g(x, i) = \begin{cases}x &i = 0\\g(x, i - 1) - \operatorname{lowbit}(g(x, i - 1)) & i, g(x, i - 1) > 0\\0&\text{otherwise.}\end{cases}
$$

Then merge all $c(g(x, i), g(y, j))$ with $g(x, i), g(y, j) > 0$.

??? note "Correctness proof"
    Let $\circ$ denote the operator that merges two pieces of information (for example, if the information is the interval sum, then $\circ = +$).
    
    Consider a one-dimensional Fenwick tree $c_1$; $c_1[g(x, 0)] \circ c_1[g(x, 1)] \circ c_1[g(x, 2)] \circ \cdots$ exactly represents the interval information of $[1 \ldots x]$ on the original array.
    
    Similarly, let $t(x) = c(x, g(y, 0)) \circ c(x, g(y, 1)) \circ c(x, g(y, 2)) \circ \cdots$; then $t(x)$ exactly represents the information of the matrix $a(x - \operatorname{lowbit}(x) + 1, 1) \ldots a(x, y)$.
    
    Again similarly, $t(g(x, 0)) \circ t(g(x, 1)) \circ t(g(x, 2)) \circ \cdots$ represents the information of the matrix $a(1, 1) \ldots a(x, y)$.
    
    In fact, if the function $t(x)$ here is seen as a Fenwick tree, it is equivalent to a Fenwick tree nested inside a Fenwick tree, which is the origin of the name "Fenwick tree nested inside a Fenwick tree".

Below we give the code for single-point add and querying the submatrix sum.

???+ note "Implementation"
    === "Single-point add"
        ```cpp
        void add(int x, int y, int v) {
          for (int i = x; i <= n; i += lowbit(i)) {
            for (int j = y; j <= m; j += lowbit(j)) {
              // note: here we must create loop variables; we cannot directly use while (x <= n) as in the one-dimensional case
              c[i][j] += v;
            }
          }
        }
        ```
    
    === "Query submatrix sum"
        ```cpp
        int sum(int x, int y) {
          int res = 0;
          for (int i = x; i > 0; i -= lowbit(i)) {
            for (int j = y; j > 0; j -= lowbit(j)) {
              res += c[i][j];
            }
          }
          return res;
        }
        
        int ask(int x1, int y1, int x2, int y2) {
          // query the submatrix sum
          return sum(x2, y2) - sum(x2, y1 - 1) - sum(x1 - 1, y2) + sum(x1 - 1, y1 - 1);
        }
        ```

### Submatrix add, query submatrix sum

Prerequisite: [prefix sum & difference](../basic/prefix-sum.md) and the [range-add range-sum](#range-add-range-sum) section on this page.

Similar to the "range-add range-sum" problem of a one-dimensional Fenwick tree, consider maintaining a difference array.

The difference array on a two-dimensional array is like this:

$$
d(i, j) = a(i, j) - a(i - 1, j) - a(i, j - 1) + a(i - 1, j - 1).
$$

??? note "Why define it this way?"
    This is because, in the ideal prescribed state, doing a two-dimensional prefix sum on the difference matrix should give the original matrix, since these are a pair of inverse operations.
    
    The formula for a two-dimensional prefix sum is:
    
    $s(i, j) = s(i - 1, j) + s(i, j - 1) - s(i - 1, j - 1) + a(i, j)$.
    
    So, letting $a$ be the original array and $d$ the difference array:
    
    $a(i, j) = a(i - 1, j) + a(i, j - 1) - a(i - 1, j - 1) + d(i, j)$
    
    Rearranging gives the formula for the two-dimensional difference.
    
    $d(i, j) = a(i, j) - a(i - 1, j) - a(i, j - 1) + a(i - 1, j - 1)$.

This way, range-adding $v$ to the submatrix with top-left corner $(x_1, y_1)$ and bottom-right corner $(x_2, y_2)$ is equivalent to, on the difference array, single-point-adding $v$ to $d(x_1, y_1)$ and $d(x_2 + 1, y_2 + 1)$ respectively, and single-point-adding $-v$ to $d(x_2 + 1, y_1)$ and $d(x_1, y_2 + 1)$ respectively.

As for the reason, express these four $d$ using the definition formula and analyze the change of each term.

Let's give an example: with the initial difference array being $0$, after adding $v$ to the submatrix $a(2, 2) \ldots a(3, 4)$, the difference array becomes:

$$
\begin{pmatrix}0&0&0&0&0\\0&v&0&0&-v\\0&0&0&0&0\\0&-v&0&0&v\end{pmatrix}
$$

(Here the submatrix $a(2, 2) \ldots a(3, 4)$ is exactly the $2 \times 3$ matrix located in the center above.)

Therefore, the way to do submatrix add is: transform it into four single-point-add operations on the difference array.

Now consider querying the submatrix sum:

For a point $(x, y)$, its two-dimensional prefix sum can be represented as:

$$
\sum_{i = 1}^x\sum_{j = 1}^y\sum_{h = 1}^i\sum_{k = 1}^j d(h, k)
$$

The reason is that the prefix sum of the prefix sum of the difference is the original prefix sum.

Similar to the "range-add range-sum" problem of a one-dimensional Fenwick tree, count the number of occurrences of $d(h, k)$, which is $(x - h + 1) \times (y - k + 1)$.

Then continue deriving:

$$
\begin{aligned}
&\sum_{i = 1}^x\sum_{j = 1}^y\sum_{h = 1}^i\sum_{k = 1}^j d(h, k)
\\=&\sum_{i = 1}^x\sum_{j = 1}^y d(i, j) \times (x - i + 1) \times (y - j + 1)
\\=&\sum_{i = 1}^x\sum_{j = 1}^y d(i, j) \times (xy + x + y + 1) - d(i, j) \times i \times (y + 1) - d(i, j) \times j \times (x + 1) + d(i, j) \times i \times j
\end{aligned}
$$

So we need to maintain four Fenwick trees, maintaining the sum information of $d(i, j)$, $d(i, j) \times i$, $d(i, j) \times j$, and $d(i, j) \times i \times j$ respectively.

Of course, similar to the one-dimensional case, if we only need submatrix add and single-point-value query, maintaining one difference array and then querying the prefix sum suffices.

Below we give the code:

???+ note "Implementation"
    ```cpp
    using ll = long long;
    ll t1[N][N], t2[N][N], t3[N][N], t4[N][N];
    
    void add(ll x, ll y, ll z) {
      for (int X = x; X <= n; X += lowbit(X))
        for (int Y = y; Y <= m; Y += lowbit(Y)) {
          t1[X][Y] += z;
          t2[X][Y] += z * x;  // note it is z * x, not z * X; likewise below
          t3[X][Y] += z * y;
          t4[X][Y] += z * x * y;
        }
    }
    
    void range_add(ll xa, ll ya, ll xb, ll yb,
                   ll z) {  // the submatrix from (xa, ya) to (xb, yb)
      add(xa, ya, z);
      add(xa, yb + 1, -z);
      add(xb + 1, ya, -z);
      add(xb + 1, yb + 1, z);
    }
    
    ll ask(ll x, ll y) {
      ll res = 0;
      for (int i = x; i; i -= lowbit(i))
        for (int j = y; j; j -= lowbit(j))
          res += (x + 1) * (y + 1) * t1[i][j] - (y + 1) * t2[i][j] -
                 (x + 1) * t3[i][j] + t4[i][j];
      return res;
    }
    
    ll range_ask(ll xa, ll ya, ll xb, ll yb) {
      return ask(xb, yb) - ask(xb, ya - 1) - ask(xa - 1, yb) + ask(xa - 1, ya - 1);
    }
    ```

## Weighted Fenwick tree and its applications

We know that an ordinary Fenwick tree is built directly on the original sequence, and $c_6$ represents the interval information of $a[5 \ldots 6]$.

However, in fact, we can also build a Fenwick tree on the weight array of the original sequence, which is a weighted Fenwick tree.

??? note "What is a weight array?"
    The weight array $b$ of a sequence $a$ satisfies that the value of $b[x]$ is the number of occurrences of $x$ in $a$.
    
    For example, the weight array of $a = (1, 3, 4, 3, 4)$ is $b = (1, 0, 2, 2)$.
    
    Clearly, the size of $b$ is related to the value range of $a$.
    
    If the value range of the original sequence is too large, and what matters is not the specific values but the relative magnitude relationship between values, one often [discretizes](../misc/discrete.md) the original array before building the weight array.
    
    In addition, the weight array is a representation of the original array's unorderedness: it focuses on describing the element content of the array while ignoring the order of the array; if two arrays differ only in order but have the same content, then their weight arrays are the same.
    
    Therefore, for problems where the order of the given array does not affect the answer, thinking on the basis of the weight array is generally more intuitive, such as [\[NOIP2021\] Sequence](https://www.luogu.com.cn/problem/P7961).

Using a weighted Fenwick tree, we can solve some classic problems.

### Single-point modification, query the global $k$-th smallest

Here we only discuss the $k$-th smallest; the $k$-th largest problem can be transformed into the $k$-th smallest problem by simple computation.

This problem can be discretized; if the value range of the original sequence $a$ is too large, discretize before building the weight array $b$. Note that the values involved in the single-point modification must also be discretized together, not just the elements in the original array $a$.

For single-point modification, we only need to transform the single-point modification on the original sequence into a single-point modification on the weight array. Specifically, modifying $a[x]$ of the original array from $y$ to $z$ is transformed into single-point modification of the weight array $b$: single-point-subtract $1$ from $b[y]$ and single-point-add $1$ to $b[z]$.

For querying the $k$-th smallest, consider binary-searching $x$ and querying the prefix sum of $[1, x]$ in the weight array, finding $x_0$ such that the prefix sum of $[1, x_0]$ is $< k$ while the prefix sum of $[1, x_0 + 1]$ is $\ge k$; then the $k$-th largest number is $x_0 + 1$ (note: here the prefix sum of $[1, 0]$ is considered $0$).

The time complexity of doing this is $\Theta(\log^2n)$.

Consider replacing binary search with binary lifting.

Let $x = 0$, $\mathrm{sum} = 0$, and enumerate $i$ from $\log_2n$ down to $0$:

-   Query the interval sum $t$ of $[x + 1 \ldots x + 2^i]$ in the weight array.
-   If $\mathrm{sum} + t < k$, the extension succeeds, $x \gets x + 2^i$, $\mathrm{sum} \gets \mathrm{sum} + t$; otherwise the extension fails, do nothing.

The $x$ obtained this way is the maximum satisfying that the prefix sum of $[1 \ldots x]$ is $< k$, so the final $x + 1$ is the answer.

This method seems to have no improvement in time efficiency, but in fact, querying the interval sum of $[x + 1 \ldots x + 2^i]$ only needs to access the value of $c[x + 2^i]$.

The reason is simple: consider $\operatorname{lowbit}(x + 2^i)$; it must be $2^i$, because $x$ has previously only accumulated $2^j$ with $j > i$. So the interval $c[x + 2^i]$ represents is exactly $[x + 1 \ldots x + 2^i]$.

Thus, the time complexity is reduced to $\Theta(\log n)$.

???+ note "Implementation"
    === "C++"
        ```cpp
        // weighted Fenwick tree, query the k-th smallest
        int kth(int k) {
          int sum = 0, x = 0;
          for (int i = log2(n); ~i; --i) {
            x += 1 << i;                   // try to extend
            if (x > n || sum + t[x] >= k)  // if the extension fails
              x -= 1 << i;
            else
              sum += t[x];
          }
          return x + 1;  // if not found, return n + 1
        }
        ```
    
    === "Python"
        ```python
        # weighted Fenwick tree, query the k-th smallest
        def kth(k):
            sum = 0
            x = 0
            i = int(log2(n))
            while ~i:
                x = x + (1 << i)  # try to extend
                if x > n or sum + t[x] >= k:  # if the extension fails
                    x = x - (1 << i)
                else:
                    sum = sum + t[x]
                i = i - 1
            return x + 1  # if not found, return n + 1
        ```

### Global inversions (global 2D dominance)

Related reading and reference implementation: [Inversions](../math/permutation.md#逆序数)

Global inversions can also be cleverly solved with a weighted Fenwick tree. The problem is: given a sequence $a$ of length $n$, find the number of pairs $(i, j)$ in $a$ with $i < j$ and $a[i] > a[j]$.

This problem can be discretized; if the value range of the original sequence $a$ is too large, discretize before building the weight array $b$.

We consider enumerating $i$ in reverse order from $n$ to $1$, as the index of the first element in the inversion, then computing how many $j > i$ satisfy $a[j] < a[i]$, and finally accumulating the answer.

In fact, we only need to do this (let the current $a[i] = x$):

-   Query the prefix sum of $b[1 \ldots x - 1]$, which is the number of inversions with left endpoint $a[i]$.
-   Increment $b[x]$ by $1$;

The reason is very natural: the elements appearing in $b[1 \ldots x-1]$ must be smaller than the current $x = a[i]$, and the reverse-order enumeration of $i$ naturally makes these elements already in the weight array have an index $j$ in the original array greater than the current index $i$.

Illustrate with an example, $a = (4, 3, 1, 2, 1)$.

Scan $i$ from $5 \to 1$:

-   $a[5] = 1$, query the prefix sum of $b[1 \ldots 0]$, which is $0$, increment $b[1]$ by $1$, $b = (1, 0, 0, 0)$.
-   $a[4] = 2$, query the prefix sum of $b[1 \ldots 1]$, which is $1$, increment $b[2]$ by $1$, $b = (1, 1, 0, 0)$.
-   $a[3] = 1$, query the prefix sum of $b[1 \ldots 0]$, which is $0$, increment $b[1]$ by $1$, $b = (2, 1, 0, 0)$.
-   $a[2] = 3$, query the prefix sum of $b[1 \ldots 2]$, which is $3$, increment $b[3]$ by $1$, $b = (2, 1, 1, 0)$.
-   $a[1] = 4$, query the prefix sum of $b[1 \ldots 3]$, which is $4$, increment $b[4]$ by $1$, $b = (2, 1, 1, 1)$.

So the final answer is $0 + 1 + 0 + 3 + 4 = 8$.

Note that after traversing $i$, the two steps of querying $b[1 \ldots x - 1]$ and incrementing $b[x]$ can be swapped, becoming first incrementing $b[x]$ and then querying $b[1 \ldots x - 1]$, without affecting the answer. Two perspectives to explain:

-   The modification of $b[x]$ does not affect the query of $b[1 \ldots x - 1]$.
-   After swapping, it is essentially querying the number of pairs with $i \le j$ and $a[i] > a[j]$, and when $i = j$ there is no $a[i] > a[j]$, so $i \le j$ is equivalent to $i < j$, so this is equivalent to the original inversion problem.

If we query the number of non-strict inversions ($i < j$ and $a[i] \ge a[j]$), then we must change to querying the sum of $b[1 \ldots x]$, and in this case the two steps cannot be swapped; again two perspectives to explain:

-   The modification of $b[x]$ **affects** the query of $b[1 \ldots x]$.
-   After swapping, it is essentially querying the number of pairs with $i \le j$ and $a[i] \ge a[j]$, and when $i = j$ we always have $a[i] \ge a[j]$, so $i \le j$ is **not equivalent** to $i < j$, and it is **not equivalent** to the original problem.

If we query the number of pairs with $i \le j$ and $a[i] \ge a[j]$, then these two steps must be swapped.

In addition, for the original inversion problem, there is another approach of enumerating $j$ forward and querying how many $i < j$ satisfy $a[i] > a[j]$. The approach is as follows (let $x = a[j]$):

-   Query the interval sum of $b[x + 1 \ldots V]$ (where $V$ is the size of $b$, i.e. the value range of $a$ (or the value range after discretization)).
-   Increment $b[x]$ by $1$.

Reason: the elements appearing in $b[x + 1 \ldots V]$ must be larger than the current $x = a[j]$, and the forward-order enumeration of $j$ naturally makes these elements already in the weight array have an index $i$ in the original array smaller than the current index $j$.

In addition, counting inversions can also be solved with [merge sort](../basic/merge-sort.md#inversions). This method can avoid discretization. The time complexity is likewise $O(n\log n)$. Reference implementations of both algorithms are in the [Inversions](../math/permutation.md#逆序数) section.

## Maintaining non-differenceable information with a Fenwick tree

Such as maintaining range extrema.

Note that although this method has a small amount of code, the time complexity of both single-point modification and range query is $\Theta(\log^2n)$, worse than the $\Theta(\log n)$ time complexity of using a segment tree.

### Range query

We still base it on the previous idea, jumping from $r$ backward along $\operatorname{lowbit}$, but we cannot jump to the left of $l$.

Therefore, if we jump to $c[x]$, first check whether the next $x - \operatorname{lowbit}(x)$ to jump to is less than $l$:

-   If it is less than $l$, we directly merge the **single point $\boldsymbol{a[x]}$** into the total information and then jump to $c[x - 1]$.
-   If it is greater than or equal to $l$, it means we did not go out of bounds, so normally merge $c[x]$ and then jump to $c[x - \operatorname{lowbit}(x)]$.

Below we give code taking range-maximum query as an example:

???+ note "Implementation"
    ```cpp
    int getmax(int l, int r) {
      int ans = 0;
      while (r >= l) {
        ans = max(ans, a[r]);
        --r;
        for (; r - lowbit(r) >= l; r -= lowbit(r)) {
          // note: do not write the loop condition as r - lowbit(r) + 1 >= l
          // otherwise when l = 1, r jumping to 0 causes an infinite loop
          ans = max(ans, C[r]);
        }
      }
      return ans;
    }
    ```

It can be proven that the time complexity of the above algorithm is $\Theta(\log^2n)$.

??? note "Time-complexity proof"
    Consider the highest bit where $r$ and $l$ differ; there must be $r$ having a $1$ at this bit and $l$ having a $0$ at this bit (because $r \ge l$).
    
    If $r$ still has a $1$ after this bit, then there must be $r - \operatorname{lowbit}(r) \ge l$, so the next step must fill the lowest $1$ of $r$ with $0$;
    
    If this $1$ of $r$ is exactly the lowest $1$ of $r$, then whether it is $r \gets r - \operatorname{lowbit}(r)$ or $r \gets r - 1$, this $1$ of $r$ must become $0$.
    
    Therefore, after at most $\log n$ transformations of $r$, the highest bit where $r$ and $l$ differ must be able to descend by one. So the total time complexity is $\Theta(\log^2n)$.

### Single-point update

???+ note "Note"
    Please first understand the following two properties of the Fenwick tree's tree structure before studying this section.
    
    -   Let $u = s \times 2^{k + 1} + 2^k$; then its number of children is $k = \log_2\operatorname{lowbit}(u)$, with numbers $u - 2^t(0 \le t < k)$.
    -   The ranges $c$ governed by all children of $u$ exactly piece together into $[l(u), u - 1]$.
    
    The meaning and proofs of these two properties can both be found in the [Properties of the Fenwick tree and its tree structure](#properties-of-the-fenwick-tree-and-its-tree-structure) section on this page.

After updating $a[x]$, we only need to update the $c[y]$ where $y$ is an ancestor of $x$ in the Fenwick tree's tree structure.

For extrema (taking the maximum as an example), a common wrong idea is: if $a[x]$ is modified to $p$, then update all $c[y]$ to $\max(c[y], p)$. Here is a counterexample: in $(1, 2, 3, 4, 5)$, modifying $5$ to $4$, the maximum is $4$, but the above modification would give $5$. Directly modifying $c[y]$ to $p$ is also wrong; a counterexample is modifying the $3$ in the above example to $4$.

In fact, for non-differenceable information, there is no way to directly modify $c[y]$ via $p$. This is because the modification itself is equivalent to "removing" the old number from the original interval and then adding a new number. The effect of "removing" on the interval information is equivalent to doing the "inverse operation", and non-differenceable information has no "inverse operation", so $c[y]$ cannot be directly modified.

In other words, for each affected $c[y]$, we must reconstruct the information of this interval.

Consider the children of $c[y]$; their information must be correct (because we update the children before the parent), and these children exactly compose the governed interval $[l(y), y - 1]$, so merging one more single point $a[y]$ gives $[l(y), y]$, i.e. $c[y]$. This way, we can reconstruct and merge each $c$ that needs modification using at most $\log n$ intervals.

???+ note "Implementation"
    ```cpp
    void update(int x, int v) {
      a[x] = v;
      for (int i = x; i <= n; i += lowbit(i)) {
        // enumerate the affected intervals
        C[i] = a[i];
        for (int j = 1; j < lowbit(i); j *= 2) {
          C[i] = max(C[i], C[i - j]);
        }
      }
    }
    ```

It is easy to see that the time complexity of the above algorithm is $\Theta(\log^2n)$.

### Tree building

One can consider splitting it into $n$ single-point modifications, building the tree in $\Theta(n\log^2n)$.

There is also a $\Theta(n)$ tree-building method; see Method 1 in the [$\Theta(n)$ tree building](#thetan-tree-building) section on this page.

## Tricks

### $\Theta(n)$ tree building

Take maintaining the interval sum as an example.

Method 1:

The value of each node is obtained by summing the values of all children directly connected to itself. So we can consider the contribution in reverse, i.e. each time after determining a child's value, use its own value to update its own direct parent.

???+ note "Implementation"
    === "C++"
        ```cpp
        // Θ(n) tree building
        void init() {
          for (int i = 1; i <= n; ++i) {
            t[i] += a[i];
            int j = i + lowbit(i);
            if (j <= n) t[j] += t[i];
          }
        }
        ```
    
    === "Python"
        ```python
        # Θ(n) tree building
        def init():
            for i in range(1, n + 1):
                t[i] = t[i] + a[i]
                j = i + lowbit(i)
                if j <= n:
                    t[j] = t[j] + t[i]
        ```

Method 2:

Earlier we mentioned that the interval $c[i]$ represents is $[i-\operatorname{lowbit}(i)+1, i]$, so we can first preprocess a $\mathrm{sum}$ prefix-sum array and then compute the $c$ array.

???+ note "Implementation"
    === "C++"
        ```cpp
        // Θ(n) tree building
        void init() {
          for (int i = 1; i <= n; ++i) {
            t[i] = sum[i] - sum[i - lowbit(i)];
          }
        }
        ```
    
    === "Python"
        ```python
        # Θ(n) tree building
        def init():
            for i in range(1, n + 1):
                t[i] = sum[i] - sum[i - lowbit(i)]
        ```

### Timestamp optimization

A very common technique for dealing with multiple test cases. If each time new data is input the Fenwick tree is brute-force cleared, it may cause a timeout. Therefore, use a $\mathrm{tag}$ to store the last time the current node was used (i.e. which test case most recently used it). Each operation checks whether the time in the $\mathrm{tag}$ of this position is the same as the current time, so as to determine whether this position should be $0$ or the value in the array.

???+ note "Implementation"
    === "C++"
        ```cpp
        // timestamp optimization
        int tag[MAXN], t[MAXN], Tag;
        
        void reset() { ++Tag; }
        
        void add(int k, int v) {
          while (k <= n) {
            if (tag[k] != Tag) t[k] = 0;
            t[k] += v, tag[k] = Tag;
            k += lowbit(k);
          }
        }
        
        int getsum(int k) {
          int ret = 0;
          while (k) {
            if (tag[k] == Tag) ret += t[k];
            k -= lowbit(k);
          }
          return ret;
        }
        ```
    
    === "Python"
        ```python
        # timestamp optimization
        tag = [0] * MAXN
        t = [0] * MAXN
        Tag = 0
        
        
        def reset():
            Tag = Tag + 1
        
        
        def add(k, v):
            while k <= n:
                if tag[k] != Tag:
                    t[k] = 0
                t[k] = t[k] + v
                tag[k] = Tag
                k = k + lowbit(k)
        
        
        def getsum(k):
            ret = 0
            while k:
                if tag[k] == Tag:
                    ret = ret + t[k]
                k = k - lowbit(k)
            return ret
        ```

## Examples

-   [Fenwick Tree 1: Single-Point Modification, Range Query](https://loj.ac/problem/130)
-   [Fenwick Tree 2: Range Modification, Single-Point Query](https://loj.ac/problem/131)
-   [Fenwick Tree 3: Range Modification, Range Query](https://loj.ac/problem/132)
-   [2D Fenwick Tree 1: Single-Point Modification, Range Query](https://loj.ac/problem/133)
-   [2D Fenwick Tree 2: Range Modification, Single-Point Query](https://loj.ac/problem/134)
-   [2D Fenwick Tree 3: Range Modification, Range Query](https://loj.ac/problem/135)
