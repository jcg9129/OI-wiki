Value category is a very important concept in C++; although it may be of little use in algorithm competitions, understanding it can help us discover and avoid unnecessary copies, thereby improving the efficiency and performance of the code.

The concept of value category has undergone multiple developments in the C language, C++98, C++11, and C++17, gradually becoming a relatively complex concept.

## Unnecessary copies

We consider the process of putting a string into a vector:

```cpp
int main() {
  std::vector<std::string> vec;
  vec.reserve(3);
  for (int i = 0; i < 3; ++i) {
    std::string str;
    std::cin >> str;
    vec.push_back(str);
  }
  return 0;
}
```

We can find that during the transfer of the string, one copy is saved in each of `str` and `vec`, doubling the memory usage.

If we insist on saving this part of the memory, we can implement a crude move operation: define a custom `MyString` struct, with a pointer inside pointing to our string, i.e. we only need to copy the pointer over, and carefully clean up the pointer of the original object to prevent it from being incorrectly destructed.

```cpp
struct MyString {
  char *beg, *end;
  // ...
};

void move_to(MyString &src, MyString &dst) {
  dst.beg = src.beg;
  dst.end = src.end;
  src.beg = src.end = nullptr;
}
```

Since this need for efficiently transferring objects is relatively common, and it interacts difficultly with C++'s construction, destruction, and other operations, C++11 introduced move semantics into the language core.

## Value categories in the C language

In the C language standard, an object is a more general concept than a variable; it refers to a region of memory with a memory address. The main attributes of an object include: size, effective type, value, and identifier. The identifier is the variable name, and the value is the meaning of this memory when interpreted with its type. For example, although `int` and `float` types both occupy 4 bytes, for the same block of memory, we will interpret different meanings.

In the C language, every expression has a type and a value category. Value categories are mainly divided into three kinds:

-   Lvalue (lvalue): an expression that implicitly refers to an object. That is, we can take the address of this expression.
-   Rvalue (rvalue): an expression that does not refer to an object, i.e. refers to a value with no storage location; we cannot take the address of this value.
-   Function designator: an expression of function type.

Therefore, only a modifiable lvalue (an lvalue without `const` modification and not an array) can be located on the left side of an assignment expression.

For an operator that requires an rvalue as its operand, whenever an lvalue is used as the operand, the lvalue-to-rvalue, array-to-pointer, or function-to-pointer standard conversion is applied to this expression to convert it into an rvalue.

Common misconceptions:

-   Continuing to operate on an rvalue expression may result in an lvalue. For example, `int *a`, the expression `a + 1` is an rvalue, but `*(a + 1)` is an lvalue.
-   Only expressions have value categories; variables do not. For example, `int *a`, we cannot say the variable `a` is an lvalue, but we can say it acts as an lvalue in the expression `a`.

## Value categories in C++98

C++98 is almost consistent with the C language in terms of value categories, but adds some new rules:

-   A function is an lvalue, because we can take its address.
-   An lvalue reference (T&) is an lvalue, because we can take its address.
-   Only `const T&` can bind to an rvalue.

### Copy elision

C++ allows the compiler to perform Copy Elision, which can reduce the creation and destruction of temporary objects.

For example, the following code triggers the Return Value Optimization (RVO) in copy elision; you will only see one construction and one copy construction, even if construction and destruction have side effects.

```cpp
struct X {
  X() { std::puts("X::X()"); }

  X(const X &) { std::puts("X::X(const X &)"); }

  ~X() { std::puts("X::~X()"); }
};

X get() {
  X x;
  return x;
}

int main() {
  X x = get();
  X y = X(X(X(X(x))));
  return 0;
}
```

## Value categories in C++11

C++11 introduced move semantics and rvalue references (`T&&`), including move construction and move assignment functions. This gives us a method to utilize temporary objects.

Our `move_to` above can be rewritten as follows:

```cpp
struct MyString {
  // ...
  MyString(MyString&& other) {
    beg = other.beg;
    end = other.end;
    other.beg = other.end = nullptr;
  }
};
```

