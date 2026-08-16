This article introduces a very important topic in linear algebra—the matrix—mainly explaining the properties and operations of matrices, as well as some applications of matrix multiplication.

## Vectors and matrices

In linear algebra, vectors are divided into column vectors and row vectors.

???+ warning "Warning"
    In the Taiwan region of China, the translations of "列" and "行" happen to be the opposite of those in the mainland region of China. In **OI Wiki**, following the convention of the mainland region of China, we adopt the translation column (列) and row (行).

The main object of study in linear algebra is the column vector, and by convention bold lowercase letters are used to denote column vectors. In linear algebra that uses a large number of vectors and matrices, when no confusion arises, the vector notation above the letters can be omitted when writing by hand.

A vector is also a special matrix. To denote a row vector, one needs to write a transpose sign at the upper-right of the bold lowercase letter. In linear algebra a row vector generally represents an equation.

## Introduction

The introduction of matrices comes from systems of linear equations. Similar to vectors, matrices embody the idea of "packaged processing" of data.

For example, take the system of linear equations:

$$
\begin{equation}
    \begin{cases}
        7x_1+8x_2+9x_3=13 \\
        4x_1+5x_2+6x_3=12 \\
        x_1+2x_2+3x_3=11
    \end{cases}
\end{equation}
$$

Matrices are generally denoted by parentheses or square brackets. Extracting the above coefficients and writing them in the form of matrix multiplication:

$$
\begin{equation}
    \begin{pmatrix}
        7 & 8 & 9 \\
        4 & 5 & 6 \\
        1 & 2 & 3
    \end{pmatrix}\begin{pmatrix}
        x_1 \\ x_2 \\ x_3
    \end{pmatrix}=\begin{pmatrix}
      13 \\ 12 \\ 11
    \end{pmatrix}
\end{equation}
$$

abbreviated as:

$$
Ax=b
$$

That is, the unknown column vector $x$, left-multiplied by a matrix $A$, gives the column vector $b$. This expression can be regarded as the basic form of linear algebra.

The main operation model studied in linear algebra is the inner product. The inner product is "multiply first, then add", the process of left-multiplying a column vector by a row vector to obtain a number.

Matrix multiplication is an extension of the inner product. Matrix multiplication is equivalent to taking a row from the left matrix and a column from the right matrix and taking their inner product, obtaining the corresponding element of the result matrix, with the mnemonic "left row, right column".

When the object of study is the column vector on the right, matrix multiplication amounts to left-multiplying the column vector. From the left-multiplication viewpoint, a matrix is a transformation of column vectors, transforming each column vector of the right matrix in the matrix multiplication and correspondingly obtaining each column vector in the result matrix.

A matrix can transform a single column vector, can "packagedly" transform a group of column vectors, and can even transform the entire space—i.e. all column vectors. When a matrix is regarded as a transformation of the entire space, it detaches from the space and becomes a pure transformation.

## Definition

For a matrix $A$, the main diagonal refers to the elements $A_{i,i}$.

The identity matrix is generally denoted by $I$, which has $1$ on the main diagonal and $0$ everywhere else.

### Matrices of the same type

Two matrices whose numbers of rows and columns are correspondingly the same are called matrices of the same type.

### Square matrix

A matrix whose number of rows equals its number of columns is called a square matrix. A square matrix is a special kind of matrix. The conventional phrase "$n$-th order matrix" actually refers to an $n$-th order square matrix. Square matrices of the same order are matrices of the same type.

When studying systems of equations, vector groups, and the rank of a matrix, we use general matrices. When studying eigenvalues and eigenvectors and quadratic forms, we use square matrices.

#### Main diagonal

The elements in a square matrix whose row number equals their column number form the main diagonal.

#### Symmetric matrix

If the elements of a square matrix are symmetric about the main diagonal, i.e. for any $i$ and $j$, the element at row $i$ column $j$ equals the element at row $j$ column $i$, then the square matrix is called a symmetric matrix.

#### Diagonal matrix

A square matrix in which all the elements outside the main diagonal are $0$ is called a diagonal matrix, generally denoted:

$$
\operatorname{diag}\{\lambda_1,\cdots,\lambda_n\}
$$

where $\lambda_1,\cdots,\lambda_n$ are the elements on the main diagonal.

A diagonal matrix is a symmetric matrix.

