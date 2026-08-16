This part on eigen- topics studies only square matrices, i.e. the linear transformation corresponding to a matrix $A$ maps $n$ vectors to $n$ vectors.

Since in practical problems one often needs to consider performing repeated transformations continuously, if one uses only the description "the linear transformation corresponding to the matrix $A$ transforms the identity matrix $I$ into $A$", it is very abstract. In this case the best approach is to find "fixed points", i.e. the part that does not move during the transformation.

However, in fact, the linear transformation corresponding to the matrix $A$ very likely has no fixed points, so one settles for the next best and looks for the part that is collinear or similar to a simple deformation.

## Eigenvalues and eigenvectors

Under the action of the linear transformation corresponding to the matrix $A$, the directions of some vectors do not change, only being stretched.

Let $V$ be a linear space over $F$, and $T$ be a linear transformation on $V$. If there exist $\lambda$ in $F$ and a **nonzero vector** $\xi$ in $V$ such that:

$$
T\xi=\lambda\xi
$$

then $\lambda$ is called an **eigenvalue** of $T$, and $\xi$ is called **an eigenvector of $T$ belonging to the eigenvalue $\lambda$**.

Eigenvectors are on the same line, and under the action of the linear transformation their direction does not change (compression to zero is also considered as the direction not changing). Eigenvectors are not unique; any vector collinear with an eigenvector is an eigenvector, but it is stipulated that the zero vector is not an eigenvector, and a vector with a direction is naturally a nonzero vector. The eigenvalue of an eigenvector is the factor by which it is stretched.

In practical applications, for eigenvectors having the same eigenvalue, one generally chooses a basis as the representative of all of them.

Let $\alpha_1,\alpha_2,\cdots,\alpha_n$ be a basis of $V$, and the matrix of $T$ under this basis be $A$, i.e.:

$$
T(\alpha_1,\alpha_2,\cdots,\alpha_n)=(\alpha_1,\alpha_2,\cdots,\alpha_n)A
$$

Let $\lambda_0$ be an eigenvalue of $T$, $\xi$ be an eigenvector of $T$ belonging to the eigenvalue $\lambda_0$, and let a nonzero vector $X$ satisfy:

$$
\xi=(\alpha_1,\alpha_2,\cdots,\alpha_n)X
$$

Then:

$$
T\xi=\lambda_0\xi
$$

$$
T(\alpha_1,\alpha_2,\cdots,\alpha_n)X=\lambda_0(\alpha_1,\alpha_2,\cdots,\alpha_n)X
$$

$$
(\alpha_1,\alpha_2,\cdots,\alpha_n)AX=\lambda_0(\alpha_1,\alpha_2,\cdots,\alpha_n)X
$$

$$
AX=\lambda_0X
$$

$$
(A-\lambda_0I)X=0
$$

So the corresponding determinant is also $0$.

## Characteristic polynomial

Consider an $n\times n$ matrix $A$, where $n\geq 0\land n\in\mathbb{Z}$. Let $\lambda$ be a parameter; the matrix $\lambda I-A$ is called the **characteristic matrix** of $A$.

The determinant of the characteristic matrix is called the **characteristic polynomial** of $A$, expanded as an $n$-th degree polynomial whose roots are the eigenvalues of $A$, denoted $p_A(\lambda)$:

$$
p_A(\lambda)=\det(\lambda I_n-A)=\begin{vmatrix}
\lambda-a_{11} & -a_{12} &  \cdots & -a_{1n} \\
-a_{21} & \lambda-a_{22} &  \cdots & -a_{2n} \\
\vdots & \vdots &  & \vdots  \\
-a_{n1} & -a_{n2} &  \cdots & \lambda-a_{nn} \\
\end{vmatrix}
$$

where $I_n$ is an $n\times n$ identity matrix. Some places define it as $p_A(\lambda)=\det(A-\lambda I_n)$, which differs from our definition only by a sign $(-1)^n$, but the $p_A(\lambda)$ obtained by our definition is always a monic polynomial, while the other definition is a monic polynomial only when $n$ is even. Note that the determinant of a $0\times 0$ matrix being $1$ is well-defined.

