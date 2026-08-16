author: codewasp942, Tiphereth-A

A linear space is a generalization of $d$-dimensional Euclidean space ($0\leq d\leq 3$) and the like; for the relationships among the related concepts, refer to [the relationship between Euclidean space and linear space](#the-relationship-between-euclidean-space-and-linear-space).

Prerequisites: Abelian group, field.

Loosely speaking, a set that is closed under some operation and satisfies associativity, an identity, and inverses forms a group. If it also satisfies commutativity, then it forms an Abelian group.

If a set is closed under the four arithmetic operations, then it forms a field. For the relevant definitions, see [Basic concepts of abstract algebra](../algebra/basic.md#fields).

## Definition

A linear space (vector space) is a basic concept and an important object of study in linear algebra. A linear space is a module-like algebraic structure composed of a set of vectors $V$, a field $\Bbb{P}$, an addition operation $+$, and scalar multiplication.

Specifically, let $(V,+)$ be an Abelian group and $\Bbb{P}$ be a field.

Define an algebraic operation between numbers in $\Bbb{P}$ and elements of $V$, called **scalar multiplication**: $\cdot:\Bbb{P}\times V\mapsto V$, denoted $p\cdot v$ or $pv$, where $p$ is in the field $\Bbb{P}$ and $v$ is in the Abelian group $V$. This scalar-multiplication operation is required to be closed, so that the operation result is always meaningful and also in the group $V$.

And it satisfies the following conditions:

1.  **Distributivity of scalar multiplication over vector addition**: for $\mathbf u,\mathbf v\in V,a\in \Bbb{P}$, $a(\mathbf u+\mathbf v)=a\mathbf u+a\mathbf v$
2.  **Distributivity of scalar multiplication over scalar addition**: for $a,b\in \Bbb{P},\mathbf u\in V$, $(a+b)\mathbf u=a\mathbf u+b\mathbf u$
3.  **Associativity of scalar multiplication (consistent with field multiplication)**: for $a,b\in \Bbb{P},\mathbf u\in V$, $a(b\mathbf u)=(ab)\mathbf u$
4.  **Identity of scalar multiplication**: let $1\in \Bbb{P}$ be the multiplicative identity of $\Bbb{P}$; then for $u\in V$, $1\mathbf u=\mathbf u$

Then the algebraic system $(V,+,\cdot,\mathbb{P})$ is said to be that $V$, with respect to $+,\cdot$, forms a **linear space** over $\Bbb{P}$; $\Bbb{P}$ is the **base field** of the linear space, the elements of $V$ are called **vectors**, and the elements of $\Bbb{P}$ are called **scalars**. When the field $\Bbb{P}$ is the real field, it is called a real linear space. When the field $\Bbb{P}$ is the complex field, it is called a complex linear space.

Whether it is a row of numbers, an arrow, or something else, as long as it satisfies the above axioms, it can be regarded as a vector, and can thus be studied using the theory of linear algebra.

The zero element of the additive group is called the zero vector, denoted $\mathbf 0$ or $\mathbf\theta$.

The addition and subtraction of vectors in the original Abelian group, together with the scalar multiplication newly defined in the linear space, are collectively called **linear operations**.

???+ note "Note"
    For convenience of writing, in the following:
    
    1.  Elements of $V$ are not bolded.
    2.  An algebraic system $(V,+,\cdot,\mathbb{P})$ satisfying the definition of a linear space is also called a linear space.
    
    Please distinguish between them.

### Intuitive understanding

Not very rigorously speaking, scalar multiplication corresponds to a kind of "**scaling**", the elements in the base field $\Bbb{P}$ represent the "**ratio**" of the scaling, and vector addition corresponds to "**superposition**". At the same time, the elements in $\Bbb{P}$ also represent the range of values of the "**coordinates**" of a vector.

Conditions 1-4 describe the connection between "scaling" and "superposition". This can be understood by combining it with arrows on the two-dimensional plane.

### Simple properties

???+ note "Note"
    The following properties can be found in group theory, etc.

For a linear space $(V,+,\cdot,\Bbb{P})$,

1.  $\theta$ is unique
2.  $\forall\alpha\in V$, $-\alpha$ is unique
3.  $\exists 0\in\mathbb{P}$, $\forall\alpha\in V$, we have $0\alpha=\theta$
4.  $\forall k\in\mathbb{P}$, we have $k\theta=\theta$
5.  $(-1)\alpha=-\alpha,~\forall\alpha\in V$
6.  No zero divisors: $\forall\alpha\in V,k\in\mathbb{P}$, we have $k\alpha=\theta\implies k=0\lor\alpha=\theta$
7.  Cancellation law of addition: $\forall\alpha,\beta,\gamma\in V$, we have $\alpha+\beta=\alpha+\gamma\implies\beta=\gamma$

    > In fact, the cancellation law of addition is a property of Abelian groups.

### Examples

1.  $\Bbb{P}^n$, with respect to the addition and multiplication over the number field $\Bbb{P}$, forms a linear space over $\Bbb{P}$. For example, $\Bbb{P}$ can be $\Bbb{R}$, $\Bbb{C}$, $\Bbb{N}_p$ ($p$ prime), etc.
2.  The $n\times m$ matrices $\Bbb{P}^{n\times m}$ over a number field $\Bbb{P}$, with respect to matrix addition and scalar multiplication, form a linear space over $\Bbb{P}$.
3.  The univariate polynomial ring $\Bbb{P}[x]$ over a number field $\Bbb{P}$, with respect to polynomial addition and scalar multiplication, forms a linear space over $\Bbb{P}$.
4.  All continuous functions on the interval $[a,b]$ (denoted $C[a,b]$), with respect to "function addition" and "scalar multiplication of a value with a continuous function", form a linear space over the value range.

## Related concepts

### Linear dependence, linear independence

For a linear space $(V,+,\cdot,\Bbb{P})$:

1.  $a_1,a_2,\dots,a_n\in V$ is called a **vector group** of $V$.
2.  For $k_1,k_2,\dots,k_n\in\Bbb{P}$, $\sum_{i=1}^nk_ia_i$ is called a **linear combination** of the vector group $a_1,a_2,\dots,a_n$.
3.  If a vector $\beta\in V$ can be expressed as a linear combination of the vector group $a_1,a_2,\dots,a_n$, then $\beta$ is said to be **linearly represented** by the vector group $a_1,a_2,\dots,a_n$.
4.  For $k_1,k_2,\dots,k_n\in\Bbb{P}$, if the vector group $a_1,a_2,\dots,a_n$ satisfies $\sum_{i=1}^nk_ia_i=\theta\iff k_i=0, i=1,2,\dots,n$, then the vector group $a_1,a_2,\dots,a_n$ is said to be **linearly independent**; otherwise the vector group $a_1,a_2,\dots,a_n$ is said to be **linearly dependent**.

It is stipulated that the zero vector is linearly dependent with any vector.

An expression of linear representation or linear dependence can be written in the form of matrix multiplication:

$$
\beta=k_1a_1+k_2a_2+\cdots+k_ra_r=(a_1,a_2,\cdots,a_r)\begin{pmatrix} k_1 \\ k_2 \\ \vdots \\ k_r \end{pmatrix}
$$

By convention, the vectors $a$ are written side by side in order on the left; the scalars $k$ are written vertically in order on the right, forming a "column vector".

Note: the "column vector" formed by scalars here is only a convenient notational form; it is not in the space $V$ and is essentially different from the vectors on the left. If the vectors on the left happen to be column vectors, placing them side by side can formally form a "matrix", and the above product is precisely the "matrix left-multiplying a column vector" form common in matrices.

As pointed out below, the linear representation here is also equivalent to: the vector $\beta$ lies in the image space of the matrix $(a_1,a_2\cdots,a_r)$.

According to the definition below, the zero vector always lies in the image space. From the viewpoint of a linear transformation, linear dependence is equivalent to multiple vectors being transformed to the zero vector after the transformation, while linear independence is equivalent to only the zero vector itself being transformed to the zero vector.

#### Properties

For a linear space $(V,+,\cdot,\Bbb{P})$,

1.  If a part of a vector group is linearly dependent, then the vector group is linearly dependent. If a vector group is linearly independent, then any of its non-empty parts is linearly independent. Abbreviated as: **"large independent, small independent"; "small dependent, large dependent"**.
2.  A vector group containing $\theta$ is linearly dependent.
3.  A vector group is linearly dependent if and only if some vector of the vector group can be linearly represented by the other vectors.
4.  If a vector $\beta$ can be linearly represented by the vector group $a_1,a_2,\dots,a_n$, then the representation is unique if and only if the vector group $a_1,a_2,\dots,a_n$ is linearly independent.
5.  If the vector group $a_1,a_2,\dots,a_n$ is linearly independent, then a vector $\beta$ can be linearly represented by the vector group $a_1,a_2,\dots,a_n$ if and only if the vector group $a_1,a_2,\dots,a_n,\beta$ is linearly dependent.

### Maximal linearly independent group, rank

Linear dependence can be understood as "redundant", indicating that some vector within the vector group can be represented by other vectors and can be deleted. After deleting them, what remains is a maximal linearly independent group.

For a linear space $(V,+,\cdot,\Bbb{P})$:

1.  For a vector group $b_1,b_2,\dots,b_m$, let $\{a_1,a_2,\dots,a_n\}\subseteq\{b_1,b_2,\dots,b_m\}$; if:

    -   the vector group $a_1,a_2,\dots,a_n$ is linearly independent.
    -   $\forall\beta\in\{b_1,b_2,\dots,b_m\}\setminus\{a_1,a_2,\dots,a_n\}$, the vector group $a_1,a_2,\dots,a_n,\beta$ is linearly dependent.

    then the vector group $a_1,a_2,\dots,a_n$ is called a **maximal linearly independent group** of the vector group $b_1,b_2,\dots,b_m$. Similarly, one can define a maximal linearly independent group of a linear space $V$.

    It is stipulated that the maximal linearly independent group of the vector group $\theta,\theta,\dots,\theta$ is the empty set, so the vector group corresponding to an all-$0$ matrix has no maximal linearly independent group.

    The way of deleting vectors from a vector group is not unique, so a maximal linearly independent group is also not unique. By convention, one deletes from left to right in order.

    Coincidentally, deleting in order, the vectors that remain are precisely, in the "look by rows" viewpoint, the columns in which the element $1$ lies in the reduced row echelon form matrix remaining from Gaussian elimination.

    The size of a maximal linearly independent group of the vector group $b_1,b_2,\dots,b_m$ is called the **rank** of the vector group, denoted $\operatorname{rank}\{b_1,b_2,\dots,b_m\}$; it is stipulated that $\operatorname{rank}\{\theta,\theta,\dots,\theta\}=0$.

    Thus, the definition of the rank of a vector group is entirely consistent with the definition of the rank of a matrix.

2.  If the vector group $a_1,a_2,\dots,a_n$ can linearly represent all vectors in the vector group $b_1,b_2,\dots,b_m$, then the vector group $b_1,b_2,\dots,b_m$ is said to be linearly representable by the vector group $a_1,a_2,\dots,a_n$.

3.  If the vector group $a_1,a_2,\dots,a_n$ can be linearly represented by the vector group $b_1,b_2,\dots,b_m$, and the vector group $b_1,b_2,\dots,b_m$ can be linearly represented by the vector group $a_1,a_2,\dots,a_n$, then the two vector groups are said to be **equivalent**, denoted $\{a_1,a_2,\dots,a_n\}\cong\{b_1,b_2,\dots,b_m\}$.

    The **equivalence** of vector groups means that the spaces spanned by the vector groups are the same. Vector groups spanning the same space are equivalent to one another, and vector groups spanning different spaces are not equivalent.

    Equivalence of vector groups is a stronger condition than equivalence of matrices; it requires not only equal ranks but also that the spaces be completely the same. Therefore, placing two matrices together **horizontally**, the rank cannot change.

    Equivalence of matrices only requires equal ranks, so matrix equivalence means the former matrix or space can reach the latter matrix or space via an invertible transformation.

#### Properties

For a linear space $(V,+,\cdot,\Bbb{P})$,

1.  Suppose the vector group $a_1,a_2,\dots,a_n$ can be linearly represented by the vector group $b_1,b_2,\dots,b_m$.
    -   If $n>m$, then the vector group $a_1,a_2,\dots,a_n$ is linearly dependent.
    -   If the vector group $a_1,a_2,\dots,a_n$ is linearly independent, then $n\leq m$.

2.  Equivalent linearly independent vector groups have equal sizes.

    Any maximal linearly independent group of a vector group has the same size.

3.  A vector group is linearly independent if and only if its rank equals its size.

4.  If the vector group $a_1,a_2,\dots,a_n$ can be linearly represented by the vector group $b_1,b_2,\dots,b_m$, then $\operatorname{rank}\{a_1,a_2,\dots,a_n\}\leq\operatorname{rank}\{b_1,b_2,\dots,b_m\}$.

5.  Equivalent vector groups have equal ranks.

### Linear span

For a linear space $(V,+,\cdot,\Bbb{P})$, $\left\{v=\sum_{i=1}^nk_ia_i:a_i\in V,k_i\in\Bbb{P},i=1,2,\dots,n\right\}$ also forms a linear space, called the linear space **spanned** by the vector group $a_1,a_2,\dots,a_n$ (or the **linear span**), denoted $\operatorname{span}\{a_1,a_2,\dots,a_n\}$.

The $n$ vectors $a$ here are not necessarily linearly independent.

### Linear subspace

For a linear space $(V,+,\cdot,\Bbb{P})$, if the algebraic system $(V_1,+,\cdot,\Bbb{P})$ satisfies:

1.  $\varnothing\ne V_1$
2.  $V_1\subseteq V$
3.  $V_1$, with respect to $+,\cdot$, forms a linear space over $\mathbb{P}$

then $V_1$ is called a linear subspace of $V$, subspace for short, denoted $V_1\leq V$.

Any space $V$ has two **trivial subspaces**: itself $V$ and the zero subspace. The zero subspace contains only the zero vector and contains no linearly independent vectors.

If the $\subseteq$ in condition 2 is replaced by $\subset$, then $V_1$ is called a proper linear subspace of $V$, denoted $V_1<V$.

It is not hard to prove: a non-empty subset $V_1$ of a linear space $V$ is a linear subspace of it if and only if the linear operations are closed on $V_1$, i.e.:

1.  $\forall u,v\in V_1$, $u+v\in V_1$
2.  $\forall v\in V_1$, $\forall k\in \Bbb{P}$, $kv\in V_1$

### Intersection, sum and direct sum, direct product

For linear spaces $(V_1,+,\cdot,\Bbb{P})$ and $(V_2,+,\cdot,\Bbb{P})$:

1.  It is not hard to verify: addition and scalar multiplication are closed on $V_1\cap V_2$, so $V_1\cap V_2$ can be called the **intersection** of the linear spaces $V_1$ and $V_2$.

    Similarly, one can define the intersection of multiple linear spaces $\bigcap_{i=1}^m V_i$.

2.  If a linear space $V$ satisfies $V=\{u+v|u\in V_1,v\in V_2\}$, then $V$ is called the **sum** of the linear spaces $V_1$ and $V_2$, denoted $V=V_1+V_2$.

    One can verify: $V_1+V_2$ is the smallest subspace containing $V_1\cup V_2$.

    Similarly, one can define the sum of multiple linear spaces $\sum_{i=1}^m V_i$.

3.  Suppose $V=V_1+V_2$; if for any element $v$ in the linear space $V$, one can find only a unique pair of vectors $v_1,v_2$ satisfying $v=v_1+v_2$, then $V$ is called the **direct sum** of the linear spaces $V_1$ and $V_2$, denoted $V_1\oplus V_2$.

    Similarly, one can define the direct sum of multiple linear spaces $\bigoplus_{i=1}^m V_i$.

4.  The **direct product** $V_1\times V_2$ of $V_1$ and $V_2$ is defined as the linear space over $\Bbb{P}$ formed by the Cartesian product of the two with respect to the following addition and scalar multiplication:

    1.  $+:(V_1\times V_2)\times(V_1\times V_2)\mapsto V_1\times V_2; ((u_1,v_1),(u_2,v_2))\to (u_1+u_2,v_1+v_2)$
    2.  $\cdot:\Bbb{P}\times(V_1\times V_2)\mapsto V_1\times V_2; (k,(u,v))\to (ku,kv)$

    Similarly, one can define the direct product of multiple linear spaces $\prod_{i=1}^m V_i$.

#### Examples

For the linear space $V=\Bbb{R}^3$, let the linear spaces:

-   $V_1:=\{(x,0,0)|x\in\Bbb{R}\}$
-   $V_2:=\{(x,y,0)|x,y\in\Bbb{R}\}$
-   $V_3:=\{(0,y,z)|y,z\in\Bbb{R}\}$
-   $V_4:=\{(x,0,z)|x,z\in\Bbb{R}\}$

then

1.  $V_1<V_2<V$, $V_3<V$
2.  $V_2=V_1+V_2$
3.  $V=V_1\oplus V_3=V_2+V_3$
4.  $V_2+V_3\leq V$

#### Properties

1.  Let $V_1,V_2,V_3$ be linear spaces over $\Bbb{P}$; like the intersection of sets, the intersection of linear spaces obeys the following laws:
    1.  Commutativity: $V_1\cap V_2=V_2\cap V_1$
    2.  Associativity: $V_1\cap(V_2\cap V_3)=(V_1\cap V_2)\cap V_3$
2.  Let $V_1,V_2,V_3$ be linear spaces over $\Bbb{P}$; similar to the union of sets, the sum of linear spaces obeys the following laws:
    1.  Commutativity: $V_1+V_2=V_2+V_1$
    2.  Associativity: $V_1+(V_2+V_3)=(V_1+V_2)+V_3$
3.  Let $V_1,V_2,V_3$ be linear spaces over $\Bbb{P}$; the intersection and sum of linear spaces have the following relationships:
    1.  $V_1\cap (V_2+V_3)\supseteq (V_1\cap V_2)+(V_1\cap V_3)$
    2.  $V_1+(V_2\cap V_3)\subseteq (V_1+V_2)\cap (V_1+V_3)$
4.  $\operatorname{span}\{a_1,a_2,\dots,a_n\}+\operatorname{span}\{b_1,b_2,\dots,b_m\}=\operatorname{span}\{a_1,a_2,\dots,a_n,b_1,b_2,\dots,b_m\}$
5.  Let $V_1,V_2$ be linear spaces over $\Bbb{P}$; then the following are equivalent:

    1.  $V_1+V_2=V_1\oplus V_2$

    2.  $\exists \beta\in V_1+V_2$ such that the way of splitting into a sum of vectors in $V_1$ and $V_2$ is unique (any $\to$ exists)

    3.  The way of splitting $\theta$ into a sum of vectors in $V_1$ and $V_2$ is unique

    4.  $V_1\cap V_2=\{\theta\}$

    ???+ note "Proof"
        $1\implies 2$: immediate from the definition.
        
        $2 \implies 3$:
        
        Let $\beta=\beta_1+\beta_2$, where $\beta_1\in V_1, \beta_2\in V_2$; if $\theta=\alpha_1+\alpha_2$, $\theta\ne\alpha_1\in V_1,\alpha_2\in V_2$, then $\beta=\beta+\theta=(\beta_1+\alpha_1)+(\beta_2+\alpha_2)$.
        
        But $\beta_1\ne\beta_1+\alpha_1$, contradicting the condition.
        
        $3 \implies 4$:
        
        Take a nonzero vector $\alpha$ in $V_1$ and $V_2$; then $\theta=\alpha+(-\alpha)=(-\alpha)+\alpha$, which contradicts the condition.
        
        $4 \implies 1$:
        
        If $V_1+V_2$ is not a direct sum, then there exists $\beta\in V_1+V_2$ such that $\beta=\beta_1+\beta_2=\gamma_1+\gamma_2$, where $\beta_1,\gamma_1\in V_1,\beta_2,\gamma_2\in V_2$ and $\beta_1,\beta_2,\gamma_1,\gamma_2$ are mutually distinct.
        
        Furthermore $\theta\ne\beta_1-\gamma_1=\gamma_2-\beta_2\in V_1\cap V_2$, contradicting the condition.

### Isomorphism

Let $V,V'$ both be linear spaces over a field $\Bbb{P}$; if there exists a bijection $\sigma:V\mapsto V'$ that preserves addition and scalar multiplication, i.e. $\forall u,v\in V$, $\forall k\in\Bbb{P}$ satisfies:

1.  $\sigma(u+v)=\sigma(u)+\sigma(v)$
2.  $\sigma(ku)=k\sigma(u)$

then $\sigma$ is called an **isomorphism** from $V$ to $V'$, and $V$ and $V'$ are said to be **isomorphic**, denoted $V\cong V'$.

???+ note "Note"
    If $\sigma$ is injective, one can define a **monomorphism**; if $\sigma$ is surjective, one can define an **epimorphism**.

#### Properties

1.  Two linear spaces over a field $\Bbb{P}$ are isomorphic if and only if their dimensions are equal. (For the definition of dimension, see [linear basis](./basis.md).)
2.  (Corollary of 1) An $n$-dimensional linear space over a field $\Bbb{P}$ is isomorphic to the linear space $\Bbb{P}^n$.

    ???+ note "Note"
        This property shows that we can basically regard coordinates and vectors as identical.

## The relationship between Euclidean space and linear space

Taking the three-dimensional Euclidean space we are most familiar with as an example, the correspondence of some of its related concepts in a linear space is shown in the following table:

| Three-dimensional Euclidean space | Linear space |
| -------- | ----------------- |
| Vector | Vector |
| Perpendicular | Orthogonal (i.e. inner product is $0$) |
| Three vectors collinear/coplanar | $k$ vectors linearly dependent |
| Three vectors not coplanar | $k$ vectors linearly independent |
| Basis vectors | [Linear basis](./basis.md) |
| Dimension of the space | Dimension of the space |

## Applications

From this section on, we mainly discuss the "look by columns" viewpoint of a system of linear equations.

The matrix $A$ itself is also composed of column vectors. Regarding $A$ itself as a group of column vectors, and $x$ as the coefficients of the unknowns, consider whether this group of column vectors in $A$ can be matched with unknowns to make up the column vector $b$. In this case the column vector $x$ is completely unknown.

The equation $Ax=b$ studied here, rearranged, is:

$$
\alpha_1 x_1 +\alpha_2 x_2 +\cdots+\alpha_n x_n=b 
$$

In this case, in matrix multiplication, the matrix $A$ on the left can be regarded as a vector group, i.e. a group of column vectors. This group of column vectors, as a basis, spans a space, and we investigate whether the column vector $b$ lies in this space.

### Looking at the solution of a system of linear equations by columns

The rank is the number of vectors in the maximal linearly independent group, representing "constraints". Then the remaining vectors will give the solution its degrees of freedom, i.e. allow redundant vectors to be given in other directions.

If we denote by $n$ the number of columns of the matrix $A$, i.e. the number of column vectors it contains, and denote by $r(A)$ the rank of the matrix $A$, then the degrees of freedom $S$:

$$
S=n-r(A)
$$

All the solutions of the system also form a vector group, and the degrees of freedom $S$ is the rank of the solution vector group of $Ax=0$, i.e. the dimension of the null space discussed below.

### Systems of equations with the same solutions

The common solutions of two systems of equations are defined as the intersection of the two solution sets.

Two systems of equations **having the same solutions** means that the solution sets of the systems are equal. Systems with equal solution sets have the same solutions, and systems with unequal solution sets do not have the same solutions.

Having the same solutions is also a stronger condition than matrix equivalence; it requires not only equal ranks but also that, after placing the two matrices together **vertically**, the rank still does not change.

Comparing this with the equivalence of vector groups: equivalence of vector groups requires that placing the matrices together horizontally, the rank does not change. Therefore, there is the following relationship:

Matrix equivalence does not necessarily have a corresponding equivalence of vector groups or systems with the same solutions, but if there is an equivalence of vector groups or systems with the same solutions, there must be a corresponding matrix equivalence (equal rank).

If the vector groups corresponding to matrices are equivalent, then after transposing the matrices, the corresponding systems of equations have the same solutions, and vice versa.

### The null space and image space of a matrix

The null space and image space in this part are described from the perspective of a linear space.

For a matrix $A$, let $W$ be the set formed by all solutions $x$ of the equation $Ax=0$; then $W$ is a linear space, and the scalar field of $W$ is the same as the field in which the elements of $A$ lie.

The $W$ in this case is called the **null space** of the matrix $A$, denoted $N(A)$.

The null space $N(A)$ of the matrix $A$ is precisely the **solution space** of the equation $Ax=0$. According to the definition of a basis below, a **fundamental system of solutions** of this equation is a basis of the null space.

If the matrix $A$ is an invertible matrix, then the null space $N(A)$ of $A$ contains only the zero vector.

For a matrix $A$, its $n$ columns are vectors $\alpha$; the space spanned by the $n$ column vectors $\alpha$ is called the **image space** of $A$, or the **column space**, denoted:

$$
R(A)=\operatorname{span}\{\alpha_1,\alpha_2,\cdots,\alpha_n\}
$$

According to the definition of dimension below, the dimension of the image space equals the rank of the matrix $A$.

By definition, for each element $y$ in the image space $R(A)$, there is a corresponding representation:

$$
y=k_1\alpha_1+k_2\alpha_2+\cdots+k_n\alpha_n=(\alpha_1,\alpha_2,\cdots,\alpha_n)\begin{pmatrix}k_1\\k_2\\\vdots\\k_n\end{pmatrix}=A\begin{pmatrix}k_1\\k_2\\\vdots\\k_n\end{pmatrix}
$$

Therefore, the image space $R(A)$ is the **range** of $Ax$ for any vector $x$.

Similarly one can define the **row space** of $A$, i.e. the range $R(A^T)$ of the transpose of $A$.

Since the row rank of a matrix equals the column rank, the dimension of the row space is also the rank of the matrix, so transposing changes the image space but not the dimension of the image space.

Here one can establish a correspondence with the earlier text:

Equivalence of vector groups is equivalent to the image spaces $R(A)$ of the corresponding matrices being the same.

Systems with the same solutions is equivalent to the row spaces $R(A^T)$ of the corresponding matrices being the same.

## References and notes

1.  Qiu Weisheng, Advanced Algebra (Vol. 2). Tsinghua University Press.
2.  [Vector space](https://en.wikipedia.org/w/index.php?title=Vector_space&oldid=1108546097). *Wikipedia, The Free Encyclopedia*.
