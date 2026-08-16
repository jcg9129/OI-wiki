Partition: representing a natural number $n$ as a sum of decreasing positive integers.

$$
n=r_1+r_2+\ldots+r_k \quad r_1 \ge r_2 \ge \ldots \ge r_k \ge 1
$$

Each positive integer in the sum is called a part.

Partition number: $p_n$. The number of ways to partition a natural number $n$.

Partition numbers starting from $0$:

| n     | 0 | 1 | 2 | 3 | 4 | 5 | 6  | 7  | 8  |
| ----- | - | - | - | - | - | - | -- | -- | -- |
| $p_n$ | 1 | 1 | 2 | 3 | 5 | 7 | 11 | 15 | 22 |

## k-part partition number

A partition of $n$ into exactly $k$ parts is called a $k$-part partition, and their number is denoted $p(n,k)$.

Obviously, the $k$-part partition number $p(n,k)$ is also the number of solutions of the following equation:

$$
n-k=y_1+y_2+\ldots+y_k\quad y_1\ge y_2\ge\ldots\ge y_k\ge 0
$$

If exactly $j$ parts in this equation are non-zero, then there are exactly $p(n-k,j)$ solutions. Therefore we have the sum:

$$
p(n,k)=\sum_{j=0}^k p(n-k,j)
$$

Taking the difference of two adjacent sums gives:

$$
p(n,k)=p(n-1,k-1)+p(n-k,k)
$$

If we tabulate it, the number in each cell equals the number to its upper-left plus the number in the cell a column-number of cells above it.

| k        | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| -------- | - | - | - | - | - | - | - | - | - |
| $p(0,k)$ | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| $p(1,k)$ | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| $p(2,k)$ | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| $p(3,k)$ | 0 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 |
| $p(4,k)$ | 0 | 1 | 2 | 1 | 1 | 0 | 0 | 0 | 0 |
| $p(5,k)$ | 0 | 1 | 2 | 2 | 1 | 1 | 0 | 0 | 0 |
| $p(6,k)$ | 0 | 1 | 3 | 3 | 2 | 1 | 1 | 0 | 0 |
| $p(7,k)$ | 0 | 1 | 3 | 4 | 3 | 2 | 1 | 1 | 0 |
| $p(8,k)$ | 0 | 1 | 4 | 5 | 5 | 3 | 2 | 1 | 1 |

### Example problem

???+ note "Computing the k-part partition number"
    Compute the $k$-part partition number $p(n,k)$. Multiple inputs, where the upper bound of $n$ is $10000$ and the upper bound of $k$ is $1000$, modulo $1000007$.
    
    Observing the table and the recurrence, updating by column is more advantageous for storage. It is not hard to write the program:
    
    ```cpp
    #include <cstdio>
    #include <cstring>
    
    int p[10005][1005]; /* number of ways to partition natural number n into k parts */
    
    int main() {
      int n, k;
      while (~scanf("%d%d", &n, &k)) {
        memset(p, 0, sizeof(p));
        p[0][0] = 1;
        int i;
        for (i = 1; i <= n; ++i) {
          int j;
          for (j = 1; j <= k; ++j) {
            if (i - j >= 0) /* p[i-j][j]: all parts greater than 1 */
            {
              p[i][j] = (p[i - j][j] + p[i - 1][j - 1]) %
                        1000007; /* p[i-1][j-1]: at least one part equal to 1. */
            }
          }
        }
        printf("%d\n", p[n][k]);
      }
    }
    ```

### Generating function

By the formula for the sum of a geometric sequence, we have:

$$
\frac{1}{1-x^k}=1+x^k+x^{2k}+x^{3k}+\ldots
$$

$$
1+p_1 x+p_2 x^2+p_3 x^3+\ldots=\frac{1}{1-x}  \frac{1}{1-x^2}  \frac{1}{1-x^3}\ldots
$$

