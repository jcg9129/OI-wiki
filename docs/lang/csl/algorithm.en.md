STL provides about 100 template functions implementing algorithms, most of which are contained in `<algorithm>`, and a part of which is contained in `<numeric>` and `<functional>`. For a complete list of functions, please [see the reference manual](https://zh.cppreference.com/w/cpp/algorithm); for sorting-related ones, you can refer to the [corresponding page of sorting content](../../basic/stl-sort.md).

-   `find`: sequential search. `find(v.begin(), v.end(), value)`, where `value` is the value to be searched for.

-   `reverse`: reverse an array or string. `reverse(v.begin(), v.end())` or `reverse(a + begin, a + end)`.

-   `unique`: remove adjacent duplicate elements in a container. `unique(ForwardIterator first, ForwardIterator last)`, the return value is an iterator pointing to the end of the container **after deduplication**, and the size of the original container does not change. Combined with `sort`, it can achieve complete container deduplication.

-   `random_shuffle`: randomly shuffle an array. `random_shuffle(v.begin(), v.end())` or `random_shuffle(v + begin, v + end)`.

    ???+ warning "The `random_shuffle` function has been removed in the latest C++ standard"
        `random_shuffle` has been deprecated since C++14 and removed since C++17.
        
        In C++11 and newer standards, you can use the `shuffle` function instead of the original `random_shuffle`. The usage is `shuffle(v.begin(), v.end(), rng)` (the last parameter passed in is the random number generator used; generally use the Mersenne Twister pseudo-random number generator [`mt19937`](https://zh.cppreference.com/w/cpp/numeric/random/mersenne_twister_engine) seeded with the true random number generator [`random_device`](https://zh.cppreference.com/w/cpp/numeric/random/random_device)).
        
        ```cpp
        // #include <random>
        std::mt19937 rng(std::random_device{}());
        std::shuffle(v.begin(), v.end(), rng);
        ```

-   `sort`: sort. `sort(v.begin(), v.end(), cmp)` or `sort(a + begin, a + end, cmp)`, where `end` is the position after the last element of the array to be sorted, and `cmp` is a custom comparison function.

-   `stable_sort`: stable sort, usage same as `sort()`.

-   `nth_element`: classify by a specified range, i.e. find the $n$-th largest element in the sequence, making all elements to its left less than it and all elements to its right greater than it. `nth_element(v.begin(), v.begin() + n, v.end(), cmp)` or `nth_element(a + begin, a + begin + n, a + end, cmp)`.

-   `binary_search`: binary search. `binary_search(v.begin(), v.end(), value)`, where `value` is the value to be searched for.

-   `merge`: **merge in order** two (already sorted) sequences onto the **insert iterator** of a third sequence. `merge(v1.begin(), v1.end(), v2.begin(), v2.end() ,back_inserter(v3))`.

-   `inplace_merge`: **merge in place into one ordered sequence** the two (already sorted by the less-than operator) ranges `[first,middle), [middle,last)`. `inplace_merge(v.begin(), v.begin() + middle, v.end())`.

-   `lower_bound`: perform binary search in an ordered sequence, returning an iterator pointing to the position of the first element **greater than or equal to** $x$. If no such element exists, returns the end iterator. `lower_bound(v.begin(),v.end(),x)`.

-   `upper_bound`: perform binary search in an ordered sequence, returning an iterator pointing to the position of the first element **greater than** $x$. If no such element exists, returns the end iterator. `upper_bound(v.begin(),v.end(),x)`.

    ???+ warning "The time complexity of `lower_bound` and `upper_bound`"
        In an ordinary array, the time complexity of these two functions is both $O(\log n)$, but in associative containers such as `set`, directly calling `lower_bound(s.begin(),s.end(),val)` has time complexity $O(n)$.
        
        Associative containers such as `set` have already encapsulated functions such as `lower_bound` (like `s.lower_bound(val)`); calling it this way has time complexity $O(\log n)$.

-   `next_permutation`: change the current permutation to the **next permutation in the full permutation**. If the current permutation is already the **last permutation in the full permutation** (elements completely arranged from large to small), the function returns `false` and changes the permutation to the **first permutation in the full permutation** (elements completely arranged from small to large); otherwise, the function returns `true`. `next_permutation(v.begin(), v.end())` or `next_permutation(v + begin, v + end)`.

-   `prev_permutation`: change the current permutation to the **previous permutation in the full permutation**. Usage same as `next_permutation`.

-   `partial_sum`: find the prefix sum. Let the source container be $x$ and the target container be $y$; then let $y[i]=x[0]+x[1]+\dots+x[i]$. `partial_sum(src.begin(), src.end(), back_inserter(dst))`.

### Usage examples

-   Use `next_permutation` to generate the full permutation of $1$ to $9$. Example problem: [Luogu P1706 Full permutation problem](https://www.luogu.com.cn/problem/P1706)

    ???+ note "Implementation"
        ```cpp
        int N = 9, a[] = {1, 2, 3, 4, 5, 6, 7, 8, 9};
        do {
          for (int i = 0; i < N; i++) cout << a[i] << " ";
          cout << endl;
        } while (next_permutation(a, a + N));
        ```
-   Use `lower_bound` and `upper_bound` to find the dividing lines of elements less than $x$, equal to $x$, and greater than $x$ in the ordered array $a$.

    ???+ note "Implementation"
        ```cpp
        int N = 10, a[] = {1, 1, 2, 4, 5, 5, 7, 7, 9, 9}, x = 5;
        int i = lower_bound(a, a + N, x) - a, j = upper_bound(a, a + N, x) - a;
        // a[0] ~ a[i - 1] are the elements less than x, a[i] ~ a[j - 1] are the elements equal to x,
        // a[j] ~ a[N - 1] are the elements greater than x
        cout << i << " " << j << endl;
        ```
-   Use `partial_sum` to compute the prefix sum of the elements in $src$, and store it in $dst$.

    ???+ note "Implementation"
        ```cpp
        vector<int> src = {1, 2, 3, 4, 5}, dst;
        // compute the prefix sum of the elements in src, dst[i] = src[0] + ... + src[i]
        // the back_inserter function acts on the dst container, providing an iterator
        partial_sum(src.begin(), src.end(), back_inserter(dst));
        for (unsigned int i = 0; i < dst.size(); i++) cout << dst[i] << " ";
        ```
-   Use `lower_bound` to find the element in the ordered array $a$ closest to $x$. Example problem: [UVa10487 Closest Sums](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=16&page=show_problem&problem=1428)

    ???+ note "Implementation"
        ```cpp
        int N = 10, a[] = {1, 1, 2, 4, 5, 5, 8, 8, 9, 9}, x = 6;
        // lower_bound will return the address of the first element in a greater than or equal to x; the computed i is its subscript
        int i = lower_bound(a, a + N, x) - a;
        // in the following two cases, a[i] (the first element in a greater than or equal to x) is the answer:
        // 1. even the smallest element in a is greater than or equal to x;
        // 2. there exists an element in a greater than or equal to x, and the first element greater than or equal to x (a[i])
        // is closer to x than the first element less than x (a[i - 1]);
        // otherwise, a[i - 1] (the first element in a less than x) is the answer
        if (i == 0 || (i < N && a[i] - x < x - a[i - 1]))
          cout << a[i];
        else
          cout << a[i - 1];
        ```
-   Use `sort` and `unique` to find the **$k$-th smallest value** in the array $a$ (note: a repeatedly-occurring value counts only once, so this problem is not finding the $k$-th smallest element). Example problem: [Luogu P1138 The k-th smallest integer](https://www.luogu.com.cn/problem/P1138)

    ???+ note "Implementation"
        ```cpp
        int N = 10, a[] = {1, 3, 3, 7, 2, 5, 1, 2, 4, 6}, k = 3;
        sort(a, a + N);
        // unique will return the address after the last element of the deduplicated array; the computed cnt is the length of the deduplicated array
        int cnt = unique(a, a + N) - a;
        cout << a[k - 1];
        ```
