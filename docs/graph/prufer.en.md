???+ note "Note"
    This article is translated from [e-maxx Prüfer Code](https://github.com/e-maxx-eng/e-maxx-eng/blob/master/src/graph/pruefer_code.md). Also, to explain: in the original text the nodes are labeled starting from $0$, and this article follows the habit of most people and changes them to labeling from $1$.

This article introduces the Prüfer sequence (Prüfer code), a method of representing a labeled tree with a unique integer sequence.

Using the Prüfer sequence we can prove [Cayley's formula](#cayleys-formula). And we will also explain how to compute the number of ways to add edges in a graph to make the graph connected.

**Note**: We do not consider trees with $1$ node.

## Prüfer sequence

### Introduction

The Prüfer sequence can represent a labeled tree with $n$ nodes using $n-2$ integers in $[1,n]$. You can also understand it as a bijection between the spanning trees of the complete graph and integer sequences. It is commonly used in combinatorial counting problems.

Heinz Prüfer invented this sequence in 1918 to prove [Cayley's formula](#cayleys-formula).

### Building the Prüfer sequence for a tree

The Prüfer sequence is built as follows: each time, select a leaf node with the smallest number and delete it, then record in the sequence the node to which it is connected. After repeating $n-2$ times, only two nodes remain, and the algorithm ends.

Obviously, using a heap can achieve $O(n\log n)$ complexity.

???+ note "Implementation"
    === "C++"
        ```cpp
        // code taken from the original text, nodes are labeled from 0
        vector<vector<int>> adj;
        
        vector<int> pruefer_code() {
          int n = adj.size();
          set<int> leafs;
          vector<int> degree(n);
          vector<bool> killed(n);
          for (int i = 0; i < n; i++) {
            degree[i] = adj[i].size();
            if (degree[i] == 1) leafs.insert(i);
          }
        
          vector<int> code(n - 2);
          for (int i = 0; i < n - 2; i++) {
            int leaf = *leafs.begin();
            leafs.erase(leafs.begin());
            killed[leaf] = true;
            int v;
            for (int u : adj[leaf])
              if (!killed[u]) v = u;
            code[i] = v;
            if (--degree[v] == 1) leafs.insert(v);
          }
          return code;
        }
        ```
    
    === "Python"
        ```python
        # nodes are labeled from 0
        adj = [[]]
        
        
        def pruefer_code():
            n = len(adj)
            leafs = set()
            degree = [0] * n
            killed = [False] * n
            for i in range(1, n):
                degree[i] = len(adj[i])
                if degree[i] == 1:
                    leafs.intersection(i)
            code = [0] * (n - 2)
            for i in range(1, n - 2):
                leaf = leafs[0]
                leafs.pop()
                killed[leaf] = True
                for u in adj[leaf]:
                    if killed[u] == False:
                        v = u
                code[i] = v
                if degree[v] == 1:
                    degree[v] = degree[v] - 1
                    leafs.intersection(v)
            return code
        ```

For example, this is the Prüfer sequence construction process of a tree with 7 nodes:

![Prüfer](./images/prufer1.png)

The final sequence is $2,2,3,3,2$.

Of course, there is also a linear construction algorithm.

### Linear construction algorithm for the Prüfer sequence

The essence of the linear construction is to maintain a pointer pointing to the node we are about to delete. First, we find that the number of leaf nodes is non-strictly monotonically decreasing; deleting one leaf node, the total number of leaf nodes either stays the same or decreases by 1.

So we consider the following process: maintain a pointer $p$. Initially, $p$ points to the leaf node with the smallest number. At the same time, we maintain the degree of each node, which conveniently lets us know whether a new leaf node is produced when deleting a node. The operations are as follows:

1.  Delete the node pointed to by $p$, and check whether a new leaf node is produced.
2.  If a new leaf node is produced, assume its number is $x$; we compare the size relationship between $p,x$. If $x>p$, then no other operation is done; otherwise, immediately delete $x$, then check whether a new leaf node is produced after deleting $x$, and repeat step $2$ until no new node is produced or the number of the new node is $>p$.
3.  Increment the pointer $p$ until encountering a not-yet-deleted leaf node;

#### Correctness

Looping the above operations $n-2$ times completes the construction of the sequence. Next, consider the correctness of the algorithm.

$p$ is the current leaf node with the smallest number; if no leaf node is produced after deleting $p$, we can only go find the next leaf node; if a leaf node $x$ is produced:

-   If $x>p$, then $p$ scanning backward will scan to it anyway, so no operation is done;
-   If $x<p$, because $p$ was originally the one with the smallest number, and $x$ is even smaller than $p$, so $x$ is the current leaf node with the smallest number, and is deleted with priority. Delete $x$ and continue this consideration until there is no smaller leaf node.

Analyzing the algorithm complexity, we find that each edge is visited at most once (when reducing the degree), and the pointer traverses each node at most once, so the complexity is $O(n)$.

#### Implementation

=== "C++"
    ```cpp
    // code taken from the original text, likewise starting from 0
    vector<vector<int>> adj;
    vector<int> parent;
    
    void dfs(int v) {
      for (int u : adj[v]) {
        if (u != parent[v]) parent[u] = v, dfs(u);
      }
    }
    
    vector<int> pruefer_code() {
      int n = adj.size();
      parent.resize(n), parent[n - 1] = -1;
      dfs(n - 1);
    
      int ptr = -1;
      vector<int> degree(n);
      for (int i = 0; i < n; i++) {
        degree[i] = adj[i].size();
        if (degree[i] == 1 && ptr == -1) ptr = i;
      }
    
      vector<int> code(n - 2);
      int leaf = ptr;
      for (int i = 0; i < n - 2; i++) {
        int next = parent[leaf];
        code[i] = next;
        if (--degree[next] == 1 && next < ptr) {
          leaf = next;
        } else {
          ptr++;
          while (degree[ptr] != 1) ptr++;
          leaf = ptr;
        }
      }
      return code;
    }
    ```

=== "Python"
    ```python
    # likewise starting from 0
    adj = [[]]
    parent = [0] * n
    
    
    def dfs(v):
        for u in adj[v]:
            if u != parent[v]:
                parent[u] = v
                dfs(u)
    
    
    def pruefer_code():
        n = len(adj)
        parent[n - 1] = -1
        dfs(n - 1)
    
        ptr = -1
        degree = [0] * n
        for i in range(0, n):
            degree[i] = len(adj[i])
            if degree[i] == 1 and ptr == -1:
                ptr = i
    
        code = [0] * (n - 2)
        leaf = ptr
        for i in range(0, n - 2):
            next = parent[leaf]
            code[i] = next
            if degree[next] == 1 and next < ptr:
                degree[next] = degree[next] - 1
                leaf = next
            else:
                ptr = ptr + 1
                while degree[ptr] != 1:
                    ptr = ptr + 1
                leaf = ptr
        return code
    ```

### Properties of the Prüfer sequence

1.  After constructing the Prüfer sequence, two nodes remain in the original tree, one of which must be the point $n$ with the largest number.
2.  The number of times each node appears in the sequence is its degree minus $1$. (Those that do not appear are leaf nodes.)

### Rebuilding the tree from the Prüfer sequence

The method of rebuilding the tree is similar. According to the properties of the Prüfer sequence, we can obtain the degree of each point in the original tree. Then we can also obtain the leaf node with the smallest number, and this node must be connected to the point corresponding to the first number of the Prüfer sequence. Then we simultaneously reduce the degrees of these two nodes by one.

By now you may already know what to do. Each time we select a node with degree $1$ and the smallest number, connect it to the point of the Prüfer sequence currently enumerated, then simultaneously reduce the degrees of the two points. In the end we are left with two points of degree $1$, one of which is node $n$. Connect them. Using a heap to maintain this process, if we find during the process of decreasing node degrees that a degree drops to $1$, we add this node to the heap; the complexity of doing this is $O(n\log n)$.

???+ note "Implementation"
    ```cpp
    // code taken from the original text
    vector<pair<int, int>> pruefer_decode(vector<int> const& code) {
      int n = code.size() + 2;
      vector<int> degree(n, 1);
      for (int i : code) degree[i]++;
    
      set<int> leaves;
      for (int i = 0; i < n; i++)
        if (degree[i] == 1) leaves.insert(i);
    
      vector<pair<int, int>> edges;
      for (int v : code) {
        int leaf = *leaves.begin();
        leaves.erase(leaves.begin());
    
        edges.emplace_back(leaf, v);
        if (--degree[v] == 1) leaves.insert(v);
      }
      edges.emplace_back(*leaves.begin(), n - 1);
      return edges;
    }
    ```

### Rebuilding the tree in linear time

Same as the method of linearly constructing the Prüfer sequence. When reducing the degree, a new leaf node is produced, so we judge the size relationship between this leaf node and the pointer $p$; if it is smaller, we consider it with priority.

#### Implementation

```cpp
// code taken from the original text
vector<pair<int, int>> pruefer_decode(vector<int> const& code) {
  int n = code.size() + 2;
  vector<int> degree(n, 1);
  for (int i : code) degree[i]++;

  int ptr = 0;
  while (degree[ptr] != 1) ptr++;
  int leaf = ptr;

  vector<pair<int, int>> edges;
  for (int v : code) {
    edges.emplace_back(leaf, v);
    if (--degree[v] == 1 && v < ptr) {
      leaf = v;
    } else {
      ptr++;
      while (degree[ptr] != 1) ptr++;
      leaf = ptr;
    }
  }
  edges.emplace_back(leaf, n - 1);
  return edges;
}
```

Through these processes, we can actually understand that the Prüfer sequence establishes a bijective relationship with labeled unrooted trees.

## Cayley's formula

The complete graph $K_n$ has $n^{n-2}$ spanning trees.

How to prove this? There are many methods, but proving it with the Prüfer sequence is very simple. Any integer sequence of length $n-2$ with value range $[1,n]$ corresponds bijectively via the Prüfer sequence to a spanning tree, so the number of schemes is $n^{n-2}$.

## Number of ways to make a graph connected

The Prüfer sequence may be even more powerful than you think. It can create a more general formula than [Cayley's formula](#cayleys-formula). For example, the following problem:

> A labeled undirected graph with $n$ points and $m$ edges has $k$ connected blocks. We wish to add $k-1$ edges to make the whole graph connected. Find the number of schemes.

### Proof

Let $s_i$ denote the number of points in the $i$-th connected block. We consider constructing a Prüfer sequence for the $k$ connected blocks. Since there are many methods of connection between two connected blocks, this is not an ordinary Prüfer sequence. So we may assume $d_i$ is the degree of the $i$-th connected block. Since the sum of degrees is twice the number of edges, so $\sum_{i=1}^kd_i=2k-2$. Then, for a given $d$ sequence, the number of ways to construct the Prüfer sequence is

$$
\binom{k-2}{d_1-1,d_2-1,\cdots,d_k-1}=\frac{(k-2)!}{(d_1-1)!(d_2-1)!\cdots(d_k-1)!}
$$

For the $i$-th connected block, it has ${s_i}^{d_i}$ ways of connection, so for a given $d$ sequence the number of ways to make the graph connected is

$$
\binom{k-2}{d_1-1,d_2-1,\cdots,d_k-1}\cdot \prod_{i=1}^k{s_i}^{d_i}
$$

Now we want to enumerate the $d$ sequence, and the expression becomes

$$
\sum_{d_i\ge 1，\sum_{i=1}^kd_i=2k-2}\binom{k-2}{d_1-1,d_2-1,\cdots,d_k-1}\cdot \prod_{i=1}^k{s_i}^{d_i}
$$

OK, this is a very unpleasant expression. But do not panic! We have the multinomial theorem:

$$
(x_1 + \dots + x_m)^p = \sum_{\substack{c_i \ge 0 ,\  \sum_{i=1}^m c_i = p}} \binom{p}{c_1, c_2, \cdots ,c_m}\cdot \prod_{i=1}^m{x_i}^{c_i}
$$

Then we do a change of variables on the original expression, letting $e_i=d_i-1$; obviously $\sum_{i=1}^ke_i=k-2$, so the original expression becomes

$$
\sum_{e_i\ge 0，\sum_{i=1}^ke_i=k-2}\binom{k-2}{e_1,e_2,\cdots,e_k}\cdot \prod_{i=1}^k{s_i}^{e_i+1}
$$

Simplifying, we get

$$
(s_1+s_2+\cdots+s_k)^{k-2}\cdot \prod_{i=1}^ks_i
$$

that is

$$
n^{k-2}\cdot\prod_{i=1}^ks_i
$$

as the answer.

## Exercises

-   [Luogu P6086 [Template] Prüfer sequence](https://www.luogu.com.cn/problem/P6086) (template problem)
-   [Luogu P11039 [MX-X3-T6] 「RiOI-4」TECHNOPOLIS 2085](https://www.luogu.com.cn/problem/P11039)
-   [UVa #10843 - Anne's game](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=20&page=show_problem&problem=1784)
-   [Timus #1069 - Prufer Code](http://acm.timus.ru/problem.aspx?space=1&num=1069)
-   [Codeforces - Clues](http://codeforces.com/contest/156/problem/D)
-   [Topcoder - TheCitiesAndRoadsDivTwo](https://archive.topcoder.com/ProblemStatement/pm/10774)