If the elements of a diagonal matrix are all $1$, it is called the identity matrix, denoted $I$. As long as the multiplication can be performed, regardless of shape, any matrix times the identity matrix remains unchanged.

#### Triangular matrix

If all the elements below and to the left of the main diagonal of a square matrix are $0$, it is called an upper-triangular matrix. If all the elements above and to the right of the main diagonal of a square matrix are $0$, it is called a lower-triangular matrix.

The product of two upper- (lower-) triangular matrices is still an upper- (lower-) triangular matrix. If the diagonal elements are all nonzero, then the upper- (lower-) triangular matrix is invertible, and the inverse is also an upper- (lower-) triangular matrix.

#### Unit triangular matrix

If the diagonal of an upper-triangular matrix $A$ is all $1$, then $A$ is called a unit upper-triangular matrix. If the diagonal of a lower-triangular matrix $A$ is all $1$, then $A$ is called a unit lower-triangular matrix.

The product of two unit upper- (lower-) triangular matrices is still a unit upper- (lower-) triangular matrix, and the inverse of a unit upper- (lower-) triangular matrix is also a unit upper- (lower-) triangular matrix.

## Operations

### Linear operations of matrices

The linear operations of matrices are divided into addition/subtraction and scalar multiplication, both performed element by element. Only matrices of the same type can be added and subtracted correspondingly.

### Matrix transpose

The transpose of a matrix writes a transpose "T" sign at the upper-right of the matrix, denoting swapping the rows and columns of the matrix.

A symmetric matrix remains unchanged before and after transposing.

### Matrix multiplication

Matrix multiplication is a generalization of the inner product of vectors.

Matrix multiplication is only meaningful when the number of columns of the first matrix equals the number of rows of the second matrix.

Let $A$ be a $P \times M$ matrix and $B$ be an $M \times Q$ matrix; let the matrix $C$ be the product of matrices $A$ and $B$,

where the element at row $i$ column $j$ of the matrix $C$ can be expressed as:

$$
C_{i,j} = \sum_{k=1}^MA_{i,k}B_{k,j}
$$

In matrix multiplication, the number at row $i$ column $j$ of the result matrix $C$ is obtained by **multiplying then adding** the $M$ numbers in row $i$ of the matrix $A$ with the $M$ numbers in column $j$ of the matrix $B$ respectively. The **multiplying then adding** here is precisely the inner product of vectors. The number at row $i$ column $j$ of the product matrix is exactly the inner product of the $i$-th row vector of the multiplier matrix $A$ and the $j$-th column vector of the multiplier matrix $B$, with the mnemonic **left row, right column**.

The vectors studied in linear algebra are mostly column vectors; according to this way of defining matrix multiplication, one often studies the left-multiplication operation of left-multiplying a column vector by a matrix, and one can also see here the idea of "packaged processing", handling many vector inner products at once.

Matrix multiplication satisfies associativity but does not satisfy general commutativity.

Using associativity, matrix multiplication can be optimized using the idea of [fast exponentiation](../binary-exponentiation.md).

In competitions, since a linear recurrence can be represented in the form of matrix multiplication, matrix fast exponentiation is also usually used to find a certain term of a linear recurrent sequence.

#### Optimization

First, for relatively small matrices, one can consider directly unrolling the loops manually to reduce the constant.

One can rearrange the loops to improve spatial locality; such an optimization does not change the time complexity of matrix multiplication, but yields a constant-level improvement.

```cpp
// Take the reference code below as an example
mat operator*(const mat& T) const {
  mat res;
  for (int i = 0; i < sz; ++i)
    for (int j = 0; j < sz; ++j)
      for (int k = 0; k < sz; ++k) {
        res.a[i][j] += mul(a[i][k], T.a[k][j]);
        res.a[i][j] %= MOD;
      }
  return res;
}

// is not as good as
mat operator*(const mat& T) const {
  mat res;
  int r;
  for (int i = 0; i < sz; ++i)
    for (int k = 0; k < sz; ++k) {
      r = a[i][k];
      for (int j = 0; j < sz; ++j)
        res.a[i][j] += T.a[k][j] * r, res.a[i][j] %= MOD;
    }
  return res;
}
```

### Inverse of a square matrix

The inverse matrix $P$ of a square matrix $A$ is the matrix such that $A \times P = I$.

The inverse matrix does not necessarily exist. If it exists, it can be solved using [Gaussian elimination](../numerical/gauss.md).

