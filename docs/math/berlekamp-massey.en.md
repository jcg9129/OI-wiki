author: AntiLeaf

The Berlekamp–Massey algorithm is an algorithm for finding the shortest recurrence of a sequence. Given a sequence of length $n$, if the order of its shortest recurrence is $m$, then the Berlekamp–Massey algorithm can find the shortest recurrence of every prefix of the sequence in $O(nm)$ time. In the worst case $m = O(n)$, so the worst-case complexity of the algorithm is $O(n^2)$.

### Definition

Define a recurrence of a sequence $\{a_0 \dots a_{n - 1} \}$ as a sequence $\{r_0\dots r_m\}$ satisfying the following:

$\sum_{j = 0} ^ m r_j a_{i - j} = 0, \forall i \ge m$

where $r_0 = 1$. $m$ is called the **order** of this recurrence.

The shortest recurrence of the sequence $\{a_i\}$ is the recurrence of least order.

### Approach

Slightly different from the definition above, here we define a new set of recurrence coefficients $\{f_0 \dots f_{m - 1}\}$ satisfying:

$a_i = \sum_{j = 0} ^ {m - 1} f_j a_{i - j - 1}, \forall i \ge m$

It is easy to see that $f_i = -r_{i + 1}$, and the order $m$ is the same as in the previous definition.

We can find the recurrence incrementally, considering each term of $\{a_i\}$ in order, and adjusting the recurrence coefficients $\{f_i\}$ whenever an error appears in the recurrence result. For convenience, in the following we denote the shortest recurrence of the first $i$ terms by $F_i = \{f_{i, j}\}$.

Obviously, initially $F_0 = \{\}$. Suppose the recurrence coefficients $F_{i - 1}$ hold for the first $i - 1$ terms of the sequence $\{a_i\}$; then for the $i$-th term there are two cases:

1.  The recurrence coefficients also hold for $a_i$; in this case no adjustment is needed, and we simply set $F_i = F_{i - 1}$.
2.  The recurrence coefficients do not hold for $a_i$; in this case $F_{i - 1}$ needs to be adjusted to obtain a new $F_i$.

Let $\Delta_i = a_i - \sum_{j = 0} ^ m f_{i - 1, j} a_{i - j - 1}$, i.e. the difference between $a_i$ and the recurrence result of $F_{i - 1}$.

If this is the first time the recurrence coefficients are modified, then this means $a_i$ is the first nonzero term in the sequence. In this case we simply set $F_i$ to be $i$ zeros; obviously this is a valid shortest recurrence.

