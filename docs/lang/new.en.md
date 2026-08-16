**Note**: Considering the actual situation of algorithm competitions, this article will not comprehensively study the syntax, but will only cover the parts that may be applied in algorithm competitions.

The syntax in this article follows the **C++11** standard. Where semantics differ, **C++11** is taken as the standard; C++14, C++17, and other syntax are mentioned as appropriate and are specially marked.

## The `auto` type specifier

The `auto` type specifier is used to automatically deduce the type of variables, etc. For example:

```cpp
auto a = 1;        // a is of type int
auto b = a + 0.1;  // b is of type double
```

Note that `auto` removes references; if you do not want copy overhead, you need to manually specify it:

```cpp
int a = 1;
int& b = a;
auto c = b;   // c is of type int, with copy overhead
auto& e = a;  // e is of type int&, without copy overhead
```

## The decltype specifier

`decltype` can deduce types based on an **entity** or an **expression**; note that the two ways of deducing types are different, and incorrect use may cause a dangling reference. It is not commonly used in competitions; here we only introduce it roughly.

```cpp
#include <iostream>
#include <vector>

int main() {
  int a = 1926;
  decltype(a) b;                 // deduce based on entity, b is of type int
  decltype(1 + 1) c;             // deduce based on expression, c is of type int
  decltype((a)) d = a;           // deduce based on expression, d is of type int&!
  std::vector<decltype(b)> vec;  // deduce based on entity, vec is of type std::vector<int>
  return 0;
}
```

## constexpr

