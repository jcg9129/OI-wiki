author: Xarfa

## Introduction

A partition tree (dividing tree) is a data structure for solving the interval $K$-th largest problem; its constant factor and difficulty of understanding are both much lower than a chairman tree (persistent segment tree). At the same time, the partition tree sticks closely to "the $K$-th largest", so it is a sorting-based data structure.

Prerequisite: [chairman tree](persistent-seg.md#chairman-tree)

## Process

### Building the tree

Building a partition tree is relatively simple, but relatively complex compared with other trees.

![](./images/dividing-1.svg)

As in the figure, each level has a seemingly unordered array. In fact, every number marked in red is **to be assigned to the left child**. And what is the assignment rule? It is comparing with **the median of this level**: if less than or equal to the median, assign to the left, otherwise assign to the right. But note here: it is not strictly **less than or equal goes left, otherwise goes right**. Because the median may have duplicates, and it has a certain relationship with the parity of $N$. The code below shows a clever use; you can refer to the code.

We cannot sort each level every time; doing so would not pass even in theoretical complexity, let alone the constant factor. We think: to find the median, one sort is enough. Why? For example, when we find the median of $l,r$, it is actually `num[mid]` after sorting.

Two key arrays:

tree\[log(N),N]: the tree, which must store all the values, with space complexity $O(n\log n)$.
toleft\[log(N),n]: the number of the first $i$ elements of each level that go into the left child; this needs a bit of understanding—it is a prefix sum.

???+ note "Implementation"
    ```pascal
    procedure Build(left,right,deep:longint); // left,right are the left and right endpoints of the interval, deep is which level
    var
      i,mid,same,ls,rs,flag:longint; // flag is used to balance the counts of the two sides
    begin
      if left=right then exit; // reached the bottom level
      mid:=(left+right) >> 1;
      same:=mid-left+1;
      for i:=left to right do 
        if tree[deep,i]<num[mid] then
          dec(same);
      
      ls:=left; // the first pointer assigned to the left child
      rs:=mid+1; // the first pointer assigned to the right child
      for i:=left to right do
      begin
        flag:=0;
        if (tree[deep,i]<num[mid])or((tree[deep,i]=num[mid])and(same>0)) then // condition for assigning to the left
        begin
          flag:=1; tree[deep+1,ls]:=tree[deep,i]; inc(ls);
          if tree[deep,i]=num[mid] then // balance the left and right counts
            dec(same);
        end
        else
        begin
          tree[deep+1,rs]:=tree[deep,i]; inc(rs);
        end;
        toleft[deep,i]:=toleft[deep,i-1]+flag;
      end;
      Build(left,mid,deep+1); // continue
      Build(mid+1,right,deep+1);
    end;
    ```

### Query

Let's first bring up the chairman-tree content. When using a chairman tree to find the interval $K$-th smallest, we use $K$ as the basis: to go left we go left, and to go right we subtract the left value; the partition tree is the same.

The hard-to-understand part of the query is the **interval shrinking**. In the figure below, the query is $3$ to $7$, so the next level only needs to query $2$ to $3$. Of course, we define $[\text{left},\text{right}]$ as the shrunken interval (target interval), and $[l,r]$ is still the interval of the current node. So why mark the target interval? Because it is **the basis for deciding whether the answer is on the left or right**.

![](./images/dividing-2.svg)

???+ note "Implementation"
    ```pascal
    function Query(left,right,k,l,r,deep:longint):longint;
    var
      mid,x,y,cnt,rx,ry:longint;
    begin
      if left=right then // writing it as l=r is also fine, because the target interval must also have the answer
        exit(tree[deep,left]);
      mid:=(l+r) >> 1;
      x:=toleft[deep,left-1]-toleft[deep,l-1]; // the number from l to left going to the left child
      y:=toleft[deep,right]-toleft[deep,l-1]; // the number from l to right going to the left child
      ry:=right-l-y; rx:=left-l-x; // ry is the number from l to right going to the right child, rx is the number from l to left going to the right child
      cnt:=y-x; // the number from left to right going to the left child
      if cnt>=k then // basic chairman-tree knowledge
        Query:=Query(l+x,l+y-1,k,l,mid,deep+1) // l+x shrinks the left boundary, l+y-1 shrinks the right interval. For the figure above, this abandons nodes 1 and 2.
      else
        Query:=Query(mid+rx+1,mid+ry+1,k-cnt,mid+1,r,deep+1); // likewise shrinking the interval, only to the right. Note to subtract cnt from k.
    end;
    ```

## Properties

Time complexity: a single query only needs $O(\log n)$, and $m$ queries is $O(m\log n)$.

Space complexity: only $O(n\log n)$ numbers need to be stored.

Personally tested results: chairman tree: $1482 \text{ms}$, partition tree: $889 \text{ms}$. (Non-recursive, with a relatively small constant factor.)

## Applications of the partition tree

Example: [Luogu P3157 \[CQOI2011\] Dynamic Inversions](https://www.luogu.com.cn/problem/P3157)

> Problem summary: given a permutation of $n$ elements ($n\leq 10^5$), there are m queries ($m\leq 5\times 10^4$); each deletes a number from the permutation and asks the number of inversions in the permutation after deleting this number.

This problem can be solved with CDQ in $\Theta(n\log^2n)$ time and $\Theta(n)$ space, and CDQ's constant factor is also excellent.

If this problem were changed to forced-online, it would generally be solved with the Fenwick-tree + chairman-tree tree-of-trees solution, with time complexity $\Theta(n\log^2n)$ and space complexity $\Theta(n\log^2n)$, with a slightly larger constant factor, which can also pass this problem.

Using a partition tree, we can solve this problem online in $\Theta(n\log^2n)$ time and $\Theta(n\log n)$ space, with a much smaller constant factor than the tree-of-trees solution. (Roughly comparable to CDQ.)

???+ warning "Note"
    For convenience of programming, this article divides the large array into two small arrays according to the middle value of the positions, i.e. the partition tree below is equivalent to the merge-sort process rather than the quicksort process. The top-level large array is a sorted array, and the bottom level is the original array.

For each node in the partition tree, we call it a right node if and only if it will be assigned to the right child at the next level, i.e. those numbers whose positions are relatively later in the original array; similarly we can define a left node. If, during the tree building, the top level is arranged in sorted order, similar to computing inversions with merge sort, we find that the number of inversions of an array is the sum, over each left node, of the number of right nodes before it.

Now consider the deletion operation. Deleting a left node reduces the whole array's inversions by the number of right nodes before it, and deleting a right node reduces it by the number of left nodes after it. So we can consider dynamically maintaining "the number of right nodes before each left node" and "the number of left nodes after each right node". This can be simply maintained with a Fenwick tree.

Note that when maintaining with a Fenwick tree, we can only compute the contribution within the same block of the partition tree, and cannot jump out of the block. For a Fenwick tree, there is a rather clever handling method.

Consider that the index range of each block on the partition tree must be of the form $[c\times 2^k+1,(c+1)\times 2^k]$, listed as follows (since the code does not involve handling the bottom level of the partition tree, we only enumerate down to the second-to-last level):

    [0001 0010] [0011 0100] [0101 0110] [0111 1000] [1001 1010] [1011 1100] [1101 1110] [1111 10000]  lev=1
    [0001 0010 0011 0100]   [0101 0110 0111 1000]   [1001 1010 1011 1100]   [1101 1110 1111 10000]    lev=2
    [0001 0010 0011 0100 0101 0110 0111 1000]       [1001 1010 1011 1100 1101 1110 1111 10000]        lev=3
    [0001 0010 0011 0100 0101 0110 0111 1000 1001 1010 1011 1100 1101 1110 1111 10000]                lev=4

Recall the principle of a Fenwick tree: when jumping up, we each time do `x += lowbit(x)`. If during the upward jump we can guarantee not to jump out of the block, then we can guarantee that only the values of elements within the block are affected. Upward queries are similar.

And to guarantee not jumping out of the block during the upward jump, we only need to ensure that $lowbit(x)<2^{lev}$ holds during the jump.

Jumping down is a completely different handling method. If each block's indices are represented in 0-index, they are of the form $[c\times 2^k,(c+1)\times 2^k)$. Then, we only need to right-shift a given index's value by k to obtain which block it is in. During the downward jump, always check whether it jumps out of the block.

Note that a Fenwick tree implemented by this method accesses a maximum index equal to the integer power of 2 closest to n, so the array index cannot be allocated as n.

Since modifications are needed at $\log n$ levels, and the time complexity of modifying at level $k$ is $\Theta(k)$, the final time complexity is $\Theta(n\log n+m\log^2n)$.

Attached code:

```cpp
--8<-- "docs/ds/code/dividing/dividing_1.cpp"
```

## Afterword

Reference blog post: [portal](https://blog.csdn.net/littlewhite520/article/details/70250722).
