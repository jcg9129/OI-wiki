## Stirling numbers of the second kind (Stirling number)

??? note "Why introduce Stirling numbers of the second kind first"
    Although called "the second kind", Stirling numbers of the second kind were described first in Stirling's related works and in Concrete Mathematics, and are also used much more frequently than Stirling numbers of the first kind.

The **Stirling number of the second kind** (Stirling subset number) $\begin{Bmatrix}n\\ k\end{Bmatrix}$, also denoted $S(n,k)$, represents the number of ways to partition $n$ pairwise distinct elements into $k$ mutually indistinguishable non-empty subsets.

### Recurrence

$$
\begin{Bmatrix}n\\ k\end{Bmatrix}=\begin{Bmatrix}n-1\\ k-1\end{Bmatrix}+k\begin{Bmatrix}n-1\\ k\end{Bmatrix}
$$

The boundary is $\begin{Bmatrix}n\\ 0\end{Bmatrix}=[n=0]$.

Consider proving it by combinatorial meaning.

When we insert a new element, there are two schemes:

-   place the new element in a subset by itself, giving $\begin{Bmatrix}n-1\\ k-1\end{Bmatrix}$ schemes;
-   place the new element into one of the existing non-empty subsets, giving $k\begin{Bmatrix}n-1\\ k\end{Bmatrix}$ schemes.

By the addition principle, adding the two gives the recurrence.

### General term formula

$$
\begin{Bmatrix}n\\m\end{Bmatrix}=\sum\limits_{i=0}^m\dfrac{(-1)^{m-i}i^n}{i!(m-i)!}
$$

We prove this formula using the inclusion-exclusion principle. Let the number of ways to partition $n$ pairwise distinct elements into $i$ pairwise distinct sets (empty sets allowed) be $G_i$, and the number of ways to partition $n$ pairwise distinct elements into $i$ pairwise distinct non-empty sets (empty sets not allowed) be $F_i$.

Obviously

$$
\begin{aligned}
G_i&=i^n\\
G_i&=\sum\limits_{j=0}^i\binom{i}{j}F_j
\end{aligned}
$$

By binomial inversion

$$
\begin{aligned}
F_i&=\sum\limits_{j=0}^{i}(-1)^{i-j}\binom{i}{j}G_j\\
&=\sum\limits_{j=0}^{i}(-1)^{i-j}\binom{i}{j}j^n\\
&=\sum\limits_{j=0}^{i}\dfrac{i!(-1)^{i-j}j^n}{j!(i-j)!}
\end{aligned}
$$

Consider the relationship between $F_i$ and $\begin{Bmatrix}n\\i\end{Bmatrix}$. Stirling numbers of the second kind require the sets to be mutually indistinguishable, so $F_i$ is exactly $i!$ times $\begin{Bmatrix}n\\i\end{Bmatrix}$. Thus

$$
\begin{Bmatrix}n\\m\end{Bmatrix}=\dfrac{F_m}{m!}=\sum\limits_{i=0}^m\dfrac{(-1)^{m-i}i^n}{i!(m-i)!}
$$

### Computing Stirling numbers of the second kind in the same row

"Same row" Stirling numbers of the second kind refers to a series of $\begin{Bmatrix}n\\i\end{Bmatrix}$ with different $i$ and the same $n$. Finding all Stirling numbers of the second kind in the same row means finding, for $i=0..n$, the number of ways to partition $n$ distinct elements into $i$ non-empty sets.

According to the general term formula given above, just compute a convolution. The time complexity of this approach is $O(n \log n)$.

The code below uses a polynomial class named `poly`, for reference only.

