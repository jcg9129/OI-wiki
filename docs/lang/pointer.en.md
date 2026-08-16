author: tsagaanbar, Enter-tainer, Xeonacid

## The address of a variable, pointers

In a program, our data all has its stored address. In each actual run of the program, the storage location of a variable in physical memory is not always the same. However, we can still, when programming, obtain the address of data in memory through certain statements.

An address is also data. The type of variable used to store addresses has a special name, called a "pointer variable", sometimes also abbreviated as "pointer".

???+ note "The size of a pointer variable"
    The size of a pointer variable differs in different environments. On a 32-bit machine, an address is represented by a 32-bit binary integer, so the size of a pointer is 4 bytes. On a 64-bit machine, an address is represented by a 64-bit binary integer, so the size of a pointer becomes 8 bytes.

An address is just a scale-like piece of data; in order to target different types of data, "pointer variables" also have different types. For example, there can be an `int`-type pointer variable, where the stored address (i.e. the value stored by the pointer variable) corresponds to the starting address of a space of size 32 bits; there can be a `char`-type pointer variable, where the stored address corresponds to the starting address of an 8-bit space.

In fact, the user can also declare a pointer variable pointing to a pointer variable.

Suppose the user defines a struct:

```cpp
struct ThreeInt {
  int a;
  int b;
  int c;
};
```

Then a `ThreeInt`-type pointer variable corresponds to a space of 3 × 32 = 96 bit.

## Declaration and use of pointers

In C/C++, the type of a pointer variable is the type name followed by an asterisk `*`. For example, the type name of an `int`-type pointer variable is `int*`.

We can use the `&` symbol to obtain the address of a variable.

To access the space corresponding to the address of a pointer variable (also called the space that the pointer **points to**), we need to **dereference** the pointer variable, using the `*` symbol.

```cpp
int main() {
  int a = 123;  // a: 123
  int* pa = &a;
  *pa = 321;  // a: 321
}
```

It is similar for struct variables. If you want to access a member in the struct that the pointer points to, you need to first dereference the pointer, then use the `.` member relation operator. However, it is more recommended to use the more convenient "arrow" operator `->` way of writing.

```cpp
struct ThreeInt {
  int a;
  int b;
  int c;
};

int main() {
  ThreeInt x{1, 2, 3}, y{6, 7, 8};
  ThreeInt* px = &x;
  (*px) = y;    // x: {6,7,8}
  (*px).a = 4;  // x: {4,7,8}
  px->b = 5;    // x: {4,5,8}
}
```

## Pointer offset

Pointer variables can also perform addition and subtraction operations **with integers**. For an `int` pointer, each time it adds 1 (increments by 1), the address it points to offsets by 32 bits (i.e. 4 bytes); if it adds 2, the address it points to offsets by 2 × 32 = 64 bits. Similarly, for a `char` pointer, each increment, the address it points to offsets by 8 bits (i.e. 1 byte).

### Using pointer offset to access an array

We said earlier that an array is a contiguous storage space. And in C/C++, directly using the array name gives the starting address of the array.

```cpp
int main() {
  int a[3] = {1, 2, 3};
  int* p = a;  // p points to a[0]
  *p = 4;      // a: [4, 2, 3]
  p = p + 1;   // p points to a[1]
  *p = 5;      // a: [4, 5, 3]
  p++;         // p points to a[2]
  *p = 6;      // a: [4, 5, 6]
}
```

When accessing elements in an array through a pointer, we often need to use "pointer offset"; in other words, access through a base address (the starting address of the array) plus an offset.

We often use the `[]` operator to access the element at a specified offset in an array. For example `a[3]` or `p[4]`. This way of writing is equivalent to performing an operation on the pointer and then referencing it, i.e. `p[4]` and `*(p + 4)` are two equivalent ways of writing.

## Null pointer

Before C++11, C++, like C, used the `NULL` macro to represent the null pointer constant; the implementation of `NULL` in C++ is generally as follows:

```cpp
// before C++11
#define NULL 0
```

