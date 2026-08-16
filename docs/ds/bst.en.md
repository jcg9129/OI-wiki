author: 2323122, aofall, AtomAlpaca, Bocity, CoelacanthusHex, countercurrent-time, Early0v0, Enter-tainer, fearlessxjdx, Great-designer, H-J-Granger, hsfzLZH1, iamtwz, Ir1d, ksyx, Marcythm, NachtgeistW, ouuan, Persdre, shuzhouliu, StudyingFather, SukkaW, Tiphereth-A, wsyhb, Yesphet, yuhuoji, lingkerio, bililateral, q-wind

## Definition

A binary search tree is a binary-tree-form data structure, defined as follows:

1.  An empty tree is a binary search tree.

2.  If the left subtree of a binary search tree is not empty, then the additional weights of all points in its left subtree are less than the value of its root node.

3.  If the right subtree of a binary search tree is not empty, then the additional weights of all points in its right subtree are greater than the value of its root node.

4.  The left and right subtrees of a binary search tree are both binary search trees.

The time taken by basic operations on a binary search tree is proportional to the height of this tree. For a binary search tree with $n$ nodes, the best-case time complexity of these operations is $O(\log n)$ and the worst case is $O(n)$. The expected height of a randomly constructed such binary search tree is $O(\log n)$.

## Process

### Definition of a binary-search-tree node

???+ note "Implementation"
    ```cpp
    struct TreeNode {
      int key;
      TreeNode* left;
      TreeNode* right;
      // maintain other information, such as height, node count, etc.
      int size;   // size of the subtree rooted at the current node
      int count;  // number of duplicates of the current node
    
      TreeNode(int value)
          : key(value), size(1), count(1), left(nullptr), right(nullptr) {}
    };
    ```

### Traversing a binary search tree

From the recursive definition of a binary search tree, the sequence of weights of the inorder traversal of a binary search tree is a non-decreasing sequence. The time complexity is $O(n)$.

The code for traversing a binary search tree is as follows:

???+ note "Implementation"
    ```cpp
    void inorderTraversal(TreeNode* root) {
      if (root == nullptr) {
        return;
      }
      inorderTraversal(root->left);
      std::cout << root->key << " ";
      inorderTraversal(root->right);
    }
    ```

### Finding the minimum/maximum

By the property of a binary search tree, the minimum on a binary search tree is the top of the tree's left chain, and the maximum is the top of the tree's right chain. The time complexity is $O(h)$.

???+ note "Implementation"
    ```cpp
    int findMin(TreeNode* root) {
      if (root == nullptr) {
        return -1;
      }
      while (root->left != nullptr) {
        root = root->left;
      }
      return root->key;
    }
    
    int findMax(TreeNode* root) {
      if (root == nullptr) {
        return -1;
      }
      while (root->right != nullptr) {
        root = root->right;
      }
      return root->key;
    }
    ```

### Searching for an element

Search for a node with value `value` in the binary search tree rooted at `root`.

The case analysis is as follows:

-   If `root` is empty, return `false`.
-   If `root`'s weight equals `value`, return `true`.
-   If `root`'s weight is greater than `value`, continue searching in `root`'s left subtree.
-   If `root`'s weight is less than `value`, continue searching in `root`'s right subtree.

The time complexity is $O(h)$.

???+ note "Implementation"
    ```cpp
    bool search(TreeNode* root, int target) {
      if (root == nullptr) {
        return false;
      }
      if (root->key == target) {
        return true;
      } else if (target < root->key) {
        return search(root->left, target);
      } else {
        return search(root->right, target);
      }
    }
    ```

Insertion, deletion, and modification all require searching in the binary search tree first.

### Inserting an element

Insert a node with value `value` in the binary search tree rooted at `root`.

The case analysis is as follows:

-   If `root` is empty, directly return a new node with value `value`.

-   If `root`'s weight equals `value`, increment the additional field of that node recording the number of times this value appears by $1$.

-   If `root`'s weight is greater than `value`, insert a node with weight `value` in `root`'s left subtree.

-   If `root`'s weight is less than `value`, insert a node with weight `value` in `root`'s right subtree.

The time complexity is $O(h)$.

???+ note "Implementation"
    ```cpp
    TreeNode* insert(TreeNode* root, int value) {
      if (root == nullptr) {
        return new TreeNode(value);
      }
      if (value < root->key) {
        root->left = insert(root->left, value);
      } else if (value > root->key) {
        root->right = insert(root->right, value);
      } else {
        root->count++;  // node values are equal, increase the duplicate count
      }
      root->size = root->count + (root->left ? root->left->size : 0) +
                   (root->right ? root->right->size : 0);  // update the node's subtree size
      return root;
    }
    ```

