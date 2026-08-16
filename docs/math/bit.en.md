Bit operations refer to unary and binary operations on the binary representation of integers, divided into two categories: **bitwise operations** and **shifts**. Bit operations are one of the most basic classes of operations in a CPU, and their speed is often quite fast.

## Integers and bit sequences

See also: [integer types](../lang/var.md#integer-type), [complement method](./numeral-sys/base.md#补数法)

We call a fixed-length sequence consisting only of `0`s and `1`s a bit sequence. The leftmost bit is called the most significant bit, and the rightmost bit is called the least significant bit.

Computers use bit sequences to represent integers within a certain range. There are only $2^N$ bit sequences of length $N$, so they can only establish a one-to-one correspondence with $2^N$ integers. This one-to-one correspondence can be divided into two categories: **signed** and **unsigned**. Signed means the corresponding integers include negative numbers, and unsigned means the corresponding integers are all non-negative.

-   For the unsigned correspondence, we can directly use the binary representation of the integer as the bit sequence, padding the high-order positions with `0` when the length is insufficient.

    Under the unsigned correspondence, a bit sequence of length $N$ can represent integers in $[0,2^N-1]$.

-   For the signed correspondence, we have two representation rules: **ones' complement** and **two's complement**.

    For non-negative integers, their representation rule is consistent with the unsigned rule; for negative integers, we take the bit sequence corresponding to their opposite (positive) number, perform a **bitwise NOT** on it (i.e. change `0` to `1` and `1` to `0`), and the result is called the ones' complement; we convert the ones' complement to an integer under the unsigned correspondence, then add one, then convert back to a bit sequence under the unsigned correspondence, discarding the part exceeding the original bit-sequence length, and the resulting new sequence is called the two's complement.

    Under the ones'-complement correspondence, a bit sequence of length $N$ can represent integers in $[-2^{N-1}+1,2^{N-1}-1]$.

    Under the two's-complement correspondence, a bit sequence of length $N$ can represent integers in $[-2^{N-1},2^{N-1}-1]$.

Taking a $3$-bit bit sequence as an example:

| Bit sequence | Unsigned integer | Signed integer (ones' complement) | Signed integer (two's complement) |
| ----- | ----- | --------- | --------- |
| `000` | $0$   | $0$       | $0$       |
| `001` | $1$   | $1$       | $1$       |
| `010` | $2$   | $2$       | $2$       |
| `011` | $3$   | $3$       | $3$       |
| `100` | $4$   | $-3$      | $-4$      |
| `101` | $5$   | $-2$      | $-3$      |
| `110` | $6$   | $-1$      | $-2$      |
| `111` | $7$   | $-0$      | $-1$      |

One can see that the biggest problem with ones' complement is that it produces $-0$, a "negative number" that does not actually exist, so in general we use only two's complement. Since, when representing a signed integer, its sign is determined solely by the most significant bit of the bit sequence, we call this bit the **sign bit**.

Converting a bit sequence to an integer is also easy: for non-negative numbers no special operation is needed; for ones' complement, negating gives the corresponding opposite number; for two's complement, negating and adding one gives the corresponding opposite number.

## Bit operations

Bit operations refer to operations that apply some [boolean function](./boolean-algebra.md#boolean-function) to a bit sequence bit by bit. Formally, for a boolean function $f:\mathbf{B}^k\to \mathbf{B}$, a bit operation is a function of the form

$$
\begin{aligned}
    F:\left(\mathbf{B}^m\right)^k&\to \mathbf{B}^m\\
    ((p_{1,1},\dots,p_{m,1}),\dots,(p_{1,k},\dots,p_{m,k}))&\mapsto (f(p_{1,1},\dots,p_{1,k}),\dots,f(p_{m,1},\dots,p_{m,k}))
\end{aligned}
$$

where $m$ is the length of the bit sequence. Likewise, we generally study only unary and binary bit operations. Unless otherwise stated, the bit operations below are limited to the unary and binary cases.

In general, we regard **bitwise NOT**, **bitwise AND**, **bitwise OR**, and **bitwise XOR** as the basic bit operations; the other bit operations can all be obtained by combining these operations.

| Bit operation | Mathematical symbol | Corresponding boolean function | C++ operator | Explanation |
| ---- | ----------------------------- | -------- | --------------- | ----------------------- |
| Bitwise NOT | $\operatorname{NOT}$ | $\lnot$ | `~` | $0$ becomes $1$, $1$ becomes $0$ |
| Bitwise AND | $\operatorname{AND}$ | $\land$ | `&` | Is $1$ only when both corresponding bits are $1$ |
| Bitwise OR | $\operatorname{OR}$ | $\lor$ | <code>\|</code> | Is $1$ as long as one of the two corresponding bits is $1$ |
| Bitwise XOR | $\oplus$, $\operatorname{XOR}$ | $\oplus$ | `^` | Is $1$ only when the two corresponding bits differ |

???+ warning "Warning"
    Take care to distinguish bit operations from boolean functions.

For example:

-   $\operatorname{NOT} 01010111=10101000$,
-   $01010011 \operatorname{AND} 00110010=00010010$,
-   $01010011 \operatorname{OR}  00110010=01110011$,
-   $01010011 \operatorname{XOR} 00110010=01100001$.

Since, in the above four bit operations, the operation on each bit is independent, these four bit operations directly inherit the properties of their corresponding boolean functions.

For convenience, when the length of the bit sequence is known, we can also directly perform bit operations on integers, for example:

$$
\begin{aligned}
    \operatorname{NOT} 5&=-6,\\
    \operatorname{NOT} (-5)&=4,\\
    5 \operatorname{AND} 6 &=4,\\
    5 \operatorname{OR} 6 &=7,\\
    5 \operatorname{XOR} 6 &=3.
\end{aligned}
$$

Assuming $x,y\geq 0$, we can also represent bit operations in the form of a sum:

$$
\begin{aligned}
    \operatorname{NOT} x&=\sum_{n=0}^{\lfloor\log_{2}x\rfloor}2^n\left(\left(\left\lfloor\frac{x}{2^n}\right\rfloor\bmod 2+1\right)\bmod 2\right)\\
    &=\sum_{n=0}^{\lfloor\log_{2}x\rfloor}\left(2^{\left\lfloor\log_{2}x\right\rfloor +1}-1-x\right)\\
    x\operatorname{AND} y&=\sum_{n=0}^{\lfloor\log_{2}\max\{x,y\}\rfloor}2^n\left(\left\lfloor\frac{x}{2^n}\right\rfloor\bmod 2\right)\left(\left\lfloor{\frac{y}{2^n}}\right\rfloor\bmod 2\right)\\
    x\operatorname{OR} y&=\sum_{n=0}^{\lfloor\log_{2}\max\{x,y\}\rfloor}2^n\left(\left(\left\lfloor\frac{x}{2^n}\right\rfloor\bmod 2\right)+\left(\left\lfloor{\frac{y}{2^n}}\right\rfloor\bmod 2\right)-\left(\left\lfloor\frac{x}{2^n}\right\rfloor\bmod 2\right)\left(\left\lfloor{\frac{y}{2^n}}\right\rfloor\bmod 2\right)\right)\\
    x\operatorname{XOR} y&=\sum_{n=0}^{\lfloor\log_{2}\max\{x,y\}\rfloor}2^n\left(\left(\left(\left\lfloor\frac{x}{2^n}\right\rfloor\bmod 2\right)+\left(\left\lfloor{\frac{y}{2^n}}\right\rfloor\bmod 2\right)\right)\bmod 2\right)\\
    &=\sum_{n=0}^{\lfloor\log_{2}\max\{x,y\}\rfloor}2^n\left(\left(\left\lfloor\frac{x}{2^n}\right\rfloor +\left\lfloor\frac{y}{2^n}\right\rfloor\right)\bmod 2\right)
\end{aligned}
$$

Where no ambiguity arises, we omit "bitwise" in the following.

## Shift

See also: [C++ bit operators](../lang/op.md#bit-operators).

A shift is a class of binary operations that "move a bit sequence left or right bit by bit"; the first argument is a bit sequence, and the second argument is generally a non-negative integer. Moving to the left is called a **left shift**, and moving to the right is called a **right shift**. According to how the vacated positions after the move are filled, shift operations can be divided into **arithmetic shifts**, **logical shifts**, and **circular shifts**. Among them,

-   a logical shift fills the vacated positions with 0,
-   an arithmetic right shift fills the vacated positions with the sign bit, and an arithmetic left shift is the same as a logical left shift,
-   a circular shift fills the vacated positions with the overflow bits.

For example, for the $8$-bit bit sequence `10 01 01 10`:

| Operation | Result |
| ---------- | ------------- |
| Arithmetic left shift by $2$ bits | `01 01 10 00` |
| Arithmetic right shift by $2$ bits | `11 10 01 01` |
| Logical left shift by $2$ bits | `01 01 10 00` |
| Logical right shift by $2$ bits | `00 10 01 01` |
| Circular left shift by $2$ bits | `01 01 10 10` |
| Circular right shift by $2$ bits | `10 10 01 01` |

In C++, we use `a << b` to denote a left shift and `a >> b` to denote a right shift; for which shift rule is specifically used, see [C++ bit operators](../lang/op.md#bit-operators).

We can implement a circular shift with the following code:

???+ note "Implementation"
    ```cpp
    --8<-- "docs/math/code/bit/bit_1.cpp:core"
    ```

## Applications of bit operations

Bit operations generally have three uses:

1.  To perform certain operations efficiently, replacing other inefficient methods. See [compiler optimizations #strength reduction](../lang/optimizations.md#strength-reduction-strength-reduction).
2.  To [represent sets](./binary-set.md) (commonly used in [bitmask DP](../dp/state.md)).
3.  The problem itself requires bit operations.

It should be noted that replacing other kinds of operations with bit operations often does not bring much optimization, but instead makes the code more complex, so one needs to weigh it carefully when using it.

### Applications related to powers of 2

Since bit operations target the binary representation, many applications related to integer powers of 2 can be derived.

Multiplying (dividing) a number by a non-negative integer power of 2:

=== "C++"
    ```cpp
    --8<-- "docs/math/code/bit/bit_2.cpp:mul"
    ```

=== "Python"
    ```python
    --8<-- "docs/math/code/bit/bit_2.py:mul"
    ```

??? warning "Warning"
    The division we usually write rounds toward $0$, whereas the right shift here rounds down (note the difference here); that is, the two methods are equivalent when the number is greater than or equal to $0$, but differ when the number is less than $0$; for example, the value of `-1 / 2` is $0$, while the value of `-1 >> 1` is $-1$.

### Taking the absolute value

On some machines, this is more efficient than `n > 0 ? n : -n`.

=== "C++"
    ```cpp
    --8<-- "docs/math/code/bit/bit_2.cpp:abs"
    ```

=== "Python"
    ```python
    --8<-- "docs/math/code/bit/bit_2.py:abs"
    ```

### Taking the maximum/minimum of two numbers

On some machines, this is more efficient than `a > b ? a : b`.

=== "C++"
    ```cpp
    --8<-- "docs/math/code/bit/bit_2.cpp:minmax"
    ```

=== "Python"
    ```python
    --8<-- "docs/math/code/bit/bit_2.py:minmax"
    ```

### Determining whether two nonzero numbers have the same sign

=== "C++"
    ```cpp
    --8<-- "docs/math/code/bit/bit_2.cpp:sgn"
    ```

=== "Python"
    ```python
    --8<-- "docs/math/code/bit/bit_2.py:sgn"
    ```

### Swapping two numbers

???+ note "This method has limitations"
    This way can only be used to swap two integers, and has a limited range of use.
    
    For swapping in the general case, it is recommended to directly call the `std::swap` function in the `algorithm` library.

```cpp
--8<-- "docs/math/code/bit/bit_2.cpp:swap"
```

### Manipulating the binary bits of a number

Getting a certain bit of the binary of a number:

=== "C++"
    ```cpp
    --8<-- "docs/math/code/bit/bit_2.cpp:get_bit"
    ```

=== "Python"
    ```python
    --8<-- "docs/math/code/bit/bit_2.py:get_bit"
    ```

Setting a certain bit of the binary of a number to $0$:

=== "C++"
    ```cpp
    --8<-- "docs/math/code/bit/bit_2.cpp:unset_bit"
    ```

=== "Python"
    ```python
    --8<-- "docs/math/code/bit/bit_2.py:unset_bit"
    ```

Setting a certain bit of the binary of a number to $1$:

=== "C++"
    ```cpp
    --8<-- "docs/math/code/bit/bit_2.cpp:set_bit"
    ```

=== "Python"
    ```python
    --8<-- "docs/math/code/bit/bit_2.py:set_bit"
    ```

Toggling a certain bit of the binary of a number:

=== "C++"
    ```cpp
    --8<-- "docs/math/code/bit/bit_2.cpp:flap_bit"
    ```

=== "Python"
    ```python
    --8<-- "docs/math/code/bit/bit_2.py:flap_bit"
    ```

These operations amount to treating a $32$-bit integer variable as a boolean array of length $32$.

## Hamming weight

The Hamming weight is the number of symbols in a string of symbols that differ from the zero-symbol (defined on the character set it uses). For a binary number, its Hamming weight equals its number of $1$s (i.e. `popcount`).

Finding the Hamming weight of a number can be solved in a loop: we continually remove the last bit of this number in binary (i.e. right-shift by $1$ bit), maintain an answer variable, and during the division update the answer according to whether the least significant bit is $1$.

The code is as follows:

```cpp
--8<-- "docs/math/code/bit/bit_2.cpp:popcnt1"
```

Finding the Hamming weight of a number can also use the `lowbit` operation: we continually subtract its `lowbit`[^note1] from this number until this number becomes $0$.

The code is as follows:

```cpp
--8<-- "docs/math/code/bit/bit_2.cpp:popcnt2"
```

### Constructing a permutation with increasing Hamming weight

In [bitmask DP](../dp/state.md), enumerating in order of increasing popcount can sometimes avoid enumerating states repeatedly. This is a major use of constructing a permutation with increasing Hamming weight.

Below we specifically explore how to construct a permutation with increasing Hamming weight in $O(n)$ time.

We know that the smallest integer with Hamming weight $n$ is $2^n-1$. As long as we can construct, in constant time, a successor with equal Hamming weight, we can, by enumerating the Hamming weight and continually finding the next number starting from $2^n-1$, construct in $O(n)$ time the required permutation of $0\sim n$.

And finding a successor of a number $x$ with equal Hamming weight follows this idea, taking $(10110)_2$ as an example:

-   Move the rightmost $1$ of $(10110)_2$ to the left; if it cannot be moved, move the $1$ to its left, and so on, obtaining $(11010)_2$.

-   Move all the $1$s in the obtained $(11010)_2$, from the original position of the last-moved $1$ down to the least significant bit, to the far right. Here the last-moved $1$ was originally in the third position, so the last three bits $010$ become $001$, obtaining $(11001)_2$.

This process can be optimized with bit operations:

```cpp
--8<-- "docs/math/code/bit/bit_3.cpp:hamming1"
```

-   In the first step, we add the number $x$ to its `lowbit`, which, in the binary representation, amounts to replacing the rightmost consecutive run of $1$s of $x$ with a single $1$ to its left. As with the binary number $(10110)_2$ just mentioned, after adding its `lowbit` it is $(11000)_2$. This actually gives the first half of our answer.
-   Next we need to fill in the $1$s at the back of the answer. The `lowbit` of $t$ is the position after moving the leftmost $1$ of the rightmost consecutive run of $1$s of $x$, while the `lowbit` of $x$ is the rightmost position of the rightmost consecutive run of $1$s of $x$. Still taking $(10110)_2$ as an example, $t = (11000)_2$, $\operatorname{lowbit}(t) = (01000)_2$, $\operatorname{lowbit}(x)=(00010)_2$.
-   The following division operation is the hardest part of this kind of bit operation to understand, but it is also the most crucial part. Let the highest $1$ of the rightmost consecutive run of $1$s of the **original number** be at bit $r$ (bit positions start from $0$), and the lowest $1$ at bit $l$; the `lowbit` of $t$ equals `1 << (r+1)`, and the `lowbit` of $x$ equals `1 << l`. What `(((t&-t)/(x&-x))>>1)` gives is `(1<<(r+1))/(1<<l)/2 = (1<<r)/(1<<l) = 1<<(r-l)`, which in binary is a $1$ followed by $r-l$ zeros, the number of zeros being exactly the number of consecutive $1$s minus $1$. Taking our number just now as an example, $\frac{\operatorname{lowbit(t)/2}}{\operatorname{lowbit(x)}} = \frac{(00100)_2}{(00010)_2} = (00010)_2$. Subtracting $1$ from this number gives the low-order bits we need to fill in, and OR-ing it with the original number gives the answer.

So the complete code for enumerating the permutation of $0\sim n$ in order of increasing Hamming weight is:

```cpp
--8<-- "docs/math/code/bit/bit_3.cpp:hamming2_begin"
--8<-- "docs/math/code/bit/bit_3.cpp:hamming2_end"
```

Here one should note the special-casing of $0$, because $0$ has no successor with the same Hamming weight.

## Related classes and functions in C++

### GCC built-in functions

GCC also has some built-in functions for bit operations:

-   `int __builtin_ffs(int x)`: returns the position of the last $1$ at the end of the binary of $x$, with positions numbered from $1$ (the least significant bit numbered $1$). Returns $0$ when $x$ is $0$.
-   `int __builtin_clz(unsigned int x)`: returns the number of leading $0$s in the binary of $x$. When $x$ is $0$, the result is undefined.
-   `int __builtin_ctz(unsigned int x)`: returns the number of consecutive $0$s at the end of the binary of $x$. When $x$ is $0$, the result is undefined.
-   `int __builtin_clrsb(int x)`: when the sign bit of $x$ is $0$, returns the number of leading $0$s in the binary of $x$ minus one; otherwise returns the number of leading $1$s in the binary of $x$ minus one.
-   `int __builtin_popcount(unsigned int x)`: returns the number of $1$s in the binary of $x$.
-   `int __builtin_parity(unsigned int x)`: determines the parity of the number of $1$s in the binary of $x$.

These functions can all have `l` or `ll` appended to the end of the function name (such as `__builtin_popcountll`) to make the argument type become (`unsigned`)`long` or (`unsigned`)`long long` (the return value is still of type `int`).
For example, sometimes we want to find the base-2 logarithm of a number; if we ignore the special case of `0`, this amounts to the number of binary digits of the number minus `1`, and the number of digits in the binary representation of an `N`-bit integer `n` can be expressed as `N - __builtin_clz(n)`, so `N - 1 - __builtin_clz(n)` can find the base-2 logarithm of `n`.

Since these functions are built-in functions that have been highly optimized by the compiler, they run very fast (some even require only a single instruction).

### More bits

If the bit sequence to be operated on is very long, you can use [`std::bitset`](../lang/csl/bitset.md).

## Recommended problems

-   [Luogu P1225 黑白棋游戏](https://www.luogu.com.cn/problem/P1225)

## References and notes

1.  [Bit Twiddling Hacks](https://graphics.stanford.edu/~seander/bithacks.html)
2.  [Bit Operation Builtins (Using the GNU Compiler Collection (GCC))](https://gcc.gnu.org/onlinedocs/gcc/Bit-Operation-Builtins.html)
3.  [Bitwise operation - Wikipedia](https://en.wikipedia.org/wiki/Bitwise_operation)

[^note1]: The first $1$ from low to high in the binary representation of a number, together with the zeros after it; for example, the `lowbit` of $(1010)_2$ is $(0010)_2$; see [Fenwick tree](../ds/fenwick.md) for details.