The expression characteristics we now focus on have increased a bit:

-   Whether it has identity: whether it refers to an object, i.e. whether it has an address.
-   Whether it can be moved: whether it has functions such as move construction, move assignment, etc., giving us a way to utilize these temporary objects.

Therefore we have three value categories:

-   Has identity, cannot be moved: lvalue (lvalue).
-   Has identity, can be moved: xvalue (xvalue).
-   No identity, can be moved: prvalue (prvalue).
-   No identity, cannot be moved: this kind of expression cannot be used.

In addition, C++11 also introduced two composite categories:

-   Has identity: generalized lvalue (glvalue), i.e. lvalues and xvalues.
-   Can be moved: rvalue (rvalue), i.e. prvalues and xvalues.

### std::move

To cooperate with move semantics, C++11 also introduced a utility function `std::move`, whose function is to forcibly convert an lvalue into an rvalue, in order to trigger move semantics.

```cpp
int main() {
  std::vector<int> a = {1, 2, 3};
  std::cout << "a: " << a.data() << std::endl;
  std::vector<int> b = a;
  std::cout << "b: " << b.data() << std::endl;
  std::vector<int> c = std::move(b);
  std::cout << "c: " << c.data() << std::endl;
}
```

Therefore we only need to change `push_back(str)` to `push_back(std::move(str))` to avoid the copy.

```cpp
int main() {
  std::vector<std::string> vec;
  vec.reserve(3);
  for (int i = 0; i < 3; ++i) {
    std::string str;
    std::cin >> str;
    vec.push_back(std::move(str));
    // another clever way of writing, requires C++17
    // std::cin >> vec.emplace_back();
  }
  return 0;
}
```

> Since `std::string` has Small String Optimization (SSO), short strings are stored directly inside the struct; you may have to input a relatively long string to observe the invariance of the `data` pointer.

## Value categories in C++17

C++17 further simplified value categories:

-   Lvalue (lvalue): has identity, cannot be moved.
-   Xvalue (xvalue): has identity, can be moved.
-   Prvalue (prvalue): initialization of an object.

C++11 extended copy elision to move; in the following code, `urvo` has no move when the compiler enables RVO.

C++17 requires that a prvalue is not necessarily materialized, and is directly constructed into the storage of its final target; before construction the object does not yet exist. Therefore in C++17 we do not have the return step, and thus do not need to depend on RVO. It can also be understood as forcing URVO (Unnamed RVO), but for NRVO (Named RVO) it is still non-mandatory.

```cpp
std::string urvo() { return std::string("123"); }

std::string nrvo() {
  std::string s;
  s = "123";
  std::cout << s;
  return s;
}

int main() {
  std::string str = urvo();  // direct construction
  std::string str = nrvo();  // not necessarily direct construction, depends on optimization
}
```

At the same time, C++17 introduced the mechanism of temporary materialization; when we need to access member variables, call member functions, etc. that require a glvalue, we can implicitly convert to an xvalue.

### Common misconceptions

In the following example:

-   In `f1`, returning `std::move(x)` is redundant; it does not bring a performance improvement, but instead interferes with the compiler performing NRVO optimization.
-   In `f2`, returning `std::move(x)` is dangerous; the function returns an rvalue reference pointing to the already-destroyed local variable `s`, resulting in a dangling reference problem.

```cpp
std::string f1() {
  std::string s = "123";
  // equivalent to return std::string(std::move(s))
  return std::move(s);
}

std::string&& f2() {
  std::string s = "123";
  return std::move(s);
}
```

## References and recommended reading

1.  [Value categories](https://en.cppreference.com/w/cpp/language/value_category)
2.  [Wording for guaranteed copy elision through simplified value categories](http://www.open-std.org/jtc1/sc22/wg21/docs/papers/2016/p0135r1.html)
3.  [Value categories in C++](https://paul.pub/cpp-value-category/)
4.  [C++ rvalue references, move, and the value category system, everything you need](https://zclll.com/index.php/cpp/value_category.html)
5.  [Copy elision](https://en.cppreference.com/w/cpp/language/copy_elision)