??? note "Implementation"
    ```cpp
    #ifndef _FEISTDLIB_POLY_
    #define _FEISTDLIB_POLY_
    
    /*
     * This file is part of the fstdlib project.
     * Version: Build v0.0.2
     * You can check for details at https://github.com/FNatsuka/fstdlib
     */
    
    #include <algorithm>
    #include <cmath>
    #include <cstdio>
    #include <vector>
    
    namespace fstdlib {
    
    using ll = long long;
    int mod = 998244353, grt = 3;
    
    class poly {
     private:
      std::vector<int> data;
    
      void out(void) {
        for (int i = 0; i < (int)data.size(); ++i) printf("%d ", data[i]);
        puts("");
      }
    
     public:
      poly(std::size_t len = std::size_t(0)) { data = std::vector<int>(len); }
    
      poly(const std::vector<int> &b) { data = b; }
    
      poly(const poly &b) { data = b.data; }
    
      void resize(std::size_t len, int val = 0) { data.resize(len, val); }
    
      std::size_t size(void) const { return data.size(); }
    
      void clear(void) { data.clear(); }
    #if __cplusplus >= 201103L
      void shrink_to_fit(void) { data.shrink_to_fit(); }
    #endif
      int &operator[](std::size_t b) { return data[b]; }
    
      const int &operator[](std::size_t b) const { return data[b]; }
    
      poly operator*(const poly &h) const;
      poly operator*=(const poly &h);
      poly operator*(const int &h) const;
      poly operator*=(const int &h);
      poly operator+(const poly &h) const;
      poly operator+=(const poly &h);
      poly operator-(const poly &h) const;
      poly operator-=(const poly &h);
      poly operator<<(const std::size_t &b) const;
      poly operator<<=(const std::size_t &b);
      poly operator>>(const std::size_t &b) const;
      poly operator>>=(const std::size_t &b);
      poly operator/(const int &h) const;
      poly operator/=(const int &h);
      poly operator==(const poly &h) const;
      poly operator!=(const poly &h) const;
      poly operator+(const int &h) const;
      poly operator+=(const int &h);
      poly inv(void) const;
      poly inv(const int &h) const;
      friend poly sqrt(const poly &h);
      friend poly log(const poly &h);
      friend poly exp(const poly &h);
    };
    
    int qpow(int a, int b, int p = mod) {
      int res = 1;
      while (b) {
        if (b & 1) res = (ll)res * a % p;
        a = (ll)a * a % p, b >>= 1;
      }
      return res;
    }
    
    std::vector<int> rev;
    
    void dft_for_module(std::vector<int> &f, int n, int b) {
      static std::vector<int> w;
      w.resize(n);
      for (int i = 0; i < n; ++i)
        if (i < rev[i]) std::swap(f[i], f[rev[i]]);
      for (int i = 2; i <= n; i <<= 1) {
        w[0] = 1, w[1] = qpow(grt, (mod - 1) / i);
        if (b == -1) w[1] = qpow(w[1], mod - 2);
        for (int j = 2; j < i / 2; ++j) w[j] = (ll)w[j - 1] * w[1] % mod;
        for (int j = 0; j < n; j += i)
          for (int k = 0; k < i / 2; ++k) {
            int p = f[j + k], q = (ll)f[j + k + i / 2] * w[k] % mod;
            f[j + k] = (p + q) % mod, f[j + k + i / 2] = (p - q + mod) % mod;
          }
      }
    }
    
    poly poly::operator*(const poly &h) const {
      int N = 1;
      while (N < (int)(size() + h.size() - 1)) N <<= 1;
      std::vector<int> f(this->data), g(h.data);
      f.resize(N), g.resize(N);
      rev.resize(N);
      for (int i = 0; i < N; ++i)
        rev[i] = (rev[i >> 1] >> 1) | (i & 1 ? N >> 1 : 0);
      dft_for_module(f, N, 1), dft_for_module(g, N, 1);
      for (int i = 0; i < N; ++i) f[i] = (ll)f[i] * g[i] % mod;
      dft_for_module(f, N, -1), f.resize(size() + h.size() - 1);
      for (int i = 0, inv = qpow(N, mod - 2); i < (int)f.size(); ++i)
        f[i] = (ll)f[i] * inv % mod;
      return f;
    }
    
    poly poly::operator*=(const poly &h) { return *this = *this * h; }
    
    poly poly::operator*(const int &h) const {
      std::vector<int> f(this->data);
      for (int i = 0; i < (int)f.size(); ++i) f[i] = (ll)f[i] * h % mod;
      return f;
    }
    
    poly poly::operator*=(const int &h) {
      for (int i = 0; i < (int)size(); ++i) data[i] = (ll)data[i] * h % mod;
      return *this;
    }
    
    poly poly::operator+(const poly &h) const {
      std::vector<int> f(this->data);
      if (f.size() < h.size()) f.resize(h.size());
      for (int i = 0; i < (int)h.size(); ++i) f[i] = (f[i] + h[i]) % mod;
      return f;
    }
    
    poly poly::operator+=(const poly &h) {
      std::vector<int> &f = this->data;
      if (f.size() < h.size()) f.resize(h.size());
      for (int i = 0; i < (int)h.size(); ++i) f[i] = (f[i] + h[i]) % mod;
      return f;
    }
    
    poly poly::operator-(const poly &h) const {
      std::vector<int> f(this->data);
      if (f.size() < h.size()) f.resize(h.size());
      for (int i = 0; i < (int)h.size(); ++i) f[i] = (f[i] - h[i] + mod) % mod;
      return f;
    }
    
    poly poly::operator-=(const poly &h) {
      std::vector<int> &f = this->data;
      if (f.size() < h.size()) f.resize(h.size());
      for (int i = 0; i < (int)h.size(); ++i) f[i] = (f[i] - h[i] + mod) % mod;
      return f;
    }
    
    poly poly::operator<<(const std::size_t &b) const {
      std::vector<int> f(size() + b);
      for (int i = 0; i < (int)size(); ++i) f[i + b] = data[i];
      return f;
    }
    
    poly poly::operator<<=(const std::size_t &b) { return *this = (*this) << b; }
    
    poly poly::operator>>(const std::size_t &b) const {
      std::vector<int> f(size() - b);
      for (int i = 0; i < (int)f.size(); ++i) f[i] = data[i + b];
      return f;
    }
    
    poly poly::operator>>=(const std::size_t &b) { return *this = (*this) >> b; }
    
    poly poly::operator/(const int &h) const {
      std::vector<int> f(this->data);
      int inv = qpow(h, mod - 2);
      for (int i = 0; i < (int)f.size(); ++i) f[i] = (ll)f[i] * inv % mod;
      return f;
    }
    
    poly poly::operator/=(const int &h) {
      int inv = qpow(h, mod - 2);
      for (int i = 0; i < (int)data.size(); ++i) data[i] = (ll)data[i] * inv % mod;
      return *this;
    }
    
    poly poly::inv(void) const {
      int N = 1;
      while (N < (int)(size() + size() - 1)) N <<= 1;
      std::vector<int> f(N), g(N), d(this->data);
      d.resize(N), f[0] = qpow(d[0], mod - 2);
      for (int w = 2; w < N; w <<= 1) {
        for (int i = 0; i < w; ++i) g[i] = d[i];
        rev.resize(w << 1);
        for (int i = 0; i < w * 2; ++i)
          rev[i] = (rev[i >> 1] >> 1) | (i & 1 ? w : 0);
        dft_for_module(f, w << 1, 1), dft_for_module(g, w << 1, 1);
        for (int i = 0; i < w * 2; ++i)
          f[i] = (ll)f[i] * (2 + mod - (ll)f[i] * g[i] % mod) % mod;
        dft_for_module(f, w << 1, -1);
        for (int i = 0, inv = qpow(w << 1, mod - 2); i < w; ++i)
          f[i] = (ll)f[i] * inv % mod;
        for (int i = w; i < w * 2; ++i) f[i] = 0;
      }
      f.resize(size());
      return f;
    }
    
    poly poly::operator==(const poly &h) const {
      if (size() != h.size()) return 0;
      for (int i = 0; i < (int)size(); ++i)
        if (data[i] != h[i]) return 0;
      return 1;
    }
    
    poly poly::operator!=(const poly &h) const {
      if (size() != h.size()) return 1;
      for (int i = 0; i < (int)size(); ++i)
        if (data[i] != h[i]) return 1;
      return 0;
    }
    
    poly poly::operator+(const int &h) const {
      poly f(this->data);
      f[0] = (f[0] + h) % mod;
      return f;
    }
    
    poly poly::operator+=(const int &h) { return *this = (*this) + h; }
    
    poly poly::inv(const int &h) const {
      poly f(*this);
      f.resize(h);
      return f.inv();
    }
    
    int modsqrt(int h, int p = mod) { return 1; }
    
    poly sqrt(const poly &h) {
      int N = 1;
      while (N < (int)(h.size() + h.size() - 1)) N <<= 1;
      poly f(N), g(N), d(h);
      d.resize(N), f[0] = modsqrt(d[0]);
      for (int w = 2; w < N; w <<= 1) {
        g.resize(w);
        for (int i = 0; i < w; ++i) g[i] = d[i];
        f = (f + f.inv(w) * g) / 2;
        f.resize(w);
      }
      f.resize(h.size());
      return f;
    }
    
    poly log(const poly &h) {
      poly f(h);
      for (int i = 1; i < (int)f.size(); ++i) f[i - 1] = (ll)f[i] * i % mod;
      f[f.size() - 1] = 0, f = f * h.inv(), f.resize(h.size());
      for (int i = (int)f.size() - 1; i > 0; --i)
        f[i] = (ll)f[i - 1] * qpow(i, mod - 2) % mod;
      f[0] = 0;
      return f;
    }
    
    poly exp(const poly &h) {
      int N = 1;
      while (N < (int)(h.size() + h.size() - 1)) N <<= 1;
      poly f(N), g(N), d(h);
      f[0] = 1, d.resize(N);
      for (int w = 2; w < N; w <<= 1) {
        f.resize(w), g.resize(w);
        for (int i = 0; i < w; ++i) g[i] = d[i];
        f = f * (g + 1 - log(f));
        f.resize(w);
      }
      f.resize(h.size());
      return f;
    }
    
    struct comp {
      long double x, y;
    
      comp(long double _x = 0, long double _y = 0) : x(_x), y(_y) {}
    
      comp operator*(const comp &b) const {
        return comp(x * b.x - y * b.y, x * b.y + y * b.x);
      }
    
      comp operator+(const comp &b) const { return comp(x + b.x, y + b.y); }
    
      comp operator-(const comp &b) const { return comp(x - b.x, y - b.y); }
    
      comp conj(void) { return comp(x, -y); }
    };
    
    const int EPS = 1e-9;
    
    template <typename FLOAT_T>
    FLOAT_T fabs(const FLOAT_T &x) {
      return x > 0 ? x : -x;
    }
    
    template <typename FLOAT_T>
    FLOAT_T sin(const FLOAT_T &x, const long double &EPS = fstdlib::EPS) {
      FLOAT_T res = 0, delt = x;
      int d = 0;
      while (fabs(delt) > EPS) {
        res += delt, ++d;
        delt *= -x * x / ((2 * d) * (2 * d + 1));
      }
      return res;
    }
    
    template <typename FLOAT_T>
    FLOAT_T cos(const FLOAT_T &x, const long double &EPS = fstdlib::EPS) {
      FLOAT_T res = 0, delt = 1;
      int d = 0;
      while (fabs(delt) > EPS) {
        res += delt, ++d;
        delt *= -x * x / ((2 * d) * (2 * d - 1));
      }
      return res;
    }
    
    const long double PI = std::acos((long double)(-1));
    
    void dft_for_complex(std::vector<comp> &f, int n, int b) {
      static std::vector<comp> w;
      w.resize(n);
      for (int i = 0; i < n; ++i)
        if (i < rev[i]) std::swap(f[i], f[rev[i]]);
      for (int i = 2; i <= n; i <<= 1) {
        w[0] = comp(1, 0), w[1] = comp(cos(2 * PI / i), b * sin(2 * PI / i));
        for (int j = 2; j < i / 2; ++j) w[j] = w[j - 1] * w[1];
        for (int j = 0; j < n; j += i)
          for (int k = 0; k < i / 2; ++k) {
            comp p = f[j + k], q = f[j + k + i / 2] * w[k];
            f[j + k] = p + q, f[j + k + i / 2] = p - q;
          }
      }
    }
    
    class arbitrary_module_poly {
     private:
      std::vector<int> data;
    
      int construct_element(int D, ll x, ll y, ll z) const {
        x %= mod, y %= mod, z %= mod;
        return ((ll)D * D * x % mod + (ll)D * y % mod + z) % mod;
      }
    
     public:
      int mod;
    
      arbitrary_module_poly(std::size_t len = std::size_t(0),
                            int module_value = 1e9 + 7) {
        mod = module_value;
        data = std::vector<int>(len);
      }
    
      arbitrary_module_poly(const std::vector<int> &b, int module_value = 1e9 + 7) {
        mod = module_value;
        data = b;
      }
    
      arbitrary_module_poly(const arbitrary_module_poly &b) {
        mod = b.mod;
        data = b.data;
      }
    
      void resize(std::size_t len, const int &val = 0) { data.resize(len, val); }
    
      std::size_t size(void) const { return data.size(); }
    
      void clear(void) { data.clear(); }
    #if __cplusplus >= 201103L
      void shrink_to_fit(void) { data.shrink_to_fit(); }
    #endif
      int &operator[](std::size_t b) { return data[b]; }
    
      const int &operator[](std::size_t b) const { return data[b]; }
    
      arbitrary_module_poly operator*(const arbitrary_module_poly &h) const;
      arbitrary_module_poly operator*=(const arbitrary_module_poly &h);
      arbitrary_module_poly operator*(const int &h) const;
      arbitrary_module_poly operator*=(const int &h);
      arbitrary_module_poly operator+(const arbitrary_module_poly &h) const;
      arbitrary_module_poly operator+=(const arbitrary_module_poly &h);
      arbitrary_module_poly operator-(const arbitrary_module_poly &h) const;
      arbitrary_module_poly operator-=(const arbitrary_module_poly &h);
      arbitrary_module_poly operator<<(const std::size_t &b) const;
      arbitrary_module_poly operator<<=(const std::size_t &b);
      arbitrary_module_poly operator>>(const std::size_t &b) const;
      arbitrary_module_poly operator>>=(const std::size_t &b);
      arbitrary_module_poly operator/(const int &h) const;
      arbitrary_module_poly operator/=(const int &h);
      arbitrary_module_poly operator==(const arbitrary_module_poly &h) const;
      arbitrary_module_poly operator!=(const arbitrary_module_poly &h) const;
      arbitrary_module_poly inv(void) const;
      arbitrary_module_poly inv(const int &h) const;
      friend arbitrary_module_poly sqrt(const arbitrary_module_poly &h);
      friend arbitrary_module_poly log(const arbitrary_module_poly &h);
    };
    
    arbitrary_module_poly arbitrary_module_poly::operator*(
        const arbitrary_module_poly &h) const {
      int N = 1;
      while (N < (int)(size() + h.size() - 1)) N <<= 1;
      std::vector<comp> f(N), g(N), p(N), q(N);
      const int D = std::sqrt(mod);
      for (int i = 0; i < (int)size(); ++i)
        f[i].x = data[i] / D, f[i].y = data[i] % D;
      for (int i = 0; i < (int)h.size(); ++i) g[i].x = h[i] / D, g[i].y = h[i] % D;
      rev.resize(N);
      for (int i = 0; i < N; ++i)
        rev[i] = (rev[i >> 1] >> 1) | (i & 1 ? N >> 1 : 0);
      dft_for_complex(f, N, 1), dft_for_complex(g, N, 1);
      for (int i = 0; i < N; ++i) {
        p[i] = (f[i] + f[(N - i) % N].conj()) * comp(0.50, 0) * g[i];
        q[i] = (f[i] - f[(N - i) % N].conj()) * comp(0, -0.5) * g[i];
      }
      dft_for_complex(p, N, -1), dft_for_complex(q, N, -1);
      std::vector<int> r(size() + h.size() - 1);
      for (int i = 0; i < (int)r.size(); ++i)
        r[i] = construct_element(D, p[i].x / N + 0.5, (p[i].y + q[i].x) / N + 0.5,
                                 q[i].y / N + 0.5);
      return arbitrary_module_poly(r, mod);
    }
    
    arbitrary_module_poly arbitrary_module_poly::operator*=(
        const arbitrary_module_poly &h) {
      return *this = *this * h;
    }
    
    arbitrary_module_poly arbitrary_module_poly::operator*(const int &h) const {
      std::vector<int> f(this->data);
      for (int i = 0; i < (int)f.size(); ++i) f[i] = (ll)f[i] * h % mod;
      return arbitrary_module_poly(f, mod);
    }
    
    arbitrary_module_poly arbitrary_module_poly::operator*=(const int &h) {
      for (int i = 0; i < (int)size(); ++i) data[i] = (ll)data[i] * h % mod;
      return *this;
    }
    
    arbitrary_module_poly arbitrary_module_poly::operator+(
        const arbitrary_module_poly &h) const {
      std::vector<int> f(this->data);
      if (f.size() < h.size()) f.resize(h.size());
      for (int i = 0; i < (int)h.size(); ++i) f[i] = (f[i] + h[i]) % mod;
      return arbitrary_module_poly(f, mod);
    }
    
    arbitrary_module_poly arbitrary_module_poly::operator+=(
        const arbitrary_module_poly &h) {
      if (size() < h.size()) resize(h.size());
      for (int i = 0; i < (int)h.size(); ++i) data[i] = (data[i] + h[i]) % mod;
      return *this;
    }
    
    arbitrary_module_poly arbitrary_module_poly::operator-(
        const arbitrary_module_poly &h) const {
      std::vector<int> f(this->data);
      if (f.size() < h.size()) f.resize(h.size());
      for (int i = 0; i < (int)h.size(); ++i) f[i] = (f[i] + mod - h[i]) % mod;
      return arbitrary_module_poly(f, mod);
    }
    
    arbitrary_module_poly arbitrary_module_poly::operator-=(
        const arbitrary_module_poly &h) {
      if (size() < h.size()) resize(h.size());
      for (int i = 0; i < (int)h.size(); ++i)
        data[i] = (data[i] + mod - h[i]) % mod;
      return *this;
    }
    
    arbitrary_module_poly arbitrary_module_poly::operator<<(
        const std::size_t &b) const {
      std::vector<int> f(size() + b);
      for (int i = 0; i < (int)size(); ++i) f[i + b] = data[i];
      return arbitrary_module_poly(f, mod);
    }
    
    arbitrary_module_poly arbitrary_module_poly::operator<<=(const std::size_t &b) {
      return *this = (*this) << b;
    }
    
    arbitrary_module_poly arbitrary_module_poly::operator>>(
        const std::size_t &b) const {
      std::vector<int> f(size() - b);
      for (int i = 0; i < (int)f.size(); ++i) f[i] = data[i + b];
      return arbitrary_module_poly(f, mod);
    }
    
    arbitrary_module_poly arbitrary_module_poly::operator>>=(const std::size_t &b) {
      return *this = (*this) >> b;
    }
    
    arbitrary_module_poly arbitrary_module_poly::inv(void) const {
      int N = 1;
      while (N < (int)(size() + size() - 1)) N <<= 1;
      arbitrary_module_poly f(1, mod), g(N, mod), h(*this), f2(1, mod);
      f[0] = qpow(data[0], mod - 2, mod), h.resize(N), f2[0] = 2;
      for (int w = 2; w < N; w <<= 1) {
        g.resize(w);
        for (int i = 0; i < w; ++i) g[i] = h[i];
        f = f * (f * g - f2) * (mod - 1);
        f.resize(w);
      }
      f.resize(size());
      return f;
    }
    
    arbitrary_module_poly arbitrary_module_poly::inv(const int &h) const {
      arbitrary_module_poly f(*this);
      f.resize(h);
      return f.inv();
    }
    
    arbitrary_module_poly arbitrary_module_poly::operator/(const int &h) const {
      int inv = qpow(h, mod - 2, mod);
      std::vector<int> f(this->data);
      for (int i = 0; i < (int)f.size(); ++i) f[i] = (ll)f[i] * inv % mod;
      return arbitrary_module_poly(f, mod);
    }
    
    arbitrary_module_poly arbitrary_module_poly::operator/=(const int &h) {
      int inv = qpow(h, mod - 2, mod);
      for (int i = 0; i < (int)size(); ++i) data[i] = (ll)data[i] * inv % mod;
      return *this;
    }
    
    arbitrary_module_poly arbitrary_module_poly::operator==(
        const arbitrary_module_poly &h) const {
      if (size() != h.size() || mod != h.mod) return 0;
      for (int i = 0; i < (int)size(); ++i)
        if (data[i] != h[i]) return 0;
      return 1;
    }
    
    arbitrary_module_poly arbitrary_module_poly::operator!=(
        const arbitrary_module_poly &h) const {
      if (size() != h.size() || mod != h.mod) return 1;
      for (int i = 0; i < (int)size(); ++i)
        if (data[i] != h[i]) return 1;
      return 0;
    }
    
    arbitrary_module_poly sqrt(const arbitrary_module_poly &h) {
      int N = 1;
      while (N < (int)(h.size() + h.size() - 1)) N <<= 1;
      arbitrary_module_poly f(1, mod), g(N, mod), d(h);
      f[0] = modsqrt(h[0], mod), d.resize(N);
      for (int w = 2; w < N; w <<= 1) {
        g.resize(w);
        for (int i = 0; i < w; ++i) g[i] = d[i];
        f = (f + f.inv(w) * g) / 2;
        f.resize(w);
      }
      f.resize(h.size());
      return f;
    }
    
    arbitrary_module_poly log(const arbitrary_module_poly &h) {
      arbitrary_module_poly f(h);
      for (int i = 1; i < (int)f.size(); ++i) f[i - 1] = (ll)f[i] * i % f.mod;
      f[f.size() - 1] = 0, f = f * h.inv(), f.resize(h.size());
      for (int i = (int)f.size() - 1; i > 0; --i)
        f[i] = (ll)f[i - 1] * qpow(i, f.mod - 2, f.mod) % f.mod;
      f[0] = 0;
      return f;
    }
    
    using m_poly = arbitrary_module_poly;
    }  // namespace fstdlib
    
    #endif
    ```

