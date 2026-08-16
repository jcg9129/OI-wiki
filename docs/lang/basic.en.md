## Code framework

If you do not want to delve into the principles behind it, when starting out you can directly memorize this "framework":

```cpp
#include <cstdio>
#include <iostream>

int main() {
  // do something...
  return 0;
}
```

??? note "What is include?"
    `#include` is actually a preprocessor command, meaning to "place" a file at this statement; the file being "placed" is called a header file. That is to say, at compile time, the compiler will "copy" the content of the header file `iostream` and "paste" it at the statement `#include <iostream>`. This way, you can use objects such as `std::cin`, `std::cout`, `std::endl`, etc. provided in `iostream`.
    
    If you have learned the C language, you will find that the header files in C++ we have encountered so far generally do not carry the `.h` suffix, and those C language header files `xx.h` have all become `cxx`, for example `stdio.h` becomes `cstdio`. This is because C++, in order to remain compatible with C, directly uses the header files in the C language; to distinguish C++ header files from C header files, the `c` prefix is used.
    
    Generally speaking, you should determine which header files to `#include` according to the needs of the C++ program you need to write. But if you `#include` redundant header files, it will only increase the compile time and will almost have no effect on the run time. So far we have only encountered the two header files `iostream` and `cstdio`; if you only need `scanf` and `printf`, you can do without `#include <iostream>`.
    
    Can we `#include` a header file we wrote ourselves? The answer is, yes.
    
    You can write a header file yourself, such as `myheader.h`. Then, place it in the same directory as your code, and `#include "myheader.h"`. Note that a custom header file needs to use quotation marks instead of angle brackets. Of course, you can also use the compilation command `-I <header_file_path>` to tell the compiler where to find the header file, and then you do not need to place the header file in the same directory as the code.

??? note "What is `main()`?"
    It can be understood that the code in `main()` will be executed when the program runs.
    
    In fact, the `main` function is called by the system or an external program. For example, when you call your program on the command line, you call the `main` function in your program (before this, the construction of global [variables](./var.md) is first completed).
    
    The final `return 0;` indicates that the program ran successfully. By default, returning 0 when the program ends indicates everything is normal, otherwise the return value indicates an error code (on Windows, the hexadecimal of this error code can be looked up on the [Windows Error Codes website](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-erref/)). To whom is this value returned? It is actually returned to the system or external program that called the program you wrote, which will receive this return value when your program ends. If you do not write a `return` statement, the default return value of a normally-ending program is also 0.
    
    In C or C++, a program return value that is not 0 will cause a runtime error (RE).

## Comments

In C++ code, there are two ways to write comments:

1.  Inline comment

    Starting with `//`, all content in the line after it is a comment.

2.  Comment block

    Starting with `/*` and ending with `*/`, all content in between is a comment, which can span multiple lines.

Comments have no effect on program execution; they can be used to explain the meaning of the program, and can also be used to make a certain piece of code not execute (but still be retained in the source file).

In engineering development, comments can facilitate future maintenance and reading by others.

In OI, few people write many comments, but comments can facilitate clarifying one's thoughts while writing code, or facilitate future review. Moreover, if you want to write problem solutions or tutorials, an appropriate amount of comments can facilitate readers in reading and understanding the intent of the code. I hope everyone can develop the good habit of writing comments.

## Input and output

### `cin` and `cout`

```cpp
#include <iostream>

int main() {
  int x, y;                          // declare variables
  std::cin >> x >> y;                // read in x and y
  std::cout << y << std::endl << x;  // output y, newline, then output x
  return 0;                          // end the main function
}
```

???+ note "What is a variable?"
    You can refer to the [variable](./var.md) page.

???+ note "What is `std`?"
    std is the **namespace** used by the C++ standard library. Using a namespace is to avoid name duplication.
    
    For detailed knowledge about namespaces, you can refer to the [namespace](./namespace.md) page.

### `scanf` and `printf`

`scanf` and `printf` are actually functions provided by the C language. In most cases, their speed is faster than `cin` and `cout`, and they can conveniently control the input/output format.

???+ note "Input/output optimization"
    For the specific differences between `cin`/`cout` and `scanf`/`prinf` and input/output optimization, please refer to the [input, output optimization](../contest/io.md) page.

```cpp
#include <cstdio>

int main() {
  int x, y;
  scanf("%d%d", &x, &y);   // read in x and y
  printf("%d\n%d", y, x);  // output y, newline, then output x
  return 0;
}
```

Here, `%d` indicates that the variable read in/output is a signed integer (`int` type) variable.

Similarly:

1.  `%s` indicates a string.
2.  `%c` indicates a character.
3.  `%lf` indicates a double-precision floating-point number (`double`).
4.  `%lld` indicates a long integer (`long long`). Depending on the system, it may also be `%I64d`.
5.  `%u` indicates an unsigned integer (`unsigned int`).
6.  `%llu` indicates an unsigned long integer (`unsigned long long`), which may also be `%I64u`.

Besides type specifiers, there are also some ways to control the format. Many are not commonly used; two commonly used ones are listed below:

1.  `%1d` indicates an integer of length 1. When reading in, even without spaces, numbers can be read in digit by digit. When outputting, if the specified length is greater than the number of digits of the number, spaces will be used to pad in front of the number. If the specified length is less than the number of digits of the number, there is no effect.
2.  `%.6lf`, used for output, keeping six decimal places.

The corresponding places of these two operators can be filled with other numbers, for example `%.3lf` indicates keeping three decimal places.

??? note "What are \"double-precision floating-point number\" and \"long integer\"?"
    These indicate the types of variables. As above, they will be left to [variables](./var.md) for unified explanation.

