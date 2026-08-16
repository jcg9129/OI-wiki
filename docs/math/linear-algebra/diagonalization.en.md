## Eigenspace

All the eigenvectors of a matrix $A$ belonging to $\lambda_0$, together with the zero vector, form a linear space, called an eigenspace of the matrix $A$, denoted $E(\lambda_0)$. It is the solution space of the homogeneous system of linear equations:

$$
(\lambda_0 I-A)X=0
$$

For the eigenspace $E(\lambda_i)=N(\lambda_i I-A)$, by the nullity-plus-rank theorem:

$$
r(\lambda_i I-A)+\operatorname{dim} N(\lambda_i I-A)=n
$$

Therefore, the dimension of the eigenspace $E(\lambda_i)$ is:

$$
\operatorname{dim} E(\lambda_i)=n-r(\lambda_i I-A)
$$

also called the **geometric multiplicity** of $\lambda_i$.

## Invariant subspace

When studying a linear transformation $T$, one often hopes to choose a basis of the space $V$ such that the matrix of the linear transformation $T$ under this basis has as simple a shape as possible.

Let $V$ be a linear space over a number field $F$, $W$ be a subspace of $V$, and $T$ be a linear transformation on $V$. If for any vector $x$ in $W$, $T(x)$ is also in $W$ (also said that the space is invariant or stable under the transformation), then $W$ is called an invariant subspace of $T$.

The space being invariant under the transformation does not mean the coordinates truly "do not change" under the transformation; it may have undergone a stretching or other deformation, only that after the deformation it still lies in the space.

-   Any subspace of a linear space $V$ is an invariant subspace of a scalar-multiplication transformation.
-   For any linear transformation $T$ in $V$, the space $V$ and the zero subspace are both invariant subspaces of $T$, called trivial invariant subspaces.
-   The intersection and sum of invariant subspaces are also invariant subspaces.

Let $W$ be an invariant subspace of a linear transformation $T$. Considering only the action of $T$ on the invariant subspace $W$ gives a linear transformation of the subspace $W$ itself, called the restriction of $T$ to the subspace $W$, denoted ${T|}_W$.

For any linear transformation $T$ in $V$, the image space $R(T)$ and the null space $N(T)$ are invariant subspaces of $T$. The meaning of these two cases is that the space $V$, before and after the transformation, completes its own compression (image space), or is compressed to $0$ (null space).

For any linear transformation $T$ in $V$, the eigenspace of $T$ is an invariant subspace of $T$.

## Primary decomposition

By the fundamental theorem of algebra, the minimal polynomial can be factored as:

$$
m_A(\lambda)={(\lambda-\lambda_1)}^{r_1}\cdots{(\lambda-\lambda_S)}^{r_S}
$$

Considering the null spaces of each factor after substituting the variable $\lambda$ in the minimal polynomial with the matrix $A$, they form a series of invariant subspaces of the matrix $A$:

$$
W_i=N({(\lambda_i I-A)}^{r_i})
$$

Theorem: The dimension of this invariant subspace $W_i$ is exactly the algebraic multiplicity of the eigenvalue $\lambda_i$.

Recall that the algebraic multiplicity refers to the degree of each factor of the characteristic polynomial, and the geometric multiplicity refers to the dimension of the eigenspace $E(\lambda_i)=N(\lambda_i I-A)$. This invariant subspace $W_i$ and the eigenspace $E(\lambda_i)$ are both null spaces of matrices, and the two matrices are related by the $r_i$-th power of the minimal polynomial. That is, the dimension of the eigenspace is the geometric multiplicity; the "eigenspace", after the $r_i$-th power of the minimal polynomial, reaches an "invariant subspace", and the dimension of the invariant subspace reaches the algebraic multiplicity of the characteristic polynomial.

This theorem is in fact a corollary of the primary decomposition theorem below.

Denote by $T$ the linear transformation corresponding to the matrix $A$, and by $T_i={T|}_{W_i}$ its restriction to each subspace $W_i$. Then the minimal polynomial of $T_i$ is $(x-\lambda_i)^{r_i}$.

Theorem: Let $V$ be a linear space over a field $F$, and $T$ be a linear transformation on $V$. Then the space $V$ can undergo a primary decomposition with respect to the linear transformation $T$, split into the direct sum of several invariant subspaces $W_i$.

