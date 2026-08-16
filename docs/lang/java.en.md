## About Java

Java is a widely used computer programming language with the characteristics of being **cross-platform**, **object-oriented**, and supporting **generic programming**; it is widely applied in enterprise-level Web application development and mobile application development.

## Environment installation

See [JDK](../tools/compiler.md#jdk).

## Basic syntax

### Main function

Java, similar to the C/C++ language, needs a function (in object orientation, this is called a method) as the entry point for program execution.

The format of Java's main function is fixed, of the form:

```java
class Test {
    public static void main(String[] args) {
        // the program's code
    }
}
```

A packaged Java program (the name is generally `*.jar`) can have many similar functions, but when running this program, only one of the functions will be run; this is defined in the `Manifest` file of the `Jar`, and knowledge about it is generally not needed in OI competitions.

### Comments

Like C/C++, Java uses `//` and `/* */` to comment single lines and multiple lines respectively.

### Basic data types

| Type name | Meaning |
| :-----: | :---: |
| boolean | boolean type |
| byte | byte type |
| char | character type |
| double | double-precision floating point |
| float | single-precision floating point |
| int | integer type |
| long | long integer type |
| short | short integer type |
| null | null |

### Declaring variables

```java
int a = 12; // set a to integer type, and assign a the value 12
String str = "Hello, OI-wiki"; // declare the string variable str
char ch = 'W';
double PI = 3.1415926;
```

### The final keyword

`final` means this is the final, unchangeable result; a variable modified by `final` can only be assigned once, and does not change after assignment.

```java
final double PI = 3.1415926;
```

### Arrays

```java
// an integer-type array with ten elements
// its syntax format is data type[] variable name = new data type[array size]
int[] ary = new int[10];
```

### Strings

-   String is a built-in class of Java.

```java
// the simplest way to construct a string variable is as follows
String a = "Hello";

// we can also construct a string variable using a character array
char[] stringArray = { 'H', 'e', 'l', 'l', 'o' };
String s = new String(stringArray);
```

### Packages and importing packages

Classes (`Class`) in Java are placed in packages (`package`). Classes with the same name are not allowed in one package. In the first line of a class, we usually specify which package this class belongs to. For example:

```java
package org.oi-wiki.tutorial;
```

The naming convention for packages is generally: `top-level domain of the project owner.second-level domain of the project owner.project name`.

We use the `import` keyword to import classes that are not under the package to which this class belongs. For example, the `Scanner` to be used below:

```java
import java.util.Scanner;
```

If we want to import all classes under a certain package, we only need to change the class name before the final semicolon of this statement to `*`.

### Input

We can handle command-line input through the `Scanner` class.

```java
package org.oiwiki.tutorial;

import java.util.Scanner;

class Test {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in); // System.in is the input stream
        int a = scan.nextInt();
        double b = scan.nextDouble();
        String c = scan.nextLine();
    }
}
```

### Output

We can perform formatted output on variables.

| Symbol | Meaning |
| :--: | :---: |
| `%f` | floating-point type |
| `%s` | string type |
| `%d` | integer type |
| `%c` | character type |

```java
class Test {
    public static void main(String[] args) {
        int a = 12;
        char b = 'A';
        double s = 3.14;
        String str = "Hello world";
        System.out.printf("%f\n", s);
        System.out.printf("%d\n", a);
        System.out.printf("%c\n", b);
        System.out.printf("%s\n", str);
    }
}
```

### Control statements

Java's flow control statements are basically the same as C++.

#### Selection

-   if

```java
class Test {
    public static void main(String[] args) {
        if ( /* judgment condition */ ){
            // execute the code inside here when the condition holds
        }
    }
}
```

-   if...else

```java
class Test {
    public static void main(String[] args) {
        if ( /* judgment condition */ ) {
            // execute the code inside here when the condition holds
        } else {
            // execute the code inside here when the condition does not hold
        }
    }
}
```

-   if...else if...else

```java
class Test {
    public static void main(String[] args) {
        if ( /* judgment condition */ ) {
            // execute the code inside here when the judgment condition holds
        } else if ( /* judgment condition 2 */ ) {
            // execute the code inside here when judgment condition 2 holds
        } else {
          // execute the code inside here when none of the above conditions hold
        }
    }
}
```

-   switch...case

```java
class Test {
    public static void main(String[] args) {
        switch ( /* expression */ ){
          case /* value 1 */:
              // execute this piece of code when the value obtained by the expression matches value 1
              break; // if the break statement is not added, the program will execute downward in order until break
          case /* value 2 */:
              // execute this piece of code when the value obtained by the expression matches value 2
              break;
          default:
              // execute the code inside here when the expression does not match the values listed above
        }
    }
}
```

#### Loops

-   for

The `for` keyword has two usages, of which the first is the ordinary `for` loop, of the form:

```java
class Test {
    public static void main(String[] args) {
        for ( /* initialization */; /* the loop's judgment condition */; /* the step executed after each loop */ ) {
            // execute the code inside the loop body when the loop condition holds
        }
    }
}
```

The second is the `foreach` usage similar to C++, used to loop over data in an array or collection, equivalent to hiding the loop variable in the previous way, of the form:

```java
class Test {
    public static void main(String[] args) {
        for ( /* element type X */ /* element name Y */ : /* collection Z */ ) {
            // in each loop of this statement block, the element Y is respectively an element in the collection Z.
        }
    }
}
```

-   while

```java
class Test {
    public static void main(String[] args) {
        while ( /* judgment condition */ ) {
            // execute the code inside the loop body when the condition holds
        }
    }
}
```

-   do...while

```java
class Test {
    public static void main(String[] args) {
        do {
          // the code that needs to be executed
        } while ( /* loop judgment condition */ );
    }
}
```

## Points to note

### The class name should be consistent with the file name

To create a Java source program, the class name and the file name need to be consistent to compile successfully, otherwise the compiler will prompt that the class cannot be found. Usually the file name will be specified in the specific OJ.

Example:

`Add.java`

```java
class Add {
    public static void main(String[] args) {
        // ...
    }
}
```

In this file, `Add` must be used as the class name in order to compile successfully.
