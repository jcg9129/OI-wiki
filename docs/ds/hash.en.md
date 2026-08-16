## Introduction

![](images/hashtable.svg)

A hash table (also called a scatter table) is a data structure that stores data in the form of "key-value". Storing data in "key-value" form means that any key uniquely corresponds to some position in memory. You only need to input the key to look up, and you can quickly find its corresponding value. You can understand a hash table as an advanced kind of array whose indices can be very large integers, floating-point numbers, strings, or even structs.

## Hash functions

To make a key correspond to a position in memory, we must compute an index for the key, i.e. compute where this data should be placed. This function that computes an index from a key is called a hash function. For example, if the key is a person's ID number, the hash function could be the last four digits of the number, or of course the first four digits. The commonly used "phone-number tail digits" in daily life is also a kind of hash function. In practical applications, the key may be something more complex, such as a floating-point number, string, struct, etc., in which case one must design a suitable hash function according to the specific situation. A hash function should be easy to compute and should make the computed indices as uniformly distributed as possible.

Once we can compute an index for a key, we know where each key's corresponding value should be placed. Suppose we use array a to store the data and the hash function is f; then the key-value pair `(key, value)` should be placed at `a[f(key)]`. No matter what type the key is or how large its range is, `f(key)` is an integer within an acceptable range and can serve as an array index.

In OI, the most common case should be when the key is an integer. When the range of the key is relatively small, one can directly use the key as the array index; but when the range of the key is relatively large, for example when using integers within the range of $10^9$ as keys, a hash table is needed. Generally, the key modulo a large prime is taken as the index, i.e. $f(x)=x \bmod M$ is taken as the hash function.

Another relatively common case is when the key is a string. Since strings are not supported as array indices, and converting a string into a number for storage can also avoid performing string comparisons multiple times, in OI one generally does not directly use a string as the key, but first computes the hash value of the string and then inserts its hash value as the key into the hash table. Regarding the hash value of a string, we generally use the base idea, imagining the string as a base-$127$ number. Then, for each string $s$ of length $n$:

$x = s_0 \cdot 127^0 + s_1 \cdot 127^1 + s_2 \cdot 127^2 + \dots + s_n \cdot 127^n$

We can take the obtained $x$ modulo $2^{64}$ (i.e. the maximum value of `unsigned long long`). This way the natural overflow of `unsigned long long` is equivalent to the modulo operation, which makes the operation more convenient.

Although this method is simple, it is not perfect. One can construct data to make this method collide (i.e. two strings' $x$ modulo $2^{64}$ give the same result).  
We can use the double-hashing method: choose two large primes $a,b$. We consider the two strings equal if and only if their hash values modulo both $a$ and $b$ are equal. This can greatly reduce the probability of a hash collision.

## Collisions

If for any key the indices computed by the hash function are all different, then we only need to place `(key, value)` at the corresponding position according to the index. But in practice, it often happens that two different keys have the same index computed by the hash function. Then some method is needed to handle collisions. In OI, the most commonly used method is chaining.

### Chaining

Chaining is also called open hashing.

Chaining opens a linked list at each place that stores data; if multiple keys index to the same place, we just put them all into the linked list at that position. When querying, we need to scan the entire linked list at the corresponding position and, for each piece of data in it, compare whether its key is consistent with the query key. If the range of indices is $1\ldots M$ and the size of the hash table is $N$, then a single insertion/query needs an expected $O(\frac{N}{M})$ comparisons.

#### Implementation

=== "C++"
    ```cpp
    constexpr int SIZE = 1000000;
    constexpr int M = 999997;
    
    struct HashTable {
      struct Node {
        int next, value, key;
      } data[SIZE];
    
      int head[M], size;
    
      int f(int key) { return (key % M + M) % M; }
    
      int get(int key) {
        for (int p = head[f(key)]; p; p = data[p].next)
          if (data[p].key == key) return data[p].value;
        return -1;
      }
    
      int modify(int key, int value) {
        for (int p = head[f(key)]; p; p = data[p].next)
          if (data[p].key == key) return data[p].value = value;
      }
    
      int add(int key, int value) {
        if (get(key) != -1) return -1;
        data[++size] = Node{head[f(key)], value, key};
        head[f(key)] = size;
        return value;
      }
    };
    ```

=== "Python"
    ```python
    M = 999997
    SIZE = 1000000
    
    
    class Node:
        def __init__(self, next=None, value=None, key=None):
            self.next = next
            self.value = value
            self.key = key
    
    
    data = [Node() for _ in range(SIZE)]
    head = [0] * M
    size = 0
    
    
    def f(key):
        return key % M
    
    
    def get(key):
        p = head[f(key)]
        while p:
            if data[p].key == key:
                return data[p].value
            p = data[p].next
        return -1
    
    
    def modify(key, value):
        p = head[f(key)]
        while p:
            if data[p].key == key:
                data[p].value = value
                return data[p].value
            p = data[p].next
    
    
    def add(key, value):
        if get(key) != -1:
            return -1
        size = size + 1
        data[size] = Node(head[f(key)], value, key)
        head[f(key)] = size
        return value
    ```

Here we also provide an encapsulated template that can be used like a map and is relatively short:

```cpp
struct hash_map {  // hash table template

  struct data {
    long long u;
    int v, nex;
  };  // forward-star structure

  data e[SZ << 1];  // SZ is a const int denoting the size
  int h[SZ], cnt;

  int hash(long long u) { return (u % SZ + SZ) % SZ; }

  // the reason for using (u % SZ + SZ) % SZ rather than u % SZ here is that
  // the % operation in C++ cannot turn a negative number into a positive one

  int& operator[](long long u) {
    int hu = hash(u);  // get the head pointer
    for (int i = h[hu]; i; i = e[i].nex)
      if (e[i].u == u) return e[i].v;
    return e[++cnt] = data{u, -1, h[hu]}, h[hu] = cnt, e[cnt].v;
  }

  hash_map() {
    cnt = 0;
    memset(h, 0, sizeof(h));
  }
};
```

Here, the hash function is designed for the type of the key and returns a linked-list head pointer for querying. In this template we wrote a hash table with key-value type `(long long, int)`, returning -1 when querying a nonexistent key. The function `hash_map()` is used to initialize at definition time.

### Closed hashing

The closed-hashing method stores all records directly in the hash table; if a collision occurs, it continues probing according to some method.

For example, linear probing: if a collision occurs at `d`, then check `d + 1`, `d + 2`…… in turn.

#### Implementation

```cpp
constexpr int N = 360007;  // N is the maximum number of elements that can be stored

class Hash {
 private:
  int keys[N];
  int values[N];

 public:
  Hash() { memset(values, 0, sizeof(values)); }

  int& operator[](int n) {
    // return a reference to the corresponding Hash[Key]
    // modify it to a nonzero value; a value of 0 is regarded as empty
    int idx = (n % N + N) % N, cnt = 1;
    while (keys[idx] != n && values[idx] != 0) {
      idx = (idx + cnt * cnt) % N;
      cnt += 1;
    }
    keys[idx] = n;
    return values[idx];
  }
};
```

## Example

[「JLOI2011」Distinct Numbers](https://www.luogu.com.cn/problem/P4305)
