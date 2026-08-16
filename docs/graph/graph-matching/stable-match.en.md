## Introduction

The **stable matching problem** is a classic problem in combinatorial optimization and cooperative game theory. Compared with the traditional graph-theory matching problem, stable matching introduces the constraints of individual preferences and stability, which makes the algorithm design rely more on preference orderings rather than purely the graph structure. In the model of the stable matching problem, each individual has preferences for potential matching objects, and the stable matching problem hopes to establish a stable matching relationship among them. In a stable matching, there does not exist any group of individuals that would collude to deviate from the current matching result because they can get a better choice. Stable matching and its related problems are widely applied in scenarios such as labor markets, school admissions, and medical resource allocation.

The stable matching problem that most commonly appears in algorithm competitions is one-to-one matching in a two-sided market, i.e. the stable marriage problem. This article will focus on introducing the stable marriage problem and its algorithm.

## Stable marriage problem

The stable marriage problem is the earliest-studied stable matching problem. Similar to bipartite matching, it can be described as a matching problem in the marriage market: suppose there are several men and women, each person has a preference ordering for the opposite sex, and the goal is to find a matching way such that there is no pair of a man and a woman who would rather abandon their respective matching objects and choose each other.

### Problem description

The matching market is composed of several men $M$ and several women $W$. Each person has a strict preference ordering for the opposite sex:

-   For each man $m\in M$, there exists a strict total order $\preceq_m$ on the set $W\cup\{m\}$;
-   For each woman $w\in W$, there exists a strict total order $\preceq_w$ on the set $M\cup\{w\}$.

Besides comparing among the opposite sex, each person also adds themselves to this preference ordering. This means that this person will only accept matching with a member of the opposite sex ranked ahead of themselves; these members of the opposite sex are called **acceptable**. Obviously, the preference ordering of unacceptable members of the opposite sex is insignificant; in principle, one only needs to give the preference ordering among the acceptable members of the opposite sex. So, these preferences with unacceptable members of the opposite sex are also called preferences with incomplete lists.

???+ example "Example"
    Suppose $m$ is a man, $w_1,w_2,w_3$ are three women, and the preference relation $w_1\prec_m m \prec_m w_2\prec_m w_3$ holds. Then, man $m$ prefers being single over matching with woman $w_1$; prefers matching with woman $w_2$ over being single; prefers matching with woman $w_3$ over matching with woman $w_2$. For man $m$, woman $w_1$ is unacceptable, and women $w_2,w_3$ are acceptable.

A **matching** $\mu:M\cup W\rightarrow M\cup W$ in the market needs to satisfy the following properties:

-   Each person can only match a member of the opposite sex or themselves, i.e. for all $m\in M$, $\mu(m)\in W\cup\{m\}$, and for all $w\in W$, $\mu(w)\in W\cup\{w\}$.
-   The matching is mutual, i.e. for all $i\in M\cup W$, $i = \mu(\mu(i))$.

A matching $\mu$ may have two kinds of instability factors:

-   If there exists an individual $i\in M\cup W$ such that $\mu(i)\prec_i i$, that is, relative to the current matching object, individual $i$ would rather be single, then $i$ is called a **blocking individual** of the matching $\mu$.
-   If there exists a pair of the opposite sex $m\in M$ and $w\in W$ such that $\mu(m)\prec_m w$ and $\mu(w)\prec_w m$, that is, relative to their respective current matching objects, man $m$ and woman $w$ prefer to be together, then $(m,w)$ is called a **blocking pair** of the matching $\mu$.

If a matching $\mu$ has neither a blocking individual nor a blocking pair, then the matching $\mu$ is called **stable**. In a stable matching, no one can break the current situation: single people cannot find anyone willing to be with them; married people are neither willing to divorce and be single, nor can find anyone willing to elope with them.

The stable matching problem asks: for any given set of preference orderings, does a stable matching always exist? If so, how to find such a stable matching?

### Gale–Shapley algorithm

Gale and Shapley proposed the **deferred acceptance algorithm** in 1962, which can find a stable matching for any given set of preference orderings. Therefore, a stable matching must exist.

