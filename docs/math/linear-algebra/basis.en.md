author: cesonic, Enter-tainer, Great-designer, Ir1d, ksyx, lychees, MegaOwIer, RUIN-RISE, wjy-yy, rsdbkhusky, ouuan, Menci, Tiphereth-A

Recalling the concept of basis vectors in high-school mathematics solid geometry, we can find a set of basis vectors $\boldsymbol{i}$, $\boldsymbol{j}$, $\boldsymbol{k}$ in three-dimensional Euclidean space, after which any vector in space can be represented by this set of basis vectors. In other words, we can **describe the infinite three-dimensional space through finitely many basis vectors**, which sufficiently reflects the importance of basis vectors.

Three-dimensional Euclidean space is a special [linear space](./vector-space.md), and the basis vectors of three-dimensional Euclidean space are generalized in a linear space to a linear basis.

The applications of linear bases in OI generally involve only two kinds of linear spaces: the $n$-dimensional real linear space $\mathbf{R}^n$ and the $n$-dimensional [boolean-domain](https://en.wikipedia.org/wiki/Boolean_domain) linear space $\mathbf{Z}_2^n$; we will introduce them in detail in the [applications](#applications) section. If you are not familiar with linear algebra, it is recommended to start reading from the applications part.

Below we introduce the linear basis starting from a general linear space, and give the common properties of the linear basis.

Prerequisites: [linear space](./vector-space.md).

A linear basis is a basis of a linear space, and is an important tool for studying linear spaces.

## Definition

A maximal linearly independent group of a linear space $V$ is called a **Hamel basis** or **linear basis** of $V$, **basis** for short.

It is stipulated that the basis of the linear space $\{\theta\}$ is the empty set.

It can be proved that any linear space has a linear basis[^existence_basis]; we define the **dimension** of a linear space $V$ as the number of elements (or cardinality) of a linear basis, denoted $\dim V$.

## Properties

1.  For a finite-dimensional linear space $V$, let its dimension be $n$; then:

    1.  Any $n+1$ vectors in $V$ are linearly dependent.

    2.  Any $n$ linearly independent vectors in $V$ are a basis of $V$.

    3.  If any vector in $V$ can be linearly represented by the vector group $a_1,a_2,\dots,a_n$, then it is a basis of $V$.

        ???+ note "Proof"
            Take any basis $b_1,b_2,\dots,b_n$ of $V$; by the given condition, the vector group $b_1,b_2,\dots,b_n$ can be linearly represented by $a_1,a_2,\dots,a_n$, so
            
            $$
            n=\operatorname{rank}\{b_1,b_2,\dots,b_n\}\leq\operatorname{rank}\{a_1,a_2,\dots,a_n\}\leq n
            $$
            
            therefore $\operatorname{rank}\{a_1,a_2,\dots,a_n\}=n$

    4.  Any linearly independent vector group $a_1,a_2,\dots,a_m$ in $V$ can be turned into a basis of $V$ by inserting some vectors.

2.  (Subspace dimension formula) Let $V_1,V_2$ be finite-dimensional linear spaces over $\Bbb{P}$, with $V_1+V_2$ and $V_1\cap V_2$ also finite-dimensional; then $\dim V_1+\dim V_2=\dim(V_1+V_2)+\dim(V_1\cap V_2)$

    ???+ note "Proof"
        Let $\dim V_1=n_1$, $\dim V_2=n_2$, $\dim(V_1\cap V_2)=m$.
        
        Take a basis $a_1,a_2,\dots,a_m$ of $V_1\cap V_2$, and extend it to bases of $V_1$ and $V_2$ respectively: $a_1,a_2,\dots,a_m,b_1,b_2,\dots,b_{n_1-m}$ and $a_1,a_2,\dots,a_m,c_1,c_2,\dots,c_{n_2-m}$.
        
        Next it suffices to prove that the vector group $a_1,a_2,\dots,a_m,b_1,b_2,\dots,b_{n_1-m},c_1,c_2,\dots,c_{n_2-m}$ is linearly independent.
        
        Suppose $\sum_{i=1}^m r_ia_i+\sum_{i=1}^{n_1-m} s_ib_i+\sum_{i=1}^{n_2-m} t_ic_i=\theta$.
        
        Then $\sum_{i=1}^{n_2-m} t_ic_i=-\sum_{i=1}^m r_ia_i-\sum_{i=1}^{n_1-m} s_ib_i$.
        
        Note that the left side of the above is in $V_2$ and the right side is in $V_1$, so both sides are in $V_1\cap V_2$, therefore $\sum_{i=1}^{n_2-m} t_ic_i=\sum_{i=1}^m k_ia_i$
        
        So $t_1=t_2=\dots=t_{n_2-m}=k_1=k_2=\dots=k_m=0$, and further $r_1=r_2=\dots=r_m=s_1=s_2=\dots=s_{n_1-m}=t_1=t_2=\dots=t_{n_2-m}=0$

3.  Let $V_1,V_2$ be finite-dimensional linear spaces over $\Bbb{P}$, with $V_1+V_2$ and $V_1\cap V_2$ also finite-dimensional; then the following are equivalent:

    1.  $V_1+V_2=V_1\oplus V_2$.

    2.  $\dim V_1+\dim V_2=\dim(V_1+V_2)$.

    3.  If $a_1,a_2,\dots,a_n$ is a basis of $V_1$ and $b_1,b_2,\dots,b_m$ is a basis of $V_2$, then $a_1,a_2,\dots,a_n,b_1,b_2,\dots,b_m$ is a basis of $V_1+V_2$.

    ???+ note "Note"
        Items 1 and 3 can be generalized to infinite-dimensional linear spaces

## Examples

Consider a basis of $\Bbb{R}^2$.

1.  As shown

    ![](./images/basis-1.svg)

    $u,v$ is a basis.

2.  As shown

    ![](./images/basis-2.svg)

    $u,v$ is a basis.

3.  As shown

    ![](./images/basis-3.svg)

    $u,v$ is not a basis, because $u=-v$.

4.  As shown

    ![](./images/basis-4.svg)

    $u,v,w$ is not a basis, because $u+4v+6w=\theta$.

## Orthogonal basis and orthonormal basis

If a basis $B$ of a linear space $V$ satisfies $\forall b,b'\in B,~(b,b')\ne 0\iff b=b'$ (i.e. pairwise orthogonal), then this basis is called an **orthogonal basis**.