### Determinant of a square matrix

The determinant is an operation on square matrices.

## Reference code

In general, one can use a two-dimensional array to simulate a matrix.

```cpp
struct mat {
  LL a[sz][sz];

  mat() { memset(a, 0, sizeof a); }

  mat operator-(const mat& T) const {
    mat res;
    for (int i = 0; i < sz; ++i)
      for (int j = 0; j < sz; ++j) {
        res.a[i][j] = (a[i][j] - T.a[i][j]) % MOD;
      }
    return res;
  }

  mat operator+(const mat& T) const {
    mat res;
    for (int i = 0; i < sz; ++i)
      for (int j = 0; j < sz; ++j) {
        res.a[i][j] = (a[i][j] + T.a[i][j]) % MOD;
      }
    return res;
  }

  mat operator*(const mat& T) const {
    mat res;
    int r;
    for (int i = 0; i < sz; ++i)
      for (int k = 0; k < sz; ++k) {
        r = a[i][k];
        for (int j = 0; j < sz; ++j)
          res.a[i][j] += T.a[k][j] * r, res.a[i][j] %= MOD;
      }
    return res;
  }

  mat operator^(LL x) const {
    mat res, bas;
    for (int i = 0; i < sz; ++i) res.a[i][i] = 1;
    for (int i = 0; i < sz; ++i)
      for (int j = 0; j < sz; ++j) bas.a[i][j] = a[i][j] % MOD;
    while (x) {
      if (x & 1) res = res * bas;
      bas = bas * bas;
      x >>= 1;
    }
    return res;
  }
};
```

## Two viewpoints for looking at a system of linear equations

There are two viewpoints for looking at a matrix $A$, or a transformation $A$.

The first viewpoint: look by rows, observing each row of $A$. In this way one regards $A$ as a system of equations. Then one obtains the process of solving equations by the elimination method.

The second viewpoint: look by columns, observing each column of $A$. $A$ itself is also composed of column vectors. In this case one amounts to regarding the transformation $A$ itself as a group of column vectors, with $x$ as the coefficients of the unknowns, considering whether this group of column vectors in $A$ can be matched with unknowns to make up the column vector $b$.

For example, the example at the beginning of the article becomes:

$$
\begin{equation}
    \begin{pmatrix}
        7 \\ 4 \\ 1
    \end{pmatrix}x_1+\begin{pmatrix}
        8 \\ 5 \\ 2
    \end{pmatrix}x_2+\begin{pmatrix}
        9 \\ 6 \\ 3
    \end{pmatrix}x_3=\begin{pmatrix}
      13 \\ 12 \\ 11
    \end{pmatrix}
\end{equation}
$$

Solving the equation becomes studying whether one can, by adjusting the three coefficients $x$, make the given three basis vectors make up the result vector.

Looking by columns is more novel than looking by rows. From the look-by-columns viewpoint, one can study linear independence and linear dependence.

## Applications of matrix multiplication

### Matrix-accelerated recurrence

Take the [Fibonacci sequence](../combinatorics/fibonacci.md) as an example. In the Fibonacci sequence, $F_1 = F_2 = 1$, $F_i = F_{i - 1} + F_{i - 2}(i \geq 3)$.

If a problem asks you to find the value of the $n$-th term of the Fibonacci sequence, the simplest method is nothing but directly recursing. But if the range of $n$ reaches the level of $10^{18}$, recursion is no longer feasible, and in this case we can consider matrix-accelerated recurrence.