The nonzero solution vector $X$ corresponding to $(\lambda_0 I-A)X=0$ is called an eigenvector of $A$ belonging to $\lambda_0$.

The linear transformation $T$ having eigenvalue $\lambda_0$ is equivalent to the matrix $A$ having eigenvalue $\lambda_0$.

The linear transformation $T$ having eigenvector $\xi$ is equivalent to the matrix $A$ having eigenvector $X$, where:

$$
\xi=(\alpha_1,\cdots,\alpha_n)X
$$

By the fundamental theorem of algebra, the characteristic polynomial can be factored as:

$$
f(\lambda)=|\lambda I-A|={(\lambda-\lambda_1)}^{d_1}\cdots{(\lambda-\lambda_m)}^{d_m}
$$

$d_i$ is called the **algebraic multiplicity** of the eigenvalue $\lambda_i$. The sum of all algebraic multiplicities is the dimension of the space $n$.

### Finding all eigenvalues and eigenvectors of a matrix

Divided into the following steps:

-   Compute the determinant $|\lambda I-A|$.
-   Find all roots of the polynomial $f(\lambda)=|\lambda I-A|$ in the field $F$, i.e. the eigenvalues of $A$.
-   For each eigenvalue $\lambda$ of $A$, solve the homogeneous system of linear equations $(\lambda I-A)X=0$, and find a fundamental system of solutions $X_1,\cdots,X_t$; then all eigenvectors of $A$ belonging to $\lambda$ are:

$$
k_1X_1+k_2X_2+\cdots+k_tX_t
$$

where the $k_i$ in this expression are not all zero.

-   The eigenvectors of the linear transformation $T$ belonging to $\lambda$ are:

$$
\xi_i=(\alpha_1,\cdots,\alpha_n)X_i
$$

Therefore, all eigenvectors belonging to $\lambda$ are:

$$
k_1\xi_1+k_2\xi_2+\cdots+k_t\xi_t
$$

where the $k_i$ in this expression are not all zero.

Whether eigenvalues and eigenvectors exist depends on the field in which $V$ lies.

## Similarity transformation

### Introduction

If an $n\times n$ matrix $A$ is an upper-triangular matrix such as

$$
A=
\begin{bmatrix}
a_{1,1}&a_{1,2}&\cdots &a_{1,n}\\
&a_{2,2}&\cdots &a_{2,n}\\
&&\ddots &\vdots \\
&&&a_{n,n}
\end{bmatrix}
$$

then

$$
\begin{aligned}
p_A(x)&=\det(xI_n-A)\\
&=
\begin{bmatrix}
x-a_{1,1}&-a_{1,2}&\cdots &-a_{1,n}\\
&x-a_{2,2}&\cdots &-a_{2,n}\\
&&\ddots &\vdots \\
&&&x-a_{n,n}
\end{bmatrix}
\\
&=\prod_{i=1}^n(x-a_{i,i})
\end{aligned}
$$

can be easily found; the lower-triangular matrix is similar. But if $A$ does not belong to these two kinds of matrices, one needs to use a similarity transformation to turn the matrix into a form whose characteristic polynomial is easy to find.

### Definition

For $n\times n$ matrices $A$ and $B$, when there exists an $n\times n$ invertible matrix $P$ satisfying

$$
B=P^{-1}AP
$$

then the matrices $A$ and $B$ are similar, and the transformation $A\mapsto P^{-1}AP$ is called a similarity transformation. Moreover, $A$ and $P^{-1}AP$ have the same characteristic polynomial.

Consider

$$
\begin{aligned}
\det(xI_n-P^{-1}AP)&=\det(xP^{-1}I_nP-P^{-1}AP)\\
&=\det(P^{-1}xI_nP-P^{-1}AP)\\
&=\det(P^{-1})\cdot \det(P)\cdot \det(xI_n-A)\\
&=\det(xI_n-A)\\
&=p_A(x)
\end{aligned}
$$