If an orthogonal basis $B$ of a linear space $V$ further satisfies $\forall b\in B,~|b|=\sqrt{(b,b)}=1$, then this basis is called an **orthonormal basis**.

The basis of any finite-dimensional linear space $V$ can be transformed into an orthogonal basis via [Schmidt orthogonalization](https://en.wikipedia.org/wiki/Gram%E2%80%93Schmidt_process).

## Applications

Based on the earlier content, we can use a linear basis to:

1.  find the rank of a given vector group;
2.  for a given vector group, find a maximal linearly independent group (or a basis of the linear space it spans);
3.  insert some vectors into a given vector group, and find a maximal linearly independent group (or a basis of the linear space it spans) in the vector group after the insertion operation;
4.  for a found maximal linearly independent group (or basis), determine whether a certain vector can be linearly represented by it;
5.  for a found maximal linearly independent group (or basis), find special elements in the linear space it spans (such as the maximum element, minimum element, etc.).

In OI, we generally call a linear basis under the $n$-dimensional real linear space $\mathbf{R}^n$ a **real linear basis**, and a linear basis under the $n$-dimensional boolean-domain linear space $\mathbf{Z}_2^n$ an **XOR linear basis**.

???+ tip "Tip"
    Addition in $\mathbf{Z}_2$ is XOR and multiplication is AND; one can prove that $\mathbf{Z}_2$ is a field.
    
    One can prove that the algebraic system $(\mathbf{Z}_2^n,+,\cdot,\mathbf{Z}_2)$ is a linear space, where:
    
    $$
    (a_1,\dots,a_n)+(b_1,\dots,b_n):=(a_1+b_1,\dots,a_n+b_n),
    $$
    
    $$
    k\cdot(a_1,\dots,a_n):=(ka_1,\dots,ka_n).
    $$
    
    That is, addition is XOR and scalar multiplication is AND.

Taking the XOR linear basis as an example, we can construct an XOR linear basis $B=\{b_1,\dots,b_n\}$ from a given group of boolean sequences $X=\{x_1,\dots,x_m\}$; this basis has the following properties:

1.  The XOR sum of any non-empty subset of $B$ is not $0$;
2.  For any element $x$ in $X$, one can take out some elements in $B$ whose XOR sum is $x$;
3.  For any set $B'$ satisfying the above two properties, its number of elements is no less than the number of elements of $B$.

We can use the XOR linear basis to:

1.  determine whether a number can be represented as the XOR sum of a subset of some number set;
2.  find the number of ways to represent a number as the XOR sum of a subset of some number set;
3.  find the maximum/minimum/$k$-th largest/$k$-th smallest XOR sum of a subset of some number set;
4.  find the rank of a number among the XOR sums of subsets of some number set.

### Construction methods

Because there is no essential difference between the XOR linear basis and the real linear basis, we next take the XOR linear basis as an example; the real-linear-basis version of the code only requires a little simple modification.

#### Greedy method

Convert each number $p$ in the original set to binary, scan from the high bit to the low bit; for the $x$-th bit that is $1$, if $a_x$ does not exist, then let $a_x \leftarrow p$ and end the scan, and if it exists, let $p\leftarrow p~\text{xor}~a_x$.

To query the maximum XOR value of any few elements in the original set, one only needs to scan the linear basis from the high bit to the low bit, and if XOR-ing with the currently scanned $a_x$ makes the answer larger, XOR the answer with $a_x$.

Why does this work? Because scanning from high bit to low bit, if the current scan reaches the $i$-th bit, it means that the $i$-th bit of the answer can be guaranteed to be $1$, and there will be no chance to change the $i$-th bit afterward.

To query the minimum XOR value of any few elements in the original set, it is the smallest of all elements in the linear-basis set.

To query whether a certain number can be XOR-ed out is similar to insertion: if the finally inserted number $p$ is XOR-ed to $0$, then it can be XOR-ed out.

??? example "Code (Luogu P3812 [【模板】线性基](https://www.luogu.com.cn/problem/P3812))"
    ```cpp
    --8<-- "docs/math/code/basis/basis_1.cpp"
    ```

#### Gaussian elimination method

The Gaussian elimination method amounts to constructing the linear basis from the perspective of a system of linear equations, and its correctness is obvious.

??? example "Code (Luogu P3812 [【模板】线性基](https://www.luogu.com.cn/problem/P3812))"
    ```cpp
    --8<-- "docs/math/code/basis/basis_2.cpp"
    ```

### Properties

The linear basis constructed by the greedy method has the following properties:

-   The linear basis has no subset with XOR sum $0$.
-   The numbers in the linear basis have different highest binary bits.

The linear basis constructed by the Gaussian elimination method satisfies the following properties:

-   The matrix after Gaussian elimination is a reduced row echelon form matrix.

    > This property includes the two properties satisfied by the linear basis constructed by the greedy method

    If you do not understand the correctness of this property, you can jump to [Gaussian elimination](../numerical/gauss.md).

Here is a sample:

```text
5
633 211 169 841 1008
```

Binary representation:

```text
1001111001
0011010011
0010101001
1101001001
1111110000
```

Linear basis generated by the greedy method:

```text
1001111001
0100110000
0011010011
0001111010
0000000000
0000010000
0000000000
0000000000
0000000000
0000000000
```

Linear basis generated by the Gaussian elimination method:

```text
1000000011
0100100000
0010101001
0001101010
0000010000
0000000000
0000000000
0000000000
0000000000
0000000000
```

This is a very good property that can help us solve many problems more conveniently. For example: given some numbers, choose some of them to XOR together, and find the maximum XOR value; if one uses the greedy method to construct the linear basis, one needs to do another greedy pass—if the current bit of `ans` is `0`, then XOR-ing will definitely be better, otherwise if the current bit is `1`, it will definitely not be better; while after using the Gaussian elimination method to construct the linear basis, one can directly XOR all elements in the linear basis together and output.

For other more classic problems (querying whether a number can be XOR-ed out, querying the $k$-th largest number that can be XOR-ed out, etc.), the linear basis obtained by the Gaussian elimination method can also solve them more conveniently.

### Time complexity

Let the vector length be $n$ and the total count be $m$; then the time complexity is $O(nm)$. Among them, the constant of the Gaussian elimination method is slightly larger.

For a real linear basis, the time complexity is $O(n^2m)$.

### Merging linear bases

Merging linear bases only needs brute-force processing, i.e. brute-force inserting one group of linear bases to be merged into another group of linear bases. The time complexity of a single merge is $O(n^2)$ (XOR linear basis) or $O(n^3)$ (real linear basis).

### Intersection of linear bases

The intersection of linear bases is, strictly speaking, finding a linear basis of the intersection space of the two linear spaces they span. This section introduces two algorithms. For both algorithms, the time complexity of a single intersection is $O(n^2)$ (XOR linear basis) or $O(n^3)$ (real linear basis).

#### Naive algorithm

Let the linear bases to be intersected be $\alpha$ and $\beta$ respectively. The algorithm for the intersection of linear bases only needs to make the following adjustments to the brute-force merging algorithm: (taking the XOR linear basis as an example)

-   Try to insert the vectors $\beta_j$ in the linear basis $\beta$ into $\alpha$ using the [greedy method](#greedy-method), and initialize the intersection of the linear bases $\gamma$ to the empty set;
-   During insertion, one needs to record the contribution of the elements of the linear basis $\beta$ in the vector to be inserted. Specifically, maintain a new vector $b$, initialized to $\beta_j$, and if the vector being inserted was XOR-ed with the vector at the $x$-th bit of the linear basis, then the contribution $b$ must also be XOR-ed once with the contribution $b_x$ recorded at the $x$-th bit;
-   If the insertion succeeds and a vector $\beta_j'$ is inserted at the $x$-th bit of the linear basis, then change the $b_x$ recorded at the $x$-th bit to the contribution $b$ of the elements of the linear basis $\beta$ in the process of obtaining $\beta_j'$;
-   If the insertion is unsuccessful, insert the contribution $b$ of the elements of the linear basis $\beta$ recorded in the process into $\gamma$.

The linear basis $\gamma$ obtained this way is the required intersection; of course, this algorithm also finds the union of the linear bases at the same time.

??? note "Explanation of the algorithm"
    Let the merged linear basis be $\{\alpha_1,\cdots,\alpha_m,\beta'_{j_1},\cdots,\beta'_{j_\ell}\}$, where $\beta'_{j_k}$ is the vector finally obtained when inserting $\beta_{j_k}$. Then $\{\alpha_1,\cdots,\alpha_m,\beta_{j_1},\cdots,\beta_{j_\ell}\}$ is likewise a merged linear basis. Denote by $\beta^+$ the set $\{\beta_{j_1},\cdots,\beta_{j_\ell}\}$; then the merged basis can be written as $\alpha\cup\beta^+$. Moreover, each vector $c$ in the sum space can be uniquely represented in the form
    
    $$
    c = a\oplus b
    $$
    
    where $a\in\operatorname{span}\alpha$ and $b\in\operatorname{span}\beta^+$. The $b$ in this decomposition is precisely the "contribution of the elements of the linear basis $\beta$" that the earlier algorithm **attempts** to record. Strictly speaking, it is only the contribution of those vectors in $\beta$ that were finally inserted successfully.
    
    For a successful insertion, the finally recorded $b$ is the $b$ term in this decomposition. Let $\beta_j\in\beta^+$. Initially, $\beta_j=0\oplus\beta_j$, which is already the correct decomposition of $\beta_j$ on the basis $\alpha\cup\beta^+$. When updating $\beta'_j=a\oplus b$ to $\beta'_j\oplus c_x$, because $\beta_j'\oplus c_x=(a\oplus a_x)\oplus(b\oplus b_x)$, one only needs to update $b$ to $b\oplus b_x$ to guarantee that the decomposition is still correct. Therefore, by induction, when $\beta'_j$ is finally inserted into the merged linear basis, the recorded contribution $b$ is the $b$ term in the above decomposition.
    
    For an unsuccessful insertion, the variable to be finally inserted will definitely become $0$, and the contribution $b$ at this point is to be inserted into $\gamma$. In this case, if one repeats the above argument, one finds that one can still guarantee that during the insertion process there is always $\beta_j'=a\oplus b$ with $a\in\operatorname{span}\alpha$, only $b$ no longer belongs to $\operatorname{span}\beta^+$. This is because at initialization, the $\beta_j$ in $\beta_j=0\oplus\beta_j$ satisfies $\beta_j\notin\beta^+$. Apart from this, the terms XOR-ed during the contribution update all belong to $\operatorname{span}\beta^+$. So, in fact, $b\oplus\beta_j\in\operatorname{span}\beta^+$.
    
    Then, why does inserting all these $b$ from unsuccessful insertions into $\gamma$ yield a linear basis of the intersection space? First, if inserting $\beta_j$ is unsuccessful, one will finally obtain $0=a\oplus b$, where $a\in\operatorname{span}\alpha$ and $b\in\operatorname{span}(\beta^+\cup\{\beta_j\})\subseteq\operatorname{span}\beta$. Therefore, $b=a$ must lie in the intersection space $\operatorname{span}\alpha\cap\operatorname{span}\beta$. Conversely, let $c$ be any element in the intersection space; because $c\in\operatorname{span}\beta$, $c$ can be represented as a linear combination (XOR sum) of elements in $\beta$:
    
    $$
    c = \bigoplus_{\beta_j\in\beta}\lambda_j\beta_j,
    $$
    
    where $\lambda_j\in\{0,1\}$. For each $\beta_j\notin\beta^+$, denote the corresponding contribution inserted into $\gamma$ by $b_j$; then
    
    $$
    c\oplus\bigoplus_{\beta_j\notin\beta^+}\lambda_jb_j = \bigoplus_{\beta_j\in\beta^+}\lambda_j\beta_j+\bigoplus_{\beta_j\notin\beta^+}\lambda_j(\beta_j\oplus b_j),
    $$
    
    Note that $b_j$ and $c$ both lie in the intersection space, so the left side must also lie in the intersection space, so the left side can be written as a linear combination of elements in $\alpha$; at the same time, for all terms on the right side, either $\beta_j\in\beta^+$, or $\beta_j\notin\beta^+$ and $\beta_j\oplus b_j\in\beta^+$, so the right side is in fact a linear combination of elements in $\beta^+$. But $\alpha\cup\beta^+$ is linearly independent, so all coefficients are $0$, that is, $c=\bigoplus_{\beta_j\notin\beta^+}\lambda_jb_j\in\operatorname{span}\{b_1,\cdots,b_j\}$. This shows that the contributions $b$ of these vectors that cannot be inserted together span the intersection space.
    
    According to this explanation, the purpose of maintaining the contribution $b$ during the process is in fact to maintain the decomposition $a\oplus b$; and when finally inserting the contribution into $\gamma$, there is always $a=b$. So, no matter whether one maintains the contribution of the elements of $\alpha$ or $\beta$ (i.e. no matter whether one maintains $a$ or $b$), the result obtained is correct. If one wants to maintain the contribution of the elements of the linear basis $\alpha$, one only needs to modify the values of the corresponding contributions at initialization: each vector $\alpha_i$ in $\alpha$ has initial contribution $\alpha_i$, while the inserted $\beta_j$ has initial contribution $0$.

The template-problem code is as follows:

??? example "Code (Library Checker [Intersection of $\mathbf F_2$ vector spaces](https://judge.yosupo.jp/problem/intersection_of_f2_vector_spaces))"
    ```cpp
    --8<-- "docs/math/code/basis/basis_intersect_1.cpp"
    ```

#### Zassenhaus algorithm

Another equivalent approach is the Zassenhaus algorithm, which can likewise compute both the union and intersection of two linear bases at the same time. Its complexity is entirely consistent with the above.

The specific steps are as follows:

-   Initialize a linear basis $\gamma$ of vector length $2n$ to empty, where the vectors are written in the form $(a,b)$ with $a$ and $b$ both of length $n$;
-   Insert the elements $\alpha_i$ in $\alpha$ into $\gamma$ in the form $(\alpha_i,\alpha_i)$;
-   Insert the elements $\beta_j$ in $\beta$ into $\gamma$ in the form $(\beta_j,0)$;
-   Among all the nonzero elements $(c_k,d_k)$ in the finally obtained linear basis $\gamma$, the collection of the terms $c_k$ among those vectors with nonzero $c_k$ forms a linear basis of the union of $\alpha$ and $\beta$, and the collection of the terms $d_k$ among those vectors with $c_k$ equal to zero forms a linear basis of the intersection of $\alpha$ and $\beta$.

The method for constructing the linear basis in the algorithm can be the [greedy method](#greedy-method) or the [Gaussian elimination method](#gaussian-elimination-method), as long as one ensures that the linear basis in $\gamma$ forms a row echelon form matrix.

Comparing the elimination step in the Zassenhaus algorithm with the naive algorithm above, one can easily find that the Zassenhaus algorithm based on the greedy method amounts to the naive algorithm maintaining the contribution of the elements of $\alpha$. If instead one first inserts all $(\alpha_i,0)$, then inserts all $(\beta_j,\beta_j)$, then the Zassenhaus algorithm based on the greedy method amounts to the naive algorithm maintaining the contribution of the elements of $\beta$. By the equivalence of the elimination steps, the correctness of the Zassenhaus algorithm also holds.

Apart from this, one can also provide an independent and more general algebraic proof:

??? note "Proof of correctness"
    Let $V$ be a linear space with subspaces $U=\operatorname{span}\alpha$ and $W=\operatorname{span}\beta$. The algorithm itself amounts to finding, by reducing to row echelon form, a basis $\gamma$ of the subspace
    
    $$
    H = \operatorname{span}(\{(\alpha_i,\alpha_i):\alpha_i\in\alpha\}\cup\{(\beta_j,0):\beta_j\in\beta\}).
    $$
    
    At the end of the algorithm, the elements $(c_k,d_k)$ in $\gamma$ need to be divided into two classes according to whether $c_k\neq 0$, so consider the projection map $\pi:H\rightarrow V$ with $\pi(a,b)=a$. Then $\pi(H)=U+W$ and one can easily verify
    
    $$
    \begin{aligned}
    \ker\pi &= H\cap(\{0\}\times V) = \{0\}\times(U\times W).
    \end{aligned}
    $$
    
    By the [related theorem of linear mappings](./linear-mapping.md#the-null-space-and-image-space-of-a-linear-mapping), $\dim H = \dim\pi(H)+\dim\ker\pi = \dim(U+W)+\dim(U\cap W)$.
    
    The first few columns of a row echelon form matrix are still a row echelon form matrix, so the number of rows with $c_k\neq 0$ is exactly equal to the row rank of $\alpha\cup\beta$, i.e. $\dim(U+W)$; and the set of $c_k$ in these rows forms a basis of $U+W$. The remaining nonzero rows are exactly $\dim(U\cap W)$ in number, and all satisfy $c_k=0$. For the $d_k$ in these rows, because $(0,d_k)\in\ker\pi$, we have $d_k\in U\cap W$; and $(0,d_k)$, as rows of a row echelon form matrix, are necessarily linearly independent, which shows that these $d_k$ are all linearly independent. Combining these, these $d_k$ are a linearly independent group of size $\dim(U\cap W)$ in the intersection space $U\cap W$, so they must also be a basis of that space.

The template-problem code is as follows:

??? example "Code (Library Checker [Intersection of $\mathbf F_2$ vector spaces](https://judge.yosupo.jp/problem/intersection_of_f2_vector_spaces))"
    ```cpp
    --8<-- "docs/math/code/basis/basis_intersect_2.cpp"
    ```

Note that when outputting, one only needs to consider the vectors whose first $n$ bits are all zero.

### Extension: prefix linear basis

This section only discusses the case of the XOR linear basis, and assumes that a single vector can be stored in $O(1)$ space and that the complexity of a single operation is always $O(1)$.

For the case of needing to query the maximum XOR value of an interval multiple times, a common approach is the [cat tree](../../ds/cat-tree.md) combined with a linear basis, with time complexity $O(nm\log m+n^2q)$, where $n$ is the vector length, $m$ is the sequence length, and $q$ is the number of queries. Another feasible approach is to use the prefix linear basis (or timestamp linear basis), which can reduce the complexity to $O(n(m+q))$.

The prefix linear basis allows, for each prefix of the sequence, maintaining the linear bases of all suffixes of that prefix, so that one can support querying the linear basis of each interval. Note that the linear bases of all suffixes $[j,i]$ of some prefix $[1,i]$ of the sequence contain one another, i.e. the linear basis of $[j,i]$ always contains the linear basis of $[j+1,i]$, so there are at most $n$ mutually distinct ones among the linear bases of these suffixes, and one can always obtain the linear bases of all these suffixes from $[i,i]$ to $[1,i]$ by gradually adding new vectors to the empty set. Therefore, using this monotonicity, one only needs to mark, for each added vector $v$, the largest index $t$ at which it appears, to store the linear bases of all suffixes in $O(n)$ space. Moreover, when querying the linear basis corresponding to the interval $[j,i]$, one only needs to keep, in the prefix linear basis at $i$, those vectors with mark $t\ge j$.

We may call the mark $t$ of each vector $v$ its timestamp. A vector $v$ in the linear basis can always be represented as the XOR sum of some elements in the original sequence, such as $v_{i_1}\oplus v_{i_2}\oplus\cdots\oplus v_{i_k}$. And among all such possible representations, the maximum of the minimum index is $t$, i.e.

$$
t(v) = \max\{j:\exists i_1,\cdots,i_k\in[j,i]\text{ s.t. }v=v_{i_1}\oplus v_{i_2}\oplus\cdots\oplus v_{i_k}\}.
$$

This expression is nothing but the statement of the previous paragraph written in formal language. The inspiration it brings us is that to maintain the timestamp of each vector $v$ in the linear basis, one only needs to greedily choose the newest possible vector to replace the old vector.

Based on the [greedy method](#greedy-method) mentioned above for constructing a linear basis, the prefix linear basis makes the following adjustments during construction:

-   Store a timestamp $t_x$ for each vector $a_x$ retained in the linear basis, initially all set to $0$;
-   To add the $i$-th vector $v$ in the sequence, still scan from the high bit to the low bit, but at the same time record the current time $i$;
-   If the $x$-th bit of $v$ is one, compare the timestamp $t_x$ of the existing vector $a_x$ in the linear basis with the current time $i$:
    -   If $i>t_x$, i.e. the vector to be added has a later time, set $a_x$ to $v$, update the timestamp to $i$, and continue the adding process for the result $a_x\oplus v$ of XOR-ing the old $a_x$ with $v$ according to the previously recorded time $t_x$;
    -   If $i<t_x$, i.e. the vector to be added has an earlier time, do not update $a_x$ and $t_x$, and continue adding after XOR-ing $v$ with $a_x$.

That is, if the current bit can be represented by a newer vector, directly use the newer vector; otherwise, retain the original vector. When updating the vector at position $x$, one cannot store the XOR result $a_x\oplus v$ at position $x$, because the timestamp of the XOR result $a_x\oplus v$ is $\min\{t(a_x)=t(v)\}=t(a_x)$, which is smaller than the timestamp $t(v)$ of the variable $v$ to be added. For the same reason, the [Gaussian elimination method](#gaussian-elimination-method) of constructing a linear basis may break the property of timestamps when updating upward during the process, so it is no longer applicable to constructing a prefix linear basis.

The template-problem code is as follows:

??? example "Code (Codeforces [1100F Ivan and Burgers](https://codeforces.com/problemset/problem/1100/F))"
    ```cpp
    --8<-- "docs/math/code/basis/prefix_basis.cpp"
    ```

If online queries are needed, one can also use $O(mn)$ space to store the prefix linear basis at each prefix and then query, which can be regarded as a kind of "persistent" linear basis. If one needs to use the properties of the linear basis obtained by the Gaussian elimination method, one can handle it separately at query time.

### Practice problems

-   [Luogu P3812 【模板】线性基](https://www.luogu.com.cn/problem/P3812)
-   [Acwing 3164. 线性基](https://www.acwing.com/problem/content/description/3167)
-   [SGU 275 to xor or not xor](https://codeforces.com/problemsets/acmsguru/problem/99999/275)
-   [HDU 3949 XOR](https://acm.hdu.edu.cn/showproblem.php?pid=3949)
-   [HDU 6579 Operation](https://acm.hdu.edu.cn/showproblem.php?pid=6579)
-   [Luogu P4151 \[WC2011\] 最大 XOR 和路径](https://www.luogu.com.cn/problem/P4151)
-   [Library Checker - Intersection of $\mathbf F_2$ vector spaces](https://judge.yosupo.jp/problem/intersection_of_f2_vector_spaces)
-   [AtCoder Grand Contest 045 A - Xor Battle](https://atcoder.jp/contests/agc045/tasks/agc045_a)
-   [Codeforces 1100F Ivan and Burgers](https://codeforces.com/problemset/problem/1100/F)
-   [Luogu P3292 \[SCOI2016\] 幸运数字](https://www.luogu.com.cn/problem/P3292)

## References and notes

1.  Qiu Weisheng, Advanced Algebra (Vol. 2). Tsinghua University Press.
2.  [Basis (linear algebra) - Wikipedia](https://en.wikipedia.org/wiki/Basis_%28linear_algebra%29)
3.  [Vector Basis -- from Wolfram MathWorld](https://mathworld.wolfram.com/VectorBasis.html)
4.  [Zassenhaus algorithm - Wikipedia](https://en.wikipedia.org/wiki/Zassenhaus_algorithm)

[^existence_basis]: [Proof that every vector space has a basis](https://en.wikipedia.org/wiki/Basis_%28linear_algebra%29#Proof_that_every_vector_space_has_a_basis)
