author: ouuan, Ir1d, Marcythm, Xeonacid

## Ways of tree blocking

You can refer to [true Mo's algorithm on a tree](../misc/mo-algo-on-tree.md).

You can also refer to [ouuan's blog / Detailed explanation of Mo's algorithm, Mo's algorithm with modification, Mo's algorithm on a tree / Mo's algorithm on a tree](https://ouuan.github.io/莫队、带修莫队、树上莫队详解/#树上莫队).

Mo's algorithm on a tree can likewise refer to the above two articles.

## Applications of tree blocking

Besides its application in Mo's algorithm, tree blocking can also be flexibly applied to some tree problems. But problems that can be solved with tree blocking often have better approaches, so there are relatively few related problems.

By the way, the tree-blocking approach to "gty's Girl Tree" can be broken by a star graph.

### [BZOJ4763 Xuehui](https://hydro.ac/p/bzoj-P4763)

First perform tree blocking, then for the key points of each block, preprocess the bitset of colors on the path from it to each key point among its ancestors, as well as the nearest key-point ancestor of each key point; the complexity is $O(n\sqrt n+\frac{nc}{32})$, where $n\sqrt n$ is the complexity of brute-force jumping upward from each key point, and $\frac{nc}{32}$ is the complexity of storing the $O(n)$ `bitset`s.

When answering a query, first brute-force jump from the endpoints of the path to the key point of the block they are in, then jump upward block by block from the key point of the block they are in, until the block where $lca$ is, then brute-force jump to $lca$. The `bitset`s between key points are already preprocessed, and the rest is computed during the brute-force jumping process. The complexity of a single query is $O(\sqrt n+\frac c{32})$, where $\sqrt n$ is the complexity of brute-force jumping within a block and jumping directly upward by block, and $O(\frac c{32})$ is the complexity of merging the preprocessed result with the brute-force-jumping result. Counting the number of colors can use the `count()` of `bitset`, and finding $\operatorname{mex}$ can use the `_Find_first()` of `bitset`.

So, the total complexity is $O((n+m)(\sqrt n+\frac c{32}))$.

??? note "Reference code"
    ```cpp
    --8<-- "docs/ds/code/tree-decompose/tree-decompose_1.cpp"
    ```

### [BZOJ4812 Yinuo Plays Poker](https://hydro.ac/p/bzoj-P4812)

This problem is basically the same as the previous one; the only difference is how to compute the answer after obtaining the `bitset`.

~~Since BZOJ computes the total time limit of all test points, which is hard to break, one can use `_Find_next()` to scrape by.~~

The intended solution is to compute every $16$ bits together, first preprocessing, for the $2^{16}$ possible cases, the number of consecutive $1$s in the high bits, the number of consecutive $1$s in the low bits, and the contribution in the middle. Except that this requires hand-writing `bitset`, because the standard library's `bitset` cannot take a certain $16$ bits……

The code can refer to [this blog](https://www.cnblogs.com/FallDream/p/bzoj4763.html).