which proves it; for $A\mapsto PAP^{-1}$ it is the same. In addition $p_A(0)=(-1)^n\cdot \det(A)$, because $p_A(0)=\det(-1\cdot I_nA)=\det(-1\cdot I_n)\cdot \det(A)$, so $\det(A)=\det(P^{-1}AP)$.

Theorem: Similar matrices have the same characteristic polynomial and eigenvalues, but not conversely.

The theorem shows that the characteristic polynomial of the matrix of a linear transformation is independent of the choice of basis, and is directly determined by the linear transformation, so it can be called the characteristic polynomial of the linear transformation.

The characteristic polynomial $f(\lambda)=|\lambda I-A|$ of a matrix $A$ is a monic polynomial. By Vieta's formulas, its $n-1$-th degree coefficient is:

$$
-(\lambda_1+\cdots+\lambda_n)=-(a_{11}+\cdots+a_{nn})=-tr A
$$

where $tr A$ is called the trace of $A$, the sum of the main-diagonal elements of $A$.

By Vieta's formulas, the constant term of the characteristic polynomial is:

$$
{(-1)}^n|A|={(-1)}^n(\lambda_1\cdots\lambda_n)
$$

Theorem: Similar matrices have the same trace.

### Commutation formula

Theorem: Regardless of whether the matrix $A$ and the matrix $B$ are square, as long as the multiplication can be performed, the trace of the matrix $AB$ equals the trace of the matrix $BA$.

One proof is direct expansion, which proves it. Another proof uses the commutation formula.

Theorem: Let $A$ be an $m$-row $n$-column matrix and $B$ be an $n$-row $m$-column matrix; then:

$$
\lambda^n|\lambda I_m-AB|=\lambda^m|\lambda I_n-BA|
$$

This formula shows that $AB$ and $BA$ have the same nonzero eigenvalues.

### Schur's lemma

Any $n$-th order matrix $A$ is similar to an upper-triangular matrix, i.e. there exists a full-rank matrix $P$ such that $P^{-1}AP$ is an upper-triangular matrix, whose main-diagonal elements are all the eigenvalues of $A$.

Corollary: Let the $n$ eigenvalues of $A$ be $\lambda_1,\cdots,\lambda_n$, and $\phi(x)$ be any polynomial; then the $n$ eigenvalues of the matrix polynomial $\phi(A)$ are:

$$
\phi(\lambda_1),\cdots,\phi(\lambda_n)
$$

In particular, the eigenvalues of $kA$ are $k\lambda_1,\cdots,k\lambda_n$, and the eigenvalues of $A^m$ are ${\lambda_1}^m,\cdots,{\lambda_n}^m$.

### Using Gaussian elimination to perform a similarity transformation

On an $n\times n$ matrix $B$ one can perform Gaussian elimination, whose basic operation is elementary row transformation.

After using the above operation on the matrix (left-multiplying by an elementary matrix) and then right-multiplying by its inverse, one gets a similarity transformation; left-multiplication is a row transformation, and it is easy to find that right-multiplication is a column transformation.

If one can turn the matrix into upper- or lower-triangular form via a similarity transformation, then one can easily find its characteristic polynomial. But if one applies the transformation $A\mapsto T_{ij}(k)AT_{ij}(-k)$ to the main-diagonal elements, then after having eliminated the element at row $i$ column $j$ to zero via $A\mapsto T_{ij}(k)A$, right-multiplying by $T_{ij}(-k)$—i.e. adding $-k$ times column $i$ of $A$ to column $j$—may cause the element that was previously eliminated to zero to now be nonzero, so one may not be able to turn it into upper- or lower-triangular form.

The following text will explain that the matrix obtained after applying transformations to the subdiagonal elements can still easily yield its characteristic polynomial.

### Upper Hessenberg matrix

