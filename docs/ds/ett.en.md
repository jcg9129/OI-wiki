author: Backl1ght

The Euler Tour Tree (ETT) is a data structure that can solve **dynamic tree** problems. ETT converts operations on a dynamic tree into interval operations on its DFS sequence, and then uses other data structures to maintain the interval operations of the sequence, thereby maintaining the operations of the dynamic tree. For example, ETT converts the add-edge operation of a dynamic tree into several sequence-split operations and sequence-merge operations; if we can maintain sequence-split operations and sequence-merge operations, we can maintain the add-edge operation of the dynamic tree.

The LCT is also a data structure that can solve dynamic tree problems; compared with ETT, the LCT is more common. The LCT is actually more suitable for maintaining tree-chain information, while ETT is more suitable for maintaining **subtree** information. For example, ETT can maintain the subtree minimum while the LCT cannot.

ETT can be maintained with any data structure, as long as that data structure supports the corresponding sequence interval operations and meets the complexity requirements. In general, one uses balanced binary search trees such as Splay or Treap to maintain the sequence, and these data structures maintain interval operations in $O(\log n)$ complexity, whereby the operations of the dynamic tree can also be maintained in $O(\log n)$ time. If a multiway balanced search tree such as a B-tree is used to maintain the interval operations, one can achieve even better complexity.

In fact, ETT can be understood as an idea, namely achieving the goal of maintaining the original tree by maintaining some sequence in one-to-one correspondence with the original tree; what this article introduces is only some feasible implementations and applications of this idea.

## Euler-tour representation of a tree

If we regard a tree edge as two directed edges, then we can represent a tree as the Euler tour of a directed graph, called the Euler tour representation (ETR) of the tree.

The sequence to be maintained later is actually a variant of the ETR, which also regards a point in the tree as a self-loop and adds it to the ETR; but since the author of the original paper did not give it a new name, we will still call it ETR.

The Euler-tour representation of a tree $T$ can be obtained by the following algorithm:

$$
\begin{array}{ll}
1 & \textbf{Input. } \text{A rooted tree }T\\
2 & \textbf{Output. } \text{The dfs sequence of rooted tree }T\\
3 & \operatorname{ET}(u)\\
4 & \qquad \text{visit vertex }u\\
5 & \qquad \text{for all child } v \text{ of } u\\
6 & \qquad \qquad \text{visit directed edge } u \to v\\
7 & \qquad \qquad \operatorname{ET}(v)\\
8 & \qquad \qquad \text{visit directed edge } v \to u\\
\end{array}
$$

The Euler-tour representation $\operatorname{ETR}(T)$ of the tree $T$ is initially empty; during the DFS, each time a node or a directed edge is visited, it is added to the tail of $\operatorname{ETR}(T)$, thus obtaining $\operatorname{ETR}(T)$.

If $T$ contains $n$ nodes, then it contains $2n - 2$ directed edges, and during the DFS each point and each directed edge is visited once, so the length of $\operatorname{ETR}(T)$ is $3n - 2$.

Regarding a point $u$ as a self-loop, $\operatorname{ETR}(T)$ can be seen as an Euler tour in a directed graph. One can break the Euler tour at some place and view it as a chain formed by some edges connected head-to-tail; one can also reglue such a chain at the break point to turn it back into an Euler tour; one can also, by adding some edges, piece together two such chains into a new Euler tour.

In the following, unless otherwise stated, the maintained sequence is by default the Euler-tour representation of the tree.

## Basic operations of ETT

The following 3 operations can be regarded as the basic operations of ETT; all can be converted into a constant number of sequence operations, so the complexity of these 3 operations is of the same order as the sequence operations.

What is given here is only one feasible implementation; it suffices to piece together the sequence corresponding to the modification with a constant number of sequence operations.

### MakeRoot(u)

That is, the reroot operation. The reroot operation in ETT is converted into 1 sequence-split operation and 1 sequence-merge operation; it can also be understood as 1 interval-translation operation.

Let the tree containing point $u$ be $T$, with its current root $r$; now we want to change the root to $u$. Let the sequence corresponding to tree $T$ be $L$; split $L$ at $(u, u)$ into sequences $L^1$ and $L^2$, where the former contains the elements of $L$ before $(u, u)$ as well as $(u, u)$, and the latter contains the remaining elements. Then the sequence obtained by merging $L^2$ and $L^1$ in turn is the sequence corresponding to the tree after rerooting.

This can be understood as performing a rotation operation on an Euler tour; the Euler tour is a cycle, and rotating it does not change the structure of the Euler tour, i.e. does not change the structure of the tree, only rotates point $u$ to the root position.

### Insert(u, v)

