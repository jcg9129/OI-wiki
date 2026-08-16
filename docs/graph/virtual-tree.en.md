author: HeRaNO, Ir1d, konnyakuxzy, ksyx, Xeonacid, konnyakuxzy, greyqz, sshwy, y-kx-b

## Introduction

???+ note "[「SDOI2011」War of attrition](https://www.luogu.com.cn/problem/P2495)"
    In a war, the battlefield is composed of $n$ islands and $n-1$ bridges; it is guaranteed that between any two islands there is one and only one path reachable. Now, our army has scouted that the enemy's headquarters is on the island numbered $1$, and they no longer have enough energy to sustain the battle; our army's victory is in sight. It is known that $k$ other islands have abundant energy; to prevent the enemy from obtaining energy, our army's task is to blow up some bridges so that the enemy cannot reach any energy-rich island. Since different bridges have different materials and structures, blowing up different bridges has different costs; our army hopes to minimize the total cost while satisfying the goal.
    
    The reconnaissance department also found that the enemy has a mysterious machine. Even after our army cuts off all energy, they can use that machine. The effect produced by the machine will not only repair all the bridges our army blew up, but also re-randomize the resource distribution (but it can be guaranteed that resources will not be distributed to island number $1$). However, the reconnaissance department also found that this machine can only be used $m$ times, so we only need to complete each task.
    
    For all data, $2\le n\le 2.5\times 10^5,1\le m\le 5\times 10^5,\sum k_i\le 5\times 10^5,1\le k_i\le n-1$.

### Naive approach

For the problem above, it is not hard to find—if the number of points of the tree is very small, then we can directly run DP.

First we call the points selected in a certain query—**"key points"**.

Let $Dp(i)$ denote—the **minimum cost** to make $i$ not connected to any key point in its subtree.

Let $w(a,b)$ denote the weight of the edge between $a$ and $b$.

Then enumerate the son $v$ of $i$:

-   If $v$ is not a key point: $Dp(i)=Dp(i) + \min \{Dp(v),w(i,v)\}$;
-   If $v$ is a key point: $Dp(i)=Dp(i) + w(i,v)$.

Very good, this way we obtain an $O(nq)$ piece of code.

It sounds quite interesting.

### Optimized approach

It is not hard to find—actually many points are useless. Take the following figure as an example:

![vtree-1](images/vtree-tree.svg)

If the key points we select are:

![vtree-2](images/vtree-key-vertex.svg)

In the figure, only the two red points are **key points**, while all the other points are "non-key points".

For this problem, we only need to guarantee that the red points cannot reach node number $1$.

Through visual observation, we can draw the conclusion—the right subtree of node number $1$ (although there may actually be multiple subtrees, here there are only two subtrees, so it is called this for now) has no red node at all, **so there is no need to DP it**.

Observing the conditions given by the problem, the total number of red points (key points) is of the same order as $n$; that is to say, actually in one query the red points are very sparse relative to the whole tree, so it would be nice if we could make the complexity determined by the total number of red points.

Therefore we need to **condense the information, condensing a whole big tree into a small tree**.

## Virtual Tree

From this we introduce the concept of the **"virtual tree"**.

Let us first intuitively look at what a virtual tree looks like.

In the figure below, the red nodes are the key points we selected. Both red and black nodes are points in the virtual tree. The black edges are the edges in the virtual tree.

![vtree-3](images/vtree-vtree1.svg)

![vtree-4](images/vtree-vtree2.svg)

![vtree-5](images/vtree-vtree3.svg)

![vtree-6](images/vtree-vtree4.svg)

Because the LCA of any two key points also needs to save important information, we need to save their LCA, so there are not necessarily only key points in the virtual tree.

It is not hard to find that the ancestor-descendant relationship in the virtual tree does not change. (That is, there will not be the ghostly thing where originally $a$ is an ancestor of $b$ and then later $a$ becomes a descendant of $b$.)

But we cannot brute-force enumerate the LCA in $O(k^2)$, so it is not hard to think of—first sort the key points by DFS order, then after sorting, find the LCA of two adjacent key points (adjacent means the absolute value of the difference of the indices in the sorted sequence equals 1), and add it to the virtual tree.

Our urgent task is how to construct the virtual tree.

Before proposing a plan, let us first confirm a fact—in the virtual tree, as long as we guarantee that the ancestor-descendant relationship does not change, we can add nodes arbitrarily.

That is, if we are willing, we can add all the points in the original tree to the virtual tree, and it will not cause WA (although it will cause TLE).

Therefore, for convenience, we can first add node number $1$ to the virtual tree, and it will not affect the answer.

### First construction process: double sorting + LCA edge connection

Because the LCA of multiple nodes may be the same, we cannot add it to the virtual tree multiple times.

A very intuitive method is:

-   Sort the key points by DFS order;
-   Traverse once, find the LCA of any two adjacent key points, and deduplicate;
-   Then build the tree according to the ancestor-descendant relationship in the original tree.

In the specific implementation, on the **key point sequence**, enumerate **two adjacent numbers**, find the LCA of each pair, and add it to the sequence $A$.

