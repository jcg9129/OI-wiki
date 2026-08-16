## Data types

The type system of C++ consists of the following parts:

1.  Fundamental types (the representative keyword/representative type is in parentheses)
    1.  No type / `void` type (`void`)
    2.  (Since C++11) Null pointer type (`std::nullptr_t`)
    3.  Arithmetic types
        1.  Integer type (`int`)
        2.  Boolean type / `bool` type (`bool`)
        3.  Character type (`char`)
        4.  Floating-point type (`float`, `double`)
2.  Compound types[^note11]

### Boolean type

A variable of type `bool` can only take two values: `true` and `false`.

In general, a variable of type `bool` occupies $1$ byte (in general, $1$ byte = $8$ bits) of space.

???+ tip "Tip"
    You can obtain the number of bits in a byte through the macro constant `CHAR_BIT` in the header file `<climits>`(C++)/`<limits.h>`(C).

???+ note "The boolean type of the C language"
    See also [Differences between C++ and other commonly used languages - bool](./cpp-other-langs.md#bool).
    
    The C language originally did not have a boolean type; it was not until C99 that the `_Bool` keyword was introduced as the boolean type, which is regarded as an unsigned integer type.
    
    ???+ note "Note"
        The `bool` type of the C language, since C23, no longer uses the integer zero and non-zero value definition, but is defined as a type sufficient to store the two constants `true` and `false`.
    
    For convenience of use, `stdbool.h` provides the three macros `bool`, `true`, `false`, defined as follows:
    
    ```c
    #define bool _Bool
    #define true 1
    #define false 0
    ```
    
    These macros were removed in C23, and since C23 `true`, `false`, and `bool` are introduced as keywords, while `_Bool` is retained as an alternative spelling[^note10].
    
    In addition, since C23 we can also obtain the bit width of the boolean type through the macro constant `BOOL_WIDTH` in `<limits.h>`.

### Integer type

Used to store integers. The most basic integer type is `int`.

???+ warning "Note"
    For historical reasons, in C++ the boolean type and character type are regarded as special integer types.
    
    In almost all cases, character types other than `signed char` and `unsigned char` **should not** be used as integer types.

Integer types generally have 5 gradations by bit width: `char`, `short`, `int`, `long`, `long long`.

The C++ standard guarantees `1 == sizeof(char) <= sizeof(short) <= sizeof(int) <= sizeof(long) <= sizeof(long long)`

For historical reasons, the bit width of integer types has multiple popular models; to solve this problem, C99/C++11 introduced [fixed-width integer types](#fixed-width-integer-types).

???+ note "The size of the `int` type"
    In the C++ standard, the number of bits of `int` is specified to be **at least** $16$ bits.
    
    In fact, on the vast majority of current platforms, the number of bits of `int` is $32$ bits.

For the `int` keyword, we can use the following modifier keywords to modify it:

Signedness:

-   `signed`: represents a signed integer (default);
-   `unsigned`: represents an unsigned integer.

Size:

-   `short`: represents **at least** a $16$-bit integer;
-   `long`: represents **at least** a $32$-bit integer;
-   (Since C++11) `long long`: represents **at least** a $64$-bit integer.

The following table gives, **in general**, the bit width and representation range size of each integer type (on a few platforms the representation range of some types may differ from the table below):

| Type name | Equivalent type | Bit width (C++ standard) | Bit width (common) | Bit width (less common) |
| --------------------------------------------------------------------- | ------------------------ | ---------- | ------ | -------------------------- |
| `signed char` | `signed char` | $8$ | - | - |
| `unsigned char` | `unsigned char` | $8$ | - | - |
| `short`, `short int`, `signed short`, `signed short int` | `short int` | $\geq 16$ | $16$ | - |
| `unsigned short`, `unsigned short int` | `unsigned short int` | $\geq 16$ | $16$ | - |
| `int`, `signed`, `signed int` | `int` | $\geq 16$ | $32$ | $16$ (common in the Win16 API) |
| `unsigned`, `unsigned int` | `unsigned int` | $\geq 16$ | $32$ | $16$ (common in the Win16 API) |
| `long`, `long int`, `signed long`, `signed long int` | `long int` | $\geq 32$ | $32$ | $64$ (common in 64-bit Linux, macOS) |
| `unsigned long`, `unsigned long int` | `unsigned long int` | $\geq 32$ | $32$ | $64$ (common in 64-bit Linux, macOS) |
| `long long`, `long long int`, `signed long long`, `signed long long int` | `long long int` | $\geq 64$ | $64$ | - |
| `unsigned long long`, `unsigned long long int` | `unsigned long long int` | $\geq 64$ | $64$ | - |

When the bit width is $x$, the representation range of a signed type is $-2^{x-1}\sim 2^{x-1}-1$[^note16], and the representation range of an unsigned type is $0 \sim 2^x-1$. Specifically, we have the following table:

| Bit width | Representation range |
| ---- | ------------------------------------------------- |
| $8$ | Signed: $-2^{7}\sim 2^{7}-1$, unsigned: $0 \sim 2^{8}-1$ |
| $16$ | Signed: $-2^{15}\sim 2^{15}-1$, unsigned: $0 \sim 2^{16}-1$ |
| $32$ | Signed: $-2^{31}\sim 2^{31}-1$, unsigned: $0 \sim 2^{32}-1$ |
| $64$ | Signed: $-2^{63}\sim 2^{63}-1$, unsigned: $0 \sim 2^{64}-1$ |

???+ note "Equivalent type expressions"
    In cases that do not cause ambiguity, it is allowed to omit some modifier keywords, or to adjust the order of the modifier keywords. This means that the same type will have multiple equivalent expressions.
    
    For example, `int`, `signed`, `int signed`, `signed int` represent the same type, while `unsigned long` and `unsigned long int` represent the same type.

In addition, some compilers implement extended integer types; for example, GCC implements 128-bit integers: the signed version `__int128_t` and the unsigned version `__uint128_t`. If you want to use these types during a competition, **please read the competition rules carefully** to determine whether the use of extended integer types is allowed or supported.

???+ warning "Note"
    STL does not necessarily have sufficient support for extended integer types, so extra care is needed when using extended integer types.
    
    ???+ note "Example code"
        ```cpp
        #include <cmath>
        #include <iostream>
        
        int f1(int n) {
          return abs(n);  // Good
        }
        
        int f2(int n) {
          return std::abs(n);  // Good
        }
        
        __int128_t f3(__int128_t n) {
          return abs(n);  // Bad
        }
        
        // Wrong
        // __int128_t f4(__int128_t n) {
        //   return std::abs(n);
        // }
        
        int main() {
          std::cout << "f1: " << f1(-42) << std::endl;
          std::cout << "f2: " << f2(-42) << std::endl;
          // std::cout << "f3: " << f3(-42) << std::endl; // Wrong
          // std::cout << "f4: " << f4(-42) << std::endl; // Wrong
          return 0;
        }
        ```
    
    The above example code has the following problems:
    
    1.  In `__int128_t f3(__int128_t)`, the C-style absolute value function is used, whose signature is `int abs(int)`, so `n` is first forcibly converted to `int`, and only then the `abs` function is called.
    2.  In `__int128_t f4(__int128_t)`, the C++-style absolute value function is used, which does not have a function overload with signature `__int128_t std::abs(__int128_t)`, so it cannot compile.
    3.  C++ stream output does not support `__int128_t` and `__uint128_t`.
    
    The following is one solution:
    
    ??? note "Corrected code"
        ```cpp
        #include <cmath>
        #include <iostream>
        
        __int128_t abs(__int128_t n) { return n < 0 ? -n : n; }
        
        std::ostream &operator<<(std::ostream &os, __uint128_t n) {
          if (n > 9) os << n / 10;
          os << (int)(n % 10);
          return os;
        }
        
        std::ostream &operator<<(std::ostream &os, __int128_t n) {
          if (n < 0) {
            os << '-';
            n = -n;
          }
          return os << (__uint128_t)n;
        }
        
        int f1(int n) { return abs(n); }
        
        int f2(int n) { return std::abs(n); }
        
        __int128_t f3(__int128_t n) { return abs(n); }
        
        int main() {
          std::cout << "f1: " << f1(-42) << std::endl;
          std::cout << "f2: " << f2(-42) << std::endl;
          std::cout << "f3: " << f3(-42) << std::endl;
        }
        ```

### Character type

Divided into "narrow character types" and "wide character types"; since algorithm competitions almost never use wide character types, here we only introduce narrow character types.

The number of bits of a narrow character type is generally $8$ bits; in fact the underlying storage method is still an integer, and the one-to-one correspondence between characters and integers is generally implemented through [ASCII encoding](http://www.asciitable.com/). There are the following three:

-   `signed char`: a type represented by a signed character, with a representation range between $-128 \sim 127$.
-   `unsigned char`: a type represented by an unsigned character, with a representation range between $0 \sim 255$.
-   `char` has the same representation and alignment as one of `signed char` or `unsigned char`, but is always an independent type.

    The signedness of `char` depends on the compiler and target platform: the default setting of ARM and PowerPC is usually unsigned, while the default setting of x86 and x64 is usually signed.

    GCC can add `-fsigned-char` or `-funsigned-char` in the compilation parameters to specify treating `char` as `signed char` or `unsigned char`; for other compilers, please refer to the documentation. Note that specifying a signedness different from the architecture default may break the ABI and cause the program to not work normally.

???+ warning "Note"
    Unlike other integer types, `char`, `signed char`, `unsigned char` are **three different types**.
    
    Generally speaking, `signed char`, `unsigned char` should not be used to store characters; in the vast majority of cases, these two types are regarded as integer types.

### Floating-point type

Used to store "real numbers" (note that they are not real numbers in the strict sense, but approximations of real numbers under certain rules), including the following three:

-   `float`: single-precision floating-point type. If supported, it matches the IEEE-754 binary32 format.
-   `double`: double-precision floating-point type. If supported, it matches the IEEE-754 binary64 format.
-   `long double`: extended-precision floating-point type. If supported, it matches the IEEE-754 binary128 format; otherwise, if supported, it matches the IEEE-754 binary64 extended format; otherwise, it matches some non-IEEE-754 extended floating-point format with precision better than binary64 and a value range at least as good as binary64; otherwise, it matches the IEEE-754 binary64 format.

| Floating-point format | Bit width | Maximum positive number | Precision digits |
| ---------------------- | --------- | -------------------------- | ---------------- |
| IEEE-754 binary32 format | $32$ | $3.4\times 10^{38}$ | $6\sim 9$ |
| IEEE-754 binary64 format | $64$ | $1.8\times 10^{308}$ | $15\sim 17$ |
| IEEE-754 binary64 extended format | $\geq 80$ | $\geq 1.2\times 10^{4932}$ | $\geq 18\sim 21$ |
| IEEE-754 binary128 format | $128$ | $1.2\times 10^{4932}$ | $33\sim 36$ |

> The minimum negative number of the IEEE-754 floating-point format is the opposite of the maximum positive number.

Because the `float` type has a small representation range and low precision, in actual applications the `double` type is often used to represent floating-point numbers.

In addition, floating-point types can support some special values:

-   Infinity (positive or negative): `INFINITY`.
-   Negative zero: `-0.0`, for example `1.0 / 0.0 == INFINITY`, `1.0 / -0.0 == -INFINITY`.
-   Not a number (NaN): `std::nan`, `NAN`, which can generally be produced by operations such as `0.0 / 0.0`. It compares unequal with any value (including itself); after C++11 we can use `std::isnan` to determine whether a floating-point number is NaN.

### No type

The `void` type is the no type; unlike the above several types, we cannot declare a variable as `void` type. But the return value of a function is allowed to be `void` type, indicating that this function has no return value.

### Null pointer type

Please refer to the [corresponding chapter](./pointer.md#null-pointer) of pointers.

## Fixed-width integer types

Since C++11, support for fixed-width integers is provided, specifically as follows:

-   `<cstdint>`: provides several fixed-width integer types and macro constants such as the maximum value, minimum value, etc. of each fixed-width integer type.
-   `<cinttypes>`: provides format macro constants for the `std::fprintf` family of functions and the `std::fscanf` family of functions for fixed-width integer types.

There are the following kinds of fixed-width integers:

-   `intN_t`: a signed integer type with width **exactly** $N$ bits, such as `int32_t`.
-   `int_fastN_t`: the **fastest** signed integer type with width **at least** $N$ bits, such as `int_fast32_t`.
-   `int_leastN_t`: the **smallest** signed integer type with width **at least** $N$ bits, such as `int_least32_t`.

For the unsigned version, we only need to add the letter u before the signed version, such as `uint32_t`, `uint_least8_t`.

The standard stipulates that the following 16 types must be implemented:

`int_fast8_t`, `int_fast16_t`, `int_fast32_t`, `int_fast64_t`,

`int_least8_t`, `int_least16_t`, `int_least32_t`, `int_least64_t`,

`uint_fast8_t`, `uint_fast16_t`, `uint_fast32_t`, `uint_fast64_t`,

`uint_least8_t`, `uint_least16_t`, `uint_least32_t`, `uint_least64_t`.

The vast majority of compilers, on this basis, also implement the following 8 types:

`int8_t`, `int16_t`, `int32_t`, `int64_t`,

`uint8_t`, `uint16_t`, `uint32_t`, `uint64_t`.

In the case where the corresponding types are implemented, the C++ standard stipulates that macro constants representing the maximum value, minimum value, and bit width of the corresponding types must be implemented, in the format of removing the `_t` at the end of the type name, converting to uppercase, and adding a suffix:

-   `_MAX` represents the maximum value, such as `INT32_MAX` being the maximum value of `int32_t`.
-   `_MIN` represents the minimum value, such as `INT32_MIN` being the minimum value of `int32_t`.

???+ warning "Note"
    Fixed-width integer types are essentially type aliases of ordinary integer types, so mixing fixed-width integer types and ordinary integer types may affect cross-platform compilation, for example:
    
    ???+ note "Example code"
        ```cpp
        #include <algorithm>
        #include <cstdint>
        #include <iostream>
        
        int main() {
          long long a;
          int64_t b;
          std::cin >> a >> b;
          std::cout << std::max(a, b) << std::endl;
          return 0;
        }
        ```
    
    `int64_t` is generally `long long int` under 64-bit Windows, and generally `long int` under 64-bit Linux, so this code cannot compile when using GCC under 64-bit Linux, but can compile when using MSVC under 64-bit Windows, because `std::max` requires the two input arguments to have exactly the same type.

In addition, since C++17, `<limits>` provides the `std::numeric_limits` class template, used to query the properties of various arithmetic types, such as the maximum value, minimum value, whether it is an integer type, whether it is signed, etc.

```cpp
#include <cstdint>
#include <limits>

std::numeric_limits<int32_t>::max();  // the maximum value of int32_t, 2'147'483'647
std::numeric_limits<int32_t>::min();  // the minimum value of int32_t, -2'147'483'648

std::numeric_limits<double>::min();  // the minimum value of double, approximately 2.22507e-308
std::numeric_limits<double>::epsilon();  // the difference between 1.0 and the next representable value of double,
                                         // approximately 2.22045e-16
```

## Type conversion

At certain times (for example when a function accepts an `int`-type parameter but a `double`-type variable is passed in), we need to convert one type into another type.

The type conversion mechanism in C++ is relatively complex; here we mainly introduce two conversions for basic data types: numeric promotion and numeric conversion.

### Numeric promotion

During numeric promotion, the value itself remains unchanged.

???+ note "Note"
    The C-style variadic argument area performs default argument promotion during value passing. For example:
    
    ???+ note "Example code"
        ```c
        #include <stdarg.h>
        #include <stdio.h>
        
        void test(int tot, ...) {
          va_list valist;
          int i;
        
          // initialize the variadic argument list
          va_start(valist, tot);
        
          for (i = 0; i < tot; ++i) {
            // get the value of the i-th variable
            double xx = va_arg(valist, double);  // Correct
            // float xx = va_arg(valist, float); // Wrong
        
            // output the underlying storage content of the i-th variable
            printf("i = %d, value = 0x%016llx\n", i, *(long long *)(&xx));
          }
        
          // clean up the memory of the variadic argument list
          va_end(valist);
        }
        
        int main() {
          float f;
          double fd, d;
          f = 123.;   // 0x42f60000
          fd = 123.;  // 0x405ec00000000000
          d = 456.;   // 0x407c800000000000
          test(3, f, fd, d);
        }
        ```
    
    When calling `test`, `f` is promoted to `double`, so the underlying storage content is the same as `fd`, and the output is
    
    ```text
    i = 0, value = 0x405ec00000000000
    i = 1, value = 0x405ec00000000000
    i = 2, value = 0x407c800000000000
    ```
    
    If we change `double xx = va_arg(valist, double);` to `float xx = va_arg(valist, float);`, GCC should give a warning similar to the following:
    
    ```text
    In file included from test.c:2:
    test.c: In function 'test':
    test.c:14:35: warning: 'float' is promoted to 'double' when passed through '...'
      14 |         float xx = va_arg(valist, float);
         |                                   ^
    test.c:14:35: note: (so you should pass 'double' not 'float' to 'va_arg')
    test.c:14:35: note: if this code is reached, the program will abort
    ```
    
    At this time the program will terminate before output.
    
    This also explains why `printf`'s `%f` can match both `float` and `double`.

#### Integer promotion

A prvalue of a small integer type (such as `char`) can be converted to a prvalue of a larger integer type (such as `int`).

Specifically, arithmetic operators do not accept types smaller than `int` as their arguments, and after the lvalue-to-rvalue conversion, if applicable, integer promotion is automatically performed.

Specifically, there are the following rules:

-   When the source type is `signed char`, `signed short / short`, it can be promoted to `int`.
-   When the source type is `unsigned char`, `unsigned short`, if `int` can hold the value range of the source type, then it can be promoted to `int`, otherwise it can be promoted to `unsigned int`. (Since `C++20`, `char8_t` also applies to this rule)
-   The promotion rule of `char` depends on whether its underlying type is `signed char` or `unsigned char`.
-   The `bool` type can be converted to `int`: `false` becomes `0`, `true` becomes `1`.
-   If the value range of the target type contains the source type, and the value range of the source type cannot be contained by `int` and `unsigned int`, then the source type can be promoted to the target type.[^note12]

???+ warning "Note"
    `char`->`short` is not a numeric promotion, because `char` is first promoted to `int / unsigned int`, and then it is `int / unsigned int`->`short`, which does not satisfy the condition of numeric promotion.

For example (the following assumes `int` is 32-bit, `unsigned short` is 16-bit, `signed char` and `unsigned char` are 8-bit, `bool` is 1-bit)

-   `(signed char)'\0' - (signed char)'\xff'` first promotes `(signed char)'\0'` to `(int)0` and `(signed char)'\xff'` to `(int)-1`, then performs the operation between `int`s, and the final result is `(int)1`.
-   `(unsigned char)'\0' - (unsigned char)'\xff'` first promotes `(unsigned char)'\0'` to `(int)0` and `(unsigned char)'\xff'` to `(int)255`, then performs the operation between `int`s, and the final result is `(int)-255`.
-   `false - (unsigned short)12` first promotes `false` to `(int)0` and `(unsigned short)12` to `(int)12`, then performs the operation between `int`s, and the final result is `(int)-12`.

#### Floating-point promotion

A floating-point number of smaller bit width can be promoted to a floating-point number of larger bit width (for example, when a variable of type `float` and a variable of type `double` perform arithmetic operations, the `float`-type variable is promoted to a `double`-type variable), and its value remains unchanged.

### Numeric conversion

During numeric conversion, the value may change.

???+ warning "Note"
    Numeric promotion takes precedence over numeric conversion. For example, `bool`->`int` is a numeric promotion rather than a numeric conversion.

#### Integer conversion

<!-- scripts.linter.preprocess.fix_details off -->

-   If the target type is an unsigned integer type with bit width $x$, then the conversion result is the result of the original value $\bmod 2^x$.

    -   If the target type bit width is greater than the source type bit width:

        -   If the source type is a signed type, in general sign extension needs to be performed first before conversion.

            For example

            -   When converting `(short)-1` (`(short)0b1111'1111'1111'1111`) to the `unsigned int` type, sign extension is performed first, obtaining `0b1111'1111'1111'1111'1111'1111'1111'1111`, then integer conversion is performed, and the result is `(unsigned int)4'294'967'295` (`(unsigned int)0b1111'1111'1111'1111'1111'1111'1111'1111`).
            -   When converting `(short)32'767` (`(short)0b0111'1111'1111'1111`) to the `unsigned int` type, sign extension is performed first, obtaining `0b0000'0000'0000'0000'0111'1111'1111'1111`, then integer conversion is performed, and the result is `(unsigned int)32'767` (`(unsigned int)0b0000'0000'0000'0000'0111'1111'1111'1111`).

        -   If the source type is an unsigned type, then zero extension needs to be performed first before conversion.

            For example, when converting `(unsigned short)65'535` (`(unsigned short)0b1111'1111'1111'1111`) to the `unsigned int` type, zero extension is performed first, obtaining `0b0000'0000'0000'0000'1111'1111'1111'1111`, then integer conversion is performed, and the result is `(unsigned int)65'535` (`(unsigned int)0b0000'0000'0000'0000'1111'1111'1111'1111`).

    -   If the target type bit width is not greater than the source type bit width, then truncation needs to be performed first before conversion.

        For example, when converting `(unsigned int)4'294'967'295` (`(unsigned int)0b1111'1111'1111'1111'1111'1111'1111'1111`) to the `unsigned short` type, truncation is performed first, obtaining `0b1111'1111'1111'1111`, then integer conversion is performed, and the result is `(unsigned short)65'535` (`(unsigned short)0b1111'1111'1111'1111`).

-   If the target type is a signed integer type with bit width $x$, then **in general**, the conversion result can be regarded as the result of the original value $\bmod 2^x$.[^note13]

    For example, when converting `(unsigned int)4'294'967'295` (`(unsigned int)0b1111'1111'1111'1111'1111'1111'1111'1111`) to the `short` type, the result is `(short)-1` (`(short)0b1111'1111'1111'1111`).

-   If the target type is `bool`, then it is [boolean conversion](#boolean-conversion).

-   If the source type is `bool`, then `false` is converted to 0 of the corresponding type, and `true` is converted to 1 of the corresponding type.

<!-- scripts.linter.preprocess.fix_details on -->

#### Floating-point conversion

Converting a floating-point number of larger bit width to a floating-point number of smaller bit width rounds this number to the nearest value under the target type.

#### Floating-point integer conversion

-   When converting a floating-point number to an integer, the entire fractional part of the floating-point number is discarded.

    If the target type is `bool`, then it is [boolean conversion](#boolean-conversion).

-   When converting an integer to a floating-point number, it is rounded to the nearest value under the target type.

    If this value cannot fit into the target type, then the behavior is undefined.

    If the source type is `bool`, then `false` is converted to zero, and `true` is converted to one.

#### Boolean conversion

When converting other types to the `bool` type, a zero value is converted to `false`, and a non-zero value is converted to `true`.

## Defining variables

Simply put[^note14], defining a variable requires including a type specifier (indicating the type of the variable) and the variable name to be defined.

For example, the following statements are all variable definition statements.

```cpp
int oi;
double wiki;
char org = 'c';
```

In the program segments we have encountered so far, variables defined in places wrapped by braces are local variables, while variables defined in places not wrapped by braces are global variables. There are actually exceptions, but for now there is no need to understand them.

Global variables that are defined without an initialization value are initialized to $0$. But local variables do not have this characteristic; they need to be manually assigned an initial value, otherwise they may cause hard-to-find bugs.

## Variable scope

Scope is the code block in which a variable can play a role.

The scope of a global variable starts from its definition[^note15] and ends at the end of the file.

The scope of a local variable starts from its definition and ends at the end of the code block.

Several statements enclosed by a pair of braces constitute a code block.

```cpp
int g = 20;  // define a global variable

int main() {
  int g = 10;         // define a local variable
  printf("%d\n", g);  // output g
  return 0;
}
```

If a variable with the same variable name is defined in a nested block of a code block, then the inner block will be unable to access the variable with the same variable name in the outer block.

For example, in the above code, the value of $g$ output will be $10$. Therefore, to prevent unexpected errors, please try to avoid the situation where local variables and global variables have the same name.

## Constants

A constant is a fixed value that does not change during program execution.

The value of a constant cannot be modified after it is defined. Just add a `const` keyword at the time of definition.

```cpp
const int a = 2;
a = 3;
```

If we modify the value of a constant, an error will be reported in the compilation stage: `error: assignment of read-only variable 'a'`.

## References and notes

1.  [Working Draft, Standard for Programming Language C++](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2022/n4917.pdf)
2.  [Type - cppreference.com](https://zh.cppreference.com/w/cpp/language/type)
3.  The C language's [arithmetic types - cppreference.com](https://zh.cppreference.com/w/c/language/arithmetic_types)
4.  [Fundamental types - cppreference.com](https://zh.cppreference.com/w/cpp/language/types)
5.  [Fixed-width integer types (since C++11) - cppreference.com](https://zh.cppreference.com/w/cpp/types/integer)
6.  William Kahan (1 October 1997). ["Lecture Notes on the Status of IEEE Standard 754 for Binary Floating-Point Arithmetic"](https://people.eecs.berkeley.edu/~wkahan/ieee754status/IEEE754.PDF).
7.  [Implicit conversions - cppreference.com](https://zh.cppreference.com/w/cpp/language/implicit_conversion)
8.  [Declarations - cppreference](https://zh.cppreference.com/w/cpp/language/declarations)
9.  [Scope - cppreference.com](https://zh.cppreference.com/w/cpp/language/scope)

[^note10]: See <https://www.open-std.org/jtc1/sc22/wg14/www/docs/n3054.pdf>

[^note11]: Includes array types, reference types, pointer types, class types, function types, etc. Since this article is aimed at beginners, we do not give a specific introduction in this article. For specifics, please refer to [Type - cppreference.com](https://zh.cppreference.com/w/cpp/language/type)

[^note12]: Excludes wide character types, bit fields, and enumeration types; see [Integer conversion - cppreference](https://zh.cppreference.com/w/cpp/language/implicit_conversion#.E6.95.B4.E5.9E.8B.E8.BD.AC.E6.8D.A2) for details.

[^note13]: Takes effect since C++20. Before C++20 the result is implementation-defined. See [Integer conversion - cppreference](https://zh.cppreference.com/w/cpp/language/implicit_conversion#.E6.95.B4.E5.9E.8B.E8.BD.AC.E6.8D.A2) for details.

[^note14]: When defining a variable, besides the type specifier, other specifiers can also be included. See [Declarations - cppreference](https://zh.cppreference.com/w/cpp/language/declarations) for details.

[^note15]: A more accurate statement is the [point of declaration](https://zh.cppreference.com/w/cpp/language/scope#.E5.A3.B0.E6.98.8E.E7.82.B9).

[^note16]: Before C++20, it was stipulated that signed integers must at least cover the representation range of [ones' complement](../math/bit.md#integers-and-bit-sequences) (i.e. $-2^{x-1}+1\sim 2^{x-1}-1$), but in fact the vast majority of implementations use [two's complement](../math/bit.md#integers-and-bit-sequences); since C++20, it is further stipulated that signed integers must be implemented using two's complement. See [Range of values - cppreference](https://en.cppreference.com/w/cpp/language/types.html#Range_of_values) for details.
