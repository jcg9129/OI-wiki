## Introduction

For a class of two-dimensional DP problems, if their value function $f(i,x)$ is a convex function of $x$ for each fixed $i$, then regarding the function $f(i,\cdot)$ as a whole as the state at $i$ and maintaining its difference (or slope)

$$
\Delta f(i,x) = f(i,x+1)-f(i,x)
$$

rather than the function itself can often optimize the transition. This idea of optimizing DP is called Slope Trick.

???+ info "\"Slope\""
    Because the functions involved in most problems only take values at integer points, calling it the difference or the slope makes no essential difference; this article, following the term Slope Trick, uniformly calls it the slope.

In specific problems, the way the slope is maintained may vary. If the range of the slope is narrow, maintaining the points where the slope changes (i.e. the kinks) is more convenient; whereas if the function's domain is narrow, maintaining the slope sequence itself may be more convenient. In more complex cases, one may need to simultaneously maintain the value of each slope segment and the length of that segment. Whatever the specific maintenance method, the essence of this kind of problem is exploiting the fact that the slope sequence changes little during the state transition to simplify the transition. Therefore, they can all be called Slope Trick.

## Convex functions

Before discussing specific problems, it is necessary to first understand the basic properties of convex functions and how their slopes change under various transformations of convex functions.

### Convex functions on the real line

The more general definition of a convex function is given on $\mathbf R$.

![](../images/slope-trick/epigraph-convex-def.svg)

???+ abstract "Convex functions on $\mathbf R$"
    If a function $f:\mathbf R\rightarrow\mathbf R\cup\{\pm\infty\}$ satisfies, for all $x,y\in\mathbf R$ and $\alpha\in(0,1)$,
    
    $$
    f(\alpha x+(1-\alpha)y) \le \alpha f(x)+(1-\alpha)f(y),
    $$
    
    then the function $f$ is called a **convex function**, where the arithmetic rules for $\pm\infty$ stipulate that $\pm\infty$ multiplied by any positive real number or added to any real number equals itself, and for any real number $x\in\mathbf R$, $-\infty<x<+\infty$.

Of course, if the inequality sign is changed to $\ge$, it is correspondingly called a concave function[^convex-def]. Because for a concave function $f$, $-f$ is always a convex function, this section only considers convex functions.

???+ info "This article only considers proper convex functions"
    To avoid discussing the value of $\infty-\infty$ and extra complex analysis, this article, when discussing concepts related to convex functions, always assumes by default that the function never attains $-\infty$ and is not always $+\infty$. Such a convex function is called a **proper convex function**. This is already sufficient for understanding the content involved in competitive programming.

Of course, the function $f$ is often not defined for all real numbers. If the domain of the function $f$ is only a subset of $\mathbf R$, then it can be extended to a function on $\mathbf R$:

$$
\tilde f(x) = \begin{cases} f(x), & x\in\operatorname{dom}f,\\ +\infty,& x\notin\operatorname{dom}f.\end{cases}
$$

Then, $f$ is called a convex function if and only if the corresponding $\tilde f$ satisfies the above definition of a convex function. Therefore, unless otherwise noted, the domain of the convex functions mentioned in this article is the real set $\mathbf R$. Clearly, a convex function $f$ can only attain finite values on one interval (i.e. a convex subset of $\mathbf R$).

???+ example "Simple examples"
    Common examples of convex functions include:
    
    1.  the constant function: $f(x)=c$, where $c\in\mathbf R$;
    2.  the linear function: $f(x)=kx+b$, where $k,b\in\mathbf R$ and $k\neq 0$;
    3.  the absolute-value function: $f(x)=|x-a|$, where $a\in\mathbf R$;
    4.  the result of restricting any convex function to some interval, for example $0_{[a,b]}(x)$ (also called the indicator function of $[a,b]$ in the context of convex analysis).

Of course, more complex convex functions can be composed via the convexity-preserving transformations mentioned below.

### Convex functions on discrete point sets

In competitive programming, many functions are defined only at some integer values. They are generally not (the above-defined) convex functions, because their domain is no longer a convex set. To handle this case, we need to separately define the convexity of a function on a discrete point set. Simply put, we first linearly interpolate the function to extend its domain to an interval, and then judge its convexity.

![](../images/slope-trick/epigraph-convex-discrete.svg)

???+ abstract "Convex functions on discrete point sets"
    Let $S\subset\mathbf R$ be a discrete point set, i.e. for any closed interval $[a,b]$, $S\cap[a,b]$ is a finite set. For a function $f:S\rightarrow\mathbf R\cup\{\pm\infty\}$, we can define a function $\tilde f:\mathbf R\rightarrow\mathbf R\cup\{\pm\infty\}$ such that:
    
    -   when $x\in S$, $\tilde f(x)=f(x)$,
    -   when $x\in(\inf S,\sup S)\setminus S$, let $s_-=\max\{s\in S:s\le x\}$, $s_+=\min\{s\in S:s\ge x\}$; then
    
        $$
        \tilde f(x) = \dfrac{s_+-x}{s_+-s_-}f(s_-)+\dfrac{x-s_-}{s_+-s_-}f(s_+),
        $$
    -   when $x\notin[\inf S,\sup S]$, $\tilde f(x)=+\infty$.
    
    Then, if $\tilde f(x)$ is a convex function on $\mathbf R$, $f(x)$ is called a **convex function** on $S$.