For $n\gt 2$, a matrix of the form

$$
H=
\begin{bmatrix}
\alpha_{1}&h_{12}&\dots&\dots&h_{1n}\\
\beta_{2}&\alpha_{2}&h_{23}&\dots &\vdots \\
&\ddots &\ddots & \ddots &\vdots \\
& &\ddots &\ddots & h_{(n-1)n}\\
&&& \beta_{n}& \alpha_{n}
\end{bmatrix}
$$

is called an upper Hessenberg matrix, where $\beta$ is the subdiagonal.

Using a similarity transformation to eliminate the elements below the subdiagonal to zero gives an upper Hessenberg matrix, and finding the characteristic polynomial of an $n\times n$ upper Hessenberg matrix can be done in $O(n^3)$ time.

We denote by $H_i$ the matrix keeping only the first $i$ rows and first $i$ columns of $H$, and denote $p_i(x)=\det(xI_i-H_i)$; then

$$
H_0=
\begin{bmatrix}
\end{bmatrix},\quad
p_0(x)=1
$$

$$
H_1=
\begin{bmatrix}
\alpha_1
\end{bmatrix},\quad
p_1(x)=\det(x I_1-H_1)=x -\alpha_1
$$

$$
H_2=
\begin{bmatrix}
\alpha_1&h_{12}\\
\beta_2&\alpha_2
\end{bmatrix},\quad
p_2(x)=\det(xI_2-H_2)=(x-\alpha_2)p_1(x)-\beta_2h_{12}p_0(x)
$$

When computing a determinant we generally choose to expand by the cofactors of the row or column with the most zeros; the cofactor is the matrix after deleting the row and column in which the currently chosen element lies; here we choose to expand by the last row, giving

$$
\begin{aligned}
p_3(x)&=
\det(xI_3-H_3)\\
&=\begin{vmatrix}
x-\alpha_1&-h_{12}&-h_{13}\\
-\beta_2&x-\alpha_2&-h_{23}\\
&-\beta_3&x-\alpha_3
\end{vmatrix}\\
&=(x-\alpha_3)\cdot (-1)^{3+3}p_2(x)-\beta_3\cdot (-1)^{3+2}
\begin{vmatrix}
x-\alpha_1&-h_{13}\\
-\beta_2&-h_{23}
\end{vmatrix}\\
&=(x-\alpha_3)p_2(x)-\beta_3(h_{23}p_1(x)+\beta_2h_{13}p_0(x))
\end{aligned}
$$

Observing and generalizing, for $2\leq i\leq n$:

$$
p_i(x)=(x-\alpha_i)p_{i-1}(x)-
\sum_{m=1}^{i-1}h_{i-m,i}
\left(
\prod_{j=i-m+1}^{i}\beta_j
\right)
p_{i-m-1}(x)
$$

At this point the entire algorithm is complete; this algorithm is generally called the Hessenberg algorithm.

## Cayley–Hamilton theorem

For any $n$-th order matrix $A$ with characteristic polynomial $f(\lambda)=|\lambda I-A|$, we must have $f(A)=0$.

For a linear transformation $T$ there is a parallel result: if $f(\lambda)$ is the characteristic polynomial of $T$, then $f(T)$ is the zero transformation.

From this theorem, one knows that for any matrix $A$, there must exist a polynomial that annihilates it.

## Minimal polynomial

Let $V$ be an $n$-dimensional vector space; since the matrix corresponding to a linear transformation has $n^2$ elements, all linear transformations form an $n^2$-dimensional linear space.

For a specific linear transformation $T$, from applying it $0$ times to applying it $n$ times, there are a total of $n^2+1$ linear transformations, whose corresponding matrices must be linearly dependent. So there exists a nonzero polynomial $f$ such that $f(T)$ is the zero transformation; the transformation $T$ is said to satisfy the polynomial $f$. Among all polynomials $f$ that $T$ satisfies, there is one of the lowest degree.

