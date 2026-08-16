## Jordan decomposition

Let $T$ be a linear transformation on the $n$-dimensional space $V$. If the minimal polynomial of $T$ is:

$$
m_A(\lambda)={(\lambda-\lambda_1)}^{r_1}{(\lambda-\lambda_2)}^{r_2}\cdots{(\lambda-\lambda_k)}^{r_k}
$$

then by the primary decomposition, the space $V$ can be decomposed into a direct sum of subspaces:

$$
V=V_1\oplus V_2\oplus\cdots\oplus V_k
$$

where $V_i=N\left({(A-\lambda_i I)}^{r_i}\right)$, and $A$ is the matrix corresponding to $T$; these subspaces are all invariant under the action of $T$.

Let the transformation $T_i$ be the projection of $V$ onto the subspace $V_i$, i.e. construct a polynomial $u_i(T)$ such that:

-   $$
    T_i=u_i(T)\frac{m_A(T)}{{(T-\lambda_i T_e)}^{r_i}}
    $$
-   $$
    T_1+T_2+\cdots+T_k=T_e
    $$

where $T_e$ denotes the identity transformation of the space $V$. Then we have the properties:

-   The restriction ${T_i|}_{V_i}$ of the transformation $T_i$ to the space $V_i$ is the identity transformation of the space $V_i$.
-   If $i$ and $j$ are unequal, the restriction ${T_i|}_{V_j}$ of the transformation $T_i$ to the space $V_j$ is the zero transformation of the space $V_j$.

Then the transformation $T_i$ maps each vector $\xi$ of the space $V$ to its component $\xi_i$ in the space $V_i$.

Construct the transformation:

$$
T_D=\lambda_1 T_1+\lambda_2 T_2+\cdots+\lambda_k T_k
$$

Since each transformation $T_i$ is a polynomial of the transformation $T$, the transformation $T_D$ is also a polynomial of the transformation $T$, so each subspace $V_i$ is invariant under the transformation $T_D$.

From the above equations, the restriction ${T_D|}_{V_i}$ of the transformation $T_D$ to the subspace $V_i$ is a homothety of the subspace $V_i$ with homothety coefficient $\lambda_i$. Therefore, the transformation $T_D$ can be diagonalized.

Construct:

$$
T_N=T-T_D
$$

Then the transformation $T_N$ is also a polynomial of the transformation $T$, so each subspace $V_i$ is invariant under the transformation $T_N$. For any vector $\xi_i$ in the subspace $V_i$:

$$
{T_N}^{r_i}(\xi_i)={T-T_D}^{r_i}(\xi_i)={T-\lambda_i T_i}^{r_i}(\xi_i)=0
$$

Let $r$ be the maximum of all $r_i$; then for any vector $\xi$ in the space $V$, the $r$-th power of the transformation $T_N$ maps the vector $\xi$ to the zero vector. Therefore the transformation $T_N$ is a nilpotent transformation.

In this way, each transformation $T$ of the space $V$ can be written as:

$$
T=T_D+T_N
$$

where $T_D$ can be diagonalized and $T_N$ is a nilpotent transformation. Because both $T_D$ and $T_N$ are polynomials of the transformation $T$, their products commute:

$$
T_DT_N=T_NT_D
$$

Theorem: Let $T_1$ and $T_2$ be two diagonalizable transformations of the space $V$ with $T_1T_2=T_2T_1$; then there exists a basis such that the matrices of $T_1$ and $T_2$ with respect to this same basis are in diagonal form.

Theorem: Let $T$ be a linear transformation on the $n$-dimensional space $V$; then there exist a diagonalizable transformation $T_D$ and a nilpotent transformation $T_N$ such that:

-   $$
    T=T_D+T_N
    $$
-   $$
    T_DT_N=T_NT_D
    $$

They are both polynomials of the transformation $T$, and they are uniquely determined by the transformation $T$.