??? note "Implementation"
    ```cpp
    int main() {
      scanf("%d", &n);
      fact[0] = 1;
      for (int i = 1; i <= n; ++i) fact[i] = (ll)fact[i - 1] * i % mod;
      exgcd(fact[n], mod, ifact[n], ifact[0]),
          ifact[n] = (ifact[n] % mod + mod) % mod;
      for (int i = n - 1; i >= 0; --i) ifact[i] = (ll)ifact[i + 1] * (i + 1) % mod;
      poly f(n + 1), g(n + 1);
      for (int i = 0; i <= n; ++i)
        g[i] = (i & 1 ? mod - 1ll : 1ll) * ifact[i] % mod,
        f[i] = (ll)qpow(i, n) * ifact[i] % mod;
      f *= g, f.resize(n + 1);
      for (int i = 0; i <= n; ++i) printf("%d ", f[i]);
      return 0;
    }
    ```

### Computing Stirling numbers of the second kind in the same column

"Same column" Stirling numbers of the second kind refers to a series of $\begin{Bmatrix}i\\k\end{Bmatrix}$ with different $i$ and the same $k$. Finding all Stirling numbers of the second kind in the same column means finding, for $i=0..n$, the number of ways to partition $i$ distinct elements into $k$ non-empty sets.

Compute using the exponential generating function.