### Deleting an element

Delete a node with value `value` in the binary search tree rooted at `root`.

First search for the node with weight `value` in the binary search tree; the case analysis is as follows:

-   If that node's additional `count` is greater than $1$, just decrease `count`.

-   If that node's additional `count` is $1$:

    -   If `root` is a leaf node, just delete the node directly.

    -   If `root` is a chain node, i.e. a node with only one child, return this child.

    -   If `root` has two non-empty children, it is generally replaced by the maximum of its left subtree (the rightmost node of the left subtree) or the minimum of its right subtree (the leftmost node of the right subtree), and then deleted.

The time complexity is $O(h)$.

???+ note "Implementation"
    The method uses `root = remove(root, 1)` to mean deleting the node with value 1 in the tree rooted at `root`, and returning the new root node.
    
    ```cpp
    // the return value here is the new root after deleting value
    TreeNode* remove(TreeNode* root, int value) {
      if (root == nullptr) {
        return root;
      }
      if (value < root->key) {
        root->left = remove(root->left, value);
      } else if (value > root->key) {
        root->right = remove(root->right, value);
      } else {
        if (root->count > 1) {
          root->count--;  // the node's duplicate count is greater than 1, decrease it
        } else {
          if (root->left == nullptr) {
            TreeNode* temp = root->right;
            delete root;
            return temp;
          } else if (root->right == nullptr) {
            TreeNode* temp = root->left;
            delete root;
            return temp;
          } else {
            TreeNode* successor = findMinNode(root->right);
            root->key = successor->key;
            root->count = successor->count;  // update the duplicate count
            // when successor->count > 1, that node should also be deleted; otherwise
            // subsequent deletion only decreases the duplicate count
            successor->count = 1;
            root->right = remove(root->right, successor->key);
          }
        }
      }
      // continue to maintain size; it is not written as --root->size;
      // because value may not be in the tree, so no deletion may have occurred
      root->size = root->count + (root->left ? root->left->size : 0) +
                   (root->right ? root->right->size : 0);
      return root;
    }
    
    // here we take the minimum of the right subtree as an example
    TreeNode* findMinNode(TreeNode* root) {
      while (root->left != nullptr) {
        root = root->left;
      }
      return root;
    }
    ```

### Finding the rank of an element

The rank is defined as the number of numbers before the first identical element after sorting the array elements in ascending order, plus one.

To find the rank of an element, first jump from the root to this element; if jumping right, add the number of nodes in the left child plus the number of duplicates of the current node to the answer, and finally add the size of the endpoint's left-child subtree plus one to the answer.

The time complexity is $O(h)$.

???+ note "Implementation"
    ```cpp
    int queryRank(TreeNode* root, int v) {
      if (root == nullptr) return 0;
      if (root->key == v) return (root->left ? root->left->size : 0) + 1;
      if (root->key > v) return queryRank(root->left, v);
      return queryRank(root->right, v) + (root->left ? root->left->size : 0) +
             root->count;
    }
    ```

### Finding the element with rank k

In a subtree, the rank of the root node depends on the size of its left subtree.

-   If its left subtree's size is greater than or equal to $k$, then the element is in the left subtree;

-   If its left subtree's size is in the interval $[k-\textit{count},k-1]$ (`count` is the number of occurrences of the current node's value), then the element is the root node of the subtree;

-   If its left subtree's size is less than $k-\textit{count}$, then the element is in the right subtree.

The time complexity is $O(h)$.

???+ note "Implementation"
    ```cpp
    int querykth(TreeNode* root, int k) {
      if (root == nullptr) return -1;  // or return another appropriate value as needed
      if (root->left) {
        if (root->left->size >= k) return querykth(root->left, k);
        if (root->left->size + root->count >= k) return root->key;
      } else {
        if (k <= root->count) return root->key;
      }
      return querykth(root->right,
                      k - (root->left ? root->left->size : 0) - root->count);
    }
    ```

## Introduction to balanced trees

One of the purposes of using a search tree is to shorten the time of inserting, deleting, modifying, and searching (insertion, deletion, and modification all include the search operation) nodes.

Regarding search efficiency, if a tree's height is $h$, then in the worst case, searching for a key requires $h$ comparisons, and the search time complexity (also the average search length, ASL) does not exceed $O(h)$. The time of all operations on an ideal binary search tree can be shortened to $O(\log n)$ (n is the total number of nodes).

However, $O(\log n)$ time complexity is only the ideal case. In the worst case, a search tree may degenerate into a linked list. Imagine a binary search tree where every node has only a right child; then its properties are the same as a linked list, and the time of all operations (insert, delete, modify, search) is $O(n)$.