$$
V=W_1\oplus W_2\oplus\cdots\oplus W_S
$$

This means that the matrix of $T$ under some basis is a quasi-diagonal matrix:

$$
\operatorname{diag}\{A_1,A_2,\cdots,A_S\}
$$

where $A_i$ is the matrix of $T_i$ under the corresponding basis.

This theorem shows that one can use invariant subspaces to simplify the matrix of a linear transformation.

## Diagonalizable matrix

For an $n$-th order square matrix $A$, if it is similar to a diagonal matrix, then $A$ is called a diagonalizable matrix, or a simple matrix.

-   The sum, product, and inverse of diagonal matrices, if they exist, are still diagonal matrices, and the elements on their diagonal are its eigenvalues.
-   The matrix of a linear transformation $T$ being a diagonalizable matrix is equivalent to the matrix of $T$ under some basis being a diagonal matrix.

Theorem: Let all the distinct eigen-roots of a matrix $A$ be $\lambda_1,\cdots,\lambda_m$; then the following propositions are equivalent:

-   The matrix $A$ is diagonalizable.
-   The matrix $A$ has $n$ linearly independent eigenvectors.
-   The following formula holds:

$$
\operatorname{dim} E(\lambda_1)+\cdots+\operatorname{dim} E(\lambda_m)=n
$$

It has been pointed out earlier that the degree of an eigenvalue in the factorization of the characteristic polynomial is called the algebraic multiplicity, and the dimension of an eigenspace is called the geometric multiplicity. This theorem also shows that the matrix $A$ being diagonalizable is equivalent to the algebraic multiplicity of each eigenvalue $\lambda$ of $A$ being equal to its geometric multiplicity.

Corollary: If an $n$-th order square matrix $A$ has exactly $n$ distinct eigenvalues, then it must be diagonalizable. The converse is not necessarily true.

Theorem: A matrix $A$ is diagonalizable if and only if the minimal polynomial of $A$ has no repeated roots.

Matrix similarity also preserves the linear dependence relationships among eigenvectors.

Eigenvectors may well not be real, and it is also entirely possible that one cannot find $n$ linearly independent eigenvectors.

For a repeated eigenvalue, the eigenvectors span a space. To describe this space, one needs to choose representatives from it. One generally chooses linearly independent representatives, and the number of representatives is the dimension of the space.

When choosing representatives, one often orthogonalizes and normalizes them. What one finally obtains is a set of orthonormal representatives.

Eigenvectors are not necessarily orthogonal; eigenvectors of different eigenvalues may not be orthogonalizable. Therefore orthogonalization can only be performed on the eigenvectors of a repeated eigenvalue. But normalization can be performed on any eigenvector.

## Nilpotent matrix

Let $T$ be a linear transformation of the space $V$. If there exists a positive integer $r$ such that $T^r$ is the zero transformation, then $T$ is called a nilpotent transformation of the space $V$.

A matrix satisfying the condition $N^r=0$ for some positive integer $r$ is called a nilpotent matrix.

One can generally further assume that $r$ is the smallest positive integer making $T^r$ the zero transformation, so the minimal polynomial of $T$ is $x^r$. Then there exists a vector $\xi_0$ such that:

-   $$
    T^r(\xi_0)=0
    $$
-   $$
    T^{r-1}(\xi_0)\neq 0
    $$

### Cyclic subspace

Theorem: Let $T$ be a linear transformation of the space $V$, and $\xi$ be a vector of the space $V$. If there exists a positive integer $s$ such that:

-   $$
    T^s(\xi)=0
    $$
-   $$
    T^{s-1}(\xi)\neq 0
    $$

then the vectors $\xi,T(\xi),\cdots,T^{s-1}(\xi)$ are linearly independent.

From this theorem one can give a definition:

Let $T$ be a linear transformation of the space $V$, and $W$ be a subspace of $V$. If there exists a vector $\xi_0$ and a positive integer $r$ such that:

-   the vectors $\xi_0,T(\xi_0),\cdots,T^{r-1}(\xi_0)$ form a basis of $W$.
-   the following equation holds:

    $$
    T^r(\xi_0)=0
    $$

then the subspace $W$ is called a cyclic subspace with respect to $T$, $T$-cyclic subspace for short. In this case $\xi_0$ is called a generating vector of the cyclic subspace $W$, and the vectors $\xi_0,T(\xi_0),\cdots,T^{r-1}(\xi_0)$ are called a cyclic basis of $W$.

