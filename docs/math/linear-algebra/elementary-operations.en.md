## Elementary matrices

The following three classes of square matrices are called elementary matrices.

### Scaling matrix

A scaling matrix is a special diagonal matrix.

$$
D_i(k)=\operatorname{diag}\{1,\cdots,1,k,1,\cdots,1\}
$$

denotes a diagonal matrix in which the $i$-th element on the main diagonal is $k$, and it is stipulated that $k$ cannot be $0$, with all the other elements being $1$.

In particular, when $k$ is $1$, $D_i(1)$ is the identity matrix $I$.

### Swap matrix

A swap matrix is a special symmetric matrix.

$$
P_{ij}=\begin{pmatrix}
I_{i-1} &  &  &  & \\
 & 0 &  & 1 & \\
 &  & I_{j-i-1} &  & \\
 & 1 &  & 0 & \\
 &  &  &  & I_{n-j}\\
\end{pmatrix}
$$

The elements of a swap matrix are all $1$ and $0$; the remaining elements on the main diagonal are all $1$, only the $i$-th element and the $j$-th element are $0$, while the two elements at row $i$ column $j$ and at row $j$ column $i$ are $1$.

A swap matrix requires that $i$ and $j$ cannot be equal.

### Addition matrix

An addition matrix sets, on the basis of the identity matrix $I$, the element at row $i$ column $j$ to $k$.

$$
T_{ij}(k)=\begin{pmatrix}
1 &  &  &  &  &  & \\
 & \ddots &  &  &  &  & \\
 &  & 1 & \cdots & k &  & \\
 &  &  & \ddots & \vdots &  & \\
 &  &  &  & 1 &  & \\
 &  &  &  &  & \ddots & \\
 &  &  &  &  &  & 1\\
\end{pmatrix}
$$

An addition matrix requires that $i$ and $j$ cannot be equal. If $k$ is $0$, then $T_{ij}(0)$ degenerates into the identity matrix $I$.

An addition matrix is a kind of upper-triangular matrix or lower-triangular matrix.

### Determinants of elementary matrices

The three kinds of elementary matrices have determinants:

$$
|D_i(k)|=k
$$

$$
|P_{ij}|=-1
$$

$$
|T_{ij}(k)|=1
$$

Since the determinant of a product of square matrices equals the product of the determinants, with the help of the equivalence of elementary transformations and matrix multiplication below, this property of elementary matrices can be used in the computation of determinants.

## Elementary transformations

Not limited to square matrices, for a general matrix $A$, one can perform elementary row transformations and elementary column transformations, collectively called elementary transformations.

Elementary row transformations, like elementary column transformations, have 3 kinds: multiplication, switching, and addition. Here we first introduce elementary row transformations:

-   Multiply the $i$-th row by a nonzero number $k$: $B\mapsto D_i(k)B$.
-   Swap rows $i$ and $j$: $B\mapsto P_{ij}B$.
-   Multiply the $j$-th row by $k$ and add to the $i$-th row: $B\mapsto T_{ij}(k)B$.

Changing the rows in the above operations to columns gives the elementary column transformations.

Among elementary transformations, switching can be realized through multiplication and addition. Obviously, addition cannot be realized through multiplication and switching. With the help of knowledge of determinants and the equivalence of elementary transformations and matrix multiplication below, one can also show that multiplication cannot be realized through addition and switching.

Therefore, compared with switching, multiplication and addition are more essential operations. The switching operation is an auxiliary operation introduced in the elimination method to guarantee the orderliness of elimination.

## Elementary transformations and matrix multiplication

One can find that all three classes of elementary matrices are the results of performing one corresponding transformation on the identity matrix $I$. In the linear transformations later, it is pointed out that there is a correspondence between linear transformations and matrices, similar to the relationship here.

Regardless of whether the matrix $A$ is square, performing an elementary row transformation on the matrix $A$ is equivalent to left-multiplying the matrix $A$ by an elementary matrix. Performing an elementary column transformation on the matrix $A$ is equivalent to right-multiplying the matrix $A$ by an elementary matrix.

### Multiplication operation

Left-multiplying by a scaling matrix $D_i(k)$ is equivalent to making the $i$-th row $k$ times. Right-multiplying by a scaling matrix $D_i(k)$ is equivalent to making the $i$-th column $k$ times.

A diagonal matrix times a diagonal matrix is still a diagonal matrix; for the multiplication of diagonal matrices, multiply the corresponding elements on the main diagonals. Since the identity matrix is a special scaling matrix, and scaling matrices require $k$ not to be $0$, one can see that as long as the elements on the main diagonal of a diagonal matrix are all nonzero, it can be split into a product of scaling matrices.