This theorem gives a decomposition of the transformation $T$, called the Jordan decomposition of $T$; $T_D$ is called the diagonalizable part of $T$, and $T_N$ is called the nilpotent part of $T$.

Similarly, there is the Jordan decomposition of matrices:

Theorem: Let $A$ be an $n$-th order matrix; then there exist a diagonalizable matrix $D$ and a nilpotent matrix $N$ such that:

-   $$
    A=D+N
    $$
-   $$
    DN=ND
    $$

They are both polynomials of the matrix $A$, and they are uniquely determined by the matrix $A$.

This theorem gives a decomposition of the matrix $A$, called the Jordan decomposition of $A$; $D$ is called the diagonalizable part of $A$, and $N$ is called the nilpotent part of $A$.

## lambda matrix

The part introduced next is a more general matrix containing the variable parameter $\lambda$, not just a table of numbers. This part of the discussion is somewhat broader compared with matrices composed purely of numbers.

For a $\lambda$ matrix, the corresponding field of the corresponding space becomes the field of rational expressions containing one variable $\lambda$.

A matrix whose elements are polynomials in $\lambda$ is called a $\lambda$ matrix, denoted $A(\lambda)$.

Since the polynomial field contains the number field, a numeric matrix is a special $\lambda$ matrix, and the characteristic matrix $\lambda I-A$ of a numeric matrix $A$ is a kind of $\lambda$ matrix.

### Elementary transformations of a lambda matrix

For $\lambda$ matrices, one can likewise define addition/subtraction, multiplication, elementary transformations, and rank. For $\lambda$ square matrices, one can likewise define the determinant, minor, and cofactor.

For $\lambda$ matrices, elementary transformations are mostly the same as for numeric matrices, only the addition transformation is changed to (here taking row transformations as an example):

-   Multiply some row by a polynomial $\varphi(\lambda)$ in $\lambda$ and add it to another row.

Note that the multiplication transformation is not modified. This is because the addition transformation does not change the determinant, while the multiplication transformation changes the determinant. To preserve the rank property of the polynomial field, the determinant can only be changed over the number field.

The corresponding elementary matrices are also modified accordingly.

It is easy to see that the determinants of all three kinds of elementary matrices are nonzero constants, so all are full rank. So their left-multiplication or right-multiplication does not change the rank of the $\lambda$ matrix.

If $A(\lambda)$ becomes $B(\lambda)$ through finitely many elementary transformations, then $A(\lambda)$ and $B(\lambda)$ are said to be equivalent.

For $\lambda$ matrices, if they are equivalent, then their ranks are the same. The converse is not true, which is different from numeric matrices.

## Smith normal form

Theorem: Let the rank of a $\lambda$ matrix be $r$; then $A(\lambda)$ is necessarily equivalent to:

$$
\begin{pmatrix}
D(\lambda) & 0\\
0 & 0\\
\end{pmatrix}
$$

where:

$$
D(\lambda)=\begin{pmatrix}
d_1(\lambda) &  & \\
 & \ddots & \\
 &  & d_r(\lambda)\\
\end{pmatrix}
$$

Each $d_i(\lambda)$ is a monic polynomial, and two adjacent polynomials have the divisibility relation $d_i(\lambda)|d_{i+1}(\lambda)$.

This normal form is called the Smith normal form, and $d_i(\lambda)$ is called an invariant factor.

The specific method of finding the Smith normal form is to eliminate from the upper-left corner to the lower-right corner; each time the upper-left element is the greatest common factor of all the polynomials remaining in the lower-right, and with the help of the upper-left element, one eliminates that row and column all to $0$.

Theorem: The condition that $A(\lambda)$ and $B(\lambda)$ are equivalent is equivalent to the condition that $A(\lambda)$ and $B(\lambda)$ have exactly the same invariant factors.

### Elementary divisors

