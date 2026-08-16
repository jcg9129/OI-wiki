author: isdanni,xyf007

The PQ tree is a tree-based data structure representing a family of permutations over a set of elements, discovered and named by Kellogg S. Booth and George S. Lueker in 1976, used to solve the following problem

> Given $m$ sets $S_i$, you need to find a permutation of $1\sim n$ such that the elements within each set are adjacent.

A PQ tree can be constructed in $O(n+\sum|S_i|)$ time. The construction method introduced in this article has time complexity $O(nm)$.

## Definition

A PQ tree has three kinds of nodes: **leaf nodes**, **P nodes**, and **Q nodes**. A leaf node represents an element in the permutation, a P node indicates that its child nodes can be arranged arbitrarily, and a Q node indicates that the order of its children can be reversed. All non-leaf nodes are either P nodes or Q nodes. A P node has at least 2 children, and a Q node has at least 3 children.  
Because of the definition of the nodes, the PQ tree itself represents **all** valid schemes, and its preorder traversal is one of them.  
The figure below is a PQ tree.  
![](https://gregable.com/2008/11/i/pq-tree.webp)  
Its preorder traversal 1,2,3,4,5 represents a valid scheme. If the children of the P node are rearranged to 4,2,3, we get another valid scheme 1,4,2,3,5. Keeping the order of the P node's children unchanged and reversing the order of the Q node's children, we get another valid scheme 5,3,2,4,1.

## Construction

**The PQ tree uses the child-sibling representation.**

We construct a PQ tree incrementally.

First establish a tree whose root is a P node with a total of $n$ children, namely $1,2,\ldots,n$, representing the PQ tree when there are no constraints. As constraints are continuously added, we continuously modify this tree.

When adding a new constraint set $S$, we mark all leaf nodes belonging to this set as **black**, and leaf nodes not in this set as **white**. For all non-leaf nodes, if all their children are black, mark them also black; if all their children are white, mark them also white; otherwise mark them as **grey**. In the figures below, black nodes, white nodes, and grey nodes are represented by black, grey, and half-black-half-grey respectively.

We require that the nodes in the PQ tree be sorted by color.

### Bottom-up method

The smallest subtree containing all black nodes is called the **pertinent subtree**, and the root of the pertinent subtree (not necessarily the root of the whole tree) is called the **pertinent root**.

The process of adding a constraint is called a reduction. A reduction is divided into two phases: the bubbling phase and the reduction phase.

#### Bubbling phase

The bubbling phase only handles the pertinent subtree. We mark all nodes in the pertinent subtree as black or grey, and compute for each node the number of pertinent child nodes it has. To complete this process efficiently, we process the pertinent subtree from the leaves toward the root. This requires recording the parent node of each point, but in the reduction phase a point's parent node often needs to be modified. To construct in linear time, only the children of a P node and the **last child of a Q node** always record the correct parent node. For the other children of a Q node, in the bubbling phase we update their parent with the last child's parent.

When encountering an intermediate node, we look at whether its siblings already have a valid parent node. If not, mark it as **blocked**. If later its siblings have a valid parent, then modify this node's parent and cancel the mark. If at the end of the bubbling phase there is still a contiguous segment of blocked nodes (as in case Q3 below), a parentless "pseudo-node" becomes the parent of that block, and is removed in the reduction phase.

#### Reduction phase

The reduction phase uses a queue to process nodes. First add all leaf nodes within the constraint to the queue. Each time take out the front node $u$ from the queue and process it. If $u$'s parent is also a node within the pertinent subtree, then enqueue $\mathit{fa}_u$.  
For each node $u$, we discuss by cases. If it does not belong to any of these cases, then there is no solution.

##### Leaf node

Mark $u$ black.

##### P node

If all children are black, mark $u$ black.  
![](https://gregable.com/2008/11/i/p1-template.png)  
![](https://gregable.com/2008/11/i/p1-replacement.png)

If $u$ has both black and white children, and $u$ is the pertinent root, then create a new P node $v$ to become the root of all its black children.  
![](https://gregable.com/2008/11/i/p2-template.png)  
![](https://gregable.com/2008/11/i/p2-replacement.png)

If $u$ has both black and white children, and $u$ is not the pertinent root, then do the following operations:

-   Create a new P node $f$ to become the root of all black children.
-   Create a new P node $e$ to become the root of all white children.
-   If $e$ (and/or $f$) has only one child, then do not create a new node, but directly assign $e$ (and/or $f$) to that child.
-   Change $u$ into a Q node and set its children to $e$ and $f$, and mark it grey.

Note that according to the earlier definition, a Q node has at least 3 children, so here $u$ is regarded as a "pseudo-node" and will be further processed later.  
![](https://gregable.com/2008/11/i/p3-template.png)  
![](https://gregable.com/2008/11/i/p3-replacement.png)

If $u$ has a grey child $p$, and $u$ is the pertinent root, then create a new P node $v$ as the root of all its black children, set $v$'s sibling to $p$'s last black child, then set $v$ as $p$'s last child.  
![](https://gregable.com/2008/11/i/p4-template.png)  
![](https://gregable.com/2008/11/i/p4-replacement.png)

If $u$ has a grey child $p$, and $u$ is not the pertinent root, then perform the following operations:

-   Create a new P node $f$ to become the root of all black children.
-   Create a new P node $e$ to become the root of all white children.
-   If $e$ (and/or $f$) has only one child, then do not create a new node, but directly assign $e$ (and/or $f$) to that child.
-   Set $e$'s sibling to $p$'s last white child, then set $e$ as $p$'s last child.
-   Set $f$'s sibling to $p$'s last black child, then set $f$ as $p$'s last child.

![](https://gregable.com/2008/11/i/p5-template.png)  
![](https://gregable.com/2008/11/i/p5-replacement.png)

If $u$ has exactly two grey children $p_1,p_2$, then perform the following operations:

-   Create a new P node $f$ to become the root of all black children.
-   If $f$ has only one child, then do not create a new node, but directly assign $f$ to that child.
-   Set the sibling of $p_1$'s last black child to $f$.
-   Set $f$'s sibling to $p_2$'s last black child.
-   Set $p_2$'s last child to $p_2$'s last white child.

It can be found that in this way $p_2$ is merged into $p_1$.  
![](https://gregable.com/2008/11/i/p6-template.png)  
![](https://gregable.com/2008/11/i/p6-replacement.png)

##### Q node

If $u$ has only black children, then mark $u$ black. (The shape of the figure below is wrong.)  
![](https://gregable.com/2008/11/i/q1-template.png)  
![](https://gregable.com/2008/11/i/q1-replacement.png)

If $u$ has a grey child $p$, and all children with the same mark appear contiguously, then perform the following operations:

-   Let $p_f$ be $p$'s last black child, $p_e$ be $p$'s last white child, $f$ be $p$'s black sibling, and $e$ be $p$'s white sibling.
-   Set $f$'s sibling to $p_f$, and $e$'s sibling to $p_e$.
-   If $p$ has no white sibling or black sibling, set $u$'s last child to $p$'s last child.
-   Delete $p$.

![](https://gregable.com/2008/11/i/q2-template.png)  
![](https://gregable.com/2008/11/i/q2-replacement.png)

If $u$ has exactly two grey children $p_1,p_2$, and all children with the same mark appear contiguously, then just perform the previous operation on both $p_1,p_2$.  
![](https://gregable.com/2008/11/i/q3-template.png)  
![](https://gregable.com/2008/11/i/q3-replacement.png)

This construction method is from the original paper, but is relatively inconvenient to implement.

### Top-down method

The implementations in OI mostly adopt this method. Actually the method is similar; the cases appearing below can basically all be found above.

Note that according to the earlier coloring process, all black and white points already satisfy the conditions, so we **only need to handle grey nodes**.

#### P node

-   If $u$ has more than two grey children, there is no solution.
-   If $u$ has only one grey child and no black children, recursively handle the grey child.
-   Otherwise first clear $u$'s children, then add all white children. Create a new Q node $q_1$ and make it a child of $u$. Add all grey children into $q_1$. Create a new P node $p$ as the root of all black children, and insert $p$ into the middle of $q_1$. (This corresponds to all cases of the P node in the bottom-up method.)

Note that we require the two grey nodes to have all white on the left and all black on the right (or vice versa), so we need to implement a split function `split`, which can split the points of this subtree into black and white parts, while retaining **all possibilities** of the nodes of the split subtree.

#### Q node

-   Find the positions $l,r$ of the leftmost and rightmost non-white nodes. If there is a non-black node within $[l+1,r-1]$, there is no solution.
-   If there are no black nodes and only one grey node, recursively handle this grey node; otherwise just split the nodes at positions $l$ and $r$.

#### Split function

Let the point to be split be $u$; we want to split $u$ into a forest with all white on the left and all black on the right. If $u$ is not a grey node then directly return the subtree. Consider only the case of a grey node.
If $u$ is a P-type node:

-   If $u$ has at least two grey children, then there is no solution.
-   Otherwise the left is all white children, the middle recursively handles the grey child, and the right is all black children. Note that to retain all possibilities, we need to create two new P nodes as the roots of the white children and black children respectively. (This corresponds to the P4 case of the bottom-up method.)
-   Delete $u$.

If $u$ is a Q-type node:

-   If neither the forward order nor the reverse order satisfies white-grey-black, then there is no solution.
-   If there are at least two grey children, there is also no solution.
-   Otherwise just recursively split the grey child.
-   Delete $u$.

Finally delete all redundant nodes (nodes with only one child).

## Code implementation

```cpp
class PQTree {
 public:
  PQTree() {}

  void Init(int n) {
    n_ = n, rt_ = tot_ = n + 1;
    for (int i = 1; i <= n; i++) g_[rt_].emplace_back(i);
  }

  void Insert(const std::string &s) {
    s_ = s;
    Dfs0(rt_);
    Work(rt_);
    while (g_[rt_].size() == 1) rt_ = g_[rt_][0];
    Remove(rt_);
  }

  std::vector<int> ans() {
    DfsAns(rt_);
    return ans_;
  }

  ~PQTree() {}

 private:
  int n_, rt_, tot_, pool_[100001], top_, typ_[100001] /* 0-P 1-Q */,
      col_[100001] /* 0-black 1-white 2-grey */;
  std::vector<int> g_[100001], ans_;
  std::string s_;

  void Fail() {
    std::cout << "NO\n";
    std::exit(0);
  }

  int NewNode(int ty) {
    int x = top_ ? pool_[top_--] : ++tot_;
    typ_[x] = ty;
    return x;
  }

  void Delete(int u) { g_[u].clear(), pool_[++top_] = u; }

  void Dfs0(int u) {  // get color of each node
    if (u >= 1 && u <= n_) {
      col_[u] = s_[u] == '1';
      return;
    }
    bool c0 = false, c1 = false;
    for (auto &&v : g_[u]) {
      Dfs0(v);
      if (col_[v]) c1 = true;
      if (col_[v] != 1) c0 = true;
    }
    if (c0 && !c1)
      col_[u] = 0;
    else if (!c0 && c1)
      col_[u] = 1;
    else
      col_[u] = 2;
  }

  bool Check(const std::vector<int> &v) {
    int p2 = -1;
    for (int i = 0; i < static_cast<int>(v.size()); i++)
      if (col_[v[i]] == 2) {
        if (p2 != -1) return false;
        p2 = i;
      }
    if (p2 == -1)
      for (int i = 0; i < static_cast<int>(v.size()); i++)
        if (col_[v[i]]) {
          p2 = i;
          break;
        }
    for (int i = 0; i < p2; i++)
      if (col_[v[i]]) return false;
    for (int i = p2 + 1; i < static_cast<int>(v.size()); i++)
      if (col_[v[i]] != 1) return false;
    return true;
  }

  std::vector<int> Split(int u) {
    if (col_[u] != 2) return {u};
    std::vector<int> ng;
    if (typ_[u]) {  // Q
      if (!Check(g_[u])) {
        std::reverse(g_[u].begin(), g_[u].end());
        if (!Check(g_[u])) Fail();
      }
      for (auto &&v : g_[u])
        if (col_[v] != 2) {
          ng.emplace_back(v);
        } else {
          auto s = Split(v);
          ng.insert(ng.end(), s.begin(), s.end());
        }
    } else {  // P
      std::vector<int> son[3];
      for (auto &&x : g_[u]) son[col_[x]].emplace_back(x);
      if (son[2].size() > 1) Fail();
      if (!son[0].empty()) {
        int n0 = NewNode(0);
        g_[n0] = son[0];
        ng.emplace_back(n0);
      }
      if (!son[2].empty()) {
        auto s = Split(son[2][0]);
        ng.insert(ng.end(), s.begin(), s.end());
      }
      if (!son[1].empty()) {
        int n1 = NewNode(0);
        g_[n1] = son[1];
        ng.emplace_back(n1);
      }
    }
    Delete(u);
    return ng;
  }

  void Work(int u) {
    if (col_[u] != 2) return;
    if (typ_[u]) {  // Q
      int l = 1e9, r = -1e9;
      for (int i = 0; i < static_cast<int>(g_[u].size()); i++)
        if (col_[g_[u][i]]) checkmin(l, i), checkmax(r, i);
      for (int i = l + 1; i < r; i++)
        if (col_[g_[u][i]] != 1) Fail();
      if (l == r && col_[g_[u][l]] == 2) {
        Work(g_[u][l]);
        return;
      }
      std::vector<int> ng;
      for (int i = 0; i < l; i++) ng.emplace_back(g_[u][i]);
      auto s = Split(g_[u][l]);
      ng.insert(ng.end(), s.begin(), s.end());
      for (int i = l + 1; i < r; i++) ng.emplace_back(g_[u][i]);
      if (l != r) {
        s = Split(g_[u][r]);
        std::reverse(s.begin(), s.end());
        ng.insert(ng.end(), s.begin(), s.end());
      }
      for (int i = r + 1; i < static_cast<int>(g_[u].size()); i++)
        ng.emplace_back(g_[u][i]);
      g_[u] = ng;
    } else {  // P
      std::vector<int> son[3];
      for (auto &&x : g_[u]) son[col_[x]].emplace_back(x);
      if (son[1].empty() && son[2].size() == 1) {
        Work(son[2][0]);
        return;
      }
      g_[u].clear();
      if (son[2].size() > 2) Fail();
      g_[u] = son[0];
      int n1 = NewNode(1);
      g_[u].emplace_back(n1);
      if (son[2].size() >= 1) {
        auto s = Split(son[2][0]);
        g_[n1].insert(g_[n1].end(), s.begin(), s.end());
      }
      if (son[1].size()) {
        int n2 = NewNode(0);
        g_[n1].emplace_back(n2);
        g_[n2] = son[1];
      }
      if (son[2].size() >= 2) {
        auto s = Split(son[2][1]);
        std::reverse(s.begin(), s.end());
        g_[n1].insert(g_[n1].end(), s.begin(), s.end());
      }
    }
  }

  void Remove(int u) {  // remove the nodes with only one child
    for (auto &&v : g_[u]) {
      int tv = v;
      while (g_[tv].size() == 1) {
        int t = tv;
        tv = g_[tv][0];
        Delete(t);
      }
      v = tv, Remove(v);
    }
  }

  void DfsAns(int u) {
    if (u >= 1 && u <= n_) {
      ans_.emplace_back(u);
      return;
    }
    for (auto &&v : g_[u]) DfsAns(v);
  }
} T;
```

## Exercises

-   [CF243E Matrix](https://codeforces.com/problemset/problem/243/E)
-   [CF1552I Organizing a Music Festival](https://codeforces.com/contest/1552/problem/I)

## References

-   Booth, Kellogg S. & Lueker, George S. (1976).["Testing for the consecutive ones property, interval graphs, and graph planarity using PQ-tree algorithms"](https://www.sciencedirect.com/science/article/pii/S0022000076800451?via%3Dihub).*[Journal of Computer and System Sciences](https://en.wikipedia.org/wiki/Journal_of_Computer_and_System_Sciences)*.**13**(3): 335–379.[doi](https://en.wikipedia.org/wiki/Doi_%28identifier%29):[10.1016/S0022-0000(76)80045-1](https://doi.org/10.1016%2FS0022-0000%2876%2980045-1).
-   [PQ Tree Algorithm and Consecutive Ones Problem](https://gregable.com/2008/11/pq-tree-algorithm.html)
-   [CF243E Matrix PQTree - RainAir's Blog](https://blog.aor.sd.cn/archives/1657/)
