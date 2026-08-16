author:F7487

## Self-Adjusting Top Tree

### Introduction

The Self-Adjusting Top Tree is a data structure for maintaining a fully dynamic forest based on Top Tree theory, proposed by Tarjan and Werneck in 2005 in their paper Self-Adjusting Top Trees, abbreviated as SATT.

The Self-Adjusting Top Tree can implement operations such as chain modification/query, subtree modification/query, and non-local search on any tree in a forest.

The Splay Tree is the foundation of the SATT, but the Splay Tree used by the SATT is a bit different in details from an ordinary Splay (it has been extended somewhat).

### Problem introduction

Maintain a forest, supporting the following operations:

-   Delete or add an edge, guaranteeing it is still a forest before and after the operation.

-   Modify the weights of a certain simple path on a certain tree.

-   Modify the subtree weights rooted at a certain point.

-   Query the sum of weights of a certain simple path on a certain tree.

-   Query the sum of subtree weights rooted at a certain point.

### Tree contraction

For any tree, we can apply the **tree contraction** theory to contract it into an edge.

Specifically, tree contraction has two basic operations: **Compress** and **Rake**. The Compress operation specifies a point $x$ of degree $2$; denote the two points adjacent to point $x$ as $y$, $z$; we connect a new edge $yz$; put the information of point $x$, edge $xz$, and edge $xy$ into $yz$ for storage, and delete them. As shown in the figure.

![](./images/top-tree1.svg)

The Rake operation specifies a point $x$ of degree $1$, and the degree of the point $y$ adjacent to point $x$ needs to be greater than $1$; let the other neighbor of point $y$ be $z$; we put the information of point $x$ and edge $xy$ into edge $yz$ for storage, and delete them. As shown in the figure.

![](./images/top-tree2.svg)

It is not hard to prove that any tree can be contracted into an edge using only Compress and Rake operations, as shown in the figure.

![](./images/top-tree3.svg)

### Cluster

For convenience of expression, we denote the original tree before any operation as $T$. The tree after performing some tree-contraction operations (possibly no operation) on $T$ is denoted as $T_x$.

We study the information contained in a certain edge in some $T_x$.

Besides carrying its own information (of course, if this edge does not exist in $T$, then this edge has no information of its own), this edge may also contain the information of other points and edges merged onto it through Compress/Rake operations. We may as well first select an edge from the tree-contraction process in the figure below, and see which points and edges in $T$ the information it contains represents.

![](./images/top-tree4.svg)

As in the figure, the selected edge and the corresponding graph have been circled in red.

We can see that the points and edges in $T$ represented by the information contained in this edge are connected. We can generalize that the information stored in any edge in any $T_x$ always manifests in $T$ as a connected subgraph. We call such a connected subgraph a **Cluster**.

However, a cluster is an **incomplete subgraph**; the endpoints of some edges it contains are not contained by the cluster itself. So we call these endpoints the **Endpoints** of the cluster, call the points of the connected subgraph it contains **Internal Nodes**, and call the edges of the connected subgraph **Internal Edges**.

For any cluster, there are the following properties:

1.  A cluster only stores and maintains the information of internal nodes and internal edges.

2.  A cluster has two endpoints. These two endpoints are the two points connected by the edge representing that cluster in $T_x$. The path between the two endpoints is called the **Cluster Path**; denote the two endpoints of a cluster as $x$, $y$; below we use $C(x,y)$ to denote this cluster.

3.  Internal nodes are only connected to endpoints or internal nodes.

