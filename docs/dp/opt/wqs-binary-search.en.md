## Introduction

This article introduces the method of optimizing dynamic-programming problems using WQS binary search. In different articles, it is also often called weighted binary search, convex-optimization DP, convex-complete-monotonicity DP, the Lagrange multiplier method, etc.; abroad it is also called the Aliens Trick. It was first summarized by Wang Qinshi in the article "An Analysis of a Class of Binary-Search Methods".

WQS binary search is usually used to solve a class of optimization problems: they have a count restriction and are relatively costly to solve directly; but once this restriction is removed, the problem itself becomes much easier.

For example, suppose the problem to be solved is to select $m$ out of $n$ items and optimize some relatively complex objective function. If we let $f(i,j)$ be the optimal value of the objective function when selecting $j$ items out of the first $i$ items, then the answer to the original problem is $f(n,m)$. In this kind of problem, the state-transition equation is usually two-dimensional. Directly implementing this state-transition equation has time complexity $O(nm)$, which is hard to accept.

Further suppose the optimization problem without the count restriction is easy to solve. But the optimal count selected does not necessarily satisfy the original problem's count restriction. Suppose too many items are selected. Then we can consider attaching a fixed penalty $k$ (the "weight" in "weighted binary search") to each selected item when selecting items, and still solve the optimization problem without the count restriction. Depending on the value of $k$, the optimal count selected will differ; moreover, as $k$ changes, the optimal count selected changes monotonically. So we can use binary search to find the $k$ that makes the optimal count selected exactly $m$. Suppose the optimal value of the objective function is $f_k(n)$ at this point; then, as long as we cancel out the value loss caused by the extra attached penalty, we obtain the answer to the original problem $f(n,m)=f_k(n)+km$. Suppose the complexity of solving the penalty-attached problem once is $O(T(n))$; then the overall complexity of the algorithm is reduced to $O(T(n)\log L)$, where $O(\log L)$ is the number of times needed to binary-search $k$.

This is the basic idea of WQS binary search. But for this idea to work, the premise is that $f(n,m)$ is convex in $m$. Otherwise, there may not exist an attached penalty $k$ that makes the optimal count exactly $m$. This is also why this DP-optimization method is often called "convex-optimization DP" or "convex-complete-monotonicity DP".

## The traditional method

Let the non-empty set $X$ be the (finite) decision space, $f:X\rightarrow\mathbf R$ the objective function, and additionally a function $g:X\rightarrow\mathbf R^d$ used to impose a restriction. The problem to be solved can be seen as computing the value function $v(y)$ of the following optimization problem at some point:

$$
\begin{aligned}
v(y)=\min_{x\in X}\;&f(x)\\
\text{subject to }&g(x)=y.
\end{aligned}
$$

For example, for the count-restricted problem mentioned earlier, $X$ can be understood as the family of subsets of the set of all items, $x\in X$ is a single subset, $f(x)$ is the value function of a single subset, and $g(x)$ is the number of elements in the subset $x$. Of course, $g(x)$ is not necessarily a count restriction; examples of more general restrictions are provided later.

???+ info "Convention"
    For convenience of writing, this article only discusses problems that minimize the objective function. Problems that maximize the objective function are similar, except one needs to correspondingly replace the (lower-)convex functions in this article with concave functions (also called upper-convex functions). Alternatively, one can, by adding a negative sign, turn the problem of maximizing the objective function into the problem of minimizing its negation.

### Geometric intuition

Because most problems encountered in competitive programming are combinatorial-optimization problems, the decision space $X$ usually has no good structure, so we can instead examine the set

$$
\mathcal D = \{(g(x),f(x))\in\mathbf R\times\mathbf R^d:x\in X\}.
$$

The traditional method mainly solves the case $d=1$, i.e. the case with only one restriction. The figure below provides a possible illustration of the point set $\mathcal D$ in this case.

![](../images/wqs-binary-search/wqs-f-g-space.svg)

The red points and blue points in the figure are the set $\mathcal D$ obtained by projecting all possible choices in $X$ onto the plane $(g(x),f(x))$. So what the original problem asks for is the minimum ordinate $v(y)$ among the points with abscissa $y$. As $y$ varies, all such points $(y,v(y))$ constitute the set of red points in the figure.

To find the ordinate of the point $(y,v(y))$, we can consider cutting the set $\mathcal D$ with a line of slope $\lambda\in\mathbf R$. As shown in the figure, when the slope of the line is chosen appropriately, the line passing through the point $(y,v(y))$ has, among all lines of slope $\lambda$ passing through the points of the set $\mathcal D$, the smallest intercept $f(x)-\lambda g(x)$. Denote this minimum as

$$
h(\lambda) = \min_{x\in X}f(x)-\lambda g(x).
$$

Then, because $(y,v(y))$ is also on this line, we obtain the solution to the original problem

$$
v(y) = h(\lambda) + \lambda y.
$$

Suppose that for all $\lambda$ in a reasonable range, the above function $h(\lambda)$ is easy to solve. This is often the case in competitive programming, because it removes the restriction of the original problem. Then, the two most important problems now faced are

1.  whether there exists such a line slope $\lambda$ that its minimum intercept is attained exactly at the point $(y,v(y))$, and
2.  if it exists, how to find such a slope $\lambda$.