???+ note "The C language's definition of `NULL`"
    Before C23, the C language has two definitions of `NULL`, differing only in type: one is an integer constant expression, and one is a constant expression converted to `void *` type, but both values are 0, and the compiler can choose any one to implement.

The mixed use of a null pointer and the integer `0` will cause many problems in C++, for example:

```cpp
int f(int x);
int f(int* p);
```

When calling `f(NULL)`, the type of the actually called function is `int(int)` rather than `int(int *)`.

???+ note "The problem caused by `NULL` in the C language"
    Compared with in C++, because there are two definitions, the problem caused by `NULL` in the C language is more serious: if in a function that passes variadic arguments, the function author wants to accept a pointer, but the function caller passes a `NULL` defined as an integer, then it will cause undefined behavior, because when using the passed-in variadic argument inside the function, a type conversion is performed, and the conversion from integer to pointer type is undefined behavior.[^note1]

To solve these problems, C++11 introduced the `nullptr` keyword as the null pointer constant.

C++ stipulates that `nullptr` can be implicitly converted to any pointer type, and the result of this conversion is the null pointer value of that type.

The type of `nullptr` is `std::nullptr_t`, called the null pointer type; a possible implementation is as follows:

```cpp
namespace std {
typedef decltype(nullptr) nullptr_t;
}
```

In addition, since C++11 the implementation of the `NULL` macro has also been modified to:

```cpp
// since C++11
#define NULL nullptr
```

???+ note "The C language's improvement to the null pointer constant"
    Based on similar reasons, C23 also introduced `nullptr` as the null pointer constant, and introduced `nullptr_t` as its type[^note1].

## Advanced use of pointers

Using pointers, the program writer can operate on data at various places during the program's runtime, without being limited to the scope.

### Use of pointer-type parameters

In C/C++, the parameters used when calling a function (procedure) are all passed into the sub-procedure in the form of copies (except references, which will be introduced later). By default, a function can only return a result to the call site through the return value. But, if a function wants to modify data outside it, or the data amount of a certain struct/class is relatively large and is not suitable for copying, then at this time, by passing the address of the external data into it, we can access or even modify the external data within it.

The following `my_swap` method, by receiving two `int`-type pointers, uses an intermediate variable in the function to complete the exchange of the values of two `int`-type variables.

```cpp
void my_swap(int *a, int *b) {
  int t;
  t = *a;
  *a = *b;
  *b = t;
}

int main() {
  int a = 6, b = 10;
  my_swap(&a, &b);
  // after the call, the value of the a variable in the main function becomes 10, and the value of the b variable becomes 6
}
```

