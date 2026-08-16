author: Hope666666

## Introduction

This article introduces the idea of DP nested in DP (DP of DP), and shows through two examples how it applies to concrete problems.

## Idea

The so-called "DP of DP" actually refers to a method that, during dynamic programming, abstracts the solving process of a subproblem (usually a DP) into an automaton (DFA), and then designs a new layer of DP on top of this automaton.

This technique is mainly applied to a class of **sequence-counting**, **probability**, or **expectation** problems. A typical problem has the following structure:

-   Given a character set $\Sigma$ and a set $A\subseteq\Sigma^n$ of "valid sequences" of length $n$ over it. Depending on the character set, sequences may be binary strings, digit strings, state sequences, and so on.
-   For each concrete sequence $s\in\Sigma^n$, one can determine via dynamic programming whether it is valid (i.e. $s\in A$), compute its weight, or find related values.
-   Ultimately, we want to count the number of, total weight of, expected value of, etc., all sequences in the set $A$.

At this point, enumerating all sequences is infeasible. So we consider abstracting the process of "determining whether a sequence is valid" (i.e. the inner DP) into a [deterministic finite automaton](../misc/fsm.md#确定性有限状态自动机) (DFA). Generally, for a fixed sequence $s\in\Sigma^n$, the state function of the inner DP can be expressed as $g(i,x;s)$, i.e. the value of some quantity when the length-$i$ prefix of the sequence $s$ has been processed and the other state components are $x$. Correspondingly, the state-transition equation of the inner DP is

$$
g(i,\cdot;s) = G(g(i-1,\cdot;s),s_i).
$$

That is, the function $g(i,\cdot;s)$ is uniquely determined by the previous function $g(i-1,\cdot;s)$ and the current character $s_i$. If we regard the function $g(i,\cdot;s)$ as a state of the automaton, then the state-transition equation of the inner DP gives a transition of the automaton. Therefore, the automaton $(Q,\Sigma,\delta,q_0,F)$ corresponding to the inner DP has the following structure:

-   The state set $Q$ is the set of functions $g(i,\cdot;s)$ corresponding to all possible $s\in\Sigma^n$ and $i=0,1,\cdots,n$;
-   The transition function $\delta:Q\times\Sigma\to Q$ is the $G$ in the state-transition equation of the inner DP;
-   The start state $q_0$ is usually obvious, namely the initial state of the inner DP;
-   The set of accepting states $F$ corresponds to all valid sequences $s\in A$.

The function $g(i,\cdot;s)$ itself may be quite complex, so when handling concrete problems, one usually needs to use [state compression](./state.md) or combine it with DFA-minimization techniques to compress the state space. This is also the main reason DP of DP can significantly reduce time and space complexity compared with brute-force DP.

After abstracting the inner DP into a DFA, one can design a new DP on this DFA to solve the original problem, i.e. the outer DP. For convenience of description, take a simple counting problem as an example. The state function of the outer DP is defined as $f(i,q)$, i.e. the number of prefixes that, upon processing the length-$i$ prefix, reach state $q\in Q$ in the DFA. Its state-transition equation is

$$
f(i,q) = \sum_{c\in\Sigma}\sum_{q'\in Q:\delta(q',c)=q} f(i-1,q').
$$

The start state is of course $f(0,q_0)$, and the final answer can usually be computed simply from $\{f(n,q):q\in F\}$. The outer DP is actually a special case of [DP on a DAG](./dag.md).

## Examples

The next two examples explain the general approach of DP of DP in detail.

### Example 1

???+ example "[Hero meet devil](https://www.luogu.com.cn/problem/P10614)"
    Given a string $S$ over the character set `ACGT` with $|S|\le 15$. For each $0\leq i \leq |S|$, find how many strings $T$ of length $m$ over the character set `ACGT` have a longest common subsequence with $S$ of length $i$.

??? note "Editorial"
    We first think of a DP: let $f_{i,j}$ denote the number of $T$ of length $i$ whose longest common subsequence with $S$ has length $j$. But this cannot be transitioned; we find the main problem is that we do not know which characters this longest common subsequence corresponds to.
    
    Consider the naive process of computing the longest common subsequence. Let $g_{i,j}$ denote the length of the longest common subsequence of the first $i$ characters of $T$ and the first $j$ characters of $S$; then we have
    
    $$
    g_{i,j} = \max\{g_{i-1,j},g_{i,j-1},g_{i-1,j-1}+[T_i=S_j]\}.
    $$
    
    We find that for a given $i$, we only need to record the value of each position of the one-dimensional array $g_i$ to accurately maintain the state of the longest common subsequence of $S$ and the first $i$ characters of $T$. Since the length of $S$ is only $15$, we find this idea feasible.
    
    So we redefine the state $f_{i,x}$ as the number of $T$ of length $i$ whose DP array with $S$ (i.e. $g_i$) is in state $x$. This DP seems to have many states, but we find $g_{i,j}-g_{i,j-1}\in\{0,1\}$, so we can maintain the difference array of $g_i$, and the number of states is $2^{|S|}$.
    
    Now think about how to transition. It is easy to see that if we know the array $g_i$ and also know $T_{i+1}$, we can compute $g_{i+1}$ via a naive LCS transition (i.e. the DP equation above). So the naive LCS becomes the inner DP that helps $f$ transition.
    
    Therefore, we enumerate $T_{i+1}$, compute the state $x'$ after $x$ transitions, and add $f_{i,x}$ to $f_{i+1,x'}$ to complete the state transition of the outer DP. Finally, we record $\textit{ans}_i$ as the answer for LCS length $i$; enumerate each state $S$ and add $f_{m,S}$ to $\textit{ans}_{\operatorname{popcount}(S)}$.