The Gale–Shapley algorithm has two symmetric versions, one where men propose and one where women propose. Taking the man-proposing Gale–Shapley algorithm as an example, the algorithm process is as follows:

1.  At the start of the algorithm, each woman is regarded as holding onto the proposal from herself, and each man is marked as active.
2.  An active man will propose to the woman he likes most among the women who are acceptable to him but to whom he has not yet proposed; if such a woman does not exist, no operation is needed. Whether or not he proposes, mark all men as inactive.
3.  A woman who receives a new proposal will compare them with her previously-held proposal, keep only the one she likes most (which may be herself), and reject all other proposals. Restore the rejected men to being marked as active.
4.  Repeat the previous two steps until there is no active man. At this point, women accept their currently-held proposals. The matching result thus obtained is a stable matching.

Since each man proposes to each woman at most once, the algorithm must end within $O(|M||W|)$ time.

The reference implementation is as follows:

??? example "Template problem [SPOJ STABLEMP - Stable Marriage Problem](https://www.spoj.com/problems/STABLEMP/) reference implementation"
    ```cpp
    --8<-- "docs/graph/code/graph-matching/stable-match/stable-match.cpp"
    ```

### Properties of stable matching

Stable matching has good theoretical properties. First, the Gale–Shapley algorithm constructively proves that a stable matching must exist.

???+ note "Theorem 1 (Gale and Shapley, 1962)"
    The Gale–Shapley algorithm obtains a stable matching. Therefore, a stable matching exists.

??? note "Proof"
    A man will not propose to a woman he does not accept, and a woman will immediately reject a proposal from a man she does not accept. Therefore, the men and women who finally match each other must be mutually acceptable, and there cannot be a blocking individual. To prove that it is a stable matching, we only need to show that there is no blocking pair.
    
    Proof by contradiction. Suppose $(m,w)$ is a blocking pair. Then, before man $m$ proposes to $\mu(m)$, he must have already proposed to $w$. But, since woman $w$ rejected $m$, she must have received a proposal from someone she likes more, $m'$. If $m'\neq \mu(w)$, then woman $w$ only prefers $\mu(w)$ over $m'$. From this, relative to $m$, woman $w$ must prefer the final matching object $\mu(w)$. This contradicts $(m,w)$ being a blocking pair. So, the matching is stable.

???+ note "Corollary"
    If $|M|=|W|$ and all members of the opposite sex are acceptable, then a stable perfect matching exists.

In the Gale–Shapley algorithm, men can propose or women can propose. Generally, the stable matchings obtained by these two versions of the Gale–Shapley algorithm are not the same. In fact, the stable matching obtained by the man-proposing Gale–Shapley algorithm is, among all stable matchings, the most favorable for men; and vice versa.

???+ note "Theorem 2 (Gale and Shapley, 1962)"
    Let $\mu_M$ and $\mu_W$ be the stable matchings obtained by the man-proposing and woman-proposing Gale–Shapley algorithms respectively. For any stable matching $\mu$, $\mu(m)\preceq_m\mu_M(m)$ holds for all $m\in M$, and $\mu(w)\preceq_w\mu_W(w)$ holds for all $w\in W$.

