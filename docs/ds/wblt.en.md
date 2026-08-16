author: hsfzLZH1, cesonic, AtomAlpaca, caijianhong, Persdre, aofall, CoelacanthusHex, Marcythm, shuzhouliu, Tiphereth-A

## Introduction

The **Weight Balanced Leafy Tree**, hereinafter called **WBLT**, is a balanced tree; compared with other balanced trees, its main advantages are simple implementation and a small constant factor. It supports interval operations and can be made persistent.

The Weight Balanced Leafy Tree, as the name implies, is a combination of the Weight Balanced Tree and the Leafy Tree.

Each node of the Weight Balanced Tree stores the size of the subtree under this node, and guarantees the tree height by keeping the size relationship of the left and right subtrees within a certain range.

The original information maintained by the Leafy Tree is stored only on the **leaf nodes** of the tree, while non-leaf nodes are only used to maintain child-node information and maintain the shape of the data structure. The well-known segment tree is a kind of Leafy Tree.

![](images/leafy-tree-1.svg)

The trees in this article all refer to binary Leafy Trees, i.e. the number of child nodes of each node can only be $0$ or $2$. In this article, $n$ refers to the number of leaf nodes of the tree. A tree with $n$ leaf nodes has a total of $2n-1$ nodes, so the space occupied by a WBLT is $\Theta(n)$.

## Basic structure and balance maintenance

This section introduces the basic structure of the WBLT, defines the concept of the tree's $\alpha$-balance, and explains how to maintain the tree's balance by rotation or merging.

### Node information

To implement a basic WBLT, one only needs to record the following information for each node:

-   `lc[x]`, `rc[x]`: the left and right child nodes;
-   `sz[x]`: the number of leaf nodes in the subtree rooted at $x$.

To implement a balanced tree with the WBLT, one also needs to record information related to the key value at each node:

-   `val[x]`: the key value at node $x$.

Because only leaf nodes actually store key values, the information stored at other nodes is obtained by merging their child nodes, to facilitate subsequent queries.

For example, a commonly-used merging method is to store the larger of the key values of the two child nodes at that node. In this way, what each node stores is the maximum of the key values of all leaf nodes in the subtree rooted at it. Based on this, the method of updating node information is as follows:

???+ example "Reference code"
    ```cpp
    --8<-- "docs/ds/code/wblt/wblt-1.cpp:push-up"
    ```

Of course, if needed, one can also implement a corresponding `push_down(x)` function.

### Auxiliary functions

Besides basic node-information maintenance, the WBLT usually also needs to implement the following auxiliary functions, used for memory management:

-   `new_node()`: create a new node;
-   `del_node(x)`: delete node $x$;
-   `new_leaf(v)`: create a new leaf node with key value $v$;
-   `join(x, y)`: connect subtrees, i.e. create a new node $z$ with $x$, $y$ as the left and right child nodes respectively;
-   `cut(x)`: split a subtree, i.e. obtain the two child nodes of node $x$ and delete node $x$.

If the implementation of the WBLT relies heavily on splitting and connecting subtrees, it will create many new nodes and release an equal number of old nodes. If old useless nodes are not reclaimed in time, the space will no longer be linear. The following are the array implementations of these auxiliary functions:

???+ example "Reference code"
    ```cpp
    --8<-- "docs/ds/code/wblt/wblt-1.cpp:helper"
    ```

After encapsulating these auxiliary functions, the array implementation and the pointer implementation have no difference in the subsequent functions.

### The concept of balance

For a tree, one can define its **balance degree** at a non-leaf node $x$ as

$$
\rho(x) = \dfrac{\min\{w(T_{\operatorname{left}(x)}),w(T_{\operatorname{right}(x)})\}}{w(T_x)}.
$$

Among them, $T_x$ denotes the subtree rooted at $x$, $w(\cdot)$ denotes the weight of the subtree (the number of its leaf nodes), and $\operatorname{left}(x)$ and $\operatorname{right}(x)$ denote the left and right leaf nodes of $x$ respectively. In particular, at a leaf node, it is stipulated that $\rho(x)=1/2$.

For $\alpha\in(0,1/2]$, if the balance degree $\rho(x)\ge\alpha$ at a certain node $x$, then that node is called **$\alpha$-balanced**. If every node of the tree is $\alpha$-balanced, then the tree is called **$\alpha$-balanced**. The set of such trees is denoted $BB[\alpha]$. A tree is **$\alpha$-balanced** if and only if it itself is $\alpha$-balanced and both its left and right subtrees are $\alpha$-balanced or it is a leaf node.

That the tree is $\alpha$-balanced has an obvious benefit: its height is $O(\log n)$. This is because each step moving from a leaf node toward the root, the number of leaf nodes contained by the subtree expands to at least $1/(1-\alpha)$ times the original, so it can only move $O(\log_{\frac{1}{1-\alpha}}n) = O(\log n)$ times. This guarantees that in an $\alpha$-balanced tree, the complexity of a single query is always strictly $O(\log n)$, and the constant of the algorithm is positively correlated with $\log(1/(1-\alpha))$ (base $2$). When $\alpha$ is within the reasonable range provided below, this constant is roughly $2\sim 3.5$.

The balance maintenance of the WBLT can usually be done by rotation or merging. The WBLTs implemented by the two methods both have strictly $O(\log n)$ complexity for a single insertion, deletion, and similar operations. However, unlike the [Treap](./treap.md) with fixed priorities, the structure of the WBLT is not unique, so the structures of the trees maintained by the two methods are not the same, although this does not affect their use. Of course, balance maintenance can also adopt a strategy similar to the [scapegoat tree](./sgt.md), using rebuilding to achieve amortized $O(\log n)$ complexity, but this loses the advantages of the WBLT such as persistence and interval operations, so it is not recommended.

