author: Early0v0, frank-xjh, Great-designer, ksyx, qiqistyle, Tiphereth-A , Saisyc, shuzhouliu, Xeonacid, xyf007

This page briefly introduces the enumeration algorithm.

## Introduction

Enumeration is a problem-solving strategy that guesses the answer based on existing knowledge.

The idea of enumeration is to keep guessing, trying possibilities one by one from a set of candidates, and then checking whether the problem's condition holds.

## Key points

### State the solution space

Build a concise mathematical model.

When enumerating, think clearly: what are the possible cases? Which elements should be enumerated?

### Reduce the enumeration space

What is the range of enumeration? Does everything need to be enumerated?

When using enumeration to solve a problem, you must think these two things through clearly, otherwise it will incur unnecessary time overhead.

### Choose an appropriate enumeration order

Judge based on the problem. For example, the example problem asks for the largest prime satisfying the condition, so naturally enumerating from large to small is more appropriate.

## Example

The following is an example of using enumeration to solve a problem and optimizing the enumeration range.

??? note "Example"
    Given an array whose elements are pairwise distinct and all nonzero, find the number of pairs in the array whose sum is $0$.

??? note "Solution idea"
    The code to enumerate two numbers is easy to write.
    
    === "C++"
        ```cpp
        for (int i = 0; i < n; ++i)
          for (int j = 0; j < n; ++j)
            if (a[i] + a[j] == 0) ++ans;
        ```
    
    === "Python"
        ```python
        for i in range(n):
            for j in range(n):
                if a[i] + a[j] == 0:
                    ans += 1
        ```
    
    === "Java"
        ```java
        for (int i = 0; i < n; ++i)
          for (int j = 0; j < n; ++j)
            if (a[i] + a[j] == 0) ++ans;
        ```
    
    Let's see how to optimize the enumeration range. Since the problem does not require the pair to be ordered, the answer is twice the count of the ordered case (consider that if `(a, b)` is an answer, then `(b, a)` is also an answer). For this situation, we only need to count the answers after artificially imposing an order, and finally multiply by $2$.
    
    We may as well require the first number to appear in a later position. The code is as follows:
    
    === "C++"
        ```cpp
        for (int i = 0; i < n; ++i)
          for (int j = 0; j < i; ++j)
            if (a[i] + a[j] == 0) ++ans;
        ans *= 2;
        ```
    
    === "Python"
        ```python
        for i in range(n):
            for j in range(i):
                if a[i] + a[j] == 0:
                    ans += 1
        ans *= 2
        ```
    
    === "Java"
        ```java
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < i; ++j)
                if (a[i] + a[j] == 0) ++ans;
        ans *= 2;
        ```
    
    It is not hard to see that we have already reduced the enumeration range of $j$, reducing the time overhead of this code.
    
    We can optimize further on top of this.
    
    Do both numbers really have to be enumerated? After enumerating one of the numbers, the problem's condition has already determined the condition on the other element (the other number); if we can find a way to directly decide whether the number required by the problem exists, we can save the time of enumerating the second number. More advanced, when the data range permits, we can use a bucket[^1] to record the numbers we have traversed.
    
    === "C++"
        ```cpp
        --8<-- "docs/basic/code/enumerate/enumerate_1.cpp"
        ```
    
    === "Python"
        ```python
        met = [False] * (MAXN * 2 + 1)
        for i in range(n):
            if met[MAXN - a[i]]:
                ans += 1
            met[a[i] + MAXN] = True
        ans *= 2
        ```
    
    === "Java"
        ```java
        boolean[] met = new boolean[MAXN * 2 + 1];
        for (int i = 0; i < n; ++i) {
            if (met[MAXN - a[i]]) ++ans;
            met[MAXN + a[i]] = true;
        }
        ans *= 2;
        ```

### Complexity analysis

-   Time complexity analysis: traversing the array $a$ once suffices to meet the problem's requirement, so when $n$ is large enough the time complexity is $O(n)$.
-   Space complexity analysis: $O(n+\max\{|x|:x\in a\})$.

## Exercises

-   [2811: Lights Out Problem - OpenJudge](http://bailian.openjudge.cn/practice/2811/)

## Footnotes

[^1]: [Bucket sort](../basic/bucket-sort.md), the [majority element problem](../misc/main-element.md#离线算法), and the [explanation of the bucket data structure on Stack Overflow](https://stackoverflow.com/questions/42399355/what-is-a-bucket-or-double-bucket-data-structure) (in English).