By the fundamental theorem of algebra, let the factorization of the invariant factors $d_1(\lambda),d_2(\lambda),\cdots,d_m(\lambda)$ of $A(\lambda)$ be:

$$
d_i(\lambda)={(\lambda-\lambda_1)}^{e_{i1}}{(\lambda-\lambda_2)}^{e_{i2}}\cdots{(\lambda-\lambda_S)}^{e_{iS}}
$$

where $\lambda_1,\cdots,\lambda_S$ are mutually distinct. Since:

$$
d_i(\lambda)|d_{i+1}(\lambda)
$$

the exponents $e_{1j},e_{2j},\cdots,e_{mj}$ are increasing, and all the exponents of the last term $d_m(\lambda)$ are nonzero.

All the factors with exponent greater than zero in the above expression are collectively called the elementary divisors of $A(\lambda)$.

Note that elementary divisors are counted with multiplicity. If for some $j$, an exponent $e_{ij}$ appears several times, then the corresponding elementary divisor ${(\lambda-\lambda_j)}^{e_{ij}}$ should also appear the corresponding number of times.

The earlier theorem shows that $A(\lambda)$ and $B(\lambda)$ being equivalent is equivalent to the two having exactly the same invariant factors. If the invariant factors are exactly the same, then naturally the elementary divisors are also exactly the same, but the converse is not true. In fact there is the conclusion:

Theorem: $A(\lambda)$ and $B(\lambda)$ having exactly the same invariant factors is equivalent to having exactly the same elementary divisors and rank.

So "having exactly the same elementary divisors and rank" also becomes a condition for determining the equivalence of $\lambda$ matrices.

During elementary transformations, one can also first transform $A(\lambda)$ into a diagonal matrix, then find the elementary divisors and rank, and then find the invariant factors to obtain the normal form. There is the conclusion:

Theorem: Let $A(\lambda)$ be equivalent to the diagonal matrix:

$$
\operatorname{diag}\{f_1(\lambda),f_2(\lambda),\cdots,f_r(\lambda),0,\cdots,0\}
$$

then all the powers of first-degree factors ${(\lambda-\lambda_j)}^{e_{ij}}$ of $f_1(\lambda),f_2(\lambda),\cdots,f_r(\lambda)$ constitute the elementary divisors of $A(\lambda)$.

The specific method of constructing the invariant factors from the elementary divisors and rank is: first classify the elementary divisors by factor, arrange them into a table, place factors of the same class in the same row arranged in descending power, place the highest power of each class of factor in a column, pad the number of columns with $1$s up to the rank $r$, and then the product of each column constitutes an invariant factor.

### Application in the characteristic matrix

If $A$ and $B$ are numeric matrices, then their characteristic matrices are $\lambda$ matrices. There is the conclusion:

Theorem: The condition that the numeric matrices $A$ and $B$ are similar is equivalent to the condition that the characteristic matrices $\lambda I-A$ and $\lambda I-B$ are equivalent.

Since the characteristic matrix $\lambda I-A$ contains $n$ $\lambda$s only on the main diagonal, its rank is $n$. By the above reasoning, the ranks of the characteristic matrices of same-type numeric matrices are always equal, so we have the equivalence:

The numeric matrices $A$ and $B$ are similar, equivalent to the characteristic matrices $\lambda I-A$ and $\lambda I-B$ having exactly the same elementary divisors.

For the characteristic matrix $\lambda I-A$, elementary transformations preserve equivalence, so they do not change the rank.

Observing the three kinds of elementary transformations, since the only rewritten addition transformation does not change the determinant, in fact all three kinds of elementary transformations only change the determinant's resulting polynomial by a constant multiple, so they do not change the factorization and degree of the determinant's resulting polynomial.

Therefore the determinant of the characteristic matrix $\lambda I-A$ is an $n$-th degree polynomial; after elementary transformation into Smith normal form, since the rank is $n$, the determinant is the product of all the invariant factors on the main diagonal, which also equals the product of all the elementary divisors. Therefore, the sum of the degrees of all the elementary divisors of the characteristic matrix $\lambda I-A$ equals $n$.

