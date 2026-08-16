This page briefly introduces binary search, the ternary search derived from the bisection idea, and binary-searching on the answer.

## Binary search

### Definition

Binary search (also called half-interval search or logarithmic search) is an algorithm used to find a particular element in a sorted array.

### Process

Take finding a number in an ascending array as an example.

Each time it examines the middle element of the current part of the array. If the middle element is exactly the one being sought, the search ends. If the middle element is less than the value being sought, then the left side will only be smaller and cannot contain the sought element, so we only need to search the right side; if the middle element is greater than the value being sought, similarly we only need to search the left side.

### Properties

#### Time complexity

The best-case time complexity of binary search is $O(1)$.

The average and worst-case time complexities of binary search are both $O(\log n)$. Because binary search halves the query interval each time, for an array of length $n$ it performs at most $O(\log n)$ lookups.

#### Space complexity

The space complexity of the iterative version of binary search is $O(1)$.

The space complexity of the recursive version (without tail-call elimination) of binary search is $O(\log n)$.

### Implementation

```cpp
int binary_search(int start, int end, int key) {
  int ret = -1;  // return index -1 when the data is not found
  int mid;
  while (start <= end) {
    mid = start + ((end - start) >> 1);  // averaging directly may overflow, so use this formula
    if (arr[mid] < key)
      start = mid + 1;
    else if (arr[mid] > key)
      end = mid - 1;
    else {  // check equality last because in most searches the value is either greater or less
      ret = mid;
      break;
    }
  }
  return ret;  // single exit point
}
```

