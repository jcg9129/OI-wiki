This page briefly introduces the linked list.

## Introduction

The linked list is a data structure used to store data, connecting elements through pointers like a chain. Its characteristic is that inserting and deleting data is very convenient, but its performance in finding and reading data is poor.

## Difference from arrays

Both linked lists and arrays can be used to store data. Unlike a linked list, an array stores all elements in order one by one. Different storage structures give them different advantages:

Because of its chain-like structure, a linked list can conveniently delete and insert data, with the number of operations being $O(1)$. But precisely because of this, the efficiency of finding and reading data is not as high as an array; the number of operations in randomly accessing data is $O(n)$.

An array can conveniently find and read data, with the number of operations in random access being $O(1)$. But the number of operations for deletion and insertion is $O(n)$.

## Constructing a linked list

???+ tip "Tip"
    When constructing a linked list, the part using pointers is rather abstract; it may be hard to understand from text description and code alone, so it is recommended to understand it together with diagrams.

### Singly linked list

A singly linked list contains a data field and a pointer field, where the data field is used to store data, and the pointer field is used to connect the current node and the next node.

![](images/list.svg)

???+ note "Implementation"
    === "C++"
        ```cpp
        struct Node {
          int value;
          Node *next;
        };
        ```
    
    === "Python"
        ```python
        class Node:
            def __init__(self, value=None, next=None):
                self.value = value
                self.next = next
        ```

### Doubly linked list

A doubly linked list likewise has a data field and a pointer field. The difference is that the pointer field is divided into left and right (or previous and next), used to connect the previous node, the current node, and the next node.

![](images/double-list.svg)

???+ note "Implementation"
    === "C++"
        ```cpp
        struct Node {
          int value;
          Node *left;
          Node *right;
        };
        ```
    
    === "Python"
        ```python
        class Node:
            def __init__(self, value=None, left=None, right=None):
                self.value = value
                self.left = left
                self.right = right
        ```

## Inserting (writing) data into a linked list

### Singly linked list

The process is roughly as follows:

1.  Initialize the data `node` to be inserted;
2.  Point `node`'s `next` pointer to `p`'s next node;
3.  Point `p`'s `next` pointer to `node`.

The specific process can refer to the figures below:

1.  ![](./images/list-insert-1.svg)
2.  ![](./images/list-insert-2.svg)
3.  ![](./images/list-insert-3.svg)

The code implementation is as follows:

???+ note "Implementation"
    === "C++"
        ```cpp
        void insertNode(int i, Node *p) {
          Node *node = new Node;
          node->value = i;
          node->next = p->next;
          p->next = node;
        }
        ```
    
    === "Python"
        ```python
        def insertNode(i, p):
            node = Node()
            node.value = i
            node.next = p.next
            p.next = node
        ```

### Singly circular linked list

Connecting the head and tail of a linked list turns it into a circular linked list. Since the linked list's head and tail are connected, when inserting data one needs to determine whether the original linked list is empty: if empty, it loops on itself; if not empty, insert data normally.

The rough process is as follows:

1.  Initialize the data `node` to be inserted;
2.  Determine whether the given linked list `p` is empty;
3.  If empty, point both `node`'s `next` pointer and `p` to itself;
4.  Otherwise, point `node`'s `next` pointer to `p`'s next node;
5.  Point `p`'s `next` pointer to `node`.

The specific process can refer to the figures below:

1.  ![](./images/list-insert-cyclic-1.svg)
2.  ![](./images/list-insert-cyclic-2.svg)
3.  ![](./images/list-insert-cyclic-3.svg)

The code implementation is as follows:

???+ note "Implementation"
    === "C++"
        ```cpp
        void insertNode(int i, Node *p) {
          Node *node = new Node;
          node->value = i;
          node->next = NULL;
          if (p == NULL) {
            p = node;
            node->next = node;
          } else {
            node->next = p->next;
            p->next = node;
          }
        }
        ```
    
    === "Python"
        ```python
        def insertNode(i, p):
            node = Node()
            node.value = i
            node.next = None
            if p == None:
                p = node
                node.next = node
            else:
                node.next = p.next
                p.next = node
        ```