Because of the property of the DFS order, at this time the sequence $A$ already contains **all points in the virtual tree**, but there may be duplicates.

So we sort the sequence $A$ by DFS order **from small to large and deduplicate**.

Finally, on the sequence $A$, enumerate the **two adjacent point numbers** $x,y$, find their LCA, and connect $\operatorname{LCA}(x,y),y$; the virtual tree is then constructed.

Why can connecting $\operatorname{LCA}(x,y)$ and $y$ achieve no duplication and no omission?

??? note "Proof"
    If $x$ is an ancestor of $y$, then connect an edge directly from $x$ to $y$. Because the DFS order guarantees that the DFS orders of $x$ and $y$ are adjacent, there is no key point on the path from $x$ to $y$.
    
    If $x$ is not an ancestor of $y$, then treat $\operatorname{LCA}(x,y)$ as an ancestor of $y$; according to the previous case, we can also prove that there is no key point on the path from $\operatorname{LCA}(x,y)$ to point $y$.
    
    So connecting $\operatorname{LCA}(x,y)$ and $y$ will not omit and will not duplicate.
    
    In addition, will there be any effect if the first point is not connected by a node? Because the first point must be the root of this tree, there will be no effect, so the total number of edges is $m-1$.

Because at least two real points are needed to summon a virtual point, plus a root node, the number of points of the virtual tree is twice the number of real points.

The time complexity is $O(m\log n)$, where $m$ is the number of key points and $n$ is the total number of points.

#### Implementation

```cpp
int dfn[MAXN];
int h[MAXN], m, a[MAXN], len;  // store the key points

bool cmp(int x, int y) {
  return dfn[x] < dfn[y];  // sort by dfs order
}

void build_virtual_tree() {
  sort(h + 1, h + m + 1, cmp);  // sort the key points by dfs order
  for (int i = 1; i < m; ++i) {
    a[++len] = h[i];
    a[++len] = lca(h[i], h[i + 1]);  // insert the lca
  }
  a[++len] = h[m];
  sort(a + 1, a + len + 1, cmp);  // sort all points on the virtual tree by dfs order
  len = unique(a + 1, a + len + 1) - a - 1;  // deduplicate
  for (int i = 1, lc; i < len; ++i) {
    lc = lca(a[i], a[i + 1]);
    conn(lc, a[i + 1]);  // connect an edge; if there is an edge weight it is distance(lc,a[i+1])
  }
}
```

Actually this is already enough to construct a virtual tree.

### Second construction process: using a monotonic stack

How to construct a virtual tree using a monotonic stack?

First we need to be clear about one purpose—we want to use a monotonic stack to maintain a chain on the virtual tree.

That is, two adjacent nodes in a stack are also adjacent on the virtual tree, and the stack is monotonically increasing from the bottom to the stack top (referring to the DFS order of the nodes in the stack being monotonically increasing); to put it bluntly, the parent of a certain node is the node below it in the stack.

First we add node $1$ to the stack.

Then next add the key nodes in DFS order from small to large.

If the LCA of the current node and the stack-top node is exactly the stack-top node, then it means they are on the same chain. So just push the current node directly onto the stack.

![vtree-7](./images/vtree-add1.svg)

If the LCA of the current node and the stack-top node is not the stack-top node:

![vtree-8](./images/vtree-add2.svg)

At this time, the chain maintained by the current monotonic stack is:

![vtree-9](./images/vtree-add3.svg)

And we need to change the chain into:

![vtree-10](./images/vtree-add4.svg)

Then we just pop the nodes marked with dashed lines from the stack; before popping, do not forget to connect an edge to its parent in the virtual tree.

![vtree-11](./images/vtree-add5.svg)

If after popping we find that the stack top is not the LCA, we should push the LCA onto the stack.

Then just push the current node onto the stack.

Below we give a specific example. Suppose we want to build a virtual tree for nodes 4, 6 and 7 of the following tree:

![vtree-12](./images/vtree-construction1.svg)

Then the steps are as follows:

-   Sort the 3 key points $6,4,7$ by DFS order, obtaining the sequence $[4,6,7]$.
-   Push $1$ onto the stack.

![vtree-13](./images/vtree-construction2.svg)

We use red points to represent points in the stack, and cyan points to represent points popped from the stack.

-   Take the first in the sequence as the current node, i.e. $4$. Then take the stack-top element, which is $1$. Find the LCA of $1$ and $4$: $LCA(1,4)=1$.
-   We find $LCA(1,4)=$ the stack-top element, indicating they are on a chain of the virtual tree, so just push the current node $4$ directly onto the stack; the current stack is $4,1$.

![vtree-14](./images/vtree-construction3.svg)

