author: aofall, greyqz, Ir1d, Link-cute, Marcythm, ouuan, Shen-Linwood, sshwy, StudyingFather

## Arithmetic operators

| Operator | Function |
| --------- | --- |
|  `+` (unary) | positive |
|  `-` (unary) | negative |
|  `*` (binary) | multiplication |
|  `/` | division |
|  `%` | modulo |
|  `+` (binary) | addition |
|  `-` (binary) | subtraction |

??? note "Unary and binary operators"
    A unary operator refers to an operator that has only one operated object, while a binary operator has two operated objects. For example, the plus sign in `1 + 2` is a binary operator; it has two operands `1` and `2`. In addition, C++ also has the only ternary operator `?:`.

Among the arithmetic operators, there are two unary operators (positive, negative) and five binary operators (multiplication, division, modulo, addition, subtraction), of which the unary operators have the highest precedence.

The modulo operator `%` means computing the remainder obtained by dividing two integers, i.e. finding the remainder.

And `-`, when it is a binary operator, acts as the subtraction operator, such as `2-1`; when it is a unary operator, it acts as the negation operator, such as `-1`.

The usage is as follows

 `op=x-y*z` 

The computed value of `op` obtained follows the precedence rules of addition, subtraction, multiplication, and division in mathematics: the higher-precedence operation is performed first, operations of the same precedence are computed according to the associativity of the operation, and parentheses raise the precedence.

### Type conversion in arithmetic operations