Otherwise, let the number of terms of $\{a_i\}$ already considered at the last modification of the recurrence coefficients be $k$. If there exists a sequence $G = \{g_0 \dots g_{m' - 1}\}$ satisfying:

$\sum_{j = 0} ^ {m' - 1} g_j a_{i' - j - 1} = 0, \forall i' \in [m', i)$

and $\sum_{j = 0} ^ {m' - 1} g_j a_{i - j - 1} = \Delta_i$, then it is not hard to see that adding $F_k$ and $G$ termwise yields a valid set of recurrence coefficients $F_i$.

Consider how to construct $G$. One feasible construction is to let

$G = \{0, 0, \dots, 0, \frac{\Delta_i}{\Delta_k}, -\frac{\Delta_i}{\Delta_k}F_{k-1}\}$

where there are a total of $i - k - 1$ zeros in front, and the final $-\frac{\Delta_i}{\Delta_k} F_{k-1}$ denotes appending $F_{k-1}$, with each term multiplied by $-\frac{\Delta_i}{\Delta_k}$, to the end of the sequence.

It is not hard to verify that in this case $\sum_{j = 0} ^ {m' - 1} g_j a_{i - j - 1} = \Delta_k \frac{\Delta_i}{\Delta_k} = \Delta_i$, so the $G$ constructed this way is valid. We then assign $F_i$ to be the result of adding $F_k$ and $G$ termwise.

If what is required is the recurrence $\{r_i\}$ conforming to the original definition, then negate all of $\{f_j\}$ and insert $r_0 = 1$ at the beginning.

From the above algorithm flow, one can see that if the order of the shortest recurrence of the sequence is $m$, then the complexity of the algorithm is $O(nm)$. In the worst case $m = O(n)$, so the worst-case complexity of the algorithm is $O(n^2)$.

When implementing the algorithm, since each adjustment of the recurrence coefficients only needs the recurrence coefficients $F_k$ from the last adjustment, if one only needs the shortest recurrence of the entire sequence, one can store only the current recurrence coefficients and those from the last adjustment, giving a space complexity of $O(n)$.

??? note "Reference implementation"
    ```cpp
    vector<int> berlekamp_massey(const vector<int> &a) {
      vector<int> v, last;  // v is the answer, 0-based, p is the module
      int k = -1, delta = 0;
    
      for (int i = 0; i < (int)a.size(); i++) {
        int tmp = 0;
        for (int j = 0; j < (int)v.size(); j++)
          tmp = (tmp + (long long)a[i - j - 1] * v[j]) % p;
    
        if (a[i] == tmp) continue;
    
        if (k < 0) {
          k = i;
          delta = (a[i] - tmp + p) % p;
          v = vector<int>(i + 1);
    
          continue;
        }
    
        vector<int> u = v;
        int val = (long long)(a[i] - tmp + p) * power(delta, p - 2) % p;
    
        if (v.size() < last.size() + i - k) v.resize(last.size() + i - k);
    
        (v[i - k - 1] += val) %= p;
    
        for (int j = 0; j < (int)last.size(); j++) {
          v[i - k + j] = (v[i - k + j] - (long long)val * last[j]) % p;
          if (v[i - k + j] < 0) v[i - k + j] += p;
        }
    
        if ((int)u.size() - i < (int)last.size() - k) {
          last = u;
          k = i;
          delta = a[i] - tmp;
          if (delta < 0) delta += p;
        }
      }
    
      for (auto &x : v) x = (p - x) % p;
      v.insert(v.begin(), 1);
    
      return v;  // $\forall i, \sum_{j = 0} ^ m a_{i - j} v_j = 0$
    }
    ```

The naive Berlekamp–Massey algorithm finds the shortest recurrence of a finite-term sequence. If the sequence whose recurrence is sought has infinitely many terms, but an upper bound on the order of the shortest recurrence is known, then one only needs to take the first $2m$ terms of the sequence to find the shortest recurrence of the entire sequence. (Proof omitted)

### Applications

Because the Berlekamp–Massey algorithm has relatively poor numerical stability, it is generally rarely used when dealing with real-number problems. For convenience of exposition, in the following we always assume that operations are performed in the residue system of some prime $p$.

#### Finding the shortest recurrence of a sequence of vectors or matrices

If we want the shortest recurrence of a sequence of vectors $\boldsymbol{v}_i$, letting the dimension of the vectors be $n$, we can pick a random $n$-dimensional row vector $\mathbf u^T$ and compute the shortest recurrence of the scalar sequence $\{\boldsymbol{u}^T\boldsymbol{v}_i\}$. By the Schwartz–Zippel lemma, the two shortest recurrences are the same with probability at least $1 - \frac n p$.

Finding the shortest recurrence of a sequence of matrices $\{A_i\}$ is similar; letting the size of the matrices be $n \times m$, one only needs to pick a random $1 \times n$ row vector $\mathbf u^T$ and an $m \times 1$ column vector $\boldsymbol{v}$, and compute the shortest recurrence of the scalar sequence $\{\boldsymbol{u}^T A_i \boldsymbol{v}\}$. By the Schwartz–Zippel lemma, one can similarly obtain that the probability of the two being the same is at least $1 - \frac{n + m} p$.

#### Optimizing matrix fast exponentiation

Let $\boldsymbol{f}_i$ be an $n$-dimensional column vector, and suppose the transition satisfies $\boldsymbol{f}_i = A \boldsymbol{f}_{i - 1}$; then one can find that $\{\boldsymbol{f}_i\}$ is a linear recurrent sequence of vectors of order at most $n$. (Proof omitted)

We can directly brute-force compute $\boldsymbol{f}_0 \dots \boldsymbol{f}_{2n - 1}$, then use the approach mentioned earlier to find the shortest recurrence of $\{\boldsymbol{f}_i\}$, and then call [homogeneous linear recurrence with constant coefficients](./poly/linear-recurrence.md).

If the required vector is $\boldsymbol{f}_m$, then the complexity of the algorithm is $O(n^3 + n\log n \log m)$. If $A$ is a sparse matrix with only $k$ nonzero entries, then the complexity can be reduced to $O(nk + n\log n \log m)$. But since the algorithm requires at least $O(nk)$ time for preprocessing, when the constraints are not tight one can also use the $O(n^2 \log m)$ linear recurrence algorithm, whose complexity is likewise acceptable.

#### Finding the minimal polynomial of a matrix

The minimal polynomial of a square matrix $A$ is the polynomial $f$ of least degree satisfying $f(A) = 0$.

In fact the minimal polynomial is precisely the shortest recurrence of $\{A^i\}$, so one can directly call the Berlekamp–Massey algorithm. If $A$ is an $n$-order square matrix, then obviously the degree of the minimal polynomial does not exceed $n$.

The bottleneck lies in computing $A^i$, because if one directly does matrix multiplication each time, the complexity reaches $O(n^4)$. But considering that finding the shortest recurrence of a sequence of matrices actually finds the shortest recurrence of $\{\boldsymbol{u}^T A^i \boldsymbol{v}\}$, we only need to compute $A^i \boldsymbol{v}$.

Assuming $A$ has $k$ nonzero entries, the complexity is $O(kn + n^2)$.

#### Finding the determinant of a sparse matrix

If one can find the characteristic polynomial of a square matrix $A$, then the constant term multiplied by $(-1)^n$ is the determinant. But the minimal polynomial is not necessarily the characteristic polynomial.

In fact, if one multiplies $A$ by a random diagonal matrix $B$, then the minimal polynomial of $AB$ is the characteristic polynomial with probability at least $1 - \frac {2n^2 - n} p$. Finally, one just divides out $\text{det}\;B$.

Let $A$ be an $n$-order square matrix with $k$ nonzero entries; then the complexity is $O(kn + n ^ 2)$.

#### Finding the rank of a sparse matrix

Let $A$ be an $n\times m$ matrix; first pick a random $n\times n$ diagonal matrix $P$ and an $m\times m$ diagonal matrix $Q$, then compute the minimal polynomial of $Q A P A^T Q$.

In fact there is no need to invoke matrix multiplication, because when finding the minimal polynomial one needs to multiply a vector by $Q A P A^T Q$, so we just multiply these matrices into the vector one by one. The answer is the degree remaining after dividing the minimal polynomial by all factors of $x$.

Let $A$ have $k$ nonzero entries and $n \le m$; then the complexity is $O(kn + n ^ 2)$.

#### Solving a sparse system of equations

**Problem**: Given $A \mathbf x = \mathbf b$, where $A$ is an $n \times n$ **full-rank** sparse matrix, and $\mathbf b$ and $\mathbf x$ are $1\times n$ column vectors. $A, \mathbf b$ are known, and one needs to solve for $x$ in complexity lower than $n^\omega$.

**Approach**: Obviously $\mathbf x = A^{-1} \mathbf b$. If we can find the shortest recurrence $\{r_0 \dots r_{m - 1}\}$ ($m \le n$) of $\{A^i \mathbf b\}$ ($i \ge 0$), then we have the conclusion

$A^{-1} \mathbf b = -\frac 1 {r_{m - 1}} \sum_{i = 0} ^ {m - 2} A^i \mathbf b r_{m - 2 - i}$

(Proof omitted)

Because $A$ is a sparse matrix, one directly recurses out $\mathbf b \dots A^{2n - 1} \mathbf b$ by definition.

Likewise, letting $A$ have $k$ nonzero entries, the complexity is $O(kn + n^2)$.

??? note "Reference implementation"
    ```cpp
    vector<int> solve_sparse_equations(const vector<tuple<int, int, int>> &A,
                                       const vector<int> &b) {
      int n = (int)b.size();  // 0-based
    
      vector<vector<int>> f({b});
    
      for (int i = 1; i < 2 * n; i++) {
        vector<int> v(n);
        auto &u = f.back();
    
        for (auto [x, y, z] : A)  // [x, y, value]
          v[x] = (v[x] + (long long)u[y] * z) % p;
    
        f.push_back(v);
      }
    
      vector<int> w(n);
      mt19937 gen;
      for (auto &x : w) x = uniform_int_distribution<int>(1, p - 1)(gen);
    
      vector<int> a(2 * n);
      for (int i = 0; i < 2 * n; i++)
        for (int j = 0; j < n; j++) a[i] = (a[i] + (long long)f[i][j] * w[j]) % p;
    
      auto c = berlekamp_massey(a);
      int m = (int)c.size();
    
      vector<int> ans(n);
    
      for (int i = 0; i < m - 1; i++)
        for (int j = 0; j < n; j++)
          ans[j] = (ans[j] + (long long)c[m - 2 - i] * f[i][j]) % p;
    
      int inv = power(p - c[m - 1], p - 2);
    
      for (int i = 0; i < n; i++) ans[i] = (long long)ans[i] * inv % p;
    
      return ans;
    }
    ```

### Example problems

1.  [LibreOJ #163. 高斯消元 2](https://loj.ac/p/163)
2.  [ICPC2021 台北 Gym103443E. Composition with Large Red Plane, Yellow, Black, Gray, and Blue](https://codeforces.com/gym/103443/problem/E)
