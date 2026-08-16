Overloading operators means redefining operators so that they support operations on specific data types. Overloading operators is a special case of overloading functions.

> When an operator appears in an expression, and at least one operand of the operator has a type of a class or enumeration, then overload resolution is used to determine which user-defined function satisfying the corresponding declaration should be called.[^ref1]

To put it plainly, if we regard using an "operator" as calling a special function (such as regarding `1+2` as calling `add(1, 2)`), and at least one of the parameters (operands) of this function has a type of `class`, `struct`, or `enum`, then the compiler needs to decide which custom function should be called according to the types of the operands.

In C++, we can overload almost all available operators.

???+ note "A listing of some overloadable operators"
    Unary operations: `+` (positive sign); `-` (negative sign); `~` (bitwise NOT); `++`; `--`; `!` (logical NOT); `*` (get the value corresponding to a pointer); `&` (get address); `->` (class member access operator), etc.
    
    Binary operations: `+`; `-`; `&` (bitwise AND); `[]` (subscript); `==`; `=` (assignment), etc.
    
    Others: `()` (function call); `""` (suffix identifier[^ref1], since C++11); `new` (memory allocation); `,` (comma operator); `<=>` (three-way comparison[^ref2], since C++20), etc.

## Restrictions

Overloading operators has the following restrictions:

-   You can only overload existing operators; you cannot define new operators yourself.
-   The following operators cannot be overloaded: `::` (scope resolution), `.` (member access), `.*` (member access through a member pointer), `?:` (ternary operator).
-   For an overloaded operator, its operator precedence, number of operands, and associativity direction must not be changed.
-   Overloading `&&` (logical AND) and `||` (logical OR) loses short-circuit evaluation.

## Implementation

Overloading operators is divided into two cases, overloading as a member function or a non-member function.

When overloaded as a member function, because there is an implicit `this` pointer pointing to the current member as a parameter, the number of function parameters is one fewer than the number of operands.

And when overloaded as a non-member function, the number of function parameters is the same as the number of operands.

Its basic format is (assuming the operator to be overloaded is `@`):

```cpp
class Example {
  // example of a member function
  return-value operator@(parameters other than itself) { /* ... */ }
};

// example of a non-member function
return-value operator@(all participating operands) { /* ... */ }
```

Below we give several examples of overloading operators.

### Basic arithmetic operators

Below we define a two-dimensional vector struct `Vector2D` and implement the corresponding overloads for addition and inner product.

??? note "Example of overloading arithmetic operators"
    ```cpp
    struct Vector2D {
      double x, y;
    
      Vector2D(double a = 0, double b = 0) : x(a), y(b) {}
    
      Vector2D operator+(Vector2D v) const { return Vector2D(x + v.x, y + v.y); }
    
      // note the type of the return value does not have to be this class
      double operator*(Vector2D v) const { return x * v.x + y * v.y; }
    };
    ```

### Increment and decrement operators

Increment and decrement operators are divided into two categories, prefix (`++a`) and postfix (`a++`). To distinguish prefix and postfix operators, when overloading the postfix operation we need to add an unused formal parameter of type `int`.

We can understand prefix increment as calling `operator++(a)` or `a.operator++()`, and postfix increment as calling `operator++(a, 0)` or `a.operator++(0)`.

??? note "Example of overloading prefix and postfix increment operators separately"
    ```cpp
    struct MyInt {
      int x;
    
      // prefix, corresponding to ++a
      MyInt &operator++() {
        x++;
        return *this;
      }
    
      // postfix, corresponding to a++
      MyInt operator++(int) {
        MyInt tmp;
        tmp.x = x;
        x++;
        return tmp;
      }
    };
    ```

Another point is that among the built-in increment and decrement operators, the prefix operator returns a reference, while the postfix operator returns a value. Although an overloaded operator does not have to follow this restriction, semantically we still expect the overloaded operator and the built-in operator to be consistent in the type of the return value.

For a type T, the typical definition of overloading the increment operator is as follows:

| Overload definition (taking `++` as an example) | Member function | Non-member function |
| --------------- | ----------------------- | -------------------------- |
| Prefix | `T& T::operator++();` | `T& operator++(T& a);` |
| Postfix | `T T::operator++(int);` | `T operator++(T& a, int);` |