The first problem is relatively easy to solve. Because as the line slope $\lambda$ changes, the set cut out by all these lines (i.e. the intersection of their corresponding upper half-planes) is necessarily a convex set. Therefore, these lines can pass through a certain point if and only if this point is on the lower convex hull of this convex set. This is equivalent to saying that the function $v(y)$ is a [convex function](./slope-trick.md#convex-functions-on-discrete-point-sets).

The second problem is more subtle. Because the abscissa of the desired point is already known to be $y$, a natural idea is to, when computing $h(\lambda)$, also find the value of the restriction function $g(x)$ at the current optimal solution $x_\lambda$. For example, in the example mentioned earlier, when solving the penalized problem, we can record the number of items selected when the penalized objective function attains its optimal solution. Then, compare $g(x_\lambda)$ with the desired $y$ and adjust the value of $\lambda$ for the next computation accordingly. This is the most traditional WQS binary-search method.

To summarize, the basic flow of traditional WQS binary search is as follows:

1.  Initially, choose a reasonable interval of $\lambda$;
2.  Choose a $\lambda$ in the current interval;
3.  Solve the penalized problem $h(\lambda)=\min_{x\in X}f(x)-\lambda g(x)$, and record the value $g(x_\lambda)$ of $g(x)$ at its optimal solution $x_\lambda$;
4.  If $g(x_\lambda)=y$, we obtain the optimal value of the original problem $v(y)=h(\lambda)+\lambda y$, and terminate the algorithm directly;
5.  Otherwise, adjust the interval of $\lambda$ according to the magnitude relationship between $g(x_\lambda)$ and $y$, and return to step 2.

This basic flow is already enough to solve some problems, but it is not perfect. Next, this article will discuss improvements to this basic flow.

### Handling the collinear case

When applying the basic flow, the first problem encountered is that the collinear case cannot be handled correctly.

If there are three or more red points collinear on the lower convex hull of the point set $\mathcal D$, then in the above basic flow, we may not be able to correctly judge the magnitude relationship between $g(x_\lambda)$ and $y$. For example, let the abscissas of the three collinear red points be $y_1,y_2,y_3$, and let the slope of the line they are collinear on be $\lambda^*$. Then, to correctly solve $v(y_2)$, we must ensure that when the algorithm terminates, the last problem computed is $h(\lambda^*)$, because $\lambda^*$ is the unique slope of a line that can pass through the point $(y_2,v(y_2))$ while minimizing the intercept. But because, in the process of solving $h(\lambda^*)$, the recorded $g(x_{\lambda^*})$ may be any of $y_1,y_2,y_3$. If the recorded $g(x_{\lambda^*})$ does not equal $y_2$, then the algorithm will erroneously continue running and adjust the interval of $\lambda$ in the direction away from $y_2$, ultimately obtaining a wrong result.

To resolve the collinear case, one handling method is, when recording the $g(x_\lambda)$ corresponding to the optimal solution $x_\lambda$, to always make it as large (or as small) as possible. At the same time, change the termination condition of the binary search from finding the $\lambda$ that exactly satisfies $g(x_\lambda)=y$ to finding the smallest (or largest) $\lambda$ satisfying $g(x_\lambda)\ge y$ (or $g(x_\lambda)\le y$). In the previous paragraph's example, this amounts to, when computing the problem $h(\lambda^*)$, outputting $g(x_{\lambda^*})$ as $y_3$. This guarantees that when the algorithm terminates, the last problem computed is $h(\lambda^*)$. When implementing this method, note that what is finally output is not $h(\lambda)+\lambda g(x_{\lambda})$ but $h(\lambda)+\lambda y$, because the recorded $g(x_\lambda)$ does not necessarily equal the actual restriction $y$.

Another handling method is real-valued binary search. If the numbers involved in the problem are all integers, then clearly the slope in WQS binary search is also an integer. Introducing real numbers in the binary search is to ensure that when the correct option $\lambda^*$ is erroneously excluded, it can be adjusted back via the fractional part, ultimately approaching the correct answer $\lambda^*$. For example, in the above example, if, when computing the problem $h(\lambda^*)$, the recorded $g(x_{\lambda^*})$ is $y_1$, which is smaller than the desired $y_2$, then the algorithm turns to considering the interval $(\lambda^*,\lambda_r]$, where $\lambda_r$ is the right endpoint of the interval $\lambda$ lies in. For the integer case, this interval should actually be written as $[\lambda_*+1,\lambda_r]$, which excludes the possibility of approaching the correct answer $\lambda^*$ in the subsequent algorithm. But in real-valued binary search, the interval considered is still $(\lambda^*,\lambda_r]$, and moreover, for $\lambda$ in this interval, the $g(x_\lambda)$ recorded when solving $h(\lambda)$ is always not less than $y_3$, and thus strictly greater than $y_2$. Therefore, as the algorithm continues, the right half-interval is continually discarded, so the final range of $\lambda$ obtained can be guaranteed to be near $\lambda^*$. Of course, because we already know the desired slope is an integer, the precision at the termination of the real-valued binary search need not be very high; it suffices to guarantee that the binary-search interval contains only one integer, which is the $\lambda^*$ to be found.

After correctly handling the collinear case, WQS binary search is enough to solve the vast majority of WQS-binary-search problems encountered in competitive programming. But this method still has some shortcomings: it cannot handle the case where $g(x_\lambda)$ is hard to record, nor the case in high-dimensional WQS binary search where multiple points are coplanar. This article will further examine the properties of the optimization problem $v(y)$ and propose a more general handling method.

## The dual method

This section introduces an implementation method of WQS binary search that only requires that for all $\lambda\in\mathbf R^d$, the value of

$$
h(\lambda) = \min_{x\in X}f(x)-\lambda\cdot g(x)
$$

can be computed efficiently, and that the optimal value $v(y)$ of the original problem is a convex function of $y\in\mathbf R^d$[^high-d-convex]. In a nutshell, this section will prove that the value function $v(y)$ of the original problem equals the optimal value of its dual problem

$$
v^\star(y) = \sup_{\lambda\in\mathbf R^d} h(\lambda)+\lambda\cdot y,
$$

and the objective function of the dual problem is a concave function of $\lambda\in\mathbf R^d$, and thus a unimodal function, which can be solved efficiently via [ternary search](../../basic/binary.md#ternary-search) or [golden-section search](../../basic/binary.md#optimization-golden-section-search), with complexity still $O(T(n)\log^d L)$. This completely resolves the problem that may arise from recording the value of $g(x_\lambda)$ in the traditional WQS binary-search method, and at the same time allows applying the idea of WQS binary search to the high-dimensional case.

In addition, this section also shows that the range of $g(x_\lambda)$ can be found via $h(\lambda)$, without additionally recording it when solving $h(\lambda)$. For example, for the case $d=1$ where the problem only involves integers, we can prove that the range of $g(x_\lambda)$ is exactly

$$
[h(\lambda-1)-h(\lambda),h(\lambda)-h(\lambda+1)].
$$

This actually also provides yet another method of resolving the collinear problem for problems that have to adopt the binary-search flow described earlier.

Next, this section will prove these conclusions using the theory of convex analysis. As for the specific applications of these methods, refer to the [Examples](#examples) section.

### Lagrange duality

Consider solving this problem with the [Lagrange multiplier method](https://en.wikipedia.org/wiki/Lagrange_multiplier). Introducing the Lagrange multiplier $\lambda\in\mathbf R^d$, the Lagrangian can be written as

$$
L(x,\lambda,y) = f(x) - \lambda\cdot g(x)+\lambda\cdot y.
$$

Because as long as one component of $g(x)-y$ is nonzero, we can let the corresponding component of $\lambda$ tend to (positive or negative) infinity,

$$
\sup_{\lambda\in\mathbf R^d}L(x,\lambda,y)
= \begin{cases}
f(x),&g(x)=y,\\
+\infty,&\text{otherwise}.
\end{cases}
$$

This shows that the original problem can be written as

$$
\begin{aligned}
v(y) &= \min_{x\in X}\sup_{\lambda\in\mathbf R^d}L(x,\lambda,y).
\end{aligned}
$$

Swapping the two extremum operations gives its [dual problem](https://en.wikipedia.org/wiki/Duality_%28optimization%29):

$$
\begin{aligned}
v^\star(y)&=\sup_{\lambda\in\mathbf R^d}\min_{x\in X}L(x,\lambda,y)\\
&=\sup_{\lambda\in\mathbf R^d}h(\lambda)+\lambda\cdot y.
\end{aligned}
$$

We will show shortly that, under the condition that $v(y)$ is a convex function of $y$, strong duality holds, i.e. $v^\star(y)=v(y)$.

### Convex conjugate

To show that strong duality holds, we need to introduce the concept of the convex conjugate.

???+ abstract "Convex conjugate"
    For a function $f:\mathbf R^d\rightarrow\mathbf R\cup\{\pm\infty\}$, its **convex conjugate**, or **Legendre–Fenchel transformation**, is the function
    
    $$
    f^*(x^*) = \sup_{x\in\mathbf R^d}x^*\cdot x - f(x).
    $$

From the perspective of the variable $x^*$, $f^*(x^*)$ is the supremum of a series of linear functions, so it is necessarily a convex function on $\mathbf R^d$.

???+ info "The \"slope vector\" and \"intercept\" of a hyperplane"
    The equation of a hyperplane in the vector space $\mathbf R^{d+1}$ discussed in this article always has the form
    
    $$
    y = k\cdot x + b.
    $$
    
    That is, this article does not involve hyperplanes parallel to the $y$-axis. For convenience of description, this article, not rigorously, calls $k$ the "slope vector" of the hyperplane and $b$ its "intercept". Writing this hyperplane's equation in a more standard form,
    
    $$
    k\cdot x - y = -b.
    $$
    
    One of its normal vectors is $(k,-1)$. Therefore, the so-called slope vector is actually the first $d$ components of the normal vector obtained by normalizing the hyperplane's normal vector so that its last component equals $-1$.

Geometrically intuitively, the convex conjugate of the function $f(x)$ describes that, over all hyperplanes with slope vector $x^*$ intersecting the epigraph of the function $f(x)$

$$
\operatorname{epi}f = \{(x,y)\in\mathbf R^d\times\mathbf R:f(x)\le y\}
$$

, the minimum intercept $f(x)-x^*\cdot x$ is $-f^*(x^*)$. In other words, the function $f(x)$ always lies above the hyperplane $y = x^*\cdot x-f^*(x^*)$ and is tangent to this plane at the point $(x_0,f(x_0))$; of course, there may be other tangent points. Such a hyperplane is called a **supporting hyperplane** of $f(x)$ at $x_0$. The intercept of a supporting hyperplane of the function $f(x)$ is uniquely determined by its slope vector, and the convex conjugate provides this mapping from the slope vector to the intercept.

Minimizing $f(x)-\lambda\cdot g(x)$ over the set $X$ is equivalent to minimizing $v(y)-\lambda\cdot y$ over the set $\{(y,v(y))\}$:

$$
\begin{aligned}
\min_x f(x)-\lambda\cdot g(x) &= \min_{y\in g(X)}\left(\min_{x\in X:g(x)=y} f(x) - \lambda\cdot g(x)\right)\\
&= \min_{y\in g(X)}\left(\min_{x\in X:g(x)=y} f(x)\right) - \lambda\cdot y \\
&= \min_{y\in g(X)}v(y) - \lambda\cdot y.
\end{aligned}
$$

Therefore,

$$
h(\lambda) = \min_{y\in g(X)}v(y) - \lambda\cdot y = -v^*(\lambda).
$$

This shows that $h(\lambda)$ is a concave function of $\lambda\in\mathbf R^d$. Further,

$$
v^\star(y) = \sup_{\lambda\in\mathbf R^d}\lambda\cdot y-v^*(\lambda) = v^{**}(y).
$$

That is, the value function $v^{\star}(y)$ of the dual problem is the double convex conjugate of the value function $v(y)$ of the original problem, also called the **biconjugate**.

So the problem reduces to: what kind of function $v(y)$ satisfies that its biconjugate equals itself? The answer to this problem is given by the following theorem:

???+ note "Theorem (Fenchel–Moreau)"
    For a function $f:\mathbf R^d\rightarrow\mathbf R\cup\{\pm\infty\}$, its biconjugate equals itself, i.e. $f^{**}=f$, if and only if one of the following three conditions is satisfied:
    
    1.  $f(x)$ is a proper convex function and [lower semi-continuous](https://en.wikipedia.org/wiki/Semi-continuity),
    2.  $f(x)\equiv+\infty$, or
    3.  $f(x)\equiv-\infty$.

??? note "Proof"
    A function is proper if and only if it never attains the value $-\infty$ and does not always attain the value $+\infty$.
    
    For the case of improper functions, we can verify that $f(x)\equiv+\infty$ and $f(x)\equiv-\infty$ are conjugate to each other. Besides this, as long as $f(x)$ attains $-\infty$ at any point, necessarily $f^*(x^*)\equiv+\infty$. So the only improper functions satisfying $f^{**}=f$ are these two cases. The following discussion is limited to proper functions. For proper functions, the condition of being lower semi-continuous and convex is equivalent to its epigraph being a closed convex set.
    
    The necessity of this condition is easy. Because $f=f^{**}$ is the convex conjugate of $f^*$, being the supremum of a series of linear functions, its epigraph is necessarily the intersection of a series of closed convex sets, and so is necessarily a closed convex set. This shows that a proper function satisfying $f^{**}=f$ is necessarily lower semi-continuous and convex.
    
    Conversely, these conditions are also sufficient. Like the proofs of other strong-duality theorems, the proof can be divided into two steps.
    
    First step, show that weak duality holds, i.e. $f(x)\ge f^{**}(x)$. By the definition of the convex conjugate, for all $x,x^*\in\mathbf R^d$,
    
    $$
    f^*(x^*) \ge x^*\cdot x-f(x).
    $$
    
    This shows that for all $x,x^*\in\mathbf R^d$, likewise
    
    $$
    f(x) \ge x^*\cdot x-f^*(x^*).
    $$
    
    Taking the supremum over $x^*$ on the right side of the inequality gives $f(x)\ge f^{**}(x)$.
    
    Second step, use the [hyperplane separation theorem](https://en.wikipedia.org/wiki/Hyperplane_separation_theorem) to show $f(x)\le f^{**}(x)$. Suppose not; there exists $x_0\in\mathbf R^d$ such that $f(x_0)>f^{**}(x_0)$ holds. Because the epigraph $\operatorname{epi}(f)$ of $f(x)$ is a closed convex set, and the singleton $\{(x_0,f^{**}(x_0))\}$ is a compact convex set, by the hyperplane separation theorem there exist $(\lambda,t)\in\mathbf R^d\times\mathbf R$ and $\alpha\in\mathbf R$ such that for all $x\in\operatorname{dom} f:=\{x\in\mathbf R^d:f(x)<+\infty\}$ and all $y\ge f(x)$,
    
    $$
    \lambda\cdot x-ty <\alpha <\lambda\cdot x_0 - tf^{**}(x_0)
    $$
    
    holds. Because $y$ can be chosen arbitrarily large, necessarily $t\ge 0$. This can be divided into two cases.
    
    First, discuss the case $t>0$. In this case, dividing all parts of the inequality by $t$ and letting $\lambda'=t^{-1}\lambda$ and $\alpha'=t^{-1}\alpha$, we get
    
    $$
    \lambda'\cdot x-y < \alpha'< \lambda'\cdot x_0-f^{**}(x_0).
    $$
    
    For all $x\in\operatorname{dom} f$, letting $y=f(x)$,
    
    $$
    \alpha' > \lambda'\cdot x - f(x).
    $$
    
    Hence, taking the supremum over $x$ on the right of the inequality,
    
    $$
    \alpha' \ge \sup_{x\in\mathbf R^d}\lambda'\cdot x - f(x) = f^*(\lambda').
    $$
    
    Further,
    
    $$
    f^{**}(x_0) < \lambda'\cdot x_0-f^*(\lambda') \le \sup_{x^*\in\mathbf R^d}x^*\cdot x_0-f^*(x^*) = f^{**}(x_0).
    $$
    
    This contradiction shows the case $t>0$ does not hold.
    
    Finally, discuss the case $t=0$. In fact, what will be shown is that it can be turned into the case $t>0$ via perturbation. Take any $\lambda_0\in\operatorname{dom}f^*$; by the definition of the convex conjugate, for any $x\in\operatorname{dom}f$ and $y\ge f(x)$,
    
    $$
    \lambda_0\cdot x-y\le f^*(\lambda_0).
    $$
    
    Therefore, for any $\varepsilon>0$,
    
    $$
    (\lambda+\varepsilon\lambda_0)\cdot x - \varepsilon y<\alpha+\varepsilon f^*(\lambda_0).
    $$
    
    At the same time, because $\alpha<\lambda\cdot x_0$, for sufficiently small $\varepsilon>0$,
    
    $$
    \alpha+\varepsilon f^*(\lambda_0) < (\lambda+\varepsilon\lambda_0)\cdot x_0 - \varepsilon f^{**}(x_0).
    $$
    
    Therefore, taking $\lambda'=\lambda+\varepsilon\lambda_0$, $t'=\varepsilon$, and $\alpha'=\alpha+\varepsilon f^*(\lambda_0)$,
    
    $$
    \lambda'\cdot x-t'y <\alpha' <\lambda'\cdot x_0 - t'f^{**}(x_0).
    $$
    
    This returns to the previous case and again leads to a contradiction.
    
    This contradiction shows there is no point $x_0\in\mathbf R^d$ satisfying $f(x_0)>f^{**}(x_0)$. Hence, always $f(x_0)\le f^{**}(x_0)$.
    
    Combining the results of these two steps gives $f^{**}(x)=f(x)$.

Therefore, strong duality holds if and only if $v(y)$ is a convex function of $y\in\mathbf R^d$[^other-conditions].

### Subgradient

The previous section showed that the value function $h(\lambda)$ of the penalized problem is the negation of the convex conjugate of the value function $v(y)$ of the original problem. Because the definition of the convex conjugate is actually a parameterized optimization problem, it also has a conclusion similar to the [envelope theorem](https://en.wikipedia.org/wiki/Envelope_theorem). But because a convex function is not everywhere differentiable, we first need to generalize the definition of the derivative to the case of convex functions. This leads to the concept of the subgradient.

???+ abstract "Subgradient"
    For a convex function $f:\mathbf R^d\rightarrow\mathbf R\cup\{\pm\infty\}$ and $x_0\in\operatorname{dom}f$, if a vector $x^*\in\mathbf R^d$ satisfies, for any $x\in\mathbf R^d$,
    
    $$
    f(x) \ge f(x_0)+x^*\cdot(x-x_0),
    $$
    
    then $x^*$ is called a **subgradient** of $f(x)$ at $x_0$. The set of all subgradients of the function $f(x)$ at $x_0$ is called its **subdifferential** at that point, denoted $\partial f(x_0)$.

Geometrically intuitively, the subdifferential of the convex function $f(x)$ at $x_0$ is the set of slope vectors of all supporting hyperplanes at that point. For the one-dimensional case, the subdifferential

$$
\partial f(x_0) = [\partial_-f(x_0),\partial_+f(x_0)],
$$

where $\partial_-f(x_0)$ and $\partial_+f(x_0)$ are the left and right derivatives of the function $f(x)$ at $x_0$ respectively. Further, for $\tilde f(x)$ extended from a convex function $f:\mathbf Z\rightarrow\mathbf R\cup\{\pm\infty\}$ on the integer set, its left and right derivatives at the integer point $x=k$ are the first differences on the left and right:

$$
\partial\tilde f(k) = [f(k)-f(k-1),f(k+1)-f(k)]. 
$$

Clearly, the convex function $f(x)$ is differentiable at the point $x_0$ if and only if its subdifferential $\partial f(x_0)$ at that point is a singleton.

Because the convex conjugate provides the mapping from the slope vector of a supporting hyperplane to its intercept, using the convex conjugate we can determine whether a slope vector $x^*$ is a subgradient of the convex function $f(x)$ at a given point $x$.

???+ note "Theorem (convex conjugate and subgradient)"
    For a proper convex function $f:\mathbf R^d\rightarrow\mathbf R$ and any $x,x^*\in\mathbf R^d$,
    
    $$
    x^*\in\partial f(x) \iff x^*\cdot x = f(x) + f^*(x^*).
    $$
    
    Further, if $f$ is also lower semi-continuous, then both conditions are equivalent to $x\in\partial f^*(x^*)$.

??? note "Proof"
    By the definition of the subgradient, $x^*\in\partial f(x)$ if and only if
    
    $$
    f(x') \ge f(x) + x^*\cdot(x'-x),~\forall x'\in\mathbf R^d.
    $$
    
    This is equivalent to
    
    $$
    x^*\cdot x - f(x) \ge x^*\cdot x'-f(x'),~\forall x'\in\mathbf R^d.
    $$
    
    This is in turn equivalent to
    
    $$
    x^*\cdot x - f(x) \ge \sup_{x'\in\mathbf R^d}x^*\cdot x'-f(x') = f^*(x^*).
    $$
    
    But by the definition of the convex conjugate, always
    
    $$
    x^*\cdot x - f(x) \le f^*(x^*).
    $$
    
    Therefore, the greater-than-or-equal sign in the former is actually equivalent to an equal sign, i.e. equivalent to
    
    $$
    x^*\cdot x = f(x) + f^*(x^*).
    $$
    
    This completes the proof of the first part.
    
    For the case where $f$ is a lower-semi-continuous proper convex function, by the Fenchel–Moreau theorem, $f^{**}=f$. Therefore, these two conditions are equivalent to
    
    $$
    x^*\cdot x = f^*(x^*) + f^{**}(x).
    $$
    
    Applying the conclusion of the first part again, they are also equivalent to $x\in\partial f^*(x^*)$.

This conclusion shows that if $f^{**}=f$, then the subdifferential $\partial f^{*}(x^*)$ of the convex conjugate $f^*$ at $x^*$ is exactly the set of $x$-components of the intersection points of the supporting hyperplane with slope vector $x^*$ and the epigraph $\operatorname{epi}f$.

???+ note "Corollary"
    For a lower-semi-continuous proper convex function $f:\mathbf R^d\rightarrow\mathbf R$ and any $x,x^*\in\mathbf R^d$,
    
    $$
    \begin{aligned}
    \partial f(x) &= \arg\max_{y^*\in\mathbf R^d} x\cdot y^* - f^*(y^*),\\
    \partial f^*(x^*) &= \arg\max_{y\in\mathbf R^d} x^*\cdot y - f(y).
    \end{aligned}
    $$

??? note "Proof"
    Below we prove the second equality. The proof of the first is similar.
    
    By the definition of the convex conjugate,
    
    $$
    f^*(x^*) = \sup_{y\in\mathbf R^d} x^*\cdot y - f(y),
    $$
    
    so
    
    $$
    x \in \arg\max_{y\in\mathbf R^d} x^*\cdot y - f(y)
    $$
    
    if and only if $f^*(x^*) = x^*\cdot x - f(x)$, and this equality holds if and only if $x\in\partial f^*(x^*)$. This proves the two sets are equal.

Applied to the scenario of this article, this conclusion shows that when solving the problem

$$
h(\lambda) = \min_{x\in X}f(x)-\lambda\cdot g(x) = \min_{y\in g(X)}v(y) - \lambda\cdot y
$$

, the value of the restriction function $g(x)$ over the optimal decision set is exactly $\partial(-h(\lambda))$. For the case $d=1$ where the problem only involves integers, this set is the interval

$$
[h(\lambda-1)-h(\lambda),h(\lambda)-h(\lambda+1)].
$$

For consecutive integers $\lambda$, these intervals are connected end to end, so when used for binary search, we only need to compute one side's endpoint.

## Proving convexity

The prerequisite for applying WQS binary search is the convexity of the value function. In competitive programming, we can guess that convexity holds via tabulation, intuitive understanding, etc. But rigorously proving convexity is often not easy. This section, combined with the following classic problem, introduces methods common in competitive programming for proving convexity.

???+ example "The tree-planting problem"
    There are $n$ tree pits, and $m$ trees are to be planted. Trees cannot be planted in two adjacent pits. Given a sequence $\{a_i\}$ of length $n$ representing the profit of planting a tree in each pit, where the profit can be positive or negative, find the maximum possible total profit of planting these $m$ trees.
    
    In short, it is the problem of solving the maximum-weight independent set of size $m$ on a chain of length $n$.

These methods can be roughly divided into four categories:

-   reduce to the convexity of the value function of a convex-optimization problem (including [linear programming](../../math/linear-programming.md), etc.) with respect to the parameter, which includes methods such as building a [min-cost flow](../../graph/flow/min-cost.md) model;
-   use the state-transition equation to inductively prove that convexity holds, possibly using some [convexity-preserving transformations](./slope-trick.md#transformations-of-convex-functions) in the process;
-   for interval-partition-type problems, verify that the cost function of each segment satisfies the [quadrangle inequality](./quadrangle.md);
-   finally, for special problems, we can also directly show convexity holds via an exchange argument.

These proof methods themselves are often tied to some solution of the problem.

### Reduce to parameterized convex optimization

Consider a parameterized convex-optimization problem of the following form:

$$
v(y)=\inf_{x\in\mathcal D(y)} f(x,y).
$$

where the objective function $f:\mathbf R^n\times\mathbf R^d\rightarrow\mathbf R\cup\{\pm\infty\}$ is, for each $y\in\mathbf R^d$, a convex function of $x\in\mathbf R^m$, and the feasible region $\mathcal D:\mathbf R^d\rightarrow \mathcal P(\mathbf R^m)$ is a set-valued function on $\mathbf R^d$, and for each $y\in\mathbf R^d$, the set $\mathcal D(y)$ is a convex set. These conditions guarantee that for any parameter $y\in\mathbf R^d$, this is a convex-optimization problem.

???+ note "Theorem"
    Suppose the above parameterized convex-optimization problem satisfies the following conditions:
    
    1.  the objective function $f(x,y)$ is a convex function of $(x,y)$;
    2.  the graph $\{(x,y):x\in\mathcal D(y)\}$ of the feasible-region mapping $y\mapsto\mathcal D(y)$ is a convex set.
    
    If for any $y\in\mathbf R^d$, $v(y)>-\infty$, then the value function $v(y)$ is a proper convex function of $y$.

??? note "Proof"
    For any $y_1,y_2\in\mathbf R^d$ and $\alpha\in(0,1)$, we need to prove
    
    $$
    v(\alpha y_1+(1-\alpha)y_2) \le \alpha v(y_1) + (1-\alpha) v(y_2).
    $$
    
    If $v(y_1)=+\infty$ or $v(y_2)=+\infty$, then the right side of the inequality is $+\infty$ and the inequality necessarily holds. Otherwise, $v(y_1)$ and $v(y_2)$ are both finite. For any $\varepsilon>0$ and $i=1,2$, there exists $x_i\in\mathcal D(y_i)$ such that $f(x_i,y_i)< v(y_i)+\varepsilon$ holds. Using the convexity of the graph of the mapping $\mathcal D$,
    
    $$
    \alpha x_1+(1-\alpha)x_2 \in \mathcal D(\alpha y_1+(1-\alpha)y_2).
    $$
    
    That is, $\alpha x_1+(1-\alpha)x_2$ is a feasible solution of the optimization problem with parameter $\alpha y_1+(1-\alpha)y_2$. Using the optimality condition and the convexity of the objective function,
    
    $$
    \begin{aligned}
    v(\alpha y_1+(1-\alpha)y_2)
    &\le f(\alpha x_1+(1-\alpha)x_2,\alpha y_1+(1-\alpha)y_2) \\
    &\le \alpha f(x_1,y_1) + (1-\alpha)f(x_2,y_2) \\
    &< \alpha v(y_1) + (1-\alpha) v(y_2) + \varepsilon.
    \end{aligned}
    $$
    
    Because the choice of $\varepsilon$ is arbitrary, letting $\varepsilon\rightarrow 0$,
    
    $$
    v(\alpha y_1+(1-\alpha)y_2) \le \alpha v(y_1) + (1-\alpha) v(y_2).
    $$
    
    Therefore, the convexity of the value function $v(y)$ holds.

In competitive programming, the most common convex-optimization problem is the linear-programming problem.

???+ note "Corollary"
    Let $c\in\mathbf R^n$, $A_1\in\mathbf R^{d_1\times n}$, $A_2\in\mathbf R^{d_2\times n}$, $y_1\in\mathbf R^{d_1}$, $y_2\in\mathbf R^{d_2}$. Consider the following parameterized linear-programming problem:
    
    $$
    v(y_1,y_2)=\min_{x\in\mathbf R^n} c\cdot x \text{ subject to }A_1x\le y_1,A_2x=y_2,x\ge 0.
    $$
    
    Then, the value function $v(y_1,y_2)$ is a convex function of $(y_1,y_2)$.

Whether it is an inequality constraint or an equality constraint, the value function of a linear program is a convex function of the constraint parameters.

Many graph-theory problems can be written in the form of a linear-programming problem:

-   network-flow problems: max flow, min cut, min-cost flow;
-   shortest-path problems without negative cycles;
-   maximum (weight) matching, minimum vertex cover, etc. of bipartite graphs;
-   maximum (weight) matching problems of general graphs;
-   minimum spanning tree problems[^mst].

Therefore, the value functions of these problems are all convex (concave) functions of the problems' parameters.

???+ warning "Integer constraints"
    When modeling practical problems with graph-theory models, there are usually implicit integer restrictions, e.g. an edge can only be selected or not, flow can only be an integer, etc. Therefore, they can only be turned into integer linear programming (ILP) problems rather than linear programming (LP) problems. Because an ILP problem is not a convex-optimization problem, its value function is not necessarily a convex function of the problem's parameters. Relaxing the integer constraints in an ILP problem gives an LP problem, but the latter does not necessarily have an optimal solution satisfying the integer constraints. Therefore, the optimal value of the LP obtained after relaxing the integer constraints may be strictly better than the corresponding ILP problem, and the two are not necessarily equivalent.
    
    The graph-theory problems listed above can all be written as an LP problem without imposing integer constraints; but for some other problems, such as the maximum independent set problem of general graphs, integer constraints are necessary. In addition, even if a graph-theory problem can be written in LP form, after introducing extra linear constraints to that problem, the equivalence between the corresponding ILP problem and the LP problem may still be broken, so this constrained graph-theory problem can no longer be written in linear-programming form.

For example, in the context of min-cost flow, there is the following common conclusion:

???+ note "Corollary"
    In the [min-cost flow model](../../graph/flow/min-cost.md), the minimum cost $v(m)$ is a convex function of the flow $m$.

??? note "Proof"
    Let the directed graph be $G=(V,E)$, the capacity of edge $(i,j)$ be $c_{ij}$, the cost per unit flow be $w_{ij}$, and the source and sink be $s$ and $t$ respectively. Let the decision variables be $\{f_{ij}\}$, where $f_{ij}$ is the flow of edge $(i,j)\in E$. Then, min-cost flow can be written as the following linear-programming problem:
    
    $$
    \begin{aligned}
    v(m)=\min_{\{f_{ij}\}}\;&\sum_{(i,j)\in E}w_{ij}f_{ij}\\
    \text{subject to }&\sum_{(j,i)\in E}f_{ji} - \sum_{(i,j)\in E}f_{ij} = 
    \begin{cases}
    -m, & i=s,\\
    m,  & i=t,\\
    0,  & \text{otherwise},
    \end{cases}
    ~\forall i\in V,\\
    &0\le f_{ij}\le c_{ij},~\forall (i,j)\in E.
    \end{aligned}
    $$
    
    Therefore, the minimum cost $v(m)$ is a convex function of the parameter $m$.

Many problems in competitive programming can be reduced to graph-theory problems such as network flow, and thus the convexity of the value function can be established in a similar way.

Using this method, we can obtain the first convexity proof of the tree-planting problem:

??? example "Convexity proof one"
    The maximum profit of the tree-planting problem can actually be obtained via the following max-cost max-flow model:
    
    -   from the source $s$, connect an edge to node $r$ with capacity $m$ and cost $0$;
    -   from node $r$, connect an edge with capacity $1$ and cost $0$ to each odd node $i=1,3,\cdots,2\lceil n/2\rceil-1$;
    -   from each even node $i=0,2,\cdots,2\lfloor n/2\rfloor$, connect an edge with capacity $1$ and cost $0$ to the sink $t$;
    -   for each $i=1,\cdots,n$, from the odd node among $i-1$ and $i$, connect an edge with capacity $1$ and cost $a_i$ to the even node.
    
    The final answer is the max cost obtained. Converting this graph-theory model into the corresponding linear-programming problem (see the proof of the corollary above for details), the total flow $m$ will appear in the inequality representing the flow restriction of the edge $(s,r)$. By the corollary, the max cost $v(m)$ is a concave function of the flow $m$.
    
    Using this min-cost flow model, we can solve this problem in $O(n\log n)$ complexity via simulated min-cost flow or [regret greedy](../../basic/greedy.md#the-regret-approach).

### Using the state-transition equation

Although the state-transition equation cannot provide an effective way of computing, it can often be used to prove that the state function $f(i,j)$ is convex in the parameter $j$. Specifically, regarding the function $f(i,\cdot)$ as the state at $i$, we can regard the state-transition equation for $f(i,j)$ as a recurrence relation for $f(i,\cdot)$, and thereby inductively prove that each $f(i,\cdot)$ is a convex function. This kind of convexity-proving method is more common in the context of [Slope Trick optimization of DP](./slope-trick.md); that page also discusses common convexity-preserving transformations.

This method can likewise be used to prove the convexity of the tree-planting problem:

??? example "Convexity proof two"
    Let $f(i,j)$ be the maximum profit when planting $j$ trees in the first $i$ pits. Examine the following state-transition equation:
    
    $$
    f(i,j) = \max\{f(i-1,j),f(i-2,j-1)+a_i\}.
    $$
    
    Regard this state-transition equation as a recurrence relation of the function $f(i,\cdot)$. Because the extremum symbol involves two different functions, this cannot be expressed in the form of a supremal convolution. But we can still prove inductively that the function $f(i,\cdot)$ is a concave function.
    
    In fact, we need to inductively prove the following two points:
    
    -   $f(i,j)-f(i-2,j-1)$ decreases in $j$;
    -   $f(i,j)-f(i-1,j)$ increases in $j$.
    
    The induction base is trivial. Suppose they hold for all natural numbers up to $i-1$; now we prove they also hold for $i$. Just verify directly.
    
    First, by the inductive hypothesis,
    
    $$
    f(i-1,j) - f(i-2,j-1) = (f(i,j)-f(i-2,j-1)) - (f(i,j)-f(i-1,j))
    $$
    
    decreases in $j$. So
    
    $$
    f(i,j) - f(i-2,j-1) = \max\{f(i-1,j) - f(i-2,j-1), a_i\}
    $$
    
    decreases in $j$, and
    
    $$
    f(i,j) - f(i-1,j) = \max\{0,a_i-(f(i,j) - f(i-2,j-1))\}
    $$
    
    increases in $j$. This completes the induction.
    
    Further,
    
    $$
    f(i,j) - f(i,j-1) = (f(i,j)-f(i-2,j-1)) - (f(i,j-1) - f(i-1,j-1)) - (f(i-1,j-1) - f(i-2,j-1))
    $$
    
    decreases in $j$. This shows $f(i,j)$ is a concave function of $j$, and hence the value function $v(m)=f(n,m)$ is a concave function of $m$.
    
    A by-product of this proof is that for any $i$, there exists $p_i$ such that
    
    $$
    f(i,j) =
    \begin{cases}
    f(i-1,j), & j\le p_i,\\
    f(i-2,j-1) + a_i, & j> p_i.
    \end{cases}
    $$
    
    This shows that we can directly maintain the sequence $f(i,\cdot)$ with a balanced tree, with complexity $O(n\log^2n)$. But the benefit is that it can handle the general case of arbitrary tree-planting spacing, and obtains all values of $v(m)$ at once.

### The quadrangle inequality

In competitive programming, another common class of problems where convexity holds is the [interval-partition problem](./quadrangle.md#interval-partition-problem). That page proves that if the cost function of a single interval satisfies the quadrangle inequality, then the minimum cost of the interval-partition problem with a restricted number of intervals is a convex function of the number of intervals. That page also provides some methods to determine whether a function $w(l,r)$ satisfies the quadrangle inequality. The most direct method is to compute its second-order mixed difference:

$$
\begin{aligned}
\Delta_l \Delta_r w(l,r) &= \Delta_l(w(l,r+1)-w(l,r)) \\
&= w(l+1,r+1)-w(l+1,r)-w(l,r+1)+w(l,r).
\end{aligned}
$$

The function $w(l,r)$ satisfies the quadrangle inequality if and only if $\Delta_l \Delta_r w(l,r)$ is non-positive. Intuitively, a function satisfying the quadrangle inequality usually means that expanding the interval to both sides—i.e. moving the left endpoint left and the right endpoint right—has some synergistic effect.

The tree-planting problem can likewise be seen as an interval-partition problem, and can be proven by verifying the quadrangle inequality.

??? example "Convexity proof three"
    Prepend an $a_0$ to the tree-planting profit sequence; it can be any value. Then, the tree-planting problem is equivalent to the interval-partition problem of splitting the sequence $\{a_0,a_1,\cdots,a_n\}$ into $m$ segments, where each segment's profit function is
    
    $$
    w(l,r) = \max_{i\in[l+1,r]} a_i
    $$
    
    . That is, the profit of each segment is the maximum profit of the trees other than the first tree—this guarantees spaced tree-planting.
    
    Because this is a maximization problem, we need to verify "crossing is greater than containing", i.e. for any $a<b<c<d$,
    
    $$
    w(a,c)+w(b,d) \ge w(a,d)+w(b,c).
    $$
    
    Substituting the expression for the profit function and letting
    
    $$
    A = \max_{i\in[a+1,b]} a_i,~ B = \max_{i\in[b+1,c]} a_i,~ C = \max_{i\in[c+1,d]}a_i,
    $$
    
    the inequality to be proven can be written as
    
    $$
    \max\{A,B\} + \max\{B,C\} \ge \max\{A,B,C\} + B.
    $$
    
    Note that the larger of the two terms $\max\{A,B\}$ and $\max\{B,C\}$ on the left side of the inequality equals $\max\{A,B,C\}$, while the smaller of them is always not less than $B$, so the inequality holds.
    
    After turning the tree-planting problem into an interval-partition problem, we only need to preprocess the interval extrema via an ST table, etc., so that the cost of a single interval can be computed in $O(1)$ each time; then we can apply the interval-partition-problem algorithm to solve the problem in $O(n\log n\log L)$ or $O(n(n+m))$ time complexity. This method can likewise handle the problem with arbitrary tree-planting spacing.

### The exchange argument

In combinatorial-optimization problems, proving the convexity of the value function often uses the exchange argument. Specifically, it is the argument method of, starting from the optimal solutions of the problems with parameters $m-1$ and $m+1$, constructing, by exchanging some elements, a feasible solution with parameter $m$ and value not exceeding $(v(m-1)+v(m+1))/2$, and thereby using the optimality of $v(m)$ to prove convexity. Compared with the convex-optimization case, there is no natural method to construct an "intermediate form" of two solutions in combinatorial-optimization problems, so the application of the exchange argument usually requires some skill.

???+ warning "\"Increasing marginal cost\" does not necessarily imply convexity"
    In combinatorial-optimization problems, the objective function often has some "increasing marginal cost" properties, but this does not necessarily imply convexity. A typical example is [\[IOI 2005\] Riv](https://www.luogu.com.cn/problem/P3354); the chain version of this problem satisfies the quadrangle inequality and thus is convex, but the tree version has examples where convexity does not hold.
    
    A common property used to characterize "increasing marginal cost" is the supermodularity of a function. For a function $f:\mathcal PX\rightarrow\mathbf R$ on the family of subsets $\mathcal PX$ of a finite set $X$, if it satisfies one of the following two equivalent properties:
    
    1.  (crossing is less than containing) for any subsets $A,B\subseteq X$, $f(A)+f(B) \le f(A\cup B) + f(A\cap B)$ holds;
    2.  (increasing marginal cost) for any subsets $A\subseteq B\subseteq X$ and $x\in X\setminus B$, $f(A\cup\{x\})-f(A)\le f(B\cup\{x\})-f(B)$ holds;
    
    then the function $f$ is called **supermodular**. But in an optimization problem with a supermodular function as the objective function, the value function
    
    $$
    v(m) = \min_{A\subseteq X} f(A) \text{ subject to }|A|=m
    $$
    
    is **not necessarily** a convex function of $m$. The reason is precisely that, from the optimal solutions with subset sizes $m-1$ and $m+1$, one generally cannot construct a feasible solution with subset size $m$ satisfying the aforementioned value-magnitude relationship.

The exchange argument provides yet another proof of the convexity of the tree-planting problem.

??? example "Convexity proof four"
    Use the exchange argument. Let the optimal schemes for planting $m-1$ trees and $m+1$ trees be given by $\{x_i^{(m-1)}\}\in\{0,1\}^n$ and $\{x_i^{(m+1)}\}\in\{0,1\}^n$ respectively, where value $1$ means a tree is planted in that pit and value $0$ means no tree is planted. Define the sequence $\{z_i\}\in\{0,\pm 1\}^n$ satisfying
    
    $$
    z_i = x_i^{(m+1)} - x_i^{(m-1)},~i=1,\cdots,n.
    $$
    
    This sequence marks the difference between the two tree-planting schemes. The positions of value $0$ in this sequence mean that pit either has a tree planted in both schemes or no tree in both; while the positions of value $-1$ and $+1$ mean that pit has a tree planted only in scheme $x^{(m-1)}$ or only in scheme $x^{(m+1)}$ respectively. Because no scheme can plant trees in adjacent pits, we have the following observations:
    
    -   in a continuous nonzero subsegment, the values of $z_i$ necessarily alternate between $\pm 1$;
    -   the $0$s on the left and right sides of a maximal continuous nonzero subsegment necessarily mean no tree is planted in either scheme.
    
    Therefore, if in some maximal continuous nonzero subsegment the sum of $z_i$ is exactly $+1$—that is, in this segment of pits scheme $x^{(m+1)}$ plants one more tree than scheme $x^{(m-1)}$—then we can exchange the tree-planting positions of the two schemes within this segment. This gives two feasible schemes each planting $m$ trees. Because the total tree-planting positions and count of the two schemes are unchanged, only redistributed, the total profit is unchanged, still $v(m-1)+v(m+1)$. But these two schemes planting $m$ trees are not necessarily optimal, so their respective profits do not exceed $v(m)$. This proves
    
    $$
    v(m-1) + v(m+1) \le 2v(m),
    $$
    
    that is, $v(m)$ is a concave function of $m$.
    
    Now, only one problem remains: whether a maximal continuous nonzero subsegment with sum exactly $+1$ exists. Because it is the sum of several alternating $\pm 1$, the sum of a continuous nonzero subsegment can only be $0$ or $\pm 1$. And because the sum of all these maximal continuous nonzero subsegments equals $2$, there must exist at least two maximal continuous nonzero subsegments with sum exactly $+1$. This completes the proof.

## Examples

This section introduces several examples of applying the WQS binary-search method in different scenarios.

### Template problem

???+ example "[Luogu P1484 Tree Planting](https://www.luogu.com.cn/problem/P1484)"
    There are $n$ tree pits, and **at most** $m$ trees are to be planted. Trees cannot be planted in two adjacent pits. Given a sequence $\{a_i\}$ of length $n$ representing the profit of planting a tree in each pit, where the profit can be positive or negative, find the maximum possible total profit of planting these $m$ trees.

??? note "Solution"
    Slightly different from the tree-planting problem discussed earlier, this problem requires planting at most $m$ trees rather than exactly $m$ trees. Still using $v(m)$ to denote the value function of the tree-planting problem discussed earlier, the answer to this problem is actually $\tilde v(m)=\max_{k\le m}v(k)$. Because $v(m)$ is a concave function, i.e. a unimodal function, the answer to this problem amounts to keeping only the part of $v(m)$ rising up to the peak, after which the function stays at the peak; this amounts to keeping only the part where the tangent slope is non-negative. Therefore, the only difference between this problem and the problem discussed earlier is that in WQS binary search, the initial slope range is $[0,\max_ia_i]$ rather than $[\min_ia_i,\max_ia_i]$.
    
    After removing the count restriction with the WQS binary-search method, the problem turns into computing the maximum-weight independent set on a chain, except the original profit $\{a_i\}$ is replaced with $\{a_i+k\}$. This is a classic dynamic-programming problem. We can let $f(i,j)$ be the maximum profit of the subproblem of the first $i$ tree pits when the $i$-th pit is chosen to plant a tree ($j=1$) or not ($j=0$). From this, we can write the state-transition equation as
    
    $$
    \begin{aligned}
    f(i,0) &= \max\{f(i-1,0),f(i-1,1)\},\\
    f(i,1) &= f(i-1,0) + a_i + k.
    \end{aligned}
    $$
    
    The initial conditions are $f(0,0)=0$ and $f(0,1)=-\infty$, and the final answer is $\max\{f(n,0),f(n,1)\}$. A single computation has complexity $O(n)$, and the overall time complexity is $O(n\log L)$, where $L=\max_i|a_i|$.
    
    The reference implementations are as follows:
    
    === "Traditional method"
        ```cpp
        --8<-- "docs/dp/code/opt/wqs-binary-search/plant-tree-1.cpp"
        ```
    
    === "Dual method"
        ```cpp
        --8<-- "docs/dp/code/opt/wqs-binary-search/plant-tree-2.cpp"
        ```

???+ example "[Luogu P2619 \[National Training Team\] Tree I](https://www.luogu.com.cn/problem/P2619)"
    Given a weighted undirected connected graph where each edge is black or white, find the minimum weight of a spanning tree with exactly $m$ white edges.

??? note "Solution"
    First, the exchange argument can prove that $v(m)$ is a convex function. Suppose all edge weights are distinct: cases where two edges have equal weight can be turned into cases where all edge weights are distinct via perturbation; then, letting the magnitude of the perturbation tend to zero, we can prove that the convexity of the function still holds in the limit case—the case where two edges have equal weight. The key of the proof is the following lemma:[^edge-swap]
    
    ???+ note "Lemma"
        Let $S$ and $T$ be two spanning trees of the undirected connected graph $G=(V,E)$. For any $e\in S\setminus T$, there exists at least one edge $f\in T\setminus S$ such that both $S-e+f$ and $T-f+e$ are spanning trees of the graph $G$.
    
    ??? note "Proof"
        Let $e=(u,v)$, and let $P$ be the unique path in the tree $T$ connecting $u$ and $v$. Because $P+e$ is the unique cycle in the graph $T+e$, deleting any edge $f$ in $P$ makes $T-f+e$ a spanning tree. At the same time, the graph $S-e$ is a forest with two connected components, whose vertex sets are denoted $V_1$ and $V_2$; so as long as we choose an edge $f\in P$ that connects $V_1$ and $V_2$, we can guarantee $S-e+f$ is a spanning tree. Such an edge $f$ always exists, because $u$ and $v$ belong to $V_1$ and $V_2$ respectively, and $P$ connects $u$ and $v$. Moreover, $f\notin S$, because in the graph $S-e$, $V_1$ and $V_2$ are not connected. This completes the proof.
    
    Let $T_{m-1}$ and $T_{m+1}$ be the minimum spanning trees with $m-1$ and $m+1$ white edges respectively. Let $e$ be a white edge of $T_{m+1}\setminus T_{m-1}$; applying the above lemma to it, there exists an edge $f\in T_{m-1}\setminus T_{m+1}$ such that both $T'=T_{m+1}-e+f$ and $T''=T_{m-1}+e-f$ are spanning trees. Because only a pair of edges is exchanged, the edge-weight sums of the trees $T'$ and $T''$ are still $v(m-1)+v(m+1)$. Further, discuss two cases:
    
    -   If $f$ is a black edge, then the number of white edges in both $T'$ and $T''$ is $m$. Their respective edge-weight sums are both not less than $v(m)$. This proves $2v(m)\le v(m-1)+v(m+1)$, so $v(m)$ is convex in $m$.
    -   If $f$ is a white edge, then the numbers of white edges in $T'$ and $T''$ are $m+1$ and $m-1$ respectively, so their edge-weight sums are not less than $v(m+1)$ and $v(m-1)$ respectively. But we have already shown that their edge-weight sums together equal $v(m-1)+v(m+1)$. This shows the edge-weight sum of $T'$ equals $v(m+1)$. Comparing $T'$ with $T_{m+1}$, the weights of $e$ and $f$ must be equal. This contradicts the assumption, so this case does not hold.
    
    This proves that $v(m)$ is a convex function of $m$.
    
    After establishing the convexity of the function $v(m)$, we can solve this problem with WQS binary search. Remove the count restriction, subtract $k$ from the weight of each white edge, and solve the minimum-spanning-tree problem. For this, we can apply [Kruskal's algorithm](../../graph/mst.md#kruskal-algorithm). Using a disjoint-set union to maintain connectivity, the algorithm complexity is $O(E\log E+E\alpha(V))$, where $E$ and $V$ are the number of edges and vertices, and $\alpha(\cdot)$ is the inverse Ackermann function. The main part of the complexity, $O(E\log E)$, is the complexity of sorting the edges, which can be further optimized in this problem. Although the minimum spanning tree needs to be computed many times during WQS binary search, each time only the weights of the white edges are increased or decreased by a number as a whole. So we can sort the white edges and black edges separately during preprocessing, and then each time the minimum spanning tree is computed, we only need to merge the reweighted white edges and black edges together. This way, the overall complexity is reduced to $O(E\log E+E\alpha(V)\log L)$, where $L$ is the length of the range of the edge weights.
    
    The reference implementations are as follows:
    
    === "Traditional method"
        ```cpp
        --8<-- "docs/dp/code/opt/wqs-binary-search/black-white-mst-1.cpp"
        ```
    
    === "Dual method"
        ```cpp
        --8<-- "docs/dp/code/opt/wqs-binary-search/black-white-mst-2.cpp"
        ```

### Interval-partition problem

???+ example "[Luogu P6246 \[IOI 2000\] Post Office, enhanced enhanced](https://www.luogu.com.cn/problem/P6246)"
    Given an increasing sequence of positive integers $\{a_i\}$ of length $n$ representing the positions of $n$ villages beside a highway, $m$ post offices need to be built. The choice of post-office positions needs to minimize the sum of distances between all villages and their nearest post office. Find this minimum.

??? note "Solution"
    This is a typical [interval-partition problem](./quadrangle.md#interval-partition-problem). For the implementation details of the binary-search queue, refer to that page.
    
    Each post office serves the villages nearest to it, so these villages are necessarily several consecutive villages beside the highway. So building $m$ post offices amounts to dividing all villages into $m$ consecutive segments and building a lowest-cost post office for each segment. As is well known, the post office should be built at the median of the village positions. From this, we can write the cost function of the interval $[l,r]$ as
    
    $$
    w(l,r) = \sum_{i=l}^r|a_i-a_{\lfloor(l+r)/2\rfloor}|.
    $$
    
    It satisfies the quadrangle inequality, because its second-order mixed difference is non-positive:
    
    $$
    \Delta_l\Delta_r w(l,r)
    = \Delta_l(a_{r+1} - a_{\lfloor(l+r+1)/2\rfloor})
    = a_{\lfloor(l+r+1)/2\rfloor}-a_{\lfloor(l+r+2)/2\rfloor} \le 0.
    $$
    
    This shows we can solve this problem in $O(n\log n\log L)$ complexity via the binary-search queue combined with WQS binary search.
    
    The reference implementations are as follows:
    
    === "Traditional method"
        ```cpp
        --8<-- "docs/dp/code/opt/wqs-binary-search/post-office-1.cpp"
        ```
    
    === "Dual method"
        ```cpp
        --8<-- "docs/dp/code/opt/wqs-binary-search/post-office-2.cpp"
        ```

### Two-dimensional restrictions

???+ example "[Codeforces 739 E. Gosha is hunting](https://codeforces.com/problemset/problem/739/E)"
    There are $n$ Pokémon; the sequences $\{p_i\}$ and $\{q_i\}$ represent the probabilities of catching the $i$-th Pokémon with a Poké Ball and a Great Ball respectively. You can throw a Poké Ball at a Pokémon, or throw a Great Ball, or throw one of each, or throw nothing. There are currently $m_1$ Poké Balls and $m_2$ Great Balls, which need to be allocated reasonably and thrown simultaneously. Find the maximum expected number of Pokémon caught. Whether a single catch succeeds is independent of the results of other catches.
    
    More generally, it can be abstracted as the following problem:
    
    Given three sequences of positive reals $\{A_i\},\{B_i\},\{C_i\}$ of length $n$, and moreover $C_i\le A_i+B_i$ holds for all $i=1,\cdots,n$. Find optimal index sets $X$ and $Y$ satisfying $|X|=m_1$ and $|Y|=m_2$ and maximizing
    
    $$
    \sum_{i\in X\setminus Y}A_i + \sum_{i\in Y\setminus X}B_i + \sum_{i\in X\cap Y}C_i.
    $$

??? note "Solution"
    The original problem can be seen as a special case of this more general problem when
    
    $$
    A_i = p_i,~ B_i = q_i,~ C_i = p_i+q_i-p_iq_i.
    $$
    
    Therefore, we only need to discuss the solution of the more general problem.
    
    Use $v(m_1,m_2)$ to denote the value function of this problem; we need to prove it is a concave function of $(m_1,m_2)$. Consider the following min-cost flow model:
    
    -   from the source $s$, connect an edge to each of nodes $x$ and $y$, with capacities $m_1$ and $m_2$ and cost $0$;
    -   for all $i=1,\cdots,n$, connect an edge from each of nodes $x$ and $y$ to node $i$, with capacity $1$ and costs $A_i$ and $B_i$ respectively;
    -   for all $i=1,\cdots,n$, connect two edges from node $i$ to the sink $t$, with capacity $1$ and costs $0$ and $C_i-A_i-B_i$ respectively.
    
    The answer to the problem is the max-cost max-flow of this min-cost flow model. The condition $C_i-A_i-B_i\le 0$ guarantees that when the flow through node $i$ is $1$, it will preferentially choose the edge with cost $0$ to flow out. Writing this min-cost flow model as a linear-programming problem, $m_1$ and $m_2$ will appear in the inequalities representing the flow restrictions of edges $(s,x)$ and $(s,y)$ respectively. Therefore, $v(m_1,m_2)$ is indeed a concave function of $(m_1,m_2)$.
    
    To apply WQS binary search, we need to consider the optimization problem after removing the count restriction. Let $k_1$ and $k_2$ be the extra rewards for putting an index into sets $X$ and $Y$ respectively. Without the count restriction, the decision about each index is independent, so
    
    $$
    h(k_1,k_2) = \sum_{i=1}^n\max\{0,A_i+k_1,B_i+k_2,C_i+k_1+k_2\}.
    $$
    
    The answer to the original problem is given by
    
    $$
    v(m_1,m_2) = \min_{k_1,k_2} h(k_1,k_2) - k_1m_1 - k_2m_2.
    $$
    
    The total time complexity is $O(n\log^2L)$, where $O(\log L)$ is the number of binary-search steps for a single dimension.
    
    The reference implementation of the Pokémon-hunting problem is as follows:
    
    ```cpp
    --8<-- "docs/dp/code/opt/wqs-binary-search/gosha-is-hunting.cpp"
    ```

### More general restrictions

???+ example "[Codeforces 1661 F. Teleporters](https://codeforces.com/problemset/problem/1661/F)"
    There are $n$ segments whose lengths are given by the sequence $\{a_i\}$. You can arbitrarily cut them into several integer-length segments, with the goal of minimizing the total sum of the squares of all segment lengths. Find the minimum number of cuts needed to bring this sum of squares down to no more than $V$.

??? note "Solution"
    Let $f(a,m)$ be the minimum sum of squares obtainable by cutting a segment of length $a$ $m$ times. By the mean inequality, when the sum of two numbers is fixed, the smaller the difference of the two numbers, the smaller the sum of their squares. So the more uniform the segment lengths obtained after cutting, the smaller the total sum of squared lengths. But due to the integer constraint, the most uniform case is obtaining $a\bmod (m+1)$ segments of length $\lceil a/(m+1)\rceil$ and $m+1-(a\bmod (m+1))$ segments of length $\lfloor a/(m+1)\rfloor$. Therefore, we have the following expression:
    
    $$
    \begin{aligned}
    f(a,m) &= (a\bmod (m+1))\left\lceil\dfrac{a}{m+1}\right\rceil^2 + (m+1-(a\bmod (m+1)))\left\lfloor\dfrac{a}{m+1}\right\rfloor^2 \\
    &= (a\bmod (m+1))\left(\left\lfloor\dfrac{a}{m+1}\right\rfloor+1\right)^2 + (m+1-(a\bmod (m+1)))\left\lfloor\dfrac{a}{m+1}\right\rfloor^2.
    \end{aligned}
    $$
    
    The equality in the second step holds because $\lceil a/(m+1)\rceil \neq \lfloor a/(m+1)\rfloor + 1$ if and only if $a\bmod (m+1) = 0$.
    
    We can prove that the function $f(a,m)$ is a convex function of $m$. To this end, we need to extend it to the case $m\in\mathbf R_{+}$. When $\lfloor a/(m+1)\rfloor = q$,
    
    $$
    \begin{aligned}
    f(a,m) &= (a-(m+1)q)(q+1)^2 + ((m+1)(q+1)-a)q^2 \\
    &= a(2q+1) - q(q+1)(m+1).
    \end{aligned}
    $$
    
    This is a line of slope $-q(q+1)$. Therefore, $f(a,m)$ is a piecewise-linear function whose slope increases as $m$ increases. This shows that $f(a,m)$ is a convex function, and its restriction to integer points is of course also a convex function[^conv-int].
    
    Using $f(\cdot,\cdot)$, we can write the minimum sum of squares obtained by cutting all segments a total of $m$ times as the value function of the following optimization problem:
    
    $$
    v(m) = \min_{\{m_i\}}\sum_i f(a_i,m_i)\text{ subject to }\sum_i m_i=m,~m_i\in\mathbf N.
    $$
    
    This is the [infimal convolution](./slope-trick.md#infimal-convolution-minkowski-sum) of several convex functions, so it is also a convex function. If the problem asked for $v(m)$, then we could solve it with the same method as the previous examples, with time complexity $O(n\log^2L)$; but this problem asks for the smallest $m$ satisfying $v(m)\le V$. The method of computing $v(m)$ via WQS binary search and then binary-searching $m$ does not work; its complexity reaches $O(n\log^3L)$. For this problem, there are the following two handling methods.
    
    **Method one**: still binary-search the slope $k$, but the basis of the binary search is an estimate of the upper and lower bounds of $v(m)$.
    
    In the traditional WQS binary-search method, for a given slope $k$, we can compute the corresponding range of the optimal $m$. Because these $(m,v(m))$ are collinear, this amounts to determining the range of $v(m)$. Therefore, we can directly binary-search the slope $k$. After obtaining the slope $k$, we can compute the smallest $m$ via the line equation
    
    $$
    v(m) = h(k) + km.
    $$
    
    The overall complexity is $O(n\log^2L)$.
    
    To determine the range of $v(m)$, we need to determine the range of $m$. One approach is to record the corresponding largest optimal solution when computing $h(k)$, using it to compute the corresponding lower bound of $v(m)$; another approach is to use $h(k)-h(k-1)$ to obtain the corresponding upper bound of $m$, and thereby the corresponding lower bound of $v(m)$. In the reference implementation, the second approach is adopted; it does not depend on the specific structure of the problem and needs no special handling.
    
    **Method two**: rewrite the optimization problem so that the value function of the dual problem is the solution to this problem.
    
    This problem can be directly seen as the following optimization problem:
    
    $$
    m(v) = \min_{\{m_i\}} \sum_i m_i \text{ subject to }\sum_i f(a_i,m_i) \le V.
    $$
    
    The analysis of this article still applies to this problem. Hence, we can use its dual problem to solve the desired $m(v)$:
    
    $$
    m(v) = \max_{k} \sum_i\min_{m_i}(m_i - \lambda f(a_i,m_i)) + \lambda V.
    $$
    
    The overall algorithm complexity is still $O(n\log^2L)$.
    
    The reference code is as follows:
    
    === "Method one"
        The code is illustrative only; to pass the original problem's data range, 128-bit integers are needed, and the initial binary-search interval should be adjusted to $[0,10^{60}]$.
        
        ```cpp
        --8<-- "docs/dp/code/opt/wqs-binary-search/teleporters-1.cpp"
        ```
    
    === "Method two"
        The code is illustrative only; due to floating-point precision issues, it cannot pass the original problem's data range.
        
        ```cpp
        --8<-- "docs/dp/code/opt/wqs-binary-search/teleporters-2.cpp"
        ```

## Exercises

Finally, we list some problems solvable by WQS binary search, for practice:

-   [Luogu P1484 Tree Planting](https://www.luogu.com.cn/problem/P1484)
-   [Luogu P1792 \[National Training Team\] Tree Planting](https://www.luogu.com.cn/problem/P1792)
-   [Luogu P2619 \[National Training Team\] Tree I](https://www.luogu.com.cn/problem/P2619)
-   [Luogu P3620 \[APIO/CTSC2007\] Data Backup](https://www.luogu.com.cn/problem/P3620)
-   [Luogu P4072 \[SDOI2016\] The Journey](https://www.luogu.com.cn/problem/P4072)
-   [Luogu P4383 \[Eight-Province Joint Exam 2018\] Link-Cut Tree](https://www.luogu.com.cn/problem/P4383)
-   [Luogu P4983 Forget Love](https://www.luogu.com.cn/problem/P4983)
-   [Luogu P5308 \[COCI 2018/2019 #4\] Akvizna](https://www.luogu.com.cn/problem/P5308)
-   [Luogu P5633 Minimum Degree-Constrained Spanning Tree](https://www.luogu.com.cn/problem/P5633)
-   [Luogu P5896 \[IOI 2016\] aliens](https://www.luogu.com.cn/problem/P5896)
-   [Luogu P6246 \[IOI 2000\] Post Office, enhanced enhanced](https://www.luogu.com.cn/problem/P6246)
-   [AtCoder Beginner Contest 218 H - Red and Blue Lamps](https://atcoder.jp/contests/abc218/tasks/abc218_h)
-   [AtCoder Beginner Contest 305 Ex - Shojin](https://atcoder.jp/contests/abc305/tasks/abc305_h)
-   [AtCoder Regular Contest 164 E - Segment-Tree Optimization](https://atcoder.jp/contests/arc164/tasks/arc164_e)
-   [Codeforces 125 E. MST Company](https://codeforces.com/problemset/problem/125/E)
-   [Codeforces 321 E. Ciel and Gondolas](https://codeforces.com/problemset/problem/321/E)
-   [Codeforces 739 E. Gosha is hunting](https://codeforces.com/problemset/problem/739/E)
-   [Codeforces 802 O. April Fools' Problem (hard)](https://codeforces.com/contest/802/problem/O)
-   [Codeforces 958 E2. Guard Duty (medium)](https://codeforces.com/problemset/problem/958/E2)
-   [Codeforces 1279 F. New Year and Handle Change](https://codeforces.com/problemset/problem/1279/F)
-   [Codeforces 1661 F. Teleporters](https://codeforces.com/problemset/problem/1661/F)
-   [Codeforces 1799 F. Halve or Subtract](https://codeforces.com/problemset/problem/1799/F)
-   [2019 Summer Petrozavodsk Camp H. Honorable Mention](https://codeforces.com/gym/102331/problem/H)

## References and notes

-   [Wang Qinshi, "An Analysis of a Class of Binary-Search Methods"](https://github.com/hzwer/shareOI/blob/master/%E5%9F%BA%E7%A1%80%E7%AE%97%E6%B3%95/%E6%B5%85%E6%9E%90%E4%B8%80%E7%B1%BB%E4%BA%8C%E5%88%86%E6%96%B9%E6%B3%95_%E7%8E%8B%E9%92%A6%E7%9F%B3.pdf)
-   [Theoretical grounds of lambda optimization by adamant - Codeforces blog](https://codeforces.com/blog/entry/98334)
-   [A Rigorous WQS Binary-Search Method by YeahPotato - Luogu blog](https://www.luogu.com.cn/article/vsffwrc3)
-   [\[Study Notes\] A Detailed Explanation of WQS Binary Search and Common Misconceptions by ikrvxt - CSDN blog](https://blog.csdn.net/Emm_Titan/article/details/124035796)
-   [Convex conjugate - Wikipedia](https://en.wikipedia.org/wiki/Convex_conjugate)
-   [Fenchel–Moreau theorem - Wikipedia](https://en.wikipedia.org/wiki/Fenchel%E2%80%93Moreau_theorem)
-   [Subderivative - Wikipedia](https://en.wikipedia.org/wiki/Subderivative)
-   [Boyd, Stephen P., and Lieven Vandenberghe. Convex optimization. Cambridge university press, 2004.](https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf)
-   Papadimitriou, Christos H., and Kenneth Steiglitz. Combinatorial optimization: algorithms and complexity. Courier Corporation, 1998.
-   Conforti, Michele, Gérard Cornuéjols, and Giacomo Zambelli. Integer programming. Springer International Publishing, 2014.
-   Schrijver, Alexander. Combinatorial optimization: polyhedra and efficiency. Vol. 24, no. 2. Berlin: Springer, 2003.

[^high-d-convex]: In practical problems, $y$ may only take finitely many lattice points in $\mathbf R^d$. What is actually needed here is that the solution $v(y)$ of the original problem can be extended to a convex function $\tilde v:\mathbf R^d\rightarrow \mathbf R\cup\{\pm\infty\}$ on $\mathbf R^d$, i.e. that $v(y)$ is **convex-extensible**. For convenience of writing, the main text still uses $v(y)$ to denote the extended function. Geometrically intuitively, this amounts to saying that all points in the point set $\{(y,v(y))\}$ lie on the lower convex hull of their convex hull. For the one-dimensional case, this condition is [easily characterized](./slope-trick.md#convex-functions-on-discrete-point-sets) in algebraic language; but for the high-dimensional case, this is a bit more complex, and [these lecture notes](https://kzmurota.fpark.tmu.ac.jp/paper/HIMSummerSchool15Murota.pdf) provide some simple sufficient conditions.

[^other-conditions]: The condition provided in the theorem seems slightly stronger than a convex function, but for the cases encountered in competitive programming, especially when $X$ is a finite set, merely emphasizing a convex function is already sufficient. The function $\tilde v$ extended from a proper convex function $v$ on a discrete set is necessarily a lower-semi-continuous convex function, because the convex hull of finitely many points is necessarily a closed convex hull, and a so-called lower-semi-continuous convex function is equivalent to one whose epigraph is a closed convex hull. As for the word "proper" in proper convex function, it is guaranteed as long as $v(y)$ attains a finite value at at least one point and is a convex function.

[^mst]: The minimum-spanning-tree problem has two common [methods](https://math.arizona.edu/~glickenstein/math443f14/golari.pdf) of being written as a linear-programming problem: the subtour-elimination formulation and the cut-based formulation. Only the former modeling method can guarantee that the resulting linear-programming problem is equivalent to the original problem.

[^edge-swap]: This lemma also holds for a general [matroid](../../math/matroid.md). It is called the **symmetric base-exchange property**; for related material refer to the [Wikipedia page](https://en.wikipedia.org/wiki/Basis_of_a_matroid). Therefore, this problem's conclusion about convexity can be generalized to a general matroid.

[^conv-int]: Of course, $f(a,m)$ and the convex hull of the function obtained by restricting it to integer points are not the same, because $f(a,m)$ may have extreme points at non-integer positions. This shows that we cannot directly use $f(a,m)$ with a real-valued domain in the optimization problem of this problem.