That is, the add-edge operation. The add-edge operation in ETT is converted into 2 sequence-split operations and 5 sequence-merge operations.

Let the tree containing point $u$ be $T_1$ and the tree containing point $v$ be $T_2$; after adding the edge, the two trees merge into one tree $T$. Let the sequence corresponding to tree $T_1$ be $L_1$ and the sequence corresponding to tree $T_2$ be $L_2$.

Split $L_1$ at $(u, u)$ into sequences $L_1^1$ and $L_1^2$, where the former contains the elements of $L_1$ before $(u, u)$ as well as $(u, u)$, and the latter contains the remaining elements. Similarly, split $L_2$ at $(v, v)$ into sequences $L_2^1$ and $L_2^2$. Then merging $L_1^2, L_1^1, [(u, v)], L_2^2, L_2^1, [(v, u)]$ in turn gives the sequence $L$ corresponding to tree $T$.

This can be understood as two reroot operations, then breaking the two Euler tours at the position of the current root, and using the two newly added directed edges to piece the two Euler tours into a new Euler tour.

### Delete(u, v)

That is, the delete-edge operation. The delete-edge operation in ETT is converted into 4 sequence-split operations and 1 sequence-merge operation.

Let the tree containing edge $(u, v)$ and edge $(v, u)$ be $T$, with its corresponding sequence $L$. After deleting the edge, $T$ splits into two trees.

Split $L$ into $L_1, [(u, v)], L_2, [(v, u)], L_3$; the sequences corresponding to the two trees formed by deleting the edge are $L_2$ and $L_1, L_3$ respectively. Note that in the sequence $L$, $[(u, v)]$ may appear after $[(v, u)]$; in this case one can first swap the values of $u$ and $v$ and then operate.

This can be understood as breaking an Euler tour at the two directed edges to form two chains, and then the two chains each connect head-to-tail to form two new Euler tours.

## Implementation

Below we introduce the implementation of ETT using a non-rotating Treap as an example; the reader is required to have prior knowledge of the relevant content of using a non-rotating Treap to maintain interval operations.

`Split` and `Merge` are basic operations of a non-rotating Treap and are not belabored here.

### SplitUp2(u)

Suppose the sequence $u$ is in is $L$; split $L$ at $u$ into sequences $L^1$ and $L^2$, where the former contains the elements of $L$ before $u$ as well as $u$, and the latter contains the remaining elements.

If each node of the Treap additionally maintains its own parent, then one can compute the position in the sequence of the element corresponding to a Treap node in $O(\log n)$ time, and then `Split` according to the position to achieve the above functionality.

One can also split bottom-up to achieve the above functionality, which is more efficient than the above method. Specifically, in the process of jumping from the node corresponding to $u$ up to the root, by the property of a binary search tree one can determine whether each node is before or after $u$ in $L$; based on this, one can compute the position of $u$ in the sequence and also determine which of the trees after splitting each node belongs to.

```cpp
/*
 * Bottom up split treap p into 2 treaps a and b.
 *   - a: a treap containing nodes with position less than or equal to p.
 *   - b: a treap containing nodes with postion greater than p.
 *
 * In the other word, split sequence containning p into two sequences, the first
 * one contains elements before p and element p, the second one contains
 * elements after p.
 */
static std::pair<Node*, Node*> SplitUp2(Node* p) {
  Node *a = nullptr, *b = nullptr;
  b = p->right_;
  if (b) b->parent_ = nullptr;
  p->right_ = nullptr;

  bool is_p_left_child_of_parent = false;
  bool is_from_left_child = false;
  while (p) {
    Node* parent = p->parent_;

    if (parent) {
      is_p_left_child_of_parent = (parent->left_ == p);
      if (is_p_left_child_of_parent) {
        parent->left_ = nullptr;
      } else {
        parent->right_ = nullptr;
      }
      p->parent_ = nullptr;
    }

    if (!is_from_left_child) {
      a = Merge(p, a);
    } else {
      b = Merge(b, p);
    }

    is_from_left_child = is_p_left_child_of_parent;
    p->Maintain();
    p = parent;
  }

  return {a, b};
}
```

### SplitUp3(u)

Suppose the sequence $u$ is in is $L$; split $L$ at $u$ into sequences $L^1$, $u$, and $L^2$, where the former contains the elements of $L$ before $u$, and the latter contains the remaining elements.

Just slightly modify `SplitUp2`.

### MakeRoot(u)

Easily obtained based on `SplitUp2` and `Merge`.

```cpp
void MakeRoot(int u) {
  Node* vertex_u = vertices_[u];
  auto [L1, L2] = Treap::SplitUp2(vertex_u);
  Treap::Merge(L2, L1);
}
```

