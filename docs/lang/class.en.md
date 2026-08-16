author: Ir1d, cjsoft, Lans1ot, JasonkayZK
A class is an extension of a struct; it can not only have member elements, but also have member functions.

In object-oriented programming (OOP), an object is an instance of a class, that is, a variable.

In C++, the `struct` keyword also defines a class; the definition of the **struct** above comes from C. For certain historical reasons, C++ retained and extended `struct`.

## Defining a class

A class is defined using the keyword `class` or `struct`; below we use `class` as an example.

```cpp
class ClassName {
  ...
};

// Example:
class Object {
 public:
  int weight;
  int value;
} e[array_length];

const Object a;
Object b, B[array_length];
Object *c;
```

It is largely the same as using `struct`. This example defines a class named `Object`. This class has two member elements, namely `weight,value`; and after `}` it uses this type to define an array `e`.

Defining a pointer to a class is the same as [`struct`](./struct.md).

### Access specifiers

Unlike the example in [`struct`](./struct.md), in this example `public` appears, which belongs to access specifiers.

-   `public`: each member after this access specifier can be publicly accessed; simply put, it can be accessed whether **inside the class** or **outside the class**.
-   `protected`: each member after this access specifier can be accessed by members **inside the class**, derived classes, or friends, but **cannot be accessed** outside the class.
-   `private`: each member after this access specifier can **only** be accessed by members **inside the class** or friends, and **cannot** be accessed from outside the class or from derived classes.

For `struct`, all its members are `public` by default. For `class`, all its members are `private` by default.

??? note "Basic concepts about friends and derived classes"
    Friend (`friend`): use the `friend` keyword to modify a certain function or class. This can make the **modified party**, without becoming a member function or member class, access the private (`private`) or protected (`protected`) members of the class. Simply put, as long as it carries the `friend` mark of this class, it can access private or protected member elements.
    
    Derived class (`derived class`): C++ allows using a class as a **base class**, and **deriving** a **derived class** through the base class. The derived class (according to specific rules) inherits the member variables and member functions in the base class. This can improve code reuse.
    
    Derivation is similar to an "is" relationship. For example, a cat (derived class) "is" a mammal (base class).
    
    For the difference between `private` and `protected` above, we can regard it as the derived class can access the `protected` elements of the base class (same for `public`), but cannot access `private` elements.

## Accessing and modifying the values of member elements

The methods are the same as [`struct`](./struct.md)

-   For a variable, use the `.` symbol.
-   For a pointer, use the `->` symbol.

## Member functions

A member function, as the name suggests, is a function contained in a class.

??? note "Examples of common member functions"
    ```cpp
    vector.push_back();
    set.insert();
    queue.empty();
    ```

```cpp
class Class_Name {
  ... type Function_Name(...) { ... }
};

// Example:
class Object {
 public:
  int weight;
  int value;

  void print() {
    cout << weight << endl;
    return;
  }

  void change_w(int);
};

void Object::change_w(int _weight) { weight = _weight; }

Object var;
```

This class has a function that prints the `Object` member elements, and a function that changes the member element `weight`.

Similar to functions, for member functions, we can also declare first and then define, as in line fourteen (declaration) and after line seventeen (definition).

If we want to call the `print` member function of `var`, we can use `var.print()` to call it.

### Overloading operators

??? note "What is overloading"
    C++ allows the writer to specify different definitions for functions or operators with the same name. This is called **overloading**.
    
    If one or more of the types and numbers of parameters of same-named functions are pairwise different, then these same-named functions are regarded as different.
    
    Note that: if the only difference between two same-named functions is the difference in the type of the return value, then they cannot be overloaded; at this time the compiler will refuse to compile!
    
    If there is no confusion when calling (referring to when calling certain same-named functions, it is impossible to uniquely determine the called function according to the types and numbers of the filled parameters, which often occurs in functions with default parameters), then the compiler will determine which function should be called according to the parameters filled when calling.
    
    And the above process is called overload resolution.

