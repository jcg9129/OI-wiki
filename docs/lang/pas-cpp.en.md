author: kexplorning, Ir1d, lvneg1

## Quick installation and environment configuration of C++

The following processes are all operated on a Windows system.

### Using an IDE

You can refer to the content in the following pages:

-   [Dev-C++](../tools/editor/devcpp.md)
-   [Code::Blocks](../tools/editor/codeblocks.md)

### Using a code editor + compiler + debugger

You can refer to the content in the [VS Code](../tools/editor/vscode.md) page. The Visual Studio Code official website has documentation explaining how to configure C++. Generally speaking, VS Code combined with plugins is more convenient to use; see the [VS Code official website](https://code.visualstudio.com/).

## Quick summary of C++ syntax

C++ programs all start running from the `main` part.

Braces indicate the beginning and end of a block statement: `{` is equivalent to `begin` in Pascal, and `}` is equivalent to `end`.

Note that, like Pascal, C++ requires a semicolon `;` at the end of each statement, but the closing brace does not need a semicolon, and there is no need to type a period `.` at the end of the program.

For comments, `//` indicates an inline comment, and `/* */` indicates a block comment.

As is customary, let us look at Hello World.

### Hello World: the first C++ program

```cpp
#include <iostream>  // import the iostream library

int main()  // the main part
{
  std::cout << "Hello World!" << std::endl;

  return 0;
}
```

Then compile and run it, and see the result.

#### Brief explanation

The first line, `#include <iostream>` means importing the `iostream` library.

??? note "Pascal library files"
    Pascal actually has library files, only that many students have never used them……

Do you see the `main` on the third line? The program starts executing from `main`.

The most important next statement is

```cpp
std::cout << "Hello World!" << std::endl;
```

`std::cout` is the output command. You may have seen some C++ programs directly write `cout`.

??? note "About the std:: prefix"
    For the issue of the `std::` prefix, see the note "What is std?" at the bottom of [this section](basic.md#cin-and-cout).

The `<<` in the middle vividly represents flow; in fact it represents how the output "flows". The meaning of this line of code is that `"Hello World!"` will first be pushed to the output stream, and then `std::endl` is pushed to the output stream.

And `std::endl` is the **output** newline command, which is similar to Pascal's `writeln`, but there is no `coutln` in C++. The difference between Pascal and C++ is that `write('Hello World!')` is equivalent to `std::cout << "Hello World!"`, and `writeln('Hello World!')` is equivalent to `std::cout << "Hello World!" << std::endl`.

Here `"Hello World!"` is a string; strings in Pascal all use single quotes `'` and cannot use double quotes, while C++ strings must use double quotes. Characters surrounded by single quotes in C++ have a different meaning, which will be mentioned later.

Alright, by here Hello World should be explained enough.

Some students may ask, what does the `return 0` at the end mean? What does that `int main()` mean? **Don't worry about it for now**; when you first write programs, just write it as a template (this is also written using a template). Because you will not use the parameters in `main` when starting out, there is no need to write it as `int main(int argc, char const *argv[])`.

#### Simple exercises

1.  Try outputting a different string.
2.  Try to understand escape characters.

### A+B Problem: the second C++ program

The classic A+B Problem.

```cpp
#include <iostream>

int main() {
  int a, b, c;

  std::cin >> a >> b;

  c = a + b;

  std::cout << c << std::endl;

  return 0;
}
```

Note: The code has many blank lines; if you are not used to it, you can remove the blank lines.

#### Brief explanation

`std::cin` is input (`cin` is C-in), and `>>` is also similar to the output syntax.

The most important of the extra statements here are two; one is the variable declaration statement.

```cpp
int a, b, c;
```

You may be used to declaring variables in Pascal:

```pas
var
a, b, c: integer;
```

C++ declarations start directly with the data type name; here, `int` (integer) at the start indicates that a variable is about to be declared.

The next most important statement is the assignment statement.

```cpp
c = a + b;
```

This is a relatively large difference between Pascal and C++ syntax: Pascal's assignment is `:=`, C++'s is `=`; while C++ tests equality with `==`.

C++ can also directly perform variable initialization assignment at the time of declaration.

```cpp
int a = 0, b = 0, c = 0;
```

#### Simple exercises

1.  Rewrite the code, submit it to an OJ, and get AC.
2.  For more input/output syntax, refer to [this section](basic.md#scanf-and-printf), and try to understand C++'s formatted output.

### Conclusion and next steps

Alright, by now you have already mastered some of the most basic things; the rest is finding the corresponding syntax and different characteristics between Pascal and C++.

But before that, it is strongly recommended to first read [Variable scope: global variables and local variables](#variable-scope-global-variables-and-local-variables).

Please make good use of <kbd>Alt</kbd>+<kbd>←</kbd> and <kbd>Alt</kbd>+<kbd>→</kbd> to jump back.

## Syntax

### Variables

#### Basic data types

C++ and Pascal are basically similar; the common ones are

-   `bool`: boolean type
-   `int`: integer type
-   `float`: single-precision floating-point type
-   `double`: double-precision floating-point type
-   `char`: character type
-   `void`: no type

C++'s single quotes are specifically used to represent a single character (character type), such as `'a'`, while a string (character-type array) must use double quotes.

C++ also has many additional data types; please refer to [Fundamental types - cppreference.com](https://zh.cppreference.com/w/cpp/language/types).

#### Constant declaration

```cpp
const double PI = 3.1415926;
```

If you are not clear about macro expansion issues, it is recommended to use constants instead of macro definitions.

### Operators

Please directly refer to the content in the [operations](./op.md) article. The appendix also provides a comparison table of operator and math function syntax.

### Conditions

#### `if` statement

```pas
if (a = b) and (a > 0) and (b > 0) then
    begin
        b := a;
    end
else
    begin
        a := b;
    end;
```

```cpp
if (a == b && a > 0 && b > 0) {
  b = a;
} else {
  a = b;
}
```

Boolean operations and comparisons

-   `and -> &&`
-   `or -> ||`
-   `not -> !`
-   `= -> ==`
-   `<> -> !=`

Notes:

1.  The precedence of `and` in Pascal and `&&` in C++ is different; C++ does not need to add parentheses to the judgment condition.
2.  In Pascal, testing equality is `=` and assignment is `:=`; in C++, testing equality is `==` and assignment is `=`.
3.  If you write `a = b` instead of `a == b` inside the parentheses of an `if` statement, the program will not report an error, but will assign `b` to `a`, and make the assignment expression `a = b` as a whole have the value of `a` after the assignment operation is completed.
4.  C++ does not need to think about whether to add a semicolon after `end`.
5.  In C++ boolean operations, non-boolean values can be automatically converted to boolean values.

???+ warning "Error-prone reminder"
    Pay special attention: **Do not write `==` as `=`!**
    
    Since C/C++ syntax is more flexible than Pascal, if you write `if (a=b)` in a judgment statement, the program will run smoothly, because `a=b` in C++ has a return value.

#### `case` and `switch`

They are not used much, so we do not expand on them in detail here.

Note: C++ does not have `1..n`, nor continuous inequalities (such as `1 < x < 2`).

### Loops

The three kinds of loops, six pieces of code below, implement the same functionality.

#### `while` loop

`while` is very similar. (The C++ here is not a complete program; some framework templates are omitted, same below)

```pas
var i: integer;

begin
    i := 1;
    while i <= 10 do
        begin
            write(i,' ');
            inc(i); // or i := i + 1;
        end;
end.
```

```cpp
int i = 1;
while (i <= 10) {
  std::cout << i << " ";
  i++;
}
```

#### `for` loop

C++'s `for` statement is very different.

```pas
var i: integer;

begin
    for i:= 1 to 10 do
        begin
            write(i, ' ');
        end;
end.
```

```cpp
for (int i = 1; i <= 10; i++) {
  std::cout << i << " ";
}
```

Notes:

1.  `for (int i = 1; i <= 10; i++){` this line has many statements; there are three statements in `for`.
2.  The first statement `int i = 1;` at this time declares a local variable `i` and initializes it. (This design is much more reasonable than Pascal.)
3.  The second statement `i <= 10;` serves as the standard for judging whether the loop continues.
4.  The third statement `i++`, executed at the end of each loop, means roughly `inc(i)` in Pascal; writing it as `++i` here is also the same. For the difference between `i++` and `++i`, please refer to other materials.

#### `repeat until` and `do while` loops

Note that `repeat until` and `do while` are different; please compare the following code

```pas
var i: integer;

begin
    i := 1;
    repeat
        write(i, ' ');
        inc(i);
    until i = 11;
end.
```

```cpp
int i = 1;
do {
  std::cout << i << " ";
  i++;
} while (i <= 10);
```

#### Loop control

In C++, the function of `break` is the same as in Pascal, exiting the loop.

And `continue` is also the same, skipping the current loop and entering the next loop (returning to the beginning).

### Arrays and strings

#### Variable-length array: standard library type Vector

Please refer to the content in the [sequence containers](csl/sequence-container.md) page.

The C++ standard library provides `vector`, equivalent to a variable-length array; the library file needs to be imported before calling.

```cpp
#include <iostream>
#include <vector>  // import the vector library

int main() {
  std::vector<int> a;  // declare vector a and define a as an empty vector object
  int n;

  std::cin >> n;
  // read a
  for (int i = 0; i < n; i++) {
    int t;
    std::cin >> t;
    a.push_back(t);  // put the read-in number t at the end of vector a; the complexity of this operation is O(1)
    /* here we cannot use subscript access to assign, because at declaration, the size of a is still empty,
    using `a[i] = t;` here is an incorrect practice.
    */
  }

  // print out all the numbers read into a
  for (int i = 0; i < n; i++) {
    std::cout << a[i] << ", ";  // !note, the first number in a is a[0];
    // if the subscript is out of bounds, it will return an unknown value (overflow), and will not report an error
  }
  std::cout << std::endl;

  return 0;
}
```

C++ accessing array members is similar to Pascal, but there is a very important difference: the first item of an array is `a[0]`, while in Pascal it can be specified by oneself.

#### String: standard library type String

Please refer to the content in the [string](csl/string.md) page.

The C++ standard library provides `string`; some of the operations it can perform are the same as `vector`, and the library file likewise needs to be imported.

```cpp
#include <iostream>
#include <string>

int main() {
  std::string s;  // declare string s

  std::cin >> s;  // read in s;
  // when reading in, all leading whitespace characters (space, newline, tab) are ignored, and the read-in string continues until the next whitespace character.

  std::cout << s << std::endl;

  return 0;
}
```

#### C-style arrays

Please refer to the content in the [arrays](array.md) page.

If you want to use a variable-length array, please use `vector`, not a C-style array.

C-style arrays are closely related to pointers, so we do not expand on them much here.

## Important differences

### Variable scope: global variables and local variables

C++ can declare variables almost **anywhere**. Please refer to [variable scope](var.md#variable-scope).

When writing Pascal procedures/functions, it is easy to forget to declare local variables `i` or `j`, and the main program generally has loops, so in most cases `i` and `j` are global variables; thus, in this case, operating on `i` in a procedure/function is very error-prone. What is even worse is that if you forget to declare this kind of local variable, the compiler does not report an error during compilation, and the program can run. (Many hard-to-find bugs come from this.)

So, when using C++, when declaring variables, such as the `i` used in a loop, **do not use global variables; use local variables whenever you can**. If you do this, you do not need to worry about variable name (such as `i`) conflicts in functions.

??? note "Additional note"
    Pascal can avoid this problem to some extent by imitating the C++ method: the main program only calls procedures/functions and does not declare global variables such as `i`, `j` that are very prone to name conflicts; if a loop is needed, write another procedure for calling.

### C++ can automatically convert types

```cpp
int i = 2;
if (i) {  // i = 0 returns false, the rest returns true
  std::cout << "true";
} else {
  std::cout << "false";
}
```

Not only is `int` converted to `bool`, there is also mutual conversion between `int` and `float`. In Pascal you can assign an integer to a floating point, but not the reverse. C++ does not have this problem.

```cpp
int a;
a = 3.2;      // at this time a = 3
float b = a;  // at this time b = 3.0
```

Distinguishing whether `/` is integer division or floating-point division is judged by the types of the divisor and dividend

```cpp
float a = 32 / 10;    // the result of 32/10 is 3 (integer division); a = 3.0
float b = 32.0 / 10;  // the result of 32.0/10 is 3.2; b = 3.2
```

`pow(a, b)` computes $a^b$; this function returns a floating point, and if it is directly used to compute the power of an integer, because there is automatic conversion, you do not need to worry that it will report an error

```cpp
int a = pow(2, 3);  // compute 2^3
```

There is also mutual conversion between `char` and `int`.

```cpp
char a = 48;              // ASCII 48 is '0'
int b = a + 1;            // b = 49
std::cout << (a == '0');  // true, outputs 1
```

In fact, `char` and `bool` in C++ are essentially integer types.

For detailed content, please refer to the article [Implicit conversions - cppreference.com](https://zh.cppreference.com/w/cpp/language/implicit_conversion).

### Many C++ statements have return values: taking how to implement reading an indefinite amount of data as an example

Sometimes you need to read until the data ends, for example, finding the sum of a group of numbers of indefinite quantity (the data can be multiple lines), until the end of the file; the way to implement it is

??? note "End-of-file EOF"
    EOF, the end-of-file identifier, is input in the command line on Windows with <kbd>Ctrl</kbd>+<kbd>Z</kbd> (you also need to press <kbd>Enter</kbd>), and on Unix-like systems input with <kbd>Ctrl</kbd>+<kbd>D</kbd>.

```cpp
#include <iostream>

int main() {
  int sum = 0, a = 0;

  while (std::cin >> a) {
    sum += a;
  }
  std::cout << sum << std::endl;

  return 0;
}
```

Implementation principle: In `while (std::cin >> a)`, `std::cin >> a` will return `false` if there is a problem with the input or the end of the file is encountered, making the loop break.

### Functions

C++ has only functions and no procedures but has `void`; it has no function value variables but has `return`.

Comparison example of Pascal functions and C++ functions:

```pas
function abs(x:integer):integer;
begin
    if x < 0 then
        begin
            abs := -x;
        end
    else
        begin
            abs := x;
        end;
end;
```

```cpp
int abs(int x) {
  if (x < 0) {
    return -x;
  } else {
    return x;
  }
}
```

In C++, the function declaration `int abs` defines the `abs()` function with a return value of type `int` (integer); the return value of the function is the value given by the `return` statement.

If you do not want a return value (i.e. Pascal's "procedure"), use `void`. `void` means "empty", returning nothing.

```pas
var ans: integer;

procedure printAns(ans:integer);
begin
    writeln(ans);
end;

begin
    ans := 10;
    printAns(ans);
end.
```

```cpp
#include <iostream>

void printAns(int ans) {
  std::cout << ans << std::endl;

  return;
}

int main() {
  int ans = 10;
  printAns(ans);

  return 0;
}
```

There is one very big difference between C++'s `return` and assigning to a function variable in Pascal. C++'s `return` returns a value, and after executing this statement, the function finishes executing; while assigning to a function variable in Pascal does not jump out of the function itself, but continues to execute. So, if Pascal needs to interrupt a function/procedure somewhere, it needs an additional command, i.e. `exit`. While C++ does not need this; if you need to interrupt somewhere, you can directly use `return`. For example (since I really cannot think of short and practical code, let us do this for now)

```cpp
#include <iostream>

void printWarning(int x) {
  if (x >= 0) {
    return;  // this statement here is equivalent to `exit;` in Pascal
  }
  std::cout << "Warning: input a negative number.";
}

int main() {
  int a;

  std::cin >> a;
  printWarning(a);

  return 0;
}
```

And in a sense, the previous `abs` function, this is the strictly equivalent version

```pas
function abs(x:integer):integer;
begin
    if x < 0 then
        begin
            abs := -x; exit; // !note here
        end
    else
        begin
            abs := x;  exit; // !note here
        end;
end;
```

```cpp
int abs(int x) {
  if (x < 0) {
    return -x;
  } else {
    return x;
  }
}
```

???+ note "Special reminder"
    In C++, `exit` exits the program; do not casually type `exit`, you should use `return`!

C++ regards both functions and procedures as functions, not even sparing `main`; for example writing `int main`, C++ regards `main` as an integer function, and here the return value is `0`. It is a customary convention that returning `0` represents the program exiting normally.

Maybe you have already guessed that the parameters in `main(int argc, char const *argv[])` are `int argc` and `char const *argv[]`, but for the meaning please refer to other materials.

### Passing parameters in functions

C++ does not have Pascal's `var` keyword that can change the passed parameters, but C++ can use references and pointers to achieve the same effect.

```pas
var a, b: integer;

procedure swap(var x,y:integer);
var temp:integer;
begin
    temp := x;
    x := y;
    y := temp;
end;

begin
    a := 10; b:= 20;    
    swap(a, b);
    writeln(a, ' ', b);
end.
```

```cpp
// code using pointers
#include <iostream>

void swap(int* x, int* y) {
  int temp;
  temp = *x;
  *x = *y;
  *y = temp;
}

int main() {
  int a = 10, b = 20;
  swap(&a, &b);
  std::cout << a << " " << b;

  return 0;
}
```

Note that the C++ code here **involves pointer issues**. Pointer issues are quite troublesome; it is recommended to read related materials.

```cpp
// code using references
#include <iostream>

void swap(int& x, int& y) {
  int temp;
  temp = x;
  x = y;
  y = temp;
}

int main(int argc, char const* argv[]) {
  int a = 10, b = 20;
  swap(a, b);
  std::cout << a << " " << b;

  return 0;
}
```

Note that the C++ code here involves **reference-related type issues**. When using references to call some STL libraries and template libraries, you may encounter some problems; at this time you need to manually declare other types. For specific materials, you can consult 《C++ Primer》 5th edition or online materials on your own.

There are other methods for passing parameters to functions in C++, one of which is to **directly use global variables to pass parameters**; if you cannot use pointers, you can first use this method. But the drawback of this method is that there is no stack to save data, so **there is no way to pass parameters in recursive functions**. (Unless you hand-write a stack; note that a hand-written stack is also a way to break through the system stack limit.)

## C++ standard library and references

Never reinvent the wheel (unless for practice); before you want to write a feature yourself, first go see whether this function or data structure already exists.

### C++ standard library

The C++ standard library's `<algorithm>` has many useful functions such as quicksort, binary search, etc., which can be directly called. Please refer to the [STL algorithms](csl/algorithm.md) page.

There are also STL containers, such as arrays, vectors (variable-size arrays), queues, stacks, etc., with many functions attached. Please refer to the [STL container introduction](csl/container.md) page.

For functions about string operations, see

-   [std::basic\_string - cppreference.com](https://zh.cppreference.com/w/cpp/string/basic_string)
-   [`<string>`- C++ Reference](https://www.cplusplus.com/reference/string/)

C/C++ pointers are very flexible things; you can refer to the [pointers](pointer.md) page. If you want to thoroughly understand pointers, it is recommended to find a book or reference manual to read carefully.

### Error troubleshooting and tips

-   [Common mistakes](../contest/common-mistakes.md)
-   [Common tricks](../contest/common-tricks.md)

### C++ language materials

-   [Learning resources](../contest/resources.md)
-   [cppreference.com](https://zh.cppreference.com/): the most important C/C++ reference
-   [C++ tutorial - Runoob](https://www.runoob.com/cplusplus/cpp-tutorial.html)
-   [C++ Language - C++ Tutorials](https://www.cplusplus.com/doc/tutorial/)
-   [Reference - C++ Reference](https://www.cplusplus.com/reference/)
-   [C++ Standard Library - Wikipedia](https://en.wikipedia.org/wiki/C%2B%2B_Standard_Library)
-   [The Ultimate Question of Programming, Refactoring, and Everything](https://www.gitbook.com/book/alexastva/the-ultimate-question-of-programming-refactoring-/details)
-   [Google C++ Style Guide](https://google.github.io/styleguide/cppguide.html)

## Afterword

Having written to here, many students may feel that this is not a first-aid guide at all; there are many things not mentioned. That is unavoidable.

Although it is for first aid, many things like how to convert a string to a number, how to search for a character in a string, these things are also not suitable for a concise and short first-aid post; if all these were written out, that would be a C++ getting-started tutorial, so please make full use of this Wiki, the reference manual, and search engines.

One point that needs to be pointed out is that the above talks about C++ syntax, but in fact much of the syntax comes from the C language; it would be better for the title to be written as 《Pascal to C/C++ first-aid post》.

Pascal was a very popular language in the latter half of the last century; it predates the C language, but with the popularization of the UNIX system and Microsoft's use of the C language, Pascal has now become history. Pascal did have later development, such as the Free Pascal open-source compiler project, adding object-oriented features (the Delphi language). Pascal's current usefulness, besides in informatics competitions, has one characteristic that other languages do not have—compilation supports very, very many old machines, such as the Gameboy, a Nintendo game console from the last century; and one more use is appearing in the form of pseudocode (Pascal-style pseudocode) in various textbooks.

Finally, Pascal's community is actually very small, while the C/C++ community is very large, with many and comprehensive help manuals and tutorials; you must master English well. There are still many, many programming languages in the world, and the discipline and technology of computing is not just about informatics competitions and programming languages.

### References for the Pascal language in this article

-   [Lazarus wiki](https://wiki.freepascal.org/)
-   [Free Pascal Reference guide](https://freepascal.org/docs-html/current/ref/ref.html)

## Appendix: Pascal and C++ operator and math function syntax comparison table

Only includes the most commonly used operators and functions.

### Basic arithmetic

|      | Pascal    | C++     |
| ---- | --------- | ------- |
| Addition | `a + b` | `a + b` |
| Subtraction | `a - b` | `a - b` |
| Multiplication | `a * b` | `a * b` |
| Integer division | `a div b` | `a / b` |
| Floating-point division | `a / b` | `a / b` |
| Modulo | `a mod b` | `a % b` |

### Logic

|   | Pascal    | C++                   |
| - | --------- | --------------------- |
| NOT | `not(a)` | `!a` |
| AND | `a and b` | `a && b` |
| OR | `a or b` | <code>a \|\| b</code> |

### Comparison

|      | Pascal   | C++      |
| ---- | -------- | -------- |
| Equal | `a = b` | `a == b` |
| Not equal | `a <> b` | `a != b` |
| Greater than | `a > b` | `a > b` |
| Less than | `a < b` | `a < b` |
| Greater than or equal to | `a >= b` | `a >= b` |
| Less than or equal to | `a <= b` | `a <= b` |

### Assignment

| Pascal                        | C++      |
| ----------------------------- | -------- |
| `a := b` | `a = b` |
| `a := a + b` | `a += b` |
| `a := a - b` | `a -= b` |
| `a := a * b` | `a *= b` |
| `a := a div b` or `a := a / b` | `a /= b` |
| `a := a mod b` | `a %= b` |

### Increment/decrement

|    | Pascal   | C++   |
| -- | -------- | ----- |
| Increment | `inc(a)` | `a++` |
| Increment | `inc(a)` | `++a` |
| Decrement | `dec(a)` | `a--` |
| Decrement | `dec(a)` | `--a` |

### Math functions

Using them requires importing the `<cmath>` library.

|       | Pascal     | C++            |
| ----- | ---------- | -------------- |
| Absolute value | `abs(a)` | `abs(a)` (integer) |
| Absolute value | `abs(a)` | `fabs(a)` (floating point) |
| $a^b$ | N/A[^ref1] | `pow(a, b)` |
| Truncation to integer | `trunc(a)` | `trunc(a)` |
| Rounding to integer | `round(a)` | `round(a)` |

[^ref1]: Extended Pascal has `a**b`, but it requires importing the `Math` library.

For other functions, please refer to:

-   [Common mathematical functions - cppreference.com](https://zh.cppreference.com/w/cpp/numeric/math)
