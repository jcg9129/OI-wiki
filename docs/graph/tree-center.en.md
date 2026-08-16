author: littleparrot12345

## Definition

In a tree, if when node $x$ is taken as the root node, the longest chain starting from $x$ is the shortest, then $x$ is called the center of this tree.

## Properties

-   The center of a tree is not necessarily unique, but there are at most $2$, and these two centers are adjacent.
-   The center of a tree must lie on the diameter of the tree.
-   The paths from all points on the tree to their farthest point must meet at the center of the tree.
-   When the center of the tree is the root node, the two chains from it to the endpoints of the diameter are the longest chain and the second-longest chain respectively.
-   When merging two trees into one tree by connecting an edge between them, connecting the centers of the two trees can minimize the diameter of the new tree.
-   The distance from the center of a tree to any other node does not exceed half of the tree diameter.

## Method

Find a point $x$ such that when it is the root node, the length of the longest chain is the shortest.

### Specific steps

1.  Maintain $len1_x$, denoting the longest chain within the subtree of node $x$.
2.  Maintain $len2_x$, denoting the longest chain that does not overlap with $len1_x$.
3.  Maintain $up_x$, denoting the longest chain outside the subtree of node $x$; this chain must pass through the parent node of $x$.
4.  Find the point $x$ that minimizes $\max(len1_x, up_x)$; then $x$ is the center of the tree.

???+ note "Reference code"
    ```cpp
    // this code assumes node numbering starts from 1, i.e. i ∈ [1,n], and uses a vector to store the graph
    int d1[N], d2[N], up[N], x, y, mini = 1e9;  // d1,d2 correspond to len1,len2 above
    
    struct node {
      int to, val;  // to is the node the edge points to, val is the edge weight
    };
    
    vector<node> nbr[N];
    
    void dfsd(int cur, int fa) {  // compute len1 and len2
      for (node nxtn : nbr[cur]) {
        int nxt = nxtn.to, w = nxtn.val;  // nxt is the node this edge leads to, val is the edge weight
        if (nxt == fa) {
          continue;
        }
        dfsd(nxt, cur);
        if (d1[nxt] + w > d1[cur]) {  // can update the longest chain
          d2[cur] = d1[cur];
          d1[cur] = d1[nxt] + w;
        } else if (d1[nxt] + w > d2[cur]) {  // cannot update the longest chain, but can update the second-longest chain
          d2[cur] = d1[nxt] + w;
        }
      }
    }
    
    void dfsu(int cur, int fa) {
      for (node nxtn : nbr[cur]) {
        int nxt = nxtn.to, w = nxtn.val;
        if (nxt == fa) {
          continue;
        }
        up[nxt] = up[cur] + w;
        if (d1[nxt] + w != d1[cur]) {  // if the longest chain in one's own subtree is not in the nxt subtree
          up[nxt] = max(up[nxt], d1[cur] + w);
        } else {  // the longest chain in one's own subtree is in the nxt subtree, can only use the second-longest chain
          up[nxt] = max(up[nxt], d2[cur] + w);
        }
        dfsu(nxt, cur);
      }
    }
    
    void GetTreeCenter() {  // count the centers of the tree, recorded as x and y (if they exist)
      dfsd(1, 0);
      dfsu(1, 0);
      for (int i = 1; i <= n; i++) {
        if (max(d1[i], up[i]) < mini) {  // found the point with the current smallest max(len1[x],up[x])
          mini = max(d1[i], up[i]);
          x = i;
          y = 0;
        } else if (max(d1[i], up[i]) == mini) {  // another center
          y = i;
        }
      }
    }
    ```

### Example

Suppose we have a tree, as shown below:

```text
           A
          / \
         B   C
        / \   \
       D   E   F
```

-   The diameter of the tree is $D \rightarrow B \rightarrow A \rightarrow C \rightarrow F$. The diameter length is $4$.
-   The center of the tree is node $A$, because the longest chain starting from $A$ (to $D$ or $F$) is both $2$.
-   If we take $B$ or $C$ as the root of the tree, then the longest chain starting from these nodes will increase, so they are not the center of the tree.

### Time complexity

The time complexity of the above algorithm is $O(n)$, where $n$ is the number of nodes in the tree.

## References

-   [TutorialsPoint: Centers of a Tree](https://www.tutorialspoint.com/centers-of-a-tree)
-   [ProofWiki: Definition of Center of Tree](https://proofwiki.org/wiki/Definition:Center_of_Tree)
-   [Wikipedia: Tree (graph theory)](https://en.wikipedia.org/wiki/Tree_%28graph_theory%29#Properties)
