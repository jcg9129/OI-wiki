## Introduction

Trees in graph theory look the same as trees in real life, except that we are used to placing the tree root at the top when considering problems. This data structure looks like an upside-down tree, hence the name.

## Definition

A tree without a fixed root node is called an **unrooted tree**. There are several equivalent formal definitions of an unrooted tree:

-   A connected undirected graph with $n$ nodes and $n-1$ edges

-   An undirected acyclic connected graph

-   An undirected graph in which there is one and only one simple path between any two nodes

-   A connected graph in which every edge is a bridge

-   A graph that has no cycle, and after adding an edge between any two different points the resulting graph contains a unique cycle

On the basis of an unrooted tree, designating one node as the **root** forms a **rooted tree**. A rooted tree is still often represented as an undirected graph, only that the superior-subordinate relationship between nodes is specified; see below for details.

## Definitions related to trees

### Applicable to both unrooted and rooted trees

-   **Forest**: a graph in which each connected component (connected block) is a tree. By definition, a tree is also a forest.

-   **Spanning tree**: a spanning subgraph of a connected undirected graph, which is also required to be a tree. That is, select $n - 1$ edges from the edge set of the graph to connect all vertices.

-   **Leaf node of an unrooted tree**: a node with degree not exceeding $1$.

    ???+ question "Why not degree exactly $1$?"
        Consider $n = 1$.

-   **Leaf node of a rooted tree**: a node with no child nodes.

### Applicable only to rooted trees

-   **Parent node**: for each node other than the root, defined as the second node on the path from this node to the root.  
    The root node has no parent node.
-   **Ancestor**: the nodes on the path from a node to the root node, except the node itself.  
    The ancestor set of the root node is empty.
-   **Child node**: if $u$ is the parent of $v$, then $v$ is a child node of $u$.  
    The order of child nodes is generally not distinguished; the binary tree is an exception.
-   **Depth of a node**: the number of edges on the path to the root node.
-   **Height of a tree**: the maximum of the depths of all nodes.
-   **Sibling**: multiple child nodes of the same parent are siblings of each other.
-   **Descendant**: child nodes and the descendants of child nodes.  
    Or understood as: if $u$ is an ancestor of $v$, then $v$ is a descendant of $u$.

![tree-definition.svg](images/tree-definition.svg)

-   **Subtree**: after deleting the edge connected to the parent, the subgraph in which this node is located.

    ![tree-definition-subtree.svg](images/tree-definition-subtree.svg)

## Special trees

-   **Chain (path graph)**: a tree satisfying that no more than $2$ edges are connected to any node is called a chain.

-   **Star**: a tree satisfying that there exists $u$ such that all nodes other than $u$ are connected to $u$ is called a star.

-   **Rooted binary tree**: a rooted tree in which each node has at most two sons (child nodes) is called a binary tree. The order of the two child nodes is often distinguished, calling them the left child node and the right child node respectively.  
    In most cases, the term **binary tree** refers to a rooted binary tree.

-   **Full/proper binary tree**: a binary tree in which the number of child nodes of each node is 0 or 2. In other words, each node is either a leaf, or its left and right subtrees are both non-empty.

    ![](images/tree-binary-proper.svg)

-   **Complete binary tree**: only the bottom two levels of nodes can have degree less than 2, and the nodes at the bottom level are all concentrated at consecutive positions on the leftmost side of that level.

    ![](images/tree-binary-complete.svg)

-   **Perfect binary tree**: a binary tree in which all leaf nodes have the same depth and the number of child nodes of all non-leaf nodes is 2 is called a perfect binary tree.

    ![](images/tree-binary-perfect.svg)

???+ warning "Warning"
    The Chinese translation of "proper binary tree" is not fixed, and the definitions of complete binary tree and full binary tree differ in different textbooks; when encountering them, one needs to judge according to the context.

The "full binary tree" that OIers speak of mostly refers to the perfect binary tree.

## Storage

### Recording only the parent node

Use an array `parent[N]` to record the parent node of each node.

This way can obtain relatively little information, and is inconvenient for top-down traversal. It is commonly used in bottom-up recurrence problems.

### Adjacency list

-   For an unrooted tree: allocate a linear list for each node, recording all nodes connected to it.
    ```cpp
    std::vector<int> adj[N];
    ```