We can see that the complexity of the operations is related to the tree's height $h$. This leads to balanced trees, which reduce the complexity of operations by maintaining the tree's height (balance) through certain operations.

### Definition of balance

Regarding whether a search tree is "**balanced**", different balanced trees have different definitions of "**balance**". For example, for a binary search tree rooted at T, if the heights of the left and right subtrees differ greatly, or the number of nodes in the left subtree is far greater than that in the right subtree, this tree clearly is not balanced.

For a binary search tree, a common definition of balance is: for the tree rooted at T, the height difference between the left and right subtrees of every node is at most 1.

-   In a [Splay tree](splay.md), for any access operation on any node (search, insertion, or deletion), the accessed node is moved to the root position of the tree.

-   An [AVL tree](avl.md) maintains, at each node N, the height information of the tree rooted at N. The AVL tree's definition of balance: T is an AVL tree if and only if its left and right subtrees are also AVL trees and $|height(T->left) - height(T->right)| \leq 1$.

-   A [Size Balanced Tree](sbt.md) maintains, at each node N, the number of nodes `size` in the tree rooted at N. Its definition of balance: the `size` of any node is not less than the `size` of any child (nephew) of its sibling.

In addition, for search trees with the same set of element values, the balanced state may not be unique. That is, two different search trees may contain the same set of element values and both be balanced.

### The balance-adjustment process

Performing an adjustment operation on a search tree that does not satisfy the balance condition can make the unbalanced search tree balanced again.

Regarding a balanced binary tree, the balance-adjustment operations include two kinds: **left rotation (Left Rotate, or zag)** and **right rotation (Right Rotate, or zig)**. Since a balanced binary tree must keep the inorder traversal sequence unchanged when adjusting, both operations do not change the inorder traversal sequence.

Here we first introduce right rotation, also called "single right rotation" or "LL balance rotation". The right rotation of node $A$ means: rotating $A$'s left child $B$ up-right to replace $A$ as the root, rotating node $A$ down-right to become the root of $B$'s right subtree, and $B$'s original right subtree becomes $A$'s left subtree.

![bst-rotate](images/bst-rotate.svg)

The right-rotation operation only changes three groups of node associations, equivalent to a cyclic permutation of three groups of edges, so a node needs to be temporarily stored before performing the rotational update.

For the right-rotation operation, the general update order is: temporarily store node $B$ (the new root), let $A$'s left child point to $B$'s right subtree $T2$, then let $B$'s right-child pointer point to $A$, and finally let $A$'s parent point to the stored $B$.

By complete analogy, there is a corresponding left-rotation operation, also called "single left rotation" or "RR balance rotation". The left-rotation and right-rotation operations are mirror images of each other.

Below is the code for left rotation and right rotation.

???+ note "Implementation"
    ```cpp
    TreeNode* rotateLeft(TreeNode* root) {
      TreeNode* newRoot = root->right;
      root->right = newRoot->left;
      newRoot->left = root;
      // update the information of the relevant nodes
      updateHeight(root);
      updateHeight(newRoot);
      return newRoot;  // return the new root node
    }
    
    TreeNode* rotateRight(TreeNode* root) {
      TreeNode* newRoot = root->left;
      root->left = newRoot->right;
      newRoot->right = root;
      updateHeight(root);
      updateHeight(newRoot);
      return newRoot;
    }
    ```

For this sample code, when calling it you need to save `root`'s parent `pre`. The method returns a pointer to the new root node; you only need to point `pre` to the new root node.

#### The four cases of broken balance

Although the definitions of different balanced binary trees differ somewhat, the difference between different balanced binary trees lies only in the information maintained at nodes and the information updated at nodes after a rotational adjustment. There are only the following four cases where the balance of a balanced binary tree is broken. The operations for balance adjustment include only left rotation and right rotation. Below we first introduce the four cases, then compare different balanced binary trees.

LL type: the left subtree of T's left child is too long, breaking the balance.

Adjustment method: right-rotate node T.

![bst-LL](images/bst-LL.svg)

RR type: similar to the LL type, the right subtree of T's right child is too long, breaking the balance.

Adjustment method: left-rotate node T.

![bst-RR](images/bst-RR.svg)

LR type: the right subtree of T's left child is too long, breaking the balance.

Adjustment method: first left-rotate node L to become an LL type, then right-rotate node T.

![bst-LR](images/bst-LR.svg)

RL type: similar to the LR type, the left subtree of T's right child is too long, breaking the balance.

Adjustment method: first right-rotate node R to become an RR type, then left-rotate node T.

![bst-RL](images/bst-RL.svg)
