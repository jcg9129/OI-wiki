This page briefly introduces Shell sort.

## Definition

Shell sort (also called the diminishing-increment sort) is an improved version of [insertion sort](./insertion-sort.md). Shell sort is named after its inventor, Donald Shell.

## Process

The sort compares and moves non-adjacent records:

1.  Divide the sequence to be sorted into several subsequences (the elements of each subsequence are equally spaced in the original array);
2.  Perform insertion sort on these subsequences;
3.  Decrease the spacing between elements in each subsequence, and repeat the process until the spacing decreases to $1$.

## Properties

### Stability

Shell sort is an unstable sorting algorithm.

### Time complexity

The best-case time complexity of Shell sort is $O(n)$.

The average-case and worst-case time complexities of Shell sort depend on the choice of the gap sequence. Let the gap sequence be $H$; below we give two classic choices of $H$, both of which reduce the complexity of the sorting algorithm to the $o(n^2)$ level.

???+ note "Proposition 1"
    If the gap sequence is $H= \{ 2^k-1\mid k=1,2,\ldots,\lfloor\log_2 n\rfloor \}$ (from large to small), then the time complexity of Shell sort is $O(n^{3/2})$.

???+ note "Proposition 2"
    If the gap sequence is $H= \{ k=2^p\cdot 3^q\mid p,q\in \mathbb N,k\le n \}$ (from large to small), then the time complexity of Shell sort is $O(n\log^2 n)$.

To prove these two propositions, we first state and prove an important theorem, which captures the most essential feature of Shell sort.

???+ note "Theorem 1"
    As soon as the program has executed one $\text{InsertionSort}(h)$, no matter how the $\text{InsertionSort}$ function is subsequently called or how the array $A$ is transformed, the following property is always maintained:
    
    $$
    \begin{array}{c}
    A_1,A_{1+h},A_{1+2h},\ldots \\
    A_2,A_{2+h},A_{2+2h},\ldots \\
    \vdots \\
    A_h,A_{h+h},A_{h+2h},\ldots
    \end{array}
    $$

Next we prove Theorem 1.

We first prove Lemma 1.

???+ note "Lemma 1"
    For integers $n,m$, a positive integer $l$, and two arrays $X(x_1,x_2,\ldots,x_{n+l}),Y(y_1,y_2,\ldots,y_{m+l})$ satisfying the following requirement:
    
    $$
    y_1 \le x_{n+1},y_2 \le x_{n+2},\ldots,y_l \le x_{n+l}
    $$
    
    then after sorting the two arrays in ascending order respectively, the above requirement still holds.