### Doubly circular linked list

When inserting data into a doubly circular linked list, besides determining whether the given linked list is empty, one also needs to modify both the left and right pointers.

The rough process is as follows:

1.  Initialize the data `node` to be inserted;
2.  Determine whether the given linked list `p` is empty;
3.  If empty, point `node`'s `left` and `right` pointers, as well as `p`, all to itself;
4.  Otherwise, point `node`'s `left` pointer to `p`;
5.  Point `node`'s `right` pointer to `p`'s right node;
6.  Point the `left` pointer of `p`'s right node to `node`;
7.  Point `p`'s `right` pointer to `node`.

The code implementation is as follows:

???+ note "Implementation"
    === "C++"
        ```cpp
        void insertNode(int i, Node *p) {
          Node *node = new Node;
          node->value = i;
          if (p == NULL) {
            p = node;
            node->left = node;
            node->right = node;
          } else {
            node->left = p;
            node->right = p->right;
            p->right->left = node;
            p->right = node;
          }
        }
        ```
    
    === "Python"
        ```python
        def insertNode(i, p):
            node = Node()
            node.value = i
            if p == None:
                p = node
                node.left = node
                node.right = node
            else:
                node.left = p
                node.right = p.right
                p.right.left = node
                p.right = node
        ```

## Deleting data from a linked list

### Singly (circular) linked list

Let the node to be deleted be `p`; when deleting it from the linked list, just overwrite `p` with the value of `p`'s next node `p->next`, and at the same time update `p`'s next-next node.

The process is roughly as follows:

1.  Assign the value of `p`'s next node to `p`, so as to erase `p->value`;
2.  Create a new temporary node `t` to store the address of `p->next`;
3.  Point `p`'s `next` pointer to `p`'s next-next node, so as to erase `p->next`;
4.  Delete `t`. At this point, although the original node `p`'s address is still in use, what is deleted is the address of the original node `p->next`, but `p`'s data is overwritten by `p->next`, so `p` exists in name only.

The specific process can refer to the figures below:

1.  ![](./images/list-delete-1.svg)
2.  ![](./images/list-delete-2.svg)
3.  ![](./images/list-delete-3.svg)

The code implementation is as follows:

???+ note "Implementation"
    === "C++"
        ```cpp
        void deleteNode(Node *p) {
          p->value = p->next->value;
          Node *t = p->next;
          p->next = p->next->next;
          delete t;
        }
        ```
    
    === "Python"
        ```python
        def deleteNode(p):
            p.value = p.next.value
            p.next = p.next.next
        ```

### Doubly circular linked list

The process is roughly as follows:

1.  Point the right pointer of `p`'s left node to `p`'s right node;
2.  Point the left pointer of `p`'s right node to `p`'s left node;
3.  Create a new temporary node `t` to store `p`'s address;
4.  Assign the address of `p`'s right node to `p`, so as to avoid `p` becoming a dangling pointer;
5.  Delete `t`.

The code implementation is as follows:

???+ note "Implementation"
    === "C++"
        ```cpp
        void deleteNode(Node *&p) {
          p->left->right = p->right;
          p->right->left = p->left;
          Node *t = p;
          p = p->right;
          delete t;
        }
        ```
    
    === "Python"
        ```python
        def deleteNode(p):
            p.left.right = p.right
            p.right.left = p.left
            p = p.right
        ```

## Techniques

### XOR linked list

The XOR linked list is essentially still a **doubly linked list**, but it uses the bitwise-XOR value to implement the functionality of a doubly linked list using only the memory size of one pointer.

We define `lr = left ^ right` in the structure `Node`, i.e. the **bitwise-XOR value** of the addresses of the two adjacent elements. When traversing forward, XOR the previous element's address with the current node's `lr` to obtain the next element's address; when traversing backward, XOR the next element's address with the current node's `lr` to obtain the previous element's address again. In this way, one can implement the same functionality of a doubly linked list with half the memory.
