## Definition

The drawer principle, also known as the pigeonhole principle.

It is often used for existence proofs and for finding the solution in the worst case.

## Simple case

If $n+1$ objects are divided into $n$ groups, then at least one group has two (or more) objects.

This theorem looks fairly obvious; the proof method considers proof by contradiction: if each group has at most $1$ object, then there are at most $1\times n$ objects, whereas in reality there are $n+1$ objects, a contradiction.

## Generalization

If $n$ objects are divided into $k$ groups, then there exists at least one group containing greater than or equal to $\left \lceil \dfrac{n}{k} \right \rceil$ objects.

The generalized form can also be proved by contradiction: if each group contains fewer than $\left \lceil \dfrac{n}{k} \right \rceil$ objects, then their total $S\leq (\left \lceil \dfrac{n}{k} \right \rceil -1 ) \times k=k\left\lceil \dfrac{n}{k} \right\rceil-k < k(\dfrac{n}{k}+1)-k=n$, a contradiction.

In addition, the partition can be weakened to a cover without changing the conclusion.  
Given a set $S$, a family $\{A_1,A_2\ldots A_k\}$ composed of non-empty subsets of $S$

-   if it satisfies $\bigcup_{i=1}^k A_i$, it is called a cover of $S$
-   if a cover further satisfies $i\neq j\to A_i\cap A_j=\varnothing$, it is called a partition of $S$.

The pigeonhole principle can be stated as follows: for a cover $\{A_1,A_2\ldots A_k\}$ of $S$, there is at least one set $A_i$ satisfying $\left\vert A_i \right\vert \geq \left\lceil \dfrac{\left\vert S \right\vert}{k} \right\rceil$.

## References

-   [Wikipedia: Pigeonhole principle](https://en.wikipedia.org/wiki/Pigeonhole_principle)
-   *Discrete Mathematics and Its Applications*: Chapter 6, Section 1
