## The C++ standard

The first thing that needs to be introduced is the version of C++ itself. Since C++ itself is just a language, and different compilers implement C++ in different ways, standardization is needed to constrain compiler implementations, so that C++ code behaves consistently under different compilers. Since C++ was born in 1985, a total of 7 official C++ standards have been released by the International Organization for Standardization (ISO), namely C++98, C++03, C++11 (also known as C++0x), C++14 (also known as C++1y), C++17 (also known as C++1z), C++20 (also known as C++2a), and C++23 (also known as C++2b). The C++ standard drafts are on the [open-std](http://www.open-std.org/jtc1/sc22/wg21/docs/papers/) website, and the progress of the latest standard can be viewed at [Current Status : Standard C++](https://isocpp.org/std/status). In addition, there are some supplementary standards, such as C++ TR1.

Each version of the C++ standard not only specifies the syntax and language features of C++, but also specifies a set of implementation specifications for the C++ built-in library; this library is the C++ standard library. The C++ standard library contains implementations of a large number of commonly used pieces of code, such as input/output, basic data structures, memory management, multithreading support, etc. Mastering the C++ standard library is a necessary step to writing more modern C++ code. The detailed documentation of the C++ standard library is on the [cppreference](https://zh.cppreference.com/) website; the documentation introduces the usage, efficiency, points of caution, etc. of the types and functions in the standard library, so please make good use of it.

It should be pointed out that different OJ platforms all have different C++ versions; for example, the [latest ICPC contest rules](https://docs.icpc.global/worldfinals-programming-environment/) support the C++20 standard. According to the resolution of the NOI Scientific Committee, starting from September 1, 2021, [NOI Linux 2.0](https://www.noi.cn/gynoi/jsgz/2021-07-16/732450.shtml) is used as the standard environment for NOI series contests and activities such as CSP-J/S. The g++ 9.3.0 specified in NOI Linux 2.0 [supports by default](https://gcc.gnu.org/projects/cxx-status.html#cxx14) the C++14 standard, and supports the C++17 standard, which can meet the needs of the vast majority of competition contestants. Therefore, when learning C++, pay attention to the standard supported by the contest, to avoid compilation errors on the field.

## Standard Template Library (STL)

STL, i.e. the Standard Template Library, is a part of the C++ standard library; it contains some templated general-purpose data structures and algorithms. Due to its templated characteristics, it can be compatible with custom data types, avoiding a lot of wheel-reinventing work. Both NOI and ICPC contests support the use of the STL library, so reasonable use of STL can avoid writing useless algorithms, and fully use the compiler's optimization of the template library to improve efficiency. For a detailed introduction to the STL library, see the corresponding pages: [STL containers](./container.md) and [STL algorithms](./algorithm.md).

??? note "What is reinventing the wheel"
    Reinventing the wheel ([Reinventing\_the\_wheel](https://en.wikipedia.org/wiki/Reinventing_the_wheel)) refers to repeatedly inventing an existing algorithm, or repeatedly writing ready-made optimized code. Reinventing the wheel is usually time-consuming and laborious, and the effect is not as good as others'. But if it is for learning or practice, then reinventing the wheel is necessary.

## Boost library

[Boost](https://www.boost.org/) is, besides the standard library, another long-renowned open-source C++ toolkit; its code has characteristics such as portability, high quality, high performance, and high reliability. The number of modules in Boost is very large, the functionality is comprehensive, and it has complete cross-platform support, so it is regarded as a quasi-standard library of C++. Quite a few features in the C++ standard also come from Boost, such as smart pointers, metaprogramming, date and time, etc. Although Boost cannot be used in OI, there are quite a few wheels in Boost that can be used to verify algorithms or do brute-force comparison; for example, Boost.Geometry has an implementation of the R-tree, Boost.Graph has graph-related algorithms, and Boost.Intrusive provides a set of intrusive containers with usage similar to STL containers. Interested readers can search for tutorials online on their own.

## References

1.  [C++ reference](https://en.cppreference.com/)
2.  [C++ reference manual](https://zh.cppreference.com/)
3.  [Wikipedia - C++](https://zh.wikipedia.org/wiki/C%2B%2B)
4.  [Boost official website](https://www.boost.org/)
5.  [Boost tutorial website](https://theboostcpplibraries.com/)