For the $k$-part partition number, the generating function is slightly more complex. Specifically, it is written as follows:

$$
\sum_{n,k=0}^\infty {p(n,k) x^n y^k }=\frac{1}{1-xy}  \frac{1}{1-x^2 y}  \frac{1}{1-x^3 y}\ldots
$$

### Ferrers diagram

Ferrers diagram: represent each part of a partition by a row of dots. The number of dots in each row is the size of that part.

By the definition of partition, the different rows in a Ferrers diagram are arranged in decreasing order. The longest row is at the top.

For example: the Ferrers diagram of the partition $12=5+4+2+1$.

![](./images/ferrers.jpg)

Flipping a Ferrers diagram along the diagonal, the new Ferrers diagram obtained is called the conjugate of the original diagram, and the new partition is called the conjugate of the original partition. Obviously, conjugation is a symmetric relation.

For example, the conjugate of the above partition $12=5+4+2+1$ is the partition $12=4+3+2+2+1$.

Maximum-$k$ partition number: the number of partitions of a natural number $n$ whose largest part is $k$.

By the definition of conjugation, there is an obvious conclusion:

The maximum-$k$ partition number and the $k$-part partition number are the same, both being $p(n,k)$.

## Distinct-part partition number

Distinct-part partition number: $pd_n$. The number of partitions of a natural number $n$ in which the parts are all distinct. (Different)

| n      | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| ------ | - | - | - | - | - | - | - | - | - |
| $pd_n$ | 1 | 1 | 1 | 2 | 2 | 3 | 4 | 5 | 6 |

Similarly, define the distinct $k$-part partition number $pd(n,k)$, denoting distinct-part partitions into at most $k$ parts; it is the number of solutions of this equation:

$$
n=r_1+r_2+\ldots+r_k\quad r_1>r_2>\ldots>r_k\ge 1
$$

Exactly as above, it is also the number of solutions of this equation:

$$
n-k=y_1+y_2+\ldots+y_k\quad y_1>y_2>\ldots>y_k\ge 0
$$

The difference here from above is that, due to distinctness, at most one part in the new equation is zero. There is an unchanged conclusion: if exactly $j$ parts are non-zero, then there are exactly $pd(n-k,j)$ solutions, where $j$ takes only $k$ or $k-1$. Therefore we directly obtain the recurrence:

$$
pd(n,k)=pd(n-k,k-1)+pd(n-k,k)
$$

Similarly, tabulating it as with binomial coefficients, the number in each cell equals the number in the cell a column-number of cells above the cell in the previous column, plus the number in the cell a column-number of cells above this cell.

| k         | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| --------- | - | - | - | - | - | - | - | - | - |
| $pd(0,k)$ | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| $pd(1,k)$ | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| $pd(2,k)$ | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| $pd(3,k)$ | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| $pd(4,k)$ | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| $pd(5,k)$ | 0 | 1 | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| $pd(6,k)$ | 0 | 1 | 2 | 1 | 0 | 0 | 0 | 0 | 0 |
| $pd(7,k)$ | 0 | 1 | 3 | 1 | 0 | 0 | 0 | 0 | 0 |
| $pd(8,k)$ | 0 | 1 | 3 | 2 | 0 | 0 | 0 | 0 | 0 |

### Example problem