??? note "Proof of Lemma 1"
    Let array $X$ after sorting be array $X'(x'_1,\ldots,x'_{n+l})$, and array $Y$ after sorting be array $Y'(y'_1,\ldots,y'_{m+l})$.
    
    For any $1\le i\le l$, $x'_{n+i}$ is less than or equal to $l-i$ elements of array $X'$, and also less than or equal to $l-i$ elements of array $X$ (this is because $X$ and $X'$ have the same multiset of elements).
    
    Then in the multiset $\{x_{n+1},\ldots,x_{n+l} \} \subset X$, the number of elements greater than or equal to $x'_{n+i}$ is at most $l-i$.
    
    Consequently the number of elements less than $x'_{n+i}$ is at least $i$; take $i$ of them, say $x_{n+k_1},x_{n+k_2},\ldots,x_{n+k_i}$. Then we have:
    
    $$
    y_{k_1}\le x_{n+k_1}\le x'_{n+i},y_{k_2}\le x_{n+k_2}\le x'_{n+i},\ldots,y_{k_i}\le x_{n+k_i}\le x'_{n+i}
    $$
    
    So $x'_{n+i}$ is greater than or equal to at least $i$ elements of $Y$, i.e. of $Y'$, and naturally $y'_i\le x'_{n+i}\,(1\le i\le l)$.

Now back to the proof of the original claim:

We actually only need to prove that after the call $\text{InsertionSort}(h)$ is immediately followed by the next call $\text{InsertionSort}(k)$, the $h$ subsequences are still sorted; the rest then follows easily by induction. Below we consider only the next call:

After executing $\text{InsertionSort}(h)$, the following groups have been sorted:

$$
\begin{array}{c}
A_1,A_{1+h},A_{1+2h},\ldots \\
A_2,A_{2+h},A_{2+2h},\ldots \\
\vdots \\
A_h,A_{h+h},A_{h+2h},\ldots
\end{array}
$$

And executing $\text{InsertionSort}(k)$ afterward sorts the following groups:

$$
\begin{array}{c}
A_1,A_{1+k},A_{1+2k},\ldots \\
A_2,A_{2+k},A_{2+2k}, \ldots \\
\vdots \\
A_k,A_{k+k},A_{k+2k},\ldots
\end{array}
$$

For each $i$ $(1\le i\le \min(h,k))$, consider the following two groups:

$$
\begin{array}{c}
A_i,A_{i+k},A_{i+2k},\ldots \\
\ldots,A_{i+h},A_{i+h+k},A_{i+h+2k},\ldots
\end{array}
$$

The reason a "$\ldots$" is also added in front of the second group is that possibly $i+h\ge k$, so there are elements in front as well.

Then the second group is the array $X$ in Lemma $1$, the first group is the array $Y$, $l$ is the length of the second group from $i+h$ up to the end, $n$ is the length of the leading "$\ldots$" of the second group, and $m$ is the number remaining in the first group after removing its first $l$ elements.

And since we have:

$$
A_i\le A_{i+h},A_{i+k}\le A_{i+h+k},\ldots
$$

by Lemma $1$, after executing $\text{InsertionSort}(k)$ to sort the two groups respectively, this relationship still holds, i.e. we still have $A_i\le A_{i+h}\,(1\le i\le \min(h,k))$.

If $i>\min(h,k)$, it is easy to see that $i$ can be obtained by taking a positive integer $w$ $(1\le w\le \min(h,k))$ plus several $k$s, so the previous case already implies the proof of this case.

Combining the above discussion, we have: after executing $\text{InsertionSort}(k)$, it is still the case that $A_i\le A_{i+h}\,(1\le i\le n-h)$.

Thus Theorem 1 is proven.

This theorem reveals the key to why Shell sort can optimize its complexity under a specific set $H$: because throughout the whole process it can consistently keep the earlier achievements from being destroyed (i.e. the $h$ subsequences remain sorted respectively), thereby greatly reducing the number of moves of the pointer $i$ in later calls.

Next we single out a number-theoretic lemma and prove it. This theorem is greatly famous in the OI community because of the problem [Xiaokai's Confusion](https://www.luogu.com.cn/problem/P3951). In the proof of the complexity of Shell sort, it also greatly extends Theorem $1$.

???+ note "Lemma 2"
    If $a,b$ are both positive integers and coprime, then the largest positive integer not in the set $\{ax+by\mid x,y\in \mathbb N \}$ is $ab-a-b$.

??? note "Proof of Lemma 2"
    Prove in two steps:
    
    -   First prove that the equation $ax+by=ab-a-b$ has no solution with both $x,y$ nonnegative integers:
    
        Without the nonnegativity restriction, two solutions are easily obtained: $(b-1,-1),(-1,a-1)$.
    
        From their general-solution form $x=x_0+tb,y=y_0-ta$, it is easy to see the two solutions above are "adjacent" (because $b-1-b=-1$).
    
        As $t$ increases, $x$ increases and $y$ decreases, so if the equation had a nonnegative integer solution, it would necessarily be sandwiched between these two solutions; but these two solutions are "adjacent", with no other solution in between.
    
        Hence there can be no nonnegative integer solution.
    -   Then prove that for any integer $c > ab-a-b$, the equation $ax+by=c$ has a nonnegative integer solution:
    
        Find a solution $(x_0,y_0)$ satisfying $0\le x_0 < b$ (this can be done from the general-solution expression).
    
        Then we have:
    
        $$
        by_0=c-ax_0\ge c-a(b-1)>ab-a-b-ab+a=-b
        $$
    
        So $b(y_0+1) > 0$, and since $b>0$, we have $y_0+1>0$, so $y_0\ge 0$.
    
        So $(x_0,y_0)$ is a nonnegative integer solution.
    
    This completes the proof.

The following theorem reveals how Lemma $2$ extends Theorem $1$.

???+ note "Theorem 2"
    If $\gcd(h_{t+1},h_t)=1$, then after the program has executed $\text{InsertionSort}(h_{t+1})$ and $\text{InsertionSort}(h_t)$, the time complexity of executing $\text{InsertionSort}(h_{t-1})$ is $O\left(\dfrac{nh_{t+1}h_t}{h_{t-1}} \right)$, and for each $j$, the number of moves of its $i$ is of the order $O\left(\dfrac{h_{t+1}h_t}{h_{t-1}} \right)$.

??? note "Proof of Theorem 2"
    For the part with $j\le h_{t+1}h_t$, the number of moves of $i$ is clearly of the order $O\left(\dfrac{h_{t+1}h_t}{h_{t-1}} \right)$.
    
    So below we assume $j>h_{t+1}h_t$.
    
    For any positive integer $k$ satisfying $1\le k\le j-h_{t+1}h_t$, note that: $h_{t+1}h_t-h_{t+1}-h_t<h_{t+1}h_t\le j-k\le j-1$
    
    And since $\gcd(h_{t+1},h_t)=1$, by Lemma $2$ there exist nonnegative integers $a,b$ such that: $ah_{t+1}+bh_t=j-k$.
    
    That is:
    
    $$
    k=j-ah_{t+1}-bh_t
    $$
    
    By Theorem $1$:
    
    $$
    A_{j-bh_t}\le A_{j-(b-1)h_t}\le \ldots\le A_{j-h_t}\le A_j
    $$
    
    and
    
    $$
    A_{j-bh_t-ah_{t+1}}\le A_{j-bh_t-(a-1)h_{t+1}}\le \ldots\le A_{j-bh_t-h_{t+1}}\le A_{j-bh_t}
    $$
    
    Combining the above, we have: $A_k=A_{j-ah_{t+1}-bh_t}\le A_j$.
    
    So for any $1\le k\le j-h_{t+1}h_t$, we have $A_k\le A_j$.
    
    In the Shell-Sort pseudocode, the pointer $i$ decreases by $h_{t-1}$ each time; after decreasing $O\left(\dfrac{h_{t+1}h_t}{h_{t-1}} \right)$ times, it makes $i\le j-h_{t+1}h_t$, whereupon $A_i\le A_j$, which does not satisfy the condition of the while loop, so it exits.
    
    Having proven the move complexity for each $j$, we can obtain the total time complexity:
    
    $$
    \sum_{j=h_{t-1}+1}^n{O\left(\frac{h_{t+1}h_t}{h_{t-1}} \right)}=O\left(\frac{nh_{t+1}h_t}{h_{t-1}}\right)
    $$
    
    Q.E.D.

Examining the proof of Theorem $2$ carefully, we can see: Theorem 1 can be "linearly combined", i.e. if $A$ is sorted at interval $h$ and also sorted at interval $k$, then it is still sorted at any nonnegative-coefficient linear combination of $h$ and $k$. And this "linearity" is exactly what Lemma $2$ guarantees.

With these two theorems, we can prove Propositions $1$ and $2$.

??? note "Proof of Proposition 1"
    Write $H$ in sequence form:
    
    $$
    H(h_1=1,h_2=3,h_3=7,\ldots,h_{\lfloor \log_2 n\rfloor}=2^{\lfloor \log_2 n\rfloor}-1)
    $$
    
    The execution order of Shell-Sort is: $\text{InsertionSort}(h_{\lfloor \log_2 n\rfloor}),\text{InsertionSort}(h_{\lfloor \log_2 n\rfloor-1}),\ldots,\text{InsertionSort}(h_2),\text{InsertionSort}(h_1)$.
    
    Analyze the complexity in two parts:
    
    -   For the leading several $h_t$ satisfying $h_t\ge \sqrt{n}$, clearly the time complexity of $\text{InsertionSort}(h_t)$ is $O\left(\dfrac{n^2}{h_t} \right)$.
    
        Consider the term $h_k$ closest to $\sqrt{n}$; we have:
    
        $$
        O\left(\frac{n^2}{h_t} \right)=O(n^{3/2})
        $$
    
        And for $h_i$ with $i> k$, since $2h_i< h_{i+1}$, we get:
    
        $$
        O\left(\frac{n^2}{h_i} \right)=O(n^{3/2}/2^{i-k})\,(i>k)
        $$
    
        So the total time complexity of the part $\ge \sqrt n$ is:
    
        $$
        \sum_{i=k}^{\lfloor \log_2 n\rfloor}{O(n^{3/2}/2^{i-k})}=O(n^{3/2})
        $$
    -   For the remaining terms satisfying $h_t< \sqrt{n}$, the complexity of the first two terms is still $O(n^{3/2})$, and for the later terms $h_t$, by Theorem $2$ the time complexity is:
    
        $$
        O\left(\frac{nh_{t+2}h_{t+1}}{h_t} \right)=O\left(\frac{nh_{t+2}\cdot h_{t+2}/2}{h_{t+2}/4} \right)=O(nh_{t+2})
        $$
    
        Using the property $2h_i < h_{i+1}$ again, the total time complexity of this part is (where $k$ below retains the meaning from the previous case):
    
        $$
        2O(n^{3/2})+\sum_{i=1}^{k-3}{O(nh_{i+1})}=O(n^{3/2})+\sum_{i=1}^{k-3}{O(nh_{k-1}/2^{k-i-3})}=O(n^{3/2})+O(nh_{k-1})=O(n^{3/2})
        $$
    
    In summary, the total time complexity is $O(n^{3/2})$.

??? note "Proof of Proposition 2"
    Note a fact: if $\text{InsertionSort}(2)$ and $\text{InsertionSort}(3)$ have already been executed, then because $2\cdot 3-2-3=1$, by Theorem $2$ each element can only have the single element adjacent before it possibly greater than it, and all elements before that are smaller than it. So the pointer $i$ needs at most two steps to exit the while loop. That is, executing $\text{InsertionSort}(1)$ at this point has complexity reduced to $O(n)$.
    
    Going further: if $\text{InsertionSort}(4)$ and $\text{InsertionSort}(6)$ have already been executed, consider the subsequence of all odd-indexed elements and the subsequence of all even-indexed elements. This amounts to executing $\text{InsertionSort}(2)$ and $\text{InsertionSort}(3)$ on these two subsequences respectively. Then likewise, executing $\text{InsertionSort}(2)$ at this point amounts to executing $\text{InsertionSort}(1)$ on the two subsequences respectively, needing only the order of the sum of the two sequences, i.e. $O(n)$ complexity, to make the array sorted at interval $2$.
    
    Continuing by induction, we obtain: if $\text{InsertionSort}(2h)$ and $\text{InsertionSort}(3h)$ have already been executed, then executing $\text{InsertionSort}(h)$ also has complexity only $O(n)$.
    
    Next, analyze the complexity in two parts:
    
    -   For the part with $h_t>n/3$, executing each $\text{InsertionSort}(h_t)$ has complexity $O(n^2/h_t)$.
    
        And $n^2/h_t<3n$, so a single insertion sort has complexity $O(n)$.
    
        And the number of elements in this part is of the order $O(\log^2 n)$, so the time complexity of this part is $O(n\log^2 n)$.
    -   For the part with $h_t\le n/3$, because $3h_t\le n$, $\text{InsertionSort}(2h_t)$ and $\text{InsertionSort}(3h_t)$ have already been executed before this, so executing $\text{InsertionSort}(h_t)$ has time complexity $O(n)$.
    
        Likewise, the number of elements in this part is also of the order $O(\log^2 n)$, so the time complexity of this part is $O(n\log^2 n)$.
    
    In summary, the total time complexity is $O(n\log^2 n)$.

### Space complexity

The space complexity of Shell sort is $O(1)$.

## Implementation

=== "C++[^ref1]"
    ```cpp
    template <typename T>
    void shell_sort(T array[], int length) {
      int h = 1;
      while (h < length / 3) {
        h = 3 * h + 1;
      }
      while (h >= 1) {
        for (int i = h; i < length; i++) {
          for (int j = i; j >= h && array[j] < array[j - h]; j -= h) {
            std::swap(array[j], array[j - h]);
          }
        }
        h = h / 3;
      }
    }
    ```

=== "Python"
    ```python
    def shell_sort(array, length):
        h = 1
        while h < length / 3:
            h = int(3 * h + 1)
        while h >= 1:
            for i in range(h, length):
                j = i
                while j >= h and array[j] < array[j - h]:
                    array[j], array[j - h] = array[j - h], array[j]
                    j -= h
            h = int(h / 3)
    ```

## References and notes

[^ref1]: [Shell sort - Wikipedia, the free encyclopedia](https://zh.wikipedia.org/wiki/%E5%B8%8C%E5%B0%94%E6%8E%92%E5%BA%8F)