The number of ways for one box to hold $i$ items with the box non-empty is $[i>0]$. We can write its exponential generating function as $F(x)=\sum\limits_{i=1}^{+\infty}\dfrac{x^i}{i!} = \mathrm{e}^x-1$. From the earlier study, we understand that $F^k(x)$ is the exponential generating function of placing $i$ labeled items into $k$ labeled boxes, so dividing out $k!$ gives the exponential generating function of placing $i$ labeled items into $k$ unlabeled boxes.

$\begin{Bmatrix}i\\k\end{Bmatrix}=\dfrac{\left[\dfrac{x^i}{i!}\right]F^k(x)}{k!}$; just compute the polynomial power in $O(n\log n)$.

In addition, $\exp F(x)=\sum\limits_{i=0}^{+\infty}\dfrac{F^i(x)}{i!}$ is the exponential generating function of placing $i$ labeled items into any number of unlabeled boxes (EXP removes the labels of the boxes by dividing each term by an $i!$). This is in fact the generating function of the Bell numbers.

This involves a lot of "labeled" and "unlabeled" content; take care to distinguish them.

??? note "Implementation"
    ```cpp
    int main() {
      scanf("%d%d", &n, &k);
      poly f(n + 1);
      fact[0] = 1;
      for (int i = 1; i <= n; ++i) fact[i] = (ll)fact[i - 1] * i % mod;
      for (int i = 1; i <= n; ++i) f[i] = qpow(fact[i], mod - 2);
      f = exp(log(f >> 1) * k) << k, f.resize(n + 1);
      int inv = qpow(fact[k], mod - 2);
      for (int i = 0; i <= n; ++i)
        printf("%lld ", (ll)f[i] * fact[i] % mod * inv % mod);
      return 0;
    }
    ```

