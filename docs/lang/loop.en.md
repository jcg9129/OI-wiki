Sometimes, we need to do one thing many times; in order not to write too much repeated code, we need loops.

Sometimes, the number of loop iterations is not a constant, so we cannot repeat the code multiple times, and must use a loop.

## for statement

The following is the structure of the for statement:

```cpp
for (initialization; judgment condition; update) {
  loop body;
}
```

Execution order:

![](images/for-loop.svg)

e.g. Read in n numbers:

```cpp
for (int i = 1; i <= n; ++i) {
  cin >> a[i];
}
```

Among the three parts of the for statement, any one part can be omitted. Among them, if the judgment condition is omitted, it is equivalent to the judgment condition always being true.

## while statement

The following is the structure of the while statement:

```cpp
while (judgment condition) {
  loop body;
}
```

Execution order:

![](images/while-loop.svg)

e.g. Verify the 3x+1 conjecture:

```cpp
while (x > 1) {
  if (x % 2 == 1) {
    x = 3 * x + 1;
  } else {
    x = x / 2;
  }
}
```

## do...while statement

The following is the structure of the do...while statement:

```cpp
do {
  loop body;
} while (judgment condition);
```

Execution order:

![](images/do-while-loop.svg)

The difference from the while statement is that the do...while statement executes the loop body first and then makes the judgment.

e.g. Enumerate permutations:

```cpp
do {
  // do someting...
} while (next_permutation(a + 1, a + n + 1));
```

## The relationship between the three statements

```cpp
// for statement

for (statement1; statement2; statement3) {
  statement4;
}

// while statement

statement1;
while (statement2) {
  statement4;
  statement3;
}
```

They are equivalent when there is no `continue` statement (see below) in statement4, but the latter method is rarely used.

```cpp
// while statement

statement1;
while (statement2) {
  statement1;
}

// do...while statement

do {
  statement1;
} while (statement2);
```

These two ways are also equivalent when there is no `continue` statement in statement1.

```cpp
while (1) {
  // do something...
}

for (;;) {
  // do something...
}
```

Both of these ways loop forever. (You can use `break` (see below) to exit.)

We can see that the three statements can replace each other, but generally speaking, the choice of statement follows the following principles:

1.  When there is a fixed increment step during the loop (the most common is enumeration), use the for statement;
2.  When only the termination condition of the loop is determined, use the while statement;
3.  When using the while statement, if you want to execute the loop body first and then make the judgment, use the do...while statement. It is generally rarely used; a common scenario is user input.

## break and continue statements

The function of the break statement is to exit the loop.

The function of the continue statement is to skip the remaining part of the loop body. Below we take the use of the continue statement in the do...while statement as an example:

```cpp
do {
  // do something...
  continue;  // equivalent to goto END;
// do something...
END:;
} while (statement);

```

Both the break and continue statements can be used in the loop bodies of all three loop statements.

Generally speaking, break and continue statements are used to make the logic of the code clearer, for example:

```cpp
// the logic is relatively unclear, and the brace levels are complex

for (int i = 1; i <= n; ++i) {
  if (i != x) {
    for (int j = 1; j <= n; ++j) {
      if (j != x) {
        // do something...
      }
    }
  }
}

// the logic is clearer, and the brace levels are simple and clear

for (int i = 1; i <= n; ++i) {
  if (i == x) continue;
  for (int j = 1; j <= n; ++j) {
    if (j == x) continue;
    // do something...
  }
}
```

```cpp
// the for statement's judgment condition is complex and does not reflect the essence of "enumeration"

for (int i = l; i <= r && i % 10 != 0; ++i) {
  // do something...
}

// the for statement is used for enumeration, and break is used for "until when to stop"

for (int i = l; i <= r; ++i) {
  if (i % 10 == 0) break;
  // do something...
}
```

```cpp
// statements are repeated, and the order is unnatural

statement1;
while (statement3) {
  statement2;
  statement1;
}

// no repeated statements, and the order is natural

while (1) {
  statement1;
  if (!statement3) break;
  statement2;
}
```
