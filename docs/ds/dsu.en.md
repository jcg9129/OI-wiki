author: HeRaNO, JuicyMio, Xeonacid, sailordiary, ouuan, Pig-Eat-Earth

![](images/disjoint-set.svg)

## Introduction

A disjoint-set union (DSU) is a data structure for managing which set elements belong to, implemented as a forest where each tree represents a set and the nodes in a tree represent the elements in the corresponding set.

As the name suggests, a DSU supports two operations:

-   Unite: merge the sets that two elements belong to (merge the corresponding trees).
-   Find: query which set an element belongs to (query the root of the corresponding tree); this can be used to determine whether two elements belong to the same set.

After modification, a DSU can support deletion or movement of a single element, or maintaining edge weights on the tree. Using a dynamically-allocated segment tree, one can also implement a [persistent DSU](./persistent-seg.md#extension-persistent-dsu-based-on-the-chairman-tree).

???+ warning "Warning"
    A DSU cannot implement the separation of sets with a low complexity.

## Initialization

Initially, each element is in a separate set, represented as a tree with only a root node. For convenience, we set the root node's parent to itself.

???+ example "Implementation"
    === "C++"
        ```cpp
        struct dsu {
          vector<size_t> pa;
        
          explicit dsu(size_t size) : pa(size) { iota(pa.begin(), pa.end(), 0); }
        };
        ```
    
    === "Python"
        ```python
        class Dsu:
            def __init__(self, size):
                self.pa = list(range(size))
        ```

## Find

We need to move up the tree until we find the root node.

![](images/disjoint-set-find.svg)

???+ example "Implementation"
    === "C++"
        ```cpp
        size_t dsu::find(size_t x) { return pa[x] == x ? x : find(pa[x]); }
        ```
    
    === "Python"
        ```python
        def find(self, x):
            return x if self.pa[x] == x else self.find(self.pa[x])
        ```

### Path compression

Every element passed during the find belongs to that set, so we can connect it directly to the root node to speed up subsequent finds.

![](images/disjoint-set-compress.svg)

???+ example "Implementation"
    === "C++"
        ```cpp
        size_t dsu::find(size_t x) { return pa[x] == x ? x : pa[x] = find(pa[x]); }
        ```
    
    === "Python"
        ```python
        def find(self, x):
            if self.pa[x] != x:
                self.pa[x] = self.find(self.pa[x])
            return self.pa[x]
        ```

## Unite

To merge two trees, we only need to connect the root of one tree to the root of the other.

![](images/disjoint-set-merge.svg)

???+ example "Implementation"
    === "C++"
        ```cpp
        void dsu::unite(size_t x, size_t y) { pa[find(x)] = find(y); }
        ```
    
    === "Python"
        ```python
        def unite(self, x, y):
            self.pa[self.find(x)] = self.find(y)
        ```

### Heuristic merging

When merging, which tree's root is chosen as the new tree's root affects the complexity of future operations. We can connect the tree with fewer nodes or smaller depth onto the other, to avoid degeneration.

??? note "Detailed complexity discussion"
    Since the only operations we need to support are merging and querying of sets, when we need to combine two sets into one, connecting either set below the other gives the correct result. But different connection methods have differences in time complexity. Specifically, if we connect a set tree with both fewer points and smaller depth below a larger set tree, then clearly, compared with the other connection scheme, subsequent find operations take less time (and it also gives a better worst-case time complexity).
    
    Of course, we cannot always encounter a set exactly as described above—with both fewer points and smaller depth. Since both features, point count and depth, are easy to maintain, we often choose one of them as the estimation function. And whichever we choose, the time complexity is $O (m\alpha(m,n))$; for the specific proof, see the paper cited in the References.
    
    In actual competitive-programming code, even without heuristic merging, the code can often complete the task within the time limit. In Tarjan's paper[^tarjan1984worst], it is proven that the worst-case time complexity without heuristic merging, using only path compression, is $O (m \log n)$. In Andrew Yao's paper[^yao1985expected], it is proven that without heuristic merging, using only path compression, in the average case, the time complexity is still $O (m\alpha(m,n))$.
    
    If only heuristic merging is used, without path compression, the time complexity is $O(m\log n)$. Since a single merge with path compression may cause a large number of modifications, sometimes path compression is not suitable. For example, in a persistent DSU or in segment-tree divide-and-conquer + DSU, a DSU with only heuristic merging is generally used.

Reference implementation of merging by node count (note that the initialization method needs to be adjusted):

???+ example "Implementation"
    === "C++"
        ```cpp
        struct dsu {
          vector<size_t> pa, size;
        
          explicit dsu(size_t size_) : pa(size_), size(size_, 1) {
            iota(pa.begin(), pa.end(), 0);
          }
        
          void unite(size_t x, size_t y) {
            x = find(x), y = find(y);
            if (x == y) return;
            if (size[x] < size[y]) swap(x, y);
            pa[y] = x;
            size[x] += size[y];
          }
        };
        ```
    
    === "Python"
        ```python
        class Dsu:
            def __init__(self, size):
                self.pa = list(range(size))
                self.size = [1] * size
        
            def unite(self, x, y):
                x, y = self.find(x), self.find(y)
                if x == y:
                    return
                if self.size[x] < self.size[y]:
                    x, y = y, x
                self.pa[y] = x
                self.size[x] += self.size[y]
        ```

## Reference implementation

The complete implementation of a DSU with path compression and merging by node count is shown below:

??? example "Reference implementation of the template problem [Luogu P3367 【Template】DSU](https://www.luogu.com.cn/problem/P3367)"
    === "C++"
        ```cpp
        --8<-- "docs/ds/code/dsu/dsu_0.cpp"
        ```
    
    === "Python"
        ```python
        --8<-- "docs/ds/code/dsu/dsu_0.py"
        ```

## Complexity

After using both path compression and heuristic merging, the average time of each operation of a DSU is only $O(\alpha(n))$, where $\alpha$ is the inverse of the Ackermann function and grows extremely slowly. That is, the average running time of a single DSU operation can be considered a very small constant. The proof of the time complexity is on [this page](./dsu-complexity.md).

???+ info "The inverse Ackermann function"
    The [Ackermann function](https://en.wikipedia.org/wiki/Ackermann_function) $A(m, n)$ is defined as follows:
    
    $A(m, n) = \begin{cases}n+1&\text{if }m=0\\A(m-1,1)&\text{if }m>0\text{ and }n=0\\A(m-1,A(m,n-1))&\text{otherwise}\end{cases}$
    
    And the inverse Ackermann function $\alpha(n)$ is defined as the inverse of the Ackermann function, i.e. the largest integer $m$ such that $A(m, m) \leqslant n$.

The space complexity of a DSU is obviously $O(n)$.

## Extended operations

On the basis of the ordinary DSU, one can make a series of modifications to make it support more operations or maintain more complex information.

### DSU with deletion

An ordinary DSU cannot support the deletion operation, because when deleting a node, it inevitably deletes all nodes in the subtree rooted at it. To solve this problem, in a DSU with deletion, one can, by establishing virtual points, guarantee that all nodes that actually store data are always leaf nodes. To this end, at initialization time, establish a virtual point for each data node and set the data node's parent to that virtual point. Since each merge of two sets only connects the two sets' roots, from beginning to end only virtual points have children. This guarantees that deleting a node does not accidentally delete other nodes.

Note that after deleting a single node, one needs to re-establish a virtual point as that node's parent; otherwise, subsequent merge and delete operations cannot be executed correctly.

??? example "Reference implementation of the template problem [SPOJ JMFILTER - Junk-Mail Filter](https://www.spoj.com/problems/JMFILTER/)"
    === "C++"
        ```cpp
        --8<-- "docs/ds/code/dsu/dsu_4.cpp"
        ```
    
    === "Python"
        ```python
        --8<-- "docs/ds/code/dsu/dsu_4.py"
        ```

A similar method can also be used to implement moving a single element between sets. See the example for implementation details.

### Weighted DSU

We can also define some kind of weight on the edges of a DSU and the operation this weight undergoes during path compression, thereby solving more problems. For example, for the classic "NOI2001" Food Chain, we can maintain an additive group modulo $3$ on the edge weights. For this kind of problem of maintaining edge weights modulo a small modulus, one can also solve it by splitting a single point of the DSU into multiple states. This technique in this special case is also called "categorical DSU" or "extended-domain DSU". Later we will illustrate these approaches with examples.

To maintain the edge weights in a DSU, one needs to push the edge weights down to be stored in the child nodes. Therefore, each node stores the edge weight between it and its parent. Only when a node's parent changes does the edge weight need to be adjusted accordingly. In general, this may happen during path compression and when merging two nodes. For example, if the edge weight is the distance between the current node and its parent, then during path compression, each time the current node's parent is replaced by the root, the distance from the parent to the root needs to be added to the edge weight stored by the current node; similarly, when merging the sets the two nodes are in, the weight of the newly connected edge between the two roots needs to be computed.

??? example "Reference implementation of the template problem [Library Checker - Unionfind with Potential](https://judge.yosupo.jp/problem/unionfind_with_potential)"
    === "C++"
        ```cpp
        --8<-- "docs/ds/code/dsu/dsu_5.cpp"
        ```
    
    === "Python"
        ```python
        --8<-- "docs/ds/code/dsu/dsu_5.py"
        ```

## Examples

In competitive programming, problems that directly examine the DSU mostly require designing a special structure for the problem.

???+ example "[UVa11987 Almost Union-Find](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=229&page=show_problem&problem=3138)"
    Implement a DSU-like data structure supporting the following operations:
    
    1.  Merge the sets that two elements belong to.
    2.  Move a single element into the set that another element is in.
    3.  Query the size and the sum of elements of the set some element belongs to.

??? note "Solution"
    In this problem, operations 1 and 3 are both easy to handle; the difficulty lies in operation 2. Suppose we want to move element $x$ into the set that element $y$ is in. In an ordinary DSU, directly setting element $x$'s parent to the root of the set that element $y$ is in does not work, because this would move all elements in the subtree of element $x$ along with it. To address this problem, the solution is to guarantee that element $x$ has no children. To this end, when establishing the DSU, establish a virtual point $\tilde x$ for each element $x$, and point element $x$'s parent to the corresponding virtual point $\tilde x$. This way, when merging two sets, because a root is always connected to another root and the roots are all virtual points, only virtual points have children, and all points that actually store elements have no children. At this point, moving an element is much easier to implement.

??? note "Reference implementation"
    === "C++"
        ```cpp
        --8<-- "docs/ds/code/dsu/dsu_1.cpp"
        ```
    
    === "Python"
        ```python
        --8<-- "docs/ds/code/dsu/dsu_1.py"
        ```

???+ example "[Luogu P2024 「NOI2011」Food Chain](https://www.luogu.com.cn/problem/P2024)"
    In the animal kingdom there are three classes of animals $A,B,C$, and the food chain of these three classes forms an interesting cycle. $A$ eats $B$, $B$ eats $C$, and $C$ eats $A$.
    
    There are now $N$ animals numbered $1 \sim N$. Each animal is one of $A,B,C$, but we do not know which class it is.
    
    Someone describes the food-chain relationships of these $N$ animals using two kinds of statements:
    
    -   The first kind is `1 X Y`, meaning $X$ and $Y$ are of the same class.
    -   The second kind is `2 X Y`, meaning $X$ eats $Y$.
    
    This person makes $K$ statements about the $N$ animals using the above two kinds of statements, one after another; some of these $K$ statements are true and some are false. A statement is false when it satisfies one of the following three conditions, otherwise it is true.
    
    -   The current statement conflicts with some previous true statement—it is false;
    -   $X$ or $Y$ in the current statement is greater than $N$—it is false;
    -   The current statement says $X$ eats $X$—it is false.
    
    Your task is to output the total number of false statements given $N$ and the $K$ statements.

??? note "Solution 1"
    Consider maintaining the food-chain information with a weighted DSU. If $x$ and $y$ are of the same class, then $x\equiv y\pmod 3$; if $x$ eats $y$, then $x - y \equiv 1 \pmod 3$. This turns this problem into the earlier template problem.
    
    Specifically, for each statement, apart from the obvious false statements where $x>n$ or $y>n$, we need to determine whether $x$ and $y$ are already connected: if already connected, compute their distance modulo the modulus and compare it with the information this statement claims; otherwise, connect the two according to the information this statement provides. Apart from the obvious cases, a statement is false if and only if the two nodes mentioned are already connected and the corresponding distance contradicts the information this statement claims.

??? note "Reference implementation 1"
    === "C++"
        ```cpp
        --8<-- "docs/ds/code/dsu/dsu_6.cpp"
        ```
    
    === "Python"
        ```python
        --8<-- "docs/ds/code/dsu/dsu_6.py"
        ```

??? note "Solution 2"
    Split one organism $x$ into three states. In the specific implementation, we can directly treat different states as different elements:
    
    -   The states in the same set as $x$ are of the same species as $x$;
    -   The states in the same set as $x+n$ can be eaten by $x$;
    -   The states in the same set as $x+2n$ can eat $x$.
    
    So, for a statement:
    
    -   `1 x y` is false if and only if:
    
        1.  $x>N$ or $y>N$;
        2.  $y$ is in the same set as one of $x+n$ or $x+2n$.
    -   `2 x y` is false if and only if:
    
        1.  $x>N$ or $y>N$;
        2.  $y$ is in the same set as one of $x$ or $x+2n$.
    -   If true, merge the corresponding states.

??? note "Reference implementation 2"
    === "C++"
        ```cpp
        --8<-- "docs/ds/code/dsu/dsu_2.cpp"
        ```
    
    === "Python"
        ```python
        --8<-- "docs/ds/code/dsu/dsu_2.py"
        ```

???+ example "[ABC396E Min of Restricted Sum](https://atcoder.jp/contests/abc396/tasks/abc396_e)"
    Given integers $N, M$ and integer sequences $X=(X_1,X_2,\ldots,X_M)$, $Y=(Y_1,Y_2,\ldots,Y_M)$, $Z=(Z_1,Z_2,\ldots,Z_M)$ of length $M$, where it is guaranteed that all elements of $X$ and $Y$ are in the range $1$ to $N$.
    
    Define a non-negative integer sequence $A=(A_1,A_2,\ldots,A_N)$ of length $N$ as a **good integer sequence** if and only if it satisfies the following condition:
    
    -   For all integers $i$ with $1 \leq i \leq M$, $A_{X_i} \oplus A_{Y_i} = Z_i$, where $\oplus$ denotes the XOR operation.
    
    Determine whether such a good integer sequence exists. If it exists, find the good integer sequence with the minimum element sum $\displaystyle \sum_{i=1}^N A_i$ and output that sequence.

??? note "Solution"
    XOR is just the "same" or "different" relationship on a single binary bit. So, splitting all binary bits of $A_i$, the XOR relationship can be maintained with a weighted DSU (or categorical DSU). Elements in the same connected component must correspond to the same bit of different numbers in $A$. When counting the answer, the elements of the same connected component are usually divided into two groups, and the values of the two groups should be different; we only need to assign $0$ to the larger group and $1$ to the other group to guarantee the minimum total weight.

??? note "Reference implementation"
    === "C++"
        ```cpp
        --8<-- "docs/ds/code/dsu/dsu_3.cpp"
        ```
    
    === "Python"
        ```python
        --8<-- "docs/ds/code/dsu/dsu_3.py"
        ```

## Exercises

-   [「NOI2015」Automatic Program Analysis](https://uoj.ac/problem/127)
-   [「JSOI2008」Star Wars](https://www.luogu.com.cn/problem/P1197)
-   [「NOIP2023」Three-Valued Logic](https://www.luogu.com.cn/problem/P9869)
-   [「NOI2002」Legend of the Galactic Heroes](https://www.luogu.com.cn/problem/P1196)

## Other applications

Kruskal in [minimum-spanning-tree algorithms](../graph/mst.md) and Tarjan's algorithm in [lowest common ancestor](../graph/lca.md) are algorithms based on the DSU.

For the related special topic, see [DSU applications](../topic/dsu-app.md).

## References and further reading

1.  [Zhihu answer: Is there really a binary path-compression optimization in the DSU?](https://www.zhihu.com/question/28410263/answer/40966441)
2.  Gabow, H. N., & Tarjan, R. E. (1985). A Linear-Time Algorithm for a Special Case of Disjoint Set Union. JOURNAL OF COMPUTER AND SYSTEM SCIENCES, 30, 209-221. [PDF](https://dl.acm.org/doi/pdf/10.1145/800061.808753)
3.  [CSDN: Extended-domain DSU & Weighted DSU](https://blog.csdn.net/qqqqqwerttwtwe/article/details/145440100)

[^tarjan1984worst]: Tarjan, R. E., & Van Leeuwen, J. (1984). Worst-case analysis of set union algorithms. Journal of the ACM (JACM), 31(2), 245-281. [ResearchGate PDF](https://www.researchgate.net/profile/Jan_Van_Leeuwen2/publication/220430653_Worst-case_Analysis_of_Set_Union_Algorithms/links/0a85e53cd28bfdf5eb000000/Worst-case-Analysis-of-Set-Union-Algorithms.pdf)

[^yao1985expected]: Yao, A. C. (1985). On the expected performance of path compression algorithms. [SIAM Journal on Computing, 14(1), 129-133.](https://epubs.siam.org/doi/abs/10.1137/0214010?journalCode=smjcat)
