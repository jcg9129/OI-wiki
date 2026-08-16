## Overview

C++'s **namespace** mechanism can be used to solve the problem of name conflicts in complex projects.

For example: all content of the C++ standard library is defined in the `std` namespace; if you define a variable called `cin`, then you can access your defined `cin` variable through `cin`, and access the standard library's `cin` object through `std::cin`, without worrying about producing a conflict.

## Declaration

The following code declares a namespace named `A`:

```cpp
namespace A {
int cnt;

void f(int x) { cnt = x; }
}  // namespace A
```

After the declaration, outside this namespace, you can access the `f` function inside the namespace `A` through `A::f(x)`, and can also access the `cnt` variable inside the namespace `A` through `A::cnt`.

The declaration of namespaces can be nested, so the following piece of code is also allowed:

```cpp
namespace A {
namespace B {
void f() { ... }
}  // namespace B

void f() {
  B::f();  // what is actually accessed is A::B::f(); since we are currently in namespace A,
           // the preceding A:: can be omitted
}
}  // namespace A

void f()  // what is defined here is the f function of the global namespace, which will not conflict
          // with either A::f or A::B::f
{
  A::f();
  A::B::f();
}
```

## The `using` directive

After declaring a namespace, if you access a member inside the namespace from outside the namespace, you need to add `namespace::` before the member name.

Is there a convenient method to allow us to directly access members inside the namespace through the member name? The answer is yes. We can use the `using` directive.

The `using` directive has the following two forms:

1.  `using namespace::memberName;`: this directive allows us to omit the namespace before a certain member name, and directly access the member through the member name, equivalent to importing this member into the current scope.
2.  `using namespace namespaceName;`: this directive allows us to directly access **any** member in the namespace through the member name, equivalent to importing all members of this namespace into the current scope.

Therefore, if `using namespace std;` is executed, all names in `std` will be introduced into the global namespace in the current scope. This way, we can use `cin` instead of `std::cin`, and `cout` instead of `std::cout`.

??? warning "The `using` directive may cause name conflicts!"
    Since `using namespace std;` introduces **all names** in `std`, if you declare a variable or function with the same name as one in `std`, it may cause a compilation error due to a name conflict.
    
    Therefore, in engineering, the `using namespace namespaceName;` directive is not recommended.

With the `using` directive, the code in [C++ syntax basics](./basic.md#cin-and-cout) can have these two equivalent ways of writing:

```cpp
#include <iostream>

using std::cin;
using std::cout;
using std::endl;

int main() {
  int x, y;
  cin >> x >> y;
  cout << y << endl << x;
  return 0;
}
```

```cpp
#include <iostream>

using namespace std;

int main() {
  int x, y;
  cin >> x >> y;
  cout << y << endl << x;
  return 0;
}
```

## Unnamed namespace

When we define only one namespace in a scope for preventing name conflicts, its definition and use can become very concise. We can use an unnamed namespace.

A namespace defined in the form `namespace { /* something ... */ } ` (omitting the namespace name) is called an unnamed namespace. An unnamed namespace in a file is regarded as having a unique name, different from all other namespaces, but multiple unnamed namespaces in the same scope are regarded as the same namespace. After an unnamed namespace is defined, the names in it can be found when used in the scope outside it, as if a `using namespace` directive was added after the unnamed namespace definition.

## Applications

### Preventing name conflicts between subtasks

In some problems with multiple subtasks, we can define a namespace for each subtask, and define the variables and functions we need to solve that subtask in it; this way, even if the implementations of two subtasks declare the same name, there will be no conflict, thereby making the subtasks not interfere with each other, which will to some extent facilitate debugging and improve the readability of the program.

### Preventing conflicts with names introduced by the standard library and the environment

At the same time, using namespaces can also prevent some names commonly used in algorithm competitions from conflicting with the standard, as in the following example:

```cpp
#include <math.h>

#include <vector>

using namespace std;

namespace Sol {
int end;  // std::end is introduced by using namespace std;

int y1;  // y1 is the second-kind Bessel function defined by POSIX

// so usually, there will be a conflict under Linux but not under Windows

void solve() {
  // using our declared end and y1 unqualified (without ::) inside Sol::solve()
  // will not cause a name conflict; while if the above code were in the global namespace, it would cause a conflict: among them, end
  // will only conflict with std::end during name lookup (i.e. compiling the code using it), while y1
  // will conflict at declaration time; and the conflict of y1, because it is related to the environment, may not even be discovered under Windows,
  // but will cause a compilation error under the Linux judging environment.
}
}  // namespace Sol

int main() { Sol::solve(); }
```

## References

-   [Namespaces - cppreference.com](https://en.cppreference.com/w/cpp/language/namespace)
