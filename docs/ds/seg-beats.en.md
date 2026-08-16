This article explains the problem of a segment tree handling historical interval extrema mentioned by Ji Ruyang (Jiry) in the [2016 National Training Team paper](https://github.com/OI-wiki/libs/blob/master/%E9%9B%86%E8%AE%AD%E9%98%9F%E5%8E%86%E5%B9%B4%E8%AE%BA%E6%96%87/%E5%9B%BD%E5%AE%B6%E9%9B%86%E8%AE%AD%E9%98%9F2016%E8%AE%BA%E6%96%87%E9%9B%86.pdf).

## Interval extremum

Broadly speaking, an interval extremum operation means taking $\max$ or $\min$ against $x$ for all numbers in the interval $[l,r]$, i.e. $a_i=\max(a_i,x)$ or $a_i=\min(a_i,x)$.

???+ note "[HDU5306 Gorgeous Sequence](https://acm.hdu.edu.cn/showproblem.php?pid=5306)"
    Maintain a sequence $a$ and perform the following operations:
    
    1.  `0 l r t` $\forall l\le i\le r,~ a_i=\min(a_i,t)$.
    2.  `1 l r` output $\max\limits_{i=l}^r a_i$.
    3.  `2 l r` output $\sum\limits_{i=l}^r a_i$.
    
    Multiple test cases, guaranteed $T\le 100,~\sum n,\sum m\le 10^6$.

Taking $\min$ over the interval means only those numbers greater than $t$ are changed. Therefore the object of this operation is no longer the whole interval, but "the numbers greater than $t$ in this interval". So we can have this idea: each node maintains the maximum $Max$, the second maximum $Se$, the interval sum $Sum$, and the count of the maximum $Cnt$ of that interval. Next we consider the operation of taking $\min$ against $t$ over the interval.

1.  If $Max\le t$, obviously this $t$ is meaningless, so return directly;
2.  If $Se<t < Max$, then this $t$ can update the maximum in the current interval. So we add $Cnt(t-Max)$ to the interval sum, then update $Max$ to $t$, and apply a tag.
3.  If $t\le Se$, then at this point you find that you don't know how many numbers are involved in the update. So our strategy is to brute-force recurse downward, and then push up the information.

What is the complexity of this algorithm? Using potential-function analysis, one can obtain that the complexity is $O(m\log n)$. See the paper for the specific analysis.

```cpp
--8<-- "docs/ds/code/seg-beats/seg-beats_1.cpp"
```

???+ note "[BZOJ4695 The Fakest Female Player](https://loj.ac/p/6565)"
    Maintain a sequence $a$ and perform the following operations:
    
    1.  `1 l r x` $\forall l\le i\le r,~ a_i=a_i+x$.
    2.  `2 l r x` $\forall l\le i\le r,~ a_i=\max(a_i,x)$.
    3.  `3 l r x` $\forall l\le i\le r,~ a_i=\min(a_i,x)$.
    4.  `4 l r` output $\sum\limits_{i=l}^r a_i$.
    5.  `5 l r` output $\max\limits_{i=l}^r a_i$.
    6.  `6 l r` output $\min\limits_{i=l}^r a_i$.
    
    $n,m\le 5\times 10^5,~|a_i|\le 10^8$. All type-$1$ operations have $|x|\le 10^3$, and the remaining operations satisfy $|x|\le10^8$.

With the same method, we maintain the maximum, second maximum, count of maximum, minimum, second minimum, count of minimum, and interval sum. Besides this information, we also need to maintain the interval $\max$, interval $\min$, and interval-add tags. Compared with the previous problem, this involves the issue of the order of pushing down tags. We adopt this strategy:

1.  We consider the interval-add tag to be the highest priority, and the other two kinds of tags equal in status.
2.  When adding a $v$ tag to a node, besides using $v$ to update the satellite information and the current node's interval-add tag, we use this $v$ to update the interval $\max$ and interval $\min$ tags.
3.  When taking $\min$ against $v$ on a node (here ignoring the brute-force process, assuming the tag satisfies the addition condition), besides updating the satellite information, we compare it with the interval $\max$ tag. If $v$ is less than the interval $\max$ tag, then all numbers will eventually become $v$, so make the interval $\max$ tag also become $v$. Otherwise leave it alone.
4.  Taking $\max$ against $v$ over the interval is analogous.

When maintaining information, when there is only one number or two numbers, the number sets may overlap, e.g. a number is both the maximum and the second minimum, which needs special handling.

```cpp
--8<-- "docs/ds/code/seg-beats/seg-beats_2.cpp"
```

Jiry proved that the complexity of this algorithm is $O(m\log^2 n)$.

???+ note "Mzl loves segment tree"
    Two sequences $A,B$; initially all numbers in $B$ are $0$. The operations to maintain are:
    
    1.  Do interval $\min$ on $A$
    2.  Do interval $\max$ on $A$
    3.  Do interval add on $A$
    4.  Query the interval sum of $B$
    
    After each operation, if the value of $A_i$ changes, add $1$ to $B_i$. $n,m\le 3\times 10^5$.

First consider the easiest interval-add operation. As long as $x\neq 0$, all numbers in the whole interval change, so just do one interval add on $B$.

For the interval extremum operation, you find that applying and pushing down tags corresponds one-to-one with the $B$ array. Essentially you divide the sequence's numbers into three classes: maximum, minimum, non-extremum, and maintain them separately (except you have not built the specific extremum set, but this does not hinder the maintenance operation). Therefore when applying a tag, just update the information of $B$ along the way (note it is not applying a tag to $B$! it is updating information!). When querying, you query on $A$, and when pushing down tags, update the information of $B$ along the way. After finding the needed node, just return the information of $B$. This operation essentially hands the extremum information to $B$ to maintain. In addition, the number-set overlap problem still needs to be handled.

???+ note "[CTSN loves segment tree](https://www.luogu.com.cn/problem/U180387)"
    Maintain two sequences $a,b$ and perform the following operations:
    
    1.  `1 l r x` $\forall l\le i\le r,~ a_i=\min(a_i,x)$.
    2.  `2 l r x` $\forall l\le i\le r,~ b_i=\min(b_i,x)$.
    3.  `3 l r x` $\forall l\le i\le r,~ a_i=a_i+x$.
    4.  `4 l r x` $\forall l\le i\le r,~ b_i=b_i+x$.
    5.  `5 l r` output $\max\limits_{i=l}^r (a_i+b_i)$.
    
    $n,m\le 3\times 10^5,~|a_i|,|b_i|,|x|\le 10^9$.

We divide the candidate answers $A_i+B_i$ in the interval $[l,r]$ into four classes: neither $A_i$ nor $B_i$ is the interval maximum of sequence $A,B$; $A_i$ is the interval maximum of sequence $A$ but $B_i$ is not the interval maximum of sequence $B$; $A_i$ is not the interval maximum of sequence $A$ but $B_i$ is the interval maximum of sequence $B$; both $A_i$ and $B_i$ are the interval maxima of sequences $A,B$. We may as well set them respectively as $C_{0,0},C_{1,0},C_{0,1},C_{1,1}$. In addition we normally maintain the interval maximum and second maximum of sequences $A,B$. When pushing down the interval-add tag and the $\min$ tag, the handling of the maxima and second maxima of $A,B$ is consistent with the above two example problems. The $\min$ tag on $A$ affects $C_{1,1}$ and $C_{1,0}$, and the tag on $B$ affects $C_{1,1}$ and $C_{0,1}$. Addition on $A,B$ affects all of $C_{0,0},C_{1,0},C_{0,1},C_{1,1}$. Just note the boundary case where $C_{0,0},C_{1,0},C_{0,1}$ do not exist (e.g. the interval $[i,i]$ has only the maxima of $A,B$ and $C_{1,1}$ existing).

Next we need to consider how to maintain $C_{0,0},C_{1,0},C_{0,1},C_{1,1}$ during pushup. We can consider, after completing the update of the maxima of $A,B$, discussing whether the maxima of $A,B$ of the left and right children equal the maxima of $A,B$ of the current node. We take the left child as an example to explain; the right child is handled similarly:

-   When both the maxima of $A,B$ of the left child equal the maxima of $A,B$ of the current node, the left child's $C_{0,0},C_{1,0},C_{0,1},C_{1,1}$ respectively contribute to the current node's $C_{0,0},C_{1,0},C_{0,1},C_{1,1}$.
-   When the left child's $A$ maximum equals the current node's $A$ maximum but the $B$ maxima are unequal, the left child's $C_{1,0},C_{1,1}$ contribute to this node's $C_{1,0}$, and $C_{0,0},C_{0,1}$ contribute to this node's $C_{0,0}$.
-   When the left child's $A$ maximum is unequal to the current node's $A$ maximum but the $B$ maxima are equal, the left child's $C_{0,1},C_{1,1}$ contribute to this node's $C_{0,1}$, and $C_{0,0},C_{1,0}$ contribute to this node's $C_{0,0}$.
-   When neither the maxima of $A,B$ of the left child equal the maxima of $A,B$ of the current node, the left child's $C_{0,0},C_{1,0},C_{0,1},C_{1,1}$ only contribute to this node's $C_{0,0}$.

The $\max(C_{0,0},C_{1,0},C_{0,1},C_{1,1})$ of the interval query result is the desired answer.

Since interval $\min$ and interval add need to be maintained simultaneously, the complexity is still $O(m\log^2 n)$.

```cpp
--8<-- "docs/ds/code/seg-beats/seg-beats_4.cpp"
```

### Summary

In this chapter we gave four example problems, explaining respectively the maintenance of basic interval extremum operations, the priority handling of multiple tags, the idea of number-set classification, and the maintenance of multiple classifications. Essentially the basic idea of handling interval extrema is the classified maintenance and efficient merging of number-set information. In the next chapter, we will discuss problems related to historical interval extrema.

## Historical extremum problems

### Historical extremum is not equal to persistence

Note that the historical extremum problems discussed in this chapter differ from so-called persistent data structures. We call this special kind of problem historical extremum problems. Historical extremum problems can be divided into three classes.

#### Historical maximum

Simply put, the historical maximum of a position is the maximum of the numbers that have ever appeared at the current position. Formally defined, we define an auxiliary array $B$, initially completely identical to $A$. After each operation on $A$, we take $\max$ over the whole array:

$$
\forall i\in[1,n],\ B_i=\max(B_i,A_i)
$$

At this point, we call $B_i$ the historical maximum of this position.

#### Historical minimum

The definition is similar to the historical maximum; after each operation on $A$, we take $\min$ over the whole array. At this point, we call $B_i$ the historical minimum of this position.

#### Historical version sum

The auxiliary array $B$ is initially all $0$. After each operation, we accumulate the whole $A$ array onto the $B$ array

$$
\forall i\in[1,n], \ B_i=B_i+A_i
$$

We call $B_i$ the historical version sum at position $i$.

Next, we divide historical extremum problems into four classes for discussion.

### Problems solvable with tags

???+ note "[CPU Monitor](https://www.luogu.com.cn/problem/P4314)"
    Sequences $A,B$ are initially identical:
    
    1.  Do interval cover $x$ on $A$
    2.  Do interval add $x$ on $A$
    3.  Query the interval $\max$ of $A$
    4.  Query the interval $\max$ of $B$
    
    After each operation, we perform one update, $\forall i\in [1,n],\ B_i=\max(B_i,A_i)$. $n,m\le 10^5$.

Let's first ignore operation 1. Then with only interval-add operations, we maintain a tag $Add$ representing the value added to the current interval; this tag can solve the interval $\max$ problem. Next consider the historical interval $\max$. We define a tag $Pre$ whose meaning is: within the lifecycle of this tag, the historical maximum of the $Add$ tag.

This definition may be relatively vague. So let's first explain the lifecycle of a tag. A tag goes through such a process:

1.  It is established at node $u$.
2.  While node $u$ accepts several new tags, it merges with the new tags (referring to tags of the same kind)
3.  Node $u$'s tag is pushed down to $u$'s children, and $u$'s tag is cleared

We consider that in this process, from step 1 until before step 3 is the lifecycle of node $u$'s tag. After two tags merge, they become the same tag, so their lifecycles also merge (i.e. take the earlier establishment time as the start of the lifecycle). An equivalent statement is the time period from the moment this node's tag was last pushed down to the current moment.

Why define the lifecycle? Using this concept, we can prove: within the lifecycle of a node's tag, its child nodes do not undergo any change, and retain the state from before this lifecycle. The reason is simple, because during this period you have not pushed down the tag.

So you can guarantee that the historical maximum of $Add$ within the current tag's lifecycle can be updated onto the child nodes' tags and information. Because the child nodes' tags and information have not changed during this time period. So when we push $u$'s tag down to its child $s$, it is not hard to find

$$
Pre_s=\max(Pre_s,Pre_u+Add_s),Add_s=Add_u+Add_s
$$

Then the information update is similar; just use the corresponding tag to update.

Next, we consider operation 1.

The interval-cover operation turns all numbers into a single number. After this, whether it is interval add/subtract or cover, the numbers in the whole interval are still the same (unless you end the current tag's lifecycle and push down the tag). Therefore we can regard all tags after the first interval cover as interval-cover tags. That is, a tag's lifecycle is roughly divided into two stages:

1.  Merging of several add/subtract operation tags, having never received a cover tag.
2.  Cover operation tags, with no so-called add/subtract tags (add/subtract tags are converted to cover tags)

So we split this node's Pre tag into $(P_1,P_2)$. $P_1$ represents the maximum add/subtract tag of the first stage; $P_2$ represents the maximum cover tag of the second stage. Using a similar method, we can do tag pushdown and information update for this. The time complexity is $O(m\log n)$ (this problem does not have the operation of taking the extremum against $x$ over the interval~).

```cpp
--8<-- "docs/ds/code/seg-beats/seg-beats_3.cpp"
```
