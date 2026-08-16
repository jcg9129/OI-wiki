author: abc1763613206, cesonic, Ir1d, MingqiHuang, xinchengo, xiaofu-15191, hsefz-ChenJunJie

## Introduction

What is a heuristic algorithm?

A heuristic algorithm is an optimization of some algorithms based on human experience and intuition.

For example, the most common one is the heuristic merging of a DSU; the code is like this:

```cpp
void merge(int x, int y) {
  int xx = find(x), yy = find(y);
  if (size[xx] < size[yy]) swap(xx, yy);
  fa[yy] = xx;
  size[xx] += size[yy];
}
```

Here, for two sets of different sizes, we merge the smaller set into the larger set, rather than merging the larger set into the smaller set.

Why? The size of this set can be regarded as the height of the set (under normal circumstances), and merging a set of smaller height into one of larger height obviously helps us find the parent.

Making a tree of smaller height become a subtree of a tree of larger height, this optimization can be called the heuristic merging algorithm.

## Algorithm content

Heuristic merging on a tree (dsu on tree) is an algorithm that, for some offline tree problems, can be faster than or equal to most algorithms and is easier to understand and implement.

Consider the following problem: [Counting Colors on a Tree](https://www.luogu.com.cn/problem/U41492).

???+ note "Example problem introduction"
    Given a tree with $n$ nodes rooted at $1$, the color of node $u$ is $c_u$; now for each node $u$, query how many different colors appear in total in the subtree rooted at $u$.
    
    $n\le 2\times 10^5$.

![dsu-on-tree-1.png](./images/dsu-on-tree-1.svg)

For this kind of problem, the solution methods are mostly to use a large number of data structures (trees of trees, etc.); if it can be done offline, is there a simpler method?

## Process

Since it supports offline, consider outputting the answer in $O(1)$ after preprocessing.

The time complexity of direct brute-force preprocessing is $O(n^2)$, i.e. performing one traversal for each child node; the complexity of each traversal is obviously of the same order as $n$, and there are $n$ nodes, so the complexity is $O(n^2)$.

We can find that the answer of each node is obtained from its subtree and itself; consider using this property to handle the problem.

We can first preprocess the size of the subtree of each node and its heavy child; the heavy child, same as in heavy-path decomposition, is the child with the subtree containing the most nodes; this process can obviously be completed in $O(n)$.

We use $cnt_i$ to denote the number of occurrences of color $i$, and $ans_u$ to denote the answer of node $u$.

When traversing a node $u$, we traverse according to the following steps:

1.  First traverse the light (non-heavy) children of $u$ and compute the answer, but **do not retain their effect on the $cnt$ array after traversal**;
2.  Traverse its heavy child, **retaining its effect on the $cnt$ array**;
3.  Traverse the subtree nodes of $u$'s light children again, adding the contributions of these nodes to obtain the answer of $u$.

![dsu-on-tree-2.png](./images/dsu-on-tree-2.svg)

The figure above is an example.

In this way, for a node, we traversed the heavy subtree once and the non-heavy subtrees twice, which is obviously the most cost-effective.

By executing this process, we obtain the answers of all subtrees of this node.

Why not merge the first step and the third step? Because the $cnt$ array cannot be reused, otherwise the space would be too large; it needs to be completed within $O(n)$ space.

Obviously if a node $u$ is traversed $x$ times, then its heavy child will be traversed $x$ times, and its light children (if any) will be traversed $2x$ times.

Note that except for the heavy child, after each traversal the $cnt$ must be cleared to zero.

## Proof

We define heavy edges and light edges the same as in heavy-path decomposition (the edge connecting to the heavy child is a heavy edge, and the rest are light edges). For the definition of the heavy child and heavy edge, see the figure below; for a tree with $n$ nodes:

The number of light edges from the root node to any node on the tree does not exceed $\log n$. We let there be $x$ light edges from the root to that node and the subtree size of that node be $y$; obviously the subtree size of the child node connected by a light edge is less than half of the parent's (if greater than half it would not be a light edge), so $y<n/2^x$; obviously $n>2^x$, so $x<\log n$.

And because if a node is the heavy child of its parent, then its subtree must be the largest among its siblings, so all parent nodes connected by heavy edges on the path from any node to the root will definitely not traverse this node when computing the answer, so the number of times a node is traversed equals the number of light edges on the path from it to the root node $+1$ (the reason for $+1$ is that it itself needs to be traversed), so the number of times a node is traversed $=\log n+1$; the total time complexity is then $O(n(\log n+1))=O(n\log n)$, and outputting the answers costs $O(m)$.

![dsu-on-tree-3.png](./images/dsu-on-tree-3.svg)

*The bold edges in the figure are heavy edges, and the child nodes connected by heavy edges are heavy children*

## Optimization

In the proof process it is mentioned that dsu on tree uses the light/heavy-child concept from heavy-path decomposition to accelerate merging. Since this is so, we can also directly use the dfs order obtained from heavy-path decomposition, turning recursion into iteration, to further optimize the constant factor of dsu on tree.

The dfs order itself has the following property: the subtree of a node is definitely continuous in the dfs order. Therefore, one can traverse the dfs-order array in reverse order. This guarantees that when traversing to a node, the other nodes in its subtree have definitely already been processed.

The dfs order obtained from heavy-path decomposition has the following excellent property: a heavy chain is definitely continuous in the dfs order. Therefore, when traversing nodes in reverse dfs order, for the node at the top of a heavy chain, the next node to traverse is definitely not the parent of this node, so its effect must be cleared; besides this, for nodes not at the top of a heavy chain, the previous node traversed is either its own heavy child, or a node of another branch whose effect has already been cleared, so its effect can be directly inherited. On this basis, use the dfs order to quickly count the effects of all light children, and record the answer.

The above process is called the non-recursive/iterative implementation of dsu on tree (also called the dfs-order implementation of dsu on tree). Compared with the original recursive implementation, it reduces the time and space overhead of recursively calling functions, obtaining a considerable constant-factor optimization, **especially when handling trees containing a large number of chain-shaped structures, it has a significant stack-space advantage.**

## Implementation

??? example "Reference implementation"
    === "Recursive implementation"
        ```cpp
        --8<-- "docs/graph/code/dsu-on-tree/dsu-on-tree_1.cpp"
        ```
    
    === "Non-recursive implementation"
        ```cpp
        --8<-- "docs/graph/code/dsu-on-tree/dsu-on-tree_2.cpp"
        ```

## Applications

1.  Some problems whose intended solution set by the problem setter is dsu on tree

    Such as [CF741D](http://codeforces.com/problemset/problem/741/D). Given a tree, the weight of each node is a letter from 'a' to 'v'; each query requires finding a path in a subtree such that the characters contained in this path, after sorting, become a palindrome.

    Because it becomes a palindrome after arrangement, a character appearing twice is equivalent to not appearing, that is to say, this path satisfies that **at most one character appears an odd number of times**.

    The normal approach is to dfs each node; at each node, forcibly enumerate all letters to find paths whose count of results after XOR being 1 is greater than 1, and then take the longest value; this is $O(n^2\log n)$, which can be optimized to $O(n\log^2n)$ with dsu on tree. For the specific approach, refer to the extended reading below.

2.  Problems that can be casually handled with dsu

    One can scrape some partial score of trees of trees (without modification operations), and the complexity of dsu is better than the $O(n\sqrt{m})$ of Mo's algorithm on a tree.

## Practice problems

[CF600E Lomsat gelral](http://codeforces.com/problemset/problem/600/E)

Problem translation: the nodes of a tree have colors; a color occupies a subtree if and only if no other color appears more than it in this subtree. Find the sum of all colors occupying each subtree.

[UOJ284 Happy Game Chicken](https://uoj.ac/problem/284)

[CF1709E XOR Tree](https://codeforces.com/contest/1709/problem/E)

## References / extended reading

[dsu on tree introduced by the author of CF741D](http://codeforces.com/blog/entry/44351)

[This author's solution](http://codeforces.com/blog/entry/48871)