### Insert(u, v)

Easily obtained based on `SplitUp2` and `Merge`.

```cpp
void Insert(int u, int v) {
  Node* vertex_u = vertices_[u];
  Node* vertex_v = vertices_[v];

  Node* edge_uv = AllocateNode(u, v);
  Node* edge_vu = AllocateNode(v, u);
  tree_edges_[u][v] = edge_uv;
  tree_edges_[v][u] = edge_vu;

  auto [L11, L12] = Treap::SplitUp2(vertex_u);
  auto [L21, L22] = Treap::SplitUp2(vertex_v);

  Node* L = L12;
  L = Treap::Merge(L, L11);
  L = Treap::Merge(L, edge_uv);
  L = Treap::Merge(L, L22);
  L = Treap::Merge(L, L21);
  L = Treap::Merge(L, edge_vu);
}
```

### Delete(u, v)

Easily obtained based on `SplitUp3` and `Merge`.

```cpp
void Delete(int u, int v) {
  Node* edge_uv = tree_edges_[u][v];
  Node* edge_vu = tree_edges_[v][u];
  tree_edges_[u].erase(v);
  tree_edges_[v].erase(u);

  int position_uv = Treap::GetPosition(edge_uv);
  int position_vu = Treap::GetPosition(edge_vu);
  if (position_uv > position_vu) {
    std::swap(edge_uv, edge_vu);
    std::swap(position_uv, position_vu);
  }

  auto [L1, uv, _] = Treap::SplitUp3(edge_uv);
  auto [L2, vu, L3] = Treap::SplitUp3(edge_vu);
  Treap::Merge(L1, L3);

  FreeNode(edge_uv);
  FreeNode(edge_vu);
}
```

## Maintaining connectivity

Points $u$ and $v$ are connected if and only if the two points belong to the same tree $T$, i.e. $(u, u)$ and $(v, v)$ belong to $\operatorname{ETR}(T)$; this can be determined by whether the roots of the Treaps that the Treap nodes corresponding to points $u$ and $v$ are in are the same.

### Example [P2147 \[SDOI2008\] Cave Survey](https://www.luogu.com.cn/problem/P2147)

A template problem for maintaining connectivity.

??? note "Reference code"
    ```cpp
    --8<-- "docs/ds/code/ett/ett_connectivity.cpp"
    ```

## Maintaining subtree information

Below we illustrate using the number of subtree nodes as an example.

For each element in $\operatorname{ETR}(T)$, if this element corresponds to a point in the tree, let its weight be $1$; if this element corresponds to an edge in the tree, let its weight be $0$. Now the number of nodes of tree $T$ can be seen as the weight sum of the elements in $\operatorname{ETR}(T)$, and one only needs to additionally maintain the sequence's weight sum to maintain the number of subtree nodes. And maintaining the sequence's weight sum is a classic operation of a non-rotating Treap.

Similarly, operations such as the subtree minimum can be converted into balanced-tree classic operations such as the sequence minimum and then maintained.

### Example [LOJ #2230 「BJOI2014」Great Merger](https://loj.ac/p/2230)

??? note "Reference code"
    ```cpp
    --8<-- "docs/ds/code/ett/ett_subtree_size.cpp"
    ```

## Maintaining tree-chain information

One can use a rather common technique of converting tree-chain information into interval information by means of the property of the bracket sequence, and then one can maintain the sequence by means of a data structure to maintain the tree-chain information. But this technique requires the maintained information to satisfy **subtractability**.

The sequence operations corresponding to the dynamic-tree operations introduced earlier may move a closing bracket in the bracket sequence before an opening bracket, so when maintaining information such as a tree-chain vertex-weight sum, one needs to additionally note that the operations must not change the order of the corresponding opening and closing brackets, and this may require rethinking the sequence operations corresponding to the dynamic-tree operations, or even rethinking which DFS sequence to maintain.

In addition, ETT has difficulty maintaining tree-chain modifications.

### Example ["Interstellar Exploration"](https://hydro.ac/p/bzoj-P3786)

The dynamic-tree operations of this problem are only changing the parent, which can be seen as deleting an edge and then adding an edge, but this may change the order of the corresponding brackets.

One can convert vertex weights into edge weights, maintain the bracket sequence of the tree, and convert the change-parent operation into translating the bracket sequence corresponding to the entire subtree to after the parent's opening bracket.

??? note "Reference code"
    ```cpp
    --8<-- "docs/ds/code/ett/ett_1.cpp"
    ```

## References

-   Dynamic trees as search trees via euler tours, applied to the network simplex algorithm - Robert E. Tarjan
-   Randomized fully dynamic graph algorithms with polylogarithmic time per operation - Henzinger et al.
