author: Dev-XYS, ttzytt, Sora233, qwqAutomaton

Prerequisites: [naive binary search tree](./bst.md), [heap basics](./heap.md).

## Introduction

The Treap (tree heap) is a **weakly balanced** **binary search tree**.

Besides the maintained **weight** ($\textit{val}$), a Treap node additionally has a random **priority** ($\textit{priority}$). Among them, the weight satisfies the binary-search-tree property, and the priority satisfies the heap property (min-heap or max-heap).

Among them, the binary-search-tree property means:

-   The weights ($\textit{val}$) of all nodes in the left subtree are smaller than the parent node.
-   The weights ($\textit{val}$) of all nodes in the right subtree are larger than the parent node.

The heap property is:

-   The priority ($\textit{priority}$) of a child node is larger or smaller than the parent node (depending on whether it is a min-heap or a max-heap).

It is not hard to see that if the same value is used, then these two data structures will become a chain after combination, so on the basis of the search tree, we further introduce a value $\textit{priority}$ for the heap. For the $\textit{val}$ value, we maintain the search-tree property; for the $\textit{priority}$ value, we maintain the heap property. Among them, the $\textit{priority}$ value is given randomly.

The figure below is an example of a Treap (here a min-heap is used, i.e. the root node has the smallest priority).

![An example of a Treap](./images/treap-treap-example.svg)

So why do we need to go to such great lengths to make this data structure conform to the properties of a tree and a heap, and give the heap value randomly?

To understand this, we first need to understand the problem of the naive binary search tree. When inserting a new node into a naive search tree, we need to recurse from the root node of this search tree; if the new node is smaller than the current node, then recurse left, and vice versa.

Finally, when we find that the current node has no child node, we make the new node the left or right child of the current node according to the size of the new node's value.

If the weights of the inserted nodes are random (in other words, inserted randomly), then the height of this naive search tree is relatively small (close to $\log n$, where $n$ is the number of nodes), while the number of nodes in each layer is relatively large, i.e. its shape will be very "fat". The Treap in the figure above is an example. So at this point the complexity of any operation will be around $O(\log n)$.

However, this is only the complexity in the random case; if we insert nodes into a naive search tree in the following very ordered order:

```plain
1 2 3 4 5
```

then this tree will degenerate into a chain, i.e. become very "thin and tall" (each inserted node is larger than the previous one, so they are all assigned to the right child):

![Example of degenerating into a chain](./images/treap-search-tree-chain.svg)

It is not hard to see that the complexity of a query also changes from $O(\log n)$ to $O(n)$.

And treap, in order to solve this problem and reach a relatively "balanced" state, "shuffles" the insertion order of nodes by maintaining random priorities satisfying the heap property, thereby allowing the binary search tree to reach the ideal complexity and avoiding the problem of degenerating into a chain.

## Proof of the complexity of Treap

Since the complexity of various operations of treap is related to the depth of the operated nodes, we first prove that the expected depth of all nodes is $O(\log n)$.

### Notation conventions

For convenience of expression, we agree that:

-   $n$ is the number of nodes.
-   In a Treap node, the one satisfying the binary-search-tree property is called the **weight**, and the one satisfying the heap property (i.e. the random one) is called the **priority**. We may as well assume the priority satisfies the min-heap property.
-   $x_k$ denotes the node with the $k$-th smallest weight.
-   $X_{i,j}$ denotes the set $\{x_i,x_{i+1},\cdots,x_{j-1},x_j\}$, i.e. the set of nodes from the $i$-th to the $j$-th after arranging in ascending order of weight.
-   $\operatorname{dep}(x)$ denotes the depth of node $x$. The depth of the root node is defined as $0$.
-   $Y_{i,j}$ is an indicator random variable, with value $1$ when $x_i$ is an ancestor of $x_j$, and $0$ otherwise. In particular, $Y_{i,i}=0$.
-   $\Pr(A)$ denotes the probability that event $A$ occurs.

### Proof of the expected depth of a node

Since the depth of node $x_i$ equals the number of its ancestors, we have

$$
\operatorname{dep}(x_i)=\sum_{k=1}^nY_{k,i}.
$$

Then by the linearity of expectation, we have

$$
E(\operatorname{dep}(x_i))=E\left(\sum_{k=1}^nY_{k,i}\right)=\sum_{k=1}^nE(Y_{k,i}).
$$

Since $Y_{k,i}$ is an indicator random variable, its expectation equals the probability that it is $1$, so

$$
E(\operatorname{dep}(x_i))=\sum_{k=1}^n\Pr(Y_{k,i}=1).
$$

We first prove a lemma: $Y_{i,j}=1$ if and only if the priority of $x_i$ is the smallest in $X_{i,j}$.