???+ note "Computing the distinct-part partition number"
    Compute the distinct-part partition number $pd_n$. Multiple inputs, where the upper bound of $n$ is $50000$, modulo $1000007$.
    
    Observing the table and the recurrence, updating by column is more advantageous for storage. In the code, the latter index is reduced in space, keeping only two adjacent terms.
    
    ```cpp
    #include <cstdio>
    #include <cstring>
    
    int pd[50005][2]; /* number of distinct-part ways to partition natural number n into k parts */
    
    int main() {
      int n;
      while (~scanf("%d", &n)) {
        memset(pd, 0, sizeof(pd));
        pd[0][0] = 1;
        int ans = 0;
        int j;
        for (j = 1; j < 350; ++j) {
          int i;
          for (i = 0; i < 350; ++i) {
            pd[i][j & 1] = 0; /* pd[i][j] depends only on pd[][j] and pd[][j-1] */
          }
          for (i = 0; i <= n; ++i) {
            if (i - j >= 0) /* pd[i-j][j]: all parts greater than 1 */
            {
              pd[i][j & 1] = (pd[i - j][j & 1] + pd[i - j][(j - 1) & 1]) %
                             1000007; /* pd[i-j][j-1]: at least one part equal to 1. */
            }
          }
          ans = (ans + pd[n][j & 1]) % 1000007;
        }
        printf("%d\n", ans);
      }
    }
    ```

### Odd partition number

Odd partition number: $po_n$. The number of partitions of a natural number $n$ in which all parts are odd. (Odd)

There is an obvious identity:

$$
\prod_{i=1}^\infty (1+x^i ) =\frac{\prod_{i=1}^\infty (1-x^{2i} ) }{\prod_{i=1}^\infty (1-x^i ) }=\prod_{i=1}^\infty \frac{1}{1-x^{2i-1} }
$$

The leftmost is the generating function of the distinct-part partition numbers, and the rightmost is the generating function of the odd partition numbers. Their corresponding coefficients are the same, therefore the odd partition numbers and the distinct-part partition numbers are the same:

$$
po_n=pd_n
$$

But obviously the $k$-part odd partition number and the distinct $k$-part partition number are not the same concept, so they are not listed here.

Let us introduce two more concepts:

Distinct even-count partition number: $pde_n$. The number of distinct-part partitions of a natural number $n$ whose number of parts is even. (Even)

Distinct odd-count partition number: $pdo_n$. The number of distinct-part partitions of a natural number $n$ whose number of parts is odd. (Odd)

Therefore we have:

$$
pd_n=pde_n+pdo_n
$$

There are also corresponding $k$-part concepts. Being too complex, they are no longer listed.

## Pentagonal number theorem

Consider separately the denominator part of the generating function of the partition numbers:

$$
\prod_{i=1}^\infty (1-x^i ) 
$$

Expanding this part, one can think of distinct-part partitions, related to the parity of the number of parts in the distinct-part partitions.

Specifically, distinct even-count partitions are counted positively in the expansion, and distinct odd-count partitions are counted negatively in the expansion. Therefore each coefficient in the expansion is the difference of the two counts. That is:

$$
\sum_{i=0}^\infty ({pde}_n-{pdo}_n ) x^n =\prod_{i=1}^\infty (1-x^i ) 
$$

Next we show that, in most cases, the two counts above are equal and the coefficient in the expansion is $0$; only in a few positions do the two counts differ by $1$ or $-1$.

Here we can use the method of constructing a correspondence.

Draw the Ferrers diagram of each distinct-part partition. The last row is called the bottom of this diagram, and the number of dots on the bottom is denoted $b$ (Bottom); the longest $45$-degree line segment connecting the last dot of the top row to some dot in the diagram is called the slide of this diagram, and the number of dots on the slide is denoted $s$ (Slide).

![](./images/bottom_slide.jpg)

To construct a correspondence between distinct even-count partitions and distinct odd-count partitions, we need to define a transformation that, while keeping the distinctness condition unchanged, changes the number of rows by $1$:

Transformation A: when $b$ is less than or equal to $s$, move the bottom to the right, making it a new slide.

Transformation B: when $b$ is greater than $s$, move the slide to the bottom, making it a new bottom.

For most $n$ and any distinct-part partition, exactly one of these two transformations can be carried out, which constructs a one-to-one correspondence between distinct even-count partitions and distinct odd-count partitions. The two parts of the partitions for which a one-to-one correspondence has been constructed have equal counts, so in this case the $n$-th coefficient in the expansion is $0$.

