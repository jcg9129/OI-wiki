author: Ir1d, YZircon, huhaoo, QAQAutoMaton, Enter-tainer, Marcythm, sshwy, partychicken, Konano, H-J-Granger, baker221, isdanni, ksyx

## Introduction

Linear programming (LP) is a general term for methods that study the extremum problem of a linear objective function under linear constraints; it is a branch of operations research and has applications in many areas. Some special cases of linear programming, such as network flow, multi-commodity flow, and other problems, may appear in competitive programming problems. Competitive programming rarely has problems that can only be solved with linear programming algorithms; the vast majority of such problems can be solved more efficiently through methods such as network-flow modeling.

### A simple example

For a problem to be written in the form of linear programming, it must have both several linear constraints and a linear objective function.

Consider the following example:

???+ example "Example"
    A breakfast chef can make a certain number of steamed buns and fried dough sticks each day; these two breakfasts are much loved by customers. To maximize profit, the chef hopes to make as much breakfast as possible, but in actual operation is limited by various resources such as ingredients and time. To this end, the chef has counted the amount of ingredients, the making time, and the corresponding profit required to make each portion of breakfast, as shown in the following table:
    
    |  Breakfast | Vegetable oil |  Flour |  Time |  Profit |
    | :-: | :-: | :-: | :-: | :-: |
    |  Steamed bun | $4$ | $7$ | $8$ | $5$ |
    |  Fried dough stick | $7$ | $3$ | $6$ | $6$ |
    
    Suppose the chef can purchase at most $66$ units of vegetable oil and $60$ units of flour each day, and can invest at most $96$ units of making time. Then, how should the chef reasonably arrange the production quantities of steamed buns and fried dough sticks to maximize the daily profit?

Described in mathematical language, let $x_1$ and $x_2$ be the quantities of steamed buns and fried dough sticks the chef makes respectively. Then "the total vegetable oil needed does not exceed $66$ units" can be expressed as

$$
4x_1 + 7x_2 \le 66.
$$

Similarly, "the total flour needed does not exceed $60$ units" and "the total time needed does not exceed $96$ units" can be expressed as

$$
\begin{aligned}
7x_1 + 3x_2 &\le 60,\\
8x_1 + 6x_2 &\le 96.
\end{aligned}
$$

In addition, the chef cannot produce a negative number of units of breakfast, so there is also the condition

$$
x_1,x_2\ge 0.
$$

The chef wants to maximize the profit under these constraints:

$$
z = 5x_1 + 6x_2.
$$

This is a typical linear programming problem. Its objective function is a linear function of the decision variables, and the constraints consist of linear equalities or inequalities of the decision variables.

### Graphical method

For a linear programming problem with only two decision variables, one can solve the problem intuitively via the graphical method.

Consider the problem of this section

$$
\begin{aligned}
\max_{x_1,x_2}\;& z = 5x_1 + 6x_2 \\
\text{subject to } & 4x_1 + 7x_2 \le 66,\\
& 7x_1 + 3x_2 \le 60,\\
& 8x_1 + 6x_2 \le 96,\\
& x_1,x_2\ge 0
\end{aligned}
$$

and its corresponding geometric image. The last row of constraints indicates that the selectable points $(x_1,x_2)$ all appear in the first quadrant, and the other three constraints indicate that the selectable points must be below the line $4x_1 + 7x_2 = 66$, the line $7x_1 + 3x_2 = 60$, and the line $8x_1 + 6x_2 = 96$. The intersection of these regions (as shown by the green region in the figure below) is the set of all selectable points:

![](images/linear-programming.svg)

Next we want to maximize the value of $z=5x_1+6x_2$. If we regard this equality as the equation of the line $5x_1+6x_2=z$, then as $z$ varies, we obtain a family of parallel lines, and the larger $z$ is, the closer the line is to the upper right. Therefore, we only need to continually move the line until reaching some critical position, such that moving a little more to the upper right, the line no longer intersects the region shown in the figure; the $z$ corresponding to the line at this point is the required maximum value.

As shown in the figure, this situation occurs at the position shown by the red point. It is the intersection of the line $4x_1 + 7x_2 = 66$ and the line $7x_1 + 3x_2 = 60$. Solving the two line equations simultaneously, its coordinates are $(6,6)$. This is the unique optimal solution of this problem. The breakfast chef's maximum profit is $z=66$.

When the problem involves more than two decision variables, the graphical method no longer applies. But some observations from the example of this section are still valid. Each inequality constraint in a linear programming problem describes a "half-plane", and the set of all feasible solutions is the intersection of these "half-planes", so it is always a "convex polygon". The optimal solution of the programming problem can always be attained at some "vertex" of this "convex polygon". The coordinates of these "vertices" can be found by solving the equations of the "boundaries" of these "half-planes" simultaneously. Extending these observations to high-dimensional space develops an efficient method for solving linear programming problems—the simplex method. This is also the most commonly applied method in competitive programming.

Another point worth noting is that, in principle, the steamed buns and fried dough sticks made by the breakfast chef are not infinitely divisible and should be some integer. Although this was not explicitly restricted in the solution process of this problem, since the final optimal solution is indeed an integer, even adding the integer restriction, the answer to this problem is still feasible. But for many programming problems, the optimal solution may not be attained at an integer point; these problems are in fact a class of integer programming problems, not simple linear programming problems. The end of this article briefly discusses this class of problems.

## Basic concepts

This section introduces the basic concepts of linear programming problems.

### Linear programming problem

A linear programming problem $P$ usually consists of the following two parts:

-   A linear objective function, i.e. a function of the form

    $$
    f(x_1,x_2,\cdots,x_n)=c_1x_1+c_2x_2+\cdots+c_nx_n
    $$

    where $c_i\in\mathbf R$ are constants;