In particular, for each edge in $T$, each is an independent cluster on its own (containing only the edge's own information); we call this kind of cluster a **Base Cluster**. For the final $T_x$ contracted from $T$ to only one edge, the cluster represented by that edge contains the information of the whole $T$ except the two endpoints; we call this cluster the **Root Cluster**.

![](./images/top-tree5.svg)

As in the figure, the base clusters mentioned above have been marked in red.

Looking at the Compress/Rake operations from the perspective of clusters, we find that these two operations "combine two clusters into one", leaving a new cluster, so the process of tree contraction is also the process of all base clusters merging into one cluster.

So we can also obtain the figure below, which is another representation of a series of tree-contraction operations.

![](./images/top-tree6.svg)

### Top Tree

We now want to represent the whole process of tree contraction of a certain tree.

We can use the two methods above to represent this process, but this is very cumbersome; if the tree contraction takes $n$ steps, we would need $n$ trees to represent the whole tree contraction.

Consider a more convenient representation of a certain tree contraction of a certain tree; we introduce the **Top Tree**.

![](./images/top-tree7.jpg)

As in the figure, this is a Top Tree based on the contraction method above and the original tree.

The Top Tree has the following properties;

1.  A Top Tree corresponds to an original tree and a method of tree-contracting it; each node of the Top Tree represents a certain edge in some $T_x$, i.e. a certain cluster formed during the tree-contraction process. The point of the form $N_x$ in the figure represents the cluster formed by the operation `compress(x)`.

2.  A node in the Top Tree has two children (each representing a cluster); the cluster represented by this node is the new cluster obtained by merging these two clusters through a Compress or Rake operation.

3.  The leaf nodes of the Top Tree are base clusters, and its root node is the root cluster. Therefore we stratify by the topological order of a Top Tree, and each layer of it represents a $T_x$.

### Implementing information maintenance with a three-degreed Self-Adjusting Top Tree

#### Principle

The Top Tree's great simplification of the tree-contraction process allows us to see the possibility of maintaining information on a tree by maintaining the tree-contraction process; the SATT maintains information on a tree through this principle.

Note that the tree-contraction process is also a process of information on the tree being continuously added; when we execute a `compress(x)`, the information of point $x$ starts to appear in some cluster from that moment, affecting our statistical result.

Suppose we now use a Top Tree to maintain a certain tree $T$, where each point and edge on the tree has a weight, and what we want to maintain is the sum of weights of $T$.

Now while maintaining, we want to modify the weight of a certain point $x$ in $T$; clearly, we need to change the node information of all nodes in the Top Tree whose cluster information contains $x$; doing so has a single-operation time complexity on the order of $O(n)$.

However, if the point we choose has very few nodes in the Top Tree whose cluster information contains $x$, i.e. its information is added to a cluster as late as possible, then the single-operation time complexity of our operation will have a great improvement. As in the figure.

![](./images/top-tree8.jpg)

The SATT maintains information on a tree by modifying the order in which the information of **a certain point / a certain path** is added to a cluster during the tree-contraction process (to reduce its single-operation time complexity when being modified).

### Actual structure

We first stratify and root an original tree $T$, then we consider the root cluster of a Top Tree of some tree-contraction order; it has two endpoints; we make one of these endpoints be the root of the original tree, and choose the other endpoint arbitrarily.

![](./images/top-tree9.jpg)

As in the figure, a set of endpoints is chosen for the root cluster; when marking the cluster here, the endpoints are also circled in.

From the basic operations of tree contraction, we know that the information of the points and edges $(j,h,c,jh,hc)$ on the cluster path is finally added to $C(k,g)$ through the Compress operation, while the non-cluster-path points $(a,b,i,f,g,e,ig,\cdots)$ are added to $C(k,g)$ through the Rake operation.

We take the cluster path out separately; this is a specially-shaped tree (a chain), and we build a top tree for this tree (the tree-contraction order it represents is arbitrary).

![](./images/top-tree10.jpg)

We call this structure the **Compress Tree**, because in this Top Tree the two children of any point are merged into their parent through the Compress operation.

The nodes in the Compress Tree are called **Compress Nodes**. Considering only the current cluster path, a non-leaf Compress Node represents a compress process, meaning merging the information of the left child and the right child, and then adding the point $x$ information stored by this `compress(x)` itself. This Compress Tree then maintains the information of the $C(k,g)$ cluster path.

In addition, in the Compress Tree, we actually impose some restrictions on the Top Tree used. Note that the Compress Tree maintains a chain where the depths of the points in $T$ are pairwise distinct; we stipulate that in the Compress Tree the in-order traversal order of base clusters is consistent with the depth of the corresponding edges in $T$, and the smaller the in-order traversal, the shallower the depth. Similarly, the relation for the `compress(x)` corresponding to each point $x$ is also like this.

Now to maintain the information of those non-cluster paths, we assume that the points and edges on these non-cluster paths have already formed maximal clusters, and these maximal clusters are formed by Rake operations among these smaller clusters circled in blue lines; for the process of forming a maximal cluster by merging some smaller clusters, we use a ternary tree to represent it; similarly, we call this structure the **Rake Tree**, and correspondingly the points in the Rake Tree are **Rake Nodes**. Each Rake Node represents a cluster, formed by its left child and right child being Raked onto the smaller cluster represented by its middle child. See the figure below for details; we can see that each point in the Rake Tree represents a smaller cluster in $T$ with the same endpoints.

![](./images/top-tree11.jpg)

As in the figure, the blue lines circle maximal clusters, and the yellow lines circle smaller clusters.

For those smaller clusters, we process them the same way, choosing cluster paths for them, building Compress Trees, ... and so on recursively, thereby building many Compress Trees and Rake Trees representing the tree-contraction process.

![](./images/top-tree12.jpg)

The figure above is the Rake-Compress Tree of the original tree (because each Rake Node is connected to a Compress Tree, it appears as a shape of a Rake Tree connected to many Compress Trees) and the Compress Tree representing the root cluster path.

Consider splicing these trees together in some way so that they form an ordered whole. Denote the common endpoint of the set of smallest clusters represented by a Rake Tree as point $x$. We add the other endpoint that is not $x$ to the middle children (a set of Compress Trees) of these Rake Nodes, but still keep their in-order traversal and the basic properties of the Top Tree, as in the figure.

![](./images/top-tree13.jpg)

This step is equivalent to letting the Rake operation of adding a certain point in $T$ happen directly in the Compress Tree; this not only allows us to correctly maintain the information of the Rake Node (just merge the information of the three children), but also makes the structure of our Compress Tree more complete. In the next step, we change the Compress Tree into a ternary tree; if the common endpoint of a certain Rake Tree is point $x$, we hang the Rake Tree at the middle child of `compress(x)`, as in the figure.

![](./images/top-tree14.jpg)

At this point, the three-degreed `compress(x)` point, its meaning becomes first Raking its middle child onto the cluster path, then counting the information of the left and right children and point $x$.

Finally, we handle the Compress Tree of the root cluster path once more: consistent with all other Compress Trees, add its two endpoints in in-order-traversal order, so that its root stores the information of the whole $T$.

Thus we have implemented maintaining the information of a tree with a three-degreed Self-Adjusting Top Tree.

![](./images/top-tree15.jpg)

To summarize, the SATT has the following properties:

1.  The SATT is composed of Compress Trees and Rake Trees; the Compress Tree is a special Top Tree; the Rake Tree is a ternary tree; they both correspond to the process of tree-contracting a tree.

2.  A point in the Compress Tree has at most three children. The Compress Tree can do rotation operations similar to a Splay tree (just guarantee its in-order traversal is unchanged; when rotating a point, keep its middle child fixed).

3.  A point in the Rake Tree must have a middle child. The Rake Tree can do rotation operations similar to a Splay tree (just guarantee its in-order traversal is unchanged; when rotating a point, keep its middle child fixed).

4.  The topological order of the SATT reflects the tree-contraction order of the original tree $T$.

Can the SATT implement the "modifying the order in which the information of a certain point / a certain path is added to a cluster during the tree-contraction process" mentioned above? The answer is affirmative.

In the SATT, there is an `access(x)` operation, whose role is to make a certain point $x$ become the non-root endpoint of the root cluster, and at the same time make `compress(x)` become the root of the SATT.

We can, through the `access(x)` operation, in amortized $O(\log n)$ complexity make the point representing `compress(x)` in the SATT rotate to the root of the whole SATT; according to the fourth property of the SATT, we change the operation order of `compress(x)`, making it execute the latest, so the information of point $x$ is added the latest; in this way, when we want to modify the information of point $x$, we only need to update `compress(x)`.

### Code implementation

#### Push-type functions

First consider pushing up information, i.e. the `Pushup(x)` function. When considering maintaining information for a certain node of the SATT, we first discuss by cases whether this point is in a Compress Tree or a Rake Tree, for the reason seen above, which is not repeated here; below we take maintaining the subtree size of a certain point as an example

```cpp
// ls(x) the left child of x
// rs(x) the right child of x
// ms(x) the middle child of x
// type==0 is a Compress Node
// type==1 is a Rake Node
void pushup(int x, int type) {
  if (type == 0)
    size[x] = size[rs(x)] + size[ms(x)] + 1;
  else
    size[x] = size[rs(x)] + size[ms(x)] + size[ls(x)];
  return;
}
```

To query the subtree size of point $x$, Access it to the SATT root; the answer is the size of its middle child $+1$; because, according to the above, after Access, its middle child is its true subtree.

Then consider pushing down information, i.e. the `Pushdown(x)` function. If we want to make an overall modification to a certain subtree in the original tree, a very natural idea is: directly Access this node to the SATT root node, and apply a tag to its middle child. Similarly, to query a subtree, directly Access and then query the middle child.

If we want to make an overall modification to a certain path in the original tree, we expose the two endpoints of the path, where `expose(x, y)` means making point $x$ become the root node of $T$ and making point $y$ become the other endpoint of the root cluster. Correspondingly on the SATT, at this point the Compress Tree of the root cluster is the path from $x$ to $y$. So just directly apply a tag to the Compress Tree of the root cluster. Similarly, to query a chain, expose and then query the root node.

So we know how to do the problem introduction problem.

```cpp
void pushdown(int x, int type) {
  if (type == 0) {
    // handle the chain
    chain[ls(x)] += chain[x] chain[rs(x)] += chain[x];
    val[ls(x)] += chain[x];
    val[rs(x)] += chain[x];
    // handle the subtree
    subtree[ls(x)] += subtree[x];
    subtree[rs(x)] += subtree[x];
    subtree[ms(x)] += subtree[x];
    val[ls(x)] += subtree[x];
    val[rs(x)] += subtree[x];
    val[ms(x)] += subtree[x];
    subtree[x] = 0;
  } else {
    subtree[ls(x)] += subtree[x];
    subtree[rs(x)] += subtree[x];
    subtree[ms(x)] += subtree[x];
    val[ls(x)] += subtree[x];
    val[rs(x)] += subtree[x];
    val[ms(x)] += subtree[x];
    subtree[x] = 0;
  }
  return;
}

// push down the tag
void pushall(int x, int type) {
  if (!isroot(x)) pushall(father[x], type);
  pushdown(x, type);
  return;
}
```

#### Splay-type functions

We know that both the Rake Tree and the Compress Tree in the SATT can be rotated, which means they can be maintained with Splay. Therefore we can write the following code:

```cpp
// is a node's middle child or has no parent
// ls the left child of a SATT node
// rs the right child of a SATT node
// ms the middle child of a SATT node
// type==1 in a Rake Tree
// type==0 in a Compress Tree
bool isroot(int x) { return rs(father[x]) != x && ls(father[x]) != x; }

bool direction(int x) { return rs(father[x]) == x; }

void rotate(int x, int type) {
  int y = father[x], z = father[y], d = direction(x), w = son[x][d ^ 1];
  if (z) son[z][ms(z) == y ? 2 : direction(y)] = x;
  son[x][d ^ 1] = y;
  son[y][d] = w;
  if (w) father[w] = y;
  father[y] = x;
  father[x] = z;
  pushup(y, type);
  pushup(x, type);
  return;
}

void splay(int x, int type, int goal = 0) {
  pushall(x, ty);  // push down the tag
  for (int y; y = father[x], (!isroot(x)) && y != goal; rotate(x, ty)) {
    if (father[y] != goal && (!isroot(y))) {
      rotate(direction(x) ^ diretion(y) ? x : y, type);
    }
  }
  return;
}
```

It is worth noting that the functions `direction` and `isroot` differ from the ordinary Splay. Because no matter how this point is rotated, the middle child of this point will not change.

#### Access-type functions

The meaning of `access(x)` is: rotate point $x$ to the root of the whole SATT, making point $x$ become one of the two endpoints of the root cluster (the other endpoint being the root node of $T$), while not changing the structure of the original tree and the root of the original tree.

To implement `access(x)`, we first rotate it to the root of the Compress Tree it is in, then remove point $x$'s right child, making point $x$ become the endpoint of the cluster corresponding to the Compress Tree it is in.

```cpp
if (rs(x)) {
  int y = new_node();
  setfather(ms(x), y, 0);
  setfather(rs(x), y, 2);
  rs(x) = 0;
  setfather(y, x, 2);
  pushup(y, 1);
  pushup(x, 0);
}
```

If at this point point $x$ has already reached the root, then exit; if not, then execute the following steps to make it cross over the Rake Tree above it:

1.  Splay its parent node (which must be a Rake Node) to the root of its Rake Tree;

2.  Splay $x$'s grandparent node (which must be a Compress Node) to the root of its Compress Tree.

3.  If $x$'s grandparent node has a right child, then swap point x and the grandparent node's right child, update the information, then exit.

4.  If the grandparent node has no right child, then first make point $x$ become the right child of the grandparent node; at this point point $x$'s original parent node has no middle child, and according to the property of a Rake Node above, it cannot exist. So call the `Delete` function to delete it, then exit.

Steps 1 and 2 are collectively called **Local Splay**. Steps 3 and 4 are collectively called **Splice**. But for convenience, we write them all in the `Splice(x)` function.

The `Delete(x)` function mentioned above is like this:

1.  Check whether the point $x$ to be deleted has a left child; if so, rotate the successor of the left child's subtree to below point $x$ (becoming the new left child), then make the right child (if any) become the right child of the left child; at this point point $x$'s left child replaces point $x$. This is equivalent to Splay's merge operation.

2.  If there is no left child, then directly let its right child replace point $x$.

It is not hard to find that `Splice(x)` changes the endpoint selection of some clusters of the original tree. After a splice is done, we treat point $x$'s parent node as the new point $x$, and perform the next splice.

Finally we will find that the point $x$ we originally wanted to operate on must be at the rightmost end of the root cluster's Compress Tree. We only need to finally do a **Global Splay** to rotate it to the SATT root.

```cpp
// ls the left child of a SATT node
// rs the right child of a SATT node
// ms the middle child of a SATT node
// son[x][0] ls
// son[x][1] rs
// son[x][2] ms
// type==1 in a Rake Tree
// type==0 in a Compress Tree
int new_node() {
  if (top) {
    top--;
    return Stack[top + 1];
  }
  return ++tot;
}

void setfather(int x, int fa, int type) {
  if (x) father[x] = fa;
  son[fa][type] = x;
}

void Delete(int x) {
  setfather(ms(x), father[x], 1);
  if (ls(x)) {
    int p = ls(x);
    pushdown(p, 1);
    while (rs(p)) p = rs(p), pushdown(p, 1);
    splay(p, 1, x);
    setfather(rs(x), p, 1);
    setfather(p, father[x], 2);
    pushup(p, 1);
    pushup(father[x], 0);
  } else
    setfather(rs(x), father[x], 2);
  Clear(x);
}

void splice(int x) {
  // local splay
  splay(x, 1);
  int y = father[x];
  splay(y, 0);
  pushdown(x, 1);
  // splice
  if (rs(y)) {
    swap(father[ms(x)], father[rs(y)]);
    swap(ms(x), rs(y));
  } else
    Delete(x);
  pushup(x, 1);
  pushup(y, 0);
}

void access(int x) {
  splay(x, 0);
  if (rs(x)) {
    int y = new_node();
    setfather(ms(x), y, 0);
    setfather(rs(x), y, 2);
    rs(x) = 0;
    setfather(y, x, 2);
    pushup(y, 1);
    pushup(x, 0);
  }
  while (father[x]) {
    splice(father[x]);
    x = father[x];
    pushup(x, 0);
  }
  splay(x, 0)  // global splay
}
```

To make a point become the root of the original tree, we Access point $x$ to the SATT root node; we know that at this point point $x$ is already an endpoint of the final-state cluster. From the in-order-traversal property of the Compress Tree, we know that reversing left and right (swapping the left and right children of all points) of the Compress Tree that point $x$ is in makes point $x$ become the root of the original tree. In the specific implementation, we perform this process by applying a reversal tag to point $x$ and pushing it down later.

```cpp
void makeroot(int x) {
  access(x);
  push_rev(x);
}
```

So `expose(x, y)` is ready to appear:

```cpp
void expose(int x, int y) {
  makeroot(x);
  access(y);
}
```

### Link & Cut

Now we want to connect an edge between two disconnected points in the original tree; we first make one of the points $x$ become the root of the original tree, then rotate the other point $y$ to the root; we know that at this point point $y$ should become the right child of point $x$. Then hang this edge on point $y$'s right child (in a SATT that only needs to maintain points, this step can be omitted).

```cpp
void Link(int x, int y, int z) {
  // z represents the edge connecting x, y
  access(x);
  makeroot(y);
  setfather(y, x, 1);
  setfather(z, y, 0);
  pushup(x, 0);
  pushup(y, 0);
}
```

`Cut` is roughly the same principle as `Link`

```cpp
void cut(int x, int y) {
  expose(x, y);
  clear(rs(x));  // delete the base cluster xy
  father[x] = ls(y) = rs(x);
  pushup(y, 0);
}
```

### Full code

??? note "[Luogu P3690 【Template】Dynamic Tree](https://www.luogu.com.cn/problem/P3690)"
    ```cpp
    --8<-- "docs/ds/code/top-tree/top-tree_1.cpp"
    ```

### Proof of the time complexity of the SATT

Let the potential function of the current state $x$ of a SATT (with $n$ points) be

$$
\varphi(x)= \sum_{i=1}^{n} r(i)
$$

where $r(i) = \lceil \log_2 \text{siz}(i) \rceil$. $\text{siz}(i)$ is the size of the subtree rooted at $i$.

Then the amortized complexity of the SATT's splay is obviously still $3n\log n + 1$, even if the SATT is a ternary tree.

Therefore for the SATT, as long as we prove that the Access function complexity is correct, we can prove the time complexity of the SATT.

We analyze the amortized complexity of Access step by step.

We first need to rotate point $x$ to the root of the Compress Tree it is in; then the amortized complexity of this step

$$
a \leq  3\log n +1
$$

Next we need to make point $x$ have no right child; then the amortized complexity of this step

$$
a = 1 + r'(\gamma)- 0 \leq \log n +1
$$

![](./images/top-tree16.jpg)

As in the figure, this is the process of removing point $x$'s right child.

Then is the process of Local Splay and Splice alternating; after several Splices, point $x$ is rotated to the root of the SATT. We analyze one group of Local Splay and Splice:

![](./images/top-tree17.jpg)

![](./images/top-tree18.jpg)

![](./images/top-tree19.jpg)

As in the figure, this reflects the process of doing one Splice on point $x$, not including the last part of left-rotating point $x$.

For convenience of expression, let $r_x(i)$ be the $r$ value of point $i$ in state $x$.

From the figure, it is easy to know that the amortized complexity of the operation from state 1 to state 2 (the Local Splay operation of rotating point $x$'s parent to the root of its Rake Tree)

$$
a \leq  3(r_2(\gamma)- r_1(\gamma))+1
$$

From the figure, it is easy to know that the amortized complexity of the operation from state 2 to state 3 (the Local Splay operation of rotating point $x$'s grandparent to the root of its Compress Tree)

$$
a \leq  3(r_3(B)- r_2(B))+1
$$

Focus on analyzing the operation from state 3 to state 4 (Splice)

$$
a = r_4(\gamma) -r_3(\gamma) +1
$$

It is not hard to find that $r_4(\gamma) \leq r_3(B)$

So the amortized complexity of this operation is

$$
\begin{aligned}
a &\leq r_3(B)- r_3(\gamma)+1\\
&\leq 3(r_3(B)- r_3(\gamma))+1\\
\end{aligned}
$$

Combining the above process, the complexity of one Splice is

$$
a\leq 3r_3(B)+3r_3(B)+3r_2(\gamma)-3r_3(\gamma)-3r_2(B)-3r_1(\gamma)+3
$$

Denote the $r$ value of the point $X$ of the next Splice (i.e. point $B$ in state 4) as $r'(X)$, and note that $r_3(\gamma),r_1(\gamma) \ge r_1(X)$, $r_3(B),r_2(\gamma) \leq r'(X)$ and $r_3(B)=r_2(B)$, so

$$
a\leq  9(r'(X)-r(X))+3
$$

Besides the above complexity, in Splice there may also be additional amortized complexity due to `delete(x)`; denote this part as $a' \leq 3\log n +1$.

Ignoring the $a'$ part for now, the $r'(X)$ of each Splice equals the $r(X)$ of the next, and the $r(X)$ of the first Splice equals the $r(X)$ when we initially rotate point $x$ to the root of its Compress Tree; then for the complexity of one `access(x)` not counting `delete(x)`, we have:

$$
a \leq 9(r'(x)-r(x))+ 3k + 1
$$

where $k$ is the number of Splices.

It seems $a$ carries a $3k+1$, causing the amortized complexity to be unanalyzable, but we have a way to deal with it; note that the rotation of zig-zig/zig-zag can be amortized this way

$$
\begin{aligned}
a &\leq 3(r'(X)-r(X)) + q\\
&\leq 3(q-1)(r'(X)-r(X))
\end{aligned}
$$

If we can find enough zig-zig and zig-zag operations, we can amortize this $3k+1$ onto these operations, thereby eliminating this $3k+1$.

We find that the Global Splay has exactly this many zig-zig and zag-zig for us to use, because the number of points in the Global Splay must be greater than $k$, and the number of points on the path from point $x$ to the Global Splay root must be no fewer than $k$; that is to say, one `access(x)` must have at least $\dfrac k2$ zig-zag operations; counting the amortized complexity of the Global Splay $a \leq 3\log n +1$, the amortized complexity of one `access(x)` not counting `delete(x)` is

$$
\begin{aligned}
a&\leq 9(r'(X)-r(X)) + 3k + 1 + 18(r''(X)-r'(X)) -S+1 +3 \log n +1,S \ge 3k\\
a&\leq 18(r''(X)-r(X)) +2 +3\log n+1\\
a&\leq 21(r''(X)-r(X)) +3
\end{aligned}
$$

Now counting $a'$, we list the total expression for performing $m$ `access(x)` operations.

$$
\sum_{i=1}^m a_i' + \sum_{i=1}^m a_i = \sum_{i=1}^m c_i + \varphi(x_n) -\varphi(x_0)
$$

What we want is the actual complexity

$$
\begin{aligned}
\sum_{i=1}^m c_i &= \sum_{i=1}^m a_i +\sum_{i=1}^m a_i' - \varphi(x_n) +\varphi(x_0)\\
&\le \sum_{i=1}^m a_i' + 21m\log n +n\log n +3m
\end{aligned}
$$

Note that the essence of the `delete(x)` operation is deleting a Rake Node, but in $m$ operations we add at most $m$ Rake Nodes; by the definition of Rake Node, we initially have at most $n$ Rake Nodes, that is to say we will do at most $m+n$ `delete(x)` operations in total; from $a' \leq 3\log n +1$ we know

$$
\sum_{i=1}^m c_i \leq 3(m+n)\log n + 21m\log n +n\log n +4m +n
$$

So we have proved the complexity of Access, and other functions are either based on Access or have constant single-operation time complexity, so we have proved the complexity of the SATT.

By the way, if, like the LCT, we omit the Global Splay process and instead directly rotate the point to Access once at each Splice, the time complexity of doing so is also correct (actual testing shows that the version omitting Global Splay is much faster, and can run neck and neck with the LCT on Luogu P3690).

### Example problems

#### Example problem 1

???+ note "[CEOI 2019 Dynamic Diameter](https://loj.ac/p/3163)"
    Given a tree with $n$ nodes where each edge has an edge weight, there are $q$ updates, each modifying the edge weight of one edge and querying the diameter of the tree. Forced online.

To maintain the dynamic diameter, after building the SATT, we only need to maintain the answer of each point in `Pushup(x)`, and finally query the answer of the root node (i.e. the diameter of the whole tree).

```cpp
void pushup(int x, int op) {
  if (op == 0) {
    // is a Compress Node
    len[x] = len[ls(x)] + len[rs(x)];
    diam[x] = maxs[ls(x)][1] + maxs[rs(x)][0];
    diam[x] =
        max(diam[x], max(maxs[ls(x)][1], maxs[rs(x)][0]) + maxs[ms(x)][0]);
    diam[x] = max(diam[x], max(max(diam[ls(x)], diam[rs(x)]), diam[ms(x)]));
    maxs[x][0] =
        max(maxs[ls(x)][0], len[ls(x)] + max(maxs[ms(x)][0], maxs[rs(x)][0]));
    maxs[x][1] =
        max(maxs[rs(x)][1], len[rs(x)] + max(maxs[ms(x)][0], maxs[ls(x)][1]));
  } else {
    // is a Rake Node
    diam[x] = maxs[ls(x)][0] + maxs[rs(x)][0];
    diam[x] =
        max(diam[x], maxs[ms(x)][0] + max(maxs[ls(x)][0], maxs[rs(x)][0]));
    diam[x] = max(max(diam[x], diam[ms(x)]), max(diam[ls(x)], diam[rs(x)]));
    maxs[x][0] = max(maxs[ms(x)][0], max(maxs[ls(x)][0], maxs[rs(x)][0]));
  }
  return;
}
```

Here $diam$ is the answer of the current point (the diameter of the cluster represented by this point). $len$ represents the length of the cluster path where the current Compress Node is; $maxs_{0/1}$ represents the maximum distance from the Compress Node to an internal point or endpoint of the cluster, not choosing the cluster-path child / not choosing the parent (if it is a Rake Node, then it only stores the maximum distance $maxs_0$ from the chosen upper endpoint of the current cluster to an internal point or endpoint of the cluster). Each time just query the diam of the SATT root node; the correctness is obvious.

Note to make some changes to `Pushrev(x)`.

```cpp
void pushrev(int x) {
  if (!x) return;
  r[x] ^= 1;
  swap(ls(x), rs(x));
  swap(maxs[x][0], maxs[x][1]);
}
```

#### Example problem 2

???+ note "[「CSP-S 2019」Centroid of a Tree](https://loj.ac/p/3213)"
    Given a tree, find the sum of the centroid numbers of the two subtrees split out after separately deleting each edge of the tree.

If we can dynamically maintain the centroid of a tree in $O(\log n)$, then we solve this problem.

The SATT supports dynamically maintaining the centroid of a tree in $O(\log n)$; achieving this requires **Non-local Search**.

For a certain property on a tree, if a point/edge has this property in the whole tree, and this property is contained in all subtrees containing it, then we call this property **Local**, otherwise we call it **Non-local**. Local information can generally be maintained through `pushup(x)`.

For example, the weight minimum is local, because if a point/edge has the minimum weight in the whole tree, then it also has the minimum weight in all subtrees containing it, while the second-minimum weight is obviously non-local.

The $diam$ we maintained above is also local information.

Back to the main topic, the centroid is obviously non-local information, which cannot be maintained through simple `pushup(x)`. We consider searching on the SATT:

Our search starts from the root node of the SATT, i.e. the root cluster. Note that the centroid has a very good property: if one side of an edge has a number of points greater than or equal to the number of points on the other side, then this side of the edge must have at least one centroid (there may be two centroids).

Denote $sum$ as the number of points of a certain cluster, and $maxs$ as the maximum $sum$ value among the middle children of all Rake Nodes of a Rake Tree.

```cpp
void pushup(int x, int op) {
  if (op == 0) {
    // is a Compress Node
    sum[x] = sum[ls(x)] + sum[rs(x)] + sum[ms(x)] + 1;
  } else {
    // is a Rake Node
    maxs[x] = max(maxs[ls(x)], max(maxs[rs(x)], sum[ms(x)]));
    sum[x] = sum[ls(x)] + sum[rs(x)] + sum[ms(x)];
  }
}
```

![](./images/top-tree20.jpg)

As in the figure, this is the SATT and the corresponding original tree $T$ when performing a Non-local Search.

We make the following comparisons:

1.  Compare the $sum$ value of cluster $compress(Y)$ with the $sum$ value of the union of cluster $compress(Z)$, cluster $A$, and point $X$ (which we temporarily call cluster $\alpha$). If the $sum$ value of $compress(Y)$ is greater than or equal to the latter, it means at least one centroid is in the subtree of $compress(Y)$, and we recurse to $compress(Y)$ to search. (If equality holds here, point $X$ is also a centroid, which needs to be recorded)

2.  Compare the $sum$ value of cluster $compress(Z)$ with the $sum$ value of the union of cluster $compress(Y)$, cluster $A$, and point $X$ (which we temporarily call cluster $\beta$). If the $sum$ value of $compress(Z)$ is greater than or equal to the latter, it means at least one centroid is in the subtree of $compress(Z)$, and we recurse to $compress(Z)$ to search. (If equality holds here, point $X$ is also a centroid, which needs to be recorded)

3.  Compare the $sum$ value of the smaller cluster with the largest $sum$ among the middle-child Rake tree of point $x$ with the $sum$ value of the union of cluster $compress(Y)$, cluster $A$, point $X$, and the other smaller clusters (which we temporarily call cluster $Y$); if the $sum$ value of that smaller cluster is greater than or equal to the latter, it means at least one centroid is in the subtree of that smaller cluster, and we recurse to it to search. If equality holds here, point $X$ is also a centroid, which needs to be recorded.

4.  If none of the above comparisons recurse, then point $X$ must be a centroid; record and exit.

The first-step search is obviously correct; how should we search afterwards?

Suppose we recurse to $Y$; then now the information stored by $Y$ is incomplete, because $compress(Y)$ only stores the information of its own cluster, while what we want is the centroid of the whole tree. The solution is to record the information of the previous cluster, and when comparing and computing at point $Y$, merge and process the information of the previous cluster with the information of point $Y$ itself. The specific implementation is as follows:

```cpp
void non_local_search(int x, int lv, int rv, int op) {
  // lv and rv are both the information of the previous cluster of the search
  if (!x) return;
  psd(x, 0);
  if (op == 0) {
    if (maxs[ms(x)] >=
        sum[ms(x)] - maxs[ms(x)] + sum[rs(x)] + sum[ls(x)] + lv + 1 + rv) {
      if (maxs[ms(x)] ==
          sum[ms(x)] - maxs[ms(x)] + sum[rs(x)] + sum[ls(x)] + lv + 1 + rv) {
        if (ans1)
          ans2 = x;
        else
          ans1 = x;
      }
      non_local_search(
          ms(x),
          sum[ms(x)] - maxs[ms(x)] + sum[rs(x)] + sum[ls(x)] + 1 + lv + rv, 0,
          1);
      return;
    }
    if (ss[rs(x)] + rv >= ss[ms(x)] + ss[ls(x)] + lv + 1) {
      if (ss[rs(x)] + rv == ss[ms(x)] + ss[ls(x)] + lv + 1) {
        if (ans1)
          ans2 = x;
        else
          ans1 = x;
      }
      non_local_search(rs(x), sum[ms(x)] + 1 + sum[ls(x)] + lv, rv, 0);
      return;
    }
    if (sum[ls(x)] + lv >= sum[ms(x)] + sum[rs(x)] + 1 + rv) {
      if (sum[ls(x)] + lv == sum[ms(x)] + sum[rs(x)] + 1 + rv) {
        if (ans1)
          ans2 = x;
        else
          ans1 = x;
      }
      non_local_search(ls(x), lv, rv + sum[ms(x)] + 1 + sum[rs(x)], 0);
      return;
    }
  } else {
    if (maxs[ls(x)] == maxs[x]) {
      non_local_search(ls(x), lv, rv, 1);
      return;
    }
    if (maxs[rs(x)] == maxs[x]) {
      non_local_search(rs(x), lv, rv, 1);
      return;
    }
    non_local_search(ms(x), lv, rv, 0);
    return;
  }
  if (ans1)
    ans2 = x;
  else
    ans1 = x;
}
```

??? note "Example code"
    ```cpp
    --8<-- "docs/ds/code/top-tree/top-tree_2.cpp"
    ```

### Reference

1.  Robert E. Tarjan and Renato F. Werneck. 2005. Self-adjusting top trees. In Proceedings of the sixteenth annual ACM-SIAM symposium on Discrete algorithms (SODA '05). Society for Industrial and Applied Mathematics, USA, 813–822. DOI 10.5555/1070432.1070547

2.  [negiizhao's blog](https://negiizhao.blog.uoj.ac/blog/4912)