## Stirling numbers of the first kind (Stirling number)

The **Stirling number of the first kind** (Stirling cycle number) $\begin{bmatrix}n\\ k\end{bmatrix}$, also denoted $s(n,k)$, represents the number of ways to partition $n$ pairwise distinct elements into $k$ mutually indistinguishable non-empty cycles.

A cycle is a circular arrangement joined head to tail. We can write a cycle $[A,B,C,D]$, and we consider $[A,B,C,D]=[B,C,D,A]=[C,D,A,B]=[D,A,B,C]$, i.e. two cycles that can be obtained from each other by rotation are equivalent. Note that we do not consider two cycles that can be obtained from each other by reflection to be equivalent, i.e. $[A,B,C,D]\neq[D,C,B,A]$.

### Recurrence

$$
\begin{bmatrix}n\\ k\end{bmatrix}=\begin{bmatrix}n-1\\ k-1\end{bmatrix}+(n-1)\begin{bmatrix}n-1\\ k\end{bmatrix}
$$

The boundary is $\begin{bmatrix}n\\ 0\end{bmatrix}=[n=0]$.

The proof of this recurrence can consider its combinatorial meaning.

When we insert a new element, there are two schemes:

-   place this new element in a cycle by itself, giving $\begin{bmatrix}n-1\\ k-1\end{bmatrix}$ schemes;
-   insert this element into any one of the existing cycles, giving $(n-1)\begin{bmatrix}n-1\\ k\end{bmatrix}$ schemes.