But for certain $n$, there exists exactly one distinct-part partition for which the above transformation cannot be carried out.

-   Case 1: when $b=s$ and the bottom and slide have a common point, transformation A cannot be carried out. In this case

$$
n=s+(s+1)+\ldots+(s+s-1)=\frac{s(3s-1)}{2}
$$

The $n$-th term of the expansion is related to the parity of the number of parts of the partition, being $(-1)^s x^n$.

-   Case 2: when $b=s+1$ and the bottom and slide have a common point, transformation B cannot be carried out. In this case

$$
n=(s+1)+(s+2)+\ldots+(s+s)=\frac{s(3s+1)}{2}
$$

The $n$-th term of the expansion is $(-1)^s x^n$.

Replacing $s$ in the above with $-s$ gives $n=\frac{s(3s-1)}{2}$, where $s$ is a negative integer, and the $n$-th term of the expansion is still $(-1)^s x^n$.

Since the two cases do not occur simultaneously at the same $n$, we can combine the two conditions, obtaining that the condition $n$ needs to satisfy is

$$
\exists k\in\mathbb{Z},n=\frac{k(3k-1)}{2}
$$

At this point, we have proved:

$$
(1-x)(1-x^2 )(1-x^3 )\ldots=\sum_{k=-\infty}^{+\infty} (-1)^k x^{\frac{k(3k-1)}{2}} =\ldots+x^{26}-x^{15}+x^7-x^2+1-x+x^5-x^{12}+x^{22}-\ldots
$$

Recall: this expression is the reciprocal of the generating function of the partition numbers, so its product with the generating function of the partition numbers is $1$. Rearranging and comparing the coefficients of the two sides gives the recurrence of the partition-number sequence.

$$
(1+p_1 x+p_2 x^2+p_3 x^3+\ldots)(1-x-x^2+x^5+x^7-x^{12}-x^{15}+x^{22}+x^{26}-\ldots)=1
$$

$$
p_n=p_{n-1}+p_{n-2}-p_{n-5}-p_{n-7}+\ldots
$$

This recurrence has infinitely many terms, but if we stipulate that the partition number of a negative number is $0$ (the partition number of $0$ has already been defined as $1$), then it simplifies to finitely many terms.

### Example problem

???+ note "Computing the partition number"
    Compute the partition number $p_n$. Multiple inputs, where the upper bound of $n$ is $50000$, modulo $1000007$.
    
    Using the method of the pentagonal number theorem. Here is the code:
    
    ```cpp
    #include <cstdio>
    
    long long a[100010];
    long long p[50005];
    
    int main() {
      p[0] = 1;
      p[1] = 1;
      p[2] = 2;
      int i;
      for (i = 1; i < 50005;
           i++) /* recurrence coefficients 1,2,5,7,12,15,22,26...i*(3*i-1)/2,i*(3*i+1)/2 */
      {
        a[2 * i] = i * (i * 3 - 1) / 2; /* pentagonal numbers are 1,5,12,22...i*(3*i-1)/2 */
        a[2 * i + 1] = i * (i * 3 + 1) / 2;
      }
      for (
          i = 3; i < 50005;
          i++) /*p[n]=p[n-1]+p[n-2]-p[n-5]-p[n-7]+p[12]+p[15]-...+p[n-i*[3i-1]/2]+p[n-i*[3i+1]/2]*/
      {
        p[i] = 0;
        int j;
        for (j = 2; a[j] <= i; j++) /* may be negative, add 1000007 in the expression */
        {
          if (j & 2) {
            p[i] = (p[i] + p[i - a[j]] + 1000007) % 1000007;
          } else {
            p[i] = (p[i] - p[i - a[j]] + 1000007) % 1000007;
          }
        }
      }
      int n;
      while (~scanf("%d", &n)) {
        printf("%lld\n", p[n]);
      }
    }
    ```
