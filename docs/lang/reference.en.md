> Declaring a named variable as a reference, i.e. an alias of an existing object or function.

A reference can be regarded as a non-null pointer encapsulated by C++; it can be used to pass the object it points to, and must point to an object at the time of declaration.

A reference is not an object, so there is no array of references, it is impossible to obtain the pointer of a reference, and there is no reference to a reference.

??? note "The reference type does not belong to object types"
    If you want references to be able to complete general copy, assignment, and other operations, such as being a container element, then you need [`reference_wrapper`](https://zh.cppreference.com/w/cpp/utility/functional/reference_wrapper), which is usually implemented by maintaining a non-null pointer.

References are mainly divided into two kinds, lvalue references and rvalue references.

??? note "Lvalues and rvalues"
    For an explanation of lvalues and rvalues, please refer to the [value category](./value-category.md) page.

## Lvalue reference T&

The reference we usually encounter is an lvalue reference, i.e. a reference bound to an lvalue; at the same time, a `const`-qualified lvalue reference can bind an rvalue. The following is a piece of example code from the [reference manual](https://zh.cppreference.com/w/cpp/language/reference).

```cpp
#include <iostream>
#include <string>

int main() {
  std::string s = "Ex";
  std::string& r1 = s;
  const std::string& r2 = s;

  r1 += "ample";  // modifying r1 modifies s
  // r2 += "!"; // error: cannot modify through a reference to const
  std::cout << r2 << '\n';  // print r2, which accesses s, outputting "Example"
}
```

The most common place for lvalue references is function parameters, used to avoid unnecessary copies.

```cpp
#include <iostream>
#include <string>

// the s in the parameter is a reference; no copy occurs when calling the function
char& char_number(std::string& s, std::size_t n) {
  s += s;  // 's' and main()'s 'str'
           // are the same object; this also shows that an lvalue can be placed on the right side of the equals sign
  return s.at(n);  // string::at() returns a reference to char
}

int main() {
  std::string str = "Test";
  char_number(str, 1) = 'a';  // the function returns an lvalue, which can be assigned to
  std::cout << str << '\n';   // this outputs "TastTest"
}
```

## Rvalue reference T&& (C++11)

An rvalue reference is a reference bound to an rvalue, used to move objects, and can also be used to **extend the lifetime of a temporary object**.

```cpp
#include <iostream>
#include <string>

using namespace std;

int main() {
  string s1 = "Test";
  // string&& r1 = s1; // error: cannot bind to an lvalue, need std::move or static_cast

  const string& r2 = s1 + s1;  // feasible: an lvalue reference to const extends the lifetime
  // r2 += "Test"; // error: cannot modify through a reference to const
  cout << r2 << '\n';

  string&& r3 = s1 + s1;  // feasible: an rvalue reference extends the lifetime
  r3 += "Test";
  cout << r3 << '\n';

  const string& r4 = r3;  // an rvalue reference can be converted to a const-qualified lvalue
  cout << r4 << '\n';

  string& r5 = r3;  // an rvalue reference can be converted to an lvalue
  cout << r5 << '\n';
}
```

## Dangling reference

When the object referred to by a reference has already been destroyed, the reference becomes a dangling reference; accessing a dangling reference is undefined behavior and may cause the program to crash.

The following are common examples of dangling references:

-   Referencing a local variable

    ```cpp
    #include <iostream>

    int& foo() {
      int a = 1;
      return a;
    }

    int main() {
      int& b = foo();
      std::cout << b << std::endl;  // undefined behavior
    }
    ```

-   Dangling reference caused by deallocation

    ```cpp
    #include <iostream>

    int main() {
      int* ptr = new int(10);
      int& ref = *ptr;
      delete ptr;

      std::cout << ref << std::endl;  // undefined behavior
    }
    ```

-   Dangling reference caused by memory reallocation

    ```cpp
    #include <iostream>

    int main() {
      std::string str = "hello";

      const char& ref = str.front();

      str.append("world");  // may reallocate memory, causing the memory pointed to by ref to be released

      std::cout << ref << std::endl;  // undefined behavior
    }
    ```

    Insertion operations of containers similar to `std::vector`, `std::unordered_map`, etc. may all cause memory reallocation.

When using references, we should always pay attention to the lifetime of the object that the reference points to, to avoid causing a dangling reference.

Usually static checking tools and good coding habits can help us avoid the problem of dangling references.

## Optimization techniques related to references

### Eliminating the copy overhead of non-lightweight object parameters

Common **non-lightweight objects** are:

-   Containers `vector`, `array`, `map`, etc.
-   `string`
-   Other types that implement or inherit special functions such as custom copy construction, move construction, etc.

And using references for **lightweight objects** cannot bring any benefit; the space occupied by a reference type as a parameter may even be larger than the type itself.

This may bring some performance burden, while possibly preventing compiler optimization.

The following belong to **lightweight objects**

-   Basic types `int`, `float`, etc.
-   Small [aggregate types](https://zh.cppreference.com/w/cpp/language/aggregate_initialization)
-   Iterators of standard library containers

### Converting an lvalue to an rvalue

Use `std::move` to [transfer](./value-category.md#stdmove) the ownership of an object. This is usually seen between local variables, or between parameters and local variables:

```cpp
#include <iostream>
#include <string>
#include <vector>

using namespace std;

string world(string str) { return std::move(str) += " world!"; }

int main() {
  // 1
  cout << world("hello") << '\n';

  vector<string> vec0;

  // 2
  {
    string&& size = to_string(vec0.size());

    size += ", " + to_string(size.size());

    vec0.emplace_back(std::move(size));
  }

  cout << vec0.front();
}
```

But it is not always necessary to do this, for example [function return value optimization](./value-category.md#common-misconceptions).

### Rvalues extending the lifetime of temporaries

Semantically, a temporary may bring an additional copy or move; although in most cases the compiler can optimize through [copy elision](./value-category.md#copy-elision), references can force the compiler not to perform these redundant operations, avoiding uncertainty.

## References

1.  [C++ language documentation——reference declaration](https://zh.cppreference.com/w/cpp/language/reference)
2.  [C++ language documentation——value category](https://zh.cppreference.com/w/cpp/language/value_category)
3.  [Does const ref lvalue to non-const func return value specifically reduce copies?](https://stackoverflow.com/questions/38909228/does-const-ref-lvalue-to-non-const-func-return-value-specifically-reduce-copies)
