The Skip List is a search data structure invented by William Pugh, supporting fast search, insertion, and deletion of data.

The expected space complexity of the skip list is $O(n)$, and the expected time complexity of the skip list's query, insertion, and deletion operations is all $O(\log n)$.

## Basic idea

As the name implies, the skip list is a data structure similar to a linked list. More precisely, the skip list is an improvement on the sorted linked list.

For convenience of discussion, all subsequent sorted linked lists are by default sorted in **ascending** order.

The search operation of a sorted linked list is to compare one by one starting from the head, until the value of the current node is greater than or equal to the value of the target node. Obviously, the complexity of this operation is $O(n)$.

On the basis of the sorted linked list, the skip list introduces the concept of **layering**. First, each layer of the skip list is a sorted linked list; in particular, the bottommost layer is the initial sorted linked list. Each node located in layer $i$ has probability $p$ of appearing in layer $i+1$, where $p$ is a constant.

Denote the layer in an $n$-node skip list that is expected to contain $\frac{1}{p}$ elements as layer $L(n)$; it is easy to obtain $L(n) = \log_{\frac{1}{p}}n$.

Searching in the skip list means starting from layer $L(n)$, comparing horizontally one by one until the next node of the current node is greater than or equal to the target node, then moving to the next layer. Repeat this process until reaching the first layer and being unable to continue the operation. At this point, if the next node is the target node, the search is successful; conversely, the element does not exist. In this way, some unnecessary comparisons are skipped during the search, so compared with the query of a sorted linked list, the query of the skip list is faster. It can be proved that the average complexity of a skip list query is $O(\log n)$.

## Complexity proof

### Space complexity

For a node, the probability that the node's highest layer number is $i$ is $p^{i-1}(1 - p)$. So, the expected number of layers of the skip list is $\sum_{i\ge 1} ip^{i - 1}(1-p) = \frac{1}{1 - p}$, and because $p$ is a constant, the **expected space complexity** of the skip list is $O(n)$.

In the worst case, each layer's sorted linked list equals the initial sorted linked list, i.e. the **worst-case space complexity** of the skip list is $O(n \log n)$.

### Time complexity

Analyzing the search path from back to front, this process can be divided into two parts: climbing from the bottommost layer to layer $L(n)$, and the subsequent operations. In the analysis, assume that the specific information of a node is unknown before it is accessed.

Suppose we are currently at a node $x$ in layer $i$; we do not know the maximum layer number of $x$ and the maximum layer number of the node to the left of $x$, only that the maximum layer number of $x$ is at least $i$. If the maximum layer number of $x$ is greater than $i$, then the next step should be to go up, the probability of this case being $p$; if the maximum layer number of $x$ equals $i$, then the next step should be to go left, the probability of this case being $1-p$.

Let $C(i)$ be the expected cost of climbing up $i$ layers in an infinitely long skip list; then we have:

$$
\begin{aligned}
C(0) & = 0 \\
C(i) & = (1-p)(1+C(i)) + p(1+C(i-1))
\end{aligned}
$$

Solving gives $C(i)=\frac{i}{p}$.

From this we can conclude: in a skip list of length $n$, the expected number of steps to climb from the bottommost layer to layer $L(n)$ has an upper bound $\frac{L(n) - 1}{p}$.

Now we only need to analyze how many more steps are needed after climbing to layer $L(n)$. It is easy to obtain that after reaching layer $L(n)$, the number of steps going left does not exceed the total number of nodes in layer $L(n)$ and higher layers, and the expectation of this total is $\frac{1}{p}$. So after reaching layer $L(n)$, the expected number of steps going left has an upper bound $\frac{1}{p}$. Similarly, after reaching layer $L(n)$, the expected number of steps going up has an upper bound $\frac{1}{p}$.

So, the expected number of search steps of a skip list query is $\frac{L(n) - 1}{p} + \frac{2}{p}$, and because $L(n)=\log_{\frac{1}{p}}n$, the **expected time complexity** of a skip list query is $O(\log n)$.

In the worst case, each layer's sorted linked list equals the initial sorted linked list, and the search process is equivalent to querying the sorted linked list of the highest layer, i.e. the **worst-case time complexity** of the skip list query operation is $O(n)$.

The insertion operation and the deletion operation are just performing a query process, recording the nodes that need to be modified along the way, and finally completing the modification. It is easy to obtain that each layer needs to modify at most one node, and because the expected number of layers of the skip list is $\log_{\frac{1}{p}}n$, the **expected time complexity** of insertion and modification is also $O(\log n)$.

## Specific implementation

### Getting the maximum layer number of a node

