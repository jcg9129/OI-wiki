C++ defines a complete set of methods for defining read-only quantities; variables modified by `const` are all read-only quantities, and the compiler will perform conflict checks at compile time to avoid modifications to read-only quantities, while possibly performing some optimizations.

Under normal circumstances, we should use `const` to modify variables and parameters as much as possible, to improve code robustness.

## The `const` type qualifier

### Constants

A variable modified by const cannot change its value after initialization.

```cpp
const int a = 0;  // the type of a is const int

// a = 1; // cannot modify a constant
```

### Constant reference, constant pointer

Both constant references and constant pointers restrict modification to the pointed-to value.

```cpp
int a = 0;
const int b = 0;

int *p1 = &a;
*p1 = 1;
const int *p2 = &a;
// *p2 = 2; // cannot modify the variable through a constant pointer
// int *p3 = &b; // cannot use int* to point to a const int variable
const int *p4 = &b;

int &r1 = a;
r1 = 1;
const int &r2 = a;
// r2 = 2; // cannot modify the variable through a constant reference
// int &p3 = b; // cannot use int& to reference a const int variable
const int &r4 = b;
```

In addition, what needs to be distinguished is the constant pointer (`const t*`) and the pointer constant (`t* const`), for example the following declarations

```cpp
int* const p1;  // pointer constant; the pointed-to address cannot be changed after initialization, the pointed-to value can be changed
const int* p2;  // constant pointer; the dereferenced value cannot be changed, can point to other int variables
const int* const p3;  // constant pointer constant; the value cannot be changed, the pointed-to address cannot be changed

// using aliases can better improve readability
using const_int = const int;
using ptr_to_const_int = const_int*;
using const_ptr_to_const_int = const ptr_to_const_int;
```

Using `const` in function parameters to qualify the parameter type can avoid the variable being incorrectly modified, while increasing code readability

```cpp
void sum(const std::vector<int> &data, int &total) {
  for (auto iter = data.begin(); iter != data.end(); ++iter)
    total += *iter;  // iter is an iterator; the type after dereferencing is const int
}
```

## `const` member functions

A `const`-qualified member function in a type can be used to restrict modification to members.

```cpp
#include <iostream>

struct ConstMember {
  int s = 0;

  void func() { std::cout << "General Function" << std::endl; }

  void constFunc1() const { std::cout << "Const Function 1" << std::endl; }

  void constFunc2(int ss) const {
    // func(); // a const member function cannot call a non-const member function
    constFunc1();

    // s = ss; // a const member function cannot modify member variables
  }
};

int main() {
  int b = 1;
  ConstMember c{};
  const ConstMember d = c;
  // d.func(); // a constant cannot call a non-const member function
  d.constFunc2(b);
  return 0;
}
```

## Constant expression `constexpr` (C++11)

A constant expression is an expression whose result can be computed at compile time, and `constexpr` requires the compiler to be able to obtain the value of a function or variable at compile time.

Compile-time computation can allow better optimization, such as hard-coding the result into the assembly, eliminating runtime computation overhead. Unlike the optimization brought by `const`, when a variable modified by `constexpr` satisfies the conditions of a constant expression, it forces the compiler to compute the result at compile time rather than at runtime.

???+ note "A more intuitive understanding is to understand `const` as \"read-only\" and `constexpr` as \"immutable\""
    ```cpp
    constexpr int a = 10;  // directly define a constant
    
    constexpr int FivePlus(int x) { return 5 + x; }
    
    void test(const int x) {
      std::array<int, x> c1;            // error, x is unknown at compile time
      std::array<int, FivePlus(6)> c2;  // feasible, FivePlus is known at compile time
    }
    ```

The following example well illustrates the difference between `const` and `constexpr`; the code uses recursion to implement the computation of the Fibonacci sequence and outputs it with control flow.

???+ note "Implementation"
    ```cpp
    #include <iostream>
    
    using namespace std;
    
    constexpr unsigned fib0(unsigned n) {
      return n <= 1 ? 1 : (fib0(n - 1) + fib0(n - 2));
    }
    
    unsigned fib1(unsigned n) { return n <= 1 ? 1 : (fib1(n - 1) + fib1(n - 2)); }
    
    int main() {
      constexpr auto v0 = fib0(9);
      const auto v1 = fib1(9);
    
      cout << v0;
      cout << ' ';
      cout << v1;
    }
    ```