## Jordan canonical form

The matrix

$$
\begin{pmatrix}
\lambda & 1 & 0 & \cdots & 0 & 0\\
0 & \lambda & 1 & \cdots & 0 & 0\\
0 & 0 & \lambda & \cdots & 0 & 0\\
\vdots & \vdots & \vdots &  & \vdots & \vdots\\
0 & 0 & 0 & \cdots & \lambda & 1\\
0 & 0 & 0 & \cdots & 0 & \lambda\\
\end{pmatrix}
$$

whose main-diagonal elements are all $\lambda$, whose elements just above the main diagonal are all $1$, and whose other positions are all $0$, is called a Jordan matrix belonging to $\lambda$, or a Jordan block.

Obviously, a nilpotent Jordan matrix is a special case of a Jordan matrix, namely the case where $\lambda$ is $0$.

Theorem: Let $T$ be a transformation of the $n$-dimensional space $V$, and $\lambda_1,\cdots,\lambda_k$ be all the mutually distinct eigenvalues of $T$; then there exists a basis such that the matrix of $T$ with respect to this basis has the shape:

$$
\begin{pmatrix}
B_1 &  &  & 0\\
 & B_2 &  & \\
 &  & \ddots & \\
0 &  &  & B_k\\
\end{pmatrix}
$$

where

$$
B_i=\begin{pmatrix}
J_{i1} &  &  & 0\\
 & J_{i2} &  & \\
 &  & \ddots & \\
0 &  &  & J_{is_i}\\
\end{pmatrix}
$$

where $J_{i1},\cdots,J_{is_i}$ are all Jordan blocks belonging to $\lambda_i$.

This is because, first, according to the minimal polynomial:

$$
m_A(\lambda)={(\lambda-\lambda_1)}^{r_1}{(\lambda-\lambda_2)}^{r_2}\cdots{(\lambda-\lambda_k)}^{r_k}
$$

there is the primary decomposition:

$$
V=V_1\oplus V_2\oplus\cdots\oplus V_k
$$

where:

$$
V_i=N\left({(A-\lambda_i I)}^{r_i}\right)
$$

and $A$ is the matrix corresponding to $T$.

Let the transformation $S_i$ be the restriction ${T|}_{V_i}$ of $T$ to $V_i$; next we attempt to perform the Jordan decomposition on each $S_i$.

Denote by $T_e$ the identity transformation on $V$. Unlike the earlier Jordan decomposition, denote by $T_i$ the nilpotent part in the Jordan decomposition of $S_i$:

$$
S_i=\lambda_i T_e+T_i
$$

Then $T_i$ is a nilpotent transformation of the subspace $V_i$, and is in fact also the restriction ${(T-\lambda_i T_e)|}_{V_i}$ of $T-\lambda_i T_e$ to $V_i$.

The subspace $V_i$ can be decomposed into a direct sum of cyclic subspaces of the nilpotent transformation $T_i$:

$$
V_i=W_{i1}\oplus W_{i2}\oplus\cdots\oplus W_{is_i}
$$

In each cyclic subspace $W_{ij}$, take a cyclic basis and arrange it in reverse order, making up a basis of $V_i$; then the matrix of $T_i$ with respect to this basis has the shape:

$$
N_i=\begin{pmatrix}
N_{i1} &  &  & 0\\
 & N_{i2} &  & \\
 &  & \ddots & \\
0 &  &  & N_{is_i}\\
\end{pmatrix}
$$

All $N_{ij}$ are nilpotent Jordan blocks. Then for the above chosen basis of $V_i$, the matrix corresponding to $S_i$ is:

$$
B_i=\begin{pmatrix}
\lambda_i &  &  & 0\\
 & \lambda_i &  & \\
 &  & \ddots & \\
