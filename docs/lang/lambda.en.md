**Note**: Considering the actual situation of algorithm competitions, this article will not comprehensively study the syntax, but will only cover the parts that may be applied in algorithm competitions.

The syntax in this article follows the **C++11** standard; other higher-version standard syntax is mentioned as appropriate and is specially marked.

## Lambda expressions

Lambda expressions are named after the $\lambda$ calculus in mathematics, directly corresponding to the lambda abstraction therein. The compiler generates an anonymous [**function object**](./new.md#function-object) at compile time according to the syntax, with the captured variables as its members, and the parameters and function body used to implement the `operator()` overload.

??? note "Function object (Function Object)"
    A function object is a kind of class object, generally implemented by overloading `operator()`, so it can be called like a function. Compared with using an ordinary function, a function object has many advantages, for example it can save state, and can be passed as a parameter to other functions, etc.

The following is one syntax of lambda:

```text
[capture] (parameters) mutable -> return-type {statement}
```

A lambda expression itself is a class; after expansion it is in the following form:

<!-- scripts.linter.preprocess.fix_details off -->

```text
class Lambda_1 {
 private:
  Lambda_1() : capture-list(init-value) { }

 public:
  return-type operator()(parameters) const { statement }

 private:
  mutable capture-list
};
```

<!-- scripts.linter.preprocess.fix_details on -->

An empty capture can be implicitly converted to a function pointer, for example:

```cpp
void (*f)(int, int) = [](int, int) -> void {};
```

Below we introduce each part of the syntax separately.

### statement function body

The function body of a lambda expression is similar to the function body of an ordinary function; besides being able to access parameters and global variables, etc., it can also access the [captured](#capture-clause) variables.

### capture clause

A lambda starts with a capture clause, which specifies which variables are captured; the capture list can be empty, or specify the capture method: variables with the `&` prefix are accessed by [reference](./reference.md), and variables without this prefix are accessed by value.

We can also use the default capture mode to capture all variables mentioned in the lambda: `&` means all captured variables are accessed by reference, and `=` means all captured variables are accessed by value.

After the default capture, we can still **explicitly** specify the capture mode for specific variables.

If we need to access the external variable `a` by reference and access the external variable `b` by value, then the following capture clauses can all do it:

-   `[&a, b]`
-   `[b, &a]`
-   `[&, b]`
-   `[b, &]`
-   `[=, &a]`

At the same time, the capture list can also be used to declare variables, whose types are deduced by the initializer, similar to using `auto` to declare variables.

The following are some common examples:

```cpp
int a = 0;
auto f0 = []() { return a * 9; };   // Error, cannot access 'a'
auto f1 = [a]() { return a * 9; };  // OK, 'a' is "captured" by value
auto f2 = [&a]() { return a++; };   // OK, 'a' is "captured" by reference
auto f3 = [v = a + 1]() {
  return v + 1;
};  // OK, use an initializer to declare the variable v, with the same type as a

// note, when using reference capture, please ensure that a is not destroyed when called
auto b = f2();  // f2 obtains the value of a from the capture list, without needing to pass a in through parameters
```

#### generalized capture: capture with initialization (C++14)

Since C++14, capture can not only be used to capture external variables, but can also be used to declare and initialize new variables, for example:

```cpp
auto f1 = [val = 520]() {
  return val;
};  // OK, define val of type int, initial value 520, return value type int

auto f2 = [val = 520LL]() {
  return val;
};  // OK, define val of type long long, initial value 520, return value type long long

auto f3 = [val = "520"]() {
  return val;
};  // OK, define val of type const char*, initial value "520", return value type const char*

auto f4 = [val = "520"s]() {
  return val;
};  // OK, since C++14, requires using namespace std; or using namespace std::literals;
    // define val of type std::string, initial value std::string("520"), return value type
    // std::string

auto f5 = [val = std::string("520")]() {
  return val;
};  // OK, define val of type std::string, initial value std::string("520"), return value type
    // std::string

auto f6 = [val = std::vector<int>(3, 6)]() {
  return val;
};  // OK, define val of type std::vector<int>, size 3, elements filled with 6, return value type
    // std::vector<int>

auto f7 = [val = 520]() -> int {
  return val;
};  // OK, define val of type int, initial value 520, return value type int

auto f8 = [val = 520]() -> long long {
  return val;
};  // OK, define val of type int, initial value 520, return value type long long
```

The initial value cannot be omitted when defining a new variable; the type of the variable is determined by the type of the initial value, equivalent to:

```text
auto val = init-value;
```

The following is an incorrect way of writing:

```cpp
auto f = [val]() { return val; };  // Error: 'val' was not declared in this
                                   // scope, identifier "val" is undefined
```

The initialization value can also be an external variable, for example:

```cpp
int value = 520;
auto f = [val = value]() { return val; };
std::cout << f();  // Output: 520
```

`val` can also be a reference type, which can reference an external variable; through this way we can give an alias to an external variable captured by reference, for example:

```cpp
int value = 520;

auto f = [&val = value]() {
  return val;
};  // OK, define val of type int&, return value type int, equivalent to int& val = value;

std::cout << f() << '\n';  // Output: 520

value = 1314;

std::cout << f() << '\n';  // Output: 1314
```

Capturing external variables and defining new variables can be used at the same time.

If you want to modify the new variable defined in capture inside the lambda expression, you need to use the `mutable` keyword; if it is a reference then it is not needed, for example:

```cpp
int value = 520;

{
  auto f = [val = value]() mutable -> int {
    return val = 1314;
  };  // requires mutable
  auto val_f = f();
  std::cout << value << ' ' << val_f << std::endl;  // Output: 520 1314
}

{
  auto f = [&val = value]() -> int { return val = 1314; };  // does not require mutable
  auto val_f = f();
  std::cout << value << ' ' << val_f << std::endl;  // Output: 1314 1314
}
```

See [mutable specification](#mutable-specification) for details.

The lifetime of a variable defined in capture follows the receiver of the lambda expression, which in the above examples is the variable $f$, because the lambda itself is actually a class, and everything in capture is a `private` member variable of this class, for example:

```cpp
int main() {
  auto f = [val = 0]() mutable -> int { return ++val; };  // val is constructed and initialized

  std::cout << f() << '\n';  // Output: 1
  std::cout << f() << '\n';  // Output: 2
  std::cout << f() << '\n';  // Output: 3
}  // val is destroyed along with f
```

### parameters (parameter list)

In most cases it is similar to a function's parameter list, for example:

```cpp
int x[] = {5, 1, 7, 6, 1, 4, 2};
std::sort(x, x + 7, [](int a, int b) { return (a > b); });
for (auto i : x) std::cout << i << " ";
```

This will print out the result of sorting the `x` array from large to small.

Since the **parameters (parameter list)** is optional, if no parameters are passed to the lambda, and its declaration does not contain [mutable](#mutable-specification), and there is no trailing return type, then the empty parentheses can be omitted.

??? note "Parameters declared with `auto`"
    After **C++14**, if a parameter uses `auto` to declare the type, then a [generic Lambda expression](#generic-lambda-c14) will be constructed.

#### Explicit object parameter (C++23)

Since **C++23**, the [explicit object parameter](https://zh.cppreference.com/w/cpp/language/function#.E5.BD.A2.E5.8F.82.E5.88.97.E8.A1.A8) can be used in the parameters of a lambda.

```cpp
auto nth_fibonacci = [](this auto self, unsigned n) -> unsigned {
  return n < 2 ? n : self(n - 1) + self(n - 2);
};

cout << nth_fibonacci(10u);
```

### mutable specification

Makes the function body able to modify variables captured by value.

```cpp
int a = 0;
auto by_value = [a]() mutable { ++a; };
auto by_ref = [&a] { ++a; };

by_value();
by_ref();
```

After executing `by_value()`, the captured member `a` of `by_value` is 1, but the external variable `a` is still 0.
And after executing `by_ref()`, the value of the external `a` becomes 1.

### return-type (return type)

Used to specify the return type of a lambda expression. If omitted, the return type will be automatically deduced (the behavior is consistent with a function whose return value is declared with `auto`).

When there are multiple `return` statements and the deduced types are inconsistent, a compilation error will occur.

```cpp
auto lam = [](int a, int b) -> int { return 0; };

auto x1 = [](int i) { return i; };

auto x2 = [](bool condition) {
  if (condition) return 1;
  return 1.0;
};  // Error, inconsistent deduced types
```

### Generic Lambda (C++14)

Using `auto` as the parameter type, we can construct a generic lambda.

```cpp
auto add = [](auto a, auto b) { return a + b; };
```

In [cpp insights](https://cppinsights.io), we can observe the `lambda` class definition generated by the compiler:

```cpp
class add_lambda {
 public:
  template <class T, class U>
  auto operator()(T a, U b) const {
    return a + b;
  }
};

add_lambda add{};
```

Both parameter declarations of `add` use `auto`, corresponding to the two template parameters `T` and `U` of the `operator()` function template of the `add_lambda` class.

### Recursion in Lambda

First let us look at an example that fails to compile:

```cpp
int n = 10;

auto dfs = [&](int i) -> void {
  if (i == n)
    return;
  else
    dfs(i + 1);  // Error: a variable declared with an auto type specifier
                 // cannot appear in its own initializer
};
```

Here we try to capture $dfs$ in the capture list, but there is a problem: the type of $dfs$ is `auto`, and the type of $dfs$ will only be deduced after the type on the right side of the equals sign is deduced, while the lambda must determine the type of $dfs$ before it can create its reference variable in order to capture $dfs$; well, this falls into a nesting-doll process.

How to solve this problem?

1.  Explicitly specify the type of $dfs$; we can use `std::function` instead.

    ???+ example "Modify the above code to:"
        ```cpp
        int n = 10;
        
        std::function<void(int)> dfs = [&](int i) -> void {
          if (i == n)
            return;
          else
            dfs(i + 1);  // OK
        };
        
        dfs(1);
        ```

    ??? warning "Recursion implemented with [`std::function`](./new.md#stdfunction) is not recommended"
        The type erasure of `std::function` usually requires allocating additional memory, while the addressing operation brought by indirect calls will further reduce performance.
        
        In a [Benchmark](https://quick-bench.com/q/U5qf_dHHKsSyVU83jmt0p_U541c) test, using the Clang 17 compiler with libc++ as the standard library, the `std::function` implementation is about 2.5 times slower than the lambda implementation of recursion.
        
        ??? note "Test code"
            ```cpp
            #include <algorithm>
            #include <functional>
            #include <numeric>
            #include <random>
            
            using namespace std;
            
            const auto& nums = [] {
              random_device rd;
              mt19937 gen{rd()};
              array<unsigned, 32> arr{};
            
              std::iota(arr.begin(), arr.end(), 0u);
              ranges::shuffle(arr, gen);
            
              return arr;
            }();
            
            static void std_function_fib(benchmark::State& state) {
              std::function<int(int)> fib;
            
              fib = [&](int n) { return n <= 2 ? 1 : fib(n - 1) + fib(n - 2); };
            
              unsigned i = 0;
            
              for (auto _ : state) {
                auto res = fib(nums[i]);
                benchmark::DoNotOptimize(res);
            
                ++i;
            
                if (i == nums.size()) i = 0;
              }
            }
            
            BENCHMARK(std_function_fib);
            
            static void template_lambda_fib(benchmark::State& state) {
              auto n_fibonacci = [](const auto& self, int n) -> int {
                return n <= 2 ? 1 : self(self, n - 1) + self(self, n - 2);
              };
            
              unsigned i = 0;
            
              for (auto _ : state) {
                auto res = n_fibonacci(n_fibonacci, nums[i]);
                benchmark::DoNotOptimize(res);
            
                ++i;
            
                if (i == nums.size()) i = 0;
              }
            }
            
            BENCHMARK(template_lambda_fib);
            ```
2.  Instead of obtaining $dfs$ by capturing, obtain it by passing it as a function parameter.

    ???+ example "Modify the above code to:"
        ```cpp
        int n = 10;
        
        // if a parameter in the parameter list has type auto, then the operator()
        // function in this Lambda class will be defined as a template function, and the template function can be instantiated later when called
        auto dfs = [&](auto& self,
                       int i) -> void  // [&] only captures the used variables, so it will not capture auto dfs
        {
          if (i == n)
            return;
          else
            self(self, i + 1);  // OK
        };
        
        dfs(dfs, 1);
        ```

    ???+ note "The difference between `auto self`, `auto& self`, and `auto&& self`:"
        Both `auto& self` and `auto&& self` theoretically only use $8$ bytes (the size of a pointer) for parameter passing, without other copies occurring. The specifics depend on how the compiler implements the Lambda and the corresponding optimization.
        While using `auto self` will cause an object copy, and the size of the copy depends on the elements in the capture list, because they are all private member variables of this Lambda class.
3.  We can manually expand the Lambda class, or use a similar way of writing, so that we can directly declare the type of $dfs$.

    ???+ example "Modify the above code to:"
        ```cpp
        int n = 10;
        
        class Lambda_1 {
         public:
          auto operator()(int i) const -> void {
            if (i == n)
              return;
            else
              (*this)(i + 1);  // OK
          }
        
          explicit Lambda_1(int& __n) : n(__n) {}
        
         private:
          int& n;
        } dfs(n);
        
        dfs(1);
        ```
4.  If the lambda does not capture any variables, we can also use a function pointer.

    If the lambda does not capture any variables, then it can be implicitly converted to a function pointer. At the same time, the lambda can now also be declared as `static`, and the function pointer type can also be declared as `static`. Relying on this, the lambda can access the function pointer without needing to capture, thereby achieving recursion.

    ???+ example "Example"
        ```cpp
        static unsigned (*fptr)(unsigned);
        
        static const auto lambda = [](const unsigned a) {
          return a < 2 ? a : (*fptr)(a - 2) + (*fptr)(a - 1);
        };
        
        static auto init = [] {
          fptr = +lambda;
          // Or
          // fptr = static_cast<unsigned (*)(unsigned)>(lambda);
          return 0;
        }();
        
        cout << lambda(10);
        ```

### Applications of Lambda expressions

#### As a Predicate for standard library algorithms

Sort from large to small:

```cpp
std::vector<int> v = {1, 2, 3, 4, 5};
std::sort(v.begin(), v.end(), [](int a, int b) { return a > b; });
```

Use [std::find\_if](https://zh.cppreference.com/w/cpp/algorithm/find) to find the first element greater than 3:

```cpp
std::vector<int> v = {1, 2, 3, 4, 5};
auto it = std::find_if(v.begin(), v.end(), [](int a) { return a > 3; });
```

#### Controlling the lifetime of intermediate variables

In algorithm competitions, we will encounter such a scenario: the initialization of a variable needs to use a previously declared variable, and its initialization process generates intermediate variables that occupy a relatively large space.

We hope to be able to destruct these intermediate variables as soon as possible to reduce memory consumption. At this time, we can use a lambda to control the lifetime of these intermediate variables.

```cpp
void solution(const vector<int>& input) {
  int b = [&] {
    vector<int> large_objects(input.size());
    int c = 0;

    for (int i = 0; i < large_objects.size(); ++i)
      large_objects[i] = i + input[i];

    for (int i = 0; i < input.size(); ++i) c += large_objects[input[i]];

    return c;
  }();

  // ...
}
```

Compared with using a block scope, a lambda allows us to use a return value, making the code more concise; compared with a function, we do not need to additionally name and declare the various captured parameters, making the code more compact.

## References

-   [cppreference-lambda](https://en.cppreference.com/w/cpp/language/lambda)
-   [Stackoverflow: Overhead with std::function](https://stackoverflow.com/a/33881130/11120338)
