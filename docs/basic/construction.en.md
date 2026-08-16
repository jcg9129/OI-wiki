author: leoleoasd, yzxoi, Estrella-Explore

This page briefly introduces the problem type of constructive problems.

## Introduction

Constructive problems are a common problem type in contests.

Formally, the answer to the problem often exhibits some kind of regularity, so that even when the problem size grows rapidly, there is still a chance to obtain the answer relatively easily.

This requires thinking, while solving the problem, about how the growth of the problem size affects the answer, and whether that effect can be generalized. For example, when designing a dynamic programming method, one has to consider what effect the transition from one state to a successor state causes.

## Characteristics

A very noticeable characteristic of constructive problems is their high degree of freedom; that is, a problem may have many ways to construct a solution, but there will be a relatively simple construction that satisfies the requirements. It seems as if the requirements have been loosened, making the problem easier, but very often it is precisely this high degree of freedom that leaves the problem without a clear line of attack and hard to get started on.

Another characteristic of constructive problems is that their form is flexible and varied. There is no universal method or template that can solve all constructive problems; it is even hard to find commonalities in the solution approaches.

## Examples

Below we list some examples to help readers appreciate some of the ideas behind constructive problems and to offer inspiration on approach. It is recommended that you think deeply before looking at the solutions, and you are also welcome to share interesting constructive problems.

### Example 1

???+ note "[Codeforces Round #384 (Div. 2) C.Vladik and fractions](http://codeforces.com/problemset/problem/743/C)"
    Construct a triple $x,y,z$ such that for a given $n$, $\dfrac{1}{x}+\dfrac{1}{y}+\dfrac{1}{z}=\dfrac{2}{n}$ holds.

??? note "Solution idea"
    The construction method of this problem can be seen from the second sample.
    
    Clearly $n,n+1,n(n+1)$ is a valid solution. As a special case, when $n=1$ there is no solution, because $n+1$ and $n(n+1)$ are equal at that point.
    
    As for how the construction idea arises, it is probably a matter of observing the samples plus a bit of number sense. This problem is not hard for people with strong mathematical intuition.

### Example 2

???+ note "[Luogu P3599 Koishi Loves Construction](https://www.luogu.com.cn/problem/P3599)"
    Task 1: Determine whether it is possible to construct, and construct, a permutation of $1\dots n$ of length $n$ whose $n$ prefix sums are pairwise distinct modulo $n$.
    
    Task 2: Determine whether it is possible to construct, and construct, a permutation of $1\dots n$ of length $n$ whose $n$ prefix products are pairwise distinct modulo $n$.

??? note "Solution idea"
    For task 1:
    
    When $n$ is odd, no valid solution can be constructed;
    
    When $n$ is even, we can construct a sequence of the form $n,1,n-2,3,\cdots$.
    
    First, we can observe that $n$ must appear in the first position of the sequence; otherwise the two prefix sums immediately before and after $n$ would inevitably fall into the awkward situation of being equal modulo $n$;
    
    Then, we consider how to construct the whole sequence:
    
    Consider obtaining the original sequence by constructing the prefix-sum sequence. We can observe that the pairwise differences of the prefix-sum sequence cannot be equal modulo $n$, because the difference sequence of the prefix-sum sequence corresponds to the original permutation.
    
    We therefore try to construct this sequence so that the prefix-sum sequence, modulo $n$, has the form
    
    $$
    0,1,-1,2,-2,\cdots
    $$
    
    It is not hard to see that it perfectly satisfies all the constraints.
    
    For task 2:
    
    When $n$ is a composite number other than $4$, no valid solution can be constructed;
    
    When $n$ is prime or equal to $4$, we can construct a sequence of the form $1,\dfrac{2}{1},\dfrac{3}{2},\cdots,\dfrac{n-1}{n-2},n$.
    
    First consider when a solution exists:
    
    Clearly, when $n$ is composite there is no solution. This is because for a composite number there exist two smaller numbers $p,q$ such that $p\times q \equiv 0 \pmod n$, for example $(3\times6)\%9=0$. Then, once both $p$ and $q$ have appeared, the prefix product of the sequence will remain $0$, so there is no solution for a composite number. As a special case, we observe that $4=2\times 2$ has no qualifying $p,q$, and therefore a valid solution exists.
    
    We consider how to construct this sequence:
    
    With the same idea as task 1, we find that $1$ must appear in the first position of the sequence, otherwise the two prefix products immediately before and after $1$ would necessarily be equal; and $n$ must appear in the last position of the sequence, because all prefix products after the position where $n$ appears are $0$ modulo $n$. After analyzing the several samples given by the problem, we find that in all samples there is a valid solution whose prefix products modulo $n$ are $1,2,3,\cdots,n$, so we can construct the sequence described above to satisfy this condition. Then we only need to prove that these $n$ numbers are pairwise distinct.
    
    We find that these numbers are all the modular inverses of $1 \cdots n-2$ plus $1$, so they are pairwise distinct, and the problem is solved.

