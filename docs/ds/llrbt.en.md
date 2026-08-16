author: c-forrest, Enter-tainer, giiiiiithub, hly1204, iamtwz, Ir1d, kigawas, ksyx, luxuryspark567, mgt, orzAtalod, sandyzikun, SunsetGlow95, Tiphereth-A, current2020, untitledunrevised, yuhuoji

The left-leaning red-black tree is a variant of the [red-black tree](./rbtree.md); it imposes certain restrictions on the position of red edges (points), so that its insertion and deletion operations can form a one-to-one correspondence with the [2-3 tree](https://en.wikipedia.org/wiki/2%E2%80%933_tree).

We assume that the reader has already mastered at least one rotation-based balanced tree, so this article will not explain the rotation operation.

## Red-black tree

### Properties

A red-black tree satisfies the following properties:

1.  A node is red or black;
2.  A NIL node (empty leaf node) is black;
3.  The colors of all children of a red node must be black, i.e. there cannot be two consecutive red nodes on any path from each leaf to the root;
4.  All simple paths from any node to each leaf in its subtree contain the same number of black nodes. (Black-height balance)

This ensures that the longest path (alternating red and black) from the root node to any leaf does not exceed twice the shortest path (all black). This guarantees the balance of the tree.

Maintaining these properties is relatively complex; if we want to insert a node, first, it must be dyed red, otherwise it will break property 4. Even so, we may still break property 3. Therefore adjustment is needed. And deleting a node is even more troublesome; similar to insertion, we cannot delete a black node, otherwise it will break the black-height balance. How to conveniently solve these problems?

## Left Leaning Red Black Tree (LLRBT)

### Explanation

The left-leaning red-black tree is an easily implementable variant of the red-black tree.

In the following schematic diagrams of the left-leaning red-black tree, it is the edges that have colors rather than the nodes. We are accustomed to using a node's color to refer to the color of its parent edge.

The left-leaning red-black tree further restricts the red-black tree; the left and right children of a black node:

-   are either both black;
-   or the left child is red and the right child is black.

Conforming case:

![llrbt1](./images/llrbt-1.png)

Non-conforming case:

![llrbt2](./images/llrbt-2.png)

This is the "left-leaning" property of the left-leaning tree: red edges can only lean left.

### Process

#### Insertion

We first use the ordinary BST insertion method to insert a red leaf node at the bottom of the tree, and then, through bottom-up adjustment, make the tree after insertion still conform to the properties of the left-leaning red-black tree. The following describes the adjustment process:

![llrbt3](./images/llrbt-3.png)

After insertion, a right-leaning red edge may be produced, so we need to perform a left rotation for the case of a right-leaning red edge:

![llrbt4](./images/llrbt-4.png)

Consider that after the left rotation two consecutive left-leaning red edges will be produced:

![llrbt5](./images/llrbt-5.png)

Therefore we need to perform a right rotation on it. And for the situation after the right rotation, we should perform `color_flip` on it: i.e. flip the colors of this node and its two children

![llrbt6](./images/llrbt-6.png)

thereby eliminating the right-leaning red edge.

??? note "Reference code (partial)"
    ```cpp
    template <class Key, class Compare>
    typename Set<Key, Compare>::Node *Set<Key, Compare>::fix_up(
        Set::Node *root) const {
      if (is_red(root->rc) && !is_red(root->lc))  // fix right leaned red link
        root = rotate_left(root);
      if (is_red(root->lc) &&
          is_red(root->lc->lc))  // fix doubly linked left leaned red link
        // if (root->lc == nullptr), then the second expr won't be evaluated
        root = rotate_right(root);
      if (is_red(root->lc) && is_red(root->rc))
        // break up 4 node
        color_flip(root);
      root->size = size(root->lc) + size(root->rc) + 1;
      return root;
    }
    
    template <class Key, class Compare>
    typename Set<Key, Compare>::Node_Set<Key, Compare>::insert(
        Set::Node_root, const Key &key) const {
      if (root == nullptr) return new Node(key, kRed, 1);
      if (root->key == key)
        ;
      else if (cmp\_(key, root->key))  // if (key < root->key)
        root->lc = insert(root->lc, key);
      else
        root->rc = insert(root->rc, key);
      return fix_up(root);
    }
    ```

#### Deletion

The deletion operation is based on this idea: we cannot delete a black node, because that would break the black height. So we need to ensure that the node we finally delete is red.

##### Deleting the minimum node

First let's try deleting the minimum value in the whole tree.

How can we ensure that the node finally deleted is red? We need to maintain a property during the downward recursion: if the current node is `h`, then we need to ensure that `h` is red, or `h->lc` is red.

Consider the correctness of doing so: if we can successfully maintain this property through various rotation and color-flipping operations, then when we reach the minimum node `h_min`, we have `h_min` is red, or `h_min`'s left subtree—but `h_min` has no left subtree at all! So this guarantees that the minimum node must be red; since it is red, we can boldly delete it, and then adjust the tree with the same adjustment idea as the insertion operation.

Below we consider how to satisfy this property; note that we will **temporarily** break several properties of the left-leaning red-black tree during the downward recursion, but will restore them when we return from the recursion.

As described in the figure below is a relatively simple case; at this point `h->rc->lc` is black, and we only need one color flip:

![llrbt-7](./images/llrbt-7.png)

Moreover, after the flip shown above, `h->rc` and `h->rc->lc` will not form consecutive red edges;

But if `h->rc->lc` is red, the situation will be more complex:

![llrbt-8](./images/llrbt-8.png)

If we only perform a color flip, consecutive red edges will be produced, and considering that when we return from recursion, we cannot fix such a situation, so it needs to be handled.

Then we can perform the deletion:

??? note "Reference code (partial)"
    ```cpp
    template <class Key, class Compare>
    typename Set<Key, Compare>::Node *Set<Key, Compare>::move_red_left(
        Set::Node *root) const {
      color_flip(root);
      if (is_red(root->rc->lc)) {
        // assume that root->rc != nullptr when calling this function
        root->rc = rotate_right(root->rc);
        root = rotate_left(root);
        color_flip(root);
      }
      return root;
    }
    
    template <class Key, class Compare>
    typename Set<Key, Compare>::Node *Set<Key, Compare>::delete_min(
        Set::Node *root) const {
      if (root->lc == nullptr) {
        delete root;
        return nullptr;
      }
      if (!is_red(root->lc) && !is_red(root->lc->lc)) {
        // make sure either root->lc or root->lc->lc is red
        // thus make sure we will delete a red node in the end
        root = move_red_left(root);
      }
      root->lc = delete_min(root->lc);
      return fix_up(root);
    }
    ```

##### Deleting an arbitrary node

We first consider deleting a leaf: similar to deleting the minimum, we also maintain a property during the process of deleting an arbitrary value, but this time it is somewhat special, because we do not only go left but can go in both the left and right directions, so the property maintained during deletion is this: if we go left, and the current node is `h`, then we need to ensure that `h` is red, or `h->lc` is red; if we go right, and the current node is `h`, then we need to ensure that `h` is red, or `h->rc` is red. This ensures that we will always delete a red node in the end.

Below we consider deleting a non-leaf node; we only need to find the minimum node in its right subtree (if any), then replace the value of this node with the value of the minimum node of the right subtree, and finally delete the minimum node in the right subtree.

![llrbt-9](./images/llrbt-9.png)

But what if there is no right subtree? We need to rotate the left subtree over, so that this problem will not occur.

??? note "Reference code (partial)"
    ```cpp
    template <class Key, class Compare>
    typename Set<Key, Compare>::Node *Set<Key, Compare>::delete_arbitrary(
        Set::Node *root, Key key) const {
      if (cmp_(key, root->key)) {
        // key < root->key
        if (!is_red(root->lc) && !(is_red(root->lc->lc)))
          root = move_red_left(root);
        // ensure the invariant: either root->lc or root->lc->lc (or root and
        // root->lc after dive into the function) is red, to ensure we will
        // eventually delete a red node. therefore we will not break the black
        // height balance
        root->lc = delete_arbitrary(root->lc, key);
      } else {
        // key >= root->key
        if (is_red(root->lc)) root = rotate_right(root);
        if (key == root->key && root->rc == nullptr) {
          delete root;
          return nullptr;
        }
        if (!is_red(root->rc) && !is_red(root->rc->lc)) root = move_red_right(root);
        if (key == root->key) {
          root->key = get_min(root->rc);
          root->rc = delete_min(root->rc);
        } else {
          root->rc = delete_arbitrary(root->rc, key);
        }
      }
      return fix_up(root);
    }
    ```

## Implementation

The following code is a `Set` implemented with a left-leaning red-black tree, i.e. an ordered non-repeatable set:

??? note "Reference code"
    ```cpp
    #include <algorithm>
    #include <memory>
    #include <vector>
    
    template <class Key, class Compare = std::less<Key>>
    class Set {
     private:
      enum NodeColor { kBlack = 0, kRed = 1 };
    
      struct Node {
        Key key;
        Node *lc{nullptr}, *rc{nullptr};
        size_t size{0};
        NodeColor color;  // the color of the parent link
    
        Node(Key key, NodeColor color, size_t size)
            : key(key), color(color), size(size) {}
    
        Node() = default;
      };
    
      void destroyTree(Node *root) const {
        if (root != nullptr) {
          destroyTree(root->lc);
          destroyTree(root->rc);
          root->lc = root->rc = nullptr;
          delete root;
        }
      }
    
      bool is_red(const Node *nd) const {
        return nd == nullptr ? false : nd->color;  // kRed == 1, kBlack == 0
      }
    
      size_t size(const Node *nd) const { return nd == nullptr ? 0 : nd->size; }
    
      Node *rotate_left(Node *node) const {
        // left rotate a red link
        //          <1>                   <2>
        //        /    \\               //    \
        //       *      <2>    ==>     <1>     *
        //             /   \          /   \
        //            *     *        *     *
        Node *res = node->rc;
        node->rc = res->lc;
        res->lc = node;
        res->color = node->color;
        node->color = kRed;
        res->size = node->size;
        node->size = size(node->lc) + size(node->rc) + 1;
        return res;
      }
    
      Node *rotate_right(Node *node) const {
        // right rotate a red link
        //            <1>               <2>
        //          //    \           /    \\
        //         <2>     *   ==>   *      <1>
        //        /   \                    /   \
        //       *     *                  *     *
        Node *res = node->lc;
        node->lc = res->rc;
        res->rc = node;
        res->color = node->color;
        node->color = kRed;
        res->size = node->size;
        node->size = size(node->lc) + size(node->rc) + 1;
        return res;
      }
    
      NodeColor neg_color(NodeColor n) const { return n == kBlack ? kRed : kBlack; }
    
      void color_flip(Node *node) const {
        node->color = neg_color(node->color);
        node->lc->color = neg_color(node->lc->color);
        node->rc->color = neg_color(node->rc->color);
      }
    
      Node *insert(Node *root, const Key &key) const;
      Node *delete_arbitrary(Node *root, Key key) const;
      Node *delete_min(Node *root) const;
      Node *move_red_right(Node *root) const;
      Node *move_red_left(Node *root) const;
      Node *fix_up(Node *root) const;
      const Key &get_min(Node *root) const;
      void serialize(Node *root, std::vector<Key> *) const;
      void print_tree(Set::Node *root, int indent) const;
      Compare cmp_ = Compare();
      Node *root_{nullptr};
    
     public:
      using KeyType = Key;
      using ValueType = Key;
      using SizeType = std::size_t;
      using DifferenceType = std::ptrdiff_t;
      using KeyCompare = Compare;
      using ValueCompare = Compare;
      using Reference = Key &;
      using ConstReference = const Key &;
    
      Set() = default;
    
      Set(Set &) = default;
    
      Set(Set &&) noexcept = default;
    
      ~Set() { destroyTree(root_); }
    
      SizeType size() const;
    
      SizeType count(const KeyType &key) const;
    
      SizeType erase(const KeyType &key);
    
      void clear();
    
      void insert(const KeyType &key);
    
      bool empty() const;
    
      std::vector<Key> serialize() const;
    
      void print_tree() const;
    };
    
    template <class Key, class Compare>
    typename Set<Key, Compare>::SizeType Set<Key, Compare>::count(
        ConstReference key) const {
      Node *x = root_;
      while (x != nullptr) {
        if (key == x->key) return 1;
        if (cmp_(key, x->key))  // if (key < x->key)
          x = x->lc;
        else
          x = x->rc;
      }
      return 0;
    }
    
    template <class Key, class Compare>
    typename Set<Key, Compare>::SizeType Set<Key, Compare>::erase(
        const KeyType &key) {
      if (count(key) > 0) {
        if (!is_red(root_->lc) && !(is_red(root_->rc))) root_->color = kRed;
        root_ = delete_arbitrary(root_, key);
        if (root_ != nullptr) root_->color = kBlack;
        return 1;
      } else {
        return 0;
      }
    }
    
    template <class Key, class Compare>
    void Set<Key, Compare>::clear() {
      destroyTree(root_);
      root_ = nullptr;
    }
    
    template <class Key, class Compare>
    void Set<Key, Compare>::insert(const KeyType &key) {
      root_ = insert(root_, key);
      root_->color = kBlack;
    }
    
    template <class Key, class Compare>
    bool Set<Key, Compare>::empty() const {
      return size(root_) == 0;
    }
    
    template <class Key, class Compare>
    typename Set<Key, Compare>::Node *Set<Key, Compare>::insert(
        Set::Node *root, const Key &key) const {
      if (root == nullptr) return new Node(key, kRed, 1);
      if (root->key == key)
        ;
      else if (cmp_(key, root->key))  // if (key < root->key)
        root->lc = insert(root->lc, key);
      else
        root->rc = insert(root->rc, key);
      return fix_up(root);
    }
    
    template <class Key, class Compare>
    typename Set<Key, Compare>::Node *Set<Key, Compare>::delete_min(
        Set::Node *root) const {
      if (root->lc == nullptr) {
        delete root;
        return nullptr;
      }
      if (!is_red(root->lc) && !is_red(root->lc->lc)) {
        // make sure either root->lc or root->lc->lc is red
        // thus make sure we will delete a red node in the end
        root = move_red_left(root);
      }
      root->lc = delete_min(root->lc);
      return fix_up(root);
    }
    
    template <class Key, class Compare>
    typename Set<Key, Compare>::Node *Set<Key, Compare>::move_red_right(
        Set::Node *root) const {
      color_flip(root);
      if (is_red(root->lc->lc)) {  // assume that root->lc != nullptr when calling
                                   // this function
        root = rotate_right(root);
        color_flip(root);
      }
      return root;
    }
    
    template <class Key, class Compare>
    typename Set<Key, Compare>::Node *Set<Key, Compare>::move_red_left(
        Set::Node *root) const {
      color_flip(root);
      if (is_red(root->rc->lc)) {
        // assume that root->rc != nullptr when calling this function
        root->rc = rotate_right(root->rc);
        root = rotate_left(root);
        color_flip(root);
      }
      return root;
    }
    
    template <class Key, class Compare>
    typename Set<Key, Compare>::Node *Set<Key, Compare>::fix_up(
        Set::Node *root) const {
      if (is_red(root->rc) && !is_red(root->lc))  // fix right leaned red link
        root = rotate_left(root);
      if (is_red(root->lc) &&
          is_red(root->lc->lc))  // fix doubly linked left leaned red link
        // if (root->lc == nullptr), then the second expr won't be evaluated
        root = rotate_right(root);
      if (is_red(root->lc) && is_red(root->rc))
        // break up 4 node
        color_flip(root);
      root->size = size(root->lc) + size(root->rc) + 1;
      return root;
    }
    
    template <class Key, class Compare>
    const Key &Set<Key, Compare>::get_min(Set::Node *root) const {
      Node *x = root;
      // will crash as intended when root == nullptr
      for (; x->lc != nullptr; x = x->lc);
      return x->key;
    }
    
    template <class Key, class Compare>
    typename Set<Key, Compare>::SizeType Set<Key, Compare>::size() const {
      return size(root_);
    }
    
    template <class Key, class Compare>
    typename Set<Key, Compare>::Node *Set<Key, Compare>::delete_arbitrary(
        Set::Node *root, Key key) const {
      if (cmp_(key, root->key)) {
        // key < root->key
        if (!is_red(root->lc) && !(is_red(root->lc->lc)))
          root = move_red_left(root);
        // ensure the invariant: either root->lc or root->lc->lc (or root and
        // root->lc after dive into the function) is red, to ensure we will
        // eventually delete a red node. therefore we will not break the black
        // height balance
        root->lc = delete_arbitrary(root->lc, key);
      } else {
        // key >= root->key
        if (is_red(root->lc)) root = rotate_right(root);
        if (key == root->key && root->rc == nullptr) {
          delete root;
          return nullptr;
        }
        if (!is_red(root->rc) && !is_red(root->rc->lc)) root = move_red_right(root);
        if (key == root->key) {
          root->key = get_min(root->rc);
          root->rc = delete_min(root->rc);
        } else {
          root->rc = delete_arbitrary(root->rc, key);
        }
      }
      return fix_up(root);
    }
    
    template <class Key, class Compare>
    std::vector<Key> Set<Key, Compare>::serialize() const {
      std::vector<int> v;
      serialize(root_, &v);
      return v;
    }
    
    template <class Key, class Compare>
    void Set<Key, Compare>::serialize(Set::Node *root,
                                      std::vector<Key> *res) const {
      if (root == nullptr) return;
      serialize(root->lc, res);
      res->push_back(root->key);
      serialize(root->rc, res);
    }
    
    template <class Key, class Compare>
    void Set<Key, Compare>::print_tree(Set::Node *root, int indent) const {
      if (root == nullptr) return;
      print_tree(root->lc, indent + 4);
      std::cout << std::string(indent, '-') << root->key << std::endl;
      print_tree(root->rc, indent + 4);
    }
    
    template <class Key, class Compare>
    void Set<Key, Compare>::print_tree() const {
      print_tree(root_, 0);
    }
    ```

## Relationship with the 2-3 tree

The 2-3 tree is an order-3 B-tree; each node is a 2-node or a 3-node, storing one or two data elements. Non-leaf 2-nodes and 3-nodes can have only two or three children respectively. Moreover, all data stored in the 2-3 tree are ordered.

The 2-3 tree and the left-leaning red-black tree are essentially equivalent. A node in a 2-3 tree can store 1 element or 2 elements, while a node in a red-black tree can store only one element. As shown in the figure below, a 2-node of a 2-3 tree corresponds to a black node, and a 3-node corresponds to a red node and a black node (bc can be regarded as parallel).

![2-3-tree-rbt](images/2-3-tree-rbt-1.svg)

![2-3-tree-rbt](images/2-3-tree-rbt-2.svg)

The figure below is a left-leaning red-black tree corresponding to a 2-3 tree.

![2-3-tree-rbt](images/2-3-tree-rbt-3.svg)

The insertion and deletion operations of the 2-3 tree and the left-leaning red-black tree are in one-to-one correspondence. [^23-vs-llrbt]

## References and further reading

-   [Left-Leaning Red-Black Trees](https://sedgewick.io/wp-content/themes/sedgewick/papers/2008LLRB.pdf)-  Robert Sedgewick Princeton University
-   [Balanced Search Trees](https://algs4.cs.princeton.edu/lectures/keynote/33BalancedSearchTrees-2x2.pdf)-\_Algorithms\_Robert Sedgewick | Kevin Wayne

[^23-vs-llrbt]: [This blog post](https://riteme.site/blog/2016-3-12/2-3-tree-and-red-black-tree.html) provides a detailed description. The "red-black tree" in the text actually refers to the "left-leaning red-black tree".