0 &  &  & \lambda_i\\
\end{pmatrix}+\begin{pmatrix}
N_{i1} &  &  & 0\\
 & N_{i2} &  & \\
 &  & \ddots & \\
0 &  &  & N_{is_i}\\
\end{pmatrix}=\begin{pmatrix}
J_{i1} &  &  & 0\\
 & J_{i2} &  & \\
 &  & \ddots & \\
0 &  &  & J_{is_i}\\
\end{pmatrix}
$$

here $J_{i1},J_{i2},\cdots,J_{is_i}$ are all Jordan blocks belonging to $\lambda_i$.

For each subspace $V_i$, choosing a basis in the above way, and making them up into a basis of $V$, then the matrix of $T$ with respect to this basis constitutes the form prescribed by the theorem.

An $n$-th order matrix of the form:

$$
\begin{pmatrix}
J_1 &  &  & 0\\
 & J_2 &  & \\
 &  & \ddots & \\
0 &  &  & J_m\\
\end{pmatrix}
$$

where each $J_i$ is a Jordan block, is called a Jordan canonical form.

Theorem: Every $n$-th order matrix $A$ is similar to a Jordan canonical form. Except for the ordering of the various Jordan blocks, the Jordan canonical form similar to $A$ is uniquely determined by $A$.

Note that in the matrix $B_i$ constructed above, the first term is a multiple of an identity matrix and can naturally commute with the second term. Therefore, the first term is the diagonalizable part of the Jordan decomposition of $B_i$, and the second term is the nilpotent part of the Jordan decomposition of $B_i$.

In the Jordan canonical form corresponding to a matrix, the diagonal matrix formed by the main-diagonal elements is the diagonalizable part of the Jordan canonical form corresponding to this matrix, and replacing the main-diagonal elements with $0$ gives the nilpotent part of the Jordan canonical form corresponding to this matrix.

Theorem: For the Jordan canonical form of a matrix $A$, each Jordan block:

$$
J_i=\begin{pmatrix}
\lambda_i & 1 &  &  & \\
 & \lambda_i & 1 &  & \\
 &  & \ddots & \ddots & \\
 &  &  & \ddots & 1\\
 &  &  &  & \lambda_i\\
\end{pmatrix}
$$

corresponds to an elementary divisor ${(\lambda-\lambda_i)}^{n_i}$ of the characteristic matrix $\lambda I-A$, and all the elementary divisors of the characteristic matrix $\lambda I-A$ correspond to all the Jordan blocks in the Jordan canonical form of the matrix $A$.

This is because the matrix $A$ is similar to its Jordan canonical form, so their characteristic matrices are also equivalent, which can be seen by transforming the characteristic matrix of the Jordan canonical form into Smith normal form.

By this theorem, with the help of the elementary divisors of the characteristic matrix $\lambda I-A$, one can write out the Jordan canonical form of the matrix $A$.

A corollary is that the matrix $A$ being diagonalizable is equivalent to all the elementary divisors of the characteristic matrix $\lambda I-A$ being of first degree.

## Frobenius theorem

The above pointed out that the rank of the Smith normal form of an $n$-th order characteristic matrix is $n$.

Theorem: Let the Smith normal form of the characteristic matrix $\lambda I-A$ of a matrix $A$ be:

$$
\operatorname{diag}\{d_1(\lambda),d_2(\lambda),\cdots,d_n(\lambda)\}
$$

then the last invariant factor $d_n(\lambda)$ is exactly the minimal polynomial $m_A(\lambda)$ of the matrix $A$.

Corollary: The equivalent conditions for a matrix $A$ to be diagonalizable are:

-   The minimal polynomial $m_A(\lambda)$ has no repeated roots.
-   The invariant factors of the characteristic matrix $\lambda I-A$ have no repeated roots.
-   All the elementary divisors of the characteristic matrix $\lambda I-A$ are of first degree.
