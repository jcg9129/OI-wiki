author: Ir1d, cjsoft, Lans1ot

A **struct** can be regarded as a combination of a series of member elements.

It can be regarded as a custom data type.

???+ note "Note"
    The `struct` described on this page is different from the `struct` in C; in C++, `struct` is extended into a class specifier similar to [`class`](./class.md).

## Defining a struct

```cpp
struct Object {
  int weight;
  int value;
} e[array_length];

const Object a;
Object b, B[array_length], tmp;
Object *c;
```

The above example defines a struct named `Object`, with two member elements `value, weight`, both of type `int`.

After `}`, it defines a constant `a`, a variable `b`, a variable `tmp`, an array `B`, and a pointer `c` of data type `Object`. For any existing type, we can use the method here to define constants, variables, pointers, arrays, etc.

*About pointers: there is no need to insist on mastering it.*

### Defining a pointer

If defining a pointer to a built-in type, then it is the same as defining a pointer normally.

If defining a struct pointer, use `StructName*` in the definition.

```cpp
struct Edge {
  /*
  ...
  */
  Edge* nxt;
};
```

The above is just an example; there is no need to dwell on the actual meaning.

## Accessing/modifying member elements

We can use `variableName.memberElementName` to access. For example, we can use `cout << var.v` to output the `v` member of `var`.

We can also use `pointerName->memberElementName` or `(*pointerName).memberElementName` to access. For example, using `(*ptr).v = tmp` or `ptr->v = tmp` can assign the member element `v` of the struct pointed to by the struct pointer `ptr` to `tmp`.

## Why do we need structs?

First, all roads lead to Rome; we can achieve the same effect without using structs. But structs can explicitly bundle member elements (usually variables in algorithm competitions) together, such as the `Object` struct in this example, which puts `value, weight` together (the actual meaning of defining this struct is to represent the weight and value of an item). The benefit of this is that it restricts the use of member elements.  
Imagine, if we do not use a struct and have two arrays `value[], Value[]`, it is easy to write them confusingly. But if we use a struct, it can reduce the chance of using variables incorrectly.

And different structs (struct types, such as the `Object` struct) or different struct variables (instances of a struct, such as the `e` array above) can have member elements with the same name (such as `tmp.value, b.value`); member elements with the same name are independent of each other (having their own memory, for example modifying `tmp.value` will not affect the value of `b.value`).  
The benefit of this is that we can use as-identical-or-similar-as-possible variables to describe an item. For example, `Object` has the member variable `value`; we can also define a `Car` struct, which also has the `value` member; if we do not use structs, perhaps we would need to define arrays with different names such as `valueOfObject[], valueOfCar[]` to distinguish them.

*If you want to describe a kind of thing in more detail, you can also define member functions. Please refer to [classes](./class.md) for detailed content.*

## More operations?

See [classes](./class.md) for details.

## Points to note

To make memory access more efficient, when handling the actual storage situation of members in a struct, the compiler may align members at certain byte positions, which means there are empty places in the struct. Therefore, the space occupied by this struct may be larger than the total space occupied by all members in it.

## References

1.  [Class - zh.cppreference.com](https://zh.cppreference.com/w/cpp/language/class)
2.  [Data structures - cplusplus.com](http://www.cplusplus.com/doc/tutorial/structures/)
3.  [Alignment - Microsoft Docs](https://docs.microsoft.com/zh-cn/cpp/cpp/alignment-cpp-declarations)