??? note "Proof"
    By symmetry, we only need to prove $\mu(m)\preceq_m\mu_M(m)$ for all $m\in M$. For this, still consider the man-proposing Gale–Shapley algorithm, and denote $k(m,w)$ as the round to which the algorithm has proceeded when woman $w$ rejects man $m$'s proposal. This round is well-defined for all $(m,w)$ satisfying $\mu_M(m)\prec_m w$.
    
    Suppose $\mu_M$ is not the most favorable for all men, that is, there exists a stable matching $\mu$ and a man $m\in M$ such that $\mu_M(m)\prec_m\mu(m)$ holds. Since the matching $\mu_M$ is stable, we have $m\preceq_m\mu_M(m)\prec_m\mu(m)$, so $\mu(m)$ is a woman, and there must be a well-defined $k(m,\mu(m))$. So, we may as well assume $m$ is exactly the one among all such men with the smallest $k(m,\mu(m))$. Suppose during the algorithm process, when woman $w=\mu(m)$ rejects man $m$, she holds onto man $m'$'s proposal, that is, $m=\mu(w)\prec_w m'$. Since $\mu$ is a stable matching, $(w,m')$ cannot be a blocking pair, and there is $\mu(m')\neq w$, so $w\prec_{m'}\mu(m')$. Since during the Gale–Shapley algorithm process, woman $w$ may not hold onto $m'$'s proposal until the end, $\mu_M(m')\preceq_{m'}w\prec_{m'}\mu(m')$. At this point, $k(m',\mu(m'))$ is well-defined. Moreover, since $w\prec_{m'}\mu(m')$, only after woman $\mu(m')$ rejects $m'$'s proposal will $w$ hold onto $m'$'s proposal, that is, $k(m',\mu(m')) < k(m,\mu(m))$. This contradicts the choice of $m$. So, by proof by contradiction, $\mu_M$ is the most favorable stable matching for all men.

A matching market may have an exponential number of stable matchings. Let $\mathcal S$ be the set of all stable matchings. On this set, two partial orders can be defined:

-   $\mu_1\preceq_M\mu_2$ if and only if $\mu_1(m)\preceq_m\mu_2(m)$ holds for all $m\in M$;
-   $\mu_1\preceq_W\mu_2$ if and only if $\mu_1(w)\preceq_w\mu_2(w)$ holds for all $w\in W$.

These two partial orders respectively indicate that the matching result is better for all men and for all women. Generally, two stable matchings are not necessarily comparable. But, any two stable matchings induce the decomposition shown in the figure, such that in the three parts obtained by the decomposition, $\mu_1\preceq_M\mu_2$, $\mu_1=\mu_2$, and $\mu_2\preceq_M\mu_1$ hold respectively. Note that although not directly drawn, the part where $\mu_1=\mu_2$ actually includes the case of matching to oneself (i.e. unmatched).

![](./images/stable-match-decompose.svg)

This decomposition relies on the following lemma:

???+ note "Lemma (Knuth, 1976)"
    Let $\mu_1$ and $\mu_2$ be two stable matchings. Let $M(\mu_i)=\{m\in M : \mu_j(m)\prec_m\mu_i(m)\}$ and $W(\mu_i)=\{w\in W:\mu_j(w)\prec_w\mu_i(w)\}$ be the sets of men and women who prefer the matching result in $\mu_i$ respectively, where $i,j=1,2$ and $i\neq j$. Then, $\mu_1$ and $\mu_2$ are both bijections between $M(\mu_1)$ and $W(\mu_2)$, and are both bijections between $M(\mu_2)$ and $W(\mu_1)$.

??? note "Proof"
    Let $m\in M(\mu_1)$. Since $m\preceq_m \mu_2(m)\prec_m\mu_1(m)$, $\mu_1(m)\in W$. Let $w=\mu_1(m)$. Because $\mu_2(w)\neq m$, and $\mu_2(w)\prec_w m$ would mean $(m,w)$ is a blocking pair of $\mu_2$, so $\mu_1(w)=m\prec_w\mu_2(w)$. That is, $w\in W(\mu_2)$. This shows $\mu_1(M(\mu_1))\subseteq W(\mu_2)$. By symmetry, we can also establish $\mu_2(W(\mu_2))\subseteq M(\mu_1)$. Since both $\mu_1$ and $\mu_2$ are injections, $|M(\mu_1)|=|W(\mu_2)|$ and both mappings are surjections. This shows that $\mu_1$ and $\mu_2$ are both bijections between $M(\mu_1)$ and $W(\mu_2)$. Similarly, they are both bijections between $M(\mu_2)$ and $W(\mu_1)$.