Below, the methods of maintaining balance by rotation and by merging are introduced separately, and the corresponding balance-maintenance and merge-operation functions are implemented. After encapsulating these functions, the two ways of maintaining tree balance have no difference in the subsequent concrete balanced-tree implementations. Moreover, no matter which method is used, the time complexity of a single balance-maintenance operation is $O(1)$, and the complexity of a single merge of tree $T_1$ and tree $T_2$ is $O\left(\left|\log\dfrac{w(T_1)}{w(T_2)}\right|\right)$.

???+ info "Notation omitting weight"
    To maintain the tree's balance, only the weight information of the subtrees needs to be retained. Therefore, for convenience of expression, the two sections discussing balance maintenance below will mix the notation of a tree and its weight. For example, the weight of subtree $x$ is also denoted by $x$, rather than $w(x)$. Similarly, the tree obtained by merging subtrees $x$ and $y$ is also represented by its weight, directly written as tree $x+y$.

### Maintaining by rotation

The rotation operation of the WBLT is exactly the same as the [rotation operation of the Treap](./treap.md#rotation), and one can adopt a rotation strategy completely consistent with the Treap. Of course, rotation itself can likewise be regarded as a process of redistributing subtree weights, so it can also be completed by splitting and connecting subtrees. The results of the two implementations are exactly consistent, but the second implementation is more convenient for the persistence of the WBLT.

???+ example "Reference code"
    === "Not relying on connecting"
        ```cpp
        --8<-- "docs/ds/code/wblt/wblt-1.cpp:rotate-not-by-joining"
        ```
    
    === "Relying on connecting"
        ```cpp
        --8<-- "docs/ds/code/wblt/wblt-1.cpp:rotate-by-joining"
        ```

Suppose after some tree modification operation, we are restoring the tree's balance from bottom to top. Now, the left and right subtrees $x$ and $y$ are no longer balanced, but they themselves are both balanced. We may as well assume the right subtree $y$ is too light, i.e. $y<\alpha(x+y)$. At this point, the shape of the tree is as shown by the tree on the left in the figure.

![](images/wblt-balance.svg)

A naive balance-maintenance strategy is to rotate $x$ to the root node, so that its original right child $w$, together with $y$, becomes the right child of the new tree, while its original left child $z$ becomes the left child of the new tree. This is equivalent to moving the weight of $w$ in the original left side of the tree to its right side. If the weight of $w$ is appropriate, such an operation can restore the tree's balance. The tree thus obtained is as shown by the tree on the right in the figure.

But, if $w$ itself is too heavy, such an operation may move too much weight to the right subtree, thereby making the left subtree of the new tree too light, i.e. $z<\alpha(x+y)$. For this situation, because the weights of both subtree $z$ and subtree $y$ are too small, we can only consider splitting $w$ into two subtrees, connected with $z$ and $y$ respectively, becoming the two subtrees of the new tree. This is equivalent to first rotating node $w$ to node $x$, then rotating it to the root node. Likewise, we can expect the tree thus obtained to reach balance, with the shape as shown by the tree at the top in the figure.

These two rotation strategies are called single rotation and double rotation respectively. The choice of single-rotation and double-rotation strategy mainly depends on the proportion of subtree $w$ relative to subtree $x$, i.e. there is a threshold $\beta$ such that

-   when $w\le\beta x$, the single-rotation strategy should be chosen;
-   when $w>\beta x$, the double-rotation strategy should be chosen.

The difficulty lies in the choice of the threshold $\beta$, which requires some concrete calculation. Blum and Mehlhorn proved that, for parameters[^wrong-range]

$$
\alpha\in\left(\dfrac{2}{11},1-\dfrac{\sqrt{2}}{2}\right]\approx(0.182,0.292],~\beta=\frac{1}{2-\alpha},
$$

the above strategy combining single rotation and double rotation can maintain the balance of a WBLT that has become unbalanced due to a single insertion or deletion.

??? note "Proof"
    What needs to be proved is that if the tree becomes unbalanced after a single insertion or deletion, its balance can be restored through the above strategy. Combining the above figure, let
    
    $$
    \rho_1 = \dfrac{y}{x+y}, ~\rho_2 = \dfrac{w}{x}, ~\rho_3 = \dfrac{v}{w}.
    $$
    
    Then, $\rho_1<\alpha\le\rho_2,\rho_3\le 1-\alpha$. There is also an implicit condition here, about the value range of $\rho_1$:
    
    -   If the imbalance is caused by inserting a single element, then we should have
    
        $$
        \dfrac{y}{x-1+y} \ge \alpha \implies \rho_1 \ge \dfrac{\alpha y}{y+\alpha} \ge \dfrac{\alpha}{1+\alpha}.
        $$
    -   If the imbalance is caused by deleting a single element, then we should have
    
        $$
        \dfrac{y+1}{x+y+1} \ge \alpha \implies \rho_1 \ge \dfrac{\alpha y}{y+1-\alpha} \ge \dfrac{\alpha}{2-\alpha}.
        $$
    
    Because for $0<\alpha<1/2$, we always have $\alpha/(2-\alpha)<\alpha/(1+\alpha)$, deleting an element causes a more severe imbalance than adding an element, especially for the case where the scale of the tree is very small.
    
    Next, the operation of restoring balance is divided into two cases:
    
    ??? note "Case one: $w$ is not too heavy, i.e. when $\rho_2\le\beta$, single rotation"
        First, $z$ and $w+y$ are balanced. This is because
        
        $$
        \left(1-\dfrac{\alpha}{2-\alpha}\right)\alpha+\dfrac{\alpha}{2-\alpha} \le \dfrac{w+y}{x+y} = (1-\rho_1)\rho_2+\rho_1 < (1-\alpha)\dfrac{1}{2-\alpha}+\alpha.
        $$
        
        The left expression is always greater than $\alpha$ for $\alpha\in(0,1)$, and the right expression is always not greater than $(1-\alpha)$ for $\alpha\in(0,1-\sqrt{2}/2]$.
        
        Secondly, $w$ and $y$ are balanced. Likewise, consider
        
        $$
        \dfrac{y}{w+y} = \dfrac{\rho_1}{(1-\rho_1)\rho_2+\rho_1}.
        $$
        
        On the one hand, for all $\alpha\in(0,(3-\sqrt{5})/2)$, we have
        
        $$
        \dfrac{y}{w+y} < \dfrac{\alpha}{(1-\alpha)\alpha+\alpha} < 1-\alpha.
        $$
        
        On the other hand, for all $\alpha\in(0,1/3)$, except the case of deleting an element with $y=1$, we always have
        
        $$
        \rho_1 \ge \min\left\{\dfrac{\alpha}{1+\alpha},\dfrac{2\alpha}{3-\alpha}\right\} = \dfrac{2\alpha}{3-\alpha},
        $$
        
        so, we have
        
        $$
        \dfrac{y}{w+y} \ge \dfrac{\dfrac{2\alpha}{3-\alpha}}{\left(1-\dfrac{2\alpha}{3-\alpha}\right)\dfrac{1}{2-\alpha}+\dfrac{2\alpha}{3-\alpha}} > \alpha.
        $$
        
        Finally, consider the remaining case, i.e. deleting an element with $y=1$. The most likely imbalance case occurs when $x=\lfloor 2/\alpha\rfloor-2$ and $w=\lfloor\beta x\rfloor$. The tree can restore balance if and only if
        
        $$
        \dfrac{1}{1+\lfloor\beta x\rfloor}\ge\alpha \iff \lfloor\beta x\rfloor\le\dfrac{1}{\alpha}-1 \iff \beta x < \dfrac{1}{\alpha} \iff x < \dfrac{2}{\alpha}-1.
        $$
        
        And this always holds. This completes the proof of this case. Note that the proof of the last case uses the property that weights are always integers, and cannot be merged into the previous discussion.
    
    ??? note "Case two: $w$ is too heavy, i.e. when $\rho_2>\beta$, double rotation"
        First, $z+u$ and $v+y$ are balanced. This is because
        
        $$
        \dfrac{\alpha}{2-\alpha}+\left(1-\dfrac{\alpha}{2-\alpha}\right)\dfrac{1}{2-\alpha}\alpha < \dfrac{z+u}{x+y} = \rho_1+(1-\rho_1)\rho_2\rho_3 <\alpha+(1-\alpha)^3
        $$
        
        The left expression is always greater than $\alpha$ for $\alpha\in(0,1)$, and the right expression is always less than $(1-\alpha)$ for $\alpha\in(0,(3-\sqrt{5})/2)$.
        
        Then, $z$ and $u$ are balanced. This is because for $\alpha\in(0,1)$, it always holds that
        
        $$
        \alpha=\dfrac{\dfrac{1}{2-\alpha}\alpha}{1-\dfrac{1}{2-\alpha}(1-\alpha)}<\dfrac{u}{z} = \dfrac{\rho_2(1-\rho_3)}{1-\rho_2\rho_3} <\dfrac{(1-\alpha)^2}{1-(1-\alpha)\alpha} < 1-\alpha.
        $$
        
        Finally, $v$ and $y$ are balanced. Similar to the other cases, consider
        
        $$
        \dfrac{y}{v+y} = \dfrac{\rho_1}{\rho_1+(1-\rho_1)\rho_2\rho_3}.
        $$
        
        On the one hand, for all $\alpha\in(0,1-\sqrt{2}/2]$, we have
        
        $$
        \dfrac{y}{v+y} < \dfrac{\alpha}{\alpha+(1-\alpha)\dfrac{1}{2-\alpha}\alpha} \le 1-\alpha.
        $$
        
        On the other hand,
        
        $$
        \dfrac{y}{v+y} \ge \dfrac{\rho_1}{\rho_1+(1-\rho_1)(1-\alpha)^2}.
        $$
        
        The right expression is not less than $\alpha$ if and only if
        
        $$
        \rho_1 \ge \dfrac{\alpha(1-\alpha)}{1+\alpha(1-\alpha)}.
        $$
        
        If the imbalance is caused by insertion, then $\rho_1\ge \alpha/(1+\alpha)$, which obviously holds. Otherwise, the case is somewhat complex:
        
        -   When $y\ge 3$, $\rho_1\ge 3\alpha/(4-\alpha)$, and $3\alpha/(4-\alpha)\ge\alpha(1-\alpha)/(1+\alpha(1-\alpha))$ holds for all $\alpha\in[1-\sqrt{3}/2,1)$;
        -   When $y=2$, the most likely imbalance case occurs when $x=\lfloor 3/\alpha\rfloor-3$, $w=\lfloor(1-\alpha)x\rfloor$ and $v=\lfloor(1-\alpha)w\rfloor$, at which point $v/(v+y)\ge\alpha$ holds for all $\alpha\in(3/22,1)$;
        -   When $y=1$, the most likely imbalance case occurs when $x=\lfloor 2/\alpha\rfloor-2$, $w=\lfloor(1-\alpha)x\rfloor$ and $v=\lfloor(1-\alpha)w\rfloor$, at which point $v/(v+y)\ge\alpha$ holds for all $\alpha\in(2/11,1)$.
        
        The discussion of the last two cases likewise uses the point that the weights of all nodes are integers.
    
    Combining the two cases, when $\alpha\in(2/11,1-\sqrt{2}/2]$, the aforementioned strategy combining single rotation and double rotation can guarantee the tree's balance.
    
    From this analysis process, we can see that the case hardest to keep balanced occurs when deleting a node from a small-scale tree. Besides $\beta=1/(2-\alpha)$, the correctness proof for other parameter choices can likewise repeat the above process, only some inequalities used need to be adjusted accordingly.

Subsequently, Hirai and Yamamoto completely determined the range of all feasible $(\alpha,\beta)$ through machine proof; the result is a rather complex two-dimensional figure:

![](images/wblt-param-range.svg)

In their article they recommend using the following strategy to maintain balance:

-   when $x>3y$, judge imbalance;
-   when $w\le 2z$, choose the single-rotation strategy, otherwise, choose the double-rotation strategy.

The reason is that this is the only strategy within the feasible parameter range that can be represented with simple integers, thereby avoiding the efficiency loss caused by floating-point operations. Their recommended strategy is equivalent to taking $(\alpha,\beta)=(1/4,2/3)$. In practice, one can choose appropriate parameters according to the specific situation.

The reference implementation is as follows:

???+ example "Reference code"
    ```cpp
    --8<-- "docs/ds/code/wblt/wblt-1.cpp:too-heavy"
    --8<-- "docs/ds/code/wblt/wblt-1.cpp:balance"
    ```

After implementing the balance-maintenance strategy, the algorithm for merging two trees is very simple. Still assuming $x>y$, the merge strategy is as follows:

-   if the right subtree $y$ is empty, directly return the left subtree $x$;
-   if the left and right subtrees $x$ and $y$ are already balanced, i.e. $y\ge\alpha(x+y)$, directly connect the two subtrees;
-   otherwise, merge $x$'s right subtree $w$ with $y$, connect the left subtree $z$ with the result of their merge, and adjust the balance of the new tree.

The reference implementation is as follows:

???+ example "Reference code"
    ```cpp
    --8<-- "docs/ds/code/wblt/wblt-1.cpp:merge-by-balancing"
    ```

It can be proved that this can maintain the balance of the merged tree, and the complexity of this operation is $O(|\log(x/y)|)$.

??? note "Proof of balance and complexity"
    We only need to consider the case where $y$ is too light, i.e. $y<\alpha(x+y)$. At this point, first merge $w$ and $y$, then connect $z$ and $w+y$. What needs to be proved is that as long as we adjust the tree's balance at the root, we can guarantee the tree's balance. Suppose the left and right subtrees of tree $w+y$ are $c$ and $d$ respectively, and the left and right subtrees of $c$ are $a$ and $b$ respectively. Adjusting balance at the root can be divided into three cases:
    
    ??? note "Case one: $z$ and $w+y$ are already balanced, no further adjustment needed, i.e. $z\ge\alpha(x+y)$"
        By the definition of balance, both subtrees $z$ and $w+y$ are balanced, and they are also balanced with each other, so the whole tree is also balanced.
    
    ??? note "Case two: $z$ is too light and $c$ is not too heavy, balance can be restored by single rotation, i.e. $z<\alpha(x+y)$ and $c\le\beta(w+y)$"
        At this point, because $z$ and $w$ are balanced, but $y$ is too light relative to $x = z+w$, the weight of subtree $z$ satisfies
        
        $$
        \alpha(1-\alpha)(x+y) <  \alpha(z+w) \le z \le \alpha(x+y) .
        $$
        
        And the weight of $c$ satisfies
        
        $$
        \alpha(w+y) \le c \le \beta(w+y).
        $$
        
        From this, $z$ and $c$ are balanced with each other, as long as
        
        $$
        \dfrac{\alpha}{1-\alpha}<\dfrac{1-\alpha}{\alpha}\alpha<\dfrac{c}{z}=\dfrac{w+y}{z}\dfrac{c}{w+y} < \dfrac{1-\alpha(1-\alpha)}{\alpha(1-\alpha)}\beta\le\dfrac{1-\alpha}{\alpha},
        $$
        
        which requires
        
        $$
        \beta\le \dfrac{(1-\alpha)^2}{1-\alpha(1-\alpha)}.
        $$
        
        And $z+c$ and $d$ are balanced with each other, as long as
        
        $$
        \alpha\le (1-\beta)(1-\alpha)\le \dfrac{d}{w+y}\dfrac{w+y}{x+y}  = \dfrac{d}{x+y} < \dfrac{d}{c+d} \le 1-\alpha,
        $$
        
        which requires
        
        $$
        \beta \le \dfrac{1-2\alpha}{1-\alpha}.
        $$
    
    ??? note "Case three: $z$ is too light and $c$ is too heavy, balance can be restored by double rotation, i.e. $z<\alpha(x+y)$ and $c>\beta(w+y)$"
        Similar to case two, we have
        
        $$
        \begin{aligned}
        \alpha(1-\alpha)(x+y) < z &\le \alpha(x+y),\\
        \beta(w+y)<c &\le (1-\alpha)(w+y),\\
        \alpha c\le a,b &\le (1-\alpha)c.
        \end{aligned}
        $$
        
        From this, $z$ and $a$ are balanced with each other, as long as
        
        $$
        \dfrac{\alpha}{1-\alpha}\le\dfrac{1-\alpha}{\alpha}\beta\alpha\le\dfrac{a}{z} = \dfrac{w+y}{z}\dfrac{a}{c+d} < \dfrac{1-\alpha(1-\alpha)}{\alpha(1-\alpha)}(1-\alpha)^2,
        $$
        
        which requires
        
        $$
        \beta\ge\dfrac{\alpha}{(1-\alpha)^2}.
        $$
        
        Secondly, $b$ and $d$ are balanced with each other, as long as
        
        $$
        \dfrac{\alpha}{1-\alpha}\le\dfrac{\beta}{1-\beta}\alpha \le \dfrac{b}{d} = \dfrac{c}{d}\dfrac{b}{c} \le \dfrac{1-\alpha}{\alpha}(1-\alpha) < \dfrac{1-\alpha}{\alpha},
        $$
        
        which requires
        
        $$
        \beta\ge\dfrac{1}{2-\alpha}.
        $$
        
        Finally, $z+a$ and $b+d$ are balanced with each other, as long as
        
        $$
        \alpha<(1-\alpha)(1-(1-\alpha)^2)\le\frac{b+d}{x+y} = \dfrac{w+y}{x+y}\dfrac{b+d}{w+y} < (1-\alpha(1-\alpha))(1-\beta\alpha) \le 1-\alpha,
        $$
        
        which requires
        
        $$
        \beta\ge\dfrac{\alpha}{1-\alpha+\alpha^2}.
        $$
    
    Combining the three cases, as long as
    
    $$
    0<\alpha\le 1-\dfrac{\sqrt{2}}{2},~\dfrac{1}{2-\alpha}\le\beta\le\dfrac{1-2\alpha}{1-\alpha},
    $$
    
    we can guarantee that the merged tree can be adjusted to balance using the strategy combining single rotation and double rotation. This obviously includes the parameter range given in the main text.
    
    Finally, let's briefly explain why the complexity of this algorithm is $O(|\log(x/y)|)$. In the merge process, if $y$ is too light relative to $x$, we try to merge with $x$'s right subtree; this process continues until the subtree rooted at some descendant node of $x$ is balanced with $y$. Because each level deeper down, the subtree weight becomes at least $(1-\alpha)$ of the original, so at most $\log_{\frac{1}{1-\alpha}}(x/y)$ iterations are needed to find the subtree balanced with $y$. Therefore, this merge algorithm calls the balance algorithm $O(\log n)$ times[^merge-complexity-cmp], so the complexity is $O(\log n)$.
    
    Although not obvious, this argument process relies on such a conclusion: in the process of continually taking the right subtree, $y$ will not, before and after one iteration, change from too light relative to the left subtree to too heavy relative to it. This is because the weight range of the subtree that can be balanced with $y$ lies between $\alpha y/(1-\alpha)$ and $(1-\alpha)y/\alpha$. Therefore, if in one iteration, it changes from $y$ too light to $y$ too heavy, then the weight of $x$'s subtree shrinks to at least $\alpha^2/(1-\alpha)^2$ of the original during this iteration. But, in a single iteration, the subtree weight can shrink to at most $\alpha$ of the original, but in the above range of $\alpha$, $\alpha>\alpha^2/(1-\alpha)^2$. This shows that the premise case is impossible, and after a certain iteration there must be a case where $y$ is balanced with some subtree of $x$.

### Maintaining by merging

Merging two subtrees means, under the guarantee that the key value of the left subtree is always not greater than the key value of the right subtree, building a new tree such that the information of all its leaf nodes is exactly the union of the leaf-node information of the left and right subtrees, and guaranteeing the tree's balance.

For this, there is the following strategy[^more-join]: (still assuming $x>y$)

-   if the right subtree $y$ is empty, directly return the left subtree $x$;
-   if the left and right subtrees $x$ and $y$ are already balanced, i.e. $y\ge\alpha(x+y)$, directly connect the two subtrees;
-   otherwise, the right subtree $y$ is too light, but if $x$'s left subtree $z$ and $w+y$ can be balanced, i.e. $z\ge\alpha(x+y)$, then first merge $w$ and $y$, then merge $z$ and $w+y$;
-   otherwise, both $z$ and $y$ are too light; at this point, we need to first merge $z$ and $w$'s left subtree $u$, then merge $w$'s right subtree $v$ and $y$, then **merge** the results of the two merges into a new tree.

Comparing this strategy with the balance strategy above, we can see that the ways of combining nodes in the last two cases are respectively similar to the results of single rotation and double rotation in the aforementioned balance strategy, only changing the connection of subtrees to merging.

It can be proved that when

$$
0<\alpha \le 1-\dfrac{\sqrt{2}}{2}\approx 0.292
$$

the tree thus obtained is always balanced, and the complexity of this operation is $O(|\log(x/y)|)$. That is to say, the cost of merging two trees is unrelated to the absolute sizes of the two trees, and only related to their relative sizes.

??? note "Proof of balance and complexity"
    Let the number of times the two subtrees need to be directly connected when merging two subtrees of weights $x$ and $y$ respectively be $\tau(x,y)$. Strictly speaking, we need to prove that when $0<\alpha\le 1-\sqrt{2}/2$, there exists a constant $C>0$ such that for any $x>y>0$, we have
    
    $$
    \tau(x,y) \le 1+C\log^+\dfrac{\alpha x}{(1-\alpha)^2y},
    $$
    
    where $\log^+ x = \max\{0,\log x\}$; moreover, for all $x/y\le(1-\alpha)/\alpha$, we have $\tau(x,y)=1$. In fact, the constant in the formula can be taken as
    
    $$
    C = -\dfrac{2}{\log(1-\alpha)}.
    $$
    
    This shows that the complexity of the merge algorithm is $O(|\log(x/y)|)$.
    
    To prove that the tree obtained by the merge algorithm is always balanced, and that the above complexity expression holds, induction is needed. For all lattice points $(x,y)\in\mathbf N^2_+$ in the first quadrant, one can assign the lexicographic order of $(x+y,|x-y|)$, which is obviously a well-order on this set, and one can induct along this order. The induction base is $(x,y)=(1,1)$; at this point, both subtrees have only one leaf node, and the subtree obtained by directly connecting must be balanced, and $\tau(x,y)=1$, conforming to the above formula. Below, assume the induction proceeds to $(x,y)$, and the conclusion holds for all points before $(x,y)$. This is divided into three cases:
    
    ??? note "Case one: trees $x$ and $y$ are balanced, i.e. $y\ge\alpha(x+y)$"
        At this point, the tree obtained by directly connecting is also balanced, and the tree-connection algorithm is only called once, so $\tau(x,y)=1$.
    
    ??? note "Case two: tree $y$ is too light, but $z$ is not too light, i.e. $y<\alpha(x+y)\le z$"
        At this point, first merge $w$ and $y$, then merge $z$ and $w+y$, so
        
        $$
        \tau(x,y) = \tau(w,y) + \tau(z,w+y).
        $$
        
        By the induction hypothesis, subtree $w+y$ is already balanced. For the second merge, we can actually directly prove that $z$ and $w+y$ are balanced:
        
        $$
        \alpha \le \dfrac{z}{z+(w+y)} = \dfrac{z}{x+y} < \dfrac{z}{z+w} \le 1-\alpha.
        $$
        
        Therefore, merging $z$ and $w+y$ is actually directly connecting the two subtrees, and $\tau(z,w+y) = 1$. Therefore, the finally obtained tree is also balanced.
        
        Now estimate the size of $\tau(w,y)$. Because $y>(\alpha/(1-\alpha))x$ and $\alpha x\le w\le(1-\alpha)x$, by scaling we know
        
        $$
        \dfrac{\alpha}{1-\alpha}<1-\alpha=\dfrac{\alpha x}{(\alpha/(1-\alpha))x}< \dfrac{w}{y} \le \dfrac{(1-\alpha)x}{y}.
        $$
        
        This shows that $w$ and $y$ being unbalanced only occurs when $w>y$, so we have
        
        $$
        \begin{aligned}
        \tau(w,y) &\le 1+C\log^+\dfrac{\alpha w}{(1-\alpha)^2y} \le 1+C\log^+\dfrac{\alpha x}{(1-\alpha)y} \\
        &= 1 + C\log(1-\alpha) + C\log^+\dfrac{\alpha x}{(1-\alpha)^2y}.
        \end{aligned}
        $$
        
        The equality in the last step holds because $x/y>(1-\alpha)/\alpha$.
        
        Therefore, we have
        
        $$
        \tau(x,y) \le 2 + C\log(1-\alpha) + C\log^+\dfrac{\alpha x}{(1-\alpha)^2y}.
        $$
    
    ??? note "Case three: both tree $y$ and $z$ are too light, i.e. $y,z<\alpha(x+y)$"
        At this point, first merge $z$ and $u$, then merge $v$ and $y$, and finally merge $z+u$ and $v+y$. Therefore,
        
        $$
        \tau(x,y) = \tau(z,u) + \tau(v,y) + \tau(z+u,v+y).
        $$
        
        Similar to the previous cases, we can estimate the weight ratio of the two subtrees at each merge step.
        
        Because $z,y<\alpha(x+y)$, we have $w>(1-2\alpha)(x+y)$. At the same time, using the balance condition, we have $\alpha\le z/x,w/x,u/w,v/w\le 1-\alpha$. This shows
        
        $$
        \begin{aligned}
        \dfrac{\alpha}{1-\alpha}<\dfrac{\alpha}{1-\alpha}\frac{1}{1-\alpha}\le \dfrac{z}{u} &= \dfrac{z}{w}\dfrac{w}{u} < \dfrac{\alpha}{1-2\alpha}\dfrac{1}{\alpha} \le \dfrac{1-\alpha}{\alpha},\\
        \dfrac{\alpha}{1-\alpha}\le\alpha\dfrac{1-2\alpha}{\alpha}< \dfrac{v}{y} &= \dfrac{v}{w}\dfrac{w}{y} \le (1-\alpha)\dfrac{(1-\alpha)x}{y} = (1-\alpha)^2\dfrac{x}{y}.
        \end{aligned}
        $$
        
        For the last term, we have
        
        $$
        \dfrac{z+u}{v+y} = \dfrac{x+y}{v+y}-1 = \dfrac{x+y}{y}\dfrac{y}{v+y} - 1 < (1-\alpha)\left(\dfrac{x}{y}+1\right)-1 < (1-\alpha)\dfrac{x}{y}.
        $$
        
        Conversely, we have
        
        $$
        \dfrac{z+u}{v+y} = \dfrac{x+y}{v+y}-1 \ge \dfrac{x+y}{(1-\alpha)^2x+y}-1 > \dfrac{1}{(1-\alpha)^3+\alpha}-1 > \dfrac{\alpha}{1-\alpha}.
        $$
        
        Using these inequalities, we can show that the finally obtained tree must be balanced. Using the induction hypothesis, we know that merging $z$ and $u$, and merging $v$ and $y$, can both guarantee the obtained tree is balanced. Moreover, the first step of merging $z$ and $u$ is actually directly connecting the two trees. For the merge of tree $z+u$ and tree $v+y$, there are two subcases:
        
        -   if $z+u\le v+y$, then their weight ratio is strictly greater than $\alpha/(1-\alpha)$, so they can be directly connected, and the result is balanced;
        -   otherwise, their weight ratio must be strictly less than $x/y$, but $(z+u)+(v+y)=x+y$, so $|(z+u)-(v+y)|<|x-y|$; by the lexicographic order given above, the induction hypothesis can also be applied in this case, and the result is also balanced.
        
        Further applying the induction hypothesis, we know:
        
        $$
        \begin{aligned}
        \tau(z,u) &= 1,\\
        \tau(v,y) &\le 1+C\log^+\dfrac{\alpha x}{y},\\
        \tau(z+u,v+y) &\le 1 + C\log^+\dfrac{\alpha x}{(1-\alpha)y}.
        \end{aligned}
        $$
        
        Adding the three inequalities directly would cause the coefficient in front of the logarithmic term to become $2C$, and the induction cannot be completed. Therefore, a more refined estimate is needed here.
        
        When $\max\{v/y,(z+u)/(v+y)\}\le(1-\alpha)/\alpha$, one of $\tau(v,y)$ and $\tau(z+u,v+y)$ must be $1$, so we have
        
        $$
        \begin{aligned}
        \tau(v,y) + \tau(z+u,v+y) &\le 2 + C\log^+\dfrac{\alpha x}{(1-\alpha)y}\\
        &= 2 + C\log(1-\alpha) + C\log^+\dfrac{\alpha x}{(1-\alpha)^2y}.
        \end{aligned}
        $$
        
        Otherwise, we should have
        
        $$
        \begin{aligned}
        \tau(v,y) + \tau(z+u,v+y) 
        &\le 2 + C\log^+\dfrac{\alpha v}{(1-\alpha)^2y} + C\log^+\dfrac{\alpha(z+u)}{(1-\alpha)^2(v+y)}\\
        &= 2 + C\log\dfrac{\alpha}{(1-\alpha)^2} + C\log^+\dfrac{\alpha v(z+u)}{(1-\alpha)^2y(v+y)}.
        \end{aligned}
        $$
        
        For $0<\alpha\le 1-\sqrt{2}/2$, we have
        
        $$
        \dfrac{\alpha}{(1-\alpha)^2} < 1-\alpha.
        $$
        
        Moreover, we have
        
        $$
        \begin{aligned}
        \dfrac{v(z+u)}{y(v+y)} &= \left(\dfrac{v+y}{y}-1\right)\left(\dfrac{x+y}{y}\dfrac{y}{v+y} - 1\right) \\
        &= \dfrac{x+y}{y} + 1 -\dfrac{x+y}{y}\dfrac{y}{v+y}-\dfrac{v+y}{y} < \dfrac{x}{y}.
        \end{aligned}
        $$
        
        This shows that for this latter case, we also have
        
        $$
        \tau(v,y) + \tau(z+u,v+y) < 2 + C\log(1-\alpha) + C\log^+\dfrac{\alpha x}{(1-\alpha)^2y}.
        $$
        
        The overall merge complexity is
        
        $$
        \tau(x,y) \le 3 + C\log(1-\alpha) + C\log^+\dfrac{\alpha x}{(1-\alpha)^2y}.
        $$
    
    Combining all cases, we have
    
    $$
    \tau(x,y) \le 3 + C\log(1-\alpha) + C\log^+\dfrac{\alpha x}{(1-\alpha)^2y}.
    $$
    
    Therefore, as long as we take $2+C\log(1-\alpha)\le 0$, the induction of the complexity can be completed. An obvious choice is
    
    $$
    C = -\dfrac{2}{\log(1-\alpha)}.
    $$
    
    This constant shows that when merging two trees, the number of times of directly connecting subtrees roughly does not exceed twice the difference in tree heights.

The reference implementation is as follows:

???+ example "Reference code"
    ```cpp
    --8<-- "docs/ds/code/wblt/wblt-1.cpp:merge"
    ```

Using this merge strategy, one can likewise easily implement the tree's balance maintenance: when unbalanced, just directly merge the left and right subtrees.

???+ example "Reference code"
    ```cpp
    --8<-- "docs/ds/code/wblt/wblt-1.cpp:balance-by-merging"
    ```

Because the sizes of the two trees needing rebalancing are always nearly balanced, the complexity of maintaining balance is $O(1)$.

## Basic balanced-tree operations

Using the functions implemented above, the WBLT can support all basic operations of a balanced tree. This section takes a multiset as an example to discuss the method of implementing a balanced tree with the WBLT.

### Building the tree

The tree-building operation is very similar to the segment tree; just recurse down bisecting the interval, until the interval length is $1$, put the information to be maintained on the leaf node, and merge the interval information when backtracking.

???+ example "Reference code"
    ```cpp
    --8<-- "docs/ds/code/wblt/wblt-2.cpp:build"
    ```

The time complexity is $O(n)$.

### Insertion and deletion

For the insertion operation, we need to recurse down from the root node, until finding the leaf node with the smallest key value greater than or equal to the key value of the inserted element, then create two new nodes, one used to store the newly inserted value, and the other as the new parent of the two leaves replacing the position of this smallest leaf node, then connect these two leaves to this parent. When backtracking, the tree's balance needs to be maintained.

![](./images/wblt-insert-delete.svg)

As shown, we want to insert an element with value $4$ into the tree on the left. First find the leaf node with value $5$, then create the leaf node $4$ and the non-leaf node $\text{d}$, and connect $4$ and $5$ to $\text{d}$. This gives the tree on the right.

For deletion, consider the reverse of the above process. That is, find a leaf node whose key value equals the value to be deleted, delete it and its parent node, and replace the parent's position with the parent's other child. When backtracking, the tree's balance likewise needs to be maintained.

The reference implementation is as follows:

???+ example "Reference code"
    ```cpp
    --8<-- "docs/ds/code/wblt/wblt-1.cpp:insert-remove"
    ```

Note the handling of the empty tree. If you do not want to handle the empty tree, you can insert an $\infty$ element into the tree in advance.

The time complexity of both operations is $O(\log n)$.

### Querying the rank

Because the shape of the WBLT is very similar to the segment tree, querying the rank can use a method similar to binary search on a segment tree: if the maximum value of the left subtree is greater than or equal to the value to be queried, jump to the left child; otherwise, jump to the right child, and at the same time add the weight of the left subtree to the answer.

The reference implementation is as follows:

???+ example "Reference code"
    ```cpp
    --8<-- "docs/ds/code/wblt/wblt-1.cpp:rank"
    ```

The time complexity is $O(\log n)$.

### Querying by rank

Still using the idea of binary search on a segment tree, only here the node's weight is compared.

The reference implementation is as follows:

???+ example "Reference code"
    ```cpp
    --8<-- "docs/ds/code/wblt/wblt-1.cpp:kth-element"
    ```

The time complexity is $O(\log n)$.

### Finding the predecessor and successor

Just combine the above two functionalities.

The reference implementation is as follows:

???+ example "Reference code"
    ```cpp
    --8<-- "docs/ds/code/wblt/wblt-1.cpp:prev-next"
    ```

If you want to implement it directly, note that nodes with the same key value may be stored in multiple leaf nodes.

### Split operation

The split of the WBLT is similar to the [rotation-free Treap](./treap.md#split), deciding to recursively split the left subtree or the right subtree going down according to the subtree size or key value. The difference is that the WBLT needs to **merge** the split subtrees to maintain the balance of the final split tree.

The reference implementation of splitting by subtree size is as follows:

???+ example "Reference code"
    ```cpp
    --8<-- "docs/ds/code/wblt/wblt-2.cpp:split"
    ```

The time complexity is $O(\log n)$.

??? note "Complexity proof"
    The number of levels recursing down obviously does not exceed the tree height, which is $O(\log n)$. What needs to be proved is that the complexity of merging the subtrees split out on the left and right sides respectively is $O(\log n)$. We may as well consider only the left-side subtree, because the right side is symmetric. Let the subtrees split out on the left side, from bottom to top, be $T_1,T_2,\cdots,T_\ell$; the number of these subtrees $\ell\in O(\log n)$. The merge process can be described as, starting from $T'_1=T_1$, merging $T'_{i-1}$ with $T_i$ to get $T'_i$, recursively merging all subtrees. The total complexity of merging can be expressed as
    
    $$
    \sum_{i=2}^\ell \tau(T_i,T'_{i-1}),
    $$
    
    where $\tau(T_i,T'_{i-1})$ is the complexity of merging $T_i$ and $T'_{i-1}$.
    
    If it is always the case that $w(T_i)\ge w(T'_{i-1})$, then by the complexity expression for merging two subtrees, we have
    
    $$
    \tau(T_i,T'_{i-1}) \in O\left(\log\dfrac{w(T_i)}{w(T'_{i-1})}\right) \subseteq O\left(\log\dfrac{w(T'_i)}{w(T'_{i-1})}\right).
    $$
    
    Because the constants in these big-$O$ notations are all consistent, they can be added directly, telescoping.
    
    But, it should be noted that $w(T_i)\ge w(T'_{i-1})$ does not always hold, because $T'_{i-1}$ is split out from the right subtree corresponding to $T_i$ in the original tree, and this right subtree may be larger than the left subtree $T_i$. Nevertheless, even if $T'_{i-1}$ is larger than $T_i$, as part of the right subtree, the weight $w(T'_{i-1})$ does not exceed $(1-\alpha)/\alpha$ times $w(T_i)$, which means that at this point $T'_{i-1}$ and $T_i$ must be balanced, and the merge complexity is $O(1)$.
    
    Summarizing these two cases together, the complexity of a single merge can be written as
    
    $$
    \tau(T_i,T'_{i-1}) \in O\left(\log\dfrac{w(T'_i)}{w(T'_{i-1})}\right) + O(1).
    $$
    
    From this, the total complexity of merging is
    
    $$
    O\left(\sum_{i=2}^\ell\left( 1+\log\dfrac{w(T'_i)}{w(T'_{i-1})}\right) \right) \subseteq O(\ell+\log w(T'_\ell)) \subseteq O(\log n).
    $$
    
    This also shows that the total complexity of the split algorithm is $O(\log n)$.

## Reference implementation

This article introduced how to use the WBLT to complete the basic operations of a balanced tree. Below is the [ordinary balanced tree template](https://loj.ac/p/104) implemented with the WBLT.

??? example "Reference code"
    ```cpp
    --8<-- "docs/ds/code/wblt/wblt-1.cpp:full-text"
    ```

Using merging and splitting, one can also implement the literary balanced tree. Below is the [literary balanced tree template](https://loj.ac/p/105) implemented with the WBLT, which needs to push down the lazy tag when accessing nodes downward.

??? example "Reference code"
    ```cpp
    --8<-- "docs/ds/code/wblt/wblt-2.cpp:full-text"
    ```

Note that the WBLT needs twice the space; when splitting and merging are involved, note garbage collection, reclaiming useless nodes in time, otherwise the space is not linear.

## References and notes

-   [Weight-balanced tree - Wikipedia](https://en.wikipedia.org/wiki/Weight-balanced_tree)
-   Nievergelt, J.; Reingold, E. M. (1973). "Binary Search Trees of Bounded Balance". SIAM Journal on Computing. 2: 33–43.
-   Blum, Norbert; Mehlhorn, Kurt (1980). "On the average number of rebalancing operations in weight-balanced trees". Theoretical Computer Science. 11 (3): 303–320.
-   Hirai, Y.; Yamamoto, K. (2011). "Balancing weight-balanced trees". Journal of Functional Programming. 21 (3): 287.
-   Blelloch, Guy E.; Ferizovic, Daniel; Sun, Yihan (2016), "Just Join for Parallel Ordered Sets", Symposium on Parallel Algorithms and Architectures, Proc. of 28th ACM Symp. Parallel Algorithms and Architectures (SPAA 2016), ACM, pp. 253–264.
-   Straka, Milan. (2011). "Adams' Trees Revisited: Correctness Proof and Efficient Implementation." International Symposium on Trends in Functional Programming. Berlin, Heidelberg: Springer Berlin Heidelberg.

[^wrong-range]: The parameter range $\alpha < 1-\dfrac{\sqrt{2}}{2},~\beta=\dfrac{1-2\alpha}{1-\alpha}$ given in the original paper of Nievergelt and Reingold is wrong. Hirai and Yamamoto's article provides the corresponding counterexample; the problem mainly appears on some very small trees, thereby causing the whole inductive proof to fail. Of course, in actual algorithm competitions, it is hard to construct data that can break these wrong parameters, so in practice it may not have too much impact.

[^merge-complexity-cmp]: Because a single balance operation is at most equivalent to connecting two subtrees, and when the two subtrees are finally balanced it still needs to call the subtree-connection algorithm once, so if counted by the number of calls to the subtree-connection algorithm, the constants of the balance-based merge operation and the directly-merging balance operation algorithm below are consistent.

[^more-join]: Through the later proof, we can see that: in the third case, $z$ and $w+y$ are always balanced; in the fourth case, $z$ and $u$ are always balanced. They can both be directly connected, without needing to merge.