??? note "Reference code"
    ```cpp
    --8<-- "docs/dp/code/dp-of-dp/dp-of-dp_1.cpp"
    ```

### Example 2

???+ example "[\[ZJOI2019\] Mahjong](https://loj.ac/p/3042)"
    Suppose mahjong tiles have $n$ kinds of ranks, each rank having $4$ tiles. Define a meld as three mahjong tiles of adjacent ranks $i,i+1,i+2$ (a run) or three mahjong tiles of the same rank $i,i,i$ (a triplet), and a pair as two mahjong tiles of the same rank $i,i$. Define a sequence of mahjong tiles as winning if and only if it (viewed as a multiset) can be split into four melds and one pair, or seven distinct pairs. Given $13$ mahjong tiles, ask the expected number of additional tiles to draw so that there exists a winning subsequence.

??? note "Editorial"
    First, for a hand of tiles, we only need to consider the count of each kind of tile, without caring about their order. Therefore, for any prefix of any hand of tiles, we can turn it into a sequence of length $n$ where each position is $0\sim 4$. Initially, the count of the $i$-th tile is $a_i$, which is equivalent to restricting the value of the $i$-th number $x_i$ in the sequence to an integer in $[a_i,4]$. Note that the transformed sequence does not consider the order of drawing tiles, but the sequence of mahjong tiles in the problem does consider order.
    
    Let $X$ denote the minimum number of draws needed to win. Directly computing the expectation $\mathbf E[X]$ is rather difficult; we can consider the following transformation. Let $h_i$ denote the number of sequences that **have not won** after drawing $i$ tiles. Because in its corresponding mahjong-tile sequence these $i$ tiles must precede the remaining $(4n-13-i)$ tiles, but the order of these $i$ tiles and the remaining $(4n-13-i)$ tiles is arbitrary, the number of mahjong-tile sequences that cannot win after drawing only the first $i$ tiles is
    
    $$
    h_i\cdot i!(4n-13-i)!.
    $$
    
    Because the total number of mahjong-tile sequences is $(4n-13)!$, the probability of not winning after drawing only the first $i$ tiles is
    
    $$
    \mathbf P[X>i] = \dfrac{h_i\cdot i!(4n-13-i)!}{(4n-13)!}.
    $$
    
    Using the tail-summation formula, we obtain the desired expectation
    
    $$
    \mathbf E[X] = \sum_{i=0}^\infty\mathbf P[X>i] = 1 + \sum_{i=1}^{4n-13}\dfrac{h_i\cdot i!(4n-13-i)!}{(4n-13)!}.
    $$
    
    At this point, the problem reduces to how to compute $h_i$. We use the DP-of-DP method to solve this.
    
    First, consider the inner DP, i.e. using dynamic programming to determine whether a (transformed) sequence corresponds to a winning hand. The seven-pairs case is relatively easy; we focus on the first winning form. To this end, let $g_{0/1,i,j,k}$ denote the maximum number of melds when the first $i$ kinds of tiles have been processed, there remain $j$ groups of $(i−1,i)$ and $k$ tiles of $i$, and there does/does not exist a pair (i.e. $0/1$). If we run the DP for a sequence and the final $g_{1,n}$ includes a number greater than or equal to $4$, then this sequence is winning.
    
    The state transitions of this DP are rather complex. We discuss them in two steps. Step one: consider the transition of $g_{0/1,i}$. This amounts to saying how the number of melds transitions when we want to add $x_i$ tiles of rank $i$ to the current hand shape without forming a new pair. Clearly, if after adding $x_i$ tiles of rank $i$ we want to obtain $\ell$ runs, $j$ pairs of $(i-1,i)$, and $k$ lone $i$s, then we should transition from $(g_{0/1,i-1})_{\ell,j}$ (this choice maximally avoids waste), and use the remaining tiles $(x_i-\ell-j-k)$ to form as many triplets as possible. Enumerating all possibilities gives the following transition equation:
    
    $$
    \tilde G(g_{0/1,i-1}, x_i)_{j,k} = \max\left\{(g_{0/1,i-1})_{\ell,j} + \ell + \left\lfloor\dfrac{x_i-\ell-j-k}{3}\right\rfloor:\ell+j+k\le x_i\right\}.
    $$
    
    Step two: consider the case where a pair needs to be formed. When adding $x_i$ tiles of rank $i$, there are the following three transitions:
    
    -   Transition $g_{0,i-1}$ plus $x_i$ tiles to $g_{0,i}$;
    -   Transition $g_{1,i-1}$ plus $x_i$ tiles to $g_{1,i}$;
    -   If $x_i\ge 2$, transition $g_{0,i-1}$ plus $x_i-2$ tiles to $g_{1,i}$.
    
    From this, we obtain all the transitions for obtaining $g_i$ by adding $x_i$ tiles to $g_{i-1}$.
    
    Having resolved the state transitions of the inner DP, we can build the **winning automaton**. The transitions of the automaton are the inner-DP transitions above; we also need to consider how to represent each state of the automaton. Each state corresponds to a possible value of $g_i$. It has three dimensions $(0/1,j,k)$. Because the $(i-1,i)$ and $i$ retained in the dimensions corresponding to $j$ and $k$ are for forming future runs, and three identical runs can always be recombined into three triplets, we only need to consider the demand for forming at most $2$ identical runs, so each hand shape only needs to retain at most $2$, i.e. $j,k\in\{0,1,2\}$. Therefore, $g_i$ can be represented as a $2\times 3\times 3$ array. In addition, to maintain the seven-pairs winning shape, we also need to add a counter to each state to indicate the maximum number of pairs that can currently be formed.
    
    The value range of each element of the array $g_i$ may be $\{-\infty\}\cup\mathbf N$, but because any number of melds greater than or equal to $4$ is a win, we can limit each element's value to at most $4$. Since a winning sequence remains a winning sequence after adding any tile, we can use the idea of DFA minimization to compress all winning states into one state. Therefore, for non-winning states, each position's value actually only needs to consider $\{-\infty\}\cup\{0,1,2,3\}$. In the implementation, $-\infty$ is represented by $-1$.
    
    Even so, the number of all possible states is still quite large, totaling $1+7\times 5^{18}$. Enumerating them is not realistic. In fact, the vast majority of these possibilities do not actually appear in a winning automaton. To avoid considering states that do not actually exist, we can use the idea of BFS, starting from the initial state and expanding the states step by step until stopping at winning states. The automaton obtained this way has $N = 2092$ states.
    
    Finally, consider how to DP on the winning automaton (i.e. the outer DP). Let $f_{i,j,k}$ denote the number of sequences that, when processing the $i$-th tile, have drawn $j$ tiles in total and reached state number $k$ on the winning automaton. When transitioning, enumerate the number of draws $0\leq t\leq 4-a_i$, where $a_i$ is the number of $i$ tiles used among the initial $13$ tiles; multiply the previous sequence count by the number of ways to choose $t$ tiles from $4-a_i$ tiles, $\dbinom{4-a_i}{t}$, and accumulate them. Formally, we have:
    
    $$
    f_{i+1,j+t,k'} = \sum_{t=0}^{4-a_i}\dbinom{4-a_i}{t}f_{i,j,k}.
    $$
    
    where $k'=\delta(k,a_i+t)$ denotes the state after adding $a_i+t$ tiles to the automaton's state $k$. After the outer DP ends, we can compute the number of sequences that still have not won after drawing $i$ tiles, i.e.
    
    $$
    h_i=\sum_{j=1}^{N} f_{n,i,j}.
    $$
    
    Substituting into the expression above gives the desired expectation.

??? note "Reference code"
    ```cpp
    --8<-- "docs/dp/code/dp-of-dp/dp-of-dp_2.cpp"
    ```

## Exercises

-   [CF979E Kuro and Topological Parity](https://codeforces.com/problemset/problem/979/E)
-   [\[TJOI2018\] Garden Party](https://loj.ac/p/2575)
-   [\[NOI2022\] Removing Stones](https://loj.ac/p/3848)
