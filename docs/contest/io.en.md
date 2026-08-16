author: Marcythm, YZircon, Chaigidel, Tiger3018, voidge, H-J-Granger, ouuan, Enter-tainer, lcfsih, Xeonacid, Ir1d

This article introduces how to optimize stream-based I/O and C-style I/O.

???+ note "Note"
    The actual speed of stream-based I/O and C-style I/O varies to some extent with the environment (such as the compiler, operating system, and hardware specifications). If you want to do a further analysis, take experimental results as authoritative. But be careful with variable control in experiments, avoiding wrong conclusions caused by multiple variables.

## Stream-based I/O

For stream-based I/O (such as `std::cin` and `std::cout`), the most commonly used optimization methods are turning off synchronization with the C streams and untying the input and output streams.

### Turning off synchronization

Use the [`std::ios::sync_with_stdio(false)`](https://en.cppreference.com/w/cpp/io/ios_base/sync_with_stdio) function to turn off synchronization with the C streams. To be compatible with C—that is, to ensure the program does not get confused when using both `printf` and `std::cout`—C++ synchronizes these two kinds of streams. A synchronized C++ stream is guaranteed to be thread-safe.

This is actually a conservative measure C++ takes for compatibility. If synchronization is on, at each I/O operation the C++ stream immediately applies this operation to the corresponding C buffer; but if the code does not involve C-style I/O, this operation is redundant. Therefore you can turn off synchronization with the C streams before doing I/O operations, but after doing so, note that in the subsequent code you cannot use both `std::cin` and `scanf`, nor both `std::cout` and `printf`; however, you can use both `std::cin` and `printf`, and you can use both `scanf` and `std::cout`.

### Untying

Use the [`tie()`](https://en.cppreference.com/w/cpp/io/basic_ios/tie) function to untie the input stream from the output stream.

By default, `std::cin` is tied to `&std::cout`, so every time formatted input is performed, `std::cout.flush()` must be called to clear the output buffer, which increases the I/O burden. You can untie them via `std::cin.tie(nullptr)` to further speed up execution.

???+ warning "Note"
    When using it, you must not omit the argument and write `std::cin.tie()`, as this does not untie them but returns the output stream tied to `std::cin`. And there is no need to do `std::cout.tie(nullptr)`, because by default no other output stream is tied to `std::cout`.

### Implementation

```cpp
std::ios::sync_with_stdio(false);
std::cin.tie(nullptr);
```

???+ note "Note"
    After both of the above operations, the program must manually `flush` to ensure that the content displayed by each `std::cout` can appear before `std::cin`. This is because in this case `std::cout` will not automatically flush the buffer when `std::cin` is called. For example:
    
    ```cpp
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout << "Please input your name: "
              << std::flush;  // or: std::endl;
                              // because each call to std::endl flushes the output buffer, while \n
                              // does not.
    // if std::flush is removed, the prompt message will not be displayed before the name is entered
    std::cin >> name;
    ```

## C-style I/O

`scanf` and `printf` still have room for efficiency improvement, and the improvement methods are all based on conversion between integers and strings.

???+ note "Note"
    The input and output optimizations introduced on this page are all for integer data. Optimizing the input and output of floating-point numbers is very complex; for input-related optimization refer to the [Bellerophon algorithm](https://dl.acm.org/doi/10.1145/93542.93557), and for output-related optimization refer to the [Ryū algorithm](https://dl.acm.org/doi/10.1145/3192366.3192369).

### Implementation design

???+ note "Note"
    The current optimization methods focus on faster I/O, while using naive methods in the data-conversion process without fully exploiting hardware features. Nowadays the vast majority of x86-architecture CPUs support the AVX2 instruction set, and one can use SIMD to accelerate conversion between integers and strings. Standard-library functions do not use SIMD optimization; for example, libstdc++'s [implementation](https://github.com/gcc-mirror/gcc/blob/releases/gcc-14.3.0/libstdc%2B%2B-v3/include/bits/charconv.h#L81) converts two consecutive digits at a time and converts them to characters via a lookup table, so optimizing the data-conversion process may also bring benefits. But within the competition scope, the optimization methods mentioned in this article are already enough for the vast majority of scenarios.

#### Input optimization

Each integer consists of two parts, a sign and digits, and the sign must come before the digit part, so the sign part is read in first. For the sign part, the `+` of a positive integer is usually omitted and does not affect the value represented by the digits that follow, whereas `-` cannot be omitted, so it must be checked. If the input contains no negative integers, this check can be omitted. For the digit part, it contains only the digits 0 to 9, so when a character that should not appear in an integer (usually a space) is read, one can determine that the integer has finished being read.

When reading, since the digits are read from left to right, Horner's method (Qin Jiushao's algorithm) can conveniently be used for the integer conversion. So the entire conversion process can be combined with the input.

While reading the digit part, one needs to determine whether the read character is a decimal digit character. One can simply use the condition `ch >= '0' && ch <= '9'`, or use the [`isdigit()`](https://en.cppreference.com/w/cpp/string/byte/isdigit) function.

#### Output optimization

When outputting, the integer needs to be converted into a string; the naive algorithm is generally used, i.e. directly computing each digit of the integer from low to high, converting them to characters, and outputting them in reverse order.

### Implementation details

#### The integer-overflow problem

In the implementation, one needs to be careful about integer overflow. For example, in output optimization, inappropriately negating a number causes the minimum value of an integer type to exceed the maximum value this integer type can represent after negation, which may lead to wrong output. A similar overflow may occur when reading the minimum value of an integer type, but in this case it may not lead to wrong input data, because the value obtained from overflow may equal the actual input value.

Signed-integer overflow is undefined behavior; in the implementation, one can use the property that negative-integer division in C rounds toward zero to avoid the above problem. But if there is no need to input or output negative numbers, or it is impossible to input or output the minimum value of this integer type, this problem will not arise.

#### Improving the generality of the implementation

If the program uses integer variables of multiple types, one may need to implement multiple input/output functions with different types but the same logic. In this case, one can use C++ [`template`](https://en.cppreference.com/w/cpp/language/templates.html) to implement input/output optimization for all integer types. For example, under the C++11 standard, define the function with

```cpp
template <typename T>
typename std::enable_if<std::is_integral<T>::value &&
                        std::is_signed<T>::value>::type
read(T &x);
```

or under the C++20 standard with

```cpp
template <std::signed_integral T>
void read(T &x);
```

For ease of reading, the implementations below assume that only `int`-type integers need to be read; these implementations are already enough for the needs of most problems.

### Implementation

Mainstream implementations differ only in the input/output functions used, and the logic of the integer-conversion part is the same. Below we introduce them according to the input/output functions each implementation uses.

#### Implementation using `getchar` and `putchar`

The core code is as follows.

```cpp
--8<-- "docs/contest/code/io/io_1.cpp:core"
```

#### Implementation using `fread` and `fwrite`

Faster input/output can be achieved via `fread` and `fwrite`. Their function signatures are as follows.

```cpp
std::size_t fread(void* buffer, std::size_t size, std::size_t count,
                  std::FILE* stream);
std::size_t fwrite(const void* buffer, std::size_t size, std::size_t count,
                   std::FILE* stream);
```

For example, `fread(Buf, 1, SIZE, stdin)` reads `SIZE` data blocks of size 1 byte from standard input into `Buf`. The return value indicates how many bytes of data were successfully read.

Since `fread` and `fwrite` read and write in whole segments, they have a speed advantage over `getchar()` and `putchar()`. If the buffer is large enough, the entire file can be read at once. But if the buffer is not large enough, multiple reads are needed to ensure all input content is read. To implement this, one only needs to redefine `getchar`.

```cpp
char buf[1 << 20], *p1, *p2;
#define gc()                                                               \
  (p1 == p2 && (p2 = (p1 = buf) + fread(buf, 1, 1 << 20, stdin), p1 == p2) \
       ? EOF                                                               \
       : *p1++)
```

Output is similar to input: first put the output content into a buffer, and finally output the buffer's content all at once via `fwrite`.

The core code is as follows.

```cpp
--8<-- "docs/contest/code/io/io_2.cpp:core"
```

Note when using this method:

-   When the debug switch is off, use `fread()`, `fwrite()`, and automatically run `fwrite()` during destruction on exit. When the debug switch is on, use `getchar()`, `putchar()` for convenient debugging.
-   For file reading/writing, add `freopen()` before all reading/writing.

#### Implementation using `mmap`

`mmap` is a Linux system call that can map a file into memory all at once, similar to a memory region that can be referenced by a pointer, with better speed in some scenarios. Its function signature is as follows:

```c
void *mmap(void addr[.length], size_t length, int prot, int flags, int fd,
           off_t offset);
```

???+ warning "Note"
    `mmap` cannot be used in a Windows environment (such as the judging systems of CodeForces and HDU), and is also not recommended for use in an official contest. In fact, `fread` is already fast enough, and if `mmap` is used to repeatedly read a small file, the overhead of doing a memory mapping once and having the kernel handle page faults is far greater than the overhead of using `fread`.

First obtain the file descriptor `fd`, then obtain the file size via `fstat`, and after that obtain the pointer `*pc` of the file mapped into memory via `mmap`. Afterward you can directly use `*pc++` to replace `getchar()` for file reading.

If you need to read from standard input, you can set `fd` to `0`. **However, using mmap on standard input is extremely dangerous behavior, and input cannot come from a terminal; you can choose to redirect a file to standard input.**

???+ note "Example: [Luogu P10815 【Template】Fast Input](https://www.luogu.com.cn/problem/P10815)"
    Read $n$ integers in the range $[-n, n]$, compute the sum, and output it, where $n \leq 10^8$. The data guarantees that for any prefix of the sequence, the sum of this prefix is within the storage range of a $32$-bit signed integer.

The reference code is as follows.

```cpp
--8<-- "docs/contest/code/io/io_3.cpp"
```

## References

[Accelerating I/O with cin.tie and sync\_with\_stdio - hankcs](https://www.hankcs.com/program/cpp/cin-tie-with-sync_with_stdio-acceleration-input-and-output.html)

[C++ Speed-up - Heavy Watal](https://heavywatal.github.io/cxx/speed.html)

['Re: mmap/mlock performance versus read' - MARC](https://marc.info/?l=linux-kernel&m=95496636207616&w=2)