The monic polynomial of the lowest degree that can annihilate the matrix $A$ is called the minimal polynomial of $A$, denoted $m_A(\lambda)$.

By the Euclidean algorithm for polynomials, the minimal polynomial is unique and divides any annihilating polynomial of $A$. In particular, the minimal polynomial divides the characteristic polynomial.

Theorem: Not counting multiplicity, the characteristic polynomial $f(\lambda)$ and the minimal polynomial $m_A(\lambda)$ of a matrix $A$ have the same roots.

Theorem: Eigenvectors of a matrix $A$ belonging to different eigenvalues are linearly independent.

## Applications

In informatics we generally consider matrices over $(\mathbb{Z}/m\mathbb{Z})^{n\times n}$, usually with $m$ prime, and performing the above similarity transformation is simple; when $m$ is composite, we can consider a method similar to the Euclidean algorithm.

??? note "Implementation"
    ```cpp
    #include <cassert>
    #include <iostream>
    #include <random>
    #include <vector>
    
    using Matrix = std::vector<std::vector<int>>;
    using i64 = int64_t;
    
    Matrix to_upper_Hessenberg(const Matrix &M, int mod) {
      Matrix H(M);
      int n = H.size();
      for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
          if ((H[i][j] %= mod) < 0) H[i][j] += mod;
        }
      }
      for (int i = 0; i < n - 1; ++i) {
        int pivot = i + 1;
        for (; pivot < n; ++pivot) {
          if (H[pivot][i] != 0) break;
        }
        if (pivot == n) continue;
        if (pivot != i + 1) {
          for (int j = i; j < n; ++j) std::swap(H[i + 1][j], H[pivot][j]);
          for (int j = 0; j < n; ++j) std::swap(H[j][i + 1], H[j][pivot]);
        }
        for (int j = i + 2; j < n; ++j) {
          for (;;) {
            if (H[j][i] == 0) break;
            if (H[i + 1][i] == 0) {
              for (int k = i; k < n; ++k) std::swap(H[i + 1][k], H[j][k]);
              for (int k = 0; k < n; ++k) std::swap(H[k][i + 1], H[k][j]);
              break;
            }
            if (H[j][i] >= H[i + 1][i]) {
              int q = H[j][i] / H[i + 1][i], mq = mod - q;
              for (int k = i; k < n; ++k)
                H[j][k] = (H[j][k] + i64(mq) * H[i + 1][k]) % mod;
              for (int k = 0; k < n; ++k)
                H[k][i + 1] = (H[k][i + 1] + i64(q) * H[k][j]) % mod;
            } else {
              int q = H[i + 1][i] / H[j][i], mq = mod - q;
              for (int k = i; k < n; ++k)
                H[i + 1][k] = (H[i + 1][k] + i64(mq) * H[j][k]) % mod;
              for (int k = 0; k < n; ++k)
                H[k][j] = (H[k][j] + i64(q) * H[k][i + 1]) % mod;
            }
          }
        }
      }
      return H;
    }
    
    std::vector<int> get_charpoly(const Matrix &M, int mod) {
      Matrix H(to_upper_Hessenberg(M, mod));
      int n = H.size();
      std::vector<std::vector<int>> p(n + 1);
      p[0] = {1 % mod};
      for (int i = 1; i <= n; ++i) {
        const std::vector<int> &pi_1 = p[i - 1];
        std::vector<int> &pi = p[i];
        pi.resize(i + 1, 0);
        int v = mod - H[i - 1][i - 1];
        if (v == mod) v -= mod;
        for (int j = 0; j < i; ++j) {
          pi[j] = (pi[j] + i64(v) * pi_1[j]) % mod;
          if ((pi[j + 1] += pi_1[j]) >= mod) pi[j + 1] -= mod;
        }
        int t = 1;
        for (int j = 1; j < i; ++j) {
          t = i64(t) * H[i - j][i - j - 1] % mod;
          int prod = i64(t) * H[i - j - 1][i - 1] % mod;
          if (prod == 0) continue;
          prod = mod - prod;
          for (int k = 0; k <= i - j - 1; ++k)
            pi[k] = (pi[k] + i64(prod) * p[i - j - 1][k]) % mod;
        }
      }
      return p[n];
    }
    
    bool verify(const Matrix &M, const std::vector<int> &charpoly, int mod) {
      if (mod == 1) return true;
      int n = M.size();
      std::vector<int> randvec(n), sum(n, 0);
      std::mt19937 gen(std::random_device{}());
      std::uniform_int_distribution<int> dis(1, mod - 1);
      for (int i = 0; i < n; ++i) randvec[i] = dis(gen);
      for (int i = 0; i <= n; ++i) {
        int v = charpoly[i];
        for (int j = 0; j < n; ++j) sum[j] = (sum[j] + i64(v) * randvec[j]) % mod;
        std::vector<int> prod(n, 0);
        for (int j = 0; j < n; ++j) {
          for (int k = 0; k < n; ++k) {
            prod[j] = (prod[j] + i64(M[j][k]) * randvec[k]) % mod;
          }
        }
        randvec.swap(prod);
      }
      for (int i = 0; i < n; ++i)
        if (sum[i] != 0) return false;
      return true;
    }
    
    int main() {
      std::ios::sync_with_stdio(false);
      std::cin.tie(nullptr);
      int n, mod;
      std::cin >> n >> mod;
      Matrix M(n, std::vector<int>(n));
      for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j) std::cin >> M[i][j];
      std::vector<int> charpoly(get_charpoly(M, mod));
      for (int i = 0; i <= n; ++i) std::cout << charpoly[i] << ' ';
      assert(verify(M, charpoly, mod));
      return 0;
    }
    ```