C++ introduces the concept of references, which, compared with pointers, are easier to use and safer. For details, see [C++: references](./reference.md) and [Differences between C and C++: pointers and references](./cpp-other-langs.md#pointers-and-references).

### Dynamic instantiation

Besides this, when writing programs, we often involve dynamic memory allocation, i.e. the program will, at runtime, dynamically request or return the memory needed to store data from the operating system. When the program requests memory by calling the operating system interface, the operating system will return the address of the space requested by the program. To use this space, we need to store the address of this space in a pointer variable.

In C++, we use the `new` operator to obtain a block of memory, and use the `delete` operator to release the space pointed to by a certain pointer.

```cpp
int* p = new int(1234);
/* ... */
delete p;
```

The above statements use the `new` operator to request a space of `int` size from the operating system, initialize the value in it to 1234, and declare an `int`-type pointer `p` pointing to this space.

Similarly, we can also use `new` to allocate a new object:

```cpp
class A {
  int a;

 public:
  A(int a_) : a(a_) {}
};

int main() {
  A* p = new A(1234);
  /* ... */
  delete p;
}
```

As above, the "`new` expression" will try to allocate a space of the corresponding size, and try to construct this object on this space, and return the address of this space.

```cpp
struct ThreeInt {
  int a;
  int b;
  int c;
};

int main() {
  ThreeInt* p = new ThreeInt{1, 2, 3};
  /* ... */
  delete p;
}
```

???+ note "List initialization"
    The `{}` operator can be used to initialize a struct without a constructor. Besides this, using the `{}` operator can make the initialization form of variables uniform. See "[list initialization (since C++11)](https://en.cppreference.com/w/cpp/language/list_initialization)" for details.

Note that when the memory requested with `new` is no longer used, we need to use `delete` to release this space. We cannot release a block of memory twice or more. And using the `delete` operation on the null pointer `nullptr` is legal.

### Dynamically creating an array

We can also use the `new[]` operator to create an array; at this time the `new[]` operator will return the first address of the array, i.e. the address of the first element of the array, and we can store this address with a pointer of the corresponding type. When releasing, we need to use the `delete[]` operator.

```cpp
size_t element_cnt = 5;
int *p = new int[element_cnt];
delete[] p;
```

The storage of elements in an array is contiguous, i.e. what `p + 1` points to is the successor element of `p`.

### Two-dimensional array

When storing data in matrix form, we may use the "two-dimensional array" data type. Semantically speaking, a two-dimensional array is an array of arrays. And computer memory can be regarded as a very long one-dimensional array. To store a two-dimensional array in computer memory, there is the concept of "contiguous" or not.

The so-called "contiguous" means that the end of any row (row) of the two-dimensional array is adjacent to the start of the next row in physical address; in other words, the whole two-dimensional array can be regarded as a one-dimensional array; conversely, the two are not necessarily physically adjacent.

For a "contiguous" two-dimensional array, we can use only one loop, and traverse all data in the array by means of a continuously incrementing pointer. And for a non-contiguous two-dimensional array, since each row is not contiguous, we need to first obtain the address of the beginning of a certain row, and then access the elements in this row.

???+ note "The storage method of a two-dimensional array"
    This way of storing data by "row (row)" is called row-major storage; correspondingly, we can also store data by column (column). Due to the characteristics of computer memory access, generally speaking, accessing contiguous data will obtain higher efficiency. Therefore, we need to choose the "row-major" or "column-major" storage method according to the possible way the data is used.

### Dynamically creating a two-dimensional array

In C/C++, we can use a statement similar to the following to declare a two-dimensional array with N rows and M columns, whose space is physically contiguous.

???+ note "Describing the dimensions of an array"
    A more general way is to use the "the n-th dimension (dimension)" phrasing. For the "row-major" storage form, the length of the first dimension of the array is N, and the length of the second dimension is M.

```cpp
int a[N][M];
```

This declaration method requires N and M to be constant expressions that can be determined at compile time.

In C/C++, the first element of an array has subscript 0, so an expression like `a[r][c]` represents the c + 1-th element of the r + 1-th row in the two-dimensional array a; we also call the subscript of this element `(r,c)`.

However, in actual use, the size of a (two-dimensional) array may not be fixed and requires dynamic memory allocation.

A common way is to declare a **one-dimensional array** of length N × M, and access the element with subscript `(r, c)` in the two-dimensional array through the subscript `r * M + c`.

```cpp
int* a = new int[N * M];
```

This method can guarantee that the two-dimensional array is **contiguous**.

???+ note "The linear storage of arrays at the physical level"
    In fact, data in memory can all be regarded as stored linearly, so under certain rules, by dynamically allocating the space of a one-dimensional array, we can store an n-dimensional array on it.

In addition, we can also obtain and use memory according to the concept of "array of arrays". For an array storing several arrays, it is actually an array storing the first addresses of several arrays, i.e. an array storing several pointer variables.

We need a variable to store the first address of this "array of arrays"—that is, the address of a pointer. This variable is a "pointer to a pointer", sometimes also called a "double pointer", such as:

```cpp
int** a = new int*[5];
```

Next, we need to request space for each array:

```cpp
for (int i = 0; i < 5; i++) {
  a[i] = new int[5];
}
```

At this point, we have completed the acquisition of memory. And for the release of the memory obtained this way, we need to perform a reverse operation: i.e. first release each array, then release the array storing the first addresses of these arrays, such as:

```cpp
for (int i = 0; i < 5; i++) {
  delete[] a[i];
}
delete[] a;
```

Note that the two-dimensional array obtained this way cannot be guaranteed to have contiguous space.

There is also another way, which needs to use a "pointer to an array".

???+ note "The difference between the array name and the address of the first element of the array"
    We said before that in C/C++, directly using the array name, the value equals the address of the first element of the array. But the type of the variable represented by the array name is actually the entire array, rather than a single element.
    
    ```cpp
    int main() { int a[5] = {1, 2, 3, 4, 5}; }
    ```
    
    Conceptually, the type of the identifier `a` in the code is `int[5]`; in practice, the offset of the address that `a + 1` points to relative to the address that `a` points to is the length of 5 `int`-type variables.

```cpp
int main() {
  int(*a)[5] = new int[5][5];
  int* p = a[2];
  a[2][1] = 1;
  delete[] a;
}
```

The memory obtained this way is also contiguous, but we can directly use the form `a[n]` to obtain the first address of the n + 1-th row (row) of the array, so using the form `a[r][c]` can access the element with subscript `(r, c)`.

Since a pointer to an array is also a definite data type, except for the first dimension of the array, the lengths of the other dimensions must all be a constant that can be determined at compile time. Otherwise, the compiler will be unable to translate expressions such as `a[n]` (`a` being a pointer to an array).

## Pointers to functions

For an introduction to functions, see the [C++ functions](./func.md) chapter.

Simply put, to call a function, we need to know the parameter types, number, and return value type of that function; these are also collectively called the interface type.

We can call a function through a function pointer. Sometimes, if the interface types of several functions are the same, using a function pointer can, according to the running of the program, **dynamically** choose the function to be called. In other words, we can, without modifying a function, make the behavior of that function change only by modifying the parameter (function pointer) passed into it.

Suppose we have several binary operation functions for the `int` type, then the parameters of the functions are 2 `int`s, and the return value is also `int`. Below is an example using a function pointer:

```cpp
#include <iostream>

int (*binary_int_op)(int, int);

int foo1(int a, int b) { return a * b + b; }

int foo2(int a, int b) { return (a + b) * b; }

int main() {
  int choice;
  std::cin >> choice;
  if (choice == 1) {
    binary_int_op = foo1;
  } else {
    binary_int_op = foo2;
  }

  int m, n;
  std::cin >> m >> n;
  std::cout << binary_int_op(m, n);
}
```

???+ note "`&`, `*`, and function pointers"
    In the C language, ways of writing such as `void (*p)() = foo;`, `void (*p)() = &foo;`, `void (*p)() = *foo;`, `void (*p)() = ***foo` all have the same result.
    
    Because a function (such as `foo`) can be implicitly converted to a pointer to a function, the way of writing `void (*p)() = foo;` can hold.
    
    Using the `&` operator can obtain the address of an object, and this also holds for functions, so the way of writing `void (*p)() = &foo;` still holds.
    
    Using the `*` operator on a function pointer can obtain the function that the pointer points to, and for a way of writing such as `**foo`, `*foo` obtains the function `foo`, which is then immediately implicitly converted to a pointer to `foo`. And so on, `**foo` still ultimately obtains a function pointer to `foo`; the user can use any number of `*`, and the result is the same.
    
    Similarly, when calling, using statements like `(*p)()` and `p()` are the same; the `*` operator can be omitted.
    
    Reference: [Why do function pointer definitions work with any number of ampersands '&' or asterisks '\*'? - stackoverflow.com](https://stackoverflow.com/questions/6893285/why-do-function-pointer-definitions-work-with-any-number-of-ampersands-or-as)

We can use the `typedef` keyword to declare the type of a function pointer.

```cpp
typedef int (*p_bi_int_op)(int, int);
```

This way we can later use the `p_bi_int_op` type, i.e. a pointer to a function whose "parameters are 2 `int`s and whose return value is also `int`".

We can use `std::function` to reference functions more conveniently. (To be continued)

Using function pointers, we can implement "callback functions". (To be continued)

## References and notes

[^note1]: See [Introduce the nullptr constant](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n3042.htm)
