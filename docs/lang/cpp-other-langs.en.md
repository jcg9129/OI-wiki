This article introduces the differences between C++ and other commonly used languages, focusing on the important or easily overlooked differences between C and C++. Although C++ is almost a superset of C, and mixing C/C++ code is generally fine, understanding the relatively important differences between C/C++ can avoid encountering some strange bugs. If you are an OIer who uses C as your main language, then this article can also help you get started with C++ more smoothly. For the unique features added by C++ compared to C, you can read the tutorial in the [Advanced C++](./class.md) part. In addition, this article also briefly introduces the differences between Python, Java, and C++.

## Differences between C and C++

### Macros and templates

One purpose of C++ templates at the time of their design was to replace macro definitions. Learning template programming is an important step from C toward C++. Unlike the textual replacement of macros, templates receive more comprehensive compiler checks at compile time, facilitating the writing of more robust code. The template feature after C++11 supports a variable-length template parameter list, which can be used to replace variable-length functions in C while ensuring type safety.

### Pointers and references

In C++ you can still use C-style pointers, but for variable passing, it is more recommended to use the C++ [reference](./reference.md) feature to achieve similar functionality. Since the object pointed to by a reference cannot be null, it can avoid some null-address access problems. However, pointers, due to their flexibility, still have their uses. It is worth mentioning that the `NULL` null pointer in C has a type-safe replacement `nullptr` starting from C++11. References and pointers can be converted to each other through the [`*` and `&` operators](./op.md).

### bool

See also [Boolean type](var.md#boolean-type).

Unlike C++, the C language originally did not have a boolean type.

The C99 standard added the `_Bool` keyword (as well as the equivalent `bool` macro) and the two macros `true` and `false`. If you need to use the three macros `bool`, `true`, `false`, you need to include the `stdbool.h` header file in the program. Using `_Bool` does not require including any additional header files.

```c
bool x = true;  // requires including stdbool.h
_Bool x = 1;    // does not require including stdbool.h
```

Starting from C23, `true`, `false`, and `bool` become keywords in the C language; using them no longer requires including the `stdbool.h` header file, while `_Bool` is retained as an alternative spelling of `bool`[^boolean-keyword].

The following table shows the changes in bool type support under different standards of the C language (for comparison, the support situation of C++ is added):

| Language standard | `bool` | `true`/`false` | `_Bool` |
| ------------ | --------------------------------- | ----------------------------------------------------- | ------------------------- |
| C89 | / | / | reserved[^reserved-identifiers] |
| C99 up to before C23 | macro, equivalent to `_Bool`, requires the `stdbool.h` header file | macro, `true` equivalent to `1`, `false` equivalent to `0`, requires the `stdbool.h` header file | keyword |
| C23 onward | keyword | keyword | alternative spelling of the keyword `bool` |
| C++ | keyword | keyword | reserved[^reserved-identifiers] |

### struct

Although the concept of struct exists in both C and C++, what they correspond to cannot be mixed! The struct in C is used to describe a fixed memory organization structure, while the struct in C++ is a kind of class, **the only difference between it and a class is that its members and inheritance behavior are public by default**, while the default members of a general class are private. This is especially fatal when writing mixed C/C++ code.

In addition, when declaring a struct, C++ also does not need to be as cumbersome as C; the C version:

```c
typedef struct Node_t {
  struct Node_t *next;
  int key;
} Node;
```

The C++ version

```cpp
struct Node {
  Node *next;
  int key;
};
```

### const

const in C only has the function of qualifying that a variable cannot be modified, while in C++, due to the emergence of a large number of new features, const is also given more usages. The successor of C's const in C++ is constexpr, and for the usage of const in C++ see the explanation on the [const](./const.md) page.

### Memory allocation

C++ adds the `new` and `delete` keywords for allocating space on the "free store"; this free store can be either the heap or the static storage area; they appeared to cooperate with "classes". Among them, `delete[]` can also directly release the memory of a dynamic array, which is very convenient. The `new` and `delete` keywords call the constructor and destructor of the type; compared with the `malloc()`, `realloc()`, `free()` functions in C, they have more complete support for types, but their efficiency is not as good as these functions in C.

In short, if the object for which you need to dynamically allocate memory is a basic type or an array of them, then you can use `malloc()` for more efficient memory allocation; but if the object you create is a non-basic type, then it is recommended to use `new` to obtain safety checks. It is worth noting that although both `new` and `malloc()` return pointers, the pointer from `new` can **only** be reclaimed with `delete`, and the pointer from `malloc()` can only be reclaimed with `free()`, otherwise there is a risk of memory leak.

### Variable declaration

Before C99, C variable declarations must be located at the beginning of a statement block; C++ and C99 onward have no such restriction.

### Variable-length arrays

After C99, the C language supports VLA (variable-length arrays), which C++ never supports.

### Struct initialization

After C99, the C language supports [designated initialization](https://en.cppreference.com/w/c/language/struct_initialization) of structs (but it is an optional feature in C11); C++ did not support ordered designated initialization until C++20, and C++ does not support the out-of-order, nested, mixed-with-ordinary-initializer, and array designated-initialization features that the C language supports[^cpp-designated-init].

### Comment syntax

The C++ style single-line comment `//` was not supported by C before C99.

## Differences between Python and C++

Python is currently the most commonly used language in the machine learning community. Compared with C++, the advantage of Python lies in being easy to learn and easy to practice. Python has a simpler and more direct syntax; for example, when defining a variable, there is no need to declare the variable type in advance. However, such simplicity also comes at a cost. Compared with C++, Python sacrifices performance. C++ is applicable to almost all platforms including embedded systems, and has faster execution speed, but Python can only be used on certain platforms that support high-level languages. C++ is closer to the low level, so it can be used to write operating systems.

## Differences between Java and C++

Java and C++ are both object-oriented languages, both using object-oriented ideas (encapsulation, inheritance, polymorphism); since object orientation has many very good features (inheritance, composition, etc.), the two have good reusability. So compared with Python, Java and C++ are more similar.

The biggest difference between the two lies in Java's JVM mechanism. JVM stands for Java Virtual Machine. A very important characteristic of the Java language is platform independence. And using the Java Virtual Machine is the key to achieving this characteristic. Generally, if a high-level language is to run on different platforms, it needs to at least be compiled into different object code. But after introducing the Java Virtual Machine, the Java language does not need to be recompiled when running on different platforms. The Java language uses the Java Virtual Machine to shield information related to the specific platform, so that a Java-language compiled program only needs to generate object code (bytecode) that runs on the Java Virtual Machine, and it can run on multiple platforms without modification.

Because of this characteristic, Java is often used for the development of programs that need to be ported to different platforms. But also because compiling a Java program needs to start from bytecode, the performance of Java is not as good as C++.

## References

[^cpp-designated-init]: <https://en.cppreference.com/w/cpp/language/aggregate_initialization>

[^boolean-keyword]: <https://www.open-std.org/jtc1/sc22/wg14/www/docs/n3054.pdf>.

[^reserved-identifiers]: Both C and C++ stipulate that an identifier starting with an underscore followed by an uppercase letter is reserved; see <https://en.cppreference.com/w/c/language/identifier> for details.