???+ note "Possible assembly code after compilation (using Compiler Explorer, Clang 19)"
    ```nasm
    fib1(unsigned int):
            push    r14
            push    rbx
            push    rax
            mov     ebx, 1
            cmp     edi, 2
            jb      .LBB0_4
            mov     r14d, edi
            xor     ebx, ebx
    .LBB0_2:
            lea     edi, [r14 - 1]
            call    fib1(unsigned int)
            add     r14d, -2
            add     ebx, eax
            cmp     r14d, 1
            ja      .LBB0_2
            inc     ebx
    .LBB0_4:
            mov     eax, ebx
            add     rsp, 8
            pop     rbx
            pop     r14
            ret
    
    main:
            push    r14
            push    rbx
            push    rax
            mov     edi, 9
            call    fib1(unsigned int) # the initialization of `v1` performed a function call
            mov     ebx, eax
            mov     r14, qword ptr [rip + std::__1::cout@GOTPCREL]
            mov     rdi, r14
            mov     esi, 55 # `v0` is replaced by the final computed result
            call    std::__1::basic_ostream<char, std::__1::char_traits<char>>::operator<<(unsigned int)@PLT
            mov     byte ptr [rsp + 7], 32
            lea     rsi, [rsp + 7]
            mov     edx, 1
            mov     rdi, r14
            call    std::__1::basic_ostream<char, std::__1::char_traits<char>>& std::__1::__put_character_sequence[abi:ne200000]<char, std::__1::char_traits<char>>(std::__1::basic_ostream<char, std::__1::char_traits<char>>&, char const*, unsigned long)
            mov     rdi, r14
            mov     esi, ebx # read the variable value
            call    std::__1::basic_ostream<char, std::__1::char_traits<char>>::operator<<(unsigned int)@PLT
            xor     eax, eax
            add     rsp, 8
            pop     rbx
            pop     r14
            ret
    ```

The `fib0` function modified by `constexpr` used constant parameters at its unique call site, making the entire function run only at compile time. Since the function has no runtime execution, the compiler determines that there is no need to generate assembly code.

At the same time, note that in the assembly, `v0` has no initialization code; in the code that calls `cout` to output `v0`, `v0` has already been replaced by the final settled result, indicating that the variable value has been computed at compile time, and the runtime computation is optimized away. While the initialization of `v1` is still an ordinary `fib1` recursive call.

So `constexpr` can be used to replace macro-defined constants, avoiding [the risks of macro definitions](./basic.md#the-define-command).

In algorithm problems, we can use `constexpr` to store variables with a relatively small data scale, to eliminate the corresponding runtime computation overhead. It is especially common in the "[table lookup / precomputation](../contest/dictionary.md)" technique, using containers such as arrays modified by `constexpr` to store answers.

???+ note "Too large a compile-time computation amount will cause a compilation error"
    The compiler will limit the overhead of compile-time computation; if the computation amount is too large, it will cause compilation to fail, and we should consider using `const`.
    
    ```cpp
    #include <iostream>
    
    using namespace std;
    
    constexpr unsigned long long fib(unsigned long long i) {
      return i <= 2 ? i : fib(i - 2) + fib(i - 1);
    }
    
    int main() {
      // constexpr auto v = fib(32); evaluation exceeded maximum depth
      const auto v = fib(32);
      cout << v;
      return 0;
    }
    ```

???+ note "The compilation error given by Clang when using constexpr"
    ```text
    <source>:10:20: error: constexpr variable 'v' must be initialized by a constant expression
        10 |     constexpr auto v = fib(32);
        |                    ^   ~~~~~~~~~~~~
    <source>:6:25: note: constexpr evaluation exceeded maximum depth of 512 calls
        6 |     return i <= 2 ? i : fib(i - 2) + fib(i - 1);
        |                         ^
    <source>:6:25: note: in call to 'fib(32)'
        6 |     return i <= 2 ? i : fib(i - 2) + fib(i - 1);
        |                         ^~~~~~~~~~
    <source>:6:25: note: in call to ...
    ```

## References

-   [C++ keyword——const](https://zh.cppreference.com/w/cpp/keyword/const)
-   [C++ keyword——constexpr](https://zh.cppreference.com/w/cpp/keyword/constexpr)