Because convex functions on $\mathbf R$ are more convenient to handle, when this article mentions convex functions, unless otherwise noted, it means convex functions on $\mathbf R$. If some function in this article is only given values at some integer points, then its values at other real numbers should be determined by $\tilde f$ in the definition, which is equivalent to directly discussing the corresponding piecewise-linear function $\tilde f$.

Convex functions on the integer set $\mathbf Z$ have a more intuitive equivalent definition:

???+ note "Equivalent definition of convex functions on $\mathbf Z$"
    A function $f:\mathbf Z\rightarrow\mathbf R\cup\{\pm\infty\}$ is convex if and only if
    
    $$
    f(x)-f(x-1)\le f(x+1)-f(x)
    $$
    
    holds for all $x\in\mathbf Z$.

??? note "Proof"
    This proposition is a simple corollary of the slope characterization of convex functions.
    
    If $f$ is a convex function on $\mathbf Z$, then by the weak increase of the slope,
    
    $$
    \Delta f(x-1,x)\le \Delta f(x-1,x+1) \le\Delta f(x,x+1).
    $$
    
    This is the above condition.
    
    Conversely, if the above condition holds, then for any $x_1<x_2$,
    
    $$
    \Delta f(x_1,x_2) = \dfrac{1}{x_2-x_1}\sum_{i=x_1}^{x_2-1}\left(f(i)-f(i-1)\right).
    $$
    
    This equals the arithmetic mean of the differences over all $i$ with $x_1\le i<x_2$. If $x_2$ increases by one, it amounts to inserting a larger difference; if $x_1$ increases by one, it amounts to removing a smallest difference. Both operations raise the mean. This shows the slope $\Delta f(x_1,x_2)$ weakly increases, i.e. $f$ is a convex function on $\mathbf Z$.

That is, as long as the slope (difference) is monotonically non-decreasing, the sequence can be regarded as a convex function on $\mathbf Z$.

### Two characterizations of convex functions

In fact, the way of characterizing convex functions by the slope can also be generalized to the general case.

???+ note "Slope characterization of convex functions"
    Let $S$ be $\mathbf R$ or a discrete subset of it; then a function $f:S\rightarrow\mathbf R\cup\{\pm\infty\}$ is a convex function if and only if the slope
    
    $$
    \Delta f(x_1,x_2) = \dfrac{f(x_2)-f(x_1)}{x_2-x_1}
    $$
    
    is a weakly increasing function of both $x_1$ and $x_2$ for any $x_1,x_2\in S$ with $x_1<x_2$.

??? note "Proof"
    For a function $f(x)$ on $\mathbf R$ and $x_1<x_2$, for $\alpha\in(0,1)$, let $x_3=\alpha x_1+(1-\alpha)x_2$; then
    
    $$
    \Delta f(x_1,x_3) \le \Delta f(x_1,x_2) \le \Delta f(x_3,x_2)
    $$
    
    is equivalent to
    
    $$
    \dfrac{f(x_3)-f(x_1)}{1-\alpha} \le f(x_2)-f(x_1) \le \dfrac{f(x_2)-f(x_3)}{\alpha}.
    $$
    
    Both inequalities are equivalent to $f(x_3)\le\alpha f(x_1)+(1-\alpha)f(x_2)$, i.e. the convexity of the function $f(x)$.
    
    For a function $f(x)$ on a discrete subset $S$ of $\mathbf R$, the necessity of the weak-increase-of-slope condition can be deduced from the convexity of $\tilde f(x)$. Now we prove its sufficiency; to this end we only need to prove that $\Delta\tilde f(x_1,x_2)$ is also weakly increasing. Let $S=\{s_i\}$ with $s_i$ strictly increasing in $i$, and let $s_{i_1}\le x_1\le s_{i_1+1}$ and $s_{i_2}\le x_2\le s_{i_2+1}$; naturally $i_1\le i_2$. Let $\Delta_i=\Delta f(s_i,s_{i+1})$; then we can prove $\Delta_{i_1}\le\Delta\tilde f(x_1,x_2)\le\Delta_{i_2}$.
    
    This has two cases. If $i_1=i_2$, then $\Delta_{i_1}=\Delta\tilde f(x_1,x_2)=\Delta_{i_2}$, and the inequality clearly holds. Otherwise,
    
    $$
    \Delta\tilde f(x_1,x_2) = \dfrac{1}{x_2-x_1}\left((s_{i_1+1}-x_1)\Delta_{i_1}+(x_2-s_{i_2})\Delta_{i_2}+\sum_{j=i_1+1}^{i_2-1}(s_{j+1}-s_j)\Delta_j\right).
    $$
    
    By the slope increase on $S$, $\Delta_i$ increases in $i$, so $\Delta_{i_1}\le\Delta\tilde f(x_1,x_2)\le\Delta_{i_2}$.
    
    Using this conclusion, for $x_1<x_2$ and $\alpha\in(0,1)$, let $x_3=\alpha x_1+(1-\alpha)x_2$, and take $i_3$ such that $s_{i_3}\le x_3\le s_{i_3+1}$ holds; then
    
    $$
    \Delta\tilde f(x_1,x_3) \le \Delta_{i_3} \le \Delta\tilde f(x_3,x_2).
    $$
    
    Substituting the expression for $x_3$ gives the convexity of $\tilde f(x)$.