-   Linear constraints, i.e. inequality or equality constraints of the form

    $$
    g_j(x_1,x_2,\cdots,x_n)=a_{j1}x_1+a_{j2}x_2+\cdots+a_{jn}x_n \le (=,\ge) b_j
    $$

    where $a_{ji},b_j\in\mathbf R$ are all constants.

A linear programming problem is to maximize or minimize the objective function under the premise of satisfying the given constraints. A solution $(x_1,x_2,\cdots,x_n)\in\mathbf R^n$ satisfying the given constraints is called a **feasible solution**; among all feasible solutions, the one that makes the objective function attain its extremum is called an **optimal solution**.

### Standard form

For convenience of description and further processing, one usually needs to specify a standard form of a linear programming problem. Different references may have different ways of stipulation; this article stipulates the standard form of linear programming as follows:

$$
\begin{aligned}
\min_{\{x_i\}}\;& \sum_{i=1}^n c_ix_i \\
\text{subject to }& \sum_{i=1}^n a_{ji}x_i = b_i \ge 0,~j=1,\cdots,m,\\
& x_i \ge 0,~i = 1,\cdots,n.
\end{aligned}
$$

That is, a linear programming problem is a minimization problem, all decision variables have non-negativity constraints, and apart from that it contains only several equality constraints whose right-hand constants are non-negative. Using [matrices](./linear-algebra/matrix.md), one can express this problem more concisely:

$$
\max\{c^Tx : Ax = b \ge 0,~ x\ge 0\}.
$$

where $x=(x_i)\in\mathbf R^n$ are the decision variables, and $b=(b_j)\in\mathbf R^m$ and $A=(a_{ji})\in\mathbf R^{m\times n}$ are the constants involved in the constraints. The size of a linear programming problem refers to its number of decision variables and its number of constraints.

