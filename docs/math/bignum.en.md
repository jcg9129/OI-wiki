> Too long, didn't read version: grab the template at the end……

## Definition

Arbitrary-Precision Arithmetic, also called big-number (bignum) computation, uses some algorithmic structures to support operations between larger integers (numbers whose size exceeds the language's built-in integer types).

## Introduction

Big-number problems contain many small details, and there is much to be careful about in the implementation.

So today let's implement a simple calculator together.

???+ note "Task"
    Input: an expression of the form `a <op> b`.
    
    -   `a` and `b` are respectively decimal non-negative integers of length no more than $1000$;
    -   `<op>` is a single character (`+`, `-`, `*`, or `/`), denoting the operation.
    -   The integers and the operator are separated by a single space.
    
    Output: the result of the operation.
    
    -   For the `+`, `-`, `*` operations, output one line representing the result;
    -   For the `/` operation, output two lines representing the quotient and the remainder respectively.
    -   It is guaranteed that all results are non-negative integers.

## Storage

In a typical implementation, big numbers are represented using a string, where each character represents one decimal digit of the number. Therefore one can say that big-number computation is actually a special kind of string processing.

When reading in the string, the most significant digit of the number is at the front of the string (the position with a small index). But by convention, the position with the smallest index holds the **least significant digit** of the number, i.e. we store the reversed string. The reason for doing so is that the length of the number may change, but we want the positions of equal place value to always stay aligned (for example, we want all ones digits to be at index `[0]`, all tens digits at index `[1]`……); at the same time, addition, subtraction, and multiplication generally proceed starting from the ones digit (recall the column arithmetic from elementary school), all of which give ample reason for "reversed storage".

Hereafter we will continue to follow this convention. Define a constant `LEN = 1004` representing the maximum length the program can accommodate.

From this it is not hard to write the code for reading in a big number:

```cpp
void clear(int a[]) {
  for (int i = 0; i < LEN; ++i) a[i] = 0;
}

void read(int a[]) {
  static char s[LEN + 1];
  scanf("%s", s);

  clear(a);

  int len = strlen(s);
  // As described above, reverse
  for (int i = 0; i < len; ++i) a[len - i - 1] = s[i] - '0';
  // s[i] - '0' is the digit represented by s[i]
  // Some readers may be more used to understanding it as ord(s[i]) - ord('0')
}
```

Output is also produced in the reverse order of storage. Since we do not want to output leading zeros, here we search downward from the most significant digit for the first nonzero digit and start outputting from there; the termination condition is `i >= 1` rather than `i >= 0` because when the whole number equals $0$ we still want to output one character `0`.

```cpp
void print(int a[]) {
  int i;
  for (i = LEN - 1; i >= 1; --i)
    if (a[i] != 0) break;
  for (; i >= 0; --i) putchar(a[i] + '0');
  putchar('\n');
}
```

Putting them together gives a complete echo program.

??? note "`copycat.cpp`"
    ```cpp
    #include <cstdio>
    #include <cstring>
    
    constexpr int LEN = 1004;
    
    int a[LEN];
    
    void clear(int a[]) {
      for (int i = 0; i < LEN; ++i) a[i] = 0;
    }
    
    void read(int a[]) {
      static char s[LEN + 1];
      scanf("%s", s);
    
      clear(a);
    
      int len = strlen(s);
      for (int i = 0; i < len; ++i) a[len - i - 1] = s[i] - '0';
    }
    
    void print(int a[]) {
      int i;
      for (i = LEN - 1; i >= 1; --i)
        if (a[i] != 0) break;
      for (; i >= 0; --i) putchar(a[i] + '0');
      putchar('\n');
    }
    
    int main() {
      read(a);
      print(a);
    
      return 0;
    }
    ```

## The four arithmetic operations

The four arithmetic operations also vary in difficulty. The simplest is big-number addition and subtraction, followed by big-number–single-precision (ordinary `int`) multiplication and big-number–big-number multiplication, and finally big-number–big-number division.

We will implement all the required functionalities in this order.

### Addition

Big-number addition is really just column addition.

![](./images/plus.svg)

That is, starting from the least significant digit, add the digits at the corresponding positions of the two addends, and check whether they reach or exceed $10$. If they do, handle the carry: increase the result at the next higher position by $1$, and decrease the result at the current position by $10$.

```cpp
void add(int a[], int b[], int c[]) {
  clear(c);

  // In big-number implementations, the array's maximum length LEN is generally
  // made a bit larger than the possible input
  // and then the last few iterations are omitted, which saves handling of quite
  // a few boundary cases
  // Because the actual input does not exceed 1000 digits, looping to LEN - 1 =
  // 1003 here is already sufficient
  for (int i = 0; i < LEN - 1; ++i) {
    // Add the digits at the corresponding positions
    c[i] += a[i] + b[i];
    if (c[i] >= 10) {
      // Carry
      c[i + 1] += 1;
      c[i] -= 10;
    }
  }
}
```

Combining this with the previous part, we can obtain an addition calculator.

??? note "`adder.cpp`"
    ```cpp
    #include <cstdio>
    #include <cstring>
    
    constexpr int LEN = 1004;
    
    int a[LEN], b[LEN], c[LEN];
    
    void clear(int a[]) {
      for (int i = 0; i < LEN; ++i) a[i] = 0;
    }
    
    void read(int a[]) {
      static char s[LEN + 1];
      scanf("%s", s);
    
      clear(a);
    
      int len = strlen(s);
      for (int i = 0; i < len; ++i) a[len - i - 1] = s[i] - '0';
    }
    
    void print(int a[]) {
      int i;
      for (i = LEN - 1; i >= 1; --i)
        if (a[i] != 0) break;
      for (; i >= 0; --i) putchar(a[i] + '0');
      putchar('\n');
    }
    
    void add(int a[], int b[], int c[]) {
      clear(c);
    
      for (int i = 0; i < LEN - 1; ++i) {
        c[i] += a[i] + b[i];
        if (c[i] >= 10) {
          c[i + 1] += 1;
          c[i] -= 10;
        }
      }
    }
    
    int main() {
      read(a);
      read(b);
    
      add(a, b, c);
      print(c);
    
      return 0;
    }
    ```

### Subtraction

Big-number subtraction is column subtraction.

![](./images/subtraction.svg)

Subtract digit by digit starting from the ones digit; when a negative case is encountered, borrow $1$ from the next higher position. The overall idea is exactly the same as addition.

```cpp
void sub(int a[], int b[], int c[]) {
  clear(c);

  for (int i = 0; i < LEN - 1; ++i) {
    // Subtract digit by digit
    c[i] += a[i] - b[i];
    if (c[i] < 0) {
      // Borrow
      c[i + 1] -= 1;
      c[i] += 10;
    }
  }
}
```

Replacing `add()` in the previous program with `sub()` gives a subtraction calculator.

??? note "`subtractor.cpp`"
    ```cpp
    #include <cstdio>
    #include <cstring>
    
    constexpr int LEN = 1004;
    
    int a[LEN], b[LEN], c[LEN];
    
    void clear(int a[]) {
      for (int i = 0; i < LEN; ++i) a[i] = 0;
    }
    
    void read(int a[]) {
      static char s[LEN + 1];
      scanf("%s", s);
    
      clear(a);
    
      int len = strlen(s);
      for (int i = 0; i < len; ++i) a[len - i - 1] = s[i] - '0';
    }
    
    void print(int a[]) {
      int i;
      for (i = LEN - 1; i >= 1; --i)
        if (a[i] != 0) break;
      for (; i >= 0; --i) putchar(a[i] + '0');
      putchar('\n');
    }
    
    void sub(int a[], int b[], int c[]) {
      clear(c);
    
      for (int i = 0; i < LEN - 1; ++i) {
        c[i] += a[i] - b[i];
        if (c[i] < 0) {
          c[i + 1] -= 1;
          c[i] += 10;
        }
      }
    }
    
    int main() {
      read(a);
      read(b);
    
      sub(a, b, c);
      print(c);
    
      return 0;
    }
    ```

Give it a try: input `1 2`——it outputs `/9999999`. Huh, how did this **OI Wiki** give me a broken piece of code……

In fact, the above code can only handle the case where the minuend $a$ is greater than or equal to the subtrahend $b$. Handling the case where the minuend is smaller than the subtrahend, i.e. $a<b$, is very simple.

$a-b=-(b-a)$

To compute the value of $b-a$, since $b>a$, we can call the `sub` function in the above code, written as `sub(b,a,c)`. To obtain the value of $a-b$, just prepend a minus sign to the result.

### Multiplication

#### Big-number–single-precision

Big-number multiplication is really just col……wait, wait a moment!

Let us first consider a simple case: one of the multipliers is an ordinary `int`. Is there a simple way to handle it?

An intuitive idea is to directly multiply each digit of $a$ by $b$. Numerically, this method is correct, but it does not conform to decimal notation, so it needs to be rearranged back into normal form.

The way to rearrange is also to handle carries digit by digit upward starting from the ones digit. But the carry here may be very large, even far larger than $9$, because each digit, after being multiplied, may reach the order of $9b$. So the carry here can no longer simply be handled with a $-10$ operation, but must be computed via the quotient and remainder of division by $10$. See the code comments for details; you may also refer to the figure below showing the process of computing the big number $1337$ times the single-precision number $42$.

![](./images/multiplication-short.png)

Of course, also for this reason, this method requires special attention to the range of the multiplier $b$. If it is of the same order of magnitude as $10^9$ (or the upper bound of the corresponding integer type), then big-number–single-precision multiplication should be used with caution.

```cpp
void mul_short(int a[], int b, int c[]) {
  clear(c);

  for (int i = 0; i < LEN - 1; ++i) {
    // Directly multiply the i-th digit of a by the multiplier and add to the
    // result
    c[i] += a[i] * b;

    if (c[i] >= 10) {
      // Handle the carry
      // c[i] / 10, the quotient of the division, becomes the increment for the
      // carry
      c[i + 1] += c[i] / 10;
      // while c[i] % 10, the remainder of the division, becomes the value left
      // in the current position
      c[i] %= 10;
    }
  }
}
```

#### Big-number–big-number

If both multipliers are big numbers, then column multiplication can once again show its power.

Recall that each step of column multiplication actually computes the sum of several $a \times b_i \times 10^i$. For example, computing $1337 \times 42$ computes $1337 \times 2 \times 10^0 + 1337 \times 4 \times 10^1$.

So we can decompose $b$ into all its digits, each of which is a single-precision number, multiply them respectively with $a$, then shift them left to their respective positions and add them to get the answer. Of course, at the end we also need to handle the carry in the same way as in the previous example.

![](./images/multiplication-long.png)

Note that this process is not entirely the same as column multiplication: our algorithm does not carry during each multiplication step, but keeps all the results at the corresponding positions, and handles the carries all at once at the very end, but this does not affect the result.

```cpp
void mul(int a[], int b[], int c[]) {
  clear(c);

  for (int i = 0; i < LEN - 1; ++i) {
    // Here we directly compute the i-th position (from low to high) of the
    // result, and handle the carry along the way
    // The i-th iteration adds to c[i] the sum of all products of a[p] and b[q]
    // with p + q = i
    // The effect is the same as directly performing the operation in the figure
    // above and summing at the end, just a more concise implementation
    for (int j = 0; j <= i; ++j) c[i] += a[j] * b[i - j];

    if (c[i] >= 10) {
      c[i + 1] += c[i] / 10;
      c[i] %= 10;
    }
  }
}
```

### Division

One way to implement big-number division is column long division.

![](./images/division.svg)

Column long division can actually be regarded as a process of successive subtraction. For example, the computation of the tens digit of the quotient in the figure above can be understood this way: after subtracting $12$ three times from $45$, it becomes less than $12$ and can no longer be subtracted, so this digit is $3$.

To reduce redundant computation, we obtain in advance the length $l_a$ of the dividend and the length $l_b$ of the divisor, and compute the quotient starting from index $l_a - l_b$, from high position to low position. This is the same as the practice of aligning the most significant digit of the first multiplication with the most significant digit of the dividend when computing by hand.

The reference program implements a function `greater_eq()` used to determine whether the dividend, with index `last_dg` as its least significant position, can have the divisor subtracted from it once more while remaining non-negative. Thereafter, for each digit of the quotient, it repeatedly calls `greater_eq()`, and when it holds, uses big-number subtraction to subtract the divisor from the remainder, thereby simulating the process of column division.

```cpp
// With the dividend a having index last_dg as its least significant position,
// can the divisor b be subtracted once more while remaining non-negative
// len is the length of the divisor b, to avoid repeated computation
bool greater_eq(int a[], int b[], int last_dg, int len) {
  // The remaining part of the dividend may be longer than the divisor; in this
  // case it is at most 1 digit longer, so this check suffices
  if (a[last_dg + len] != 0) return true;
  // Compare digit by digit from high to low
  for (int i = len - 1; i >= 0; --i) {
    if (a[last_dg + i] > b[i]) return true;
    if (a[last_dg + i] < b[i]) return false;
  }
  // The equal case is also feasible
  return true;
}

void div(int a[], int b[], int c[], int d[]) {
  clear(c);
  clear(d);

  int la, lb;
  for (la = LEN - 1; la > 0; --la)
    if (a[la - 1] != 0) break;
  for (lb = LEN - 1; lb > 0; --lb)
    if (b[lb - 1] != 0) break;
  if (lb == 0) {  // The divisor cannot be zero
    puts("> <");
    return;
  }

  // c is the quotient
  // d is the remaining part of the dividend, which naturally becomes the
  // remainder after the algorithm ends
  for (int i = 0; i < la; ++i) d[i] = a[i];
  for (int i = la - lb; i >= 0; --i) {
    // Compute the i-th digit of the quotient
    while (greater_eq(d, b, i, lb)) {
      // If it can be subtracted, subtract
      // This section is a big-number subtraction
      for (int j = 0; j < lb; ++j) {
        d[i + j] -= b[j];
        if (d[i + j] < 0) {
          d[i + j + 1] -= 1;
          d[i + j] += 10;
        }
      }
      // Increment this digit of the quotient by 1
      c[i] += 1;
      // Return to the beginning of the loop and check again
    }
  }
}
```

## The introductory part is complete!

Combining the implementations of the four arithmetic operations introduced above completes the calculator program mentioned at the beginning.

??? note "`calculator.cpp`"
    ```cpp
    #include <cstdio>
    #include <cstring>
    
    constexpr int LEN = 1004;
    
    int a[LEN], b[LEN], c[LEN], d[LEN];
    
    void clear(int a[]) {
      for (int i = 0; i < LEN; ++i) a[i] = 0;
    }
    
    void read(int a[]) {
      static char s[LEN + 1];
      scanf("%s", s);
    
      clear(a);
    
      int len = strlen(s);
      for (int i = 0; i < len; ++i) a[len - i - 1] = s[i] - '0';
    }
    
    void print(int a[]) {
      int i;
      for (i = LEN - 1; i >= 1; --i)
        if (a[i] != 0) break;
      for (; i >= 0; --i) putchar(a[i] + '0');
      putchar('\n');
    }
    
    void add(int a[], int b[], int c[]) {
      clear(c);
    
      for (int i = 0; i < LEN - 1; ++i) {
        c[i] += a[i] + b[i];
        if (c[i] >= 10) {
          c[i + 1] += 1;
          c[i] -= 10;
        }
      }
    }
    
    void sub(int a[], int b[], int c[]) {
      clear(c);
    
      for (int i = 0; i < LEN - 1; ++i) {
        c[i] += a[i] - b[i];
        if (c[i] < 0) {
          c[i + 1] -= 1;
          c[i] += 10;
        }
      }
    }
    
    void mul(int a[], int b[], int c[]) {
      clear(c);
    
      for (int i = 0; i < LEN - 1; ++i) {
        for (int j = 0; j <= i; ++j) c[i] += a[j] * b[i - j];
    
        if (c[i] >= 10) {
          c[i + 1] += c[i] / 10;
          c[i] %= 10;
        }
      }
    }
    
    bool greater_eq(int a[], int b[], int last_dg, int len) {
      if (a[last_dg + len] != 0) return true;
      for (int i = len - 1; i >= 0; --i) {
        if (a[last_dg + i] > b[i]) return true;
        if (a[last_dg + i] < b[i]) return false;
      }
      return true;
    }
    
    void div(int a[], int b[], int c[], int d[]) {
      clear(c);
      clear(d);
    
      int la, lb;
      for (la = LEN - 1; la > 0; --la)
        if (a[la - 1] != 0) break;
      for (lb = LEN - 1; lb > 0; --lb)
        if (b[lb - 1] != 0) break;
      if (lb == 0) {
        puts("> <");
        return;
      }
    
      for (int i = 0; i < la; ++i) d[i] = a[i];
      for (int i = la - lb; i >= 0; --i) {
        while (greater_eq(d, b, i, lb)) {
          for (int j = 0; j < lb; ++j) {
            d[i + j] -= b[j];
            if (d[i + j] < 0) {
              d[i + j + 1] -= 1;
              d[i + j] += 10;
            }
          }
          c[i] += 1;
        }
      }
    }
    
    int main() {
      read(a);
    
      char op[4];
      scanf("%s", op);
    
      read(b);
    
      switch (op[0]) {
        case '+':
          add(a, b, c);
          print(c);
          break;
        case '-':
          sub(a, b, c);
          print(c);
          break;
        case '*':
          mul(a, b, c);
          print(c);
          break;
        case '/':
          div(a, b, c, d);
          print(c);
          print(d);
          break;
        default:
          puts("> <");
      }
    
      return 0;
    }
    ```

## Digit-compressed big numbers

### Introduction

In ordinary big-number addition, subtraction, and multiplication, we always split the numbers participating in the operation into individual digits before operating.

For example, when computing $8192\times 42$, if following the big-number-times-big-number method, what we actually compute is $(8000+100+90+2)\times(40+2)$.

When there are many digits, the numbers split out are also many, and the efficiency of big-number operations drops.

Is there a way to make some optimizations?

Note that the way of splitting the number does not affect the final result, so we can merge several digits together.

### Procedure

Still taking the above example, if we split off one number every two digits, we can split it into $(8100+92)\times 42$.

This kind of splitting does not affect the final result, but because fewer numbers are split out, the computational efficiency is improved.

Understanding this process from the perspective of [numeral systems](./numeral-sys/base.md), we operate in a larger base (splitting off one number every two digits above can be regarded as operating in base $100$), thereby reducing the number of digits participating in the operation and improving efficiency.

This is the idea of **digit-compressed big numbers**.

Below we give the addition code for digit-compressed big numbers, to further illustrate the implementation method:

??? note "Reference implementation of digit-compressed big-number addition"
    ```cpp
    // Here the arrays a, b, c are all numbers in base p
    // When finally outputting the answer, the number needs to be converted to
    // decimal
    void add(int a[], int b[], int c[]) {
      clear(c);
    
      for (int i = 0; i < LEN - 1; ++i) {
        c[i] += a[i] + b[i];
        if (c[i] >= p) {  // In ordinary big-number arithmetic, p=10
          c[i + 1] += 1;
          c[i] -= p;
        }
      }
    }
    ```

### Efficient column division under digit compression

When using digit compression, if the trial-quotient still uses the method introduced above, since the number of trials will be many, the computational constant will be very large. For example, in base ten-thousand, each digit needs on average 5000 trial-quotients, and this huge constant is unacceptable. Therefore we need a more efficient trial-quotient method.

We can use `double` as a medium. Suppose the dividend has 4 digits, which are $a_4,a_3,a_2,a_1$, and the divisor has 3 digits, which are $b_3,b_2,b_1$; then we only need to trial one digit of the quotient: using base $base$, estimate the quotient with the expression $\dfrac{a_4 base + a_3}{b_3 + b_2 base^{-1} + (b_1+1)base^{-2}}$. And for the case of multiple digits, it is just the single-digit approach plus a loop. Since the divisor uses 3 digits of precision to participate in the estimation, it can be guaranteed that the relationship between the estimated quotient q' and the actual quotient q satisfies $q-1 \le q' \le q$, so each digit needs at most two trial-quotients even in the worst case. But at the same time it requires $base^3$ to be within the effective precision of `double`, i.e. $base^3 < 2^{53}$, so when using this method it is recommended not to exceed base 32768, otherwise errors are easily produced due to insufficient precision, leading to incorrect results.

In addition, since the estimated quotient is always less than or equal to the actual quotient, there is room for further optimization. In the vast majority of cases each digit is estimated only once; this way, when estimating the quotient for the next digit, although the obtained quotient may cause the trial result to be greater than or equal to base due to the error of the previous digit, this does not matter—as long as the carries are handled uniformly at the end. For example, suppose base is 10 and we compute $395081/9876$; the trial-quotient computation steps are as follows:

1.  First the trial-quotient gives $3950/988=3$, so $395081-(9876 \times 3 \times 10^1) = 98801$; an error occurs at this step, but ignore it and continue to the next step.
2.  Continue the trial-quotient computation on the remainder 98801, giving $9880/988=10$, so $98801-(9876 \times 10 \times 10^0) = 41$, which is the final remainder.
3.  Add up the results of the trial-quotient process and handle the carries, i.e. $3 \times 10^1 + 10 \times 10^0 = 40$ is the exact quotient.

Although the method looks simple, it is easy to fall into pitfalls in the concrete implementation, so below we provide an implementation that has been verified many times to be correct, for reference; the details to note are also written in the comments.

??? note "Reference implementation of efficient column division for digit-compressed big numbers"
    ```cpp
    // Full template and implementation https://baobaobear.github.io/post/20210228-bigint1/
    // Subtract the result of multiplying b by mul and left-shifting by offset;
    // serves the division
    BigIntSimple &sub_mul(const BigIntSimple &b, int mul, int offset) {
      if (mul == 0) return *this;
      int borrow = 0;
      // Unlike subtraction, borrow may be large, so the subtraction style cannot
      // be used
      for (size_t i = 0; i < b.v.size(); ++i) {
        borrow += v[i + offset] - b.v[i] * mul - BIGINT_BASE + 1;
        v[i + offset] = borrow % BIGINT_BASE + BIGINT_BASE - 1;
        borrow /= BIGINT_BASE;
      }
      // If there is still a borrow, continue processing
      for (size_t i = b.v.size(); borrow; ++i) {
        borrow += v[i + offset] - BIGINT_BASE + 1;
        v[i + offset] = borrow % BIGINT_BASE + BIGINT_BASE - 1;
        borrow /= BIGINT_BASE;
      }
      return *this;
    }
    
    BigIntSimple div_mod(const BigIntSimple &b, BigIntSimple &r) const {
      BigIntSimple d;
      r = *this;
      if (absless(b)) return d;
      d.v.resize(v.size() - b.v.size() + 1);
      // Precompute the reciprocal of (the top three digits of the divisor + 1);
      // if the top three digits are a3, a2, a1
      // then db is the reciprocal of a3 + a2/base + (a1+1)/base^2, finally used
      // to estimate each digit of the quotient by multiplication
      // This method can be used within the int32 range when BIGINT_BASE<=32768
      // but even using int64, it is only usable when BIGINT_BASE<=131072
      // (limited by the precision of double)
      // It guarantees that the estimated result q' and the actual result q
      // satisfy q'<=q<=q'+1
      // so each digit needs only one trial-quotient on average, as long as the
      // carries are handled uniformly afterward
      // If a larger base is to be used, another trial-quotient scheme is needed
      double t = (b.get((unsigned)b.v.size() - 2) +
                  (b.get((unsigned)b.v.size() - 3) + 1.0) / BIGINT_BASE);
      double db = 1.0 / (b.v.back() + t / BIGINT_BASE);
      for (size_t i = v.size() - 1, j = d.v.size() - 1; j <= v.size();) {
        int rm = r.get(i + 1) * BIGINT_BASE + r.get(i);
        int m = std::max((int)(db * rm), r.get(i + 1));
        r.sub_mul(b, m, j);
        d.v[j] += m;
        if (!r.get(i + 1))  // Check whether the most significant digit is
                            // already 0, to avoid extreme cases
          --i, --j;
      }
      r.trim();
      // Correct the ones place of the result
      int carry = 0;
      while (!r.absless(b)) {
        r.subtract(b);
        ++carry;
      }
      // Correct the carry of each digit
      for (size_t i = 0; i < d.v.size(); ++i) {
        carry += d.v[i];
        d.v[i] = carry % BIGINT_BASE;
        carry /= BIGINT_BASE;
      }
      d.trim();
      d.sign = sign * b.sign;
      return d;
    }
    
    BigIntSimple operator/(const BigIntSimple &b) const {
      BigIntSimple r;
      return div_mod(b, r);
    }
    
    BigIntSimple operator%(const BigIntSimple &b) const {
      BigIntSimple r;
      div_mod(b, r);
      return r;
    }
    ```

## Karatsuba multiplication

Let the number of digits of the big numbers be $n$; then big-number–big-number column multiplication takes $O(n^2)$ time. This section introduces an algorithm with a better time complexity, proposed by the former Soviet (Russian) mathematician Anatoly Karatsuba, a divide-and-conquer algorithm.

Consider two large decimal integers $x$ and $y$, each containing $n$ digits (leading zeros allowed). Take any $0 < m < n$, and write

$$
\begin{aligned}
x &= x_1 \cdot 10^m + x_0, \\
y &= y_1 \cdot 10^m + y_0, \\
x \cdot y &= z_2 \cdot 10^{2m} + z_1 \cdot 10^m + z_0,
\end{aligned}
$$

where $x_0, y_0, z_0, z_1 < 10^m$. We obtain

$$
\begin{aligned}
z_2 &= x_1 \cdot y_1, \\
z_1 &= x_1 \cdot y_0 + x_0 \cdot y_1, \\
z_0 &= x_0 \cdot y_0.
\end{aligned}
$$

Observe that

$$
z_1 = (x_1 + x_0) \cdot (y_1 + y_0) - z_2 - z_0,
$$

so to compute $z_1$, one only needs to compute $(x_1 + x_0) \cdot (y_1 + y_0)$ and then subtract $z_0$ and $z_2$.

The above formula is actually the core of the Karatsuba algorithm: it transforms a multiplication problem of length $n$ into $3$ subproblems of smaller length. If we let $m = \left\lceil \dfrac n 2 \right\rceil$ and denote by $T(n)$ the time for the Karatsuba algorithm to compute the multiplication of two $n$-digit integers, then $T(n) = 3 \cdot T \left(\left\lceil \dfrac n 2 \right\rceil\right) + O(n)$, and by the master theorem $T(n) = \Theta(n^{\log_2 3}) \approx \Theta(n^{1.585})$.

The whole process can be implemented recursively. For clarity, the code below implements polynomial multiplication via the Karatsuba algorithm, and handles all the carry problems at the end.

??? note "karatsuba_mulc.cpp"
    ```cpp
    int *karatsuba_polymul(int n, int *a, int *b) {
      if (n <= 32) {
        // For small sizes, compute directly to avoid the efficiency loss of
        // further recursion
        int *r = new int[n * 2 + 1]();
        for (int i = 0; i <= n; ++i)
          for (int j = 0; j <= n; ++j) r[i + j] += a[i] * b[j];
        return r;
      }
    
      int m = n / 2 + 1;
      int *r = new int[m * 4 + 1]();
      int *z0, *z1, *z2;
    
      z0 = karatsuba_polymul(m - 1, a, b);
      z2 = karatsuba_polymul(n - m, a + m, b + m);
    
      // Compute z1
      // Temporary change, restored after computation
      for (int i = 0; i + m <= n; ++i) a[i] += a[i + m];
      for (int i = 0; i + m <= n; ++i) b[i] += b[i + m];
      z1 = karatsuba_polymul(m - 1, a, b);
      for (int i = 0; i + m <= n; ++i) a[i] -= a[i + m];
      for (int i = 0; i + m <= n; ++i) b[i] -= b[i + m];
      for (int i = 0; i <= (m - 1) * 2; ++i) z1[i] -= z0[i];
      for (int i = 0; i <= (n - m) * 2; ++i) z1[i] -= z2[i];
    
      // Combine z0, z1, z2 to obtain the result
      for (int i = 0; i <= (m - 1) * 2; ++i) r[i] += z0[i];
      for (int i = 0; i <= (m - 1) * 2; ++i) r[i + m] += z1[i];
      for (int i = 0; i <= (n - m) * 2; ++i) r[i + m * 2] += z2[i];
    
      delete[] z0;
      delete[] z1;
      delete[] z2;
      return r;
    }
    
    void karatsuba_mul(int a[], int b[], int c[]) {
      int *r = karatsuba_polymul(LEN - 1, a, b);
      memcpy(c, r, sizeof(int) * LEN);
      for (int i = 0; i < LEN - 1; ++i)
        if (c[i] >= 10) {
          c[i + 1] += c[i] / 10;
          c[i] %= 10;
        }
      delete[] r;
    }
    ```

??? note "About `new` and `delete`"
    See [memory pools](../contest/common-tricks.md#memory-pools).

But such an implementation has a problem: in base $b$, each coefficient of the polynomial may reach the order of $n \cdot b^2$, which may cause integer overflow in a digit-compressed implementation; and if the carry problem is handled during the polynomial multiplication, then the results of $x_1 + x_0$ and $y_1 + y_0$ may reach $2 \cdot b^m$, adding one digit (if the $x_1 - x_0$ computation is adopted, one has to specially handle the negative-number case). Therefore, one needs to decide which implementation to adopt according to the actual application scenario.

## Efficient big-integer multiplication based on polynomials

If the data scale reaches $10^{10^5}$ or larger, ordinary big-number multiplication may time out. This section introduces the method of optimizing such multiplication with polynomials.

For an $n$-digit decimal integer $a$, one can regard it as a polynomial $A=a_{0} 10^0+a_{1} 10^1+\cdots+a_{n-1} 10^{n-1}$ whose coefficient at each position is an integer not exceeding $10$. In this way, we transform the multiplication of two integers into the multiplication of two polynomials.

Ordinary polynomial multiplication still has time complexity $O(n^2)$, but it can be optimized with algorithms from the polynomial chapter such as the [fast Fourier transform](poly/fft.md) and [number-theoretic transform](poly/ntt.md), and the optimized time complexity is $O(n\log n)$.

## Wrapper class

[Here](https://paste.ubuntu.com/p/7VKYzpC7dn/) is a wrapped big-integer class, and [here](https://github.com/Baobaobear/MiniBigInteger/blob/main/bigint_tiny.h) is a super-mini implementation class supporting dynamic length and the four arithmetic operations.

??? note "Here is another template"
    ```cpp
    constexpr int MAXN = 9999;
    // MAXN is the largest digit in a single position
    constexpr int MAXSIZE = 10024;
    // MAXSIZE is the number of positions
    constexpr int DLEN = 4;
    
    // DLEN records how many digits are compressed
    struct Big {
      int a[MAXSIZE], len;
      bool flag;  // marks the '-' sign
    
      Big() {
        len = 1;
        memset(a, 0, sizeof a);
        flag = false;
      }
    
      Big(const int);
      Big(const char*);
      Big(const Big&);
      Big& operator=(const Big&);
      Big operator+(const Big&) const;
      Big operator-(const Big&) const;
      Big operator*(const Big&) const;
      Big operator/(const int&) const;
      // TODO: Big / Big;
      Big operator^(const int&) const;
      // TODO: Big ^ Big;
    
      // TODO: Big bitwise operations;
    
      int operator%(const int&) const;
      // TODO: Big ^ Big;
      bool operator<(const Big&) const;
      bool operator<(const int& t) const;
      void print() const;
    };
    
    Big::Big(const int b) {
      int c, d = b;
      len = 0;
      // memset(a,0,sizeof a);
      CLR(a);
      while (d > MAXN) {
        c = d - (d / (MAXN + 1) * (MAXN + 1));
        d = d / (MAXN + 1);
        a[len++] = c;
      }
      a[len++] = d;
    }
    
    Big::Big(const char* s) {
      int t, k, index, l;
      CLR(a);
      l = strlen(s);
      len = l / DLEN;
      if (l % DLEN) ++len;
      index = 0;
      for (int i = l - 1; i >= 0; i -= DLEN) {
        t = 0;
        k = i - DLEN + 1;
        if (k < 0) k = 0;
        g(j, k, i) t = t * 10 + s[j] - '0';
        a[index++] = t;
      }
    }
    
    Big::Big(const Big& T) : len(T.len) {
      CLR(a);
      f(i, 0, len) a[i] = T.a[i];
      // TODO: overload here?
    }
    
    Big& Big::operator=(const Big& T) {
      CLR(a);
      len = T.len;
      f(i, 0, len) a[i] = T.a[i];
      return *this;
    }
    
    Big Big::operator+(const Big& T) const {
      Big t(*this);
      int big = len;
      if (T.len > len) big = T.len;
      f(i, 0, big) {
        t.a[i] += T.a[i];
        if (t.a[i] > MAXN) {
          ++t.a[i + 1];
          t.a[i] -= MAXN + 1;
        }
      }
      if (t.a[big])
        t.len = big + 1;
      else
        t.len = big;
      return t;
    }
    
    Big Big::operator-(const Big& T) const {
      int big;
      bool ctf;
      Big t1, t2;
      if (*this < T) {
        t1 = T;
        t2 = *this;
        ctf = true;
      } else {
        t1 = *this;
        t2 = T;
        ctf = false;
      }
      big = t1.len;
      int j = 0;
      f(i, 0, big) {
        if (t1.a[i] < t2.a[i]) {
          j = i + 1;
          while (t1.a[j] == 0) ++j;
          --t1.a[j--];
          // WTF?
          while (j > i) t1.a[j--] += MAXN;
          t1.a[i] += MAXN + 1 - t2.a[i];
        } else
          t1.a[i] -= t2.a[i];
      }
      t1.len = big;
      while (t1.len > 1 && t1.a[t1.len - 1] == 0) {
        --t1.len;
        --big;
      }
      if (ctf) t1.a[big - 1] = -t1.a[big - 1];
      return t1;
    }
    
    Big Big::operator*(const Big& T) const {
      Big res;
      int up;
      int te, tee;
      f(i, 0, len) {
        up = 0;
        f(j, 0, T.len) {
          te = a[i] * T.a[j] + res.a[i + j] + up;
          if (te > MAXN) {
            tee = te - te / (MAXN + 1) * (MAXN + 1);
            up = te / (MAXN + 1);
            res.a[i + j] = tee;
          } else {
            up = 0;
            res.a[i + j] = te;
          }
        }
        if (up) res.a[i + T.len] = up;
      }
      res.len = len + T.len;
      while (res.len > 1 && res.a[res.len - 1] == 0) --res.len;
      return res;
    }
    
    Big Big::operator/(const int& b) const {
      Big res;
      int down = 0;
      gd(i, len - 1, 0) {
        res.a[i] = (a[i] + down * (MAXN + 1)) / b;
        down = a[i] + down * (MAXN + 1) - res.a[i] * b;
      }
      res.len = len;
      while (res.len > 1 && res.a[res.len - 1] == 0) --res.len;
      return res;
    }
    
    int Big::operator%(const int& b) const {
      int d = 0;
      gd(i, len - 1, 0) d = (d * (MAXN + 1) % b + a[i]) % b;
      return d;
    }
    
    Big Big::operator^(const int& n) const {
      Big t(*this), res(1);
      int y = n;
      while (y) {
        if (y & 1) res = res * t;
        t = t * t;
        y >>= 1;
      }
      return res;
    }
    
    bool Big::operator<(const Big& T) const {
      int ln;
      if (len < T.len) return true;
      if (len == T.len) {
        ln = len - 1;
        while (ln >= 0 && a[ln] == T.a[ln]) --ln;
        if (ln >= 0 && a[ln] < T.a[ln]) return true;
        return false;
      }
      return false;
    }
    
    bool Big::operator<(const int& t) const {
      Big tee(t);
      return *this < tee;
    }
    
    void Big::print() const {
      printf("%d", a[len - 1]);
      gd(i, len - 2, 0) { printf("%04d", a[i]); }
    }
    
    void print(const Big& s) {
      int len = s.len;
      printf("%d", s.a[len - 1]);
      gd(i, len - 2, 0) { printf("%04d", s.a[i]); }
    }
    
    char s[100024];
    ```

## Exercises

-   [NOIP 2012 国王游戏](https://loj.ac/problem/2603)
-   [SPOJ - Fast Multiplication](http://www.spoj.com/problems/MUL/en/)
-   [SPOJ - GCD2](http://www.spoj.com/problems/GCD2/)
-   [UVa - Division](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1024)
-   [UVa - Fibonacci Freeze](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=436)
-   [Codeforces - Notepad](http://codeforces.com/contest/17/problem/D)

## References and links

1.  [Karatsuba algorithm - Wikipedia](https://en.wikipedia.org/wiki/Karatsuba_algorithm)
