author: orzAtalod

The content of this part is reproduced and modified from [Time Complexity - A Brief Discussion of Potential Analysis](https://www.luogu.com.cn/blog/Atalod/shi-jian-fu-za-du-shi-neng-fen-xi-qian-tan), with the consent of the original author.

## Definitions

### The Ackermann function

Here, we first give the definition of $\alpha(n)$. To give this definition, we first give the definition of $A_k(j)$.

Define $A_k(j)$ as:

$$
A_k(j)=\left\{
\begin{aligned}
&j+1& &k=0&\\
&A_{k-1}^{(j+1)}(j)& &k\geq1&
\end{aligned}
\right.
$$

i.e. the Ackermann function.

Here, $f^i(x)$ denotes applying $f$ to $x$ $i$ times consecutively, i.e. $f^0(x)=x$, $f^i(x)=f(f^{i-1}(x))$.

Then define $\alpha(n)$ as the smallest integer value making $A_{\alpha(n)}(1)\geq n$. Note that we previously described it as $A_{\alpha(n)}(\alpha(n))\geq n$; either way, they both grow very slowly, with values not exceeding 4.

### Basic definitions

Each node has a rank. The rank here is not the number of nodes, but the depth. A node's initial rank is 0; when merging, if the ranks of the two nodes differ, merge the node of smaller rank onto the node of larger rank without updating the larger node's rank value. Otherwise, randomly merge one node onto the other and increase the root node's rank value by 1. Here the root node's rank gives the height of that tree. Denote x's rank as $rnk(x)$, and similarly denote x's parent as $fa(x)$. We always have $rnk(x)+1\leq rnk(fa(x))$.

To define the potential function, we need to predefine an auxiliary function $level(x)$, where $level(x)=\max(k:rnk(fa(x))\geq A_k(rnk(x)))$. When $rnk(x)\geq1$, define another auxiliary function $iter(x)=\max(i:rnk(fa(x))\geq A_{level(x)}^i(rnk(x))$. The $x$ these functions are defined on all satisfy $rnk(x)>0$ and $x$ is not the root of some tree.

The above definitions may make you a bit dizzy. Let's sort it out again: for an $x$ and $fa(x)$, if $rnk(x)>0$, one can always find a pair $i,k$ such that $rnk(fa(x))\geq A_k^i(rnk(x))$, and $level(x)=\max(k)$; under this premise, $iter(x)=\max(i)$. $level$ describes the maximum iteration level of $A$, and $iter$ describes the maximum number of iterations at the maximum iteration level.

For these two functions, $level(x)$ always increases or stays the same as operations proceed, and if $level(x)$ does not increase, $iter(x)$ also only increases or stays the same. Moreover, they always satisfy the following two inequalities:

$$
0\leq level(x)<\alpha(n)
$$

$$
1\leq iter(x)\leq rnk(x)
$$

Considering the definitions of $level(x)$, $iter(x)$, and $A_k^j$, these are easy to prove and are left to the reader to become familiar with the definitions.

Define the potential function $\Phi(S)=\sum\limits_{x\in S}\Phi(x)$, where $S$ denotes an entire disjoint-set union and $x$ is a node in it. Define $\Phi(x)$ as:

$$
\Phi(x)=
\begin{cases}
\alpha(n)\times \mathit{rnk}(x)& \mathit{rnk}(x)=0\ \text{or}\ x\ \text{is the root of some tree}\\
(\alpha(n)-\mathit{level}(x))\times \mathit{rnk}(x)-iter(x)& \text{otherwise}
\end{cases}
$$

Then we prove that the amortized time complexity is $\Theta(\alpha(n))$ through the potential changes caused by the operations. Note that the $union(x,y)$ operation we discuss here guarantees that both $x$ and $y$ are roots of some tree, so there is no need to additionally perform $find(x)$ and $find(y)$.

We can see that the potential is always a non-negative number. Also, at the start, the potential of the disjoint-set union is $0$.

## Proof

### The union(x,y) operation

Its cost in time is $\Theta(1)$, so we consider the potential change it causes.

Here, we assume $rnk(x)\leq rnk(y)$, i.e. $x$ is attached to $y$. Then the only nodes whose potential increases are $x$ (from root to non-root), $y$ (its rank may increase), and $y$'s children before the operation (their parent's rank may increase). We first prove that the potential of $y$'s child $c$ before the operation cannot increase, and if it decreases, it decreases by at least $1$.

Let $c$'s potential before the operation be $\Phi(c)$ and after be $\Phi(c')$; here $c$ can be any non-root node with $rnk(c)>0$, and the operation can be any operation, including the find operation below. We discuss three cases.

1.  $iter(c)$ and $level(c)$ did not increase. Clearly $\Phi(c)=\Phi(c')$.
2.  $iter(c)$ increased, $level(c)$ did not increase. Here $iter(c)$ increases by at least one, i.e. $\Phi(c')\leq \Phi(c)-1$; the potential function decreased, and by at least 1.
3.  $level(c)$ increased, $iter(c)$ may decrease. But since $0<iter(c)\leq rnk(c)$, $iter(c)$ decreases by at most $rnk(c)-1$, while $level(c)$ increases by at least $1$. By the definition $\Phi(c)=(\alpha(n)-level(c))\times rnk(c)-iter(c)$, we get $\Phi(c')\leq\Phi(c)-1$.
4.  Other cases. Since $rnk(c)$ is unchanged and $rnk(fa(c))$ does not decrease, they do not exist.

So the only nodes whose potential may increase are $x$ or $y$. And $x$ went from root to non-root; if $rnk(x)=0$, then always $\Phi(x)=\Phi(x')=0$. Otherwise, we always have $\alpha(x)\times rnk(x)\geq(\alpha(n)-level(x))\times rnk(x)-iter(x)$, i.e. $\Phi(x')\leq \Phi(x)$.

Therefore, the only point whose potential may increase is $y$. And $y$'s potential increases by at most $\alpha(n)$. Therefore, the amortized time complexity of the $union$ operation is $\Theta(\alpha(n))$.

### The find(a) operation

If the search path contains $\Theta(s)$ nodes, then clearly its search time complexity is $\Theta(s)$. If, due to the search operation, no node's potential increases and at least $s-\alpha(n)$ nodes' potentials decrease by at least $1$, we can prove the time complexity of the $find(a)$ operation is $\Theta(\alpha(n))$. To avoid confusion, here we use $a$ as the parameter, and the $x$ that appear all generically refer to some node in a disjoint-set union.

First we prove that no node's potential increases. Clearly, we proved above that the potential of all non-root nodes does not increase, and the root node's $rnk$ did not change, so no node's potential increases.

Next we prove that at least $s-\alpha(n)$ nodes' potentials decrease by at least $1$. We proved above that if $level(x)$ or $iter(x)$ changes, their potential decreases by at least $1$. So we only need to prove that at least $s-\alpha(n)$ nodes' $level(x)$ or $iter(x)$ change.

Recall the definition of a non-root node's potential, $\Phi(x)=(\alpha(n)-level(x))\times rnk(x)-iter(x)$, where $level(x)$ and $iter(x)$ are the largest numbers making $rnk(fa(x))\geq A_{level(x)}^{iter(x)}(rnk(x))$.

So, if $root_x$ denotes the root of the tree $x$ is in, we only need to prove $rnk(root_x)\geq A_{level(x)}^{iter(x)+1}(rnk(x))$. By the definition of $A_k^i$, $A_{level(x)}^{iter(x)+1}(rnk(x))=A_{level(x)}(A_{level(x)}^{iter(x)}(rnk(x)))$.

Note that we may use $k(x)$ to denote $level(x)$ and $i(x)$ to denote $iter(x)$ to avoid overly long expressions. Here it is $rnk(root_x)\geq A_{k(x)}(A_{k(x)}^{i(x)}(x))$.

When you get here, you may have a feeling of "what is this thing". This means you may need to read it a few more times, or skip some content and read it later.

Here, we need an external $A_{k(x)}$, meaning we may need to find another point $y$. Let $y$ be the point on the search path after $x$ satisfying $k(y)=k(x)$; here "after on the search path" is equivalent to "is an ancestor of $x$". Clearly, not every $x$ has such a $y$. It is easy to prove that the number of $x$ without such a $y$ does not exceed $\alpha(n)+2$, because only the last $x$ for each $k$, as well as $a$ and $root_a$, have no such $y$.

We emphasize again that $fa(x)$ refers to $x$'s parent **before** path compression; $x$'s parent **after** path compression is uniformly denoted $root_x$. For each $x$ that has a $y$, we always have $rnk(y)\geq rnk(fa(x))$. At the same time, we have $rnk(fa(x))\geq A_{k(x)}^{i(x)}(rnk(x))$. Since $k(x)=k(y)$, we use $k$ to refer to both, i.e. $rnk(fa(x))\geq A_k^{i(x)}(rnk(x))$. We need to build an $A_k$, so we can ignore the value of $iter(y)$ and directly use the weakened version $rnk(fa(y))\geq A_k(rnk(y))$.

If we combine the inequalities, something magical happens. We find that $rnk(fa(y))\geq A_k^{i(x)+1}(rnk(x))$. That is, to iterate from $rnk(x)$ to $rnk(fa(y))$, one can iterate $A_k$ at least $i(x)+1$ times without exceeding $rnk(fa(y))$.

Clearly, $rnk(root_y)\geq rnk(fa(y))$, and $rnk(x)$ is unchanged during path compression. Therefore, we obtain $rnk(root_x)\geq A_k^{i(x)+1}(rnk(x))$, i.e. the value of $iter(x)$ increases by at least 1; if $rnk(x)$ did not increase, then $level(x)$ must have increased.

So $\Phi(x)$ decreased by at least 1. Since there are at least $s-\alpha(n)-2$ such nodes $x$, in the end $\Phi(S)$ decreased by at least $s-\alpha(n)-2$, and the amortized time complexity is $\Theta(\alpha(n)+2)=\Theta(\alpha(n))$.

## Why a disjoint-set union can be adversarially exploited

This question asks: if we do not merge by rank, which properties are broken, causing the time complexity of the disjoint-set union to fail to be guaranteed as $\Theta(m\alpha(n))$.

If, when merging, the node of larger $rnk$ is merged onto the node of smaller $rnk$, we set the $rnk$ value of that smaller-$rnk$ node to the other node's $rnk$ value plus one. This way, we can guarantee $rnk(fa(x))\geq rnk(x)+1$, so a "compile error everywhere"-like property violation does not occur.

Clearly, if we do this, what we break is the sentence "$y$'s potential increases by at most $\alpha(n)$" in the $union(x,y)$ function.

There exists a structure that can lower the time complexity of a path-compression disjoint-set union to $\Omega(m\log_{1+\frac{m}{n}}n)$, defined as follows:

A binomial tree (actually somewhat different from the usual binomial tree), where j is a constant, and $T_k$ is a $T_{k-1}$ plus a $T_{k-j}$ as a child of the root.

![binomial tree](./images/dsu-complexity.svg)

Boundary condition: $T_1$ to $T_j$ are all single points.

Let $rnk(T_k)=r_k$; here we have $r_k=(k-1)/j$ (proof omitted). Each round of operations, we attach it to a single node and then query the bottom $j$ nodes. That is, when we attach to the single node, the single node's potential increases by $(k-1)/j+1$. When $j=\lfloor\frac{m}{n}\rfloor$, $i=\lfloor\log_{j+1}\frac{n}{2}\rfloor$, $k=ij$, the potential increase is:

$$
\alpha(n)\times((ij-1)/j+1)=\alpha(n)\times((\lfloor\log_{\lfloor\frac{m}{n}\rfloor+1}\frac{n}{2}\rfloor\times \lfloor\frac{m}{n}\rfloor-1)/\lfloor\frac{m}{n}\rfloor+1)
$$

Transforming it and removing all the floor symbols, we can derive that the potential increase $\geq \alpha(n)\times(\log_{1+\frac{m}{n}}n-\frac{n}{m})$, and $m$ operations is $\Omega(m\log_{1+\frac{m}{n}}n-n)=\Omega(m\log_{1+\frac{m}{n}}n)$.

## About heuristic merging

Since merging by rank is harder to write than heuristic merging, many experts choose to write the disjoint-set union with heuristic merging. Specifically, this maintains a $size(x)$ for each root and each time merges the one with smaller $size$ onto the one with larger $size$.

So can heuristic merging be adversarially exploited?

First, we can explain from the properties in which rank participates in the proof. If $size$ can replace the role of $rnk$, then heuristic merging can be used. To summarize quickly, the properties in which rank participates in the proof are the following three:

1.  Each merge, at most one node's rank rises, and it rises by at most 1.
2.  Always $rnk(fa(x))\geq rnk(x)+1$.
3.  A node's rank does not decrease.

Regarding the second and third, $siz$ clearly satisfies them; however, the first is not satisfied: if $x$ is merged onto $y$, then $siz(y)$ increases by $siz(x)$.

So we can consider using $\log_2 siz(x)$ to replace $rnk(x)$.

Regarding the first property, since a node's $siz$ at most doubles, $\log_2 siz(x)$ rises by at most 1. Regarding the second and third properties, the conclusions are relatively obvious, and the proofs are omitted here.

So, if you do not want to write merging by rank, just write heuristic merging; the time complexity is still $\Theta(m\alpha(n))$.