The slope being monotonically non-decreasing can be seen as an equivalent definition of a convex function. Precisely because the slope of a convex function has monotonicity, when maintaining the slope one usually needs to choose data structures such as a [heap (priority queue)](../../ds/heap.md) or a [balanced tree](../../ds/bst.md).

This article will also use another equivalent characterization of convex functions. For a function $f:\mathbf R\rightarrow\mathbf R\cup\{\pm\infty\}$, we can examine the region above the function's graph in the plane, i.e.

$$
\operatorname{epi} f = \{(x,y)\in\mathbf R^2 : y\ge f(x)\}.
$$

This region is also called the **epigraph** of the function $f$. The convexity of a function is equivalent to the convexity of its epigraph:

???+ note "Epigraph characterization of convex functions"
    A function $f:\mathbf R\rightarrow\mathbf R\cup\{\pm\infty\}$ is a convex function if and only if $\operatorname{epi}f$ is a convex set in $\mathbf R^2$.

??? note "Proof"
    If $f$ is a convex function, then for $(x_1,y_1),(x_2,y_2)\in\operatorname{epi}f$ and any $\alpha\in(0,1)$,
    
    $$
    \alpha y_1+(1-\alpha)y_2 \ge \alpha f(x_1)+(1-\alpha)f(x_2) \ge f(\alpha x_1+(1-\alpha) x_2).
    $$
    
    So $\alpha(x_1,y_1)+(1-\alpha)(x_2,y_2)\in\operatorname{epi}f$.
    
    Conversely, if $\operatorname{epi}f$ is a convex set, then for any $x_1<x_2$ and $\alpha\in(0,1)$,
    
    $$
    \alpha(x_1,f(x_1))+(1-\alpha)(x_2,f(x_2)) \in \operatorname{epi}f.
    $$
    
    This is equivalent to $\alpha f(x_1)+(1-\alpha)f(x_2)\ge f\left(\alpha x_1+(1-\alpha)x_2\right)$, i.e. the convexity of $f$.

As we will see shortly, using the epigraph, we can connect the infimal convolution of convex functions with the Minkowski sum of convex sets.

## Transformations of convex functions

Next, this article introduces some convexity-preserving transformations frequently encountered in Slope Trick.

### Non-negative linear combination

For convex functions $f$ and $g$ and non-negative real numbers $\alpha,\beta\ge0$, the function $\alpha f+\beta g$ is also a convex function. Moreover,

$$
\Delta(\alpha f+\beta g) = \alpha\Delta f + \beta\Delta g.
$$

Therefore, if we have maintained the slopes of the convex functions $f$ and $g$, to obtain the slope of their non-negative linear combination $\alpha f+\beta g$, we only need to compute segment by segment.

In problems of maintaining slopes, often the form of one of the functions is relatively simple, in which case the modification complexity can be reduced via lazy tags. In problems of maintaining kinks, to compute the slope kinks of $f+g$, we only need to merge the slope kinks of $f$ and $g$.

### Infimal convolution (Minkowski sum)

Another common operation on convex functions is the infimal convolution. For functions $f$ and $g$, the function

$$
h(x) = \inf_{y\in\mathbf R}f(y)+g(x-y)
$$

is called the **infimal convolution**[^inf-conv] of $f$ and $g$. If $f$ and $g$ are both convex functions, their infimal convolution is also a convex function.

![](../images/slope-trick/epigraph-convex-minkowski.svg)

??? example "Explanation of the figure"
    As shown in the figure, to find the infimal convolution $h$ of $f$ and $g$, we can regard each point on the graph of $f$ (the red dashed line in the third figure) as the origin, and draw the graph of $g$ (the blue dashed line in the third figure) in the corresponding coordinate system. As the coordinate origin moves along the graph of $f$, the outline of the trajectory of the graph (epigraph) of $g$ (i.e. the lower convex hull) is the graph of $h$. We can see that each slope segment of $h$ is either a slope segment of $f$ or a slope segment of $g$: they are just resorted by slope magnitude. In this process, the roles of $f$ and $g$ can be swapped, i.e. letting the graph of $f$ move along the graph of $g$ gives a consistent result.