Simulate adding one more layer up with probability $p$, and finally take the minimum with the upper-limit value.

```cpp
int randomLevel() {
  int lv = 1;
  // MAXL = 32, S = 0xFFFF, PS = S * P, P = 1 / 4
  while ((rand() & S) < PS) ++lv;
  return min(MAXL, lv);
}
```

### Query

Query whether a node with key `key` exists in the skip list. In the specific implementation, one can set two sentinel nodes to reduce the discussion of boundary conditions.

```cpp
V& find(const K& key) {
  SkipListNode<K, V>* p = head;

  // find the last node in this layer whose key is less than key, then go to the next layer
  for (int i = level; i >= 0; --i) {
    while (p->forward[i]->key < key) {
      p = p->forward[i];
    }
  }
  // now it is less-than, so we need to go one more step forward
  p = p->forward[0];

  // successfully found the node
  if (p->key == key) return p->value;

  // node does not exist, return INVALID
  return tail->value;
}
```

### Insertion

Insert the node `(key, value)`. The process of inserting a node is to first perform a query process, recording along the way which nodes the new node is to be inserted after, and finally perform the insertion. The last node in each layer whose key is less than `key` is the node that needs to be modified.

```cpp
void insert(const K &key, const V &value) {
  // used to record the nodes that need to be modified
  SkipListNode<K, V> *update[MAXL + 1];

  SkipListNode<K, V> *p = head;
  for (int i = level; i >= 0; --i) {
    while (p->forward[i]->key < key) {
      p = p->forward[i];
    }
    // the node that needs to be modified in layer i is p
    update[i] = p;
  }
  p = p->forward[0];

  // if it already exists then modify
  if (p->key == key) {
    p->value = value;
    return;
  }

  // get the maximum layer number of the new node
  int lv = randomLevel();
  if (lv > level) {
    lv = ++level;
    update[lv] = head;
  }

  // create a new node
  SkipListNode<K, V> *newNode = new SkipListNode<K, V>(key, value, lv);
  // insert the new node in layers 0~lv
  for (int i = lv; i >= 0; --i) {
    p = update[i];
    newNode->forward[i] = p->forward[i];
    p->forward[i] = newNode;
  }

  ++length;
}
```

### Deletion

Delete the node with key `key`. The process of deleting a node is to first perform a query process, recording along the way which nodes the node to delete is after, and finally perform the deletion. The last node in each layer whose key is less than `key` is the node that needs to be modified.

```cpp
bool erase(const K &key) {
  // used to record the nodes that need to be modified
  SkipListNode<K, V> *update[MAXL + 1];

  SkipListNode<K, V> *p = head;
  for (int i = level; i >= 0; --i) {
    while (p->forward[i]->key < key) {
      p = p->forward[i];
    }
    // the node that needs to be modified in layer i is p
    update[i] = p;
  }
  p = p->forward[0];

  // node does not exist
  if (p->key != key) return false;

  // start deleting from the bottommost layer
  for (int i = 0; i <= level; ++i) {
    // if this layer does not have p, the deletion is done
    if (update[i]->forward[i] != p) {
      break;
    }
    // disconnect p's link
    update[i]->forward[i] = p->forward[i];
  }

  // reclaim space
  delete p;

  // deleting a node may cause the maximum layer number to decrease
  while (level > 0 && head->forward[level] == tail) --level;

  // skip list length
  --length;
  return true;
}
```

### Full code

The following code is a map implemented with a skip list. It has not been seriously tested; for reference only.

