author: Alex-McAvoy, lingkerio, LvCGame

## Weighted path length of a tree

Suppose a binary tree has $n$ weighted leaf nodes; the sum of the products of the path length from the root to each leaf node and the corresponding leaf node's weight is called the **Weighted Path Length of Tree (WPL)**.

Let $w_i$ be the weight of the $i$-th leaf node of the binary tree and $l_i$ be the path length from the root to the $i$-th leaf node; then the WPL formula is as follows:

$$
WPL=\sum_{i=1}^nw_il_i
$$

![](./images/huffman-tree-1.svg)

As shown in the figure above, its WPL computation process and result are as follows:

$$
WPL=2*2+3*2+4*2+7*2=4+6+8+14=32
$$

## Structure

For a given group of leaf nodes with fixed weights, different binary trees can be constructed; among them, the **binary tree with the smallest WPL** is called a **Huffman tree**.

For a Huffman tree, the smaller a leaf node's weight, the farther it is from the root, and the larger a leaf node's weight, the closer it is to the root; in addition, only its leaf nodes have degree $0$, and all other nodes have degree $2$.

## The Huffman algorithm

The Huffman algorithm is used to construct a Huffman tree; the algorithm steps are as follows:

1.  **Initialization**: from the given $n$ weights, construct $n$ binary trees each with only one root node, obtaining a set of binary trees $F$.
2.  **Selecting and merging**: from the binary-tree set $F$, select the **two** binary trees with the **smallest** root-node weights as the left and right subtrees respectively to construct a new binary tree, whose root node's weight is the sum of the weights of its left and right subtrees' root nodes.
3.  **Deleting and adding**: delete the two binary trees serving as the left and right subtrees from $F$, and add the newly built binary tree into $F$.
4.  Repeat steps 2 and 3; when only one binary tree remains in the set, this binary tree is the Huffman tree.

![](./images/huffman-tree-2.svg)

### Proof of correctness

???+ note "Lemma"
    The two leaf nodes with the smallest weights in an optimal prefix-code tree (Huffman tree) are always the deepest leaf nodes, and adjusting these two nodes to be siblings at least does not break the optimality of the code tree.

??? note "Proof"
    We use proof by contradiction to prove this proposition. Suppose that in an optimal prefix-code tree, there exist two leaf nodes with the smallest weights that are not the deepest leaf nodes. Let these two nodes be $a$ and $b$, and let their depths be smaller than that of some deepest leaf node. For this deepest leaf node $c$, we can swap the positions of $a$ and $c$, or of $b$ and $c$. Since the Huffman algorithm guarantees that each level of the tree merges by the leaf nodes with the smallest weights, after swapping, the tree's weighted path length (WPL) will decrease. From this contradiction we can conclude that the assumption does not hold, so the two leaf nodes with the smallest weights must be the deepest leaf nodes.
    
    Next, assume these two smallest-weight leaf nodes are $a$ and $b$ with the same depth. If in an optimal prefix-code tree these two nodes are not siblings, suppose there exist other nodes $c$ and $d$ that are siblings of $a$ and $b$ respectively (assume $a$ and $c$ are siblings, $b$ and $d$ are siblings). We can merge $a$ and $b$ into one subtree.
    
    -   If the sum of the weights of $a$ and $b$ after merging is smaller than the weight of $c$ or $d$, then we can merge the merged subtree with the node of larger weight (such as $c$ or $d$) to form a new subtree, and the WPL will decrease.
    -   If the sum of the weights of $a$ and $b$ is not smaller than the weights of $c$ and $d$, we can directly adjust $a$ and $b$ to be siblings, with $c$ and $d$ as another pair of siblings, and the WPL will not increase.
    
    Therefore, after such adjustment, optimality is not broken. Q.E.D.

???+ note "Theorem"
    The prefix-code tree obtained by the Huffman algorithm is an optimal prefix-code tree.

??? note "Proof"
    We use mathematical induction to prove this theorem.
    
    -   **Base case**: When the number of letters $n = 2$, clearly directly merging the two letters into one tree is the optimal code tree.
    -   **Inductive hypothesis**: Assume that for a number of letters $n = k$ ($k \geq 2$), the Huffman algorithm can obtain the optimal prefix-code tree.
    -   **Inductive step**: For a number of letters $n = k + 1$, we select the two letters with the smallest weights out of the $k+1$ letters and merge them into one subtree, with the subtree's root as a virtual letter (virtual node). By the lemma, this operation does not break the optimality of the prefix-code tree. At this point, the virtual letter together with the remaining letters forms $k$ letters, and by the inductive hypothesis, when the number of letters is $k$, the Huffman algorithm can obtain the optimal prefix-code tree.
    
    Therefore, by mathematical induction, the Huffman algorithm can obtain the optimal prefix-code tree for any number of letters $n$. Q.E.D.

## Huffman coding

In program design, one usually marks each character with a separate code to represent a group of characters, i.e. **encoding**.

When performing binary encoding, if all codes are assumed to be of equal length, then representing $n$ different characters requires $\left \lceil \log_2 n \right \rceil$ bits, which is called **fixed-length encoding**.