For a general diagonal matrix, regardless of whether the elements are $0$, there is a corresponding conclusion. Left-multiplying by a diagonal matrix is equivalent to making the corresponding rows some multiple of the original, with the multiple being exactly the corresponding element on the main diagonal of the diagonal matrix. Right-multiplying by a diagonal matrix performs the same operation on the corresponding columns.

Since the determinant of a scaling matrix $D_i(k)$ is $k$, after performing a multiplication operation on a row or column of a square matrix, the determinant corresponding to the square matrix becomes $k$ times the original. The determinant of a diagonal matrix is the product of the main-diagonal elements.

The multiplication of scaling matrices is commutative, and the multiplication of diagonal matrices is also commutative; when the multiplication involves only diagonal matrices, the order can be arbitrary.

The multiplication operation corresponding to the identity matrix keeps the matrix $A$ unchanged, and in actual applications such an operation is not performed.

### Switching operation

Left-multiplying by a swap matrix $P_{ij}$ is equivalent to swapping the $i$-th row and the $j$-th row. Right-multiplying by a swap matrix $P_{ij}$ is equivalent to swapping the $i$-th column and the $j$-th column.

Similar to the relationship of scaling matrices and diagonal matrices, here we introduce the concept of a permutation matrix. A permutation matrix is a square matrix in which each row and each column has exactly one $1$, with all the other positions being $0$. The identity matrix $I$ is also a special permutation matrix.

A permutation matrix is consistent with performing a permutation operation on the rows of the identity matrix $I$, and also consistent with performing a permutation operation on the columns of the identity matrix $I$. The identity matrix $I$ itself corresponds to the identity transformation.

Left-multiplying by a permutation matrix is equivalent to permuting the rows of the original matrix, and right-multiplying by a permutation matrix is equivalent to permuting the columns of the original matrix; the corresponding permutation method is consistent with performing a permutation operation on the rows or columns of the identity matrix $I$.

Permutation matrices correspond exactly to permutations, and the multiplicative group formed by permutation matrices is isomorphic to the permutation group. Since there is a theorem that, in the case where the identity transformation is regarded as a product of zero swaps, any permutation can be split into a product of swaps, any permutation matrix can also be split into a product of swap matrices.

Since the determinant of a swap matrix is $-1$, after performing a switching operation on a row or column of a square matrix, the determinant corresponding to the square matrix becomes $-1$ times the original.

The multiplication of swap matrices is not commutative, and the multiplication of permutation matrices is also not commutative.

The determinant of a permutation matrix is ${(-1)}^p$, where $p$ is the inversion number of the permutation corresponding to the permutation matrix, i.e. the number of swaps into which the permutation is split.

### Addition operation

Left-multiplying by an addition matrix $T_{ij}(k)$ is equivalent to adding $k$ times the $j$-th row to the $i$-th row. Right-multiplying by an addition matrix $T_{ij}(k)$ is equivalent to adding $k$ times the $i$-th column to the $j$-th column.

If this is hard to memorize, one can observe what operation the addition matrix $T_{ij}(k)$ performs on the identity matrix $I$; the two are corresponding: left-multiplication is an operation on rows, and right-multiplication is an operation on columns, conforming to the mnemonic "left row, right column".

Since the determinant of an addition matrix is $1$, after performing an addition operation on a square matrix, the determinant corresponding to the square matrix is unchanged.

The multiplication of addition matrices is not commutative.

The addition operation corresponding to the identity matrix keeps the matrix $A$ unchanged, and in actual applications such an operation is not performed.

#### Upper-triangular matrix

An addition matrix is a kind of upper-triangular matrix or lower-triangular matrix. Since the two kinds of matrices are symmetric about the main diagonal, here we discuss the upper-triangular matrix. In fact, in this example, one only needs to perform elementary row transformations, without column transformations.

If the main diagonal of an upper-triangular matrix is all $1$, then it can be split into a product of a sequence of addition matrices. The order of splitting is: first perform addition operations on the first row of the identity matrix $I$, then perform addition operations on the second row of the identity matrix $I$, and so on, until every row has been operated on.

Since the multiplication of addition matrices is not commutative, the order of the above operations cannot be swapped.

If the main diagonal of an upper-triangular matrix is all nonzero, then it can be split into a product of a sequence of addition matrices and scaling matrices. When operating on each row of the identity matrix $I$, one can first perform a multiplication operation on that row, with the effect of making the main-diagonal element become the specified nonzero value.

If the main diagonal of an upper-triangular matrix contains a $0$, then it cannot be split into a product of a sequence of elementary matrices.

