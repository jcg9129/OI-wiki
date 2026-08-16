author: fudonglai, AngelKitty, labuladong

This page introduces the difference between recursion and divide-and-conquer algorithms and how to combine them.

## Recursion

### Definition

Recursion, in mathematics and computer science, refers to the method of using a function itself within the definition of that function; in computer science it additionally refers to a method of solving a problem by repeatedly decomposing it into subproblems of the same kind.

### Introduction

> To understand recursion, you must first understand recursion.

The basic idea of recursion is that a function calls itself directly or indirectly, so that solving the original problem is transformed into solving many subproblems with the same nature but a smaller size. When solving, you only need to focus on how to divide the original problem into qualifying subproblems, without paying too much attention to how each subproblem is solved.

Here are some examples that help in understanding recursion:

1.  [What is recursion?](./divide-and-conquer.md)
2.  How do you sort a pile of numbers? Answer: split them in half, sort the left half first and then the right half, and finally merge them. As for how to sort the left and right halves, please reread this sentence.
3.  How old are you this year? Answer: last year's age plus one year; I was born in 1999.
4.  ![An example for understanding recursion](images/divide-and-conquer-1.png)

Recursion is very common in mathematics. For example, set theory's formal definition of the natural numbers is: 1 is a natural number, and every natural number has a successor, which is also a natural number.

The two most important features of recursive code: a termination condition and a self-call. The self-call is solving a subproblem, while the termination condition defines the answer to the simplest subproblem.

```cpp
int func(input value) {
  if (termination condition) return solution to the smallest subproblem;
  return func(reduced size);
}
```

### Why write recursion

1.  Clear structure and strong readability. For example, implementing [merge sort](./merge-sort.md) in two different ways:

    === "C++"
        ```cpp
        // Merge sort algorithm without recursion
        template <typename T>
        void merge_sort(vector<T> a) {
          int n = a.size();
          for (int seg = 1; seg < n; seg = seg + seg)
            for (int start = 0; start < n - seg; start += seg + seg)
              merge(a, start, start + seg - 1, std::min(start + seg + seg - 1, n - 1));
        }
        
        // Merge sort algorithm using recursion
        template <typename T>
        void merge_sort(vector<T> a, int front, int end) {
          if (front >= end) return;
          int mid = front + (end - front) / 2;
          merge_sort(a, front, mid);
          merge_sort(a, mid + 1, end);
          merge(a, front, mid, end);
        }
        ```

    === "Python"
        ```python
        # Merge sort algorithm without recursion
        def merge_sort(a):
            n = len(a)
            seg, start = 1, 0
            while seg < n:
                while start < n - seg:
                    merge(a, start, start + seg - 1, min(start + seg + seg - 1, n - 1))
                    start = start + seg + seg
                seg = seg + seg
        
        
        # Merge sort algorithm using recursion
        def merge_sort(a, front, end):
            if front >= end:
                return
            mid = front + (end - front) / 2
            merge_sort(a, front, mid)
            merge_sort(a, mid + 1, end)
            merge(a, front, mid, end)
        ```

    Clearly, the recursive version is easier to understand than the non-recursive one. The recursive version's approach is obvious at a glance: sort the left half, sort the right half, and finally merge the two halves. The non-recursive version, on the other hand, looks baffling, full of hard-to-understand boundary-computation details, especially prone to bugs and hard to debug.

2.  Practice analyzing the structure of a problem. When you find that a problem can be decomposed into smaller problems of the same structure, after writing enough recursion you will keenly notice this feature and thereby solve problems efficiently.

### Disadvantages of recursion

During program execution, recursion is implemented using the stack. Each time a function call is entered, the stack grows by one stack frame, and each time a function returns, the stack shrinks by one stack frame. The stack is not infinitely large, so when the recursion depth is too great, the consequence is a **stack overflow**.

Recursion is sometimes clearly efficient, as with merge sort; **sometimes it is inefficient**, such as counting the hairs on the Monkey King's body, because the stack consumes extra space, whereas a simple iteration consumes none. For instance, in this example, given the head of a linked list, compute its length:

```cpp
// Typical iterative-traversal framework
int size(Node *head) {
  int size = 0;
  for (Node *p = head; p != nullptr; p = p->next) size++;
  return size;
}

// I just want to write recursion; recursion is number one under heaven
int size_recursion(Node *head) {
  if (head == nullptr) return 0;
  return size_recursion(head->next) + 1;
}
```

![\[A comparison of the two, with compiler set to Clang 10.0 and optimization set to O1\](https://quick-bench.com/q/rZ7jWPmSdltparOO5ndLgmS9BVc)](images/divide-and-conquer-2.png "\[A comparison of the two, with compiler set to Clang 10.0 and optimization set to O1](https://quick-bench.com/q/rZ7jWPmSdltparOO5ndLgmS9BVc)")

### Optimizing recursion

Main pages: [Search optimization](../search/opt.md) and [Memoized search](../dp/memo.md)

A fairly basic recursive implementation may recurse too many times and easily time out. In that case the recursion needs to be optimized. [^ref1]

## Divide and conquer

### Definition

Divide and conquer, literally "divide and rule", means dividing a complex problem into two or more identical or similar subproblems, until at last the subproblems can be solved simply and directly, and the solution to the original problem is the merger of the solutions to the subproblems.

### Process

The core idea of a divide-and-conquer algorithm is "divide and conquer".

The rough flow can be divided into three steps: divide -> solve -> merge.

1.  Decompose the original problem into subproblems of the same structure.
2.  After decomposing down to some easily solvable boundary, solve recursively.
3.  Merge the solutions of the subproblems into the solution of the original problem.

Problems that divide and conquer can solve generally have the following features:

-   The problem can be solved easily once its size is reduced to a certain degree.
-   The problem can be decomposed into several smaller problems of the same kind, i.e. the problem has the optimal-substructure property, and the solutions of the subproblems it is decomposed into can be merged into the solution of the problem.
-   The subproblems into which the problem is decomposed are mutually independent, i.e. the subproblems do not contain common subproblems.

???+ warning "Note"
    If the subproblems are not independent, then divide and conquer repeatedly solves the common subproblems, doing a lot of unnecessary work. In this case, although divide and conquer can still be used, it is generally better to use [dynamic programming](../dp/basic.md).

Take merge sort as an example. Suppose the function implementing merge sort is named `merge_sort`. Make its responsibility clear, namely **to sort the array passed to it**. This problem can obviously be decomposed. Sorting an array is equivalent to sorting the left and right halves of the array separately, then merging them into one array.

```cpp
void merge_sort(an array) {
  if (can be handled easily) return;
  merge_sort(the left half of the array);
  merge_sort(the right half of the array);
  merge(the left half of the array, the right half of the array);
}
```

If you pass it half of the array, then after processing, that half of the array is already sorted. Note that `merge_sort` is extremely similar to the postorder-traversal template of a binary tree. Because the routine of a divide-and-conquer algorithm is **divide -> solve (reaching bottom) -> merge (backtracking)**: first divide left and right, then handle the merge; backtracking is popping the stack, which is equivalent to a postorder traversal.

The implementation of the `merge` function is the same as merging two sorted linked lists.

## Key points

### Key points for writing recursion

**Understand what a function does and trust that it can accomplish the task; absolutely do not jump into the function trying to explore more details,** otherwise you will get lost in endless details and be unable to extricate yourself—how many stacks can a human brain hold?

Take traversing a binary tree as an example.

```cpp
void traverse(TreeNode* root) {
  if (root == nullptr) return;
  traverse(root->left);
  traverse(root->right);
}
```

These few lines of code are enough to traverse any binary tree. For the recursive function `traverse(root)`, as long as you trust that giving it a root node `root` lets it traverse the tree, then you only need to pass this node's left and right children to the function again.

Similarly, extend it to traversing an N-ary tree. The way it is written is exactly the same as for a binary tree. However, for an N-ary tree there is obviously no inorder traversal.

```cpp
void traverse(TreeNode* root) {
  if (root == nullptr) return;
  for (auto child : root->children) traverse(child);
}
```

## Differences

### The difference between recursion and enumeration

The difference between recursion and enumeration is: enumeration divides the problem horizontally and then solves the subproblems one after another, whereas recursion decomposes the problem level by level, a vertical split.

### The difference between recursion and divide and conquer

Recursion is a programming technique, a way of thinking about solving problems; a divide-and-conquer algorithm is largely based on recursion, an algorithmic idea for solving more specific problems.

## A detailed worked example

???+ note "[437. Path Sum III](https://leetcode-cn.com/problems/path-sum-iii/)"
    Given a binary tree, each of whose nodes stores an integer value.
    
    Find the total number of paths whose sum equals a given value.
    
    The path does not need to start at the root nor end at a leaf, but the direction of the path must be downward (only from parent node to child node).
    
    The binary tree has at most 1000 nodes, and the node values are integers in the range \[-1000000,1000000].
    
    Example:
    
    ```text
    root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
    
          10
         /  \
        5   -3
       / \    \
      3   2   11
     / \   \
    3  -2   1
    
    Return 3. The paths with sum equal to 8 are:
    
    1.  5 -> 3
    2.  5 -> 2 -> 1
    3. -3 -> 11
    ```
    
    ```cpp
    --8<-- "docs/basic/code/divide-and-conquer/divide-and-conquer_1.h"
    ```

??? note "Reference code"
    ```cpp
    --8<-- "docs/basic/code/divide-and-conquer/divide-and-conquer_1.cpp"
    ```

??? note "Problem analysis"
    The problem looks very complicated, but the code is extremely concise.
    
    First, be clear that solving a tree problem recursively necessarily traverses the entire tree, so the binary-tree traversal framework (recursively calling the function itself on the left and right subtrees separately) must appear in the main function pathSum. So what should each node do? Each node should check how many qualifying paths its own subtree contains. And with that, this problem is finished.
    
    Following the technique described earlier, and based on the analysis just now, clearly define what each recursive function should do:
    
    `PathSum` function: given a node and a target value, return the total number of paths whose sum equals the target value in the tree rooted at this node.
    
    `count` function: given a node and a target value, return how many paths in the tree rooted at this node begin at this node and have sum equal to the target value.
    
    ??? note "Reference code (with comments)"
        ```cpp
        int pathSum(TreeNode *root, int sum) {
          if (root == nullptr) return 0;
          int pathImLeading = count(root, sum);  // number of paths starting at myself
          int leftPathSum = pathSum(root->left, sum);  // total paths on the left (trust it to compute this)
          int rightPathSum =
              pathSum(root->right, sum);  // total paths on the right (trust it to compute this)
          return leftPathSum + rightPathSum + pathImLeading;
        }
        
        int count(TreeNode *node, int sum) {
          if (node == nullptr) return 0;
          // Can I be a standalone path?
          int isMe = (node->val == sum) ? 1 : 0;
          // Left side, how many sum - node.val can you make?
          int leftNode = count(node->left, sum - node->val);
          // Right side, how many sum - node.val can you make?
          int rightNode = count(node->right, sum - node->val);
          return isMe + leftNode + rightNode;  // this is how many I can make here
        }
        ```
    
    Again the same saying: **understand what each function can do, and trust that they can accomplish it.**
    
    To summarize, the `PathSum` function provides the binary-tree traversal framework, and during the traversal it calls the `count` function on each node (a preorder traversal is used here, but inorder and postorder work too). The `count` function is also a binary-tree traversal, used to find paths with the target value that begin at that node.

## Exercises

-   [Recursion practice set on LeetCode](https://leetcode.com/explore/learn/card/recursion-i/)
-   [Divide-and-conquer practice set on LeetCode](https://leetcode.com/tag/divide-and-conquer/)

## References and notes

[^ref1]: [labuladong's Algorithm Cheat Sheet - Recursion Explained](https://labuladong.gitbook.io/algo/suan-fa-si-wei-xi-lie/di-gui-xiang-jie)