??? note "Proof of the lemma"
    Consider a case discussion of the situations of $x_i$ and $x_j$.
    
    1.  If $x_i$ is the root node: since the priority satisfies the min-heap property, the priority of $x_i$ is the smallest, and for any $x_j$, $x_i$ is an ancestor of $x_j$.
    2.  If $x_j$ is the root node: similarly, $x_j$ has the smallest priority, so $x_i$ is not the one with the smallest priority in $X_{i,j}$; at the same time $x_i$ is also not an ancestor of $x_j$.
    3.  If $x_i$ and $x_j$ are in the two subtrees of the root node (one left, one right), then the root node $r\in X_{i,j}$. Therefore the priority of $x_i$ cannot be the smallest in $X_{i,j}$ (because the root node's is smaller than it). At the same time, since $x_i$ and $x_j$ belong to two subtrees, $x_i$ is also not an ancestor of $x_j$.
    4.  If $x_i$ and $x_j$ are in the same subtree of the root node, then this subtree can be taken out separately as a new treap, and the above proof can be carried out recursively.

Then by the lemma, the expected depth can be transformed into

$$
E(\operatorname{dep}(x_i))=\sum_{k=1}^n\Pr(x_k=\min X_{i,k}\land k\neq i).
$$

And because the priorities of the nodes are random, we assume that the probability that any node in the set $X_{i,j}$ has the smallest priority is the same, so

$$
\begin{aligned}
E(\operatorname{dep}(x_i))&=\sum_{k=1}^n\Pr(x_k=\min X_{i,k}\land k\neq i)\\
&=\sum_{k=1}^{n}\Pr(x_k=\min X_{i,k})-1\\
&=\sum_{k=1}^n\dfrac{1}{|i-k|+1}-1\\
&=\sum_{k=1}^{i-1}\dfrac{1}{i-k+1}+\sum_{k=i+1}^n\dfrac{1}{k-i+1}\\
&=\sum_{j=2}^i\dfrac 1j+\sum_{j=2}^{n-i+1}\dfrac 1j\\
&\le 2\sum_{j=2}^n\dfrac 1j < 2\sum_{j=2}^n\int_{j-1}^j\dfrac 1x\mathrm dx\\
&=2\int_1^n\dfrac 1x\mathrm dx=2\ln n=O(\log n).
\end{aligned}
$$

Therefore the expected depth of each node is $O(\log n)$.

And the complexity of the operations of a naive binary search tree is all $O(h)$, and the complexity of treap maintaining the heap property is also $O(h)$, so the expected complexity of various operations of treap is all $O(\log n)$.

???+ note "Intuitive understanding of the expected complexity"
    First, we need to recognize that the $\textit{priority}$ attribute of a node is directly related to the layer it lies in. Recall the heap property again:
    
    -   The child node value ($\textit{priority}$) is larger or smaller than the parent node (depending on whether it is a min-heap or a max-heap)
    
    We find that a node with a low layer number, such as the root node of the whole tree, also has a smaller $\textit{priority}$ attribute (in a min-heap). And, in a naive search tree, a node inserted earlier is also more likely to have a relatively small layer number. We can understand this $\textit{priority}$ attribute in association with the insertion order; in this way, we also understand why treap can shuffle the insertion order of nodes through $\textit{priority}$.

When inserting a new node into treap, we need to maintain both the tree and heap properties at the same time. Among them, the search-tree property can be maintained during insertion, while the maintenance of the heap property has two handling methods, namely rotation, and splitting and merging. The treaps using these two methods are called **rotating treap** and **rotation-free treap** respectively.

## Rotating treap

The **rotating treap** maintains balance by rotation, similar to the rotation operation of an AVL tree, divided into **left rotation** and **right rotation**. That is, it performs balance operations on the treap according to the priority of the heap while satisfying the condition of a binary search tree.

The rotating treap has a relatively small constant factor among all balanced trees when solving ordinary balanced-tree problems.

The code in the explanation below implements the rotating treap with pointers; the full array-form implementation is attached at the end of the article.

???+ info "Info"
    The `rank` in the code represents the priority mentioned earlier (the $\textit{priority}$ attribute), and this attribute satisfies the min-heap property.

### Node structure

```cpp
struct Node {
  Node *ch[2];  // the addresses of the two child nodes
  int val, rank;
  int rep_cnt;  // the number of times the current value (val) repeats
  int siz;      // the size of the subtree rooted at the current node

  Node(int val) : val(val), rep_cnt(1), siz(1) {
    ch[0] = ch[1] = nullptr;
    rank = rand();
    // note that at initialization, rank is given randomly
  }

  void upd_siz() {
    // used to recompute the value of siz after rotation and deletion
    siz = rep_cnt;
    if (ch[0] != nullptr) siz += ch[0]->siz;
    if (ch[1] != nullptr) siz += ch[1]->siz;
  }
};
```

### Rotation

The rotation operation is a very important operation of treap, mainly used to adjust the layer numbers of different nodes while keeping the treap's tree property, so as to maintain the heap property.

The left rotation and right rotation of the rotation operation may not be particularly easy to distinguish; the following are two relatively obvious characteristics:

The meaning of the rotation operation:

-   Under the premise of not affecting the search-tree property, make the subtree opposite to the rotation direction the root node (e.g. for left rotation, make the right subtree the root node)
-   Without affecting the property, and after rotation, the child node in the same direction as the rotation becomes the original root node (e.g. for left rotation, the left child after rotation is the root node before rotation)

The left rotation and right rotation operations are mutual, as shown in the figure below.

![Rotation operation](./images/treap-rotate.svg)

```cpp
enum rot_type { LF = 1, RT = 0 };

void _rotate(Node *&cur,
             rot_type dir) {  // the dir parameter represents the rotation direction, 0 for right rotation, 1 for left rotation
  // note that the cur passed in is a reference to a pointer, i.e. modifying this
  // cur also modifies the variable together; if this cur is a child node of another tree, then when
  // found via ch, it will also be found here

  // the following code all explains the case of left rotation
  Node *tmp = cur->ch[dir];  // make C the root node;
                             // here tmp
                             // is a temporary node pointer pointing to the node that becomes the new root node

  /* left rotation: i.e. making the right child the root node
   *         A                 C
   *        / \               / \
   *       B  C    ---->     A   E
   *         / \            / \
   *        D   E          B   D
   */
  cur->ch[dir] = tmp->ch[!dir];    // make A's right child D
  tmp->ch[!dir] = cur;             // make C's left child A
  cur->upd_siz(), tmp->upd_siz();  // update size information
  cur = tmp;  // finally assign the variable temporarily storing tree C to the current root node (note cur is a reference)
}
```

### Insertion

Similar to the insertion of an ordinary binary search tree, but during insertion the heap property of the priority needs to be maintained through rotation.

```cpp
void _insert(Node *&cur, int val) {
  if (cur == nullptr) {
    // no such node, directly create a new one
    cur = new Node(val);
    return;
  } else if (val == cur->val) {
    // if there is a node with this same value, increase the repeat count by one
    cur->rep_cnt++;
    cur->siz++;
  } else if (val < cur->val) {
    // maintain the search-tree property, val smaller than the current node is inserted to the left, and vice versa
    _insert(cur->ch[0], val);
    if (cur->ch[0]->rank < cur->rank) {
      // in a min-heap, the upper node's priority must be smaller
      // because the newly inserted left child is smaller than the parent node, now the left child needs to become the parent node
      _rotate(cur, RT);  // note the rotation property above, to rotate the left child up, a right rotation is needed
    }
    cur->upd_siz();  // the size changes after insertion, needs updating
  } else {
    _insert(cur->ch[1], val);
    if (cur->ch[1]->rank < cur->rank) {
      _rotate(cur, LF);
    }
    cur->upd_siz();
  }
}
```

### Deletion

It is mainly a case discussion; different cases have different handling methods; the tree size changes after deletion, so note to update it. And if the node to be deleted has a left subtree and a right subtree, we need to consider who becomes the parent node after deletion (maintaining the node with the smaller rank on top).

```cpp
void _del(Node *&cur, int val) {
  if (val > cur->val) {
    _del(cur->ch[1], val);
    // a larger value is in the right subtree, and vice versa
    cur->upd_siz();
  } else if (val < cur->val) {
    _del(cur->ch[0], val);
    cur->upd_siz();
  } else {
    if (cur->rep_cnt > 1) {
      // if the node to be deleted is repeated, we can directly decrease the repeat value
      cur->rep_cnt--, cur->siz--;
      return;
    }
    uint8_t state = 0;
    state |= (cur->ch[0] != nullptr);
    state |= ((cur->ch[1] != nullptr) << 1);
    // 00 neither, 01 left but no right, 10 no left but right, 11 both
    Node *tmp = cur;
    switch (state) {
      case 0:
        delete cur;
        cur = nullptr;
        // no child node at all, directly delete this node
        break;
      case 1:  // left but no right
        cur = tmp->ch[0];
        // make the root the left child, then delete the original root node; note that tmp here is copied from cur,
        // and cur is a reference
        delete tmp;
        break;
      case 2:  // right but no left
        cur = tmp->ch[1];
        delete tmp;
        break;
      case 3:
        rot_type dir = cur->ch[0]->rank < cur->ch[1]->rank
                           ? RT
                           : LF;  // dir is the child with the smaller rank
        _rotate(cur, dir);  // this rotation can rotate the child with the smaller priority up; rt is 0,
                            // and lf is 1, which is exactly the reverse of the actual subtree index
        _del(
            cur->ch[!dir],
            val);  // after the rotation is complete, the original root node is on the rotation-direction side, so we need to
                   // continue deleting this original root node
                   // if the node to be deleted is at the "upper level" of the whole tree, then we will keep, through
                   // this rotation operation here, rotating it until it has no subtree (or only one), then delete it.
        cur->upd_siz();
        // deletion causes the size to change
        break;
    }
  }
}
```

### Querying the rank by value

Meaning of the operation: query the rank of the value val in the subtree rooted at cur (the number of nodes in this subtree smaller than val + 1)

```cpp
int _query_rank(Node *cur, int val) {
  int less_siz = cur->ch[0] == nullptr ? 0 : cur->ch[0]->siz;
  // the number of nodes in this tree smaller than val
  if (val == cur->val)
    // if this node is exactly the node to query
    return less_siz + 1;
  else if (val < cur->val) {
    if (cur->ch[0] != nullptr)
      return _query_rank(cur->ch[0], val);
    else
      return 1;  // if the left subtree is empty, it means it is smaller than the smallest node, so this number is the smallest
  } else {
    if (cur->ch[1] != nullptr)
      // if the value to query is larger than this node, then this node's left subtree and this node itself are all smaller than the value to query
      // so we need to add these two values, plus the result of searching to the right
      // (the rank of the value val in the subtree rooted at the right subtree)
      return less_siz + cur->rep_cnt + _query_rank(cur->ch[1], val);
    else
      return cur->siz + 1;
    // without a right subtree, directly the whole tree + 1, equivalent to less_siz + cur->rep_cnt + 1
  }
}
```

### Querying the value by rank

To query the value by rank, we first need to know how to judge which part of the tree the node to query is in:

The following is a table of the judgment method:

| Left subtree | Root node / current node | Right subtree |
| ----------- | ---------------------------------- | ---------------------- |
| rank ≤ size of left subtree | rank > size of left subtree, and ≤ size of left subtree + repeat count of root node | rank > size of left subtree + repeat count of root node |

Note that if it is in the right subtree, we need to handle the original `rank` during recursion. Recursing is equivalent to querying the value for this rank in the right subtree; to convert the rank into one based on the right subtree, we need to subtract from the original `rank` the size of the left subtree and the repeat count of the root node.

We can imagine all nodes as a sorted array, or a number line (as below),

    1 -> |nodes of left subtree|root node|nodes of right subtree| -> n
                               ^
                               the rank to query
                         ⬇convert into a rank based on the right subtree
    1 -> |nodes of right subtree| -> n
           ^
           the rank to query

The conversion method here is to directly subtract from the rank the size of the left subtree and the repeat count of the root node.

```cpp
int _query_val(Node *cur, int rank) {
  // query the value of the rank-th largest node in the tree
  int less_siz = cur->ch[0] == nullptr ? 0 : cur->ch[0]->siz;
  // less siz is the size of the left subtree
  if (rank <= less_siz)
    return _query_val(cur->ch[0], rank);
  else if (rank <= less_siz + cur->rep_cnt)
    return cur->val;
  else
    return _query_val(cur->ch[1], rank - less_siz - cur->rep_cnt);  // see above
}
```

### Querying the first node smaller than val

Note that a global variable in the class, `q_prev_tmp`, is used here.

This value is only changed when val is larger than the current node value, so returning this variable is returning the last time val was larger than the current node's value, after which it becomes smaller.

```cpp
int _query_prev(Node *cur, int val) {
  if (val <= cur->val) {
    // still larger than val, so search in the left subtree
    if (cur->ch[0] != nullptr) return _query_prev(cur->ch[0], val);
  } else {
    // only when we can enter this else will q_prev_tmp be updated
    q_prev_tmp = cur->val;
    // the current node is already smaller than val, but it is uncertain whether it is the largest, so we go to the right subtree to continue searching
    if (cur->ch[1] != nullptr) _query_prev(cur->ch[1], val);
    // the subsequent recursion may not change q_prev_tmp
    // anymore, then just directly return this value; in short, what is returned is the last
    // cur->val that entered this else
    return q_prev_tmp;
  }
  return NIL;
}
```

### Querying the first node larger than val

Very similar to the previous one, just with the greater-than and less-than signs swapped.

```cpp
int _query_nex(Node *cur, int val) {
  if (val >= cur->val) {
    if (cur->ch[1] != nullptr) return _query_nex(cur->ch[1], val);
  } else {
    q_nex_tmp = cur->val;
    if (cur->ch[0] != nullptr) _query_nex(cur->ch[0], val);
    return q_nex_tmp;
  }
  return NIL;
}
```

## Rotation-free treap

The operation style of the rotation-free treap makes it naturally support features such as maintaining sequences and persistence.

The **rotation-free treap** is also called the split-merge treap. It has only two core operations, namely **split** and **merge**. Through these two operations, other operations can be implemented more conveniently than the rotating treap in many cases. Below we introduce these two operations one by one.

???+ note "Note"
    When explaining the rotation-free treap, one should mention **FHQ-Treap** (by Fan Haoqiang), i.e. the persistent, interval-operation-supporting rotation-free Treap. For more content, please refer to the "Fan Haoqiang on Data Structures" ppt.

### Split

#### Split by value

The split process accepts two parameters: the root pointer $\textit{cur}$ and the key value $\textit{key}$. The result is splitting the treap pointed to by the root pointer into two treaps, the first treap where the values ($\textit{val}$) of all nodes are less than or equal to $\textit{key}$, and the second treap where the values of all nodes are greater than $\textit{key}$.

This process first judges whether $\textit{key}$ is less than the value of $\textit{cur}$; if less, then it means $\textit{cur}$ and its entire right subtree are all greater than $\textit{key}$, belonging to the second treap. Of course, part of the left subtree may also have values greater than $\textit{key}$, so we still need to continue recursively splitting the left subtree. For the part of the left subtree greater than $\textit{key}$, we make it the left subtree of $\textit{cur}$, so that all nodes on the entire $\textit{cur}$ are greater than $\textit{key}$.

Correspondingly, if $\textit{key}$ is greater than or equal to the value of $\textit{cur}$, it means the entire left subtree of $\textit{cur}$ and itself are less than or equal to $\textit{key}$, belonging to the first treap after splitting. And, part of $\textit{cur}$'s right subtree may also be less than or equal to $\textit{key}$, so we need to continue recursively splitting the right subtree. Make the part less than or equal to $\textit{key}$ the right subtree of $\textit{cur}$, so that all nodes on the entire $\textit{cur}$ are less than or equal to $\textit{key}$.

The figure below shows the case of splitting by value when the value of $\textit{cur}$ is less than or equal to $\textit{key}$. [^ref1]

![Split by value](./images/treap-none-rot-split-by-val.svg)

```cpp
pair<Node *, Node *> split(Node *cur, int key) {
  if (cur == nullptr) return {nullptr, nullptr};
  if (cur->val <= key) {
    // cur and its left subtree must belong to the first tree after splitting
    auto temp = split(cur->ch[1], key);
    // but it may also have part of its right subtree smaller than key
    cur->ch[1] = temp.first;
    // we take out the part smaller than key as cur's right subtree, so the entire cur is smaller than
    // key; the remaining part of the right subtree becomes the second treap after splitting
    cur->upd_siz();
    // the tree size changes after splitting, needs updating
    return {cur, temp.second};
  } else {
    // same as above
    auto temp = split(cur->ch[0], key);
    cur->ch[0] = temp.second;
    cur->upd_siz();
    return {temp.first, cur};
  }
}
```

#### Split by rank

Compared with split by value, this operation is more like querying the value by rank in the rotating treap (the rank of a certain node is the number of nodes in the tree with values smaller than this node $+ 1$):

This function accepts two parameters, the node pointer $\textit{cur}$ and the rank $\textit{rk}$, and returns three treaps after splitting.

Among them, the rank of each node in the first treap is smaller than $\textit{rk}$, the rank of the second equals $\textit{rk}$, and the second treap has only one node (there cannot be multiple equal ones; if there are, the `cnt` in the `Node` structure is increased), and the third is greater.

The key point of this operation is judging which part of the tree the node whose rank equals $\textit{cur}$ is in, which is also an important part of the rotating treap's operation of querying the value by rank; it is explained in great detail above and is not explained too much here.

And, the recursion part of this operation is also very similar to split by value, which is not repeated here.

```cpp
tuple<Node *, Node *, Node *> split_by_rk(Node *cur, int rk) {
  if (cur == nullptr) return {nullptr, nullptr, nullptr};
  int ls_siz = cur->ch[0] == nullptr ? 0 : cur->ch[0]->siz;
  if (rk <= ls_siz) {
    // the node whose rank equals cur is in the left subtree
    Node *l, *mid, *r;
    tie(l, mid, r) = split_by_rk(cur->ch[0], rk);
    cur->ch[0] = r;  // the ranks in the returned third treap are all greater than rk
    // after cur's left subtree is set to r, the ranks of all nodes in the entire cur are greater than rk
    cur->upd_siz();
    return {l, mid, cur};
  } else if (rk <= ls_siz + cur->cnt) {
    // the one equal to cur is the current node
    Node *lt = cur->ch[0];
    Node *rt = cur->ch[1];
    cur->ch[0] = cur->ch[1] = nullptr;
    // the second treap after splitting has only one node, so its subtrees need to be set to empty
    return {lt, cur, rt};
  } else {
    // the node whose rank equals cur is in the right subtree
    // the recursion process is the same as above
    Node *l, *mid, *r;
    tie(l, mid, r) = split_by_rk(cur->ch[1], rk - ls_siz - cur->cnt);
    cur->ch[1] = l;
    cur->upd_siz();
    return {cur, mid, r};
  }
}
```

### Merge

The merge process accepts two parameters: the root pointer $\textit{u}$ of the left treap and the root pointer $\textit{v}$ of the right treap. It must be satisfied that the values of all nodes in $\textit{u}$ are less than or equal to the values of all nodes in $\textit{v}$. Generally speaking, the two treaps we merge are both originally split from one treap, so it is not hard to satisfy that the values of all nodes in $\textit{u}$ are smaller than $\textit{v}$.

In the rotating treap, we use the rotation operation to maintain $\textit{priority}$ conforming to the heap property, while rotation cannot change the tree's property. In the rotation-free treap, we use merging to achieve the same effect.

Because the two treaps are already ordered, when merging we only need to consider which tree to "put on top" and which to "put below", i.e. we need to judge which tree to make the subtree. Obviously, by the heap property, we need to put the one with smaller $\textit{priority}$ on top (a min-heap is used here).

At the same time, we also need to satisfy the search-tree property, so if the $\textit{priority}$ of $\textit{u}$'s root node is smaller than $\textit{v}$'s, then $\textit{u}$ is the new root node, and $\textit{v}$, because its value is larger than $\textit{u}$, should be merged with $\textit{u}$'s right subtree; conversely, $\textit{v}$ is the new root node, and then because $u$'s value is smaller than $\textit{v}$, it is merged with $v$'s left subtree.

```cpp
Node *merge(Node *u, Node *v) {
  // the interiors of the two trees passed in already conform to the search-tree property
  // and the values of all nodes in u < the values of all nodes in v
  // so when merging we need to maintain the heap property
  // a min-heap is used here
  if (u == nullptr && v == nullptr) return nullptr;
  if (u != nullptr && v == nullptr) return u;
  if (v != nullptr && u == nullptr) return v;

  if (u->prio < v->prio) {
    // u's prio is smaller, u should be the parent node
    u->ch[1] = merge(u->ch[1], v);
    // because v is larger than u, make v u's right subtree
    u->upd_siz();
    return u;
  } else {
    // v is smaller, v should be the parent node
    v->ch[0] = merge(u, v->ch[0]);
    // u is smaller than v, so the parameters when recursing are like this
    v->upd_siz();
    return v;
  }
}
```

### Insertion

In the rotation-free treap, basic operations such as insertion, deletion, and querying the rank by value can be implemented either with the ordinary binary search tree method or with split and merge. Generally speaking, implementing with split and merge is more concise, but the speed is a bit slower [^ref2]. To help better understand the rotation-free treap, the following operations are all implemented with split and merge.

When implementing the insertion operation, we utilize some properties of the split operation. That is, nodes with values less than or equal to $\textit{val}$ are split into the first treap.

So, suppose we split the current treap according to $\textit{val}$. There will be the following two trees, satisfying the following conditions:

$$
\begin{aligned}
T_1 &\le val\\
T_2 &> val
\end{aligned}
$$

Among them, $T_1$ denotes the set of all nodes split into the first treap after splitting, and $T_2$ is the second.

If we continue to split $T_1$ by $\textit{val} - 1$, then the following two trees will be produced, satisfying the following conditions:

$$
\begin{gathered}
T_{1\ \text{left}} \le val - 1\\
T_{1\ \text{right}} > val - 1 \ \And \ T_{1\ \text{right}} \le val
\end{gathered}
$$

Among them, $T_{1\ \text{left}}$ denotes the set of all nodes split into the first treap after $T_1$ is split, and $T_{1\ \text{right}}$ is the second. And in the formula above, the latter part $\And \ T_{1\ \text{right}} \le val$ comes from the condition $T_1 \le val$ that $T_1$ satisfies.

It is not hard to find that as long as $\textit{val}$ and the node's value are integers (integers are used in most usage scenarios), then there is only one node satisfying the $T_{1\ \text{right}}$ condition, namely the node whose value equals $\textit{val}$.

When inserting, if we find that a node satisfying $T_{1\ \text{right}}$ exists, then we can directly increase the repeat count; otherwise, create a new node.

Note that after splitting the tree, we still need to use the merge operation to "stick" it back together, so that it can be used again next time. And, we also need to note that the parameter order of the merge operation has a requirement: the values of all nodes of the first tree need to be smaller than the second.

```cpp
void insert(int val) {
  auto temp = split(root, val);
  // split the whole tree into two according to the value of val
  // note the implementation of split, the subtree equal to val is in the left subtree
  auto l_tr = split(temp.first, val - 1);
  // the left subtree of l_tr <= val - 1; if there is a node = val, it must be in the right subtree
  Node *new_node;
  if (l_tr.second == nullptr) {
    // no such node, create a new one, otherwise directly increase the repeat count.
    new_node = new Node(val);
  } else {
    l_tr.second->cnt++;
    l_tr.second->upd_siz();
  }
  Node *l_tr_combined =
      merge(l_tr.first, l_tr.second == nullptr ? new_node : l_tr.second);
  // merge T_1 left and T_1 right
  root = merge(l_tr_combined, temp.second);
  // merge T_1 and T_2
}
```

### Deletion

The deletion operation also uses a method similar to the insertion operation, finding the node whose value equals $\textit{val}$ and deleting it.

```cpp
void del(int val) {
  auto temp = split(root, val);
  auto l_tr = split(temp.first, val - 1);
  if (l_tr.second->cnt > 1) {
    // if the repeat count of this node is greater than 1, just decrease it
    l_tr.second->cnt--;
    l_tr.second->upd_siz();
    l_tr.first = merge(l_tr.first, l_tr.second);
  } else {
    if (temp.first == l_tr.second) {
      // it is possible that the whole T_1 has only this node, so we also need to set this point to null to mark it as deleted
      temp.first = nullptr;
    }
    delete l_tr.second;
    l_tr.second = nullptr;
  }
  root = merge(l_tr.first, temp.second);
}
```

### Querying the rank by value

The rank is the number of nodes smaller than this value $+ 1$, so we split the current tree according to $\textit{val} - 1$; then the first tree after splitting satisfies:

$$
T_1 \le val - 1
$$

If the tree's values and $\textit{val}$ are integers, then $T_1$ contains all nodes with values smaller than $\textit{val}$.

```cpp
int qrank_by_val(Node* cur, int val) {
  auto temp = split(cur, val - 1);
  int ret = (temp.first == nullptr ? 0 : temp.first->siz) + 1;  // + 1 by definition
  root = merge(temp.first, temp.second);  // split it, then stick it back
  return ret;
}
```

### Querying the value by rank

After calling the `split_by_rk()` function, three split treaps are returned, of which the second contains only one node whose rank equals $\textit{rk}$, so we directly return this node's $\textit{val}$.

```cpp
int qval_by_rank(Node *cur, int rk) {
  Node *l, *mid, *r;
  tie(l, mid, r) = split_by_rk(cur, rk);
  int ret = mid->val;
  root = merge(merge(l, mid), r);
  return ret;
}
```

### Querying the first node smaller than val

This problem can be transformed into finding, among all nodes smaller than $\textit{val}$, the one with the largest rank. We split this treap according to $\textit{val}$; the values of the nodes in the returned first treap are then all smaller than $\textit{val}$, and then we call `qval_by_rank()` to find the node with the largest value in this tree.

```cpp
int qprev(int val) {
  auto temp = split(root, val - 1);
  // temp.first is the subtree with values smaller than val
  int ret = qval_by_rank(temp.first, temp.first->siz);
  // what is queried here is the value of the largest one among all nodes smaller than val
  root = merge(temp.first, temp.second);
  return ret;
}
```

### Querying the first node larger than val

Similar to the previous operation, this problem can be transformed into finding, among all nodes larger than $\textit{val}$, the one with the smallest rank. Then after splitting according to $\textit{val}$, the values of all nodes in the returned second treap are larger than $\textit{val}$.

Then we query the value of the node with rank $1$ in this tree (i.e. the node with the smallest value), and we can successfully find the first node larger than $\textit{val}$.

```cpp
int qnex(int val) {
  auto temp = split(root, val);
  int ret = qval_by_rank(temp.second, 1);
  // query the one with the smallest value among all subtrees larger than val
  root = merge(temp.first, temp.second);
  return ret;
}
```

### Build

Convert a sequence $\{a_n\}$ with $n$ nodes into a treap.

One can brute-force insert these $n$ nodes one by one; each time a node with weight $v$ is inserted, split the whole treap by weight into two parts, weight less than or equal to $v$ and weight greater than $v$, then create a new node with weight $v$, and merge the two parts and the new node in ascending order; the time complexity of a single insertion is $O(\log n)$, and the total time complexity is $O(n\log n)$.

In some problems, there may be multiple operations of inserting an ordered sequence, in which case the tree-building operation needs to be completed in $O(n)$ time complexity.

Method one: during the recursive tree-building process, each time select the midpoint of the current interval as the tree root of this interval, and assign each node an appropriate priority value so that the new tree satisfies the heap property. This guarantees the tree height is $O(\log n)$.

Method two: during the recursive tree-building process, each time select the midpoint of the current interval as the tree root of this interval, then give each node a random priority. This guarantees the tree height is $O(\log n)$, but does not guarantee that it satisfies the heap property. This is also correct, because the priority of the rotation-free treap is used to make the `merge` operation a bit more random, not to guarantee the tree height.

Method three: observe that the treap is a Cartesian tree, and use the $O(n)$ tree-building method of the Cartesian tree, maintaining the right chain with a monotonic stack.

### Interval operations of the rotation-free treap

#### Building the tree

One big advantage of the rotation-free treap over the rotating treap is that it can implement various interval operations. Below we take the [template problem](https://loj.ac/problem/105) of the Literary Balanced Tree as an example to introduce the interval operations of treap.

> You need to write a data structure (you can refer to the problem title) to maintain an ordered sequence.
>
> The following operation needs to be provided: reverse an interval; for example, if the original ordered sequence is $5\ 4\ 3\ 2\ 1$, and the reversed interval is $[2,4]$, then the result is $5\ 2\ 3\ 4\ 1$.
> For $100\%$ of the data, $1 \le n$ (initial interval length) $m$ (number of reversals) $\le 10^5$

In this problem, what we need to implement is interval reversal, so we first need to consider how to build the tree; the built tree needs to be the initial interval.

We just need to insert the indices of the interval into the treap in sequence, so that during the in-order traversal (first traverse the left subtree, then the current node, finally the right subtree), we can obtain this interval [^ref3].

We know that in a naive binary search tree, inserting nodes in increasing order builds a long chain, and by in-order traversal, we can naturally obtain this interval.

<div align=center>
  <img style="width: 50%; " src="../images/treap-search-tree-chain.svg" >
</div>

As in the figure above, inserting nodes into a naive search tree in the order $1\ 2\ 3\ 4\ 5$, the in-order traversal also yields $1\ 2\ 3\ 4\ 5$.

But in a treap, after inserting nodes in increasing order, during the merge operation the tree structure will also be adjusted according to $\textit{priority}$; in such a case, how to ensure that the in-order traversal will definitely output correctly?

You can refer to the [monotonic-stack tree-building method of the Cartesian tree](./cartesian-tree.md) to understand this problem.

Let the newly inserted node be $\textit{u}$.

First, because nodes are inserted in increasing order, each newly inserted node will definitely be connected to the right chain of the treap (i.e. the chain formed by the nodes passed when going right from the root node all the way down the right subtree).

Starting from the root node, the $\textit{priority}$ of the nodes on the right chain is increasing (min-heap). Then we can find the first node on the right chain whose $\textit{priority}$ is greater than $\textit{u}$; we call this node $\textit{v}$, and replace this node with $\textit{u}$.

Because $\textit{u}$ must be greater than all other nodes on this tree, we need to make $\textit{v}$ and its subtree the left subtree of $\textit{u}$. And at this point $\textit{u}$ has no right subtree.

It can be found that during the in-order traversal, $\textit{u}$ must be the last one traversed (because $\textit{u}$ is the last one in the right chain, and in an in-order traversal, the right subtree is the last one traversed).

The figure below shows the change when a treap inserts nodes $1 \sim 5$ in increasing order, at the moment of inserting node $5$; you can use this figure to better understand the process of inserting in increasing order.

![Inserting a node](./images/treap-none-rot-seg-build.svg)

#### Interval reversal

When reversing the interval $[l, r]$, the basic idea is to split the tree into three intervals $[1, l - 1],\ [l, r],\ [r + 1, n]$, then reverse the middle $[l, r]$ [^ref3].

The specific operation of reversal is to swap the positions of each left and right child node of the subtree within the interval. The figure below shows the treap after reversing the $[3, 4]$ and $[3, 5]$ intervals of the treap in the figure above.

![Interval reversal](./images/treap-none-rot-seg-flip-ex.svg)

Note that if we reverse by this method, then each time the $[l, r]$ interval is reversed, $r - l$ nodes will be swapped in position; such frequent operations obviously cannot satisfy the data range of $10^5$, and its single-reversal complexity of $O(n \times \log_2 n)$ is even worse than brute force (because, besides needing linear time to swap nodes, we also need to spend $O(\log_2 n)$ time in the tree to find the nodes to swap).

Looking again at the problem requirements, we can find that because only the operated interval needs to be output at the end, we do not actually need to swap every time. In this way, we can use the lazy tag commonly used in segment trees to optimize the complexity. When swapping, we only need to apply a tag on the parent node, representing that each left and right child node under this subtree needs to be swapped.

In a segment tree, we generally push down the lazy tag during updates and queries. This is because, during updates and queries, the range we want to update/query does not necessarily coincide with the range represented by the lazy tag, so we need to push down the tag first to ensure that the queried and updated values are correct.

It is the same in the rotation-free treap. In the specific operation we will split the treap into the three trees mentioned above, then apply a lazy tag to the middle tree and merge these three trees. Because the interval we want to reverse and the interval represented by the lazy tag do not necessarily coincide, we need to push down the tag when splitting. And, the split and merge operations will cause changes to each node and the node represented by its lazy tag, so we also need to push down the lazy tag before merging.

In other words, when the structure of the tree changes, when we perform a split or merge operation and need to change the left/right child information of a certain point, we should push down the tag before, not after, because the lazy tag needs to be pushed down to the child nodes, but if the lazy tag has not yet been pushed down after changing the left/right child information, then the lazy tag loses its push-down target. [^ref4]

<!-- TODO: a figure can be added to explain why the tag needs to be pushed down when splitting and merging -->

The following is the code explanation; the code references [^ref3].

Because most of the operations in interval operations are the same as the ordinary rotation-free treap, here we only explain the parts that differ from the ordinary rotation-free treap.

#### Pushing down the tag

Note that the lazy tag here represents needing to swap the position of each child node in this tree. So if the child node of the current node also has a lazy tag, then two reversals cancel out. If the child node does not need to be reversed, then this lazy tag needs to continue to be pushed down to the child node.

```cpp
// this pushdown here is a member function of the Node class, where to_rev is the lazy tag
void pushdown() {
  swap(ch[0], ch[1]);
  if (ch[0] != nullptr) ch[0]->to_rev ^= 1;
  if (ch[1] != nullptr) ch[1]->to_rev ^= 1;
  to_rev = false;
}

void check_tag() {
  if (to_rev) pushdown();
}
```

#### Split

Note that in this problem, because of the reversal operation, the $\textit{val}$ in the treap will not conform to the binary-search-tree property (see the figure in the interval reversal part), so we cannot judge whether to recurse into the left subtree or the right subtree based on $\textit{val}$.

So the split here is more similar to split by rank in the ordinary rotation-free treap, judging whether to recurse into the left or right subtree based on the current tree size; in other words, we judge by the position of this node in the tree at the start.

The ranks of the nodes in the returned first treap are all less than or equal to $\textit{sz}$, while the ranks of the nodes in the second treap are all greater than $\textit{sz}$.

```cpp
#define siz(_) (_ == nullptr ? 0 : _->siz)

pair<Node*, Node*> split(Node* cur, int sz) {
  // judge by the tree size
  if (cur == nullptr) return {nullptr, nullptr};
  cur->check_tag();
  // push down before splitting
  if (sz <= siz(cur->ch[0])) {
    auto temp = split(cur->ch[0], sz);
    cur->ch[0] = temp.second;
    cur->upd_siz();
    return {temp.first, cur};
  } else {
    auto temp =
        split(cur->ch[1],
              sz - siz(cur->ch[0]) -
                  1);  // this conversion is explained in "querying the value by rank" of the rotating treap
    cur->ch[1] = temp.first;
    cur->upd_siz();
    return {cur, temp.second};
  }
}
```

#### Merge

The only thing to note is pushing down the lazy tag before merging

```cpp
Node *merge(Node *sm, Node *bg) {
  // small, big
  if (sm == nullptr && bg == nullptr) return nullptr;
  if (sm != nullptr && bg == nullptr) return sm;
  if (sm == nullptr && bg != nullptr) return bg;
  sm->check_tag(), bg->check_tag();
  if (sm->prio < bg->prio) {
    sm->ch[1] = merge(sm->ch[1], bg);
    sm->upd_siz();
    return sm;
  } else {
    bg->ch[0] = merge(sm, bg->ch[0]);
    bg->upd_siz();
    return bg;
  }
}
```

#### Interval reversal

As introduced earlier, split out the three intervals $[1, l - 1],\ [l, r],\ [r + 1, n]$, then apply a tag to the middle interval and merge.

```cpp
void seg_rev(int l, int r) {
  // here less and more are relative to l
  auto less = split(root, l - 1);
  // all those less than or equal to l - 1 will be in the left subtree of less
  auto more = split(less.second, r - l + 1);
  // the interval of the first r - l + 1 elements starting from l
  more.first->to_rev = true;
  root = merge(less.first, merge(more.first, more.second));
}
```

#### In-order traversal printing

Note to push down the tag when printing.

```cpp
void print(Node* cur) {
  if (cur == nullptr) return;
  cur->check_tag();
  // in-order traversal -> first left subtree, then itself, finally right subtree
  print(cur->ch[0]);
  cout << cur->val << " ";
  print(cur->ch[1]);
}
```

## Full code

### Rotating treap

#### Pointer implementation

??? note "Full code"
    The following is the full version of the code explained above, the template code for the ordinary balanced tree.
    
    ```cpp
    // author: (ttzytt)[ttzytt.com]
    #include <cstdint>
    #include <cstdio>
    #include <cstdlib>
    using namespace std;
    
    struct Node {
      Node *ch[2];
      int val, rank;
      int rep_cnt;
      int siz;
    
      Node(int val) : val(val), rep_cnt(1), siz(1) {
        ch[0] = ch[1] = nullptr;
        rank = rand();
      }
    
      void upd_siz() {
        siz = rep_cnt;
        if (ch[0] != nullptr) siz += ch[0]->siz;
        if (ch[1] != nullptr) siz += ch[1]->siz;
      }
    };
    
    class Treap {
     private:
      Node *root;
    
      constexpr static int NIL = -1;  // used to indicate that the queried value does not exist
    
      enum rot_type { LF = 1, RT = 0 };
    
      int q_prev_tmp = 0, q_nex_tmp = 0;
    
      void _rotate(Node *&cur, rot_type dir) {  // 0 for right rotation, 1 for left rotation
        Node *tmp = cur->ch[dir];
        cur->ch[dir] = tmp->ch[!dir];
        tmp->ch[!dir] = cur;
        cur->upd_siz(), tmp->upd_siz();
        cur = tmp;
      }
    
      void _insert(Node *&cur, int val) {
        if (cur == nullptr) {
          cur = new Node(val);
          return;
        } else if (val == cur->val) {
          cur->rep_cnt++;
          cur->siz++;
        } else if (val < cur->val) {
          _insert(cur->ch[0], val);
          if (cur->ch[0]->rank < cur->rank) {
            _rotate(cur, RT);
          }
          cur->upd_siz();
        } else {
          _insert(cur->ch[1], val);
          if (cur->ch[1]->rank < cur->rank) {
            _rotate(cur, LF);
          }
          cur->upd_siz();
        }
      }
    
      void _del(Node *&cur, int val) {
        if (val > cur->val) {
          _del(cur->ch[1], val);
          cur->upd_siz();
        } else if (val < cur->val) {
          _del(cur->ch[0], val);
          cur->upd_siz();
        } else {
          if (cur->rep_cnt > 1) {
            cur->rep_cnt--, cur->siz--;
            return;
          }
          uint8_t state = 0;
          state |= (cur->ch[0] != nullptr);
          state |= ((cur->ch[1] != nullptr) << 1);
          // 00 neither, 01 left but no right, 10 no left but right, 11 both
          Node *tmp = cur;
          switch (state) {
            case 0:
              delete cur;
              cur = nullptr;
              break;
            case 1:  // left but no right
              cur = tmp->ch[0];
              delete tmp;
              break;
            case 2:  // right but no left
              cur = tmp->ch[1];
              delete tmp;
              break;
            case 3:
              rot_type dir = cur->ch[0]->rank < cur->ch[1]->rank ? RT : LF;
              _rotate(cur, dir);
              _del(cur->ch[!dir], val);
              cur->upd_siz();
              break;
          }
        }
      }
    
      int _query_rank(Node *cur, int val) {
        int less_siz = cur->ch[0] == nullptr ? 0 : cur->ch[0]->siz;
        if (val == cur->val)
          return less_siz + 1;
        else if (val < cur->val) {
          if (cur->ch[0] != nullptr)
            return _query_rank(cur->ch[0], val);
          else
            return 1;
        } else {
          if (cur->ch[1] != nullptr)
            return less_siz + cur->rep_cnt + _query_rank(cur->ch[1], val);
          else
            return cur->siz + 1;
        }
      }
    
      int _query_val(Node *cur, int rank) {
        int less_siz = cur->ch[0] == nullptr ? 0 : cur->ch[0]->siz;
        if (rank <= less_siz)
          return _query_val(cur->ch[0], rank);
        else if (rank <= less_siz + cur->rep_cnt)
          return cur->val;
        else
          return _query_val(cur->ch[1], rank - less_siz - cur->rep_cnt);
      }
    
      int _query_prev(Node *cur, int val) {
        if (val <= cur->val) {
          if (cur->ch[0] != nullptr) return _query_prev(cur->ch[0], val);
        } else {
          q_prev_tmp = cur->val;
          if (cur->ch[1] != nullptr) _query_prev(cur->ch[1], val);
          return q_prev_tmp;
        }
        return NIL;
      }
    
      int _query_nex(Node *cur, int val) {
        if (val >= cur->val) {
          if (cur->ch[1] != nullptr) return _query_nex(cur->ch[1], val);
        } else {
          q_nex_tmp = cur->val;
          if (cur->ch[0] != nullptr) _query_nex(cur->ch[0], val);
          return q_nex_tmp;
        }
        return NIL;
      }
    
     public:
      void insert(int val) { _insert(root, val); }
    
      void del(int val) { _del(root, val); }
    
      int query_rank(int val) { return _query_rank(root, val); }
    
      int query_val(int rank) { return _query_val(root, rank); }
    
      int query_prev(int val) { return _query_prev(root, val); }
    
      int query_nex(int val) { return _query_nex(root, val); }
    };
    
    Treap tr;
    
    int main() {
      srand(0);
      int t;
      scanf("%d", &t);
      while (t--) {
        int mode;
        int num;
        scanf("%d%d", &mode, &num);
        switch (mode) {
          case 1:
            tr.insert(num);
            break;
          case 2:
            tr.del(num);
            break;
          case 3:
            printf("%d\n", tr.query_rank(num));
            break;
          case 4:
            printf("%d\n", tr.query_val(num));
            break;
          case 5:
            printf("%d\n", tr.query_prev(num));
            break;
          case 6:
            printf("%d\n", tr.query_nex(num));
            break;
        }
      }
    }
    ```

#### Array implementation

The following is the bzoj ordinary balanced tree template code, implemented with arrays.

??? note "Full code"
    ```cpp
    --8<-- "docs/ds/code/treap/treap_1.cpp"
    ```

### Rotation-free treap

#### Pointer implementation

??? note "Full code"
    The following is the full version of the code explained above, the template code for the ordinary balanced tree.
    
    ```cpp
    
    // author: (ttzytt)[ttzytt.com]
    #include <cstdio>
    #include <cstdlib>
    #include <ctime>
    #include <tuple>
    using namespace std;
    
    struct Node {
      Node *ch[2];
      int val, prio;
      int cnt;
      int siz;
    
      Node(int _val) : val(_val), cnt(1), siz(1) {
        ch[0] = ch[1] = nullptr;
        prio = rand();
      }
    
      Node(Node *_node) {
        val = _node->val, prio = _node->prio, cnt = _node->cnt, siz = _node->siz;
      }
    
      void upd_siz() {
        siz = cnt;
        if (ch[0] != nullptr) siz += ch[0]->siz;
        if (ch[1] != nullptr) siz += ch[1]->siz;
      }
    };
    
    struct none_rot_treap {
    #define _3 second.second
    #define _2 second.first
      Node *root;
    
      pair<Node *, Node *> split(Node *cur, int key) {
        if (cur == nullptr) return {nullptr, nullptr};
        if (cur->val <= key) {
          auto temp = split(cur->ch[1], key);
          cur->ch[1] = temp.first;
          cur->upd_siz();
          return {cur, temp.second};
        } else {
          auto temp = split(cur->ch[0], key);
          cur->ch[0] = temp.second;
          cur->upd_siz();
          return {temp.first, cur};
        }
      }
    
      tuple<Node *, Node *, Node *> split_by_rk(Node *cur, int rk) {
        if (cur == nullptr) return {nullptr, nullptr, nullptr};
        int ls_siz = cur->ch[0] == nullptr ? 0 : cur->ch[0]->siz;
        if (rk <= ls_siz) {
          Node *l, *mid, *r;
          tie(l, mid, r) = split_by_rk(cur->ch[0], rk);
          cur->ch[0] = r;
          cur->upd_siz();
          return {l, mid, cur};
        } else if (rk <= ls_siz + cur->cnt) {
          Node *lt = cur->ch[0];
          Node *rt = cur->ch[1];
          cur->ch[0] = cur->ch[1] = nullptr;
          return {lt, cur, rt};
        } else {
          Node *l, *mid, *r;
          tie(l, mid, r) = split_by_rk(cur->ch[1], rk - ls_siz - cur->cnt);
          cur->ch[1] = l;
          cur->upd_siz();
          return {cur, mid, r};
        }
      }
    
      Node *merge(Node *u, Node *v) {
        if (u == nullptr && v == nullptr) return nullptr;
        if (u != nullptr && v == nullptr) return u;
        if (v != nullptr && u == nullptr) return v;
        if (u->prio < v->prio) {
          u->ch[1] = merge(u->ch[1], v);
          u->upd_siz();
          return u;
        } else {
          v->ch[0] = merge(u, v->ch[0]);
          v->upd_siz();
          return v;
        }
      }
    
      void insert(int val) {
        auto temp = split(root, val);
        auto l_tr = split(temp.first, val - 1);
        Node *new_node;
        if (l_tr.second == nullptr) {
          new_node = new Node(val);
        } else {
          l_tr.second->cnt++;
          l_tr.second->upd_siz();
        }
        Node *l_tr_combined =
            merge(l_tr.first, l_tr.second == nullptr ? new_node : l_tr.second);
        root = merge(l_tr_combined, temp.second);
      }
    
      void del(int val) {
        auto temp = split(root, val);
        auto l_tr = split(temp.first, val - 1);
        if (l_tr.second->cnt > 1) {
          l_tr.second->cnt--;
          l_tr.second->upd_siz();
          l_tr.first = merge(l_tr.first, l_tr.second);
        } else {
          if (temp.first == l_tr.second) {
            temp.first = nullptr;
          }
          delete l_tr.second;
          l_tr.second = nullptr;
        }
        root = merge(l_tr.first, temp.second);
      }
    
      int qrank_by_val(Node *cur, int val) {
        auto temp = split(cur, val - 1);
        int ret = (temp.first == nullptr ? 0 : temp.first->siz) + 1;
        root = merge(temp.first, temp.second);
        return ret;
      }
    
      int qval_by_rank(Node *cur, int rk) {
        Node *l, *mid, *r;
        tie(l, mid, r) = split_by_rk(cur, rk);
        int ret = mid->val;
        root = merge(merge(l, mid), r);
        return ret;
      }
    
      int qprev(int val) {
        auto temp = split(root, val - 1);
        int ret = qval_by_rank(temp.first, temp.first->siz);
        root = merge(temp.first, temp.second);
        return ret;
      }
    
      int qnex(int val) {
        auto temp = split(root, val);
        int ret = qval_by_rank(temp.second, 1);
        root = merge(temp.first, temp.second);
        return ret;
      }
    };
    
    none_rot_treap tr;
    
    int main() {
      srand(time(nullptr));
      int t;
      scanf("%d", &t);
      while (t--) {
        int mode;
        int num;
        scanf("%d%d", &mode, &num);
        switch (mode) {
          case 1:
            tr.insert(num);
            break;
          case 2:
            tr.del(num);
            break;
          case 3:
            printf("%d\n", tr.qrank_by_val(tr.root, num));
            break;
          case 4:
            printf("%d\n", tr.qval_by_rank(tr.root, num));
            break;
          case 5:
            printf("%d\n", tr.qprev(num));
            break;
          case 6:
            printf("%d\n", tr.qnex(num));
            break;
        }
      }
    }
    ```

### Interval operations of the rotation-free treap

#### Pointer implementation

??? note "Full code"
    The following is the full version of the code explained above, the template code for the Literary Balanced Tree problem.
    
    ```cpp
    
    // author: (ttzytt)[ttzytt.com]
    #include <cstdlib>
    #include <ctime>
    #include <iostream>
    using namespace std;
    
    // reference: https://www.cnblogs.com/Equinox-Flower/p/10785292.html
    struct Node {
      Node* ch[2];
      int val, prio;
      int cnt;
      int siz;
      bool to_rev = false;  // need to reverse every node under this subtree
    
      Node(int _val) : val(_val), cnt(1), siz(1) {
        ch[0] = ch[1] = nullptr;
        prio = rand();
      }
    
      int upd_siz() {
        siz = cnt;
        if (ch[0] != nullptr) siz += ch[0]->siz;
        if (ch[1] != nullptr) siz += ch[1]->siz;
        return siz;
      }
    
      void pushdown() {
        swap(ch[0], ch[1]);
        if (ch[0] != nullptr) ch[0]->to_rev ^= 1;
        // if the original child node also needs to be reversed, then two reversals cancel out; if the child node is not reversed, then this
        //  tag needs to continue to be pushed to the child node
        if (ch[1] != nullptr) ch[1]->to_rev ^= 1;
        to_rev = false;
      }
    
      void check_tag() {
        if (to_rev) pushdown();
      }
    };
    
    struct Seg_treap {
      Node* root;
    #define siz(_) (_ == nullptr ? 0 : _->siz)
    
      pair<Node*, Node*> split(Node* cur, int sz) {
        // partition by the tree size
        if (cur == nullptr) return {nullptr, nullptr};
        cur->check_tag();
        if (sz <= siz(cur->ch[0])) {
          // the left subtree is enough
          auto temp = split(cur->ch[0], sz);
          // not all of the left subtree is needed, temp.second is not needed
          cur->ch[0] = temp.second;
          cur->upd_siz();
          return {temp.first, cur};
        } else {
          // the left plus part of the right (including this node itself, of course)
          auto temp = split(cur->ch[1], sz - siz(cur->ch[0]) - 1);
          cur->ch[1] = temp.first;
          cur->upd_siz();
          return {cur, temp.second};
        }
      }
    
      Node* merge(Node* sm, Node* bg) {
        // small, big
        if (sm == nullptr && bg == nullptr) return nullptr;
        if (sm != nullptr && bg == nullptr) return sm;
        if (sm == nullptr && bg != nullptr) return bg;
        sm->check_tag(), bg->check_tag();
        if (sm->prio < bg->prio) {
          sm->ch[1] = merge(sm->ch[1], bg);
          sm->upd_siz();
          return sm;
        } else {
          bg->ch[0] = merge(sm, bg->ch[0]);
          bg->upd_siz();
          return bg;
        }
      }
    
      void insert(int val) {
        auto temp = split(root, val);
        auto l_tr = split(temp.first, val - 1);
        Node* new_node;
        if (l_tr.second == nullptr) new_node = new Node(val);
        Node* l_tr_combined =
            merge(l_tr.first, l_tr.second == nullptr ? new_node : l_tr.second);
        root = merge(l_tr_combined, temp.second);
      }
    
      void seg_rev(int l, int r) {
        // here less and more are relative to l
        auto less = split(root, l - 1);
        // all those less than or equal to l - 1 will be on the left of less
        auto more = split(less.second, r - l + 1);
        // take out the first r - l + 1 starting from l
        more.first->to_rev = true;
        root = merge(less.first, merge(more.first, more.second));
      }
    
      void print(Node* cur) {
        if (cur == nullptr) return;
        cur->check_tag();
        print(cur->ch[0]);
        cout << cur->val << " ";
        print(cur->ch[1]);
      }
    };
    
    Seg_treap tr;
    
    int main() {
      srand(time(nullptr));
      int n, m;
      cin >> n >> m;
      for (int i = 1; i <= n; i++) tr.insert(i);
      while (m--) {
        int l, r;
        cin >> l >> r;
        tr.seg_rev(l, r);
      }
      tr.print(tr.root);
    }
    ```

## Example problems

[Ordinary Balanced Tree](https://loj.ac/problem/104)

[Literary Balanced Tree (Splay)](https://loj.ac/problem/105)

[「ZJOI2006」Bookshelf](https://www.luogu.com.cn/problem/P2596)

[「NOI2005」Maintaining a Sequence](https://www.luogu.com.cn/problem/P2042)

[CF 702F T-Shirts](http://codeforces.com/problemset/problem/702/F)

## References and notes

[^ref1]: The design of this figure references [the illustration of the Wikipedia treap entry](https://en.wikipedia.org/wiki/Treap)

[^ref2]: <https://charleswu.site/archives/1051>

[^ref3]: <https://www.cnblogs.com/Equinox-Flower/p/10785292.html>

[^ref4]: <https://www.luogu.com.cn/blog/85514/fhq-treap-xue-xi-bi-ji>