### Example 3

???+ note "[AtCoder Grand Contest 032 B](https://atcoder.jp/contests/agc032/tasks/agc032_b)"
    Given an integer $N$, construct an undirected graph with $N$ vertices. Label the vertices $1\ldots N$, and require it to satisfy the following conditions:
    
    -   It is a simple connected graph.
    -   There exists an integer $S$ such that for every vertex, the sum of the indices of its adjacent vertices is $S$.
    
    The input data is guaranteed to have a solution.

??? note "Solution idea"
    By analyzing the cases $n=3,4,5$, we can find a construction idea.
    
    Construct a complete $k$-partite graph, ensuring that these $k$ parts have equal sums. Then the value of $S$ for every vertex is equal, namely $\dfrac{(k-1)\sum_{i=1}^{n}i}{k}$.
    
    If $n$ is even, then we can pair up the numbers from the two ends, i.e. $\{1,n\},\{2,n-1\}\cdots$
    
    If $n$ is odd, then we can take $n$ out as its own group, and pair up the remaining $n-1$ numbers, i.e. $\{n\},\{1,n-1\},\{2,n-2\}\cdots$
    
    The connectivity of the graph constructed this way for $n\ge 3$ is easy to prove and will not be belabored here.
    
    The problem is solved.

### Example 4

???+ note "[BZOJ 4971 "Lydsy1708 Monthly Contest" Remembered Knapsack](https://vjudge.net/problem/BZOJ-4971)"
    After a hard day's work, Little Q fell asleep. In his mind emerged the scene of learning the 0/1 knapsack when he had just entered university; back then, as a freshman, Little Q solved a simple 0/1 knapsack problem. The problem goes like this:
    
    Given $n$ items whose volumes are $v_1,v_2,…,v_n$, compute the number of ways to select some of the items (possibly none) so that the total volume is exactly $w$. Because the answer may be very large, you only need to output the answer modulo $P$.
    
    Because of staying up late doing problems for a long time, he could only see the $w$ and $P$ in the sample input, and that the sample output was $k$; he could not make out how many items there were, nor the volume of each item. Even after he woke up, Little Q never saw $n$ and $v$ clearly. Please write a program to help Little Q reconstruct the past sample input.

??? note "Solution idea"
    This is one of the constructive problems with the highest degree of freedom. This is exactly what leads to being clueless and hard to get started.
    
    First, it is not hard to see that the modulus is a red herring. Since we construct the data freely, we can always keep the number of ways from exceeding the modulus.
    
    Through a curious line of thought, we come up with the idea of constructing $n$ small items of cost $1$ and a few large items of cost greater than $\dfrac{w}{2}$.
    
    Since only one of each large item can be taken, each large item of cost $x$ contributes $\dbinom{n}{w-x}$ to the number of ways.
    
    Let $f_{i,j}$ denote the minimum number of large items when there are $i$ ones and the number of ways is $j$.
    
    Preprocess $f$ with DP; by calculation we know that we only need to preprocess all values for $i\le 20$.
    
    The problem is solved.