???+ note "Note"
    Refer to [Compiler optimization § Shift instead of multiplication](../lang/optimizations.md#shift-instead-of-multiplication). For the case where $n$ is signed, when you can guarantee $n\ge 0$, `n >> 1` uses fewer instructions than `n / 2`.

### Minimizing the maximum

Note that "sorted" here is in a generalized sense. If, in an array, one side (left or right) all satisfies some condition while the other side all fails to satisfy it, this can also be regarded as a kind of order (if we treat "satisfies the condition" as $1$ and "does not satisfy" as $0$, then at least along this one dimension of the condition it is sorted). In other words, binary search can be used to find the largest (or smallest) value satisfying some condition.

To find the smallest possible value of the largest value satisfying some condition (minimizing the maximum), the first idea is to enumerate this "maximum" candidate answer from small to large and check whether it is valid. If the answer is monotonic, binary search can be used to find the answer faster. Therefore, to use binary search to solve such a "minimize the maximum" problem, the following three conditions must be met:

1.  The answer lies within a fixed interval;
2.  It may not be easy to find a value that satisfies the condition, but it must be relatively easy to determine whether a given value satisfies the condition;
3.  Feasible solutions satisfy a certain monotonicity over the interval. In other words, if $x$ satisfies the condition, then $x + 1$ or $x - 1$ also satisfies it. (This yields the monotonicity mentioned above.)

Of course, maximizing the minimum works the same way.

### Binary search in the STL

The C++ standard library implements [`std::lower_bound`](https://zh.cppreference.com/w/cpp/algorithm/lower_bound), which finds the first element not less than a given value, and [`std::upper_bound`](https://zh.cppreference.com/w/cpp/algorithm/upper_bound), which finds the first element greater than a given value; both are defined in the header `<algorithm>`.

Both are implemented with binary search, so the elements must be sorted before calling them.

### bsearch

`bsearch` is the C standard library's implementation of binary search, defined in `<stdlib.h>`. In the C++ standard library, it is defined in `<cstdlib>`. `qsort` and `bsearch` are the only two algorithm-like functions in the C language.

Compared with `qsort`'s four parameters (see [STL for sorting](./stl-sort.md)), `bsearch` adds, at the far left, the parameter "the address of the element to search for". It is passed as an address so that the same comparison function used for `qsort` can be reused directly, achieving an immediate lookup after sorting. Therefore this parameter cannot be passed a concrete value directly; instead, the value to search for must first be stored in a variable, and the address of that variable passed in.

So `bsearch` has five parameters in total: the address of the element to search for, the array name, the number of elements, the element size, and the comparison rule. The comparison rule is still provided by specifying a comparison function; see [STL for sorting](./stl-sort.md) for details.

The return value of `bsearch` is the address of the found element, of type `void`.

Note: `bsearch` differs from the `lower_bound` and `upper_bound` above in two ways:

-   When there are multiple duplicate elements matching the condition, it returns the first matching element encountered during the binary search, which may therefore lie in the middle of the duplicate elements.
-   When no matching element is found, it returns NULL.

`lower_bound` can implement exactly the same functionality as `bsearch`, so a problem that can be passed using `bsearch` can be directly rewritten with `lower_bound` as well. However, because of the second difference above — for example, searching for 3 in the sequence 1, 2, 4, 5, 6 — it becomes difficult to implement the functionality of `lower_bound` with `bsearch`.

Since implementing `lower_bound` with `bsearch` is rather difficult, is it necessarily impossible? The answer is no; there is a somewhat tricky technique. By exploiting a characteristic of how the compiler handles the comparison function — that it always points the first argument at the element being searched for and the second argument at an element in the array being searched — `bsearch` can also implement `lower_bound` and `upper_bound`, as shown in the example below. Only, this requires the array being searched to be a global array, so that its base address can be passed in directly.

```cpp
int A[100005];  // example global array

// find the address of the first element not less than the search element
int lower(const void *p1, const void *p2) {
  int *a = (int *)p1;
  int *b = (int *)p2;
  if ((b == A || compare(a, b - 1) > 0) && compare(a, b) > 0)
    return 1;
  else if (b != A && compare(a, b - 1) <= 0)
    return -1;  // uses address subtraction, so the element type must be specified
  else
    return 0;
}

// find the address of the first element greater than the search element
int upper(const void *p1, const void *p2) {
  int *a = (int *)p1;
  int *b = (int *)p2;
  if ((b == A || compare(a, b - 1) >= 0) && compare(a, b) >= 0)
    return 1;
  else if (b != A && compare(a, b - 1) < 0)
    return -1;  // uses address subtraction, so the element type must be specified
  else
    return 0;
}
```

Since today's OI contestants rarely write pure C, and this method has limited use, it is not a focus. For beginners, we recommend honestly using the `lower_bound` and `upper_bound` functions in C++.

### Binary-searching on the answer

When solving problems, we often consider enumerating the answer and then checking whether the enumerated value is correct. If monotonicity holds, then the conditions for using binary search are met. Replacing this enumeration with binary search gives "binary-searching on the answer".

???+ note "[Luogu P1873 Cutting Trees](https://www.luogu.com.cn/problem/P1873)"
    The lumberjack Mirko needs to fell $M$ meters of timber. This is an easy job for Mirko, because he has a beautiful new logging machine that can mow down forests like wildfire. However, Mirko is only allowed to fell a single row of trees.

    Mirko's logging machine works as follows: Mirko sets a height parameter $H$ (meters), the machine raises a huge saw blade to height $H$, and saws off the part of every tree taller than $H$ (of course, the part of a tree not exceeding $H$ meters stays unchanged). Mirko then gets the parts of the trees that were sawn off.

    For example, if the heights of a row of trees are $20,~15,~10,~17$ and Mirko raises the blade to a height of $15$ meters, then after cutting the trees' remaining heights are $15,~15,~10,~15$, and Mirko gets $5$ meters of timber from tree $1$ and $2$ meters of timber from tree $4$, for a total of $7$ meters.

    Mirko cares deeply about ecological protection, so he does not want to fell too much timber. This is precisely why he sets the blade as high as possible. Your task is to help Mirko find the largest integer height $H$ of the blade such that he obtains at least $M$ meters of timber. That is, if the blade were raised by another $1$ meter, he would not get $M$ meters of timber.

??? note "Solution idea"
    We could enumerate the answer over $1$ to $10^9$, but this naive approach certainly cannot get full marks, because enumerating from $1$ to $10^9$ is too time-consuming. We can binary-search over the interval $[1,~10^9]$ for the answer and then check the feasibility of each answer (usually with a greedy method). **This is binary-searching on the answer.**

??? note "Reference code"
    ```cpp
    int a[1000005];
    int n, m;
    
    bool check(int k) {  // check feasibility; k is the blade height
      long long sum = 0;
      for (int i = 1; i <= n; i++)       // check each tree
        if (a[i] > k)                    // if the tree is taller than the blade height
          sum += (long long)(a[i] - k);  // accumulate the timber length
      return sum >= m;                   // feasible if it meets the minimum length
    }
    
    int find() {
      int l = 1, r = 1e9 + 1;   // left-closed, right-open, so 10^9 must be increased by 1
      while (l + 1 < r) {       // if the two points are not adjacent
        int mid = (l + r) / 2;  // take the middle value
        if (check(mid))         // if feasible
          l = mid;              // raise the blade height
        else
          r = mid;  // otherwise lower the blade height
      }
      return l;  // return the left value
    }
    
    int main() {
      cin >> n >> m;
      for (int i = 1; i <= n; i++) cin >> a[i];
      cout << find();
      return 0;
    }
    ```
    
    After reading the code above, you will surely have two questions:
    
    1.  Why is the search interval left-closed and right-open?
    
        Because when the search reaches the end, it looks like this (taking the valid maximum as an example):
    
        ![](./images/binary-final-1.svg)
    
        and then
    
        ![](./images/binary-final-2.svg)
    
        The valid minimum is exactly the opposite.
    2.  Why return the left value?
    
        Same as above.

## Ternary search

### Introduction

Binary search can be used to approximate the zeros of a function. To find the extremum of a unimodal function, one usually needs ternary search.

For a function $f(x)$, if there exists $x^*$ such that $f(x)$ is monotonically increasing for $x<x^*$ and monotonically decreasing for $x>x^*$, then $f(x)$ is called a unimodal function. Clearly, $x^*$ is its maximizer and $f(x^*)$ is its maximum.

??? note "Why not find the extremum by finding a zero of the derivative?"
    Objectively, after computing the derivative, finding the extremum of the unimodal function by using binary search to find the zero of the derivative (since the function is unimodal, the zero of its derivative within the same range is unique) is feasible.

    But first, for some functions the process and result of differentiation are rather complex.

    Second, in some problems the unimodal function whose extremum is sought is not a single function, but a function obtained by special operations on multiple functions (such as finding the maximum of the minimum of several linear functions with not entirely identical monotonicity). In this case the derivative of the function may be piecewise, and it may be non-differentiable at some points.

???+ warning "Note"
    Ternary search can find both the maximum of a unimodal function and the minimum of a "unimodal valley" function. For convenience, unless otherwise specified, the text below takes finding the maximum of a unimodal function as an example.

### Process

The basic idea of ternary search is similar to that of binary search, but each operation picks two points $lmid < rmid$ (the two blue points in the figure below) within the current interval $[l,r]$ (between the two orange points in the figure below). As shown below, if $f(lmid)<f(rmid)$, then $f$ must be monotonically increasing on $[l,lmid)$ (the red part in the figure below), so the maximizer (the green point in the figure below) cannot lie in this interval and it can be discarded; however, we cannot rule out the possibility that the maximizer lies to the right of $rmid$, so we cannot discard more. The reverse case is analogous.

![](images/ternary.svg)

The correctness of ternary search does not depend on the choice of $lmid$ and $rmid$; usually the two trisection points can be taken. However, their choice does affect the efficiency of ternary search. This is because each ternary-search operation discards one of the two side intervals. To reduce the number of ternary-search operations, the two side intervals should be as large as possible. Therefore, taking $lmid$ and $rmid$ as $mid-\varepsilon$ and $mid+\varepsilon$ respectively at each operation is a good choice. In fact, the choice of $mid\pm \varepsilon$ amounts to computing the approximate derivative $\dfrac{f(mid+\varepsilon)-f(mid-\varepsilon)}{2\varepsilon}$ at $mid$ and judging its sign to determine on which side of $mid$ the extremum lies.

### Implementation

The pseudocode is as follows:

$$
\begin{array}{l}
\textbf{Algorithm}\operatorname{TernarySearch}(f,l,r):\\
\textbf{Input. } \text{A unimodal function } f(x) \text{ and its domain } [l,r].  \\
\textbf{Output. } \text{The maximizer }x^*\text{, up to an error of }\varepsilon\text{, and its value } f(x^*). \\
\textbf{Method. } \\
\begin{array}{ll}
1 & \textbf{while } r - l > \varepsilon\\
2 & \qquad mid\gets (l+r)/2\\
3 & \qquad lmid\gets mid - \varepsilon / 3 \\
4 & \qquad rmid\gets mid + \varepsilon / 3 \\
5 & \qquad \textbf{if } f(lmid) < f(rmid) \\
6 & \qquad \qquad l\gets lmid \\
7 & \qquad \textbf{else } \\
8 & \qquad \qquad r\gets rmid \\
9 & x^* \gets (l+r)/2 \\
10& \textbf{return } x^*,~ f(x^*)
\end{array}
\end{array}
$$

???+ tip "Choosing the split points"
    In the code, the split points are chosen as $mid \pm \varepsilon / 3$ to ensure that the split points are always between the current $l$ and $r$, thereby avoiding an infinite loop.

???+ info "The integer case"
    If the domain of the function $f(x)$ is the integers, then both the ternary search above and the golden-section search below should terminate when $r-l$ is small. For small $r-l$, the maximizer must be found by brute-force traversal.

### Optimization: golden-section search

If a single call to $f(x)$ is expensive and the number of calls to $f(x)$ must be further reduced, the constant factor of ternary search can be further improved by the golden-section search. This is also an important part of the optimum-seeking method proposed by Hua Luogeng.

In ternary search, each iteration requires two function calls, and after a single iteration the interval length shrinks to at most $1/2$ of the original. This means that to reach precision $\varepsilon$, at least

$$
2\log_2\dfrac{r-l}{\varepsilon}
$$

function calls are needed. This is the best result ternary search can achieve. If other split points are chosen, such as the trisection points, the number of calls increases further, because the interval shrinks more slowly after a single iteration.

The improvement idea of the golden-section search is to reuse split points computed earlier. This way, except for the first iteration which needs two function calls, every other iteration needs only one function call. Let the golden ratio be

$$
\phi = \dfrac{\sqrt{5}-1}{2} \approx 0.618.
$$

At each iteration, the chosen split points are the left and right golden-section points:

$$
m^l = \phi l +(1-\phi)r,~m^r = (1-\phi)l+\phi r.
$$

Dividing a segment at golden-section points has a self-similar structure. That is, $m^l$ is the left golden-section point of the segment $[l,r]$ and also the right golden-section point of the segment $[l,m^r]$. The benefit of choosing split points this way is that among the split points chosen in iteration $k>1$, one is always a point computed before, whose result can be reused directly.

![](./images/golden-section-search.svg)

After choosing split points this way, to reach precision $\varepsilon$ only

$$
1 + \log_{\phi^{-1}}\dfrac{r-l}{\varepsilon} \approx 1 + 1.44\log_2\dfrac{r-l}{\varepsilon}
$$

function calls are needed. Asymptotically, the number of function calls is smaller.

The pseudocode is as follows:

$$
\begin{array}{l}
\textbf{Algorithm}\operatorname{GoldenSectionSearch}(f,l,r):\\
\textbf{Input. } \text{A unimodal function } f(x) \text{ and its domain } [l,r].  \\
\textbf{Output. } \text{The maximizer }x^*\text{, up to an error of }\varepsilon\text{, and its value } f(x^*). \\
\textbf{Method. } \\
\begin{array}{ll}
1 & lmid \gets \phi l + (1-\phi)r \\
2 & rmid \gets (1-\phi)l + \phi r \\
3 & lval \gets f(lmid) \\
4 & rval \gets f(rmid) \\
5 & \textbf{while } r - l > \varepsilon \\
6 & \qquad \textbf{if } lval > rval \\
7 & \qquad \qquad r \gets rmid \\
8 & \qquad \qquad rmid \gets lmid \\
9 & \qquad \qquad rval \gets lval \\
10& \qquad \qquad lmid \gets \phi l + (1-\phi)r \\
11& \qquad \qquad lval \gets f(lmid) \\
12& \qquad \textbf{else} \\
13& \qquad \qquad l \gets lmid \\
14& \qquad \qquad lmid \gets rmid \\
15& \qquad \qquad lval \gets rval \\
16& \qquad \qquad rmid \gets (1-\phi)l + \phi r \\
17& \qquad \qquad rval \gets f(rmid) \\
18& x^* \gets (l+r)/2 \\
19& \textbf{return }x^*,~f(x^*)
\end{array}
\end{array}
$$

### Example problems

???+ note "[Luogu P3382 - Ternary search](https://www.luogu.com.cn/problem/P3382)"
    Given a degree-$N$ function and a range $[l, r]$, find the unique value of $x$ such that the function is monotonically increasing on $[l, x]$ and monotonically decreasing on $[x, r]$.

??? note "Solution idea"
    This problem asks for the value of the argument at which the degree-$N$ function takes its maximum on $[l, r]$, so ternary search can obviously be used.

??? note "Reference code"
    === "C++"
        ```cpp
        --8<-- "docs/basic/code/binary/binary_1.cpp"
        ```
    
    === "Python"
        ```python
        --8<-- "docs/basic/code/binary/binary_1.py"
        ```

### Exercises

-   [UVa 1476 - Error Curves](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=447&page=show_problem&problem=4222)
-   [UVa 10385 - Duathlon](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=15&page=show_problem&problem=1326)
-   [UOJ 162 - [Tsinghua Training 2015] Bulb Test](https://uoj.ac/problem/162)
-   [Luogu P7579 - "RdOI R2" Weigh](https://www.luogu.com.cn/problem/P7579)

## Fractional programming

See: [Fractional programming](../misc/frac-programming.md)

Fractional programming is usually described as the following problem: each item has two attributes $c_i$, $d_i$, and we are asked to select several of them in some way so as to maximize or minimize $\frac{\sum{c_i}}{\sum{d_i}}$.

Classic examples include the optimal ratio cycle, the optimal ratio spanning tree, and so on.

Fractional programming can be solved with binary search.

## References

-   [Ternary search - Wikipedia](https://en.wikipedia.org/wiki/Ternary_search)
-   [Golden-section search - Wikipedia](https://en.wikipedia.org/wiki/Golden-section_search)
-   [Ternary search - CP Algortihms](https://cp-algorithms.com/num_methods/ternary_search.html)