By the addition principle, adding the two gives the recurrence.

### General term formula

Stirling numbers of the first kind have no practical general term formula.

### Computing Stirling numbers of the first kind in the same row

Similar to Stirling numbers of the second kind, we construct the generating function of same-row Stirling numbers of the first kind, i.e.

$F_n(x)=\sum\limits_{i=0}^n\begin{bmatrix}n\\i\end{bmatrix}x^i$

According to the recurrence, it is not hard to write

$F_n(x)=(n-1)F_{n-1}(x)+xF_{n-1}(x)$

Thus

$F_n(x)=\prod\limits_{i=0}^{n-1}(x+i)=\dfrac{(x+n-1)!}{(x-1)!}$

This is in fact the rising factorial power of degree $n$ of $x$, denoted $x^{\overline n}$. This can naturally be found by brute-force divide-and-conquer multiplication in $O(n\log^2n)$, but using rising-power-related approaches one can find it in $O(n\log n)$; for details see [polynomial shift | continuous point-value shift](../poly/shift.md#同一行第一类无符号-stirling-数).

### Computing Stirling numbers of the first kind in the same column

Following the computation of Stirling numbers of the second kind, we can solve this problem using the exponential generating function. Note that since the recurrence is related to the row, we cannot use the recurrence to compute same-column Stirling numbers of the first kind.

Obviously, the exponential generating function of a single cycle is

$F(x)=\sum\limits_{i=1}^n\dfrac{(i-1)!x^i}{i!}=\sum\limits_{i=1}^n\dfrac{x^i}{i}$

Its $k$-th power is the exponential generating function of $\begin{bmatrix}i\\k\end{bmatrix}$; just compute in $O(n\log n)$.

??? note "Implementation"
    ```cpp
    int main() {
      scanf("%d%d", &n, &k);
      fact[0] = 1;
      for (int i = 1; i <= n; ++i) fact[i] = (ll)fact[i - 1] * i % mod;
      ifact[n] = qpow(fact[n], mod - 2);
      for (int i = n - 1; i >= 0; --i) ifact[i] = (ll)ifact[i + 1] * (i + 1) % mod;
      poly f(n + 1);
      for (int i = 1; i <= n; ++i) f[i] = (ll)fact[i - 1] * ifact[i] % mod;
      f = exp(log(f >> 1) * k) << k, f.resize(n + 1);
      for (int i = 0; i <= n; ++i)
        printf("%lld ", (ll)f[i] * fact[i] % mod * ifact[k] % mod);
      return 0;
    }
    ```

## Applications

### Mutual conversion between rising powers and ordinary powers

We denote the rising factorial power $x^{\overline{n}}=\prod_{k=0}^{n-1} (x+k)$.

Then one can use the following identity to convert rising powers into ordinary powers:

$$
x^{\overline{n}}=\sum_{k} \begin{bmatrix}n\\ k\end{bmatrix} x^k
$$

To convert ordinary powers into rising powers, we have the following identity:

$$
x^n=\sum_{k} \begin{Bmatrix}n\\ k\end{Bmatrix} (-1)^{n-k} x^{\overline{k}}
$$

### Mutual conversion between falling powers and ordinary powers

We denote the falling factorial power $x^{\underline{n}}=\dfrac{x!}{(x-n)!}=\prod_{k=0}^{n-1} (x-k)$.

Then one can use the following identity to convert ordinary powers into falling powers:

$$
x^n=\sum_{k} \begin{Bmatrix}n\\ k\end{Bmatrix} x^{\underline{k}}
$$

To convert falling powers into ordinary powers, we have the following identity:

$$
x^{\underline{n}}=\sum_{k} \begin{bmatrix}n\\ k\end{bmatrix} (-1)^{n-k} x^k
$$

### Relationship between the falling-factorial-power representation and the point-value representation of a polynomial

Here, the falling-factorial-power representation of a polynomial is representing a polynomial in the form

$$
f(x)=\sum\limits_{i=0}^nb_i{x^{\underline{i}}}
$$

while the point-value representation is representing a polynomial using $n+1$ points

$$
(i,a_i),i=0..n
$$

Obviously, the falling factorial powers $b$ and the point values $a$ satisfy such a relationship:

$$
a_k=\sum\limits_{i=0}^{n}b_ik^{\underline{i}}
$$

That is

$$
\begin{aligned}
a_k&=\sum\limits_{i=0}^{n}\dfrac{b_ik!}{(k-i)!}\\\dfrac{a_k}{k!}&=\sum\limits_{i=0}^kb_i\dfrac{1}{(k-i)!}
\end{aligned}
$$

This is a convolution-form expression; we can complete the mutual conversion between point values and falling factorial powers in $O(n\log n)$ time complexity.

## Exercises

-   [HDU3625 Examining the Rooms](https://acm.hdu.edu.cn/showproblem.php?pid=3625)
-   [UOJ540 联合省选 2020 组合数问题](https://uoj.ac/problem/540)
-   [UOJ269 清华集训 2016 如何优雅地求和](https://uoj.ac/problem/269)

## References and notes

1.  [Stirling Number of the First Kind - Wolfram MathWorld](http://mathworld.wolfram.com/StirlingNumberoftheFirstKind.html)
2.  [Stirling Number of the Second Kind - Wolfram MathWorld](http://mathworld.wolfram.com/StirlingNumberoftheSecondKind.html)