-   Take the second in the sequence as the current node, which is $6$. Then take the stack-top element, which is $4$. Find the LCA of $6$ and $4$: $LCA(6,4)=1$.
-   We find $LCA(6,4)\neq$ the stack-top element, entering the judgment phase.
-   Judgment phase: we find that the DFS order of the stack-top node $4$ is greater than $LCA(6,4)$, but the DFS order of the second-largest node (the node below the stack-top node) $1$ equals the LCA (actually, equal DFS orders mean the nodes are also equal), indicating that the LCA has already been pushed onto the stack, so directly connect the edge $1\to4$, i.e. the edge from the LCA to the stack-top element. And pop $4$ from the stack.

![vtree-15](./images/vtree-construction4.svg)

-   Having finished the judgment phase, push $6$ onto the stack; the current stack is $6,1$.

![vtree-16](./images/vtree-construction5.svg)

-   Take the third in the sequence as the current node, which is $7$. Then take the stack-top element, which is $6$. Find the LCA of $7$ and $6$: $LCA(7,6)=3$.
-   We find $LCA(7,6)\neq$ the stack-top element, entering the judgment phase.
-   Judgment phase: we find that the DFS order of the stack-top node $6$ is greater than $LCA(7,6)$, but the DFS order of the second-largest node (the node below the stack-top node) $1$ is less than the LCA, indicating that the LCA has not yet been pushed onto the stack, so directly connect the edge $3\to6$, i.e. the edge from the LCA to the stack-top element. Pop $6$ from the stack, and push $LCA(6,7)$ onto the stack.
-   Having finished the judgment phase, push $7$ onto the stack; the current stack is $1,3,7$.

![vtree-17](./images/vtree-construction6.svg)

-   We find that all 3 nodes in the sequence have already been pushed onto the stack, and exit the loop.
-   At this time there are still 3 nodes in the stack: $1,3,7$; obviously they are on a chain, so directly connect: the edges $1\to3$ and $3\to7$.
-   The virtual tree is then built!

![vtree-18](./images/vtree-construction7.svg)

We next delete those points that were never pushed onto the stack (the non-cyan points); the corresponding virtual tree looks like this:

![vtree-19](./images/vtree-construction8.svg)

There are many details in this, for example if we store the virtual tree using the adjacency list way of storing the graph, we need to clear the adjacency list. But directly clearing the entire adjacency list is very slow, so we just **clear the adjacency list corresponding to an element when an element that has never been pushed onto the stack is pushed onto the stack**.

The time complexity is likewise $O(m\log n)$ (because of the sorting), where $m$ is the number of key points and $n$ is the total number of points.

#### Implementation

The C++ code for building the virtual tree looks roughly like this:

???+ note "Code implementation"
    ```cpp
    bool cmp(const int x, const int y) { return id[x] < id[y]; }
    
    void build() {
      sort(h + 1, h + k + 1, cmp);
      sta[top = 1] = 1, g.sz = 0, g.head[1] = -1;
      // push node 1 onto the stack, clear the adjacency list corresponding to node 1, set the number of adjacency-list edges to 0
      for (int i = 1, l; i <= k; ++i)
        if (h[i] != 1) {
          // if node 1 is a key node, do not add it repeatedly
          l = lca(h[i], sta[top]);
          // compute the LCA of the current node and the stack-top node
          if (l != sta[top]) {
            // if the LCA and the stack-top element are different, it means the current node is not on the chain stored by the current stack
            while (id[l] < id[sta[top - 1]])
              // when the Dfs order of the second-largest node is greater than the Dfs order of the LCA
              g.push(sta[top - 1], sta[top]), top--;
            // connect and pop the chain that does not overlap with the chain where the current node is located
            if (id[l] > id[sta[top - 1]])
              // if the LCA is not equal to the second-largest node (the greater-than here is actually no different from not-equal)
              g.head[l] = -1, g.push(l, sta[top]), sta[top] = l;
            // it means the LCA is pushed onto the stack for the first time; clear its adjacency list, connect an edge and pop the stack-top element, and push the LCA
            // onto the stack
            else
              g.push(l, sta[top--]);
            // it means the LCA is exactly the second-largest node; directly pop the stack-top element
          }
          g.head[h[i]] = -1, sta[++top] = h[i];
          // the current node must be pushed onto the stack for the first time; clear the adjacency list and push it onto the stack
        }
      for (int i = 1; i < top; ++i)
        g.push(sta[i], sta[i + 1]);  // connect the last remaining chain
      return;
    }
    ```

So we have learned how to build a virtual tree!

For the war-of-attrition problem, just directly run on the virtual tree the DP explained at the very beginning; we have effectively used the virtual tree to exclude those useless non-key nodes! Still consider all sons $v$ of $i$:

-   If $v$ is not a key point: $Dp(i)=Dp(i) + \min \{Dp(v),w(i,v)\}$
-   If $v$ is a key point: $Dp(i)=Dp(i) + w(i,v)$

So this problem passes very easily.

## Recommended exercises

-   [「SDOI2011」War of attrition](https://www.luogu.com.cn/problem/P2495)
-   [「HEOI2014」Big project](https://www.luogu.com.cn/problem/P4103)
-   [CF613D Kingdom and its Cities](http://codeforces.com/contest/613/problem/D/)
-   [「HNOI2014」World tree](https://www.luogu.com.cn/problem/P3233)