For binary arithmetic operators, when the types of the two variables participating in the operation are the same, no [type conversion](./var.md#type-conversion) occurs, and the operation result will be held by the type of the variables participating in the operation; otherwise, type conversion will occur to make the types of the two variables consistent. For the rules of conversion, see [type conversion](./var.md#type-conversion).

For example, for an integer (`int`) variable $x$ and another double-precision floating-point (`double`) type variable $y$:

-  The result of `x/3` will be an integer;
-  The result of `x/3.0` will be a double-precision floating point;
-  The result of `x/y` will be a double-precision floating point;
-  The result of `x*1/3` will be an integer;
-  The result of `x*1.0/3` will be a double-precision floating point;

## Bit operators

See also: [bit operations](../math/bit.md#bit-operations).

| Operator | Function |
| --------- | ---- |
|  `~` | bitwise NOT |
|  `&` (binary) | bitwise AND |
|  `|` | bitwise OR |
|  `^` | bitwise XOR |
|  `<<` | bitwise left shift |
|  `>>` | bitwise right shift |

For the meaning of bit operations, refer to the [bit operations](../math/bit.md) page. Note that the precedence of bit operations is lower than that of arithmetic operators (except negation), and bitwise AND, bitwise OR, and XOR are lower than comparison operators (see [C++ operator precedence table](#c-operator-precedence-table) for details), so extra attention is needed when using them, and parentheses should be added when necessary.

In shift operations, if the following situations occur, the behavior is undefined:

1.  The right operand (i.e. the shift amount) is negative;
2.  The right operand is greater than or equal to the number of bits of the left operand;

For example, for a variable `a` of type `int32_t`, both `a<<-1` and `a<<32` are undefined.

For the left shift operation of a signed non-negative number, we need to ensure that the shifted result can be held by the type of the original number, otherwise the behavior is also undefined.[^note1] Performing a left shift operation on a negative number is also undefined.[^note2]

For the right shift operation, the excess bits on the right will be discarded, and the left side is more complex: for unsigned numbers, $0$ is padded on the left[^note3]; while for signed numbers, the number of the highest bit (which is actually the sign bit, $0$ for non-negative numbers, $1$ for negative numbers) is padded[^note4].

## Increment/decrement operators

Sometimes we need to make a variable increase by 1 (increment) or decrease by 1 (decrement); at this time the increment operator `++` and the decrement operator `--` come in handy.

The increment/decrement operator can be placed before or after a variable; before the variable it is called prefix, and after the variable it is called postfix. When used alone, prefix and postfix do not need to be specially distinguished; if the value of the expression is needed, attention is required; for specifics see the example below. For detailed situations, refer to the example part introduced in [references](./reference.md).

```cpp
i = 100;

op1 = i++;  // op1 = 100, first op1 = i, then i = i + 1

i = 100;

op2 = ++i;  // op2 = 101, first i = i + 1, then assign op2

i = 100;

op3 = i--;  // op3 = 100, first assign op3, then i = i - 1

i = 100;

op4 = --i;  // op4 = 99, first i = i - 1, then assign op4
```

## Compound assignment operators

Compound assignment operators are actually abbreviated forms of expressions. They can be divided into compound arithmetic operators `+=`, `-=`, `*=`, `/=`, `%=` and compound bit operators `&=`, `|=`, `^=`, `<<=`, `>>=`.

For example, `op = op + 2` can be written as `op += 2`, `op = op - 2` can be written as `op -= 2`, and `op= op * 2` can be written as `op *= 2`.

## Conditional operator

The conditional operator can be regarded as an abbreviation of the `if` statement; in `a ? b : c`, if the expression `a` holds, then the result of this conditional expression is `b`, otherwise the result of the conditional expression is `c`.
## Comparison operators

| Operator | Function |
| ------ | ---- |
|  `>` | greater than |
|  `>=` | greater than or equal to |
|  `<` | less than |
|  `<=` | less than or equal to |
|  `==` | equal to |
|  `!=` | not equal to |

What especially needs attention among them is to distinguish the equality operator `==` from the assignment operator `=`; this is especially important in judgment statements.

 `if (op=1)` and `if (op==1)` look similar, but their actual functions are vastly different. The first statement is assigning to op; if the assignment is non-0 it is a true value, so the condition of the expression is always satisfied, and it cannot achieve the effect of judgment; while the second statement is the one that judges the value of `op`.

## Logical operators

| Operator | Function |
| ------ | --- |
|  `&&` | logical AND |
|  `||` | logical OR |
|  `!` | logical NOT |

```cpp
Result = op1 && op2;  // when both op1 and op2 are true, Result is true

Result = op1 || op2;  // when one of op1 or op2 is true, Result is true

Result = !op1;  // when op1 is false, Result is true
```

The **built-in** operators `&&` and `||` perform short-circuit evaluation (if the result is known after evaluating the first operand, the second is not evaluated); overloaded operators do not have this characteristic and always evaluate both operands.

## Comma operator

The comma operator can separate multiple expressions; the separated expressions are computed in order from left to right, and the value of the whole expression is the value of the last expression. The precedence of the comma expression is the **lowest** among all operators.

```cpp
exp1, exp2, exp3;  // the final value is the operation result of exp3.

Result = 1 + 2, 3 + 4, 5 + 6;
// the value of Result obtained is 3 rather than 11, because the precedence of the assignment operator "="
// is higher than the comma operator, so the assignment operation is performed first before the comma operation.

Result = (1 + 2, 3 + 4, 5 + 6);

// if you want the value of Result to obtain the result of the comma operation, you should raise the precedence by wrapping the whole expression in parentheses; at this time
// the value of Result is 11.
```

## Member access operators

| Operator | Function |
| --------- | -------- |
|  `[]` | array subscript |
|  `.` | object member |
|  `&` (unary) | get address / get reference |
|  `*` (unary) | indirect addressing / dereference |
|  `->` | pointer member |

These operators are used to access the members or memory of an object; except for the last operator, the above operators can all be overloaded. For content related to `&`, `*`, and `->`, please read the [pointers](./pointer.md) and [references](./reference.md) tutorials. Here two rarely-used operators `.*` and `->*` are also omitted; their specific usage can be seen in the [C++ language manual](https://zh.cppreference.com/w/cpp/language/operator_member_access).

```cpp
auto result1 = v[1];  // get the object with subscript 2 in v
auto result2 = p.q;   // get the q member of object p
auto result3 = p -> q;  // get the q member of the object pointed to by pointer p, equivalent to (*p).q
auto result4 = &v;      // get the pointer pointing to v
auto result5 = *v;      // get the object pointed to by pointer v
```

## C++ operator precedence table

From [C++ operator precedence - cppreference](https://zh.cppreference.com/w/cpp/language/operator_precedence), with modifications.

| Operator | Description | Example | Overloadable |
| :------------------: | :------: | :----------------------------------------------------------: | :--: |
| **Level 1** | | | |
| `::` | scope resolution operator | `Class::age = 2;` | Not overloadable |
| **Level 2** | | | |
| `++` | postfix increment operator | `for (int i = 0; i < 10; i++) cout << i;` | Overloadable |
| `--` | postfix decrement operator | `for (int i = 10; i > 0; i--) cout << i;` | Overloadable |
| `type()  type{}` | cast | `unsigned int a = unsigned(3.14);` | Overloadable |
| `()` | function call | `isdigit('1')` | Overloadable |
| `[]` | array data access | `array[4] = 2;` | Overloadable |
| `.` | object-style member call | `obj.age = 34;` | Not overloadable |
| `->` | pointer-style member call | `ptr->age = 34;` | Overloadable |
| **Level 3** (right-to-left associativity) | | | |
| `++` | prefix increment operator | `for (i = 0; i < 10; ++i) cout << i;` | Overloadable |
| `--` | prefix decrement operator | `for (i = 10; i > 0; --i) cout << i;` | Overloadable |
| `+` | positive sign | `int i = +1;` | Overloadable |
| `-` | negative sign | `int i = -1;` | Overloadable |
| `!` | logical negation | `if (!done) …` | Overloadable |
| `~` | bitwise negation | `flags = ~flags;` | Overloadable |
| `(type)` | C-style cast | `int i = (int) floatNum;` | Overloadable |
| `*` | pointer dereference | `int data = *intPtr;` | Overloadable |
| `&` | address-of value | `int *intPtr = &data;` | Overloadable |
| `sizeof` | return type memory | `int size = sizeof floatNum; int size = sizeof(float);` | Not overloadable |
| `new` | dynamic element memory allocation | `long *pVar = new long; MyClass *ptr = new MyClass(args);` | Overloadable |
| `new []` | dynamic array memory allocation | `long *array = new long[n];` | Overloadable |
| `delete` | dynamic element memory destruction | `delete pVar;` | Overloadable |
| `delete []` | dynamic array memory destruction | `delete [] array;` | Overloadable |
| **Level 4** | | | |
| `.*` | class object member reference | `obj.*var = 24;` | Not overloadable |
| `->*` | class pointer member reference | `ptr->*var = 24;` | Overloadable |
| **Level 5** | | | |
| `*` | multiplication | `int i = 2 * 4;` | Overloadable |
| `/` | division | `float f = 10.0 / 3.0;` | Overloadable |
| `%` | remainder (modulo operation) | `int rem = 4 % 3;` | Overloadable |
| **Level 6** | | | |
| `+` | addition | `int i = 2 + 3;` | Overloadable |
| `-` | subtraction | `int i = 5 - 1;` | Overloadable |
| **Level 7** | | | |
| `<<` | bitwise left shift | `int flags = 33 << 1;` | Overloadable |
| `>>` | bitwise right shift | `int flags = 33 >> 1;` | Overloadable |
| **Level 8** | | | |
| `<=>` | three-way comparison operator | `if ((i <=> 42) < 0) ...` | Overloadable |
| **Level 9** | | | |
| `<` | less than | `if (i < 42) ...` | Overloadable |
| `<=` | less than or equal to | `if (i <= 42) ...` | Overloadable |
| `>` | greater than | `if (i > 42) ...` | Overloadable |
| `>=` | greater than or equal to | `if (i >= 42) ...` | Overloadable |
| **Level 10** | | | |
| `==` | equal to | `if (i == 42) ...` | Overloadable |
| `!=` | not equal to | `if (i != 42) ...` | Overloadable |
| **Level 11** | | | |
| `&` | bitwise AND operation | `flags = flags & 42;` | Overloadable |
| **Level 12** | | | |
| `^` | bitwise XOR operation | `flags = flags ^ 42;` | Overloadable |
| **Level 13** | | | |
| `|` | bitwise OR operation | `flags = flags | 42;` | Overloadable |
| **Level 14** | | | |
| `&&` | logical AND operation | `if (conditionA && conditionB) ...` | Overloadable |
| **Level 15** | | | |
| `||` | logical OR operation | `if (conditionA || conditionB) ...` | Overloadable |
| **Level 16** (right-to-left associativity) | | | |
| `? :` | conditional operator | `int i = a > b ? a : b;` | Not overloadable |
| `throw` | exception throwing | `throw EClass("Message");` | Not overloadable |
| `=` | assignment | `int a = b;` | Overloadable |
| `+=` | add-assignment operation | `a += 3;` | Overloadable |
| `-=` | subtract-assignment operation | `b -= 4;` | Overloadable |
| `*=` | multiply-assignment operation | `a *= 5;` | Overloadable |
| `/=` | divide-assignment operation | `a /= 2;` | Overloadable |
| `%=` | modulo-assignment operation | `a %= 3;` | Overloadable |
| `<<=` | bitwise-left-shift-assignment operation | `flags <<= 2;` | Overloadable |
| `>>=` | bitwise-right-shift-assignment operation | `flags >>= 2;` | Overloadable |
| `&=` | bitwise-AND-assignment operation | `flags &= new_flags;` | Overloadable |
| `^=` | bitwise-XOR-assignment operation | `flags ^= new_flags;` | Overloadable |
| `|=` | bitwise-OR-assignment operation | `flags |= new_flags;` | Overloadable |
| **Level 17** | | | |
| `,` | comma separator | `for (i = 0, j = 0; i < 10; i++, j++) ...` | Overloadable |

Note that the table does not list operators such as `const_cast`, `static_cast`, `dynamic_cast`, `reinterpret_cast`, `typeid`, `sizeof...`, `noexcept`, and `alignof`, because their usage form is the same as a function call and there is no ambiguity.

## References and notes

[^note1]: Before C++20, if the original value is a signed type and the shifted result can be held by the unsigned version of the original type, then this result is [converted](../lang/var.md#type-conversion) to the corresponding signed value, otherwise the behavior is undefined; the left shift of an unsigned number discards the bits shifted out of the result type. Since C++20, `a << b` is specified as the value of $a\cdot 2^b$ modulo $2^N$ ($N$ is the bit width of the result type), i.e. whether it is a signed number or an unsigned number, the left shift directly discards the bits shifted out of the result type (i.e. [arithmetic left shift / logical left shift](../math/bit.md#shift)).

[^note2]: Before C++20. For the behavior since C++20, see[^note1].

[^note3]: I.e. [logical right shift](../math/bit.md#shift).

[^note4]: I.e. [arithmetic right shift](../math/bit.md#shift). Before C++20, signed right shift is implementation-defined; in most implementations, arithmetic right shift is adopted. Since C++20, `a >> b` is specified as $\lfloor a/2^b\rfloor$, so signed right shift is arithmetic right shift.