This lemma shows that the posets $(\mathcal S,\preceq_M)$ and $(\mathcal S,\preceq_W)$ are [duals](../../math/order-theory.md#对偶) of each other. Moreover, under each partial order, the set $\mathcal S$ constitutes a [lattice](../../math/order-theory.md#有向集与格). Because $\mathcal S$ is finite, these two lattices must have a maximum element and a minimum element. These two extreme elements are exactly the stable matchings obtained by the two versions of the Gale–Shapley algorithm mentioned earlier.

???+ note "Theorem 3 (Conway and Knuth, 1976)"
    The posets $(\mathcal S,\preceq_M)$ and $(\mathcal S,\preceq_W)$ are mutually dual lattices. Moreover, $\mu_M$ and $\mu_W$ are the maximum element and minimum element of $(\mathcal S,\preceq_M)$ respectively, and the minimum element and maximum element of $(\mathcal S,\preceq_W)$ respectively.

??? note "Proof"
    By the lemma, it is easy to show that the two posets are dual. If $\mu_1\preceq_M\mu_2$, this shows $M(\mu_1)=\varnothing$; by the lemma, $W(\mu_2)=\varnothing$, which is $\mu_2\preceq_W\mu_1$. And vice versa. This shows the two are mutually dual. Combining with Theorem 2 above, we obtain that $\mu_M$ and $\mu_W$ are the extreme elements of the two posets. What also needs to be proved in the proposition is that the two posets are lattices. By symmetry, we only need to prove that $(\mathcal S,\preceq_M)$ is a lattice. Then, by the symmetry of the meet and join operations, we only need to prove that the join of stable matchings is still a stable matching. Formally, for any $\mu_1,\mu_2\in\mathcal S$, we need to prove that the matching $\mu=\mu_1\lor_M\mu_2$ satisfying $\mu(m)=\mu_1(m)\lor_m\mu_2(m)$ for all $m\in M$ is a stable matching, where $\lor_m$ is the join operation under the total order $\preceq_m$ (i.e. the one $m$ prefers between the two).
    
    We still use the notation in the lemma. For $i\in M(\mu_1)\cup W(\mu_2)$, $\mu(i)=\mu_1(i)$; otherwise, $\mu(i)=\mu_2(i)$. Since both $\mu_1$ and $\mu_2$ are stable, there is no blocking individual, and $\mu$ is likewise. Suppose $(m,w)$ is a blocking pair of $\mu$. If $m\in M(\mu_1)$, then $\mu_2(m)\prec_m\mu_1(m)=\mu(m)\prec_m w$. At this point, if $w\in W(\mu_2)$, then $\mu_1(w)=\mu(w)\prec_w m$, so $(m,w)$ is a blocking pair of $\mu_1$, a contradiction; otherwise, $w\in W\setminus W(\mu_2)$, and $\mu_2(w)=\mu(w)\prec_w m$, so $(m,w)$ is a blocking pair of $\mu_2$, also a contradiction. Similarly, the case $m\in M\setminus M(\mu_1)$ can only derive a contradiction. By proof by contradiction, such a blocking pair does not exist. So, $\mu_1\lor_M\mu_2$ is a stable matching. The proposition is proved.

Finally, in all stable matchings, the set of unmatched men and women is fixed.

???+ note "Theorem 4 (McVitie and Wilson, 1970)"
    Let $\mu_1$ and $\mu_2$ be two stable matchings. Then, the fixed-point sets of $\mu_1$ and $\mu_2$ are the same.

??? note "Proof"
    Suppose there exists $m\in M$ such that $\mu_1(m)=m$ and $\mu_2(m)\neq m$ holds for some $\mu_1,\mu_2\in\mathcal S$. At this point, $m\in M(\mu_2)$. By the lemma, $m=\mu_1(m)\in W(\mu_1)$, which contradicts $m\in M$. So, there is no such $m\in M$. Similarly, there is no such $w\in W$. So, the fixed-point sets of any two stable matchings must be the same.

Besides these properties discussed in this section, stable matching also has some good strategic properties. Regarding this content, refer to the literature provided at the end of the article.

## Related problems

Stable matching and similar problems also appear in many other contexts.

### College admissions problem

If the one-to-one matching constraint in the stable marriage problem is relaxed to allow many-to-one matching, we obtain the **college admissions problem**. At this point, a college can admit multiple students, as long as the admission quota is not exceeded; but a student is still only allowed to enter at most one college to study. Similar contexts also appear in scenarios such as company recruitment and hospitals admitting intern doctors.

For this kind of problem, the Gale–Shapley algorithm is still applicable. For example, in the student-applying Gale–Shapley algorithm, a college can maintain a waitlist of length not exceeding the quota, and each time, as long as the number of applications exceeds the quota, reject the worst student's application. The earlier discussion of the properties of stable matching is still applicable to this scenario. In particular, the version corresponding to Theorem 4 is that in all stable matchings, the number of students a school can admit is fixed. This is also called the **rural hospitals theorem**. Because it means that no matter how the matching mechanism is changed, as long as the obtained result is stable, those rural hospitals that cannot fill their doctor positions will forever be unable to recruit people.

### Stable roommates problem

If the condition in the stable marriage problem that only members of the opposite sex can be matched is relaxed, we obtain the **stable roommates problem**. At this point, initially there are only several students, who need to be paired up two by two to become roommates. For this kind of problem, a stable matching does not necessarily exist. Irving proposed in 1985 an algorithm that can solve this problem in $O(n^2)$ time.

### House allocation problem

In the stable marriage problem, two groups of individuals have preferences for each other, so it is a two-sided matching problem. Besides this, one-sided matching problems can also be considered. A common scenario is the **house allocation problem**. There are $n$ residents, each owning a house. Each person has a strict preference for all houses. Now, these houses are to be reallocated to these residents, requiring that no resident be allocated a house worse than the initial one, and that there does not exist any number of residents who can privately exchange properties to obtain a more satisfactory outcome. For this problem, it can be solved by the Top Trading Cycle algorithm in $O(n^2)$ time. This kind of problem also appears in scenarios such as kidney transplants.

## Exercises

-   [UOJ 41. 【Tsinghua Training 2014】Matrix Transformation](https://uoj.ac/problem/41)
-   [Codeforces 1147 F. Zigzag Game](https://codeforces.com/problemset/problem/1147/F)

## References and notes

-   [What is an algorithm: how to find a stable marriage pairing - Matrix67](https://matrix67.com/blog/archives/2976)
-   [Gale–Shapley algorithm: finding a stable matching in a bipartite graph](https://reimuyk.github.io/2021-03-24-Gale-Shapley-Algorithm/)
-   [Stable matching problem - Wikipedia](https://en.wikipedia.org/wiki/Stable_matching_problem)
-   [Lattice of stable matchings - Wikipedia](https://en.wikipedia.org/wiki/Lattice_of_stable_matchings)
-   [Stable roommates problem - Wikipedia](https://en.wikipedia.org/wiki/Stable_roommates_problem)
-   [Top trading cycle - Wikipedia](https://en.wikipedia.org/wiki/Top_trading_cycle)
-   [Stable matching: Theory, evidence, and practical design - the 2012 Nobel Prize in Economics](https://www.nobelprize.org/uploads/2018/06/popular-economicsciences2012.pdf)
-   [Notes on Matching and Market Design by Xiang Sun](https://www.xiangsun.org/wp-content/uploads/2013/02/notes-2015-matching.pdf)
-   Gale, David, and Lloyd S. Shapley. "College admissions and the stability of marriage." The American mathematical monthly 69, no. 1 (1962): 9-15.
-   Irving, Robert W. "An efficient algorithm for the stable roommates problem." Journal of Algorithms 6, no. 4 (1985): 577-595.
-   Knuth, Donald Ervin. "Marriages stables." Technical report (1976).
-   McVitie, David G., and Leslie B. Wilson. "Stable marriage assignment for unequal sets." BIT Numerical Mathematics 10, no. 3 (1970): 295-309.
-   Roth, Alvin E., and Marilda Sotomayor. "Two-sided matching." Handbook of game theory with economic applications 1 (1992): 485-541.
-   Roth, Alvin E. "Deferred acceptance algorithms: History, theory, practice, and open questions." international Journal of game Theory 36, no. 3-4 (2008): 537-569.