Geometrically intuitively, $\operatorname{epi}h$ is the [Minkowski sum](../../geometry/convex-hull.md#minkowski-sum) of $\operatorname{epi}f$ and $\operatorname{epi}g$. If $f$ and $g$ are both piecewise-linear functions, then $h$ is likewise a piecewise-linear function, and its slope segments can be seen as the result of merging (and resorting) the slope segments of $f$ and $g$.

??? note "Proof"
    Let $f,g$ both be convex functions and $h$ their infimal convolution. Let $x_1<x_2$ and $\alpha\in(0,1)$. By the definition of the infimal convolution, for any $\varepsilon>0$, there exist $y_i,z_i\in\mathbf R$ such that $y_i+z_i=x_i$ and
    
    $$
    h(x_i) + \varepsilon > f(y_i) + g(z_i).
    $$
    
    Hence, combining the convexity of $f,g$ and the definition of $h$,
    
    $$
    \begin{aligned}
    \alpha h(x_1)+(1-\alpha)h(x_2) + \varepsilon 
    &> \alpha f(y_1) + (1-\alpha) f(y_2) + \alpha g(z_1) + (1-\alpha) g(z_2)\\
    &\ge f\left(\alpha y_1+(1-\alpha)y_2\right) + g\left(\alpha z_1+(1-\alpha)z_2\right)\\
    &\ge h(\alpha x_1+(1-\alpha)x_2).
    \end{aligned}
    $$
    
    Because $\varepsilon>0$ is chosen arbitrarily,
    
    $$
    \alpha h(x_1)+(1-\alpha)h(x_2) \ge h(\alpha x_1+(1-\alpha)x_2).
    $$
    
    This gives the convexity of $h$.
    
    Then, for the geometric intuition, strictly speaking we can only prove the following conclusion:
    
    $$
    \operatorname{epi} f + \operatorname{epi} g\subseteq \operatorname{epi}h \subseteq \operatorname{cl}(\operatorname{epi} f + \operatorname{epi} g).
    $$
    
    where $\operatorname{cl}$ denotes the closure.
    
    For any $(x,y)\in\operatorname{epi} f + \operatorname{epi} g$, there exist $(x_1,y_1)\in\operatorname{epi} f$ and $(x_2,y_2)\in\operatorname{epi} g$ such that $x=x_1+x_2$ and
    
    $$
    y = y_1+y_2 \ge f(x_1)+g(x_2) \ge h(x_1+x_2)=h(x).
    $$
    
    Hence, $(x,y)\in\operatorname{epi}h$. This shows $\operatorname{epi} f + \operatorname{epi} g\subseteq \operatorname{epi}h$.
    
    Conversely, for any $(x,y)\in\operatorname{epi}h$, $y\ge h(x)$. By the definition of $h$, for any $\varepsilon>0$, there exists $x_1+x_2=x$ such that
    
    $$
    y + \varepsilon > f(x_1) + g(x_2).
    $$
    
    Let $y_1=f(x_1)$ and $y_2=g(x_2)$; then $y+\varepsilon>y_1+y_2$. This shows that for any $\varepsilon>0$, $(x_1,y_1)+(x_2,y_2)\in\operatorname{epi} f + \operatorname{epi} g$ lies on the segment connecting the points $(x,y)$ and $(x,y+\varepsilon)$. Taking $\varepsilon\rightarrow 0$ gives $\operatorname{epi}h \subseteq \operatorname{cl}(\operatorname{epi} f + \operatorname{epi} g)$.
    
    So $\operatorname{epi} f + \operatorname{epi} g = \operatorname{epi}h$ if and only if it is a closed convex set. One condition making this hold is that $f$ and $g$ are both proper convex functions and [lower semi-continuous](https://en.wikipedia.org/wiki/Semi-continuity). For competitive-programming applications, this is already sufficient; for example, piecewise-linear functions always satisfy these conditions.

In practical problems, if one of $f$ and $g$ has few slope segments, we can directly insert the fewer slope segments into the more numerous ones; otherwise, we may need to use methods such as [heuristic merging](../../graph/dsu-on-tree.md) or a [mergeable heap](../../ds/heap.md) to reduce the overall merging complexity, or find a corresponding handling method according to the specific problem.

### The extremum operation

The maximum of two convex functions is still a convex function, but the minimum of two convex functions is not necessarily a convex function.

Many common minimum operations can be turned into infimal convolutions:

???+ example "Examples"
    -   $f(x)=\min_{y\in [x+a,x+b]}g(y)$ is still a convex function, because it can be seen as an infimal convolution:
    
        $$
        f(x) = \min_{y\in\mathbf R}g(y) + 0_{[-b,-a]}(x-y).
        $$
    -   $f(x)=\min\{g(x-a_i)+b_i\}$ is a convex function on $\mathbf Z$, as long as $g(x)$ is a convex function on $\mathbf Z$ and the function $h:a_i\mapsto b_i$ defined on the finite set $\{a_i\}\subset\mathbf Z$ is also a convex function on that discrete set. This is because the extended function $\tilde f(x)$ can be seen as an infimal convolution:
    
        $$
        \tilde f(x) = \min_{y\in\mathbf R}\tilde h(y)+\tilde g(x-y).
        $$
    
        Therefore, the pre-extension function $f(x)$ is also a convex function.

But not all minimum operations preserve convexity.

???+ example "Counterexample"
    Let $g(x)$ be a convex function; the function $f(x)=\min\{g(x-1)+kx,g(x)\}$ is not necessarily a convex function.

In some special problems, although the dynamic-programming transition equation can be written in the form of the minimum of two convex functions and is hard to turn into an infimal-convolution form, the value function can still preserve convexity. In practice, one usually needs to combine tabulation and guessing to find a reasonable slope-transition method for this kind of problem.

Having understood convex functions and their common transformations, we can understand the method of Slope Trick optimizing DP through specific problems. The examples in this article are roughly divided into two groups, maintaining kinks and maintaining slopes, to understand the common operations and implementation details of these two maintenance methods. But, as emphasized earlier, the maintenance method is not the essence of Slope Trick; one should choose the appropriate slope-segment maintenance method according to the specific problem's needs.

## Maintaining kinks

This kind of problem usually appears in problems that require minimizing the sum of several absolute values. Because in this kind of problem, the absolute value of the slope of the value function is not large, maintaining the kinks where the slope changes is more convenient.

Maintaining kinks means maintaining the points in a piecewise-linear function where the slope changes. This is equivalent to, for each slope segment $[l_i,r_i]$ with slope $k_i$, maintaining only its endpoint information, without additionally maintaining the slope itself; therefore, in this kind of problem, each time the slope changes it should change by only a fixed amount. For example, if we maintain the kink set $\xi_{-s}\le\cdots\le\xi_{-1}\le\xi_{1}\le\cdots\le\xi_{t}$, it amounts to saying: the slope in the interval $[\xi_{-1},\xi_1]$ is $0$; each kink passed to the left decreases the slope by one, and each kink passed to the right increases the slope by one; hence, in the interval $[\xi_2,\xi_3]$ the slope is $2$, in the interval $[\xi_{-3},\xi_{-2}]$ the slope is $-2$, and so on. In formal language, the function can be written using slope kinks as

$$
f(x) = f(\xi_1) + \sum_{i=-s}^{-1}\max\{\xi_i-x,0\} + \sum_{i=1}^{\ell}\max\{x-\xi_i,0\}.
$$

Its minimum is $f(\xi_{-1})=f(\xi_1)$, and it can be attained at any position in the interval $[\xi_{-1},\xi_1]$.

![](../images/slope-trick/epigraph-convex-kinks.svg)

### Example: minimum-cost increasing sequence

???+ example "[\[BalticOI 2004\] Sequence](https://www.luogu.com.cn/problem/P4331)"
    Given a sequence $\{a_i\}$ of length $n$, find a strictly increasing sequence $\{b_i\}$ that minimizes $\sum_i|a_i-b_i|$; output the minimum value and any one optimal scheme $\{b_i\}$.

??? note "Solution"
    First, $\{b_i\}$ being strictly increasing is equivalent to $\{b'_i\}=\{b_i-i\}$ being weakly increasing. Therefore, we can find, for $\{a'_i\}=\{a_i-i\}$, the weakly increasing sequence $\{b'_i\}=\{b_i-i\}$ with the smallest difference, and then recover the sequence $\{b_i\}$.
    
    Consider the naive DP solution. Let $f_i(x)$ be the minimum difference between the selected numbers and the first $i$ numbers of $\{a'_i\}$ when the first $i$ numbers of the sequence $\{b'_i\}$ have been selected and the $i$-th number does not exceed $x$:
    
    $$
    f_i(x) = \min\sum_{j=1}^i|a'_j-b'_j|\text{ s.t. }b'_1\le b'_2\le\cdots\le b'_i\le x.
    $$
    
    We easily obtain the state-transition equation as
    
    $$
    f_i(x) = \min_{y\le x}f_{i-1}(y)+|a'_i-y|.
    $$
    
    The initial state is $f_0(x)\equiv 0$, and what is finally sought is $\min_xf_n(x)$. Using the transformations of convex functions mentioned earlier, going from $f_{i-1}(x)$ to $f_i(x)$ requires two transformations:
    
    1.  First, add $|a'_i-x|$, which amounts to increasing all slope segments in the interval $(-\infty,a'_i]$ by $-1$ and all slope segments in the interval $[a'_i,+\infty)$ by $1$;
    2.  Take the minimum of the resulting function, turning $g(x)=f_{i-1}(x)+|a'_i-x|$ into $f_i(x)=\min_{y\le x}g(y)$. By the earlier analysis, this amounts to the infimal convolution of $g(x)$ and $0_{[0,+\infty)}$. Because the latter has only one slope segment, with slope $0$ extending rightward to infinity, inserting it into the slope segments of $g(x)$ amounts to deleting all positive slope segments therein.
    
    Having clarified these operations, we can already directly maintain all slope segments with a balanced tree, but the code is rather complex. Note that in the problem the slope changes by at most $1$ each time, so the absolute values of all slope segments do not exceed $n$. Instead of directly maintaining slope segments, it is more convenient to directly maintain slope kinks.
    
    Let the kink set of $f_{-1}(x)$ be $\xi_{-k}\le\cdots\le\xi_{-1}\le\xi_{1}\le\cdots\le\xi_{\ell}$. Then, the above two operations respectively correspond to:
    
    1.  Add a kink $a'_i$ of a negative slope segment and a kink $a'_i$ of a positive slope segment;
    2.  Pop all kinks $\xi_1,\cdots,\xi_{\ell}$ of positive slope segments.
    
    In actual maintenance, because after each operation there are no kinks of positive slope segments, i.e. the slope kinks have the form $\xi_{-k}\le\cdots\le\xi_{-1}$, and the operation always happens at the boundary of positive and negative slope segments, we can directly maintain a max-heap storing all kinks. The two operations respectively correspond to:
    
    1.  Insert $a'_i$ twice;
    2.  Pop the heap top.
    
    Of course, after each operation we need to maintain the minimum value of the current function. Because after the operation there is no positive slope segment, the function minimum is its value at the top of the max-heap. Let the heap top before each operation be $\xi_{-1}$ and the minimum be $f_{i-1}(\xi_{-1})$. Because the popped heap top is the smallest kink of the positive slope segments, the function minimum equals the function value there, so we can directly compute the function value at the heap top before popping, i.e.
    
    $$
    f_{i-1}(\max\{a'_i,\xi_{-1}\})+|\max\{a'_i,\xi_{-1}\}-a'_i|=f_{i-1}(\xi_{-1})+\max\{0,\xi_{-1}-a'_i\}.
    $$
    
    Here, the first term is equal because $f_{i-1}(x)$ has no positive slope segment. Therefore, each time we only need to keep accumulating $\max\{0,\xi_{-1}-a'_i\}$ onto the minimum.
    
    This problem also requires outputting an optimal scheme. Because at the end of the operations the optimal solution is the heap top, the value of $b'_n$ can be directly determined. If we already know the $i$-th optimal solution $b'_i$, to solve for the optimal solution of $f_{i-1}(x)$ satisfying $x\le b'$, we only need to note that because $f_{i-1}(x)$ is convex, the closer to its global minimum point, the better the solution; hence, as long as we record the global minimum point of $f_{i-1}(x)$ and take its minimum with $b'_i$, we obtain the optimal $b'_{i-1}$.
    
    The time complexity is $O(n\log n)$.
    
    ```cpp
    --8<-- "docs/dp/code/opt/slope-trick/sequence.cpp"
    ```

Template problems:

-   [Codeforces 713 C. Sonya and Problem Without a Legend](https://codeforces.com/problemset/problem/713/C)
-   [Luogu P2893 \[USACO08FEB\] Making the Grade G](https://www.luogu.com.cn/problem/P2893)
-   [Luogu P4331 \[BalticOI 2004\] Sequence](https://www.luogu.com.cn/problem/P4331)
-   [Luogu P4597 Sequence](https://www.luogu.com.cn/problem/P4597)
-   [AtCoder 2nd Dwango Challenge Qualifier E - Fireworks](https://atcoder.jp/contests/dwango2016-prelims/tasks/dwango2016qual_e)

### Example: the case with restricted transitions

???+ example "[\[NOISG 2018 Finals\] Safety](https://www.luogu.com.cn/problem/P11598)"
    Given a sequence $\{a_i\}$ of length $n$, find a sequence $\{b_i\}$ satisfying $|b_i-b_{i-1}|\le h$ for all $1<i\le n$ and minimizing $\sum_i|a_i-b_i|$; output the minimum value.

??? note "Solution"
    The content is roughly similar to the previous problem, except the restriction on the sequence $\{b_i\}$ has changed. Likewise, let $f_i(x)$ be the minimum difference of the first $i$ numbers when the $i$-th number is $x$:
    
    $$
    f_i(x) = \min\sum_{j=1}^i|a_j-b_j|\text{ s.t. }|b_{j-1}-b_j|\le h,\forall 1<j\le i,~b_i=x.
    $$
    
    From this, the state-transition equation is
    
    $$
    f_i(x) = |a_i-x| + \min_{|y-x|\le h} f_{i-1}(y). 
    $$
    
    The initial condition is $f_0(x)\equiv 0$. What is finally sought is still $\min_xf_n(x)$.
    
    The state transition is decomposed into operations on convex functions, in two steps:
    
    1.  First take the extremum of $f_{i-1}(x)$, turning it into $\min_{|y-x|\le h} f_{i-1}(y)$, which amounts to the infimal convolution of $f_{i-1}(x)$ and $0_{[-h,h]}(x)$;
    2.  Then add the resulting function to $|a_i-x|$.
    
    Likewise, because the slope changes by only one each time, we can consider maintaining kinks. Then these two operations can be described as:
    
    1.  Move all negative slope segments left by $h$ and all positive slope segments right by $h$;
    2.  Insert $a_i$ twice.
    
    Clearly, for this problem, maintaining the positive and negative slope segments separately is more convenient. Because the operations mainly concentrate near the zero slope segment, consider using a [double-ended heap (opposing heaps)](../../ds/binary-heap.md#opposing-heaps), i.e. maintaining the kinks of the negative and positive slope segments with a max-heap and a min-heap respectively. The overall translation of the kinks is done with lazy tags. Because the second operation requires inserting an $a_i$ into each of the two heaps, and after insertion the top of the max-heap is not necessarily still less than or equal to the top of the min-heap. In this case, swap the two heap tops until the size relationship of the tops is satisfied.
    
    Finally, consider how to update the minimum during the operations. Because the first, translation, operation does not change the minimum, we only need to consider the operation of swapping the heap tops. Let $\xi_{-1}>\xi_1$; when swapping the heap tops $\xi_{-1}$ and $\xi_1$, the function changes from
    
    $$
    \max\{0,x-\xi_{-1}\}+\max\{0,x-\xi_1\}
    $$
    
    to
    
    $$
    \max\{0,x-\xi_{1}\}+\max\{0,x-\xi_{-1}\}.
    $$
    
    In this process, the shape of the function is unchanged, only translated down by $|\xi_{-1}-\xi_1|$. Therefore, to keep the function unchanged before and after swapping the heap tops, we only need to accumulate $|\xi_{-1}-\xi_1|$ onto the minimum.
    
    The time complexity of the algorithm is still $O(n\log n)$, because after each element is added, the operation of swapping the heap tops is executed at most once.
    
    ```cpp
    --8<-- "docs/dp/code/opt/slope-trick/safety.cpp"
    ```

Template problems:

-   [Luogu P4272 \[CTSC2009\] Sequence Transformation](https://www.luogu.com.cn/problem/P4272)
-   [Luogu P11598 \[NOISG 2018 Finals\] Safety](https://www.luogu.com.cn/problem/P11598)
-   [AtCoder Beginner Contest 217 H - Snuketoon](https://atcoder.jp/contests/abc217/tasks/abc217_h)
-   [AtCoder Regular Contest 070 E - NarrowRectangles](https://atcoder.jp/contests/arc070/tasks/arc070_c)
-   [AtCoder Regular Contest 123 D - Inc, Dec - Decomposition](https://atcoder.jp/contests/arc123/tasks/arc123_d)

## Maintaining slopes

There are also some problems where maintaining the slope is more convenient. This kind of problem can also usually be solved with the ideas of [regret greedy](../../basic/greedy.md#the-regret-approach) or simulated min-cost flow. In the min-cost flow model, the minimum cost is often a convex function of the flow, which provides the basis for using Slope Trick.

### Example: the stock-trading problem

???+ example "[Codeforces 865 D. Buy Low Sell High](https://codeforces.com/problemset/problem/865/D)"
    Given a sequence of stock prices over $n$ days $\{p_i\}$ (all positive), with initial holding $0$, each day you can buy one share, sell one share, or not trade; find the maximum profit after $n$ days.

??? note "Solution"
    First consider the naive DP solution. Let $f_i(x)$ be the maximum profit when the number of shares held at the end of day $i$ is $x\ge 0$; then
    
    $$
    f_i(x) = \max\{f_{i-1}(x-1)-p_i,f_{i-1}(x),f_{i-1}(x+1)+p_i\}.
    $$
    
    The initial state is $f_0(0)=0$, and for all $x\neq 0$, $f_0(x)=-\infty$. The answer to the problem is $f_n(0)$.
    
    Going from $f_{i-1}(x)$ to $f_i(x)$ requires two transformations:
    
    1.  Take the supremal convolution of $f_{i-1}(x)$ with the piecewise-linear function $\tilde h(x)$ (clearly a concave function) corresponding to the function
    
        $$
        h_i(x) = \begin{cases}p_i,&x=-1,\\0,&x=0,\\-p_i,&x=1\end{cases}
        $$
    
        ;
    2.  Because this causes the function to have finite values in the interval $[-1,0)$, contradicting the requirement $x\ge 0$, we need to take the part of the function in $[0,+\infty)$.
    
    Turning them into changes of slope segments gives the following two steps:
    
    1.  Insert a slope segment of length $2$ and slope $-p_i$;
    2.  Delete, among the slope segments with finite slope, the one with the largest slope and length $1$.
    
    Because the length of a slope segment is always a natural number, we may as well maintain several length-one slope segments, so we only need to record the slope of each segment. Because we only need insertion and max-access operations, we only need a max-heap. The operations have two steps:
    
    1.  Insert $-p_i$ twice;
    2.  Pop the heap top.
    
    We also need to maintain the value of $f_i(0)$. Because the function obtained in the first step has value $f_{i-1}(0)+p_i$ at $x=-1$, its value at $x=0$ is that value plus the heap top about to be popped—which is the slope of the function on the interval $[-1,0]$. Because the truncation does not change the function value at $x=0$, this is $f_i(0)$.
    
    Comparing this algorithm's implementation with the code of the [minimum-cost increasing sequence](#example-minimum-cost-increasing-sequence) above, we can see that this algorithm is equivalent to finding the minimum cost of turning the stock prices into a weakly decreasing sequence.
    
    The time complexity is $O(n\log n)$.
    
    ```cpp
    --8<-- "docs/dp/code/opt/slope-trick/stock.cpp"
    ```

Template problems:

-   [Codeforces 865 D. Buy Low Sell High](https://codeforces.com/problemset/problem/865/D)

### Example: the earth-moving problem

???+ example "[\[USACO16OPEN\] Landscaping P](https://www.luogu.com.cn/problem/P2748)"
    Given sequences $\{a_i\}$ and $\{b_i\}$ of length $n$, representing the amount of dirt the $i$-th garden already has and the amount it needs (no more and no less). Buying one unit of dirt to put into any garden costs $X$, hauling one unit of dirt away from any garden costs $Y$, and transporting one unit of dirt from garden $i$ to garden $j$ costs $Z|i-j|$. Find the minimum cost of satisfying all gardens' needs. ($a_i,b_i\le 10$)

??? note "Solution"
    Consider the naive DP solution. Let $f_i(x)$ be the minimum cost of satisfying the first $i$ gardens' needs with a net surplus of $x$ units of dirt transported to the later gardens. If $x<0$, it amounts to a net deficit of $|x|$ units of dirt that need to be transported from the later gardens. Then we can write the state-transition equation as
    
    $$
    f_i(x) = \min_{y\in\mathbf R} f_{i-1}(y) + |y|Z + h((x-y)+(b_i-a_i)).
    $$
    
    where the function $h(\delta)$ denotes the cost when the net dirt purchase of the current garden is $\delta$, i.e.
    
    $$
    h(\delta) = \max\{0,\delta\}X + \max\{0,-\delta\}Y = \max\{\delta X,-\delta Y\}.
    $$
    
    It is clearly a convex function. The meaning of this state-transition equation is
    
    -   when the net surplus dirt of the previous $i-1$ gardens is $y$, the minimum cost is $f_{i-1}(y)$;
    -   the cost of transporting the net surplus (deficit) dirt between $i$ and $i-1$ is $|y|Z$;
    -   the minimum cost of adjusting the $i$-th garden's dirt from $a_i$ to $b_i$ via buying and selling, and adjusting the net surplus dirt from $y$ to $x$, is $h((x-y)+(b_i-a_i))$.
    
    The initial state is $f_0(0)=0$, and for all $x\neq 0$, $f_0(x)=+\infty$. The answer to the problem is $f_n(0)$.
    
    Transforming the function $f_{i-1}(x)$ into $f_i(x)$ can be divided into three steps:
    
    1.  First, add $|x|Z$ to get $f_{i-1}(x)+|x|Z$;
    2.  Then, take the infimal convolution with $h(x)$ to get $\min_{y\in\mathbf R}f_{i-1}(y)+|y|Z+h(x-y)$;
    3.  Finally, translate the function left by $(b_i-a_i)$ units.
    
    Turned into operations on slope segments, these are likewise three steps:
    
    1.  Add $-Z$ to all slope segments to the left of the origin, and add $Z$ to all slope segments to the right of the origin;
    2.  Replace all slope segments smaller than $-Y$ with $-Y$, and all slope segments larger than $X$ with $X$;
    3.  Translate all slope segments left by $(b_i-a_i)$ units.
    
    In the original problem $a_i$ and $b_i$ are very small, so we only need to maintain several length-$1$ slope segments. Although there are infinitely many slope segments, they have an upper bound $X$ and a lower bound $-Y$, and the number of slope segments strictly between the two is not large. Because no insertion operation is involved, we can maintain the slope segments on the two sides of the origin with two stacks, and the interval-add and interval-extremum operations are all done with lazy tags. The above three operations respectively correspond to:
    
    1.  Apply lazy tags to the left and right stacks respectively, adding $-Z$ to the left and $Z$ to the right;
    2.  Each time an element is popped from a stack, take the max with $-Y$ and the min with $X$. If the left stack is empty, pop $-Y$. If the right stack is empty, pop $X$;
    3.  Pop the top $(b_i-a_i)$ elements of the left stack and insert them into the right stack; of course, when $b_i-a_i<0$, do the reverse.
    
    When swapping the stack tops, update the answer: moving left subtracts the current slope, and moving right adds the current slope.
    
    The algorithm complexity is $O(n\max\{a_i,b_i\})$.
    
    ```cpp
    --8<-- "docs/dp/code/opt/slope-trick/landscaping.cpp"
    ```

Template problems:

-   [Luogu P2748 \[USACO16OPEN\] Landscaping P](https://www.luogu.com.cn/problem/P2748)
-   [Kyoto University PC 2016 H - WAAAAAAAAAAAAALL](https://atcoder.jp/contests/kupc2016/tasks/kupc2016_h)
-   [JAG Practice Contest 2017 J - Farm Village](https://atcoder.jp/contests/jag2017autumn/tasks/jag2017autumn_j)

## Exercises

At the end of this article, we provide some problems that have appeared in various competitive-programming contests and can be solved with Slope Trick, for practice.

-   [Luogu P3642 \[APIO2016\] Fireworks Display](https://www.luogu.com.cn/problem/P3642)
-   [Luogu P9962 \[THUPC 2024 Preliminary\] A Tree](https://www.luogu.com.cn/problem/P9962)
-   [Luogu P11317 \[RMI 2021\] Paths](https://www.luogu.com.cn/problem/P11317)
-   [AtCoder Beginner Contest 383 G - Bar Cover](https://atcoder.jp/contests/abc383/tasks/abc383_g)
-   [Codeforces 280 D. k-Maximum Subsequence Sum](https://codeforces.com/problemset/problem/280/D)
-   [Codeforces 280 E. Sequence Transformation](https://codeforces.com/problemset/problem/280/E)
-   [Codeforces 802 O. April Fools' Problem (hard)](https://codeforces.com/contest/802/problem/O)
-   [Codeforces 1209 H. Moving Walkways](https://codeforces.com/contest/1209/problem/H)
-   [Codeforces 1229 F. Mateusz and Escape Room](https://codeforces.com/contest/1229/problem/F)
-   [Codeforces 1534 G. A New Beginning](https://codeforces.com/problemset/problem/1534/G)
-   [Codeforces 1787 H. Codeforces Scoreboard](https://codeforces.com/problemset/problem/1787/H)
-   [2019 Summer Petrozavodsk Camp H. Honorable Mention](https://codeforces.com/gym/102331/problem/H)
-   [2018 ACM-ICPC World Finals C. Conquer The World](https://codeforces.com/gym/102482/problem/C)
-   [300iq Contest 3 F. Farm of Monsters](https://codeforces.com/gym/102538/problem/F)

## References and notes

-   [\[Tutorial\] Slope Trick - zscoder](https://codeforces.com/blog/entry/47821)
-   [Slope trick explained - Kuroni](https://codeforces.com/blog/entry/77298)
-   [Slope Trick - USACO Guide](https://usaco.guide/adv/slope-trick?lang=cpp)
-   [\[Tutorial\] Intuition on Slope Trick - maomao90](https://codeforces.com/blog/entry/103222)

[^convex-def]: Different textbooks may use different names for convex functions.

[^inf-conv]: Also often called the $\min$ convolution, $\inf$ convolution, or $(\min,+)$ convolution.