Overloading operators can, to some extent, replace functions and simplify code.

The following gives an example of overloading operators.

```cpp
class Vector {
 public:
  int x, y;

  Vector() : x(0), y(0) {}

  Vector(int _x, int _y) : x(_x), y(_y) {}

  int operator*(const Vector& other) const { return x * other.x + y * other.y; }

  Vector operator+(const Vector&) const;
  Vector operator-(const Vector&) const;
};

Vector Vector::operator+(const Vector& other) const {
  return Vector(x + other.x, y + other.y);
}

Vector Vector::operator-(const Vector& other) const {
  return Vector(x - other.x, y - other.y);
}

// regarding lines 4,5 indicating assigning values to x,y, see the following text for the specific implementation.
```

This example defines a vector class, and overloads the `* + -` operators, which respectively represent vector inner product, vector addition, and vector subtraction.

The template for overloading operators can be roughly divided into the following parts.

```text
/* overload within class definition */ return type operator symbol(parameters){...}

/* declare within class definition, define externally */ return type class name::operator symbol(parameters){...}
```

For a custom class, if certain operators are overloaded (generally speaking, only the `<` comparison operator needs to be overloaded), then we can use the corresponding STL containers or algorithms, such as [`sort`](../basic/stl-sort.md).

To learn more, see item four of "References".

??? note "Operators that can be overloaded"
    ```text
    +       -       *       /       %       ^       &
    |       ~       !       =       <       >       +=
    -=      *=      /=      %=      ^=      &=      |=
    <<      >>      >>=     <<=     ==      !=      <=
    >=      &&      ||      ++      --      ,       ->*
    ->      ()      []      new     new []  delete  delete []
    ```

### Setting initial values when instantiating a variable

To complete this operation, we need to define a **default constructor** (Default constructor).

```cpp
class ClassName {
  ... ClassName(...)... { ... }
};

// Example:
class Object {
 public:
  int weight;
  int value;

  Object() {
    weight = 0;
    value = 0;
  }
};
```

This example defines the default constructor of `Object`; this function can, when we instantiate an `Object`-type variable, initialize all member elements to `0`.

If there is no explicit constructor, then the compiler considers this class to have an implicit default constructor. In other words, if no constructor is defined, then the compiler will automatically generate a default constructor, and will initialize according to the types of the member elements (the same as defining variables of built-in types).

In this case, the member elements are all uninitialized, and the result of accessing an uninitialized variable is undefined (that is, we do not know what value will be returned).

If we need to customize the initialized value, we can define (or overload) the constructor again.

??? note "About defining (or overloading) constructors"
    Generally speaking, the default constructor takes no parameters, which distinguishes it from the constructor. The definitions of the constructor and the default constructor are largely the same, only differing in the number of parameters.
    
    Constructors can be overloaded (of course, the first time is called defining). Note that if a constructor is already defined, then the compiler will no longer generate a parameterless default constructor. This may cause the behavior of trying to construct a variable in the default way (referring to not filling in initialization parameters) to fail to compile.

When using C++11 or above, we can use `{}` to initialize variables.

??? note "About `{}`"
    Using `{}` for initialization will use the lightweight proxy object std::initializer\_list for initialization.
    
    The initialization steps are roughly as follows
    
    1.  Try to find a constructor among the parameters that has `std::initializer_list`, and call it if there is one (after calling, the following search is no longer performed, same below).
    2.  Try to fill the elements in `{}` into other constructor parameters; if the parameters can be filled in order (default parameters are also included), then call this constructor.
    3.  If there are no `private` member elements, then try to assign values in order according to element definition order or subscript order **outside the class**.
    
    *The above process is only a simplified version of the complete process; for detailed content see "Reference nine"*