### Function call operator

The function call operator `()` can only be overloaded as a member function. By overloading the `()` operator for a class, we can make objects of this class be called like functions.

A common application of overloading the `()` operator is to pass a struct that overloads the `()` operator as a custom comparison function into STL containers such as a priority queue.

Below is an example: given the names and scores of $n$ students, sort by score in descending order, and for those with the same score sort by name in ascending lexicographic order, and output the name and score of the highest-ranked person.

Below we define a comparison struct to implement the custom sorting method of the priority queue.

??? note "Example of overloading the function call operator"
    ```cpp
    struct student {
      string name;
      int score;
    };
    
    struct cmp {
      bool operator()(const student& a, const student& b) const {
        return a.score < b.score || (a.score == b.score && a.name > b.name);
      }
    };
    
    // note that the passed-in template parameter is the struct name rather than an instance
    priority_queue<student, vector<student>, cmp> pq;
    ```

### Comparison operators

In `std::sort` and some STL containers, the `<` operator is needed. When using custom types, we need to manually overload it.

Below is an example that implements the same functionality as the previous section

??? note "Example of overloading the comparison operator"
    ```cpp
    struct student {
      string name;
      int score;
    
      // overload the < operator
      bool operator<(const student& a) const {
        return score < a.score || (score == a.score && name > a.name);
        // the this pointer is omitted above; the complete expression is as follows:
        // this->score<a.score||(this->score==a.score&&this->name>a.name);
      }
    };
    
    priority_queue<student> pq;
    ```

The above code overloads the less-than sign as a member function; of course overloading it as a non-member function is also possible.

??? note "Overloading as a non-member function"
    ```cpp
    struct student {
      string name;
      int score;
    };
    
    bool operator<(const student& a, const student& b) {
      return a.score < b.score || (a.score == b.score && a.name > b.name);
    }
    
    priority_queue<student> pq;
    ```

In fact, as long as we have the `<` operator, the overloads of the other five comparison operators can also be easily implemented.

```cpp
/* clang-format off */

// the following implementations all overload the less-than sign as a non-member function

bool operator<(const T& lhs, const T& rhs) { /* overload the less-than operator here */ }
bool operator>(const T& lhs, const T& rhs) { return rhs < lhs; }
bool operator<=(const T& lhs, const T& rhs) { return !(lhs > rhs); }
bool operator>=(const T& lhs, const T& rhs) { return !(lhs < rhs); }
bool operator==(const T& lhs, const T& rhs) { return !(lhs < rhs) && !(lhs > rhs); }
bool operator!=(const T& lhs, const T& rhs) { return !(lhs == rhs); }
```

??? note "About the three-way comparison operator in C++20"
    If using C++20 or a higher version, we can directly use the default three-way comparison operator to simplify the code.[^ref3]
    
    ```cpp
    auto operator<=>(const T &lhs, const T &rhs) = default;
    ```
    
    The order of the default comparison is compared one by one in the order of member variable declaration.[^ref4]
    
    We can also use a custom three-way comparison. At this time it is required to choose the order relation contained in the comparison (`std::strong_ordering`, `std::weak_ordering`, or `std::partial_ordering`), or return an object such that:
    
    -   If `a < b`, then `(a <=> b) < 0`;
    -   If `a > b`, then `(a <=> b) > 0`;
    -   If `a` and `b` are equal or equivalent, then `(a <=> b) == 0`.
    
    For specific implementation details, please refer to [comparison operators #three-way comparison - cppreference](https://zh.cppreference.com/w/cpp/language/operator_comparison#Three-way_comparison).

References and notes:

[^ref1]: [Operator overloading - cppreference](https://zh.cppreference.com/w/cpp/language/operators)

[^ref2]: [User-defined literals - cppreference](https://zh.cppreference.com/w/cpp/language/user_literal)

[^ref3]: [Comparison operators #three-way comparison - cppreference](https://zh.cppreference.com/w/cpp/language/operator_comparison#.E4.B8.89.E8.B7.AF.E6.AF.94.E8.BE.83)

[^ref4]: [Default comparisons - cppreference](https://zh.cppreference.com/w/cpp/language/default_comparisons)