??? note "Reference code"
    ```cpp
    #include <cassert>
    #include <climits>
    #include <ctime>
    #include <iostream>
    #include <map>
    using namespace std;
    
    template <typename K, typename V>
    struct SkipListNode {
      int level;
      K key;
      V value;
      SkipListNode **forward;
    
      SkipListNode() {}
    
      SkipListNode(K k, V v, int l, SkipListNode *nxt = NULL) {
        key = k;
        value = v;
        level = l;
        forward = new SkipListNode *[l + 1];
        for (int i = 0; i <= l; ++i) forward[i] = nxt;
      }
    
      ~SkipListNode() {
        if (forward != NULL) delete[] forward;
      }
    };
    
    template <typename K, typename V>
    struct SkipList {
      static constexpr int MAXL = 32;
      static constexpr int P = 4;
      static constexpr int S = 0xFFFF;
      static constexpr int PS = S / P;
      static constexpr int INVALID = INT_MAX;
    
      SkipListNode<K, V> *head, *tail;
      int length;
      int level;
    
      SkipList() {
        srand(time(nullptr));
    
        level = length = 0;
        tail = new SkipListNode<K, V>(INVALID, 0, 0);
        head = new SkipListNode<K, V>(INVALID, 0, MAXL, tail);
      }
    
      ~SkipList() {
        delete head;
        delete tail;
      }
    
      int randomLevel() {
        int lv = 1;
        while ((rand() & S) < PS) ++lv;
        return MAXL > lv ? lv : MAXL;
      }
    
      void insert(const K &key, const V &value) {
        SkipListNode<K, V> *update[MAXL + 1];
    
        SkipListNode<K, V> *p = head;
        for (int i = level; i >= 0; --i) {
          while (p->forward[i]->key < key) {
            p = p->forward[i];
          }
          update[i] = p;
        }
        p = p->forward[0];
    
        if (p->key == key) {
          p->value = value;
          return;
        }
    
        int lv = randomLevel();
        if (lv > level) {
          lv = ++level;
          update[lv] = head;
        }
    
        SkipListNode<K, V> *newNode = new SkipListNode<K, V>(key, value, lv);
        for (int i = lv; i >= 0; --i) {
          p = update[i];
          newNode->forward[i] = p->forward[i];
          p->forward[i] = newNode;
        }
    
        ++length;
      }
    
      bool erase(const K &key) {
        SkipListNode<K, V> *update[MAXL + 1];
        SkipListNode<K, V> *p = head;
    
        for (int i = level; i >= 0; --i) {
          while (p->forward[i]->key < key) {
            p = p->forward[i];
          }
          update[i] = p;
        }
        p = p->forward[0];
    
        if (p->key != key) return false;
    
        for (int i = 0; i <= level; ++i) {
          if (update[i]->forward[i] != p) {
            break;
          }
          update[i]->forward[i] = p->forward[i];
        }
    
        delete p;
    
        while (level > 0 && head->forward[level] == tail) --level;
        --length;
        return true;
      }
    
      V &operator[](const K &key) {
        V v = find(key);
        if (v == tail->value) insert(key, 0);
        return find(key);
      }
    
      V &find(const K &key) {
        SkipListNode<K, V> *p = head;
        for (int i = level; i >= 0; --i) {
          while (p->forward[i]->key < key) {
            p = p->forward[i];
          }
        }
        p = p->forward[0];
        if (p->key == key) return p->value;
        return tail->value;
      }
    
      bool count(const K &key) { return find(key) != tail->value; }
    };
    
    int main() {
      SkipList<int, int> L;
      map<int, int> M;
    
      clock_t s = clock();
    
      for (int i = 0; i < 1e5; ++i) {
        int key = rand(), value = rand();
        L[key] = value;
        M[key] = value;
      }
    
      for (int i = 0; i < 1e5; ++i) {
        int key = rand();
        if (i & 1) {
          L.erase(key);
          M.erase(key);
        } else {
          int r1 = L.count(key) ? L[key] : 0;
          int r2 = M.count(key) ? M[key] : 0;
          assert(r1 == r2);
        }
      }
    
      clock_t e = clock();
      cout << "Time elapsed: " << (double)(e - s) / CLOCKS_PER_SEC << endl;
      // about 0.2s
    
      return 0;
    }
    ```

## Random-access optimization of the skip list

Accessing the $k$-th node in the skip list is equivalent to accessing the $k$-th node in the initial sorted linked list; obviously the time complexity of this operation is $O(n)$, which is not good enough.

The random-access optimization of the skip list is to additionally maintain, for each forward pointer, the length of this forward pointer. Suppose $A$ and $B$ are both nodes in the skip list, where $A$ is the $a$-th node of the skip list and $B$ is the $b$-th node of the skip list $(a < b)$, and in a certain layer of the skip list $A$'s forward pointer points to $B$; then the length of this forward pointer is $b - a$.

Now to access the $k$-th node in the skip list, one can start from the top layer, traverse this layer's linked list horizontally, until the current node's position plus the length of the current node's forward pointer in this layer is greater than or equal to $k$, then move to the next layer. Repeat this process until reaching the first layer and being unable to continue the operation. At this point, the current node is the $k$-th node in the skip list.

In this way, one can quickly access the $k$-th element of the skip list. It can be proved that the time complexity of this operation is $O(\log n)$.

## References

1.  [Skip Lists: A Probabilistic Alternative to Balanced Trees](https://15721.courses.cs.cmu.edu/spring2018/papers/08-oltpindexes1/pugh-skiplists-cacm1990.pdf)
2.  [Skip List](https://en.wikipedia.org/wiki/Skip_list)
3.  [A Skip List Cookbook](http://cglab.ca/~morin/teaching/5408/refs/p90b.pdf)
