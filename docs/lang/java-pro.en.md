???+ warning "Note"
    The following content is all written based on the Java JDK 8 version; the possibility of some changes in higher versions is not ruled out.

## Faster input and output

`Scanner` and `System.out.print` will work well at the very beginning, but will reduce efficiency when handling larger inputs, so we will need to use some methods to improve IO speed.

### Using Kattio + StringTokenizer as input

One of the most commonly used methods is to use [Kattio.java](https://github.com/Kattis/kattio/blob/master/Kattio.java) from Kattis to improve IO efficiency.[^ref1] This method wraps `StringTokenizer` and `PrintWriter` in one class for convenient use. And when actually solving problems (if the contest organizer/committee allows), you can directly use this template.

Below is the IO template that should be included in the code; since Kattis's original Kattio contains some functionality that is not commonly used, the template below has been adjusted somewhat (the original Kattio uses MIT as the license).

```java
class Kattio extends PrintWriter {
    private BufferedReader r;
    private StringTokenizer st;
    // standard IO
    public Kattio() { this(System.in, System.out); }
    public Kattio(InputStream i, OutputStream o) {
        super(o);
        r = new BufferedReader(new InputStreamReader(i));
    }
    // file IO
    public Kattio(String intput, String output) throws IOException {
        super(output);
        r = new BufferedReader(new FileReader(intput));
    }
    // returns null when there is no other input
    public String next() {
        try {
            while (st == null || !st.hasMoreTokens())
                st = new StringTokenizer(r.readLine());
            return st.nextToken();
        } catch (Exception e) {}
        return null;
    }
    public int nextInt() { return Integer.parseInt(next()); }
    public double nextDouble() { return Double.parseDouble(next()); }
    public long nextLong() { return Long.parseLong(next()); }
}
```

The code below simply demonstrates the use of Kattio:

```java
class Test {
    public static void main(String[] args) {
        Kattio io = new Kattio();
        // string input
        String str = io.next();
        // int input
        int num = io.nextInt();
        // output
        io.println("Result");
        // please make sure to close the IO stream to ensure the output is correctly written
        io.close();
    }
}
```

### Using StreamTokenizer as input

In some cases, using `StringTokenizer` will cause MLE (Memory Limit Exceeded); at this time we need to use `StreamTokenizer` as input.

```java
import java.io.*;
public class Main {
    // IO code
    public static StreamTokenizer in = new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in), 32768));
    public static PrintWriter out = new PrintWriter(new OutputStreamWriter(System.out));
    public static double nextDouble() throws IOException { in.nextToken(); return in.nval; }
    public static float nextFloat() throws IOException { in.nextToken(); return (float)in.nval; }
    public static int nextInt() throws IOException { in.nextToken(); return (int)in.nval; }
    public static String next() throws IOException { in.nextToken(); return in.sval; }
    public static long nextLong() throws Exception { in.nextToken(); return (long)in.nval;}
    
    // usage example
    public static void main(String[] args) throws Exception {
        int n = nextInt();
        out.println(n);
        out.close();
    }
}
```

### Analysis and comparison between the Kattio + StringTokenizer method and the StreamTokenizer method

1.  `StreamTokenizer` uses less memory compared with `StringTokenizer`; when the Java standard solution MLEs, you can try using `StreamTokenizer`, but `StreamTokenizer` loses precision and will have problems when reading some data;
    -   The `StreamTokenizer` source code has a `Type`; this `Type` decides the type according to the input content; if the input is a string like `123oi` that **starts with a digit**, it will forcibly consider the type to be `double` type, so reading a `String` type as `double` type during reading will throw an exception;
    -   `StreamTokenizer` will lose precision when reading numbers of size `1e14` and above;
2.  When using `PrintWriter`, note that you need to `close()` the output stream at the very end of the program or use `flush()` to clear the buffer when output is needed, otherwise the content will not be written to the console/file.
3.  `Kattio` inherits from the `PrintWriter` class, so its own object has the functionality of `PrintWriter`, so you can directly call the functions of the `PrintWriter` class to output, while modifying `StringTokenizer` as its own member variable. The second `Main` uses both `StreamTokenizer` and `PrintWriter` as its own member variables, so there is a slight difference in usage.

In summary, in most cases, the usage situation of `StringTokenizer` is superior to `StreamTokenizer`; in extreme MLE cases you can try `StreamTokenizer`, and at the same time `StreamTokenizer` is powerless to handle data above the `int` range.

## BigInteger and number theory

`BigInteger` is the high-precision computation class provided by Java, which can conveniently solve high-precision problems.

### Initialization

The commonly used ways to create `BigInteger` are the following two:

```java
import java.io.PrintWriter;
import java.math.BigInteger;

class Main {
    static PrintWriter out = new PrintWriter(System.out);
    public static void main(String[] args) {
        BigInteger a = new BigInteger("12345678910");  // create a BigInteger object from a string in decimal form
        out.println(a);  // the value of a is 12345678910 
        BigInteger b = new BigInteger("1E", 16);  // create a BigInteger object from a string in a specified base
        out.println(b);  // the value of b is 30 
        out.close();
    }
}

```

### Basic operations

Below, `this` is used to represent the current `BigIntger`:

| Function name | Function |
| :-------------------------: | :----------------------------: |
| `abs()` | Return the absolute value of `this` |
| `negate()` | Return the opposite of `this` |
| `add(BigInteger val)` | Return the sum of `this` and `val` |
| `subtract(BigInteger val)` | Return the difference of `this` and `val` |
| `multiply(BigInteger val)` | Return the product of `this` and `val` |
| `divide(BigInteger val)` | Return the quotient of `this` and `val` |
| `remainder(BigInteger val)` | Return the remainder of `this` divided by `val` |
| `mod(BigInteger val)` | Return the value of `this` modulo `val` |
| `pow(int val)` | Return `this` to the `val`-th power |
| `and(BigInteger val)` | Return the bitwise AND of `this` and `val` |
| `or(BigInteger val)` | Return the bitwise OR of `this` and `val` |
| `not()` | Return the bitwise NOT of `this` |
| `xor(BigInteger val)` | Return the bitwise XOR of `this` and `val` |
| `shiftLeft(int n)` | Return `this` left-shifted by `n` bits |
| `shiftRight(int n)` | Return `this` right-shifted by `n` bits |
| `max(BigInteger val)` | Return the larger of `this` and `val` |
| `min(BigInteger val)` | Return the smaller of `this` and `val` |
| `bitCount()` | Return the number of `1`s in the binary of `this` excluding the sign bit |
| `bitLength()` | Return the length of the binary of `this` excluding the sign bit |
| `getLowestSetBit()` | Return the rightmost set-bit position in the binary of `this` |
| `compareTo(BigInteger val)` | Compare the sizes of `this` and `val` |
| `toString()` | Return the decimal string representation of `this` |
| `toString(int radix)` | Return the base-`radix` string representation of `this` |

Usage example is as follows:

```java
import java.io.PrintWriter;
import java.math.BigInteger;

public class Main {
    static PrintWriter out = new PrintWriter(System.out);
    static BigInteger a, b;
    
    static void abs() {
        out.println("abs:");
        a = new BigInteger("-123");
        out.println(a.abs());  // output 123 
        a = new BigInteger("123");
        out.println(a.abs());  // output 123 
    }
    
    static void negate() {
        out.println("negate:");
        a = new BigInteger("-123");
        out.println(a.negate());  // output 123 
        a = new BigInteger("123");
        out.println(a.negate());  // output -123 
    }
    
    static void add() {
        out.println("add:");
        a = new BigInteger("123");
        b = new BigInteger("123");
        out.println(a.add(b));  // output 246 
    }
    
    static void subtract() {
        out.println("subtract:");
        a = new BigInteger("123");
        b = new BigInteger("123");
        out.println(a.subtract(b));  // output 0 
    }
    
    static void multiply() {
        out.println("multiply:");
        a = new BigInteger("12");
        b = new BigInteger("12");
        out.println(a.multiply(b));  // output 144 
    }
    
    static void divide() {
        out.println("divide:");
        a = new BigInteger("12");
        b = new BigInteger("11");
        out.println(a.divide(b));  // output 1 
    }
    
    static void remainder() {
        out.println("remainder:");
        a = new BigInteger("12");
        b = new BigInteger("10");
        out.println(a.remainder(b));  // output 2 
        a = new BigInteger("-12");
        b = new BigInteger("10");
        out.println(a.remainder(b));  // output -2 
    }
    
    static void mod() {
        out.println("mod:");
        a = new BigInteger("12");
        b = new BigInteger("10");
        out.println(a.mod(b));  // output 2 
        a = new BigInteger("-12");
        b = new BigInteger("10");
        out.println(a.mod(b));  // output 8 
    }
    
    static void pow() {
        out.println("pow:");
        a = new BigInteger("2");
        out.println(a.pow(10));  // output 1024 
    }
    
    static void and() {
        out.println("and:");
        a = new BigInteger("3");  // 11 
        b = new BigInteger("5");  // 101 
        out.println(a.and(b));  // output 1 
    }
    
    static void or() {
        out.println("or:");
        a = new BigInteger("2");  // 10 
        b = new BigInteger("5");  // 101 
        out.println(a.or(b));  // output 7 
    }
    
    static void not() {
        out.println("not:");
        a = new BigInteger("2147483647");  // 01111111 11111111 11111111 11111111 
        out.println(a.not());  // output -2147483648, binary is: 10000000 00000000 00000000 00000000 
    }
    
    static void xor() {
        out.println("xor:");
        a = new BigInteger("6");  // 110 
        b = new BigInteger("5");  // 101 
        out.println(a.xor(b));  // 011 output 3 
    }
    
    static void shiftLeft() {
        out.println("shiftLeft:");
        a = new BigInteger("1");
        out.println(a.shiftLeft(10));  // output 1024 
    }
    
    static void shiftRight() {
        out.println("shiftRight:");
        a = new BigInteger("1024");
        out.println(a.shiftRight(8));  // output 4 
    }
    
    static void max() {
        out.println("max:");
        a = new BigInteger("6");
        b = new BigInteger("5");
        out.println(a.max(b));  // output 6 
    }
    
    static void min() {
        out.println("min:");
        a = new BigInteger("6");
        b = new BigInteger("5");
        out.println(a.min(b));  // output 5 
    }
    
    static void bitCount() {
        out.println("bitCount:");
        a = new BigInteger("6");  // 110 
        out.println(a.bitCount());  // output 2 
    }
    
    static void bitLength() {
        out.println("bitLength:");
        a = new BigInteger("6");  // 110 
        out.println(a.bitLength());  // output 3 
    }
    
    static void getLowestSetBit() {
        out.println("getLowestSetBit:");
        a = new BigInteger("8");  // 1000 
        out.println(a.getLowestSetBit());  // output 3 
    }
    
    static void compareTo() {
        out.println("compareTo:");
        a = new BigInteger("8");
        b = new BigInteger("9");
        out.println(a.compareTo(b));  // output -1 
        a = new BigInteger("8");
        b = new BigInteger("8");
        out.println(a.compareTo(b));  // output 0 
        a = new BigInteger("8");
        b = new BigInteger("7");
        out.println(a.compareTo(b));  // output 1 
    }
    
    static void toStringTest() {
        out.println("toString:");
        a = new BigInteger("15");
        out.println(a.toString());  // output 15 
        out.println(a.toString(16));  // output f 
    }
    
    public static void main(String[] args) {
        abs();
        negate();
        add();
        subtract();
        multiply();
        divide();
        remainder();
        mod();
        pow();
        and();
        or();
        not();
        xor();
        shiftLeft();
        shiftRight();
        max();
        min();
        bitCount();
        bitLength();
        getLowestSetBit();
        compareTo();
        toStringTest();
        out.close();
    }
}
```

### Mathematical operations

Below, `this` is used to represent the current `BigIntger`:

| Function name | Function |
| :----------------------------------: | :------------------------------: |
| `gcd(BigInteger val)` | Return the greatest common divisor of the absolute value of `this` and the absolute value of `val` |
| `isProbablePrime(int val)` | Return a boolean value indicating whether `this` is prime |
| `nextProbablePrime()` | Return the first prime greater than `this` |
| `modPow(BigInteger b, BigInteger p)` | Return the value of `this` to the `b`-th power modulo `p` |
| `modInverse(BigInteger p)` | Return the multiplicative inverse of `this` modulo `p` |

Usage example is as follows:

```java
import java.io.PrintWriter;
import java.math.BigInteger;

public class Main {
    static PrintWriter out = new PrintWriter(System.out);
    static BigInteger a, b, p;
    
    static void gcd() {  // greatest common divisor 
        a = new BigInteger("120032414321432144212100");
        b = new BigInteger("240231431243123412432140");
        out.println(String.format("gcd(%s,%s)=%s", a.toString(), b.toString(), a.gcd(b).toString()));  // gcd(120032414321432144212100,240231431243123412432140)=20 
    }
    
    static void isPrime() {  // determine whether the number is prime based on Miller-Rabin; the larger the parameter, the higher the accuracy and the higher the complexity. The accuracy is (1-1/(val*2)) 
        a = new BigInteger("1200324143214321442127");
        out.println("a:" + a.toString());
        out.println(a.isProbablePrime(10) ? "a is prime" : "a is not prime");  // a is not prime 
    }
    
    static void nextPrime() {  // find the next prime of the number 
        a = new BigInteger("1200324143214321442127");
        out.println("a:" + a.toString());
        out.println(String.format("a nextPrime is %s", a.nextProbablePrime().toString()));  // a nextPrime is 1200324143214321442199 
    }
    
    static void modPow() {  // fast exponentiation, faster than the normal version, with mathematical optimization inside 
        a = new BigInteger("2");
        b = new BigInteger("10");
        p = new BigInteger("1000");
        out.println(String.format("a:%s b:%s p:%s", a, b, p));
        out.println(String.format("a^b mod p:%s", a.modPow(b, p).toString()));//  24 
    }
    
    static void modInverse() {  // inverse element 
        a = new BigInteger("10");
        b = new BigInteger("3");
        out.println(a.modInverse(b));  // a ^ (p-2) mod p = 1 
    }
    
    public static void main(String[] args) {
        gcd();
        isPrime();
        nextPrime();
        modPow();
        modInverse();
        out.close();
    }
}
```

For knowledge related to Miller-Rabin, you can consult [Miller–Rabin primality test](../math/number-theory/prime.md#millerrabin-素性测试).

## Basic data types and wrapper data types

### Introduction

Since basic types do not have object-oriented characteristics, in order for them to participate in object-oriented development, Java provides corresponding wrapper classes for the eight basic types, namely `Byte`, `Double`, `Float`, `Integer`, `Long`, `Short`, `Character`, and `Boolean`. The correspondence between the two is as follows:

| Basic data type | Wrapper data type |
| :-------: | :---------: |
| `byte` | `Byte` |
| `short` | `Short` |
| `boolean` | `Boolean` |
| `char` | `Character` |
| `int` | `Integer` |
| `long` | `Long` |
| `float` | `Float` |
| `double` | `Double` |

### Differences

Here we take `int` and `Integer` as an example:

1.  `Integer` is the wrapper class of `int`, while `int` is a basic type of data in Java.
2.  `Integer` type can only be used after being instantiated, while `int` type does not need to be.
3.  `Integer` actually corresponds to a reference; when you `new` an `Integer`, an object is actually generated, while `int` directly stores data.
4.  The default value of `Integer` is `null`, and it can accept `null` and `int` type data; the default value of `int` is 0, and it cannot accept `null` type data.
5.  For `Integer`, using `==` to determine whether two variables are the same may lead to incorrect results; you can only use `equals()`, while `int` can directly use `==`.

### Boxing and unboxing

Here we take `int` and `Integer` as an example:

The essence of `Integer` is an object, and `int` is a basic type; the two types cannot be directly assigned to each other. When conversion is needed, we should convert the basic type to the wrapper type; this practice is called boxing, and the reverse is called unboxing.

```java
// basic type
int value1 = 1;
// boxing to convert to wrapper type
Integer integer = Integer.valueOf(value1);
// unboxing to convert to basic type
int value2 = integer.intValue();
```

Java 5 introduced the automatic boxing/unboxing mechanism:

```java
Integer integer = 1;
int value = integer;
```

???+ warning "Note"
    Although the JDK adds the automatic boxing/unboxing mechanism, please choose the appropriate type when declaring variables, because the wrapper type `Integer` can accept `null`, while the basic type `int` cannot accept `null`. Therefore, when performing an unboxing operation on a wrapper type with a `null` value, an exception will be thrown. The following code demonstrates this behavior.
    
    ```java
    Integer integer = Integer.valueOf(null);
    integer.intValue();  // throws a java.lang.NumberFormatException exception
    
    Integer integer = null;
    integer.intValue();  // throws a java.lang.NullPointerException exception
    ```

## Inheritance

Creating new designs based on existing designs is inheritance in object-oriented programming. In inheritance, a new class is not produced out of thin air, but defined based on an already-existing class. Through inheritance, the new class automatically obtains all the members in the base class, including member variables and methods, including members with various access attributes, whether `public` or `private`. Obviously, defining a new class through inheritance is far simpler, quicker, and more convenient than writing a new class from scratch. Inheritance is one of the important means to support code reuse.

In Java, the keyword for inheritance is `extends`, and Java only supports single inheritance, but can implement multiple interfaces.

In Java, all classes are subclasses of the `Object` class.

When a subclass inherits from a parent class, all the members of the parent class, including variables and methods, become members of the subclass, except constructors. Constructors are unique to the parent class, because their names are the names of the class, so the parent class's constructors do not exist in the subclass. Except for this, the subclass inherits all the members of the parent class.

Each member has different access attributes; the subclass inherits all the members of the parent class, but the different access attributes make the subclass differ when using these members: some parent-class members directly become the subclass's external interface, while some are deeply hidden, and even the subclass itself cannot directly access them.

The following table lists the access attributes in the subclass of parent-class members with different access attributes:

| Parent-class member access attribute | Meaning in the parent class | Meaning in the subclass |
| :-----------: | :---------------: | :--------------------------------------------: |
| `public` | Open to all classes | Open to all classes |
| `protected` | Only other classes in the package, itself, and subclasses can access | Only other classes in the package, itself, and subclasses can access |
| default (`default`) | Only other classes in the package can access | If the subclass and parent class are in the same package, only other classes in the package can access; otherwise equivalent to `private`, cannot access |
| `private` | Only itself can access | Cannot access |

## Polymorphism

In Java, when assigning an object to a variable, the type of the object must match the type of the variable. But since Java has the concept of inheritance, it can be redefined as **a variable can hold its declared type or any subtype of that type**.

If a type implements an interface, it can also be called a subtype of that interface.

Variables that hold object types in Java are polymorphic variables. The term "polymorphism" (literally meaning many forms) refers to a variable being able to hold objects of different types (i.e. its declared type or any subtype).

Polymorphic variables:

1.  Java's object variables are polymorphic; they can hold more than one type of object.
2.  What they can hold is an object of the declared type, or an object of a subclass of the declared type.
3.  When assigning an object of a subclass to a variable of the parent class, upcasting occurs.

## Generics

Generics refer to not setting the specific type of the attributes or method parameters in a class when defining the class, but defining the type when using it (or creating an object). The essence of generics is parameterized types, i.e. the operated data type is specified as a parameter.

Generics provide a mechanism for compile-time type safety detection, which allows detecting illegal types at compile time.

## Interfaces

### Introduction

An interface (Interface) in Java is an abstract type, a collection of abstract methods, usually declared with `interface`. A class inherits the abstract methods of an interface by implementing the interface.

An interface is not a class; the way to write an interface is very similar to a class, but they belong to different concepts. A class describes the attributes and methods of an object. An interface contains the methods that a class is to implement.

Unless the class implementing the interface is an abstract class, this class must define all the methods in the interface.

An interface cannot be instantiated, but can be implemented. A class that implements an interface must implement all the methods described in the interface, otherwise it must be declared as an abstract class. In addition, in Java, an interface type can be used to declare a variable; they can become a null pointer, or be bound to an object implemented by this interface.

### Differences from classes

1.  An interface cannot be used to instantiate objects.
2.  An interface has no constructors.
3.  All methods in an interface must be abstract methods; after Java 8, non-abstract methods modified by the `default` keyword can be used in interfaces.
4.  An interface cannot contain member variables, except static and final variables.
5.  An interface is not inherited by a class, but is to be implemented by a class.
6.  Interfaces support multiple inheritance; classes do not support multiple inheritance.

### Declaration

```java
[visibility] interface interfaceName [extends otherInterfaceName] {
        // declare variables
        // abstract methods
}
```

### Implementation

```java
...implements interfaceName[, otherInterfaceName, otherInterfaceName..., ...] ...
```

## Lambda expressions

### Introduction

Lambda expressions can also be called closures; they are the most important new feature of Java 8.

Lambda expressions allow passing a function as a parameter of a method (a function is passed into a method as a parameter).

Using lambda expressions can make code more concise and compact.

### Syntax

-   Optional type declaration: there is no need to declare the parameter type; the compiler can uniformly recognize the parameter value.
-   Optional parameter parentheses: a single parameter does not need to define parentheses, but multiple parameters need to define parentheses.
-   Optional braces: if the body contains one statement, then braces do not need to be used.
-   Optional return keyword: if the body has only one expression return value, then the compiler will automatically return the value; braces need to specify that the expression returned a value.

Lambda expressions are declared as follows:

```java
// 1. no parameters needed, return value is 5
() -> 5

// 2. receive one parameter (numeric type), return twice its value
x -> 2 * x

// 3. accept 2 parameters (numbers) and return their difference
(x, y) -> x – y

// 4. receive 2 int-type integers and return their sum
(int x, int y) -> x + y

// 5. accept a String object and print it to the console, returning nothing (looks like returning void)
(String s) -> System.out.print(s)
```

Taking a custom comparator that sorts a string array by length as an example, a lambda expression can be applied in the following form.

```java
import java.util.Arrays;

public class Main {
    static PrintWriter out = new PrintWriter(System.out);
    
    public static void main(String[] args) {
        String[] plants = {"Mercury", "venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"};
        Arrays.sort(plants, (String first, String second) -> (first.length() - second.length()));
        for (String word : plants) {
            out.print(word + " ");
        }
        out.close();
    }
}
```

We can also use multiple statements in a lambda expression, like the following example.

```java
import java.io.PrintWriter;
import java.util.Arrays;

public class Main {
    static PrintWriter out = new PrintWriter(System.out);
    
    public static void main(String[] args) {
        String[] plants = {"Mercury", "venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"};
        Arrays.sort(plants, (first, second) ->
        {
            // the formal parameter types are not written; they can be judged from the context
            int result = first.length() - second.length();
            return result;
        });
        for (String word : plants) {
            out.print(word + " ");
        }
        out.close();
    }
}
```

Here, `->` is a derivation symbol, indicating that the parentheses in front receive the parameters, and derive the return value that follows (essentially it passes the method).

### Functional interfaces

1.  It is an interface, conforming to the Java interface definition.
2.  An interface containing only one abstract method.
3.  Because there is only one unimplemented method, a lambda expression can automatically fill it in.

Functional interfaces are used as follows:

???+ example "Output strings whose length is a multiple of 2"
    ```java
    import java.io.PrintWriter;
    
    public class Main {
        static PrintWriter out = new PrintWriter(System.out);
        
        public static void main(String[] args) {
            String[] plants = {"Mercury", "venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"};
            Test test = s -> {  // lambda expression as an instance of the functional interface
                if (s.length() % 2 == 0) {
                    return true;
                }
                return false;
            };
            for (String word : plants) {
                if (test.check(word)) {
                    out.print(word + " ");
                }
            }
            out.close();
        }
    }
    
    interface Test {
        public boolean check(String s);
    }
    ```

???+ example "Implement the four arithmetic operations of addition, subtraction, multiplication, and division"
    ```java
    import java.io.PrintWriter;
    
    public class Main {
        static PrintWriter out = new PrintWriter(System.out);
        
        public static double calc(double a, double b, Calculator util) {
            return util.operation(a, b);
        }
        
        public static void main(String[] args) {
            Calculator util[] = new Calculator[4];  // define a functional interface array
            util[0] = (a, b) -> a + b;
            util[1] = (a, b) -> a - b;
            util[2] = (a, b) -> a * b;
            util[3] = (a, b) -> a / b;
            double a = 20, b = 15;
            for (Calculator c : util) {
                System.out.println(calc(a, b, c));
            }
            out.close();
        }
    }
    
    interface Calculator {
        public double operation(double a, double b);
    }
    ```

## Collection

`Collection` is an interface in Java, implemented by multiple generic container interfaces. Here, `Collection` refers to a data structure that stores object types.

The `Collection` element type in Java must be an object when defined; it cannot be a basic data type.

The usages of the following content are all based on the property of polymorphism in Java, and all appear in the form of implementing interfaces.

The commonly used interfaces include `List`, `Queue`, `Set`, and `Map`.

### Container definition

When defining a generic container class, we need to specify the data type at the time of definition. If the data type is not specified, and it is treated as `Object` type to add data arbitrarily, although it can compile in Java 8, there will be many warning risks.

For example, the following definition is safe; the container only accepts `Integer` type.

```java
List<Integer> list1 = new LinkedList<>();
```

And the following definition will produce warnings.

```java
List list = new ArrayList<>();
list.add(1);
list.add(true);
list.add(1.01);
list.add(1L);
list.add("I am String");
```

Therefore, unless there are special needs, the second behavior is not recommended; the compiler cannot help check whether the stored data is safe. When getting a value with `list.get(index)`, the type of the data cannot be made clear (the data type obtained is all `Object`), and it needs to be manually cast back to the original type; a slight carelessness may result in a mis-cast exception.

If the type is clarified, such as `List<Integer>`, at this time the compiler will check the type of the stored data, and only integer data can be stored. When declaring a collection variable, you can only use the wrapper type `List<Integer>` or a custom `Class`, and not a basic type such as `List<int>`.

### List

#### ArrayList

`ArrayList` is an array that supports dynamic growth according to demand; the initial length is 10 by default. If the current length is exceeded, it expands by $\dfrac{3}{2}$.

##### Initialization

```java
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;

public class Main {
    static PrintWriter out = new PrintWriter(System.out);
    
    public static void main(String[] args) {
        List<Integer> list1 = new ArrayList<>();  // create a self-growing array named list1, with initial length being the default value (10)
        List<Integer> list2 = new ArrayList<>(30);  // create a self-growing array named list2, with initial length 30
        List<Integer> list3 = new ArrayList<>(list2);  // create a self-growing array named list3, using the elements and size in list2 as its own initial values
    }
}
```

#### LinkedList

`LinkedList` is a doubly linked list.

##### Initialization

```java
import java.io.PrintWriter;
import java.util.LinkedList;
import java.util.List;

public class Main {
    static PrintWriter out = new PrintWriter(System.out);
    
    public static void main(String[] args) {
        List<Integer> list1 = new LinkedList<>();  // create a doubly linked list named list1 
        List<Integer> list2 = new LinkedList<>(list1);  // create a doubly linked list named list2, adding all elements in list1 
    }
}
```

#### Common methods

Below, `this` is used to represent the current `List<Integer>`:

| Function name | Function |
| :-----------------------: | :------------------------------: |
| `size()` | Return the length of `this` |
| `add(Integer val)` | Insert the element `val` at the end of `this` |
| `add(int idx, Integer e)` | Insert the element `e` at position `idx` of `this` |
| `get(int idx)` | Return the value at position `idx` in `this`; throw an exception if out of bounds |
| `set(int idx, Integer e)` | Modify the value at position `idx` in `this` to `e` |

Usage example and difference comparison:

```java
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

public class Main {
    static PrintWriter out = new PrintWriter(System.out);
    static List<Integer> array = new ArrayList<>();
    static List<Integer> linked = new LinkedList<>();
    
    static void add() {
        array.add(1);  // time complexity is O(1) 
        linked.add(1);  // time complexity is O(1) 
    }
    
    static void get() {
        array.get(10);  // time complexity is O(1) 
        linked.get(10);  // time complexity is O(11) 
    }
    
    static void addIdx() {
        array.add(0, 2);  // worst-case time complexity is O(n)
        linked.add(0, 2);  // worst-case time complexity is O(n)
    }
    
    static void size() {
        array.size();  // time complexity is O(1)
        linked.size();  // time complexity is O(1)
    }
    
    static void set() {  // this method returns the value of the element originally at that position
        array.set(0, 1);  // time complexity is O(1)
        linked.set(0, 1);  // worst-case time complexity is O(n)
    }

}
```

#### Traversal

```java
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.List;

public class Main {
    static PrintWriter out = new PrintWriter(System.out);
    static List<Integer> array = new ArrayList<>();
    static List<Integer> linked = new LinkedList<>();
    
    static void function1() {  // naive traversal
        for (int i = 0; i < array.size(); i++) {
            out.println(array.get(i));  // traverse the self-growing array, complexity is O(n)
        }
        for (int i = 0; i < linked.size(); i++) {
            out.println(linked.get(i));  // traverse the doubly linked list, complexity is O(n^2), because the get(i) complexity of LinkedList is O(i)
        }
    }
    
    static void function2() {  // enhanced for loop traversal 
        for (int e : array) {
            out.println(e);
        }
        for (int e : linked) {
            out.println(e);  // complexity is both O(n) 
        }
    }
    
    static void function3() {  // iterator traversal 
        Iterator<Integer> iterator1 = array.iterator();
        Iterator<Integer> iterator2 = linked.iterator();
        while (iterator1.hasNext()) {
            out.println(iterator1.next());
        }
        while (iterator2.hasNext()) {
            out.println(iterator2.next());
        }  // complexity is both O(n) 
    }

}
```

???+ warning "Note"
    Do not delete elements from a `List` during a `for` or `foreach` traversal, otherwise an exception will be thrown.
    
    The reason is also very simple: `list.size()` changes, but the number of times already looped in the loop does not change accordingly. The data originally expected at the next `index` becomes the data at the current `index` due to the delete operation; when the next loop runs, the operation will become the data originally expected at the index after next, and eventually will cause the operated data to not meet expectations.

### Queue

#### LinkedList

We can use `LinkedList` to implement an ordinary queue; the underlying layer is a linked list simulating a queue.

##### Initialization

```java
Queue<Integer> q = new LinkedList<>();
```

`LinkedList` implements the `List` interface and the `Deque` interface at the underlying layer, and the `Deque` interface inherits from the `Queue` interface, so `LinkedList` can implement both `List` and `Queue`.

#### ArrayDeque

We can use `ArrayDeque` to implement an ordinary queue; the underlying layer is an array simulating a queue.

##### Initialization

```java
Queue<Integer> q = new ArrayDeque<>();
```

`ArrayDeque` implements the `Deque` interface at the underlying layer, and the `Deque` interface inherits from the `Queue` interface, so `ArrayDeque` can implement `Queue`.

#### Differences between LinkedList and ArrayDeque in implementing the Queue interface

1.  Data structure: in terms of data structure, both `ArrayDeque` and `LinkedList` implement the Java Deque double-ended queue interface. But `ArrayDeque` does not implement the Java List interface, so it does not have the behavior of operating according to index position.
2.  Thread safety: neither `ArrayDeque` nor `LinkedList` considers thread synchronization, and neither guarantees thread safety.
3.  Underlying implementation: in terms of underlying implementation, `ArrayDeque` is based on a dynamic array, while `LinkedList` is based on a doubly linked list.
4.  In terms of traversal speed: `ArrayDeque` is a contiguous memory space, and based on the locality principle can better hit CPU cache lines, while `LinkedList` is a discrete memory space that is unfriendly to cache lines.
5.  In terms of operation speed: the stack and queue behaviors of both `ArrayDeque` and `LinkedList` are $O(1)$ time complexity; the push and enqueue of `ArrayDeque` may trigger expansion, but from an amortized analysis it is still $O(1)$ time complexity.
6.  In terms of extra memory consumption: `ArrayDeque` has idle space outside the head pointer and tail pointer of the array, while `LinkedList` adds predecessor and successor pointers on the nodes.

#### PriorityQueue

`PriorityQueue` is a priority queue, by default a min-heap.

##### Initialization

```java
Queue<Integer> q1 = new PriorityQueue<>();  // min-heap
Queue<Integer> q2 = new PriorityQueue<>((x, y) -> {return y - x;});  // max-heap
```

#### Common methods

In the table below, the queue is defined as `Queue<Integer>`.

| Function name | Function |
| :------------------: | :----------------------------------------: |
| `size()` | Return the current queue length |
| `add(Integer val)` | Insert `val` into the queue; if the capacity limit of the queue is violated during insertion, an exception will be thrown |
| `offer(Integer val)` | Insert `val` into the queue; if the capacity limit of the queue is violated during insertion, the insertion fails, but no exception is thrown |
| `isEmpty()` | Determine whether the queue is empty; return `true` if empty |
| `peek()` | Return the queue-front element; return `null` if the queue is empty |
| `poll()` | Return and delete the queue-front element; return `null` if the queue is empty |

Usage example and difference comparison:

```java
import java.io.PrintWriter;
import java.util.LinkedList;
import java.util.PriorityQueue;
import java.util.Queue;

public class Main {
    static PrintWriter out = new PrintWriter(System.out);
    static Queue<Integer> q1 = new LinkedList<>();
    static Queue<Integer> q2 = new PriorityQueue<>();
    
    static void add() {  // add and offer have no difference in functionality; the difference is whether an exception is thrown 
        q1.add(1);  // time complexity is O(1) 
        q2.add(1);  // time complexity is O(logn) 
    }
    
    static void isEmpty() {
        q1.isEmpty();  // time complexity is O(1) 
        q2.isEmpty();  // space complexity is O(1) 
    }
    
    static void size() {
        q1.size();  // time complexity is O(1) 
        q2.size();  // return the length of q2 
    }
    
    static void peek() {
        q1.peek();  // time complexity is O(1) 
        q2.peek();  // time complexity is O(logn) 
    }
    
    static void poll() {
        q1.poll();  // time complexity is O(1) 
        q2.poll();  // time complexity is O(logn) 
    }
}
```

#### Traversal

```java
import java.io.PrintWriter;
import java.util.LinkedList;
import java.util.PriorityQueue;
import java.util.Queue;

public class Main {
    static PrintWriter out = new PrintWriter(System.out);
    static Queue<Integer> q1 = new LinkedList<>();
    static Queue<Integer> q2 = new PriorityQueue<>();
    
    static void test() {
        while (!q1.isEmpty()) {  // complexity is O(n) 
            out.println(q1.poll());
        }
        while (!q2.isEmpty()) {  // complexity is O(nlogn) 
            out.println(q2.poll());
        }
    }

}
```

### Deque

`Deque` is the double-ended queue in `Java`; we usually use it for queue operations and stack operations.

#### Main functions

In the table below, the queue is defined as `Deque<Integer>`.

| Function name | Function |
| :-----------------------: | :----------------------------------------: |
| `addFirst(Integer val)` | Insert `val` at the queue head; if the capacity limit of the queue is violated during insertion, an exception will be thrown |
| `offerFirst(Integer val)` | Insert `val` at the queue head; if the capacity limit of the queue is violated during insertion, the insertion fails, but no exception is thrown |
| `removeFirst()` | Return and delete the queue-head element; if the queue is empty, an exception will be thrown |
| `pollFirst()` | Return and delete the queue-head element; if the queue is empty, return `null` |
| `peekFirst()` | Return the queue-head element; if the queue is empty, return `null` |
| `push(Integer val)` | Insert `val` at the queue head, equivalent to `addFirst` |
| `pop()` | Return and delete the queue-head element, equivalent to `removeFirst` |
| `remove()` | Delete the queue-head element, equivalent to `removeFirst` |
| `poll()` | Delete the queue-head element, equivalent to `pollFirst` |
| `addLast(Integer val)` | Insert `val` at the queue tail; if the capacity limit of the queue is violated during insertion, an exception will be thrown |
| `offerLast(Integer val)` | Insert `val` at the queue tail; if the capacity limit of the queue is violated during insertion, the insertion fails, but no exception is thrown |
| `removeLast()` | Return and delete the queue-tail element; if the queue is empty, an exception will be thrown |
| `pollLast()` | Return and delete the queue-tail element; if the queue is empty, return `null` |
| `peekLast()` | Return the queue-tail element; if the queue is empty, return `null` |
| `add(Integer val)` | Insert `val` at the queue tail, equivalent to `addLast` |
| `offer(Integer val)` | Insert `val` at the queue tail, equivalent to `offerLast` |

#### Stack operations

```java
import java.util.ArrayDeque;
import java.util.Deque;

public class Main {
    static Deque<Integer> stack = new ArrayDeque<>();
    static int[] a = {1, 2, 3, 4, 5};
    
    public static void main(String[] args) {
        for (int v : a) {
            stack.push(v);
        }
        while (!stack.isEmpty()) { // output 5 4 3 2 1
            System.out.println(stack.pop()); 
        }
    }
}

```

#### Double-ended queue operations

```java
import java.util.ArrayDeque;
import java.util.Deque;

public class Main {
    static Deque<Integer> deque = new ArrayDeque<>();
    
    static void insert() {
        deque.addFirst(1);
        deque.addFirst(2);
        deque.addLast(3);
        deque.addLast(4);
    }
    
    public static void main(String[] args) {
        insert();
        while (!deque.isEmpty()) { // output 2 1 3 4
            System.out.println(deque.poll());
        }
        insert();
        while (!deque.isEmpty()) { // output 4 3 1 2
            System.out.println(deque.pollLast());
        }
    }
}
```

### Set

`Set` is a data structure that keeps the elements in the container non-repeating.

#### HashSet

A `Set` with random-position insertion.

##### Initialization

```java
Set<Integer> s1 = new HashSet<>();
```

#### LinkedHashSet

A `Set` that maintains insertion order.

##### Initialization

```java
Set<Integer> s2 = new LinkedHashSet<>();
```

#### TreeSet

A `Set` that keeps the elements in the container ordered, ascending by default.

##### Initialization

```java
Set<Integer> s3 = new TreeSet<>();
Set<Integer> s4 = new TreeSet<>((x, y) -> {return y - x;});  // descending 
```

##### More uses of TreeSet

These methods are newly created and implemented by `TreeSet`; we cannot use the `Set` interface to call the following methods, so we create it as follows:

```java
TreeSet<Integer> s3 = new TreeSet<>();
TreeSet<Integer> s4 = new TreeSet<>((x, y) -> {return y - x;});  // descending 
```

In the table below, `this` is used to represent the current `TreeSet<Integer>`.

| Function name | Function |
| :--------------------: | :--------------------------------------: |
| `first()` | Return the first element in `this`; return `null` if none |
| `last()` | Return the last element in `this`; return `null` if none |
| `floor(Integer val)` | Return the first element in `this` less than or equal to `val`; return `null` if none |
| `ceiling(Integer val)` | Return the first element in `this` greater than or equal to `val`; return `null` if none |
| `higher(Integer val)` | Return the first element in `this` greater than `val`; return `null` if none |
| `lower(Integer val)` | Return the first element in `this` less than `val`; return `null` if none |
| `pollFirst()` | Return and delete the first element in `this`; return `null` if none |
| `pollLast()` | Return and delete the last element in `this`; return `null` if none |

Code example:

```java
import java.util.TreeSet;

public class Main {
    static int[] a = {4,7,1,2,3,6};
    
    public static void main(String[] args) {
        TreeSet<Integer> set = new TreeSet<>();
        for(int v:a) {
            set.add(v);
        }
        Integer a2 = set.first();
        System.out.println(a2); // return 1
        Integer a3 = set.last();
        System.out.println(a3); // return 7
        Integer a4 = set.floor(5);
        System.out.println(a4); // return 4
        Integer a5 = set.ceiling(6);
        System.out.println(a5); // return 6
        Integer a6 = set.higher(7);
        System.out.println(a6); // return null
        Integer a7 = set.lower(2);
        System.out.println(a7); // return 1
        Integer a8 = set.pollFirst();
        System.out.println(a8); // return 1
        Integer a9 = set.pollLast();
        System.out.println(a9); // return 7
    }
}
```

#### Common methods of Set

| Function name | Function |
| :-----------------------: | :------------------------------------: |
| `size()` | Return the size of the current set |
| `add(Integer val)` | Insert `val` into the set |
| `contains(Integer val)` | Determine whether the set has the element `val` |
| `addAll(Collection e)` | Add all elements in the container `e` into the current set |
| `retainAll(Collection e)` | Delete the elements in the current set that do not appear in the container `e`, i.e. find the intersection of the current set and `e` |
| `removeAll(Collection e)` | Delete the elements in the current set that appear in the container `e`, i.e. find the difference of the current set and `e` |

```java
import java.io.PrintWriter;
import java.util.HashSet;
import java.util.LinkedHashSet;
import java.util.Set;

public class Main {
    static PrintWriter out = new PrintWriter(System.out);
    static Set<Integer> s1 = new HashSet<>();
    static Set<Integer> s2 = new LinkedHashSet<>();
    
    static void add() {
        s1.add(1);
    }
    
    static void contains() {  // determine whether the set has an element with value 2; return true if yes, otherwise false 
        s1.contains(2);
    }
    
    static void test1() {  // the union of s1 and s2 
        Set<Integer> res = new HashSet<>();
        res.addAll(s1);
        res.addAll(s2);
    }
    
    static void test2() {  // the intersection of s1 and s2 
        Set<Integer> res = new HashSet<>();
        res.addAll(s1);
        res.retainAll(s2);
    }
    
    static void test3() {  // difference: s1 - s2 
        Set<Integer> res = new HashSet<>();
        res.addAll(s1);
        res.removeAll(s2);
    }
}
```

#### Traversal

```java
import java.io.PrintWriter;
import java.util.HashSet;
import java.util.LinkedHashSet;
import java.util.Set;

public class Main {
    static PrintWriter out = new PrintWriter(System.out);
    static Set<Integer> s1 = new HashSet<>();
    static Set<Integer> s2 = new LinkedHashSet<>();
    
    static void test() {
        for (int key : s1) {
            out.println(key);
        }
        out.close();
    }
}
```

### Map

`Map` is a data structure that maintains key-value pairs `<Key, Value>`, where `Key` is unique.

#### HashMap

A `Map` with random-position insertion.

##### Initialization

```java
Map<Integer, Integer> map1 = new HashMap<>();
```

#### LinkedHashMap

A `Map` that maintains insertion order.

##### Initialization

```java
Map<Integer, Integer> map2 = new LinkedHashMap<>();
```

#### TreeMap

A `Map` that keeps `key` ordered, ascending by default.

##### Initialization

```java
Map<Integer, Integer> map3 = new TreeMap<>();
Map<Integer, Integer> map4 = new TreeMap<>((x, y) -> {return y - x;});  // descending
```

#### Common methods

Below, `this` is used to represent the current `Map<Integer, Integer>`:

| Function name | Function |
| :-------------------------------: | :---------------------------: |
| `put(Integer key, Integer value)` | Insert `<key, value>` into `this` |
| `size()` | Return the size of `this` |
| `containsKey(Integer key)` | Determine whether there is an element in `this` whose key is `key` |
| `get(Integer key)` | Return the value corresponding to the element in `this` whose key is `key` |
| `keySet()` | Return the keys of all elements in `this` as a set |

Usage example:

```java
import java.io.PrintWriter;
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.TreeMap;

public class Main {
    static PrintWriter out = new PrintWriter(System.out);
    
    static Map<Integer, Integer> map1 = new HashMap<>();
    static Map<Integer, Integer> map2 = new LinkedHashMap<>();
    static Map<Integer, Integer> map3 = new TreeMap<>();
    static Map<Integer, Integer> map4 = new TreeMap<>((x,y)->{return y-x;});
    
    static void put(){  // insert an element with key 1 and value 1
        map1.put(1, 1);
    }
    static void get(){  // return the value with key 1
        map1.get(1);
    }
    static void containsKey(){  // determine whether there is a key-value pair with key 1
        map1.containsKey(1);
    }
    static void KeySet(){
        map1.keySet();
    }
}
```

#### Traversal

```java
import java.io.PrintWriter;
import java.util.HashMap;
import java.util.Map;

public class Main {
    static PrintWriter out = new PrintWriter(System.out);
    
    static Map<Integer, Integer> map1 = new HashMap<>();
    
    static void print() {
        for (int key : map1.keySet()) {
            out.println(key + " " + map1.get(key));
        }
    }
}
```

Of course, the types of the keys and values can also be changed. For example, `Map` can also be defined as:

```java
Map<String, Set<Integer>> map = new HashMap<>();
```

## Arrays

`Arrays` is a utility class in `java.util` for operating on arrays. The methods are all static methods, which can be called directly using the class name.

### Arrays.sort()

`Arrays.sort()` is a method for sorting an array; the main overloaded methods are as follows:

```java
import java.util.Arrays;
import java.util.Comparator;

public class Main {
    static int[] a = new int[10];
    static Integer[] b = new Integer[10];
    static int firstIdx, lastIdx;
    
    public static void main(String[] args) {
        Arrays.sort(a);  // 1 
        Arrays.sort(a, firstIdx, lastIdx);  // 2 
        Arrays.sort(b, new Comparator<Integer>() {  // 3 
            @Override
            public int compare(Integer o1, Integer o2) {
                return o2 - o1;
            }
        });
        Arrays.sort(b, firstIdx, lastIdx, new Comparator<Integer>() {  // 4 
            @Override
            public int compare(Integer o1, Integer o2) {
                return o2 - o1;
            }
        });
        // since there are Lambda expressions after Java 8, the third and fourth overloads can also be written as 
        Arrays.sort(b, (x, y) -> {  // 5 
            return y - x;
        });
        Arrays.sort(b, (x, y) -> {  // 6 
            return y - x;
        });
    }
}
```

The meanings of the overloaded methods corresponding to the numbers:

1.  Sort the array `a`, ascending by default.
2.  Sort the specified positions of the array `a`, ascending by default; the sorting interval is left-closed right-open `[firstIdx, lastIdx)`.
3.  Sort the array `a` in a custom form; second parameter `-` first parameter for descending, first parameter `-` second parameter for ascending; when customizing the sorting comparator, the array element type must be an object type.
4.  Sort the specified positions of the array `a` in a custom way; the sorting interval is left-closed right-open `[firstIdx, lastIdx)`; when customizing the sorting comparator, the array element type must be an object type.
5.  Same as 3, using a Lambda expression to optimize the code length.
6.  Same as 4, using a Lambda expression to optimize the code length.

???+ note "The underlying function of `Arrays.sort()`"
    1.  When the element type of the parameter array of `Arrays.sort` is a basic data type (`byte`, `short`, `char`, `int`, `long`, `double`, `float`), it defaults to `DualPivotQuicksort` (dual-pivot quicksort), whose worst-case complexity can reach $O(n^2)$.
    2.  When the element type of the parameter array of `Arrays.sort` is a non-basic data type, it defaults to `legacyMergeSort` and `TimSort` (merge sort), with complexity $O(n\log n)$.

We can verify with the following code:

???+ example "[Codeforces 1646B - Quality vs Quantity](https://codeforces.com/problemset/problem/1646/B)"
    There are $n$ integers; you need to divide them into two groups; can there exist a group whose length is less than the other group while its sum is greater than it.

??? note "Example problem code"
    ```java
    import java.io.BufferedReader;
    import java.io.IOException;
    import java.io.InputStreamReader;
    import java.io.PrintWriter;
    import java.util.Arrays;
    import java.util.StringTokenizer;
    
    public class Main {
        static class FastReader {
            StringTokenizer st;
            BufferedReader br;
            
            public FastReader() {
                br = new BufferedReader(new InputStreamReader(System.in));
            }
            
            String next() {
                while (st == null || !st.hasMoreElements()) {
                    try {
                        st = new StringTokenizer(br.readLine());
                    } catch (IOException e) {
                        e.printStackTrace();
                    }
                }
                return st.nextToken();
            }
            
            int nextInt() {
                return Integer.parseInt(next());
            }
            
            long nextLong() {
                return Long.parseLong(next());
            }
            
            double nextDouble() {
                return Double.parseDouble(next());
            }
            
            String nextLine() {
                String str = "";
                try {
                    str = br.readLine();
                } catch (IOException e) {
                    e.printStackTrace();
                }
                return str;
            }
        }
        
        static PrintWriter out = new PrintWriter(System.out);
        static FastReader in = new FastReader();
        
        static void solve() {
            int n = in.nextInt();
            // changing the array type here from Integer to int will cause TLE
            Integer[] a = new Integer[n + 10];
            for (int i = 1; i <= n; i++) {
                a[i] = in.nextInt();
            }
            Arrays.sort(a, 1, n + 1);
            long left = a[1];
            long right = 0;
            int x = n;
            for (int i = 2; i < x; i++, x--) {
                left = left + a[i];
                right = right + a[x];
                if (right > left) {
                    out.println("YES");
                    return;
                }
            }
            out.println("NO");
        }
        
        public static void main(String[] args) {
            int t = in.nextInt();
            while (t-- > 0) {
                solve();
            }
            out.close();
        }
    }
    ```

### Arrays.binarySearch()

`Arrays.binarySearch()` is a method for performing binary search on a contiguous interval of an array; the premise is that the array must be ordered, and the time complexity is $O(\log_n)$; the main overloaded methods are as follows:

```java
import java.util.Arrays;

public class Main {
    static int[] a = new int[10];
    static Integer[] b = new Integer[10];
    static int firstIdx, lastIdx;
    static int key;
    
    public static void main(String[] args) {
        Arrays.binarySearch(a, key);  // 1 
        Arrays.binarySearch(a, firstIdx, lastIdx, key);  // 2 
    }
}
```

The source code is as follows:

```java
private static int binarySearch0(int[] a, int fromIndex, int toIndex, int key) {
    int low = fromIndex;
    int high = toIndex - 1;
    
    while (low <= high) {
        int mid = (low + high) >>> 1;
        int midVal = a[mid];
        
        if (midVal < key)
            low = mid + 1;
        else if (midVal > key)
            high = mid - 1;
        else
            return mid; // key found
    }
    return -(low + 1);  // key not found.
}
```

The meanings of the overloaded methods corresponding to the numbers:

1.  Binary-search whether `key` exists in the array a; if it exists, return its subscript. If it does not exist, return a negative number.
2.  Binary-search whether `key` exists in the array a; if it exists, return its subscript; the search interval is left-closed right-open `[firstIdx,lastIdx)`. If it does not exist, return a negative number.

### Arrays.fill()

The `Arrays.fill()` method assigns the elements at contiguous positions in an array to a uniform element. The parameters it accepts are the array, `fromIndex`, `toIndex`, and the number to fill. After the method executes, the values of all elements in the left-closed right-open interval `[firstIdx,lastIdx)` of the array are the number to fill.

## Collections

`Collections` is a utility class in `java.util` for operating on collections. The methods are all static methods, which can be called directly using the class name.

### Collections.sort()

The underlying principle of `Collections.sort()` is to convert all elements in it into an array and call `Arrays.sort()`, and after completing the sort, assign it back to the original collection. And because the element type of `Collection` in Java is all object type, it is always merge sort that handles it.

This method cannot sort a specified interval of the collection.

Underlying source code:

```java
default void sort(Comparator<? super E> c) {
    Object[] a = this.toArray();
    Arrays.sort(a, (Comparator) c);
    ListIterator<E> i = this.listIterator();
    for (Object e : a) {
        i.next();
        i.set((E) e);
    }
}
```

### Collections.binarySearch()

`Collections.binarySearch()` performs binary search on a specified interval of a collection; the functionality is the same as `Arrays.binarySearch()`.

```java
Collections.binarySearch(list, key);
```

This method cannot search a specified interval.

### Collections.swap()

The functionality of `Collections.swap()` is to swap the elements at two specified positions in a collection.

```java
 Collections.swap(list, i, j);
```

## Others

### Numerical comparison problem

In Java, if it is purely a numeric type, `-0.0 = 0.0`. If it is an object type, then `-0.0 != 0.0`. If you try to use a `Set` to count the number of slopes, this problem will cause trouble. The provided solution is to add `0.0` to all slope values before adding them to the `Set`.

```java
import java.io.PrintWriter;

public class Main {
    static PrintWriter out = new PrintWriter(System.out);
    
    static void A() {
        Double a = 0.0;
        Double b = -0.0;
        out.println(a.equals(b));  // false 
    }
    
    static void B() {
        Double a = 0.0;
        Double b = -0.0 + 0.0;
        out.println(a.equals(b));  // true 
    }
    
    static void C() {
        double a = 0.0;
        double b = -0.0;
        out.println(a == b);  // true 
    }
    
    
    public static void main(String[] args) {
        A();
        B();
        C();
        out.close();
    }
}
```

## References

[^ref1]: [Input & Output - USACO Guide](https://usaco.guide/general/input-output?lang=java#method-3---io-template)
