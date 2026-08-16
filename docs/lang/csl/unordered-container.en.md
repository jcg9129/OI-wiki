## Overview

Since the C++11 standard, four unordered associative containers implemented based on [hashing](../../ds/hash.md) have been formally incorporated into the C++ standard template library, namely: `unordered_set`, `unordered_multiset`, `unordered_map`, `unordered_multimap`.

??? note "Usage when the compiler does not support C++11"
    Before C++11, unordered associative containers belonged to the TR1 extension of C++. So, if the compiler does not support C++11, when using them we need to add the `tr1/` prefix to the header file name and use the `std::tr1` namespace. For example, `#include <unordered_map>` needs to be changed to `#include <tr1/unordered_map>`; `std::unordered_map` needs to be changed to `std::tr1::unordered_map` (if using `using namespace std;`, then `tr1::unordered_map`).

They have many things in common with the corresponding associative containers in terms of functionality, functions, etc., while the biggest difference is reflected in that ordinary associative containers are generally implemented with a red-black tree, and internal elements are sorted in a specific order; while these unordered associative containers store elements using hashing, and internal elements are not sorted in any specific order, so when accessing elements in an unordered associative container, the access order also has no guarantee.

The characteristic of using hashing storage makes most operations of unordered associative containers (including search, insertion, deletion) **in the average case** able to be completed in constant time complexity, which is more excellent than the logarithmic-in-container-size time complexity of associative containers.

??? warning "Warning"
    In the worst case, the time complexity of operations such as insertion, deletion, and search on an unordered associative container will be **linear in the container size**! This situation often arises when a large number of hash collisions occur in the container.
    
    At the same time, since operations on unordered associative containers usually have a relatively large constant factor, their efficiency is sometimes not much better than ordinary associative containers.
    
    Therefore, unordered associative containers should be used with caution, and abuse should be avoided as much as possible (for example, being too lazy to discretize and directly using `unordered_map<int, int>` as an ordinary array with unlimited space).

Since unordered associative containers have many things in common with the corresponding associative containers in usage and operations, here we no longer introduce the various operations of unordered associative containers; readers can refer to [associative containers](./associative-container.md) for this content.

## Creating hash collisions

As mentioned above, in the worst case, the time complexity of some operations on an unordered associative container will be linear in the container size.

When the hash function is determined, data can be constructed to make a large number of hash collisions occur in the container, causing the complexity to reach the upper bound.

In the standard library implementation, the hash value of each element is obtained by taking the value modulo a prime, more specifically, a prime in [this list](https://github.com/gcc-mirror/gcc/blob/releases/gcc-8.1.0/libstdc%2B%2B-v3/src/shared/hashtable-aux.cc) (for g++ 6 and earlier compilers, this prime is generally $126271$; for g++ 7 and later compilers, this prime is generally $107897$).

Therefore, we can achieve the purpose of creating a large number of hash collisions by inserting multiples of these moduli into the container.

## Custom hash functions

Using a custom hash function can effectively avoid the large number of hash collisions produced by constructed data.

To use a custom hash function, we need to define a struct and overload the `()` operator in the struct, like this:

```cpp
struct my_hash {
  size_t operator()(int x) const { return x; }
};
```

Of course, to ensure that the hash function will not be quickly cracked (for example, on Codeforces, submissions using unordered associative containers are hacked), we can try to add some randomization functions (such as time) in the hash function to increase the difficulty of cracking.

For example, [this blog](https://codeforces.com/blog/entry/62393) gives the following hash function:

```cpp
struct my_hash {
  static uint64_t splitmix64(uint64_t x) {
    x += 0x9e3779b97f4a7c15;
    x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9;
    x = (x ^ (x >> 27)) * 0x94d049bb133111eb;
    return x ^ (x >> 31);
  }

  size_t operator()(uint64_t x) const {
    static const uint64_t FIXED_RANDOM =
        chrono::steady_clock::now().time_since_epoch().count();
    return splitmix64(x + FIXED_RANDOM);
  }

  // hash function for std::pair<int, int> as the primary key type
  size_t operator()(pair<uint64_t, uint64_t> x) const {
    static const uint64_t FIXED_RANDOM =
        chrono::steady_clock::now().time_since_epoch().count();
    return splitmix64(x.first + FIXED_RANDOM) ^
           (splitmix64(x.second + FIXED_RANDOM) >> 1);
  }
};
```

After writing the custom hash function, we can pass the custom hash function into the container through the definition `unordered_map<int, int, my_hash> my_map;` or `unordered_map<pair<int, int>, int, my_hash> my_pair_map;`.