Obviously, a $T$-cyclic subspace $W$ is invariant under the action of $T$, and for any vector $\xi$ in the cyclic subspace $W$, $T^r(\xi)=0$, where $r$ is the dimension of the cyclic subspace.

### Nilpotent Jordan block

If the space $W$ is a cyclic subspace of the transformation $T$, then the restriction ${T|}_W$ of $T$ to $W$ is a nilpotent transformation of $W$, and the matrix of ${T|}_W$ with respect to the reverse-ordered cyclic basis $T^{r-1}(\xi_0),T^{r-2}(\xi_0),\cdots,\xi_0$ of $W$ is the following $r$-th order upper-triangular matrix:

$$
N_r=\begin{pmatrix}
0 & 1 & 0 & \cdots & 0 & 0\\
0 & 0 & 1 & \cdots & 0 & 0\\
0 & 0 & 0 & \cdots & 0 & 0\\
\vdots & \vdots & \vdots &   & \vdots& \vdots\\
0 & 0 & 0 & \cdots & 0 & 1\\
0 & 0 & 0 & \cdots & 0 & 0\\
\end{pmatrix}
$$

The matrix $N_r$ is called an $r$-th order nilpotent Jordan matrix, or an $r$-th order nilpotent Jordan block.

Let $T$ be a nilpotent transformation of the $n$-dimensional space $V$; the uniquely determined group of positive integers $r_1\geq\cdots\geq r_S$ appearing in the decomposition of $V$ into cyclic subspaces with respect to $T$ is called the invariant indices of $T$.

For an $n$-th order nilpotent matrix $A$, $A$ is similar to a matrix $N$ of the above shape, which also uniquely determines a sequence of positive integers $r_1\geq\cdots\geq r_S$, called the invariant indices of the matrix $A$.

Although a nilpotent matrix cannot be similar to a diagonal matrix, it can be similar to such a canonical form. In the Jordan canonical form, combining diagonalization by similarity and the canonical form of a nilpotent matrix gives the canonical form that a general matrix can reach via a similarity transformation.

### Some theorems

1.  Let $T$ be a nilpotent transformation of the space $V$, and

    $$
    h(x)=a_0+a_1x+\cdots+a_mx^m
    $$

    be a polynomial; then the linear transformation $h(T)$ has an inverse transformation if and only if $a_0\neq 0$. When $h(T)$ is invertible, the inverse transformation of $h(T)$ is also a polynomial of $T$.

2.  Let $T$ be a nilpotent transformation of the space $V$, $W$ be an $r$-dimensional $T$-cyclic subspace, and $\xi$ be a vector in $W$. If there exists an integer $k$ such that

    $$
    T^{r-k}(\xi)=0
    $$

    then there exists a vector $\eta$ in $W$ such that

    $$
    \xi=T^k(\eta)
    $$

3.  Let $T$ be a nilpotent transformation of the $n$-dimensional space $V$, $x^r$ be the minimal polynomial of $T$, and let $W_1$ be an $r$-dimensional $T$-cyclic subspace; then there exists a complementary subspace $W_2$ of $W_1$ such that:

    $$
    V=W_1\oplus W_2
    $$

    and $W_2$ is also invariant under the action of $T$.

4.  Let $T$ be a nilpotent transformation of the $n$-dimensional space $V$; then $V$ can be decomposed into a direct sum of $T$-cyclic subspaces:

    $$
    V=W_1\oplus W_2\oplus\cdots\oplus W_S
    $$

5.  Every $n$-th order nilpotent matrix is similar to a matrix of the form:

    $$
    N=\begin{pmatrix}
    N_{r_1} &   &   & 0\\
      & N_{r_2} &   &  \\
      &   & \cdots &  \\
    0 &   &   & N_{r_S}\\
    \end{pmatrix}
    $$

    where each $N_{r_i}$ is an $r_i$-th order nilpotent Jordan block.

6.  If it is stipulated that the $T$-cyclic subspaces $W_i$ are arranged in descending order of dimension $r_i$, $r_1\geq\cdots\geq r_S$, then the way of decomposing $V$ into $T$-cyclic subspaces is uniquely determined by $T$.