??? note "Why is there an `&` operator in `scanf`?"
    Here, `&` is actually the address-of operator, returning the address of the variable in memory. And the parameter that scanf receives is the address of the variable. This may only be fully and clearly explained in [pointers](./pointer.md); for now just remember it.

??? note "What is `\n`?"
    `\n` is an **escape character** representing a newline.
    
    Escape characters are used to represent some characters that cannot be directly input, such as the newline character that cannot be directly input because a string literal cannot span lines, the quotation mark that cannot be input because it has special meaning, and the backslash that cannot be input because it represents an escape character.
    
    Common escape characters are:
    
    1.  `\t` indicates a tab character.
    
    2.  `\\` indicates `\`.
    
    3.  `\"` indicates `"`.
    
    4.  `\0` indicates the null character, used to indicate the end of a C-style string.
    
    5.  `\r` indicates a carriage return. In Linux the newline character is `\n`, and in Windows the newline character is `\r\n`. In OI, if the output needs a newline, just use `\n`. But when reading in, if character-by-character reading is used, it may cause some problems due to the newline character, which needs attention. For example, `gets` treats `\n` as the end of the string; at this time, if the newline character is `\r\n`, `\r` will remain at the end of the string.
    
    6.  Specially, `%%` indicates `%`, which can only be used in `printf` or `scanf`; in other string literals just simply use `%`.
    
    ??? note "What is a literal?"
        A "literal" is a piece of program that is directly used as a value in the code, for example `3` is an `int` literal, `'c'` is a char literal. The `"hello world"` in the program we wrote above is also a string literal.
        
        A literal without explanation and appearing for no reason is also called a "magic number"; if the code needs to be read by people, this is a very discouraged behavior.

## Some extended content

### Whitespace characters in C++

In C++, all whitespace characters (spaces, tabs, newlines), whether multiple or single, are treated as the same. (Of course, those within quotation marks treated as part of a string do not count.)

Therefore, you can freely use any code style (except that inline comments, string literals, and preprocessor commands must be within a single line), for example:

```cpp
--8<-- "docs/lang/code/basic/basic_1.cpp:main"
```

Of course, doing this is not recommended.

A code style that is also widely used but different from the code style required by **OI Wiki**:

```cpp
--8<-- "docs/lang/code/basic/basic_2.cpp:main"
```

### The `#define` command

`#define` is a preprocessor command used to define macros, essentially text replacement. For example:

```cpp
#include <iostream>
#define n 233

// n is not a variable; instead, the compiler will replace all n text in the code with 233,
// but n that is part of an identifier will not be replaced, e.g. fn will not be replaced with f233;
// similarly, those inside strings will not be replaced

int main() {
  std::cout << n;  // outputs 233
  return 0;
}
```

??? note "What is an identifier?"
    An identifier is a group of characters that can be used as a variable name. For example, `abcd` and `abc1` are both valid identifiers, while `1a` and `c+b` are both invalid identifiers.
    
    An identifier begins with an English letter or underscore, and in the middle only English letters, underscores, and digits are allowed. It is worth noting that keywords (such as `int`, `for`, `if`) cannot be used as identifiers.

??? note "What is a preprocessor command?"
    A preprocessor command is a command accepted by the preprocessor, used to perform preliminary text transformations on the code, such as the file inclusion operation `#include` and macro processing `#define`, etc. For GCC, by default the output `.i` file of the preprocessing stage is not retained. You can use the `-E` option to retain the output file.

Macros can take parameters; a macro with parameters can be used like a function:

```cpp
#include <iostream>
#define sum(x, y) ((x) + (y))
#define square(x) ((x) * (x))

int main() {
  std::cout << sum(1, 2) << ' ' << 2 * sum(3, 5) << std::endl;  // outputs 3 16
}
```

But a macro with parameters is different from a function. Because a macro is text replacement, it will cause many problems. For example:

```cpp
#include <iostream>
#define sum(x, y) x + y
// here it should be #define sum(x, y) ((x) + (y))
#define square(x) ((x) * (x))

int main() {
  std::cout << sum(1, 2) << ' ' << 2 * sum(3, 5) << std::endl;
  // the output is 3 11, because #define is text replacement, and the latter statement is replaced with 2 * 3 + 5
  int i = 1;
  std::cout << square(++i) << ' ' << i;
  // the output is undefined, because ++i is executed twice
  // and modifying the same variable multiple times in the same statement is undefined behavior (with exceptions)
}
```

Using `#define` is risky (since the scope of `#define` is the entire program, it may cause text to be unexpectedly replaced, requiring the use of `#undef` to cancel the definition in time), so it should be used with caution. The more recommended approach is: use the `const` qualifier to declare constants, and use functions instead of macros.

But, in OI, `#define` still has its uses (the following two are discouraged usages, which will reduce the standardization of the code):

1.  `#define int long long`+`signed main()`. Usually used to avoid errors caused by forgetting to enable long long, or to rule out the possibility of errors caused by forgetting to enable long long during debugging. (It may also cause an increased constant factor or even TLE, or MLE due to running out of space.)
2.  `#define For(i, l, r) for (int i = (l); i <= (r); ++i)`, `#define pb push_back`, `#define mid ((l + r) / 2)`, used to shorten the code length.

However, `#define` also has advantages, for example combining it with preprocessor directives such as `#ifdef` has a magical effect, for example:

```cpp
#ifdef LINUX
// code for linux
#else
// code for other OS
#endif
```

We can control the compiled code through `-DLINUX` at compile time, without modifying the source file. This also has an advantage: the executable file compiled through `-DLINUX` does not contain code for other operating systems; that code has already been deleted during preprocessing.

`#define` can also use the `#` and `##` operators, greatly facilitating debugging.