> See also [constant expression constexpr (C++11)](const.md#constant-expression-constexpr-c11)

## Range-based `for` loop

Using a range for to traverse an iterable object has the same efficiency as traversing with an iterator. The efficiency of both is generally better than index traversal, because there is no need to address according to the index.

The following is a simple syntax of the range-based `for` loop:

```cpp
for (item_declaration : range_initializer) statement
```

For example:

```cpp
std::array<int, 4> arr = {1, 2, 3, 4};
for (int x : arr) {
  std::cout << x << std::endl;
}
```

The code effect produced by the above syntax is equivalent to the following code:

```cpp
std::array<int, 4> arr = {1, 2, 3, 4};
for (auto px = arr.begin(), ed = arr.end(); px != ed; ++px) {
  std::cout << *px << std::endl;
}
```

### item-declaration

Declare a variable to receive the elements in the container on the right; the variable type should be consistent with the type of the sub-elements in the container. We can use `auto` to automatically deduce the type; for complex types, `auto&` is often used to prevent copy overhead.

### range-initializer

The range initializer can be any kind of iterable object (such as an array, or a class object that defines the `begin` and `end` member functions). If an expression is put in, the expression will only be evaluated once.

Example:

```cpp
int a[] = {1, 1, 4, 5, 1, 4};
std::vector<int> b{1, 1, 4, 5, 1, 4};
std::map<std::string, int> c{{"114", 114}, {"514", 514}};
for (int i : a) std::cout << i;
for (auto i : b) std::cout << i;
// the type of i below is std::pair<const std::string, int>&
for (auto& i : c) std::cout << i.first << i.second;
for (auto i : {1, 1, 4, 5, 1, 4}) std::cout << i;
```

### Custom types supporting range for

Just provide the `begin` and `end` member functions; the return type needs to support comparison, increment, and dereference (the `*` operator).

Here is an example:

```cpp
#include <iostream>

struct C {
  int a[4];

  int* begin() { return a; }

  int* end() { return a + 4; }
};

int main() {
  C c = {1, 9, 2, 6};
  for (auto i : c) std::cout << i << " ";
  std::cout << std::endl;
  // output: 1 9 2 6
  return 0;
}
```

### Init-statement (C++20)

In C++20, we can also use an init-statement to implement some functionality, such as a loop counter:

```cpp
#include <iostream>
#include <vector>

int main() {
  std::vector<int> v = {0, 1, 2, 3, 4, 5};

  for (int counter = 0; auto i : v)  // the init-statement (C++20)
    std::cout << counter++ << ' ' << i << std::endl;
}
```

## Structured binding (C++17)

Structured binding is a syntactic sugar provided by C++17, which can conveniently extract sub-elements or references to sub-elements, like this:

```cpp
struct C {
  int x{1}, y{2};
};

int arr[]{4, 5, 6};

auto [c1, c2] = C{};       // c1=1,c2=2; int type
auto& [a1, a2, a3] = arr;  // a1=arr[0],a2=arr[1],a3=arr[2]; int& type
```

Note the following points:

-   The number of variables declared on the left must be consistent with the number of sub-elements of the object on the right
-   The type declaration needs to use `auto`
-   We can use `&` to modify it to get references

You can write this when traversing a `map` container:

```cpp
std::map<std::string, int> m = {{"k1", 1}, {"k2", 2}};

// use "auto&", no copy overhead
for (auto& [k, v] : m) {
  // the type of k is const std::string&, because the key comes with const modification
  // the type of v is int&
  std::cout << k << ' ' << v << std::endl;
}
```

## std::tuple

[tuple](https://zh.cppreference.com/w/cpp/utility/tuple) is defined in the header file `<tuple>`; it is a generalization of `std::pair`, and can store multiple values of different types. Let us look at an example:

```cpp
#include <iostream>
#include <tuple>
#include <vector>

constexpr auto expr = 4 - 1;  // expr = 3

int main() {
  std::vector<int> vec = {1, 9, 2, 6, 0};
  std::tuple<int, int, std::string, std::vector<int>> tup =
      std::make_tuple(817, 114, "514", vec);

  // use get<> to obtain a sub-element; the content inside the angle brackets must be an integer constant expression
  for (auto i : std::get<expr>(tup)) std::cout << i << " ";
  // the first element is numbered 0, so std::get<3> gives us a std::vector<int>
  return 0;
}
```

After C++17, we can use structured binding to extract values, like this:

```cpp
std::vector<int> vec = {1, 9, 2, 6, 0};
std::tuple<int, int, std::string, std::vector<int>> tup =
    std::make_tuple(817, 114, "514", vec);

auto& [a, b, c, d] = tup;  // C++17 Structured binding
std::cout << a << ' ' << b << c << std::endl;
std::cout << d.size() << ' ' << d[2] << std::endl;
```

### Member functions

| Function | Effect |
| ----------- | -------------------- |
| `operator=` | Assign the content of one `tuple` to another |
| `swap` | Swap the contents of two `tuple`s |

Example:

```cpp
constexpr std::tuple<int, int> tup = {1, 2};
std::tuple<int, int> tupA = {2, 3}, tupB;
tupB = tup;
tupB.swap(tupA);
```

### Non-member functions

| Function | Effect |
| -------------- | ---------------------------- |
| `make_tuple` | Create a `tuple` object, whose type is defined according to the types of each argument |
| `std::get` | Tuple-style access to a specified element |
| `std::tie` | Assign the values in a tuple to existing variables |
| `operator==` etc. | Compare the values in a `tuple` in lexicographic order |
| `std::swap` | Specialized `std::swap` algorithm |

Example:

```cpp
std::tuple<int, int> tupA = {2, 3}, tupB;
tupB = std::make_tuple(1, 2);
std::swap(tupA, tupB);
std::cout << std::get<1>(tupA) << std::endl;
int x;
std::tie(x, std::ignore) = tupB;
std::cout << x << std::endl;
```

`std::tie` assigns tuple elements to existing variables, and we can use `std::ignore` to skip unneeded elements. Structured binding directly declares new variables (supporting value/reference binding), and must accept all elements.

## Function object

An object that can use the function call operator `operator()` is called a function object (FunctionObject).

It is not a language feature, but a [concept or requirement](https://zh.cppreference.com/w/cpp/named_req/FunctionObject), widely applied in the standard library.

Function objects can be roughly divided into two categories:

1.  Function pointers
2.  Class objects that overload the `operator()` operator

[lambda](./lambda.md) is a typical function object of the second category; it stores the captured content in member variables and overloads the function call operator.

## Lambda expressions

> Please refer to the [Lambda expressions](lambda.md) page.

## std::function

???+ warning "Please note the performance overhead"
    `std::function` introduces a certain performance overhead; as tested by [Benchmark](./lambda.md#recursion-in-lambda), it usually causes a performance loss of 2 to 3 times or more.
    
    Because it uses the technique of type erasure, and this is usually implemented via the virtual function mechanism, calling a virtual function introduces additional [overhead](https://stackoverflow.com/questions/5057382/what-is-the-performance-overhead-of-stdfunction).
    
    Please consider using [**Lambda expressions**](./lambda.md) or a [**function object**](#function-object) instead.

`std::function` is a general-purpose function wrapper, defined in the header file `<functional>`.

An instance of `std::function` can store, copy, and call any [**Callable**](https://zh.cppreference.com/w/cpp/named_req/Callable) object, including [**Lambda expressions**](./lambda.md), member function pointers, or other [**function objects**](#function-object).

If a `std::function` does not contain any callable object (such as default construction), calling it will throw a [`std::bad_function_call`](https://zh.cppreference.com/w/cpp/utility/functional/bad_function_call) exception.

```cpp
#include <functional>
#include <iostream>

struct Foo {
  Foo(int num) : num_(num) {}

  void print_add(int i) const { std::cout << num_ + i << '\n'; }

  int num_;
};

void print_num(int i) { std::cout << i << '\n'; }

struct PrintNum {
  void operator()(int i) const { std::cout << i << '\n'; }
};

int main() {
  // store a free function
  std::function<void(int)> f_display = print_num;
  f_display(-9);

  // store a Lambda
  std::function<void()> f_display_42 = []() { print_num(42); };
  f_display_42();

  // store a call to a member function
  std::function<void(const Foo&, int)> f_add_display = &Foo::print_add;
  const Foo foo(314159);
  f_add_display(foo, 1);
  f_add_display(314159, 1);

  // store a call to a data member accessor
  std::function<int(Foo const&)> f_num = &Foo::num_;
  std::cout << "num_: " << f_num(foo) << '\n';

  // store a call to a function object
  std::function<void(int)> f_display_obj = PrintNum();
  f_display_obj(18);
}
```

## Variadic function templates

Before C++11, both class templates and function templates could only accept a fixed number of template parameters. C++11 allows **any number, any type** of template parameters.

Here we only briefly introduce variadic **function** templates.

The function template `fun` declared in the following code can accept any number, any type of template parameters as its template formal parameters.

```cpp
template <typename... Clazz>
void fun(Clazz... paras) {}
```

`paras` is a function parameter pack, accepting 0 or more function arguments. `Clazz` is a template parameter pack, accepting 0 or more template arguments (non-type, type, or template); when marked with `typename` it only accepts types.

It can be simply understood as follows:

-   A template parameter pack is usually some type names (but compile-time constants or template names can also be used)
-   A function parameter pack is usually some variable names

Now we can call the `fun` function like this:

```cpp
fun();
fun(1);
fun(1, 2, 3);
fun(1, 0.0, "abc");
```

### Parameter pack expansion

#### Parameter pack expansion syntax

Parameter pack expansion is very simple; just use `...`, and it will automatically separate with `,`. For example:

```cpp
template <class A, class... C>
void func(A arg1, C... arg2) {
  // C is a template parameter pack
  tuple<A, C...>();  // expands to tuple<int, int, double, bool>();

  // arg2 is a function parameter pack
  func(arg2...);  // expands to func( 2, 1.1, true );
}

func(1, 2, 1.1, true);
```

Parameter pack expansion can also be accompanied by the needed operations, for example:

```cpp
template <class A, class... C>
void func(A arg1, C... arg2) {
  func((arg2 + 1)...);
  // expands to func( (2+1) , (1.1+1), (2.1f+1) );
}

func(1, 2, 1.1, 2.1f);
```

#### Termination function

The above function cannot run, because the number of parameters keeps decreasing, and finally becomes empty parameters and reports an error.

We need to specify a termination condition; we can provide an ordinary function, like this:

```cpp
void func() {}

template <class A, class... C>
void func(A arg1, C... arg2) {
  std::cout << arg1 << std::endl;
  func((arg2 + 1)...);
}

func(1, 2, 1.1, 2.1f);
```

This way, when the number of parameters is not 0 it calls the template, and when empty it calls the ordinary function, so it can run normally.

### Fold expressions (C++17)

C++17 provides a convenient syntax for handling **function parameter packs**; its syntax is as follows (it must be wrapped in parentheses):

1.  `( pack op ... )`, becomes `(E1 op (... op (EN-1 op EN)))`
2.  `( ... op pack )`, becomes `(((E1 op E2) op ...) op EN)`
3.  `( pack op ... op init )`, becomes `(E1 op (... op (EN−1 op (EN op I))))`
4.  `( init op ... op pack )`, becomes `((((I op E1) op E2) op ...) op EN)`

Let us simply demonstrate it and it will be easy to understand:

```cpp
template <class... C>
void func(C... args) {
  (std::cout << ... << args) << std::endl;
  // syntax 4, equivalent to ↓
  // ( ( ( std::cout << 1 ) << 2.1 ) << true ) << std::endl;
  // output: 12.11  note true is output as 1, because boolalpha is not specified here

  std::cout << (args && ...) << std::endl;
  // syntax 1, equivalent to ↓
  // std::cout << ( 1 && ( 2.1 && true ) ) ) << std::endl;
  // output: 1
}

func(1, 2.1, true);
```

### Abbreviated function templates (C++20)

Since C++20, we can directly use `auto ...` as the parameter type to achieve the abbreviation of function templates:

```cpp
void func(auto... args) { (std::cout << ... << args) << std::endl; }
```

Note that it is still essentially a function template, equivalent to the following way of writing:

```cpp
template <class... T>
void func(T... args) {
  (std::cout << ... << args) << std::endl;
}
```

## Ranges library (C++20)

> The ranges library is an extension of the iterator and generic algorithm library, making iterators and algorithms more powerful through composition and reducing errors.

A range is a traversable sequence, including arrays, containers, views, etc.

When complex operations need to be performed on ranges such as containers, the [ranges library](https://zh.cppreference.com/w/cpp/ranges) can make algorithm writing easier and clearer.

### View

A view is a lightweight object that implements some algorithms through specific mechanisms (such as custom iterators), providing ranges with more traversal methods to meet needs.

The ranges library has already implemented some commonly used views, roughly divided into two kinds:

1.  **Range factories**, used to construct some special ranges; using this kind of factory can save the step of manually constructing a container, reduce overhead, and directly generate a range.
2.  **Range adaptors**, providing various traversal support; they can be called like functions, and can also be connected through the pipe operator `|` to achieve chained calls.

**Range adaptors**, as [**range adaptor closure objects**](https://zh.cppreference.com/w/cpp/named_req/RangeAdaptorClosureObject), also belong to [**function objects**](#function-object); they overload `operator|`, making them able to be assembled together like a pipeline.

??? note "The pipe operator"
    The `|` here should be understood as the pipe operator, not the bitwise OR operator; this usage comes from the [pipe](https://zh.wikipedia.org/wiki/%E7%AE%A1%E9%81%93_%28Unix%29) in Linux.

Under complex operations, it can also maintain good readability, with the following characteristics:

If A, B, C are some range adaptor closure objects, R is some range, and other letters are possible valid arguments, then the expression

    R | A(a) | B(b) | C(c, d)

is equivalent to

    C(B(A(R, a), b), c, d)

Below we take `ranges::take_view` and `ranges::iota_view` as an example:

```cpp
#include <iostream>
#include <ranges>

int main() {
  const auto even = [](int i) { return 0 == i % 2; };

  for (int i : std::views::iota(0, 6) | std::views::filter(even))
    std::cout << i << ' ';
}
```

1.  The range factory `std::views::iota(0, 6)` generates a range of the integer sequence from 0 to 5
2.  The range adaptor `std::views::filter(even)` filters the previous range, generating a range with only even numbers left
3.  The two operations are connected using the pipe operator

The above code does not need to additionally allocate heap space to store the range generated at each step; the actual generation and filtering operations occur during the traversal operation (more specifically, the internal iterator construction, increment, and dereference), which is Zero Overhead.

At the same time, the lifetime of the externally-input range is equal to the lifetime of the internal elements of the **range adaptor**. If the external range (such as a container, range factory) has already been destroyed, then traversing these views again has the same effect as dereferencing a dangling pointer, which is undefined behavior.

To avoid the above situation, we should strictly require that the lifetime of the adaptor lies within the lifetime of any range it uses.

???+ note "When the range is destroyed, the elements inside the view all dangle"
    ```cpp
    #include <iostream>
    #include <ranges>
    #include <vector>
    
    using namespace std;
    
    int main() {
      auto view = [] {
        vector<int> vec{1, 2, 3, 4, 5};
        return vec | std::views::filter([](int i) { return 0 == i % 2; });
      }();
    
      for (int i : view) cout << i << ' ';  // runtime undefined behavior
    
      return 0;
    }
    ```

### Constrained Algorithm

> C++20 provides constrained versions of most algorithms in the namespace std::ranges; you can use an iterator-sentinel pair or a single range as arguments to specify the range, and it supports projections and pointer-to-member callable objects. In addition, it also changes the return types of most algorithms to return all potentially useful information computed during algorithm execution.

These algorithms can be understood as improved versions of the old standard library algorithms; they are all function objects, providing more friendly overloads and argument type checking (based on [`concept`](https://zh.cppreference.com/w/cpp/language/constraints)). Let us first take the comparison of `std::sort` and `ranges::sort` as an example.

```cpp
#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int main() {
  vector<int> vec{4, 2, 5, 3, 1};

  sort(vec.begin(), vec.end());  // {1, 2, 3, 4, 5}

  for (const int i : vec) cout << i << ", ";
  cout << '\n';

  ranges::sort(vec, ranges::greater{});  // {5, 4, 3, 2, 1}

  for (const int i : vec) cout << i << ", ";

  return 0;
}
```

`ranges::sort` and `sort` have the same algorithm implementation, but `ranges::sort` provides a range-based overload, making argument passing more concise. Most other algorithms under the `std` namespace also have corresponding range-overload versions located in the `ranges` namespace.

Using these range arguments, combined with the views from the previous section, allows us to maintain code readability while performing complex operations. Let us look at an example:

```cpp
#include <algorithm>
#include <array>
#include <iostream>
#include <ranges>

using namespace std;

int main() {
  const auto& inputs = views::iota(0u, 9u);  // produce the integer sequence from 0 to 8
  const auto& chunks = inputs | views::chunk(3);  // divide the sequence into chunks, 3 elements per chunk
  const auto& cartesian_product =
      views::cartesian_product(chunks, chunks);  // compute the Cartesian product of the chunks with themselves

  for (const auto [l_chunk, r_chunk] : cartesian_product)
    // compute the sum of the integers of the two chunks under the Cartesian product
    cout << ranges::fold_left(l_chunk, 0u, plus{}) +
                ranges::fold_left(r_chunk, 0u, plus{})
         << ' ';
}
```

???+ note "Output:"
    6 15 24 15 24 33 24 33 42

## References

1.  [C++ reference manual](https://zh.cppreference.com/)