Regardless of whether there is a $0$ on the main diagonal of an upper-triangular matrix, the determinant of an upper-triangular matrix equals the product of the main-diagonal elements, consistent with a diagonal matrix.

#### Addition operations transforming a square matrix into a diagonal matrix

Using only addition operations, one can turn any square matrix into a diagonal matrix; this example requires both elementary row transformations and elementary column transformations.

If the first row and first column of a square matrix contain a nonzero element, then one can, through addition operations, make the upper-left element nonzero, and then, with the help of elementary row transformations and elementary column transformations, make everything in the first row and first column except the upper-left element become $0$.

If the first row and first column of a square matrix are already all $0$, then one directly looks at the second row and second column.

With the help of this method, one can even stipulate that the nonzero elements of the diagonal matrix are all in the upper-left.

If the first row and first column of a square matrix are already all $0$, then one looks at whether the remaining rows and columns have a nonzero element; as long as there is a nonzero element, one can, through an addition operation, make some element in the first row and first column become nonzero, and then reduce to the initial situation, making the upper-left element nonzero.

Only when the remaining rows and columns also have no nonzero element can the upper-left element fail to become nonzero, in which case the remaining square matrix is already the zero matrix.

#### Canonical form matrix

With the help of elementary transformations, one can reduce any matrix, regardless of shape, to a canonical form matrix.

A canonical form matrix has an identity matrix $I$ as a submatrix located in the upper-left, with the rest all being $0$. The reduction method is similar to the operation of transforming a square matrix into a diagonal matrix, and requires the help of multiplication operations to make the upper-left nonzero element become $1$.

After a matrix is transformed into a canonical form matrix, the number of elements $1$ it contains is exactly the rank of the matrix.

## Invertible matrices

Let $A$ be an $n$-th order matrix. If there exists an $n$-th order matrix $B$ such that $AB=BA=I$, then $A$ is called an invertible matrix or non-singular matrix, and $B$ is called the inverse matrix of $A$, denoted $A^{-1}$.

If a matrix $A$ is invertible, then the inverse matrix of $A$ is uniquely determined by $A$.

The inverse $A^{-1}$ of an invertible matrix $A$ is also invertible, and the inverse of $A^{-1}$ is $A$.

The product $AB$ of two invertible matrices $A$ and $B$ is also invertible, and the inverse is $B^{-1}A^{-1}$.

The transpose $A^T$ of an invertible matrix $A$ is also invertible, and the inverse of the transpose equals the transpose of the inverse.

### Inverses of elementary matrices

Elementary matrices are all invertible, and the inverse is an elementary matrix of the same class:

$$
{D_i(k)}^{-1}=D_i\left(\frac{1}{k}\right)
$$

$$
P_{ij}^{-1}=P_{ij}
$$

$$
T_{ij}(k)^{-1}=T_{ij}(-k)
$$

Obviously the identity matrix $I$ is invertible, with inverse matrix still $I$.

Elementary transformations preserve the invertibility of a matrix; before and after the transformation the matrices are either both invertible or both non-invertible.

A matrix $A$ is invertible if and only if the matrix $A$ can be written as a product of elementary matrices, i.e. can be transformed into the identity matrix $I$ through elementary transformations.

After determinants are introduced, one can know:

A matrix $A$ is invertible if and only if the rank of the matrix $A$ is $n$, if and only if the determinant of the matrix $A$ is nonzero.

A simple notation is: denote by $E_{ij}$ the $n\times n$ matrix whose element at row $i$ column $j$ is $1$ and the rest are zero; then

-   $D_i(k)=I_n+(k-1)E_{ii}$
-   $P_{ij}=I_n-E_{ii}-E_{jj}+E_{ij}+E_{ji}$
-   $T_{ij}(k)=I_n+kE_{ij}$

This notation can also be applied to their inverse matrices.

## Applications

### Solving systems of linear equations

For a system of linear equations, the coefficients in front of the unknowns form the coefficient matrix; if one appends the constant terms of the system of linear equations to the right end of the coefficient matrix, one forms the augmented matrix.

Applying elementary row transformations, one can first transform the augmented matrix corresponding to the system of linear equations into a row echelon form matrix, then into a reduced row echelon form matrix, and then complete the solution of the system of linear equations. This method is called solving a system of linear equations by the elimination method; the Gauss–Jordan elimination later is an elimination algorithm performed in a certain order.

### Determinant computation

Since the determinant of a product of square matrices equals the product of the determinants of the square matrices, the determinants of elementary matrices are easy to compute, and elementary transformations are equivalent to the multiplication of elementary matrices, elementary transformations are also used in determinant computation.

Since performing elementary transformations in a certain order is more convenient for writing programs, determinant computation can also use the Gauss–Jordan elimination algorithm later.