According to the [matrix form of the recurrence](../combinatorics/fibonacci.md#matrix-form) of the Fibonacci sequence:

$$
\begin{bmatrix}
  F_{n-1} & F_{n-2}
\end{bmatrix} \begin{bmatrix}
  1 & 1 \\
  1 & 0
\end{bmatrix} = \begin{bmatrix}
  F_n & F_{n-1}
\end{bmatrix}
$$

Define the initial matrix $\text{ans} = \begin{bmatrix}F_2 & F_1\end{bmatrix} = \begin{bmatrix}1 & 1\end{bmatrix}, \text{base} = \begin{bmatrix} 1 & 1 \\ 1 & 0 \end{bmatrix}$. Then $F_n$ equals the element at row 1 column 1 of the matrix $\text{ans} \text{base}^{n-2}$, i.e. the element at row 1 column 1 of $\begin{bmatrix}1 & 1\end{bmatrix} \begin{bmatrix} 1 & 1 \\ 1 & 0 \end{bmatrix}^{n-2}$.

???+ warning "Note"
    Matrix multiplication does not satisfy commutativity, so it must never be written as the element at row 1 column 1 of $\begin{bmatrix} 1 & 1 \\ 1 & 0 \end{bmatrix}^{n-2} \begin{bmatrix}1 & 1\end{bmatrix}$. In addition, for the case $n \leq 2$, one can directly output $1$ without executing matrix fast exponentiation.

Why multiply by the $n-2$-th power of the $\text{base}$ matrix rather than the $n$-th power? Because $F_1, F_2$ can be found without matrix multiplication. That is, after just one multiplication, $F_3$ is already found. If you still do not quite understand why the power is $n-2$, it is recommended to compute it by hand.

Below is example code (core part) for finding the $n$-th term of the Fibonacci sequence modulo $10^9+7$.

```cpp
constexpr int mod = 1000000007;

struct Matrix {
  int a[3][3];

  Matrix() { memset(a, 0, sizeof a); }

  Matrix operator*(const Matrix &b) const {
    Matrix res;
    for (int i = 1; i <= 2; ++i)
      for (int j = 1; j <= 2; ++j)
        for (int k = 1; k <= 2; ++k)
          res.a[i][j] = (res.a[i][j] + a[i][k] * b.a[k][j]) % mod;
    return res;
  }
} ans, base;

void init() {
  base.a[1][1] = base.a[1][2] = base.a[2][1] = 1;
  ans.a[1][1] = ans.a[1][2] = 1;
}

void qpow(int b) {
  while (b) {
    if (b & 1) ans = ans * base;
    base = base * base;
    b >>= 1;
  }
}

int main() {
  int n = read();
  if (n <= 2) return puts("1"), 0;
  init();
  qpow(n - 2);
  println(ans.a[1][1] % mod);
}
```

This is a slightly more complex example.

$$
\begin{gathered}
f_{1} = f_{2} = 0\\
f_{n} = 7f_{n-1}+6f_{n-2}+5n+4\times 3^n
\end{gathered}
$$

We find that $f_n$ is related to $f_{n-1}, f_{n-2}, n$, so we consider constructing a matrix to describe the state.

But we find that if the matrix has only these three elements $\begin{bmatrix}f_n& f_{n-1}& n\end{bmatrix}$, it is difficult to construct the transition equation, because the exponentiation and the $+1$ cannot be described by a matrix.

So we consider constructing a larger matrix.

$$
\begin{bmatrix}f_n& f_{n-1}& n& 3^n & 1\end{bmatrix}
$$

We hope to construct a recurrence matrix that can transition to

$$
\begin{bmatrix}
f_{n+1}& f_{n}& n+1& 3^{n+1} & 1
\end{bmatrix}
$$

The transition matrix is

$$
\begin{bmatrix}
7 & 1 & 0 & 0 & 0\\
6 & 0 & 0 & 0 & 0\\
5 & 0 & 1 & 0 & 0\\
12 & 0 & 0 & 3 & 0\\
5 & 0 & 1 & 0 & 1
\end{bmatrix}
$$

### Matrix representation of modifications

???+ note "[「THUSCH 2017」大魔法师](https://loj.ac/p/2980)"
    The great magician Little L made $n$ magic crystal balls, each of which has energy values of three attributes: water, fire, earth. Little L arranged these $n$ crystal balls in a row on the ground from front to back, and then began today's magic performance.
    
    We use $A_i,\ B_i,\ C_i$ to denote the water, fire, earth energy values of the $i$-th crystal ball from front to back (indexed from $1$).
    
    Little L plans to cast $m$ spells. Each time, he chooses an interval $[l, r]$, and then casts one of the following $3$ major categories, $7$ kinds of spell:
    
    1.  Magic excitation: cause the energy of a **specific attribute** in each crystal ball in the interval to erupt, thereby strengthening the energy of another **specific attribute**. Specifically, there are the following three possible manifestations:
    
        -   Fire element excites water element energy: let $A_i = A_i + B_i$.
        -   Earth element excites fire element energy: let $B_i = B_i + C_i$.
        -   Water element excites earth element energy: let $C_i = C_i + A_i$.
    
            **Note that strengthening the energy of one attribute does not change the energy of another attribute; for example, $A_i = A_i + B_i$ does not increase or decrease $B_i$.**
    2.  Magic enhancement: Little L waves his staff, consuming $v$ points of his own mana, to change the energy of a **specific attribute** of each crystal ball in the interval. Specifically, there are the following three possible manifestations:
    
        -   Fire element energy fixed-value enhancement: let $A_i = A_i + v$.
        -   Water element energy doubling enhancement: let $B_i=B_i \cdot v$.
        -   Earth element energy absorption and fusion: let $C_i = v$.
    3.  Magic release: Little L gathers the energy of all crystal balls in the interval together, fuses them into a new crystal ball, and then gives it to the offstage audience. Each attribute's energy value of the generated crystal ball equals the algebraic sum of the corresponding energy values of all crystal balls in the interval. **Note that the process of magic release does not actually change the energy of the crystal balls in the interval.**
    
    It is worth mentioning that the raw materials of the crystal balls Little L makes and fuses are all customized OI Factory crystals, so these crystal balls have an energy threshold $998244353$. When the energy value of some attribute in a crystal ball is greater than or equal to this threshold, the energy value automatically takes the modulus by the threshold, thereby avoiding the crystal ball exploding.
    
    Little W, as Little L's (only) audience, watched the entire performance and received each crystal ball Little L fused during the performance. Little W wants to know what the energy values of the three attributes contained in these crystal balls are respectively.

Since the associativity and distributivity of matrices hold, single-point modifications can naturally be generalized to intervals, i.e. after deriving the matrices, one directly uses a segment tree to maintain the interval matrix products.

Below we give a few examples.

Transition of $A_i = A_i + v$

$$
\begin{bmatrix}
A & B & C & 1
\end{bmatrix}
\begin{bmatrix}
1 & 0 & 0 & 0\\
0 & 1 & 0 & 0\\
0 & 0 & 1 & 0\\
v & 0 & 0 & 1\\
\end{bmatrix}=
\begin{bmatrix}
A+v & B & C & 1\\
\end{bmatrix}
$$

Transition of $B_i=B_i \cdot v$

$$
\begin{bmatrix}
A & B & C & 1
\end{bmatrix}
\begin{bmatrix}
1 & 0 & 0 & 0\\
0 & v & 0 & 0\\
0 & 0 & 1 & 0\\
0 & 0 & 0 & 1\\
\end{bmatrix}=
\begin{bmatrix}
A & B \cdot v & C & 1\\
\end{bmatrix}
$$

???+ note "[「LibreOJ 6208」树上询问](https://loj.ac/p/6208)"
    There is a tree with $n$ nodes, rooted at node $1$. Each node has two weights $k_i, t_i$, both with initial value $0$.
    
    Three kinds of operations are given:
    
    1.  $\operatorname{Add}( x , d )$ operation: for all nodes on the path from $x$ to the root, $k_i\leftarrow k_i + d$
    2.  $\operatorname{Mul}( x , d )$ operation: for all nodes on the path from $x$ to the root, $t_i\leftarrow t_i + d \times k_i$
    3.  $\operatorname{Query}( x )$ operation: query the weight $t_x$ of node $x$
    
        $n,~m \leq 100000, ~-10 \leq d \leq 10$

If one thinks directly, the push-down operations and the maintenance of information are not very easy to think of. But a matrix can express them easily.

$$
\begin{aligned}
\begin{bmatrix}k & t & 1 \end{bmatrix}
\begin{bmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
d & 0 & 1
\end{bmatrix}
&=
\begin{bmatrix}k+d & t & 1 \end{bmatrix}\\
\begin{bmatrix}k & t & 1 \end{bmatrix}
\begin{bmatrix}
1 & d & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{bmatrix}
&=
\begin{bmatrix}k & t+d \times k & 1 \end{bmatrix}
\end{aligned}
$$

### Fixed-length path counting

???+ note "Problem statement"
    Given an $n$-th order directed graph where every edge has edge weight $1$, and an integer $k$, your task is to find, for all pairs of points $(u,v)$, the number of paths of length $k$ from $u$ to $v$ (not necessarily simple paths, i.e. the points or edges on the path may be traversed multiple times).

We represent this directed graph with the adjacency matrix $G$ (for an edge $(u\to v)$ in the graph, let $G[u,v]=1$, with the rest of the matrix being $0$; if there are multiple edges, then set $G[u,v]$ to the number of multiple edges). The following algorithm also applies to the case where the graph has self-loops.

Obviously, this adjacency matrix corresponds to the answer when $k=1$.

Suppose we know the matrix formed by the number of paths of length $k$, denoted matrix $C_k$; we want to find $C_{k+1}$. Obviously there is the DP transition equation

$$
C_{k+1}[i,j] = \sum_{p = 1}^{n} C_k[i,p] \cdot G[p,j]
$$

We can regard it as a matrix multiplication operation, so the above transition can be described as

$$
C_{k+1} = C_k \cdot G
$$

Then expanding this recurrence we obtain

$$
C_k = \underbrace{G \cdot G \cdots G}_{k \text{ times}} = G^k
$$

To compute this matrix power, we can use the idea of fast exponentiation (binary exponentiation) to compute the result in $O(n^3 \log k)$ complexity.

### Fixed-length shortest path

???+ note "Problem statement"
    Given an $n$-th order weighted directed graph and an integer $k$. For each pair of points $(u,v)$ find the length of the shortest path from $u$ to $v$ containing exactly $k$ edges. (Not necessarily a simple path, i.e. the points or edges on the path may be traversed multiple times.)

We still construct the adjacency matrix $G$ of this graph, where $G[i,j]$ denotes the edge weight from $i$ to $j$. If there is no edge between points $i,j$, then $G[i,j]=\infty$. (In the case of multiple edges, take the minimum edge weight.)

Obviously the above matrix corresponds to the answer to the problem when $k=1$. We still assume we know the answer for $k$, denoted matrix $L_k$. Now we want to find the answer for $k+1$. Obviously there is the transition equation

$$
L_{k+1}[i,j] = \min_{1\le p \le n} \left\{L_k[i,p] + G[p,j]\right\}
$$

In fact we can draw an analogy with matrix multiplication; you find that the above transition simply changes the product-and-sum of matrix multiplication into addition-and-minimum, so we define this operation as $\odot$, i.e.

$$
A \odot B = C~~\Longleftrightarrow~~C[i,j]=\min_{1\le p \le n}\left\{A[i,p] + B[p,j]\right\}
$$

Thus we obtain

$$
L_{k+1} = L_k \odot G
$$

Expanding the recurrence we obtain

$$
L_k = \underbrace{G \odot \ldots \odot G}_{k\text{ times}} = G^{\odot k}
$$

We can still use the matrix fast exponentiation method to compute the above, because it obviously has associativity. The time complexity is $O(n^3 \log k)$.

### Length-bounded path counting / shortest path

The above algorithm only applies to the case where the number of edges is fixed. However, we can improve the algorithm to solve the case where the number of edges is less than or equal to $k$. Specifically, consider the following problem:

???+ note "Problem statement"
    Given an $n$-th order directed graph with edge weight $1$, and an integer $k$, your task is to find, for each pair of points $(u,v)$, the number of paths of length less than or equal to $k$ from $u$ to $v$ (not necessarily simple paths, i.e. the points or edges on the path may be traversed multiple times).

For each point $v$, we build a virtual point $v'$ to record the answer, and add the two edges $(v,v')$ and $(v',v')$ to the graph. Then for a pair of points $(u,v)$, the number of paths from $u$ to $v$ with number of edges less than or equal to $k$ equals the number of paths from $u$ to $v'$ with number of edges exactly equal to $k+1$; this is because for any path with $m$ edges $(p_0=u)\to p_1\to p_2 \to \dots \to p_{m-1} \to (p_m=v)$ ($m \le k$), there exists a path with $k+1$ edges $(p_0=u)\to p_1 \to p_2 \to \dots \to p_{m-1} \to (p_m=v) \to v'  \to \dots \to v'$ in one-to-one correspondence with it.

For finding the shortest path with number of edges less than or equal to $k$, one only needs to add a self-loop with edge weight $0$ to each point.

## Exercises

-   [Luogu P1962 斐波那契数列](https://www.luogu.com.cn/problem/P1962), i.e. the example problem above, same as POJ3070
-   [Luogu P1349 广义斐波那契数列](https://www.luogu.com.cn/problem/P1349), the $\text{base}$ matrix needs a slight change
-   [Luogu P1939 【模板】矩阵加速（数列）](https://www.luogu.com.cn/problem/P1939), the $\text{base}$ matrix becomes a $3 \times 3$ matrix, with a derivation process similar to the above.
