A **union** is a special class type that can hold only one of its non-static data members at any one time.

The union was formally added to the entry level of the NOI syllabus in 2023.

## Defining a union

The class specifier declared by a union is similar to the declaration of a class or [struct](./struct.md):

```cpp
union MyUnion {
  int x;
  long long y;
} x;
```

The definition of a union is similar to a struct. According to the above definition, `MyUnion` can likewise be used as a custom type. The name `MyUnion` can be omitted.

## Accessing/modifying member elements

Similar to a struct, we can likewise use `variableName.memberName` to access.

The size of the memory space occupied by a union is **not less than** the size of its largest member; all members **share the memory space and address**. When one member is assigned, due to memory sharing, the other members in this union are all overwritten. That is, at any one time only the value of one member can be stored in the union.

For more uses of unions, see [cppreference: union declaration](https://zh.cppreference.com/w/cpp/language/union).