If the **usage frequency of each character is equal**, then fixed-length encoding is undoubtedly the most space-efficient encoding method; but if characters appear with different frequencies, one can let high-frequency characters use as short a code as possible and low-frequency characters use as long a code as possible, constructing a kind of **variable-length encoding** to obtain better space efficiency.

When designing variable-length encoding, one must consider the uniqueness of decoding; if no code in a group of codes is a prefix of any other code, then this group of codes is called a **prefix code**, which guarantees the uniqueness of decoding.

A Huffman tree can be used to construct the **shortest prefix code**, i.e. the **Huffman code**; its construction steps are as follows:

1.  Let the character set to be encoded be $d_1,d_2,\dots,d_n$, and their frequencies of appearance in the string be $w_1,w_2,\dots,w_n$.
2.  Take $d_1,d_2,\dots,d_n$ as leaf nodes and $w_1,w_2,\dots,w_n$ as the weights of the leaf nodes, and construct a Huffman tree.
3.  Stipulate that the left branch of the Huffman code tree represents $0$ and the right branch represents $1$; then the $0$/$1$ sequence formed by the path from the root to each leaf node is the code of the character corresponding to that leaf node.

![](./images/huffman-tree-3.svg)

## Sample code

??? note "Building a Huffman tree"
    ```cpp
    struct HNode {
      int weight;
      HNode *lchild, *rchild;
    };
    
    using Htree = HNode *;
    
    Htree createHuffmanTree(int arr[], int n) {
      Htree forest[N];
      Htree root = NULL;
      for (int i = 0; i < n; i++) {  // store all points into the forest
        Htree temp;
        temp = (Htree)malloc(sizeof(HNode));
        temp->weight = arr[i];
        temp->lchild = temp->rchild = NULL;
        forest[i] = temp;
      }
    
      for (int i = 1; i < n; i++) {  // n-1 iterations to build the Huffman tree
        int minn = -1, minnSub;  // minn is the index of the smallest tree root, minnSub is the index of the second-smallest tree root
        for (int j = 0; j < n; j++) {
          if (forest[j] != NULL && minn == -1) {
            minn = j;
            continue;
          }
          if (forest[j] != NULL) {
            minnSub = j;
            break;
          }
        }
    
        for (int j = minnSub; j < n; j++) {  // assign values based on minn and minnSub
          if (forest[j] != NULL) {
            if (forest[j]->weight < forest[minn]->weight) {
              minnSub = minn;
              minn = j;
            } else if (forest[j]->weight < forest[minnSub]->weight) {
              minnSub = j;
            }
          }
        }
    
        // build the new tree
        root = (Htree)malloc(sizeof(HNode));
        root->weight = forest[minn]->weight + forest[minnSub]->weight;
        root->lchild = forest[minn];
        root->rchild = forest[minnSub];
    
        forest[minn] = root;     // assign the pointer to the new tree to the minn position
        forest[minnSub] = NULL;  // set the minnSub position to empty
      }
      return root;
    }
    ```

??? note "Computing the WPL of a constructed Huffman tree"
    ```cpp
    struct HNode {
      int weight;
      HNode *lchild, *rchild;
    };
    
    using Htree = HNode *;
    
    int getWPL(Htree root, int len) {  // recursive implementation; for an already-built Huffman tree, find the WPL
      if (root == NULL)
        return 0;
      else {
        if (root->lchild == NULL && root->rchild == NULL)  // leaf node
          return root->weight * len;
        else {
          int left = getWPL(root->lchild, len + 1);
          int right = getWPL(root->rchild, len + 1);
          return left + right;
        }
      }
    }
    ```

??? note "For an unbuilt Huffman tree, directly find its WPL"
    ```cpp
    int getWPL(int arr[], int n) {  // for an unbuilt Huffman tree, directly find its WPL
      priority_queue<int, vector<int>, greater<int>> huffman;  // min-heap
      for (int i = 0; i < n; i++) huffman.push(arr[i]);
    
      int res = 0;
      for (int i = 0; i < n - 1; i++) {
        int x = huffman.top();
        huffman.pop();
        int y = huffman.top();
        huffman.pop();
        int temp = x + y;
        res += temp;
        huffman.push(temp);
      }
      return res;
    }
    ```

??? note "For a given sequence, compute the Huffman code"
    ```cpp
    struct HNode {
      int weight;
      HNode *lchild, *rchild;
    };
    
    using Htree = HNode *;
    
    void huffmanCoding(Htree root, int len, int arr[]) {  // compute the Huffman code
      if (root != NULL) {
        if (root->lchild == NULL && root->rchild == NULL) {
          printf("The code of the character with node %d is: ", root->weight);
          for (int i = 0; i < len; i++) printf("%d", arr[i]);
          printf("\n");
        } else {
          arr[len] = 0;
          huffmanCoding(root->lchild, len + 1, arr);
          arr[len] = 1;
          huffmanCoding(root->rchild, len + 1, arr);
        }
      }
    }
    ```
