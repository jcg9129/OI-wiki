Studying linear mappings is studying mappings between linear spaces.

A linear mapping can be represented in the form of a matrix, so in linear mappings one can find corresponding relationships for a large number of concepts in matrices.

## Linear mappings and linear transformations

Let $V$ and $W$ be two linear spaces over a field $F$, and $T$ be a mapping from $V$ to $W$.

If for any vectors $x$ and $y$ in $W$ and any scalars $k$ and $l$ in the field $F$, we have:

$$
T(kx+ly)=kTx+lTy
$$

then $T$ is called a linear mapping from $V$ to $W$. If $W=V$, then $T$ is called a linear transformation on $V$.

For example, the identity transformation $T_e$ keeps the space unchanged, and the zero transformation $T_0$ maps the space to the zero space.

One can denote by $L(V,W)$ the set of all linear mappings from $V$ to $W$. For all linear transformations $L(V,V)$, this is also denoted $L(V)$.

### Properties

-   A linear mapping maps the zero vector to the zero vector.
-   A linear mapping preserves the form of linear operations, i.e. the linear mapping of a linear operation equals the linear operation of the linear mappings.
-   A linear mapping preserves linear dependence, i.e. if it is linearly dependent before the mapping, it is also linearly dependent after the mapping.

But a linear mapping does not preserve linear independence. If it is linearly independent before the mapping, it is not necessarily linearly independent after the mapping.

## Matrix representation of a linear mapping

Let the dimension of $V$ be $n$, a basis of $V$ be $\alpha_1,\cdots,\alpha_n$, the dimension of $W$ be $m$, a basis of $W$ be $\beta_1,\cdots,\beta_m$, and $T$ be a linear mapping from $V$ to $W$.

Represent each $\alpha$ after being mapped by $T$ using $\beta$:

$$
T\alpha_j=a_{1j}\beta_1+\cdots+a_{mj}\beta_m
$$

Using matrix notation:

$$
T(\alpha_1,\cdots,\alpha_n)=(T\alpha_1,\cdots,T\alpha_n)=(\beta_1,\cdots,\beta_m)A
$$

The matrix $A$ is called the matrix representation of the linear mapping $T$ under these two bases.

## The null space and image space of a linear mapping

The null space and image space here are described from the perspective of a linear mapping. With the help of the matrix representation, one can see that the null space and image space of a linear mapping are consistent with the null space and image space of a matrix.

Let $T$ be a linear mapping from the space $V$ to the space $W$, and let:

$$
N(T)=\{x\in V|Tx=0\}
$$

$$
R(T)=Im(T)=\{y\in W|y=Tx,Vx\in V\}
$$

It is easy to verify that $N(T)$ is a subspace of $V$ and $R(T)$ is a subspace of $W$; $N(T)$ and $R(T)$ are called the null space and image space of $V$, and the dimension of $N(T)$ is called the **nullity** of $T$, and the dimension of $R(T)$ is called the **rank** of $T$.

Theorem: Let $T$ be a linear mapping from the space $V$ to the space $W$, with $V$ of finite dimension; then $N(T)$ and $R(T)$ are both finite-dimensional, and:

$$
\operatorname{dim} N(T)+\operatorname{dim} R(T)=\operatorname{dim} V
$$

That is, the nullity of $T$ plus its rank equals the dimension of its domain $V$.

## Matrix representation of a linear transformation

Let the dimension of $V$ be $n$, a basis of $V$ be $\alpha_1,\cdots,\alpha_n$, and $T$ be a linear transformation on $V$; then:

$$
T\alpha_j=a_{1j}\alpha_1+\cdots+a_{nj}\alpha_n
$$

Using matrix notation:

$$
T(\alpha_1,\cdots,\alpha_n)=(T\alpha_1,\cdots,T\alpha_n)=(\alpha_1,\cdots,\alpha_n)A
$$

The matrix $A$ is called the matrix representation of the linear transformation $T$ under this basis.

By the structure of the space and the linearity of $T$, $T$ is completely determined by $T\alpha_1,\cdots,T\alpha_n$, so $T$ uniquely determines a matrix $A$.

Theorem: Let the dimension of $V$ be $n$, and $\alpha_1,\cdots,\alpha_n$ be a basis of $V$; taking any $n$-th order square matrix $A$, there is one and only one linear transformation $T$ from $V$ to $V$ such that the matrix of $T$ is exactly $A$.

Corollary: There is a one-to-one correspondence between $L(V,V)$ and all $n$-th order square matrices.

For example: the zero transformation corresponds to the zero matrix, and the identity transformation corresponds to the identity matrix.

## The space formed by linear transformations

Theorem: $L(V)$ can also form a linear space; introduce the operations in $L(V)$: for any $T_1$ and $T_2$ in $L(V)$, any $x$ in $V$, and any $k$ in the field $F$, we have:

$$
(T_1+T_2)x=T_1x+T_2x
$$

$$
(kT_1)x=k(T_1x)
$$

It is easy to verify that $L(V)$ is a linear space over $F$, i.e. the linear transformation space.

