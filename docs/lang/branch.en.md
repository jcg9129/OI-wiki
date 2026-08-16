By default, a program executes in the order of the code; sometimes we need to selectively execute certain statements, and at this time we need the functionality of branching to achieve it. Choosing appropriate branch statements can improve the efficiency of the program.

## if statement

### Basic if statement

The following is the structure of the basic if statement.

```cpp
if (condition) {
  body;
}
```

The if statement evaluates the condition; if the result is true (non-zero), it executes the statement, otherwise it does not.

If there is only a single statement in the body, the braces can be omitted.

### if...else statement

```cpp
if (condition) {
  body1;
} else {
  body2;
}
```

The if...else statement is similar to the if statement; else does not need to write a condition again. When the condition of the if statement is satisfied, the statement inside the if will be executed; when the condition of the if statement is not satisfied, the statement inside the else will be executed. Similarly, when the body has only one statement, the braces can be omitted.

### else if statement

```cpp
if (condition1) {
  body1;
} else if (condition2) {
  body2;
} else if (condition3) {
  body3;
} else {
  body4;
}
```

The else if statement is a combination of if and else, judging multiple conditions and choosing different statement branches. The final else statement does not need to write a condition again. For example, if condition 1 is true, execute body 1; if condition 3 is true while conditions 1 and 2 are both false, execute body 3; only when all conditions are false is body 4 executed.

In fact, this statement is equivalent to the else clause of the first if having only one if statement, which is put together after omitting the braces. If the conditions are in a parallel relationship with each other, writing this way can make the logic of the code clearer.

Logically, it is roughly equivalent to this passage:

> The relationship between the roots of a quadratic equation and the discriminant:
>
> -   If ($\Delta<0$)
>     the equation has no solution;
> -   Otherwise, if ($\Delta=0$)
>     the equation has two identical real solutions;
> -   Otherwise
>     the equation has two different real solutions;

## switch statement

```cpp
switch (selection clause) {
  case label1:
    body1;
  case label2:
    body2;
  default:
    body3;
}
```

When the switch statement executes, it first computes the value of the selection clause, then selects the corresponding label according to the value of the selection clause, and starts executing from the label. Here, the selection clause must be an integer-type expression, and the labels must all be integer-type constants. For example:

```cpp
int i = 1;  // the data type of i here is integer, which satisfies the requirement of an integer-type expression

switch (i) {
  case 1:
    cout << "OI WIKI" << endl;
}
```

```cpp
char i = 'A';

// the data type of i here is character, but char
// is also an integer type, which satisfies the requirement of an integer-type expression
switch (i) {
  case 'A':
    cout << "OI WIKI" << endl;
}
```

In the switch statement, we also need to add break statements to interrupt according to the need, otherwise after the corresponding case is selected, the statements in all subsequent cases and the statements in default will all be run. See the example below for a specific example.

```cpp
char i = 'B';

switch (i) {
  case 'A':
    cout << "OI" << endl;
    break;

  case 'B':
    cout << "WIKI" << endl;

  default:
    cout << "Hello World" << endl;
}
```

After running the above code, the output results are `WIKI` and `Hello World`; if you do not want the statements of the branches below to be run, you need break. See the example below for a specific example.

```cpp
char i = 'B';

switch (i) {
  case 'A':
    cout << "OI" << endl;
    break;

  case 'B':
    cout << "WIKI" << endl;
    break;

  default:
    cout << "Hello World" << endl;
}
```

After running the above code, the output result is WIKI, because of the existence of break, the subsequent statements will not continue to be executed. The last statement does not need break, because there is no statement below.

The entry labels cannot be repeated, but can be reversed. That is to say, the order of the entry labels does not matter. The order of appearance of each case (including default) can be arbitrary. For example:

```cpp
char i = 'B';

switch (i) {
  case 'B':
    cout << "WIKI" << endl;
    break;

  default:
    cout << "Hello World" << endl;
    break;

  case 'A':
    cout << "OI" << endl;
}
```

The case clauses of switch can also optionally add braces. But note that if you need to define variables in the switch statement, the braces must be added. For example:

```cpp
char i = 'B';

switch (i) {
  case 'A': {
    int i = 1, j = 2;
    cout << "OI" << endl;
    ans = i + j;
    break;
  }

  case 'B': {
    int qwq = 3;
    cout << "WIKI" << endl;
    ans = qwq * qwq;
    break;
  }

  default: {
    cout << "Hello World" << endl;
  }
}
```

??? note "How to understand switch"
    In the above text, a lot of terms such as "case clause" and "case sub-clause" are used; in fact, in the low-level implementation, switch is equivalent to a set of jump statements. Because of this, there is the clever trick of Duff's Device; those who wish to understand it can study it on their own.
