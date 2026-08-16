## Dynamic centroid decomposition

Dynamic centroid decomposition is used to solve tree path-information statistics problems **with point-weight/edge-weight modification**.

### Centroid decomposition tree

Recall the computation process of centroid decomposition.

For a node $x$, the simple paths in its subtree include two kinds: those passing through node $x$, composed of one or two paths starting from $x$; and those not passing through node $x$, i.e. paths already contained in the subtrees of all its child nodes.

For the computation of simple paths in a subtree, we choose a decomposition center $rt$, compute the information of the paths in the subtree passing through this node, then for each of its child nodes, treat the connected component where that point is located after deleting $rt$ as a subtree, and compute recursively. The chosen decomposition center points can constitute a tree-shaped structure, called the **centroid decomposition tree**. We find that the total size of the connected components represented by the nodes at the same level of the centroid decomposition tree (i.e. the connected component with that node as the decomposition center) is $O(n)$. This means that the time complexity of centroid decomposition is related to the depth of the centroid decomposition tree; if the depth of the centroid decomposition tree is $h$, then the complexity of centroid decomposition is $O(nh)$.

It can be proved that when we choose the centroid of the connected component as the decomposition center each time, the depth of the centroid decomposition tree is the smallest, being $O(\log n)$. In this way, we can count the information of $O(n^2)$ paths on the tree within $O(n\log n)$ time complexity.

Since the shape of the tree does not change during dynamic centroid decomposition, the shape of the centroid decomposition tree also does not change during dynamic centroid decomposition.

Below is the reference code for finding the centroid decomposition tree:

```cpp
void calcsiz(int x, int f) {
  siz[x] = 1;
  maxx[x] = 0;
  for (int j = h[x]; j; j = nxt[j])
    if (p[j] != f && !vis[p[j]]) {
      calcsiz(p[j], x);
      siz[x] += siz[p[j]];
      maxx[x] = max(maxx[x], siz[p[j]]);
    }
  maxx[x] =
      max(maxx[x], sum - siz[x]);  // maxx[x] denotes the maximum subtree size when x is the root
  if (maxx[x] < maxx[rt])
    rt = x;  // here we cannot write <= , to guarantee that rt does not change during the second calcsiz
}

void pre(int x) {
  vis[x] = true;  // means x is not considered in the subsequent process
  for (int j = h[x]; j; j = nxt[j])
    if (!vis[p[j]]) {
      sum = siz[p[j]];
      rt = 0;
      maxx[rt] = inf;
      calcsiz(p[j], -1);
      calcsiz(rt, -1);  // compute twice, the second time finds the sizes of the subtrees when rt is the root
      fa[rt] = x;
      pre(rt);  // record the parent on the centroid decomposition tree
    }
}

int main() {
  sum = n;
  rt = 0;
  maxx[rt] = inf;
  calcsiz(1, -1);
  calcsiz(rt, -1);
  pre(rt);
}
```

### Implementing modification

During querying and modification, we brute-force jump to the parent on the centroid decomposition tree to modify. Since the depth of the centroid decomposition tree is at most $O(\log n)$, doing so guarantees the complexity.

During dynamic centroid decomposition, we need the distance from a node to its ancestors on the centroid decomposition tree and other information; since a point has at most $O(\log n)$ ancestors, we can additionally compute the depth $dep[x]$ or use LCA when computing the centroid decomposition tree, preprocessing these distances or implementing real-time queries. **Note**: the distance from a node to its ancestors on the centroid decomposition tree does not necessarily increase, and cannot be accumulated!

During dynamic centroid decomposition, the information of a node in its ancestor nodes on the centroid decomposition tree may be counted repeatedly; this is where we need to eliminate the effect of the duplicated part. The general method is to record a connected component in two ways: one is its distance information to the decomposition center, and the other is its distance information to the parent of the decomposition center on the centroid decomposition tree. This part of the content will be shown in the example problems.

??? note "Example problem [「ZJOI2007」Hide and Seek](https://www.luogu.com.cn/problem/P2056)"
    Given a tree with $n$ nodes; initially all nodes are black. You need to implement the following two operations:
    
    1.  Reverse the color of a node (white to black, black to white);
    2.  Query the distance between the two farthest black points on the tree.
    
        $n\le 10^5,m\le 5\times 10^5$

Find the centroid decomposition tree, and for each node $x$ maintain two **deletable heaps**. $dist[x]$ stores the distance information from all black points in the connected component represented by node $x$ to $x$, and $ch[x]$ denotes the distance information from the black points among all children of node $x$ on the centroid decomposition tree and itself to $x$; because of this problem's greedy method of finding the answer, and two paths from the same subtree cannot become one complete path, we only insert its own value and the maximum value in each of its subtrees into this heap. We find that the sum of the two largest values in $ch[x]$ (if there are not two, then all values) is the longest black-endpoint path passing through node $x$ when the decomposition center is $x$. We can use a deletable heap $ans$ to store the answers of all nodes, and the maximum value in this heap is the answer we seek.

We can maintain these deletable heaps $dist[x],ch[x],ans$ according to the above definitions. When a value in $dist[x]$ changes, we can also maintain $ch[x],ans$ within $O(\log n)$ time complexity.

Now let's see how the $dist[x]$ value changes when we reverse the color of a point. When the node was originally black, what we perform is a delete operation; when the node was originally white, what we perform is an insert operation.

Suppose we want to reverse the color of node $x$. For all its ancestors $u$, we insert or delete $dist(x,u)$ in $dist[u]$, and simultaneously maintain the values of $ch[x],ans$. In particular, we need to insert or delete the value $0$ in $ch[x]$.

Reference code:

```cpp
--8<-- "docs/graph/code/dynamic-tree-divide/dynamic-tree-divide_1.cpp"
```

???+ note "Example problem [Luogu P6329 【Template】Centroid Decomposition Tree | Zhenbo](https://www.luogu.com.cn/problem/P6329)"
    Given a tree with $n$ nodes, where each node on the tree has a weight $v[x]$. Implement the following two operations:
    
    1.  Query the sum of weights of nodes at distance no more than $y$ from node $x$;
    2.  Modify the point weight of node $x$ to $y$, i.e. $v[x]=y$.

We use a dynamically-allocated weighted segment tree to record the distance information.

Similar to the idea of the previous problem, for each node, we maintain a segment tree $dist[x]$, denoting the distance information from all nodes in the decomposition block $x$ to node $x$, with the index being the distance, and the weight adding the point weight. The segment tree $ch[x]$ denotes the distance information from all nodes in the decomposition block $x$ to the parent node of node $x$ on the decomposition tree.

In this problem, all queries and modifications need to modify all ancestors on the centroid decomposition tree.

Taking the query operation as an example, if we want to query the sum of weights of nodes at distance no more than $y$ from node $x$, we first add to the answer the sum of weights in the segment tree $dist[x]$ from index $0$ to $y$, then we traverse all ancestors $u$ of $x$, let its lower-level ancestor be $v$, let $d=dist(x,u)$; if we do not enter the subtree containing $x$, i.e. the subtree rooted at $v$, then we add to the answer the sum of weights in the segment tree $dist[u]$ from index $0$ to $y-d$. Since we have repeatedly counted the part rooted at $v$, we subtract from the answer the sum of weights in the segment tree $ch[v]$ from index $0$ to $y-d$.

When performing the modification operation, we need to simultaneously maintain $dist[x]$ and $ch[x]$.

Reference code:

```cpp
--8<-- "docs/graph/code/dynamic-tree-divide/dynamic-tree-divide_2.cpp"
```
