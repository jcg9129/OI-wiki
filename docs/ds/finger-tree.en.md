author: isdanni

???+ warning "Note"
    This chapter is optional reading; before reading, please make sure you have some understanding of functional programming.

## Introduction

The **finger tree** is a **purely functional** data structure proposed by Ralf Hinze and Ross Paterson.

## Why finger trees are needed

In functional programming, the list is a very common data type. For sequence-based operations—including adding and removing elements at both ends (double-ended-queue operations), inserting, concatenating, and deleting at any node, finding an element satisfying a requirement, and splitting a sequence into subsequences—almost all functional languages provide support. But for efficient support of more operations, these languages struggle. Even where there are corresponding implementations, they are usually very complex and hard to use in practice.

The finger tree provides a purely functional sequence data structure that can perform operations such as access and adding to the front and back of the sequence in amortized constant time, and concatenation and random access in logarithmic time. Besides good asymptotic running-time bounds, finger trees are also very flexible: when combined with a [monoidal tag](https://en.wikipedia.org/wiki/Monoidal_category) on the elements, finger trees can be used to implement efficient random-access sequences, ordered sequences, interval trees, and priority queues.

## Basic structure

A finger tree stores data at the tree's "fingers" (leaves), with amortized constant access time. A finger is a point that can access part of the data structure. In an imperative language, this is called a pointer. In a finger tree, a "finger" is a structure pointing to the end of the sequence or a leaf node. A finger tree also stores in each internal node the result of applying some associative operation to its descendants. The data stored in internal nodes can be used to provide functionality beyond that of tree-class data structures.

1.  The depth of a finger tree is computed from bottom to top.
2.  The first level of the finger tree, i.e. the leaf nodes of the tree, contains only values, with depth $0$. The second level has depth $1$. The third level has depth $2$, and so on.
3.  The closer to the root, the deeper the subtree of the original tree (the tree before it was a finger tree) that the node points to. This way, working down the tree goes from the leaves to the root of the tree, which is opposite to a typical tree data structure. To obtain this kind of structure, we must ensure the original tree has a uniform depth. When declaring a node object, it must be parameterized by the type of the child nodes. The nodes on the spine at depth $1$ and above point to trees; through this parameterization, they can be represented by nested nodes.

### Turning a tree into a finger tree

???+ note "Note"
    A **2-3 tree** is a tree data structure in which each node with children (an internal node) has two children (a $2$-node) and one data element, or three children (a $3$-node) and two data elements. A 2-3 tree is a B-tree of order $3$. The nodes outside the tree (leaf nodes) have no children and one or two data elements.

We will begin this process with a balanced 2-3 tree. For a finger tree to work properly, all leaf nodes need to be at the same level. As shown in the figure below (image taken from the finger-tree paper):

![](./images/finger-tree-1.png)

A finger is "a structure that can efficiently access the nodes of the tree near a particular location." To make a finger tree, we need to put fingers at the left and right ends of the tree, take the leftmost and rightmost internal nodes of the tree and pull them up, letting the rest of the tree hang between them; this gives us amortized constant access time to the ends of the sequence.

![](./images/finger-tree-2.png)

This new data structure is called a finger tree. A finger tree consists of several layers (the blue boxes below) distributed along its spine (the brown line):

![](./images/finger-tree-3.png)

```haskell
data FingerTree a = Empty
                  | Single a
                  | Deep (Digit a) (FingerTree (Node a)) (Digit a)

data Digit a = One a | Two a a | Three a a a | Four a a a a
data Node a = Node2 a a | Node3 a a a
```

The numbers in the example are nodes with letters. Each list is partitioned by the prefix or suffix of each node on the spine. In the converted 2-3 tree, the top-level digit list seems to be able to have length two or three, while the lower levels have length only one or two. To make certain applications of finger trees run so efficiently, a finger tree allows $1$ to $4$ subtrees at each level. A finger tree's digit can be converted into a list, such as:

```haskell
type Digit a = One a | Two a a | Three a a a | Four a a a a
```

The top level has elements of type $a$, and the next level has elements of type Node $a$; because of the nodes between the spine and the leaves, this generally means that the $n$-th level of the tree has elements of type $Node^{n}$ $a$, or 2-3 trees of depth $n$. This means a sequence of $n$ elements is represented by a tree of depth $\Theta(\log n)$. An element at distance $d$ from the nearest end is stored at depth $\Theta(\log d)$ in the tree.

### Deque operations

Finger trees can also make efficient deques. Whether or not the structure is persistent, all operations take $\Theta(1)$ time. It can be seen as an extension of the implicit deque[^okasaki1999purely]:

1.  Replacing pairs with 2-3 nodes provides enough flexibility to support efficient concatenation. (To keep constant-time deque operations, Digit must be extended to four.)
2.  Annotating internal nodes with a monoid allows efficient splitting.

```haskell
data ImplicitDeque a = Empty
                     | Single a
                     | Deep (Digit a) (ImplicitDeque (a, a)) (Digit a)

data Digit a = One a | Two a a | Three a a a
```

## Time complexity

Finger trees provide amortized constant-time access to the tree's "fingers" (leaves), where the data is stored, and logarithmic-time concatenation and splitting in the size of the smaller part. They also store in each internal node the result of applying some associative operation to its descendants. The "summary" data stored in internal nodes can be used to provide functionality of data structures beyond trees.

| Operation                            | Finger tree                    | Annotated 2-3 tree | List             | Vector |
| ----------------------------- | ---------------------- | ----------------------------- | -------------------- | ---------- |
| `const`,`snoc`                | $O(1)$                 | $O(\log n)$                   | $O(1)$/$O(n)$        | $O(n)$     |
| `viewl`,`viewr`               | $O(1)$                 | $O(\log n)$                   | $O(1)$/$O(n)$        | $O(1)$     |
| `measure`/`length`            | $O(1)$                 | $O(1)$                        | $O(n)$               | $O(1)$     |
| `append`                      | $O(\log \min(l1, l2))$ | $O(\log n)$                   | $O(n)$               | $O(m+n)$   |
| `split`                       | $O(\log \min(n, l-n))$ | $O(\log n)$                   | $O(n)$               | $O(1)$     |
| `replicate`                   | $O(\log n)$            | $O(\log n)$                   | $O(n)$               | $O(n)$     |
| `fromList`,`toList`,`reverse` | $O(l)$/$O(l)$/$O(l)$   | $O(l)$                        | $O(1)$/$O(1)$/$O(n)$ | $O(n)$     |
| `index`                       | $O(\log \min(n, l-n))$ | $O(\log n)$                   | $O(n)$               | $O(1)$     |

## Applications

Finger trees can be used to build other trees. For example, a priority queue can be implemented by tagging internal nodes with the minimum priority among their children in the tree, or an indexed list/array can be implemented by tagging nodes with the count of leaves among their children. Other applications include random-access sequences (described below), ordered sequences, and interval trees.

Finger trees can provide average $O(1)$ push, reverse, and pop, and $O(\log n)$ append and split; and can be adapted to indexed or sorted sequences. Like all functional data structures, it is inherently persistent; that is, old versions of the tree are always retained.

For code implementations, the implementation of the finite sequence `Seq` in the Haskell core library uses 2-3 finger trees ([Data.Sequence](https://hackage.haskell.org/package/containers-0.6.5.1/docs/Data-Sequence.html)), and the [implementation](https://ocaml-batteries-team.github.io/batteries-included/hdoc2/BatFingerTree.html) of the `BatFingerTree` module in OCaml also uses a generic finger-tree data structure. Finger trees can be implemented with or without lazy evaluation, but laziness allows a simpler implementation.

## References and further reading

1.  Ralf Hinze and Ross Paterson, "[Finger trees: a simple general-purpose data structure](http://www.staff.city.ac.uk/~ross/papers/FingerTree.html)", Journal of Functional Programming 16:2 (2006) pp 197-217.
2.  [Finger Tree - Wikipedia](https://en.wikipedia.org/wiki/Finger_tree)

[^okasaki1999purely]: [Purely Functional Data Structures](https://www.cambridge.org/us/academic/subjects/computer-science/programming-languages-and-applied-logic/purely-functional-data-structures), Chris Okasaki (1999)