The above Hessenberg algorithm does not have numerical stability, so a matrix over $\mathbb{R}^{n\times n}$ needs to be adjusted with other algorithms before use, or one should use another numerically stable algorithm instead.

We can relate the characteristic polynomial to homogeneous linear recurrences with constant coefficients, and can also combine the Cayley–Hamilton theorem and polynomial modulo to speed up some algorithms for finding matrix powers over a field.

The Cayley–Hamilton theorem states

$$
\begin{aligned}
p_A(A)&=A^n+c_1A^{n-1}+\cdots +c_{n-1}A+c_nI\\
&=O
\end{aligned}
$$

where $O$ is the $n\times n$ zero matrix, $A\in\mathbb{C}^{n\times n}$, and $p_A(x)=x^n+\sum_{i=1}^nc_ix^{n-i}\in\mathbb{C}[x]$ is the characteristic polynomial of $A$.

If we want to find $A^K$ where $K$ is large, then we can find $f(x)=x^K\bmod{p_A(x)}$ and then use $f(A)=A^K$.

And $\deg(f(x))\lt n$ is obvious. Let $f(x)=\sum_{i=0}^{n-1}f_ix^i$ and $n=km$; then

$$
\begin{aligned}
f_{km-1}x^{km-1}+\cdots +f_1x+f_0&=(\cdots (f_{km-1}x^{k-1}+\cdots +f_{k(m-1)})x^k\\
&+f_{k(m-1)-1}x^{k-1}+\cdots +f_{k(m-2)})x^k\\
&+\cdots\\
&+f_{k-1}x^{k-1}+\cdots +f_1x+f_0
\end{aligned}
$$

Letting $k=\sqrt{n}$, one can find that computing $f(A)$ requires about $O(\sqrt{n})$ matrix-matrix multiplications.

## References

-   Rizwana Rehman, Ilse C.F. Ipsen. [La Budde's Method for Computing Characteristic Polynomials](https://ipsen.math.ncsu.edu/ps/charpoly3.pdf).
-   Marshall Law. [Computing Characteristic Polynomials of Matrices of Structured Polynomials](http://summit.sfu.ca/system/files/iritems1/17301/etd10125_.pdf).