-   For a rooted tree:
    -   Method one: if what is given is an undirected graph, it can still be stored in the above form. Below we will introduce how to distinguish the superior-subordinate relationship of nodes.
    -   Method two: if the input data can ensure the superior-subordinate relationship of nodes, then we can use this information. Allocate a linear list for each node, recording all its child nodes; if needed, we can also record its parent node in another array.
        ```cpp
        std::vector<int> children[N];
        int parent[N];
        ```
        Of course, we can also use other ways (such as a linked list) instead of `std::vector`.

### Left-child right-sibling representation

#### Procedure

For a rooted tree, there exists a simple representation method.

First, arbitrarily determine an order for all child nodes of each node.

Then, for each node, record two values: its **first child node** `child[u]` and its **next sibling node** `sib[u]`. If there is no child node, then `child[u]` is empty; if this node is the last child node of its parent node, then `sib[u]` is empty.

#### Implementation

Traversing all child nodes of a node can be implemented in the following way.

```cpp
int v = child[u];  // start from the first child node
while (v != EMPTY_NODE) {
  // ...
  // process child node v
  // ...
  v = sib[v];  // go to the next child node, i.e. a sibling of v
}
```

It can also be abbreviated to the following form.

```cpp
for (int v = child[u]; v != EMPTY_NODE; v = sib[v]) {
  // ...
  // process child node v
  // ...
}
```

### Binary tree

We need to record the left and right child nodes of each node.

???+ note "Implementation"
    ```cpp
    int parent[N];
    int lch[N], rch[N];
    // -- or --
    int child[N][2];
    ```

## Tree traversal

### DFS on a tree

DFS on a tree is the following process: first visit the root node, then visit the subtrees of each son of the root node respectively.

It can be used to find information such as the depth and parent of each node.

### Binary tree DFS traversal

#### Preorder traversal

![preorder](images/tree-basic-preorder.svg)

Traverse the binary tree in the order **root, left, right**.

???+ note "Implementation"
    ```cpp
    void preorder(BiTree* root) {
      if (root) {
        cout << root->key << " ";
        preorder(root->left);
        preorder(root->right);
      }
    }
    ```

#### Inorder traversal

![inorder](images/tree-basic-inorder.svg)

Traverse the binary tree in the order **left, root, right**.

???+ note "Implementation"
    ```cpp
    void inorder(BiTree* root) {
      if (root) {
        inorder(root->left);
        cout << root->key << " ";
        inorder(root->right);
      }
    }
    ```

#### Postorder traversal

![postorder](images/tree-basic-postorder.svg)

Traverse the binary tree in the order **left, right, root**.

???+ note "Implementation"
    ```cpp
    void postorder(BiTree* root) {
      if (root) {
        postorder(root->left);
        postorder(root->right);
        cout << root->key << " ";
      }
    }
    ```

#### Reverse derivation

Given the inorder traversal sequence and one other sequence, we can find the third sequence.

![reverse](images/tree-basic-reverse.svg)

1.  The first of the preorder is the `root`, and the last of the postorder is the `root`.
2.  First determine the root node, then according to the inorder traversal, the part to the left of the root is the left subtree, and the part to the right of the root is the right subtree.
3.  Each subtree can be regarded as a brand-new tree, still following the above pattern.

### BFS on a tree

Start from the tree root and visit nodes strictly by level.

During the BFS process, we can also incidentally find the depth and parent node of each node.

#### Level-order traversal of a tree

The level-order traversal of a tree refers to traversing each node horizontally level by level, according to the level relationship from the root node to the leaf nodes. According to the definition of BFS, we know that the traversal order obtained by BFS is a kind of level-order traversal. But level-order traversal requires distinguishing different levels, so its result is usually represented in the form of a two-dimensional array.

For example, the result of the level-order traversal of the tree in the figure below is `[[1], [2, 3, 4], [5, 6]]` (each level from left to right).

![tree-basic-levelOrder](images/tree-basic-levelOrder.svg)

???+ note "Implementation"
    ```cpp
    vector<vector<int>> levelOrder(Node* root) {
      if (!root) {
        return {};
      }
      vector<vector<int>> res;
      queue<Node*> q;
      q.push(root);
      while (!q.empty()) {
        int currentLevelSize = q.size();  // number of nodes in the current level
        res.push_back(vector<int>());
        for (int i = 0; i < currentLevelSize; ++i) {
          Node* cur = q.front();
          q.pop();
          res.back().push_back(cur->val);
          for (Node* child : cur->children) {  // add all child nodes
            q.push(child);
          }
        }
      }
      return res;
    }
    ```