For linear transformations $T_1$ and $T_2$ in $L(V)$, define the product $T_1T_2$ of $T_1$ and $T_2$ as:

$$
(T_1T_2)x=T_2(T_1x)
$$

One can verify that $(T_1T_2)$ is also a linear transformation in $L(V)$, and the product of linear transformations satisfies associativity but not commutativity, similar to the product of matrices.

For a linear transformation $T_1$ in $L(V)$, if there is a linear transformation $T_2$ in $L(V)$ such that for any vector $x$ in $V$:

$$
(T_1T_2)x=T_1(T_2x)=x
$$

then $T_2$ is called the inverse transformation of $T_1$, denoted:

$$
T_2=T_1^{-1}
$$

and:

$$
T_1T_2=T_2T_1=T_e
$$

Theorem: Let the dimension of $V$ be $n$, $\alpha_1,\cdots,\alpha_n$ be a basis of $V$; under this basis the matrix of the linear transformation $T_1$ is $A$ and the matrix of $T_2$ is $B$; then:

-   The matrix of the linear transformation $T_1+T_2$ is $A+B$
-   The matrix of the scalar multiplication of a linear transformation $kT_1$ is $kA$
-   The matrix of the product of linear transformations $T_1T_2$ is $AB$
-   If the inverse transformation of the linear transformation $T_1$ exists, its matrix is $A^{-1}$

## Coordinates

Let $n$ vectors $x$ be a basis of the $n$-dimensional space $V$; for any vector $y$ in $V$, let $y$ be:

$$
y=a_1x_1+a_2x_2+\cdots+a_nx_n=(x_1,x_2,\cdots,x_n)\begin{pmatrix}a_1\\a_2\\\vdots\\a_n\end{pmatrix}
$$

The column vector:

$$
\begin{pmatrix}a_1\\a_2\\\vdots\\a_n\end{pmatrix}
$$

is called the **coordinates** of the vector $y$ under the basis $x_1,x_2,\cdots,x_n$.

As one can see, coordinates are a column vector composed of scalars in the field, and should be distinguished from the vectors in the Abelian group.

## Coordinate transformation formula

Let the dimension of $V$ be $n$, with a transformation $T$ in $L(V)$, and the matrix of $T$ under the basis $\alpha_1,\cdots,\alpha_n$ be $A$. Let:

$$
\xi=(\alpha_1,\cdots,\alpha_n)\begin{pmatrix}x_1\\x_2\\\vdots\\x_n\end{pmatrix}
$$

and:

$$
T\xi=T(\alpha_1,\cdots,\alpha_n)\begin{pmatrix}y_1\\y_2\\\vdots\\y_n\end{pmatrix}
$$

then:

$$
T\xi=T(\alpha_1,\cdots,\alpha_n)\begin{pmatrix}y_1\\y_2\\\vdots\\y_n\end{pmatrix}=(\alpha_1,\cdots,\alpha_n)A\begin{pmatrix}x_1\\x_2\\\vdots\\x_n\end{pmatrix}
$$

Column-vector points in the space $V$ are essentially all in the form of "basis times coordinates". A column-vector point $x$ in the space $V$ itself uses the identity matrix $I$ as its basis, i.e. $x=Ix$.

Only with the same basis, when the basis is fixed, a pure linear transformation $T$ is left-multiplying the coordinates by an ordinary matrix.

Regard the linear transformation $T$ as an observation filter on the space $V$. The linear transformation $T$ acts on the space $V$, distorting the space $V$. After adding the filter, the position of the point itself does not change.

This theorem also shows that a linear transformation $T$ on the column-vector basis is equivalent to right-multiplying the basis by a transition matrix.

Thus, between different bases, the coordinate relationship is left-multiplying by the inverse of the transition matrix.

## Transition matrix

Let $n$ vectors $x$ and $n$ vectors $y$ be two bases of the space $V$. For $1\leq i\leq n$, let the coordinates of each vector $y_i$ under the basis $x_1,x_2,\cdots,x_n$ be:

$$
y_i=(x_1,x_2,\cdots,x_n)\begin{pmatrix}a_{1i}\\a_{2i}\\\vdots\\a_{ni}\end{pmatrix}
$$

Then the $n$ vectors $y$ are arranged into the matrix on the left side of the equation, and the $n$ coordinates are arranged into the matrix $A$ on the right side of the equation:

$$
(y_1,y_2,\cdots,y_n)=(x_1,x_2,\cdots,x_n)A
$$

The matrix $A$ is called the **transition matrix** from the basis $x_1,x_2\cdots,x_n$ to the basis $y_1,y_2\cdots,y_n$, also called the transformation matrix.

Obviously the transition matrix is invertible. For the above expression, the transition matrix from the basis $y_1,y_2\cdots,y_n$ to the basis $x_1,x_2\cdots,x_n$ is $A^{-1}$.

As one can see, the transition matrix is a matrix composed of scalars in the field, not a matrix arranged from the vectors in the Abelian group, and should be distinguished.

Let $n$ vectors $x$ and $n$ vectors $y$ be two bases of the space $V$. For the same vector $z$ in the space $V$:

$$
z=(x_1,x_2,\cdots,x_n)\begin{pmatrix}\xi_1\\\xi_2\\\vdots\\\xi_n\end{pmatrix}=(y_1,y_2\cdots,y_n)\begin{pmatrix}\eta_1\\\eta_2\\\vdots\\\eta_n\end{pmatrix}
$$

Substituting into the above

$$
(y_1,y_2\cdots,y_n)=(x_1,x_2\cdots,x_n)A
$$

by uniqueness, we obtain:

$$
\begin{pmatrix}\xi_1\\\xi_2\\\vdots\\\xi_n\end{pmatrix}=A\begin{pmatrix}\eta_1\\\eta_2\\\vdots\\\eta_n\end{pmatrix}
$$

or

$$
\begin{pmatrix}\eta_1\\\eta_2\\\vdots\\\eta_n\end{pmatrix}=A^{-1}\begin{pmatrix}\xi_1\\\xi_2\\\vdots\\\xi_n\end{pmatrix}
$$

This is a transformation purely between coordinates; the coordinate transformation formulas are all in the scalar field. Since the earlier text made a distinction, the vectors in the linear space and the Abelian group are "abstract vectors", while the coordinates and the elements of the transition matrix are all in the scalar field, regarded as "concrete vectors"; the two kinds of vectors should be regarded as "different things".

A matrix can transform the entire space, i.e. all coordinates; the column vector $x$, as coordinates, spreads across the whole space.

The identity matrix $I$ is composed of unit vectors. The matrix $A$ transforms the identity matrix $I$ into each column vector of the matrix $A$, i.e. transforms the unit vectors into each column vector of the matrix $A$. Therefore left-multiplying by the matrix $A$ can also be regarded as transforming the space this way.

Left-multiplying a vector by a matrix can also be regarded as left-multiplying the coordinates by a vector group. From the viewpoint of coordinates:

$$
Iy=Xa
$$

For the same column vector $y$, in the "normal" space, the space represented by the identity matrix $I$, its coordinates are $y$, and in the new space after the transformation, its coordinates will be denoted $a$. In this way, the matrix $X$ is not only a basis in the normal space, but also the transition matrix from the vector group $I$ to the vector group $X$.

A linear transformation $T$ maps one basis to another basis, so the coordinates are also mapped to other coordinates.

If the transition matrix of the linear transformation $T$ corresponding to mapping the basis $\alpha$ to $\beta$ is $A$, then the corresponding basis matrices satisfy $\beta=\alpha A$.

Then the relationship of the coordinates is exactly reversed. Suppose the coordinates after the mapping by the linear transformation $T$ are $b$, i.e. after adding the filter one observes coordinates $b$; then the representation of the point in $V$ is $\beta b$. The way to restore is to use the transition matrix, writing the representation of the point in $V$ as $\alpha Ab$. Thus the view that coordinate transformation is left-multiplying by the inverse of the transition matrix becomes evident.

## Linear transformations and matrix similarity

The relationship of a linear transformation $T$ in the space $V$ to the basis $\alpha$ of the space $V$:

The linear transformation $T$ acts on the basis $\alpha$, mapping the basis $\alpha$ to $T(\alpha)$, which amounts to right-multiplying the basis $\alpha$ by an $A$, i.e. $T(\alpha)=\alpha A$.

The problem matrix similarity considers is: the same linear transformation $T$ is described as the matrix $B$ in the space $V$ with basis $\beta$, and as the matrix $A$ in the space $V$ with basis $\alpha$.

If the transition matrix is $C$, i.e. $\beta=\alpha C$, then what is the connection between the two descriptions $B$ and $A$.

Since it is the same transformation $T$, one can find a fact that the transition-matrix relationship before and after the transformation always holds, i.e.:

$$
T(\beta)=T(\alpha)C=\alpha AC
$$

The linear transformation $T$ is still a right-multiplication from the perspective of the basis $\beta$; the basis $\beta$ is converted to the basis $\alpha$ and then right-multiplied by a $C$, keeping the relationship of the transition matrix $C$ before and after the transformation:

$$
T(\beta)=\beta B=\alpha CB
$$

Thus the problem is solved:

$$
B=C^{-1}AC
$$

Theorem: Let there be a transformation $T$ in $L(V)$; then the matrices of $T$ under different bases are **similar**.

For square matrices $A$ and $B$, if there exists an invertible matrix $C$ such that $B=C^{-1}AC$, then $A$ and $B$ are similar.

Matrix similarity preserves rank, so matrix similarity can imply matrix equivalence. But two equivalent matrices are not necessarily similar.

Since matrix similarity is closely related to shape, matrix similarity has no relationship with the equivalence of vector groups or systems with the same solutions.

Looking back, the interpretation of matrix similarity is 4 equations: $\beta=\alpha C$, $T(\alpha)=\alpha A$, $T(\beta)=\beta B$, $T(\beta)=T(\alpha)C$.

## References

-   [【官方双语/合集】线性代数的本质 - 系列合集 P13 09 - 基变换](https://www.bilibili.com/video/BV1Ls411b7r2)
