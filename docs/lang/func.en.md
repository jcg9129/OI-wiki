author: Ir1d, tsagaanbar, yang-lile

## Declaring a function

A function in programming is generally a collection of several statements. We can also call it a "**subroutine**". In programming, if there are some repeated procedures, we can extract them to form a function. A function can receive several values, which are called the parameters of the function. A function can also return a certain value, which is called the return value of the function.

To declare a function, we need the return value type, the name of the function, and the parameter list.

```cpp
// return value type int
// function name some_function
// parameter list int, int
int some_function(int, int);
```

As above, we declared a function named `some_function`, which needs to receive two parameters of type `int`, and the return value type is also `int`. We can consider that this function will perform some operations on the two passed-in integers and return a result of the same type.

## Implementing a function: writing the function definition

Only the declaration of a function is not enough; it can only let us know the **interface** type of the function when calling (i.e. what data it receives, what data it returns), but it lacks the specific internal implementation, i.e. the **definition** of the function. We can write code **elsewhere after the declaration** to **implement** this function (it can also be implemented in another file, but the separately compiled files need to be given together during linking).

If a function has a return value, then we need to return the value to the caller through the `return` statement. Once a function executes to the `return` statement, it directly ends the current function and no longer executes the subsequent statements.

```cpp
int some_function(int, int);  // declaration

/* some other code here... */

int some_function(int x, int y) {  // definition
  int result = 2 * x + y;
  return result;
  result = 3;  // this statement will not be executed
}
```

At the time of definition, we give names to the variables of the function's parameter list. This way, we can use these variables in the function definition.

If it is in the same file, we can also directly **merge the declaration and definition together**, in other words, complete the definition at the time of declaration.

```cpp
int some_function(int x, int y) { return 2 * x + y; }
```

If a function does not need a return value, then mark the return value type of the function as `void`; if a function does not need parameters, then the parameter list can be left empty. Similarly, a function with no return value will also end execution when it executes to the `return;` statement.

```cpp
void say_hello() {
  cout << "hello!\n";
  cout << "hello!\n";
  cout << "hello!\n";
  return;
  cout << "hello!\n";  // this statement will not be executed
}
```

## Calling a function

Like variables, a function needs to be declared first before it can be used. The behavior of using a function is called "calling". We can call other functions inside any function, including the function itself. The behavior of a function calling itself is called **recursion**.

In most languages, the way to write a function call is the **function name plus a pair of parentheses** `()`, such as `foo()`. If the function needs parameters, then we fill the parameters it needs into the parentheses in order, separated by commas, such as `foo(1, 2)`. A function call is also an expression, and the **return value of the function** is the **value of the expression**.

The parameters written out when declaring a function can be understood as variables that can be used **inside the current call of the function**; the values of these variables are initialized by the values passed in at the call site. Look at the following example:

```cpp
void foo(int, int);

/* ... */

void foo(int x, int y) {
  x = x * 2;
  y = y + 3;
}

/* ... */

a = 1;
b = 1;
// before the call: a = 1, b = 1
foo(a, b);  // call foo
            // after the call: a = 1, b = 1
```

In the above example, `foo(a, b)` is a call to `foo`. When calling, the `x` and `y` variables in `foo` are initialized by the values of `a` and `b` at the call site respectively. Therefore, the modifications to the variables `x` and `y` in `foo` **do not affect the values of the variables at the call site**.

If we need to modify the values of variables in a function (subroutine), then we need to adopt the "pass by reference" method.

```cpp
void foo(int& x, int& y) {
  x = x * 2;
  y = y + 3;
}

/* ... */

a = 1;
b = 1;
// before the call: a = 1, b = 1
foo(a, b);  // call foo
            // after the call: a = 2, b = 4
```

In the above code, we see that a "`&` (and symbol)" is added after "`int`" in the function parameter list, which indicates a **reference** to the `int` type. When calling `foo`, the `a` and `b` variables at the call site initialize the two references to the `int` type, `x` and `y`, in `foo` respectively. The `x` and `y` in `foo` can be understood as "aliases" of the `a` and `b` variables at the call site, i.e. the operations on `x` and `y` in `foo` are the operations on `a` and `b` at the call site.

## The `main` function

In particular, every C/C++ program needs to have a function named `main`. Any program will start running from the `main` function.

> The `main` function can also have parameters; through the parameters of the `main` function, we can obtain the instructions passed to this program from the outside (i.e. the "command-line arguments"), in order to make different reactions.

Below is a piece of code that calls a function (subroutine):

```cpp
// hello_subroutine.cpp

#include <iostream>

void say_hello() {
  std::cout << "hello!\n";
  std::cout << "hello!\n";
  std::cout << "hello!\n";
}

int main() {
  say_hello();
  say_hello();
}
```