### Binary tree Morris traversal

The core problem of binary tree traversal is how to return to the current node and continue traversing after traversing the child nodes of the current node. Both the recursive method and the non-recursive method of traversing a binary tree use a stack structure to record the return path, in order to achieve movement from a lower level to an upper level. Its space complexity is $O(\log n)$ at best and $O(n)$ at worst (when the binary tree is linear).

The essence of Morris traversal is to avoid using a stack, and use the idle `right` pointer of a lower-level node to point back to some node at an upper level, thereby completing the movement from a lower level to an upper level.

#### Procedure of Morris traversal

Assume we arrive at the current node `cur`, starting at the root node position.

1.  If `cur` is empty, the traversal stops; otherwise perform the following process.
2.  If `cur` has no left subtree, `cur` moves right (`cur = cur->right`).
3.  If `cur` has a left subtree, find the rightmost node on the left subtree, denoted `mostRight`.
    -   If the `right` pointer of `mostRight` points to empty, make it point to `cur`, then `cur` moves left (`cur = cur->left`).
    -   If the `right` pointer of `mostRight` points to `cur`, modify it to `null`, then `cur` moves right (`cur = cur->right`).

For example, `cur` starts visiting from node 1.

![tree-basic-morris-1](images/tree-basic-morris-1.svg)

When `cur` visits node 2 for the first time, find the rightmost node 4 on the left subtree, and make the `right` pointer of 4 point to `cur` (node 2).

![tree-basic-morris-2](images/tree-basic-morris-2.svg)

`cur` returns to the upper level through the `right` pointer of 4; when visiting node 2 for the second time, find the rightmost node 4 on the left subtree, modify the `right` pointer of 4 to `null`, then continue visiting the right subtree. The subsequent process is omitted.

![tree-basic-morris-1](images/tree-basic-morris-1.svg)

The visiting order of the whole tree is `1242513637`. We can find that nodes with a left subtree are visited twice, and nodes without a left subtree are visited only once.

???+ note "Implementation"
    ```cpp
    void morris(TreeNode* root) {
      TreeNode* cur = root;
      while (cur) {
        if (!cur->left) {
          // if the current node has no left child, output the value of the current node and enter the right subtree
          std::cout << cur->val << " ";
          cur = cur->right;
          continue;
        }
        // find the rightmost node of the left subtree of the current node
        TreeNode* mostRight = cur->left;
        while (mostRight->right && mostRight->right != cur) {
          mostRight = mostRight->right;
        }
        if (!mostRight->right) {
          // if the right pointer of the rightmost node is empty, make it point to the current node, and enter the left subtree
          mostRight->right = cur;
          cur = cur->left;
        } else {
          // if the right pointer of the rightmost node points to the current node, it means the left subtree has been fully traversed, output the value of the current node and enter the right subtree
          mostRight->right = nullptr;
          std::cout << cur->val << " ";
          cur = cur->right;
        }
      }
    }
    ```

### Unrooted tree

#### Procedure

Tree traversal is generally depth-first traversal; the thing most needing attention in this process is avoiding repeated visits to nodes.

Since a tree is an acyclic graph, we only need to record from which node the current node was visited, and then enter all adjacent nodes except that node, to avoid repeated visits.

???+ note "Implementation"
    ```cpp
    void dfs(int u, int from) {
      // recursively enter all child nodes except from
      // for the starting node, from is empty, so all adjacent nodes will be visited, which is consistent with expectation
      for (int v : adj[u])
        if (v != from) {
          dfs(v, u);
        }
    }
    
    // when starting the traversal
    int EMPTY_NODE = -1;  // a non-existent number
    int root = 0;         // arbitrarily take a node as the starting point
    dfs(root, EMPTY_NODE);
    ```

### Rooted tree

For a rooted tree, we need to distinguish the superior-subordinate relationship of nodes.

Examining the above traversal process, if we traverse from the root, then when we visit a node, the value of `from` is exactly the number of its parent node.

Through this way, we can find the parent node of all nodes, as well as the child node list, for an undirected input.

**Part of the content of this page is quoted from the blog post [Binary tree: preorder traversal, inorder traversal, postorder traversal](https://blog.csdn.net/weixin_43357638/article/details/99730284), following the CC 4.0 BY-SA copyright license.**