???+ tip "Vector inequalities"
    Vector inequalities like $b \ge 0$ appear many times in this article. In general, for vectors $x,y\in\mathbf R^n$, the inequality $x\le y$ means $\forall i(x_i\le y_i)$, i.e. comparison in the real-number sense dimension by dimension. This relationship is a [partial order](./order-theory.md#二元关系) on the vector space, that is, there are cases where two vectors cannot be compared.

The choice of the standard form is only for convenience of writing and has nothing special, because any linear programming problem can be equivalently written in the following six forms:

$$
\begin{aligned}
&\min\{c^Tx : Ax = b,~ x\ge 0\},\\
&\min\{c^Tx : Ax \ge b\},\\
&\min\{c^Tx : Ax \ge b,~ x\ge 0\},\\
&\max\{c^Tx : Ax = b,~ x\ge 0\}, \\
&\max\{c^Tx : Ax \le b\},\\
&\max\{c^Tx : Ax \le b,~ x\ge 0\}.\\
\end{aligned}
$$

The following operations can equivalently transform any linear programming problem into one of these six forms:

1.  By adding a negative sign, i.e. changing $c$ to $-c$, one can convert between a maximization problem and a minimization problem.
2.  By adding a negative sign, i.e. replacing $a_j^Tx \lesseqqgtr b_j$ with $-a_j^Tx \gtreqqless -b_j$, one can convert between the two directions of an inequality constraint, or make the right-hand constant of an equality constraint non-negative.
3.  Every equality constraint $a_j^Tx = b_j$ can be replaced with two inequality constraints in opposite directions $a_j^Tx \ge b_j$ and $a_j^Tx \le b_j$.
4.  Every inequality constraint $a_j^Tx \le(\ge) b_j$ can be converted, by adding a non-negative slack variable $s_j$, into an equality constraint $a_j^Tx +(-) s_j = b_j$ and the corresponding non-negativity constraint $s_j\ge 0$.
5.  If some decision variable $x_i$ has no non-negativity constraint, then it can be replaced by the difference of two non-negative variables, i.e. $x_j = x^+_j - x^-_j$ with $x^+_j,x^-_j \ge 0$.

The size of the linear programming problem obtained through these transformations does not exceed twice the size of the original problem, and the feasible solutions and optimal solutions of these problems can easily be converted between each other. Therefore, for a general-form linear programming problem, one can always first transform it into the standard form (or one of the above six forms) before solving.

??? example "Example"
    Consider the linear programming problem
    
    $$
    \begin{aligned}
    \max\;& 3x_1 - 2x_2 + x_3 \\
    \text{subject to }& 2x_1 + 3x_2 + 4x_3 \ge 1,\\
    & 3x_1 + 4x_2 \le 5,\\
    & 5x_2 - x_3 = -1, \\
    & x_1, x_2 \ge 0.
    \end{aligned}
    $$
    
    Through operations 1, 2, and 3 one can transform it into the form $\min\{c^Tx : Ax \ge b\}$, i.e.
    
    $$
    \begin{aligned}
    \min\;& -3x_1 + 2x_2 - x_3 \\
    \text{subject to }& 2x_1 + 3x_2 + 4x_3 \ge 1,\\
    & -3x_1 - 4x_2 \ge -5,\\
    & 5x_2 - x_3 \ge -1, \\
    & -5x_2 + x_3 \ge 1, \\
    & x_1 \ge 0,\\
    & x_2 \ge 0.
    \end{aligned}
    $$
    
    Through operations 4 and 5 one can transform it into the form $\max\{c^Tx : Ax = b,~ x\ge 0\}$, i.e.
    
    $$
    \begin{aligned}
    \max\;& 3x_1 - 2x_2 + x^+_3 - x^-_3 \\
    \text{subject to }& 2x_1 + 3x_2 + 4x^+_3 - 4x^-_3 - x_4 = 1,\\
    & 3x_1 + 4x_2 + x_5 = 5,\\
    & 5x_2 - x^+_3 + x^-_3 = -1, \\
    & x_1, x_2, x^+_3, x^-_3, x_4, x_5 \ge 0.
    \end{aligned}
    $$

### Feasible region and the solution of the problem

The set of all feasible solutions $\mathcal D\subseteq\mathbf R^n$ is called the **feasible region** of the linear programming problem $P$. From a geometric point of view, each inequality constraint $a_j^T x \le b_j$ describes a half-space $\{x\in\mathbf R^n:a_j^T x \le b_j\}$, and each equality constraint $a^T_jx = b_j$ describes a hyperplane $\{x\in\mathbf R^n:a_j^Tx=b_j\}$, so the feasible region must be the intersection of finitely many half-spaces and hyperplanes. In the field of optimization[^poly-names], such a geometric body is usually called a **polyhedron** in $\mathbf R^n$. A polyhedron must be a closed convex set, but is not necessarily bounded. A bounded polyhedron is also called a **polytope**. A polytope can be regarded as the generalization of a polygon in the plane to high-dimensional space, and a polyhedron further generalizes it to the possibly unbounded case.

???+ example "Examples of polyhedra"
    Here we list some common polyhedra:
    
    1.  The empty set $\varnothing$, also called the **nullitope**, whose dimension is stipulated to be $-1$.
    2.  An **affine subspace**, i.e. the intersection of several hyperplanes $\{x\in\mathbf R^n:Ax = b\}$. It is equivalent to the solution set of the system of linear equations $Ax = b$: when the system has no solution, it is the empty set; otherwise, it can always be written in the form $x_0+V$, where $x_0\in\mathbf R^n$ and $V\subseteq\mathbf R^n$ is an $n-\operatorname{rank}(A)$-dimensional linear subspace. In particular, a hyperplane is also an affine subspace.
    3.  A **polyhedral cone**, i.e. all non-negative linear combinations $\{\sum_i\alpha_ix_i:\alpha_i\ge 0\}$ of finitely many points $\{x_i\}$ in space. It is a convex cone with vertex at the origin. Equivalently, it can be regarded as a polyhedron enclosed by several hyperplanes passing through the origin, i.e. $\{x\in\mathbf R^n : Ax\le 0\}$. In particular, a half-space is also a polyhedral cone.
    4.  A polytope, i.e. a bounded polyhedron. In particular, the $-1$-, $0$-, $1$-, $2$-, $3$-dimensional polytopes are the common empty set, point, segment, polygon, and (usual) polyhedron. A set is a polytope if and only if it is the convex hull $\{\sum_i\alpha_ix_i:\alpha_i\ge 0,~\sum_i\alpha_i=1\}$ of finitely many points $\{x_i\}$. A $k$-dimensional polytope is at least the convex hull generated by $k+1$ points.
    5.  A **simplex**, i.e. a $k$-dimensional polytope generated by exactly $k+1$ points. It is the simplest $k$-dimensional polytope. In particular, the $-1$-, $0$-, $1$-, $2$-, $3$-dimensional polytopes are respectively the empty set, point, segment, triangle, and tetrahedron. The simplest example of a $k$-dimensional simplex is $\{x\in\mathbf R^k:x_i\ge 0,~\sum_ix_i=1\}$. In fact, any $k$-dimensional simplex can be turned into such a special case via an affine transformation (i.e. translation and scaling). It is worth noting that the simplex method is not really performed on a simplex.
    
    Any polyhedron can be regarded as the [Minkowski sum](../geometry/convex-hull.md#闵可夫斯基和) of a polyhedral cone and a polytope: the former describes the unbounded part of the polyhedron, and the latter describes the shape of the bounded part of the polyhedron. This polyhedral cone is unique: the polyhedral cone obtained from the decomposition of the polyhedron $\{x\in\mathbf R^n:Ax\le b\}$ must be $\{x\in\mathcal R^n:Ax\le 0\}$.

The solution of a linear program is closely related to the structure of the polyhedron. For a polyhedron $\mathcal D\in\mathbf R^n$ and a vector $c\in\mathbf R^n\setminus\{0\}$, consider the following linear programming problem $P$: (the minimization case can be discussed similarly)

$$
\max\{c^Tx:x\in\mathcal D\}.
$$

From a geometric point of view, this amounts to, under the premise that the hyperplane $H:c^Tx = z$ has at least one intersection point with the feasible region $\mathcal{D}$, moving the hyperplane $H$ along the direction of the vector $c$ to make $z$ as large as possible. There are then three possibilities:

-   The feasible region $\mathcal D$ is the empty set. This indicates that the problem $P$ has no feasible solution, and some of its constraints are mutually contradictory. In this case, the problem $P$ is called **infeasible**, and its optimal value is stipulated to be $-\infty$.

-   The feasible region $\mathcal D$ is non-empty, but it contains a ray with direction vector $c$, i.e. there exists $x_0\in\mathbf R^n$ such that $x_0+tc\in\mathcal D$ holds for all $t\ge 0$. Because one can continually move the hyperplane $H$ along the direction of the vector $c$, and during the movement the set $H\cap\mathcal D$ contains at least some point of this ray and is definitely non-empty, the objective function $c^Tx = c^Tx_0 + tc^Tc$ can attain arbitrarily large values. In this case, the problem $P$ is called **unbounded**, and its optimal value is stipulated to be $+\infty$.

-   The feasible region $\mathcal D$ is non-empty and contains no ray with direction vector $c$. In this case, the problem $P$ is called **bounded**. Let $z^*\in\mathbf R$ be the optimal value of the problem $P$. The hyperplane $H^*:c^Tx = z^*$ is in a critical position: it intersects the polyhedron $\mathcal D$, and $\mathcal D$ is contained in the half-space $\{x:c^Tx\le z^*\}$. Such a hyperplane is called a **supporting hyperplane** of the polyhedron $\mathcal D$. The optimal solution set of the problem $P$ is $H^*\cap\mathcal D$. As the intersection of a supporting hyperplane and a polyhedron, the set $H^*\cap\mathcal D$ must be a polyhedron and is contained in the boundary of $\mathcal D$. It is called a **face** of the polyhedron $\mathcal D$. Vividly speaking, a polyhedron is enclosed by these faces. Besides these faces formed by the intersection of supporting hyperplanes and the polyhedron, in general, a polyhedron also has two faces: the empty set and the polyhedron itself. All faces of a polyhedron, under the set containment relation, form the structure of a [lattice](../math/order-theory.md#有向集与格).

    The dimension of a face of a $d$-dimensional polyhedron must be an integer between $0$ and $d$. A face of dimension $0$ (i.e. a point) is called a **vertex** or **corner point** of the polyhedron $\mathcal D$, a face of dimension $1$ is called an **edge** of the polyhedron $\mathcal D$, and a face of dimension $d-1$ is called a **facet** of the polyhedron $\mathcal D$. But not all polyhedra have vertices. Because a face of a face of a polyhedron is still a face of the polyhedron, and only an affine subspace has no strictly smaller non-empty face, all minimal faces of a polyhedron $\mathcal D$ are affine subspaces. Moreover, the minimal faces of the same polyhedron have the same dimension; in particular, the dimension of the minimal faces of the polyhedron $\mathcal D=\{x\in\mathbf R^n:Ax\le b\}$ is $n-\operatorname{rank}A$.

    Because a face of a polyhedron is the solution set of a bounded linear programming problem, one needs to figure out how to determine the equations of the faces of a polyhedron. Let the polyhedron $\mathcal D$ be described by several constraints $a_j^Tx \lesseqqgtr b_j$, and let $F$ be a face of $\mathcal D$. If some constraint attains equality at all $x\in F$, then this constraint is said to be **tight** on the face $F$. The points on the face $F$ obviously satisfy the system of equations obtained by taking these tight constraints as equalities, and the intersection of the affine subspace determined by this system of equations with the polyhedron $\mathcal D$ is the face $F$. Conversely, arbitrarily choosing a subset of the constraints of the polyhedron $\mathcal D$, the intersection of the affine subspace obtained by taking these constraints as equalities and solving them simultaneously with the polyhedron is a face of $\mathcal D$. Moreover, the more tight constraints chosen, the smaller (in the sense of containment) the resulting face.

    In particular, the coefficient matrix $\begin{pmatrix}A\\ I\end{pmatrix}$ of the feasible region $\mathcal D=\{x\in\mathbf R^n:Ax=b,~x\ge 0\}$ of the standard-form linear program has rank $n$, so its minimal faces are its vertices. That is, if the problem is bounded, then its optimal solution can always be chosen as some vertex. Moreover, this vertex can be obtained by choosing $n$ linearly independent tight constraints simultaneously. This is precisely the convenience of the standard form of linear programming.

???+ example "Example"
    In the figure below, $\mathcal D$ is the feasible region. When the coefficients in the objective function are $c_1,c_2,c_3$, they correspond respectively to the three cases of a unique optimal solution, multiple optimal solutions, and unboundedness. For the first two cases, the corresponding red thick solid line is (one of) the supporting hyperplanes corresponding to the solution set, and the optimal solution sets are the vertex $B$ and the edge $\overline{CD}$ of the polyhedron $\mathcal D$ respectively. For the third case, because the feasible region $\mathcal D$ contains a ray with direction $c_3$, the hyperplane with $c_3$ as its normal vector can continually move along the $c_3$ direction, and thus the problem is unbounded.
    
    ![](./images/lp-feasible.svg)

These discussions ignored the case $c=0$. In this case, the linear programming problem obviously cannot be unbounded, so either the problem itself is infeasible, or the optimal value equals $0$ and the optimal solution set is $\mathcal D$ itself. This special class of linear programs is also called a **feasibility linear program**.

It is worth pointing out that the problems of determining whether a linear programming problem is feasible, whether it is bounded, and finding a feasible solution of a system of inequalities are all just as difficult as solving the linear programming problem itself[^reducible]. For example, the proof of the strong duality theorem below shows that solving a bounded linear programming problem is equivalent to finding a feasible solution of a set of inequalities. Therefore, for tasks such as determining whether a system of inequalities has a solution and determining whether a system of equations has a non-negative solution, the most effective way is to solve the corresponding feasibility linear program[^other-methods].

In addition, if a constraint of a linear programming problem is not tight on any face of the feasible region, then this constraint is **redundant**. In the example of the breakfast chef at the beginning of this article, the working-time constraint is a redundant constraint. The problem of determining whether some inequality $a_j^Tx\le b_j$ in a given system of inequalities is redundant can be solved by solving the linear programming problem $\max\{a_j^Tx:x\in\mathcal D\}$ and comparing it with $b_j$.

## Common algorithms

In competitive programming, few problems can be solved only through linear programming algorithms. Most problems that can be solved with the linear programming method can usually also be solved through more specialized and more efficient algorithms such as network flow.

Common algorithms for solving linear programming problems are as follows:

-   [Simplex method](./simplex.md)
-   Ellipsoid method
-   Interior-point method

Although the worst-case complexity of the simplex method is exponential, while the complexity of the interior-point method is polynomial, both classes of algorithms perform very well in most practical problems. In contrast, although the theoretical complexity of the ellipsoid method is polynomial, it usually runs slowly and is not practical.

It is currently unknown whether there exists a strongly-polynomial-complexity algorithm for linear programming problems.

## Dual problem

Every linear programming problem corresponds to a dual problem. The solutions of the original problem and the dual problem are closely related. Through the dual problem, one not only gains a deeper understanding of the structure of the problem, but can often also improve the solving efficiency of the original problem.

For a linear programming problem $P$ (all lowercase-letter variables involved are vectors)

$$
\begin{aligned}
\min_{x_1,x_2,x_3}\;& c_1^Tx_1 + c_2^Tx_2 + c_3^Tx_3 \\
\text{subject to }& A_{11}x_1 + A_{12}x_2 + A_{13}x_3 \ge b_1,\\
& A_{21}x_1 + A_{22}x_2 + A_{23}x_3 = b_2,\\
& A_{31}x_1 + A_{32}x_2 + A_{33}x_3 \le b_3,\\
& x_1\ge 0,~ x_3\le 0,
\end{aligned}
$$

its dual problem $D$ is the linear programming problem

$$
\begin{aligned}
\max_{y_1,y_2,y_3}\;&b_1^Ty_1+b_2^Ty_2+b_3^Ty_3 \\
\text{subject to }&A_{11}^Ty_1 + A_{21}^Ty_2 + A_{31}^Ty_3\le c_1,\\
&A_{12}^Ty_1 + A_{22}^Ty_2 + A_{32}^Ty_3 = c_2,\\
&A_{13}^Ty_1 + A_{23}^Ty_2 + A_{33}^Ty_3 \ge c_3,\\
&y_1\ge 0,~ y_3\le 0.
\end{aligned}
$$

where the decision variables $y_1,y_2,y_3$ of the dual problem are the Lagrange multipliers of the three classes of constraints of the original problem respectively; conversely, the decision variables $x_1,x_2,x_3$ of the original problem are also the Lagrange multipliers of the three classes of constraints of the dual problem respectively. It is easy to verify that the dual problem of the dual problem is the original problem.

The correspondence between the original problem $P$ and the dual problem $D$ is as follows:

|  Minimization problem |  Maximization problem |
| :----: | :----: |
| Greater-than-or-equal constraint |  Non-negative variable  |
| Less-than-or-equal constraint |  Non-positive variable  |
|  Equality constraint  |  Unrestricted variable |
|  Non-negative variable  | Less-than-or-equal constraint |
|  Non-positive variable  | Greater-than-or-equal constraint |
|  Unrestricted variable | Equality constraint  |
| Objective function coefficient | Constraint right-hand constant |
| Constraint right-hand constant | Objective function coefficient |

In particular, the dual problem of the standard-form linear programming problem

$$
\min\{c^Tx:Ax=b,~x\ge 0\}
$$

is

$$
\max\{b^Ty:A^Ty\le c\}.
$$

### Duality principle

The original problem and the dual problem are not only mirror images of each other in form, but their solutions are also closely related. This is called the **duality principle** (duality principal). For convenience of exposition, in this section, when stating and proving theorems, we adopt the standard-form original problem.

First, the **weak duality theorem** states that the maximum value of the dual problem does not exceed the minimum value of the original problem.

???+ note "Weak duality theorem"
    For all $A\in\mathbf R^{m\times n}$, $b\in\mathbf R^m$, and $c\in\mathbf R^n$, we always have
    
    $$
    \max\{b^Ty:A^Ty\le c\} \le \min\{c^Tx:Ax=b,~x\ge 0\}.
    $$

??? note "Proof"
    If either the original problem or the dual problem is infeasible, then this inequality is trivial. Assume both problems are feasible. Then, for all feasible $x$ and $y$,
    
    $$
    b^Ty = x^TA^Ty \le x^Tc.
    $$
    
    Therefore, taking the extrema of both sides, the weak duality theorem holds.

Based on the weak duality theorem, the situation of the solutions of the original problem and the dual problem can only be one of the following four cases:

1.  Both the original problem and the dual problem are infeasible, i.e. $-\infty\le+\infty$;
2.  The original problem is infeasible and the dual problem is unbounded, i.e. $+\infty\le+\infty$;
3.  The original problem is unbounded and the dual problem is infeasible, i.e. $-\infty\le-\infty$;
4.  Both the original problem and the dual problem are bounded.

The weak duality theorem has many corollaries. For example, it actually gives a method for determining the unboundedness of the original problem using the feasibility of the original problem and the dual problem.

???+ note "Corollary"
    A linear programming problem is unbounded if and only if it is feasible and its dual problem is infeasible.

Applying the weak duality theorem to a feasibility linear programming problem gives Farkas's lemma (and its various variants).

???+ note "Farkas's lemma"
    For $A\in\mathbf R^{m\times n}$ and $b\in\mathbf R^n$, exactly one of the following cases holds:
    
    1.  There exists $x\in\mathbf R^n$ such that $Ax=b$ and $x\ge 0$;
    2.  There exists $y\in\mathbf R^m$ such that $A^T y\ge 0$ and $b^Ty<0$.

??? note "Proof"
    Consider the linear programming problem $\max\{0:Ax=b,~x\ge 0\}$; its dual problem is $\min\{b^Ty:A^Ty\ge 0\}$. The dual problem is obviously feasible, because at least $0\in\mathbf R^m$ is a feasible solution. Therefore, by the weak duality theorem, either the original problem is feasible or the dual problem is unbounded, one of the two. The original problem being feasible is case 1 of Farkas's lemma, and the dual problem being unbounded is equivalent to case 2 of Farkas's lemma. This proves Farkas's lemma.

Farkas's is in fact a kind of [hyperplane separation theorem](https://en.wikipedia.org/wiki/Hyperplane_separation_theorem). Case 1 says that the point $b$ lies in the polyhedral cone $C$ generated by the column vectors of $A$; therefore, Farkas's lemma states that, if and only if the point $b$ is not in this convex cone $C$, there exists a hyperplane $H:y^Tx = 0$ passing through the origin with normal vector $y$ that strongly separates the point $b$ and the polyhedral cone $C$.

In fact, for the fourth case allowed by the weak duality theorem, a stronger conclusion holds: the optimal values of the original problem and the dual problem are equal. Combining the latter three cases gives the **strong duality theorem**: as long as one of the original problem or the dual problem is feasible, their optimal values must be equal.

???+ note "Strong duality theorem"
    For all $A\in\mathbf R^{m\times n}$, $b\in\mathbf R^m$, and $c\in\mathbf R^n$,
    
    $$
    \max\{b^Ty:A^Ty\le c\} = \min\{c^Tx:Ax=b,~x\ge 0\}.
    $$
    
    as long as one of the two sets is non-empty.

??? note "Proof"
    The only case not covered by the weak duality theorem is the case where both the original problem and the dual problem are feasible. In this case, consider the following feasibility linear programming problem $Q$:
    
    $$
    \max\{0:c^Tx \le b^Ty,~Ax=b,~x\ge 0,~A^Ty\le c\}.
    $$
    
    If the problem $Q$ has a feasible solution $(x^*,y^*)\in\mathbf R^n\times\mathbf R^m$, then, by the weak duality theorem and optimality,
    
    $$
    b^Ty^* \le \max\{b^Ty:A^Ty\le c\} \le \min\{c^Tx:Ax=b,~x\ge 0\} \le c^Tx^*,
    $$
    
    but $c^Tx^*\le b^Ty^*$, so all these inequalities can attain equality, that is, not only does strong duality hold, but $x^*$ and $y^*$ are the optimal solutions of the original problem and the dual problem respectively.
    
    Therefore, it suffices to prove that the problem $Q$ is feasible. Suppose not. Following the proof of Farkas's lemma, one can consider the dual problem $DQ$ of the problem $Q$:
    
    $$
    \min\{c^T\mu - b^T\lambda : ct - A^T\lambda \ge 0,~ -bt + A\mu = 0,~t\ge 0,~\mu\ge 0\}.
    $$
    
    Because $(t,\lambda,\mu)=(0,0,0)$ is a feasible solution of the dual problem $DQ$, by the weak duality theorem, the problem $Q$ being infeasible means the dual problem $DQ$ is unbounded, i.e. there exists a $(t^*,\lambda^*,\mu^*)$ such that
    
    $$
    c^T\mu^* - b^T\lambda^* <0,~ ct^* - A^T\lambda^* \ge 0,~ -bt^* + A\mu^* = 0,~t^*\ge 0,~\mu^*\ge 0.
    $$
    
    In this case, if $t^*>0$, then these inequalities actually show that $(x,y)=(\mu^*/t^*,\lambda^*/t^*)$ is a feasible solution of the aforementioned problem, contradicting the assumption. So there can only be $t^*=0$. This shows
    
    $$
    c^T\mu^* < b^T\lambda^*,~ A^T\lambda^*\le 0,~ A\mu^*=0,~\mu^*\ge 0.
    $$
    
    But because we have already assumed that both the original problem and the dual problem in the theorem are feasible, that is, there exists $(x_0,y_0)$ such that
    
    $$
    Ax_0 = b,~ x_0\ge 0,~ A^Ty_0\le c
    $$
    
    holds, we have
    
    $$
    0 = (A\mu^*)^Ty_0 = (A^Ty_0)^T\mu^* \le c^T\mu^* < b^T\lambda^* = x_0^TA^T\lambda^* \le 0.
    $$
    
    This is obviously a contradiction. This contradiction shows that the problem $Q$ is feasible, and thus shows that strong duality holds.

From the proof process of the strong duality theorem one can also obtain the following corollary:

???+ note "Corollary"
    Let a pair of feasible solutions $x^*$ and $y^*$ of the original problem and the dual problem satisfy strong duality, i.e. $c^Tx^* = b^Ty^*$. Then they are also the optimal solutions of the original problem and the dual problem respectively.

The strong duality theorem shows that for a feasible linear programming problem, one only needs to solve its dual problem to obtain the optimal value of the original problem.

### Complementary slackness conditions

Like other optimization problems, the complementary slackness conditions are part of the optimality conditions of a linear programming problem. Moreover, because the objective function is linear, for a linear programming problem, the complementary slackness conditions are the necessary and sufficient condition for a feasible solution to be an optimal solution.

The so-called **complementary slackness** condition means that only when a constraint in the original problem (dual problem) attains equality (i.e. the constraint is tight) can the variable corresponding to it in the dual problem (original problem) take a nonzero value. If we also regard a variable taking a nonzero value as a slack constraint, then this is equivalent to saying that the corresponding variable and constraint in the original problem and the dual problem cannot be slack at the same time. Therefore, this condition is called the complementary slackness condition.

Taking the standard-form linear programming problem as an example, the following conclusion holds:

???+ note "Theorem"
    Suppose $x^*$ and $y^*$ are feasible solutions of the original problem $\min\{c^Tx:Ax=b,~x\ge 0\}$ and the dual problem $\max\{b^Ty:A^Ty\le c\}$ respectively. Then $x^*$ and $y^*$ are also the optimal solutions of the original problem and the dual problem respectively if and only if the complementary slackness condition holds, i.e.
    
    $$
    x^T(A^Ty-c) = 0.
    $$

??? note "Proof"
    Because $x^*$ and $y^*$ are both feasible solutions,
    
    $$
    b^Ty^* - c^Tx^* = (x^*)^T(A^T y^* - c).
    $$
    
    Therefore, the complementary slackness condition holds if and only if $b^Ty^* = c^Tx^*$. By the corollary of the strong duality theorem, this condition holds if and only if $x^*$ and $y^*$ are the optimal solutions of the original problem respectively.

The standard form may be too special. A slightly more general form of this theorem is as follows:

???+ note "Theorem"
    Suppose $x^*$ and $y^*$ are feasible solutions of the original problem $\min\{c^Tx:Ax\ge b,~x\ge 0\}$ and the dual problem $\max\{b^Ty:A^Ty\le c,~y\ge 0\}$ respectively. Then $x^*$ and $y^*$ are also the optimal solutions of the original problem and the dual problem respectively if and only if the complementary slackness condition holds, i.e.
    
    $$
    x^T(A^Ty-c) = y^T(Ax-b) = 0.
    $$

??? note "Proof"
    The proof is basically the same as above, only this time one writes the difference as
    
    $$
    b^Ty^* - c^Tx^* = (x^*)^T(A^T y^* - c) - (y^*)^T(Ax^*-b).
    $$

The complementary slackness conditions provide a simple condition for determining the optimality of a feasible solution of a linear programming problem.

### Primal-dual method

The dual problem can assist in solving the original problem. When solving a linear programming problem, one method often used is the **primal-dual method**. It, by solving a series of relatively simple auxiliary problems, gradually improves the solution of the dual problem, and thus obtains the optimal solution of the primal problem.

For the standard-form original problem

$$
(P)\qquad\min\{c^Tx : Ax=b\ge 0,~ x\ge 0\}
$$

and its dual problem

$$
(D)\qquad\max\{b^Ty : A^Ty\le c\},
$$

the previous section has already explained that to find their optimal solutions, one only needs to find a pair of feasible solutions of problems $(P)$ and $(D)$ such that they satisfy the complementary slackness condition $x^T(A^Ty-c)=0$. So consider the following procedure:

1.  Starting from a feasible solution $y$ of the dual problem $(D)$, compute the set of tight constraints of the dual problem

    $$
    I = \{i : (A^Ty - c)_i = 0\}.
    $$

2.  By the complementary slackness condition, if there exists a feasible solution $x$ of problem $(P)$ such that $x_i>0$ holds only for $i\in I$, it means an optimal solution has already been found. Therefore, consider the linear programming problem

    $$
    (RP)\qquad
    \begin{aligned}
    \min_{x,s}\;& \mathbf 1^Ts \\
    \text{subject to } & Ax + s = b, \\
    & x_i \ge 0,~\forall i \in I,\\
    & x_i = 0,~\forall i \notin I,\\
    & s \ge 0.
    \end{aligned}
    $$

3.  If the minimum value of problem $(RP)$ is $0$, then the $x^*$ in the optimal solution $(x^*,0)$ is the optimal solution of the original problem $(P)$. Otherwise, one can find the solution $\bar y$ of its dual problem $(DRP)$:

    $$
    (DRP)\qquad
    \begin{aligned}
    \max_{y}\;& b^Ty \\
    \text{subject to }& \sum_{j}a_{ji}y_j \le 0,~\forall i\in I,\\
    & y \le 1.
    \end{aligned}
    $$

    By the strong duality theorem, $b^T\bar y = 1^Ts^*>0$.

4.  Improve the feasible solution of the dual problem $(D)$ according to the solution of problem $(DRP)$. Let $y' = y + \varepsilon \bar y$, where $\varepsilon>0$; then $b^Ty' = b^Ty + \varepsilon b^T\bar y > b^Ty$ must hold. Therefore, as long as one ensures that $y'$ is still a feasible solution of the dual problem $(D)$, one should choose the value of $\varepsilon$ as large as possible.

    For $i\in I$,

    $$
    \sum_ja_{ji}y'_j = \sum_ja_{ji}y_j + \varepsilon \sum_ja_{ji}\bar y_j \le c_i,
    $$

    so these constraints of problem $(D)$ can always be satisfied.

    For the remaining constraints, i.e. when $i\notin I$, one only needs to take

    $$
    \varepsilon = \min\left\{\dfrac{c_i - \sum_{j}a_{ji}y_j}{\sum_{j}a_{ji}\bar y_j}:i\notin I,~\textstyle\sum_{j}a_{ji}\bar y_j>0\right\}
    $$

    to improve the solution of the dual problem as much as possible while ensuring feasibility, and then return to step 1 to continue iterating. In particular, if the set in the above expression is the empty set, i.e. $\varepsilon=+\infty$, then the dual problem $(D)$ is unbounded and the original problem $(P)$ is infeasible.

In this process only problem $(DRP)$ actually needs to be solved; it is related to problem $(RP)$ through the strong duality theorem. Problem $(DRP)$ provides a direction for improving the solution of the dual problem, and compared with the dual problem $(D)$ itself, the form of problem $(DRP)$ is simpler. The feasibility of problem $(DRP)$ is guaranteed by Farkas's lemma, and the constraint $y\le 1$ is just a normalization condition ensuring that problem $(DRP)$ is bounded.

In competitive programming, the primal-dual method is widely applied to various combinatorial optimization problems. For example, the [Hungarian algorithm](../graph/graph-matching/bigraph-weight-match.md#hungarian-algorithmkuhnmunkres-algorithm) for maximum-weight bipartite matching, the [cycle-canceling algorithm](../graph/flow/min-cost.md) and the [SSP algorithm (primal-dual algorithm)](../graph/flow/min-cost.md#ssp-算法) for minimum-cost flow, the [Dijkstra algorithm](../graph/shortest-path.md#dijkstra-算法) for shortest paths, and the [Ford–Fulkerson augmenting algorithm](../graph/flow/max-flow.md#fordfulkerson-增广) for maximum flow can all be regarded as direct applications of the primal-dual method.

## Integer programming

**Integer programming** usually refers to **integer linear programming** (ILP). The standard form of integer linear programming is as follows:

$$
\begin{aligned}
\min_{x}\; & c^Tx \\
\text{subject to } & Ax = b \ge 0,\\
& x \ge 0,\\
& x \in \mathbf Z^n,
\end{aligned}
$$

where $A\in\mathbf R^{m\times n}$, $b\in\mathbf R^m$, $c\in\mathbf R^n$. That is, integer linear programming is the problem obtained by adding to the linear programming problem the constraint that the decision variables must be integers.

The integer constraint significantly increases the complexity of integer programming problems. Many combinatorial optimization problems, such as the knapsack problem, the satisfiability problem, and numerous optimization problems in graph theory, can be represented as integer programming models, and most of these problems have been proved to be NP-hard.

### Totally unimodular matrices

Precisely for this reason, for many large-scale integer optimization problems, one sometimes considers relaxing its integer constraint and instead solving a linear programming problem. Generally speaking, the optimal value of the relaxed linear programming problem is only a lower-bound estimate of the original integer programming problem (assuming the problem is a minimization problem). But if the optimal solution of the relaxed linear programming problem happens to be an integer solution, then it must also be the optimal solution of the original integer programming problem.

A natural question is whether there exists a condition that can guarantee that the optimal solution of a linear programming problem is an integer solution. The concept of a totally unimodular matrix provides such a condition.

???+ abstract "Totally unimodular matrix"
    If the determinants of all square submatrices of a matrix $A\in\mathbf R^{m\times n}$ are $0$ or $\pm 1$, then the matrix $A$ is called a **totally unimodular matrix**.

In particular, all elements of a totally unimodular matrix are $0$ or $\pm 1$. Using the concept of a totally unimodular matrix, one can state the following conclusion:

???+ note "Theorem"
    For a totally unimodular matrix $A\in\mathbf Z^{m\times n}$, $b\in\mathbf Z^{m}$, and $c\in\mathbf Z^n$, the linear programming problem and its dual problem
    
    $$
    \min\{c^Tx : Ax=b,x\ge 0\} = \max\{b^Ty: A^Ty\le c\}
    $$
    
    both have integer optimal solutions, as long as they are both bounded.

??? note "Proof"
    It has been explained earlier that the optimal solution set of a linear programming problem can be taken as one of its minimal faces, and the latter is the solution of the system of equations obtained by taking several linearly independent tight constraints as equalities and solving them simultaneously:
    
    $$
    \{x\in\mathbf R^n : a_j^Tx = b_j,~\forall j\in J\}.
    $$
    
    Denote this system of equations as $A_Jx=b_J$, with $A_J=(A_1,A_2)$, where $A_1$ is a full-rank square matrix with determinant $\pm 1$. Then, by Cramer's rule, the solution
    
    $$
    x = \begin{pmatrix}A_1^{-1}b_J \\ 0\end{pmatrix}
    $$
    
    is an integer solution on the minimal face.

Among common graph-theory models, the coefficient matrices of the linear programming problems corresponding to network flow, shortest paths, bipartite graphs, etc. are all totally unimodular matrices. Therefore, as long as these problems involve only integer parameters, their optimal solutions can be taken as integers, without worrying that the solution of the linear programming problem corresponds to a fractional flow, fractional matching, etc. So problems such as [maximum flow](../graph/flow/max-flow.md), [minimum cut](../graph/flow/min-cut.md), [minimum-cost flow](../graph/flow/min-cost.md), [shortest paths](../graph/shortest-path.md), [difference constraints](../graph/diff-constraints.md), and [maximum (weight) bipartite matching and minimum vertex cover](../graph/graph-matching/bigraph-match.md#线性规划形式) can all be transformed into linear programming problems to solve. Moreover, maximum flow and minimum cut, shortest paths and difference constraints, maximum bipartite matching and minimum vertex cover are pairwise dual problems of each other.

Besides this, there are also some common graph-theory models whose feasible solutions happen to be all the vertices of some polytope whose vertices are all integer points. Therefore, by cleverly choosing the constraints, one can make the solution of the corresponding combinatorial optimization problem exactly the optimal solution of some linear programming problem. For example, graph-theory models such as general graph matching and spanning trees belong to this case, so problems such as [general graph maximum (weight) matching](../graph/graph-matching/general-weight-match.md) and [minimum spanning tree](../graph/mst.md) can likewise be transformed into linear programming problems.

## References and notes

-   Schrijver, Alexander. Theory of linear and integer programming. John Wiley & Sons, 1998.
-   Papadimitriou, Christos H., and Kenneth Steiglitz. Combinatorial optimization: algorithms and complexity. Courier Corporation, 1998.
-   [Duality in linear programming. Part 1—definition and construction. by adamant - Codeforces blog](https://codeforces.com/blog/entry/105049)
-   [Duality in linear programming. Part 2—in competitive programming. by adamant - Codeforces blog](https://codeforces.com/blog/entry/105789)

[^poly-names]: Different references may have different definitions of these two terms: some references call the bounded case a "polyhedron" and the unbounded case a "polytope"; some references do not assume that they must be convex sets; some references use "polyhedron" to refer to polytopes in three-dimensional space. This article adopts definitions consistent with references such as Schrijver (1998) and Boyd and Vandenberghe (2004).

[^reducible]: A more rigorous statement is that they can be reduced to one another in polynomial time.