```cpp
class Object {
 public:
  int weight;
  int value;

  Object() {
    weight = 0;
    value = 0;
  }

  Object(int _weight = 0, int _value = 0) {
    weight = _weight;
    value = _value;
  }

  // the same as
  // Object(int _weight,int _value):weight(_weight),value(_value) {}
};

// the same as
// Object::Object(int _weight,int _value){
//   weight = _weight;
//   value = _value;
// }
//}

Object A;        // ok
Object B(1, 2);  // ok
Object C{1, 2};  // ok,(C++11)
```

??? note "About implicit type conversion"
    Sometimes code like the following is written
    
    ```cpp
    class Node {
     public:
      int var;
    
      Node(int _var) : var(_var) {}
    };
    
    Node a = 1;
    ```
    
    It looks very illogical; an `int` type cannot possibly be converted to a `node` type. But the compiler will not give an `error` prompt.
    
    The reason is that when assigning, `1` is first used as a parameter to call `node::node(int)`, then the default copy function is called for assignment.
    
    But in most cases, the writer will want the compiler to report an error. At this time we can append the `explicit` keyword before the constructor. This will tell the compiler that it must be called explicitly.
    
    ```cpp
    class Node {
     public:
      int var;
    
      explicit Node(int _var) : var(_var) {}
    };
    ```
    
    That is to say, `node a=1` will report an error, but `node a=node(1)` will not. Because the latter explicitly calls the constructor. Of course, most people will not write the latter code, but this example is enough to illustrate the role of explicit.
    
    *However, in algorithm competitions, to avoid this kind of situation, what is commonly used is "strengthening the standardization of the code", avoiding it from the source*

### Destruction

This is an unavoidable problem. Every variable will be destroyed when its scope ends.

But for a pointer that already points to dynamically-allocated memory, this pointer will not automatically release the memory it points to when destroyed; we need to manually release the dynamic memory.

If the member elements of a struct contain pointers, we will likewise encounter this problem. We need to use a destructor to manually release the dynamic memory.

The **destructor** (Destructor) will be called when this variable is destroyed. The method of overloading is the same as the constructor, but we need to add `~` before it

*The default-defined destructor is usually sufficient for algorithm competitions; usually we only overload the destructor when the member elements contain pointers.*

```cpp
class Object {
 public:
  int weight;
  int value;
  int* ned;

  Object() {
    weight = 0;
    value = 0;
  }

  ~Object() { delete ned; }
};
```

### Assigning values to class variables

By default, when assigning, it proceeds according to the rule of assigning to the corresponding member elements. We can also use `class name()` or `class name{}` as a temporary variable to assign.

The former only calls the copy constructor, while the latter calls the default constructor before calling the copy constructor.

In addition, by default, all assignments performed are **shallow copies** between corresponding elements; if there are pointers in the member elements, then after the assignment is complete, the member pointers of the two variables have the same address.

```cpp
// A,tmp1,tmp2,tmp3 are of type Object
tmp1 = A;
tmp2 = Object(...);
tmp3 = {...};
```

If you need to solve the pointer problem or perform more operations, you need to overload the corresponding constructor.

*For more content about constructors, see item six of "References".*

## References

1.  [cppreference class](https://zh.cppreference.com/w/cpp/language/class)
2.  [cppreference access](https://zh.cppreference.com/w/cpp/language/access)
3.  [cppreference default\_constructor](https://zh.cppreference.com/w/cpp/language/default_constructor)
4.  [cppreference operator](https://zh.cppreference.com/w/cpp/language/operators)
5.  [cplusplus Data structures](http://www.cplusplus.com/doc/tutorial/structures/)
6.  [cplusplus Special members](http://www.cplusplus.com/doc/tutorial/classes2/)
7.  [C++11 FAQ](http://www.stroustrup.com/C++11FAQ.html)
8.  [cppreference Friendship and inheritance](http://www.cplusplus.com/doc/tutorial/inheritance/)
9.  [cppreference value initialization](https://zh.cppreference.com/w/cpp/language/value_initialization)
