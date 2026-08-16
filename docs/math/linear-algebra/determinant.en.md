The determinant is an operation on square matrices. For a square matrix $A$, $\det A$ denotes the determinant of the square matrix $A$.

This article introduces three definitions of the determinant. It can be proved that the definitions in this article are equivalent.

## Definition via full permutations

Prerequisites: [permutations](../permutation.md), [inversion number](../permutation.md#逆序数).

This method can be used to manually compute determinants of lower order; its time complexity is of factorial order.

Use the notation $\pi(j_1j_2\cdots j_n)$ to denote the inversion number of the permutation $j_1j_2\cdots j_n$, and $S_n$ for the set of all permutations of length $n$. The notation:

$$
\begin{aligned}
\det A &= \begin{vmatrix}
a_{11} & a_{12} & \cdots & a_{1n}\\
a_{21} & a_{22} & \cdots & a_{2n}\\
\vdots & \vdots &  & \vdots\\
a_{n1} & a_{n2} & \cdots & a_{nn}\\
\end{vmatrix} \\
&= \sum_{(j_1j_2\cdots j_n) \in S_n} (-1)^{\pi(j_1j_2\cdots j_n)} a_{1 j_1} a_{2 j_2}\dots a_{n j_n}
\end{aligned}
$$

denotes that the $n$-th order determinant is an algebraic sum of $n!$ terms, where these terms are the products $a_{1j_1}a_{2j_2}\cdots a_{nj_n}$ of all possible $n$ elements taken from different rows and different columns of the square matrix $A$.

The sign in front of the term $a_{1j_1}a_{2j_2}\cdots a_{nj_n}$ is ${(-1)}^{\pi(j_1j_2\cdots j_n)}$, that is, when $j_1j_2\cdots j_n$ is an even permutation, the sign is positive, and when $j_1j_2\cdots j_n$ is an odd permutation, the sign is negative.

The diagonal rule for second- and third-order determinants in fact adopts the full-permutation definition. The reason the diagonal rule no longer applies to determinants of fourth order and above is the same. In particular, a first-order determinant is the element itself.

Theorem: Taking elements from rows $i_1,i_2,\cdots,i_n$ and columns $j_1,j_2,\cdots,j_n$ of an $n$-th order determinant to form the product

$$
a_{i_1j_1}a_{i_2j_2}\cdots a_{i_nj_n}
$$

here $i_1,i_2,\cdots,i_n$ and $j_1,j_2,\cdots,j_n$ are both permutations of the $n$ numbers $1,2,\cdots,n$. Then the sign of this term in the determinant is ${(-1)}^{s+t}$, where

$$
s=\pi(i_1i_2\cdots i_n)
$$

$$
t=\pi(j_1j_2\cdots j_n)
$$

Theorem: A determinant equals its transposed determinant.

Theorem: Suppose all the elements of the $i$-th row of the determinant $\det A$ can be expressed as a sum of two terms:

$$
\begin{vmatrix}
a_{11} & a_{12} & \cdots & a_{1n}\\
\vdots & \vdots &  & \vdots\\
b_{i1}+c_{i1} & b_{i2}+c_{i2} & \cdots & b_{in}+c_{in}\\
\vdots & \vdots &  & \vdots\\
a_{n1} & a_{n2} & \cdots & a_{nn}\\
\end{vmatrix}
$$

Then this determinant equals the sum of two determinants $\det A_1$ and $\det A_2$. Here the $i$-th row of $A_1$ is $b_{i1},b_{i2},\cdots,b_{in}$, the $i$-th row of $A_2$ is $c_{i1},c_{i2},\cdots,c_{in}$, and the remaining rows of $A_1$ and $A_2$ are all the same as $A$. The same property also holds for columns.

## Definition via induction

This method only describes an algebraic property of the determinant; its time complexity is also of factorial order and is not suitable for computation.

### Cofactor

In an $n$-th order determinant $\det A$, arbitrarily fix $k$ rows and $k$ columns of the matrix $A$. The $k$-th order matrix formed by the elements at the intersections of these rows and columns is called a $k$-th order submatrix, and its determinant is called a $k$-th order minor.

For an $n$-th order determinant $\det A$, the minor matrix $M_{ij}$ of some element $a_{ij}$ refers to the remaining $(n-1)$-th order submatrix of the original matrix $A$ after deleting the row and column in which $a_{ij}$ lies; its determinant $\det M_{ij}$ is called the minor.

For an $n$-th order determinant $\det A$, the minor $\det M_{ij}$ of the element $a_{ij}$, after being attached with the sign ${(-1)}^{i+j}$, is called the cofactor of the element $a_{ij}$, denoted by the symbol $A_{ij}$.

From the definition via full permutations in the previous section, one can deduce the conclusion:

Theorem: If in an $n$-th order determinant $\det A$, the elements of the $i$-th row or the $j$-th column, except $a_{ij}$, are all $0$, then this determinant equals the product of $a_{ij}$ and its cofactor $A_{ij}$.

### Determinant expansion

Since transposing a square matrix does not change the determinant, it suffices to introduce either expansion by rows or expansion by columns.

The determinant $\det A$ is defined as the sum of the products of all the elements of any one of its rows (or columns) with their corresponding cofactors.

In other words, the determinant can be recursively defined using the expansion by rows (or by columns):

$$
\begin{aligned}
\det A &= a_{i1}A_{i1}+a_{i2}A_{i2}+\cdots+a_{in}A_{in} \\
&= \sum_{j = 1}^{n} a_{ij}A_{ij} \\
&= \sum_{j = 1}^{n} (-1)^{i + j} a_{ij} \det M_{ij}
\end{aligned}
$$

$$
\begin{aligned}
\det A &= a_{1j}A_{1j}+a_{2j}A_{2j}+\cdots+a_{nj}A_{nj} \\
&= \sum_{i = 1}^{n} a_{ij}A_{ij} \\
&= \sum_{i = 1}^{n} (-1)^{i + j} a_{ij} \det M_{ij}
\end{aligned}
$$

The recursion terminates at the determinant of a first-order matrix, which is the unique element contained in that matrix.

Thus we have the conclusion:

Theorem: The sum of the products of the elements of some row (or some column) of the determinant $\det A$ with the cofactors of the corresponding elements of another row (or another column) equals $0$.

In other words, when $i\neq j$:

$$
a_{i1}A_{j1}+a_{i2}A_{j2}+\cdots+a_{in}A_{jn}=0
$$

$$
a_{1i}A_{1j}+a_{2i}A_{2j}+\cdots+a_{ni}A_{nj}=0
$$

## Axiomatic definition

The axiomatic definition says that an operation satisfying certain properties can only be the determinant.

Prerequisites: [elementary operations](./elementary-operations.md).

Denote by $D_i(k)$ the [scaling matrix](./elementary-operations.md#scaling-matrix), by $P_{ij}$ the [swap matrix](./elementary-operations.md#swap-matrix), and by $T_{ij}(k)$ the [addition matrix](./elementary-operations.md#addition-matrix).

For an operation $\det$ on an $n$-th order matrix $A$, if it satisfies the following four properties, it is called a determinant:

-   Multiplying all the elements of some row or some column of a determinant simultaneously by a number $k$ is equal to multiplying this determinant by $k$.

    $$
    \det(D_i(k)A) = \det(AD_i(k)) = k \det A
    $$

-   Swapping two rows or two columns of a determinant changes the sign of the determinant.

    $$
    \det(P_{ij}A) = \det(AP_{ij}) = -\det A
    $$

-   Multiplying the elements of some row or some column of a determinant by the same number and adding to the corresponding elements of another row or another column leaves the determinant unchanged.

    $$
    \det(T_{ij}(k)A) = \det(AT_{ij}(k))= \det A
    $$

-   The determinant of the identity matrix is $1$.

    $$
    \det I = 1
    $$

Using the properties of the determinant related to elementary transformations, one can conveniently manually compute determinants of higher order. [Computing the determinant via "Gaussian elimination"](../numerical/gauss.md#行列式计算) also uses this property, with time complexity $O(n^3)$.

The above properties also have several corollaries:

-   A common factor of some row or some column of a determinant can be pulled out of the determinant symbol.
-   If all the elements of some row or some column of a determinant are $0$, then this determinant equals $0$.
-   If a determinant has two rows or two columns whose corresponding elements are proportional, then this determinant equals $0$.
-   If a determinant has two rows or two columns that are completely identical, then this determinant equals $0$.

These corollaries are very commonly used when computing determinants by hand.
