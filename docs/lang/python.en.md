author: cmpute, Henry-ZHR, ranwen, abc1763613206, billchenchina, chinggg, ChungZH, CoelacanthusHex, countercurrent-time, Dong Tsing-hsuen, Early0v0, Enter-tainer, F1shAndCat, Great-designer, hensier, HeRaNO, Hszzzx, imba-tjd, Ir1d, ksyx, lingxier, LovelyBuggies, Marcythm, mgt, Mooos-MoSheng, NachtgeistW, ouuan, Rottenwooood, shawlleyw, shuzhouliu, sshwy, SukkaW, Suyun514, Tiphereth-A, tLLWtG, wineee, wxh06, Xeonacid, yusancky, zyouxam, zzjjbb, jiangmuran, CuriosityQiu

## About Python

Python is an interpreted language that is already widely used in the world. It provides efficient high-level data structures, and can also do object-oriented programming simply and effectively, and can also be used in algorithm competitions.

### Advantages of Python

-   Python is an **interpreted** language: Python does not need compilation and linking, which can reduce operation steps to a certain extent.
-   Python is an **interactive** language: the Python interpreter implements interactive operation, and we can directly input and execute instructions in the terminal.
-   Python is **easy to learn and use**: Python provides a large number of data structures, and also supports the development of large programs.
-   Python has **strong compatibility**: Python simultaneously supports the Windows, macOS, and Unix operating systems.
-   Python has **strong practicality**: from simple input/output to scientific computing and even large WEB applications, we can write suitable Python programs.
-   Python **programs are concise and readable**: Python code is usually shorter than code in other languages that implements the same functionality.
-   Python **supports extension**: Python can develop C language programs (i.e. CPython), and supports linking the Python interpreter with applications developed in the C language, using Python to extend and control that application.

### Notes on learning Python

-   The main Python version currently used is Python 3.7 and above; Python 2 and Python 3.6 and earlier Python 3 are already [unsupported](https://devguide.python.org/versions/#unsupported-versions), but are still used by some old systems and code. This article will **introduce the newer versions of Python**. If you encounter Python 2 code, you can try the [`2to3`](https://docs.python.org/zh-cn/3/library/2to3.html) program to convert Python 2 code into Python 3 code.
-   The design philosophy and syntax structure of Python **differ greatly from some other languages**; it hides many low-level details, so it presents a practical and elegant style.
-   Python is a highly dynamic interpreted language, so its **program running speed is relatively slow**, especially when using its built-in `for` loop statement. When using Python, we should try to use built-in functions such as `filter`, `map`, or use [list comprehension](https://www.pythonforbeginners.com/basics/list-comprehensions-in-python) syntax to improve program performance.

## Environment setup

See [Python 3](../tools/compiler.md#python-3). Or:

-   Windows: you can also obtain Python for free and quickly in the Microsoft Store.

-   macOS/Linux: in general, most Linux distributions already come with Python. If you only intend to learn Python syntax and have no other development needs, there is no need to install Python separately.

    ???+ warning "Note"
        On some systems that install Python by default (referring to installation using a package manager) (such as Unix systems), you should run `python3` in the terminal to open the Python 3 interpreter.[^ref1]

In addition, we can also use tools such as venv, conda, Nix, etc. to manage the Python toolchain and Python packages, create isolated virtual environments, and avoid dependency problems.

As an interpreted language, the execution method of Python is somewhat different from C++; this difference is often not reflected when programming with an IDE, so here we need to emphasize the different ways of running programs.

When you type `python3` in the command line or just open IDLE, you actually enter an interactive programming environment, also called "REPL" ("Read-Eval-Print Loop"); beginners can input statements here and immediately see the result, which makes verifying some syntax extremely easy, and we will also use this form extensively below.

But if you want to write a complete program, you had better create a new text file (usually with the suffix `.py`), and then execute `python3 filename.py` in the command line, and you can run the code and see the result.

### Python versions provided by some platforms

| System name/version | python version |
| ---------------- | ----------------------- |
| Noi Linux 2.0 | 3.8.0, Include requests |
| Luogu judge machine | 3.11.5, NumPy 1.25.2 |
| Hydro-based OJ | 3.8.0+ Include NumPy |
| Ubuntu 22.04 (built-in) | 3.10.4 |
| Microsoft Store | latest official version |

???+ warning "Note"
    This table is valid at the time of writing this article (2025/01/15); it is recommended to go to the relevant platform to re-verify.

Currently, the domestic mirror caches for **source code** are mainly the [Beijing Jiaotong University Free and Open Source Software Mirror Site](https://mirror.bjtu.edu.cn/python/) and the [Huawei Open Source Mirror Site](https://repo.huaweicloud.com/python/); you can try to download the Python installation file there.

## Using `pip` to install third-party libraries

The vitality of Python largely comes from the rich third-party libraries; "calling libraries" is a routine operation when writing some utility programs, and `pip` is the preferred program for installing third-party libraries. Since Python 3.4, it is included by default in the Python binary installer.

The third-party libraries in `pip` are mainly stored on the [Python Package Index (PyPI)](https://pypi.org/); users can also specify other third-party library hosting platforms. For usage, refer to usage help such as [pypi mirror usage help - Tsinghua University Open Source Software Mirror Site](https://mirrors.tuna.tsinghua.edu.cn/help/pypi/). You can obtain more PyPI mirror sources on [MirrorZ](https://mirrorz.org/list/pypi).

???+ info "Install a package using the Tsinghua University Open Source Mirror Site"
    ```sh
    pip install -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple <some-package>
    ```

## Basic syntax

The syntax of Python is concise and easy to understand, and there are also many official and third-party documents and tutorials. Here we only introduce some language features that are relatively practical for OIers; you can learn more Python tutorials on web pages such as the [Python documentation](https://docs.python.org/zh-cn/3/) and the [Python Wiki](https://wiki.python.org/moin/).

### Comments

Adding comments does not affect the running of the code, but adding comments can make the code easier to understand and use.

```python
# what starts with the # character is a single-line comment

"""
a multi-line string is wrapped with triple quotes
(i.e. three single quotes or three double quotes),
but is also commonly used for comments
"""
```

Adding comment code does not affect the code. We encourage adding comments to make the code easier to understand and use.

### Basic data types

#### Everything is an object

In Python, you do not need to declare the variable name and its type in advance; just assign directly to create variables of various types:

```pycon
>>> x = -3  # no need to add a semicolon at the end of the statement
>>> x
-3
>>> f = 3.1415926535897932384626; f  # if you really want to add a semicolon you can, this saves a line
3.141592653589793
>>> s1 = "O"
>>> s1  # in Python double quotes and single quotes have the same function
'O'
>>> b = 'A' == 65  # 'A' and 65 are not the same data type, so they are not equal
>>> b  # the first letters of True, False are both uppercase
False
>>> True + 1 == 2 and not False != 0  # expressions in Python mostly use words, but also support symbols
True
```

But this does not mean Python has no concept of types; in fact the interpreter will automatically infer the variable type according to the assignment or operation, and you can use the built-in function `type()` to view the types of these variables:

```pycon
>>> type(x)
<class 'int'>
>>> type(f)
<class 'float'>
>>> type(s1)  # note, do not name a string str, otherwise the str object will be tampered with
<class 'str'>
>>> type(b)
<class 'bool'>
```

???+ note "What are [**built-in functions**](https://docs.python.org/zh-cn/3/library/functions.html)?"
    In C/C++, many common functions are scattered in different header files, but the Python interpreter has many practical and general functions built in, which you can use directly without needing to notice their existence; but this also brings a small problem: the names of these built-in functions are mostly common words, and you need to be careful to avoid naming your own variables the same, otherwise strange results may occur.

As we can see, Python has built-in integer, floating-point, string, and boolean types, which can be analogized to `int`, `float`, `string`, and `bool` in C++. But there are some obvious differences, such as no `char` character type and no `double` type (but `float` actually corresponds to double precision in C); if you need more precise floating-point operations, you can use the [decimal](https://docs.python.org/zh-cn/3/library/decimal.html) module in the standard library; if you need complex numbers, Python also has a built-in `complex` type (which also means it is best not to name a variable `complex`).
We can see that these types all start with `class`, and this is exactly the key difference between Python and C++: all data in a Python program is represented by objects or relationships between objects; functions are objects, and types themselves are also objects:

```pycon
>>> type(int)
<class 'type'>
>>> type(pow)  # the built-in function for exponentiation, introduced below
<class 'builtin_function_or_method'>
>>> type(type)  # type() is also a built-in function, but somewhat special; interested readers can look it up on their own
<class 'type'>
```

You may feel that these concepts are hard to understand for a moment and useless, so we will not go deeper for now; in the examples below you may gradually appreciate that Python's objects provide powerful methods, and when programming we should prioritize operating around objects rather than processes, which will make our code appear more compact and clear.

#### Number operations

Someone said that you can treat the Python installed in your system as a multi-purpose calculator, which is true.  
In interactive mode, you can input an expression after the prompt `>>>`, and like most other languages (such as C++), use the operators `+`, `-`, `*`, `/`, `%` to operate on numbers, and can also use `()` for grouping that conforms to associativity; readers can experiment on their own, and here we only show the parts that differ greatly from C++:

```pycon
>>> 5.0 * 6  # the operation result of floating-point numbers is a floating-point number
30.0
>>> 15 / 3  # unlike C/C++, division always returns the floating-point float type
5.0
>>> 5 / 100000  # too many digits, the result is displayed in scientific notation form
5e-05
>>> 5 // 3 # using integer division (floor division) rounds down and outputs the integer type
1
>>> -5 // 3 # conforms to the floor-rounding principle, note this is different from C/C++
-2
>>> 5 % 3 # modulo
2
>>> -5 % 3 # the modulo result of a negative number is definitely non-negative, this is also different from C/C++, but both satisfy (a//b)*b+(a%b)==a
1
>>> x = abs(-1e4)  # the built-in function for absolute value
>>> x += 1  # there is no increment/decrement operator
>>> x  # scientific notation defaults to float
10001.0
```

In the above practice, we can find that the division operation (`/`) always returns the floating-point type (in Python 2 it returns an integer). If you want an integer or floor-rounded result, you can use integer division (`//`). Similarly, you can also, like in C++, use modulo (`%`) to compute the remainder, and the form of scientific notation is also the same.

In particular, Python uses `**` for exponentiation, and also provides an efficient implementation of [fast exponentiation](../math/binary-exponentiation.md) through the built-in `pow(a, b, mod)`.

```pycon
>>> 3 ** 4 # exponentiation
81
>>> 2 ** 512
13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084096
>>> pow(2, 512, int(1e4)) # i.e. the fast implementation of 2**512 % 10000, 1e4 is float so it needs to be converted to int
4096
>>> 2048 ** 2048 # try a big integer in IDLE?
>>> 0.1 + 0.1 + 0.1 - 0.3 == 0.  # like C/C++, note that floating-point numbers cannot be directly tested for equality
False
```

#### Data type determination

For a variable, you can use `type(object)` to return the type of the variable, for example the values of `type(8)` and `type('a')` are `<class 'int'>` and `<class 'str'>` respectively.

#### [Basic input/output](https://docs.python.org/zh-cn/3/tutorial/inputoutput.html)

Input/output in Python is mainly done through the built-in functions `input()` and `print()`; the usage of `print()` is very intuitive:

```pycon
>>> a = [1,2,3]; print(a[-1])  # a newline is added at the end by default when printing
3
>>> print(ans[0], ans[1])  # can output any number of variables, separated by spaces by default
1 2
>>> print(a[0], a[1], end='')  # set end='', so no newline at the end
1 2>>>
>>> print(a[0], a[1], sep=', ')  # set sep=', ', change the separator style
1, 2
>>> print(str(a[0]) + ', ' + str(a[1]))  # same output as above, but manually concatenated into a whole string
```

The behavior of the `input()` function is close to `getline()` in C++, i.e. it reads a whole line as a string, and there is no newline character at the end.

```pycon
>>> s = input('Please enter a string of numbers: '); s  # when debugging yourself, you can pass a string to input() as a prompt
Please enter a string of numbers: 1 2 3 4 5 6
'1 2 3 4 5 6'
```

#### Strings

Python 3 provides a powerful string type based on [Unicode](https://docs.python.org/zh-cn/3/howto/unicode.html#unicode-howto), which is used similarly to `string` in C++, and some concepts such as escape characters are also common; besides plus-sign concatenation and index access, it additionally supports scalar-multiplication `*` to repeat a string, and the `in` operator.

```pycon
>>> s1 = "O"  # both single and double quotes can wrap a string, sometimes saving escape characters
>>> s1 += 'I-Wiki'  # to stay synchronized with C++, it is recommended to use double quotes
>>> 'OI' in s1  # detecting substrings is very convenient
True
>>> len(s1)  # similar to C++'s s.length(), but more general
7
>>> s2 = """ Thank you for reading
... Welcome to contribute!
"""   # a string using triple quotes can span multiple lines
>>> s1 + s2 
'OI-Wiki Thank you for reading\nWelcome to contribute!'
>>> print(s1 + s2)  # here we use the print() function to print the string
OI-Wiki Thank you for reading
Welcome to contribute!
>>> s2[2] * 2 + s2[3] + s2[-1]  # negative index counts from the right, add len(s), equivalent to the residue class ring modulo n
'nnk!'
>>> s1[0] = 'o'  # str is an immutable type, cannot be modified in place, actually += also creates a new object
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
```

Python supports multiple compound data types that can combine different values together. The most commonly used `list` type is a group of values marked with square brackets and separated by commas. For example, `[1, 2, 3]` and `['a','b','c']` are both lists.

Besides indexing, strings also support *slicing*, whose design is very ingenious, in the format `s[left-closed index:right-open index:step]`:

```pycon
>>> s = 'OI-Wiki Thank you for reading\nWelcome to contribute!'
>>> s[:8]  # omitting the left-closed index starts from the beginning
'OI-Wiki '
>>> s[8:14]  # the beauty of the left-closed right-open design, length 14-8=6, and seamlessly connects with the previous string
'Thank '
>>> s[-4:]  # omitting the right-open index goes to the end
'te!'
>>> s[8:14:2]  # step is 2
'Tak'
>>> s[::-1]  # when step is -1, we obtain the reversed string
'!etubirtnoc ot emocleW\ngnidaer rof uoy knahT ikiW-IO'
>>> s  # but the original string is unchanged
'OI-Wiki Thank you for reading\nWelcome to contribute!'
```

In the latest Python 3 version, strings are encoded in Unicode, that is, Python's strings support multiple languages.[^ref2] In Python, we can use the built-in function `ord()` on a Unicode character to convert it to the corresponding Unicode code, and the reverse conversion uses the built-in function `chr()`. In C/C++, the `char` type can also be inter-converted with the corresponding ASCII code.

If we want to convert a number into the corresponding string, we can use the built-in function `str()`; conversely we can use `int()` and `float()`; you can analogize this to a cast in C/C++, but the parentheses are not added to the type but wrap the argument as part of the function.

Python's string type provides many powerful methods, including computing the index and number of occurrences of a certain character, converting case, and so on; here we do not list them one by one, and it is strongly recommended to check the [official documentation](https://docs.python.org/zh-cn/3/library/stdtypes.html#text-sequence-type-str) to familiarize yourself with common methods; when encountering string operations you should first consider using these methods rather than doing it yourself.

### Creating arrays

Students coming from C++ may be very confused about how to create arrays in Python; here we introduce the syntax of creating "arrays" in Python. It needs to be emphasized that what we introduce is actually several [sequence types](https://docs.python.org/zh-cn/3/library/stdtypes.html#iterator-types), which are essentially different from C's arrays and closer to `vector` in C++.

#### Using `list`

A list (`list`) is probably the most commonly used and most powerful sequence type in Python; a list can store elements of any type, including nested lists, which conforms to the definition of a "generalized list" in data structures. Note that it should not be confused with the doubly linked list [`list`](./csl/sequence-container.md#list) in the C++ STL, so this article will use "list" instead of `list` to avoid misunderstanding.

```pycon
>>> []  # create an empty list, note that lists use square brackets
[]
>>> nums = [0, 1, 2, 3, 5, 8, 13]; nums  # initialize a list, note that the whole list can be printed directly
[0, 1, 2, 3, 5, 8, 13]
>>> nums[0] = 1; nums  # supports index access, supports modifying elements
[1, 1, 2, 3, 5, 8, 13]
>>> nums.append(nums[-2]+nums[-1]); nums  # append() is like vector's push_back(), and both have no return value
[1, 1, 2, 3, 5, 8, 13, 21]
>>> nums.pop()  # pop and return the last element, can be used as a stack; it can actually also specify a position, defaulting to the end
21
>>> nums.insert(0, 1); nums  # like vector's insert(position, val)
[1, 1, 1, 2, 3, 5, 8, 13]
>>> nums.remove(1); nums  # remove an element by value (only deletes the first occurrence), throws an error if it does not exist
[1, 1, 2, 3, 5, 8, 13]
>>> len(nums)  # find the list length, similar to vector's size(), but len() is a built-in function
7
>>> nums.reverse(); nums  # reverse in place
[13, 8, 5, 3, 2, 1, 1]
>>> sorted(nums)  # obtain the sorted list
[1, 1, 2, 3, 5, 8, 13]
>>> nums  # but the original list is not sorted
[13, 8, 5, 3, 2, 1, 1]
>>> nums.sort(); nums  # sort in place, can specify the parameter key as the sorting criterion
[1, 1, 2, 3, 5, 8, 13]
>>> nums.count(1)  # similar to std::count()
2
>>> nums.index(1)  # return the index of the first occurrence of the value, throws an error if it does not exist
0
>>> nums.clear(); nums  # like vector's clear()
```

The above examples show the similarities between lists and `vector`; the common operations in `vector` can generally also find corresponding methods in a list, but some methods such as `len()`, `sorted()` appear in the form of built-in functions, while functions in the STL algorithm such as `find()`, `count()`, `max_element()`, `sort()`, `reverse()` become methods of objects in Python; when using them you need to be careful to distinguish; for more methods see the [list details](https://docs.python.org/zh-cn/3/tutorial/datastructures.html#more-on-lists) in the official documentation. Below we will show some powerful features of lists as Python's basic sequence type:

Python supports multiple compound data types that can combine different values together. The most commonly used `list` type is a group of values marked with square brackets and separated by commas. For example, `[1, 2, 3]` and `['a','b','c']` are both lists.

```pycon
>>> lst = [1, '1'] + ["2", 3.0]  # adding lists directly generates a new list
>>> lst  # storing different types here is just to show it can be done, but this is not good practice
[1, '1', '2', 3.0]
>>> 3 in lst  # the practical membership test operation, strings also have this operation and additionally support substring detection
True
>>> [1, '1'] in lst  # only supports single-member detection, will not find a "subsequence"
False
>>> lst[1:3] = [2, 3]; lst  # slice and assign, the original list is modified
[1, 2, 3, 3.0]
>>> lst[::-1]  # obtain a new reversed list
[3.0, 3, 2, 1]
>>> lst *= 2; lst  # scalar-multiplication concatenation
[1, 2, 3, 3.0, 1, 2, 3, 3.0]
>>> del lst[4:]; lst  # can also write lst[4:] = [], the del statement can be used for more than just deleting elements in a sequence
[1, 2, 3, 3.0]
```

The above examples show some common operations of lists as sequences; we can see that many operations such as slicing are common with strings, but strings are "immutable sequences" while lists are "mutable sequences", so lists can be flexibly modified through slicing. In C/C++ we often process character arrays through loops; below we will show how to use [list comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions) to convert between strings and lists:

```pycon
>>> # build an integer array over the interval [65, 70), range is also a type, can be regarded as a left-closed right-open interval, the third parameter step can be omitted
>>> nums = list(range(65,70))  # remember range also needs a layer of list() outside
[65, 66, 67, 68, 69]
>>> lst = [chr(x) for x in nums]  # the typical structure of a list comprehension, [exp for var in iterable if cond]
>>> lst  # the above two lines can be merged into [chr(x) for x in range(65,70)]
['A', 'B', 'C', 'D', 'E']
>>> s = ''.join(lst); s # use the empty string '' to concatenate the elements in the list to generate a new string
'ABCDE'
>> list(s)  # a string generates a list of characters
['A', 'B', 'C', 'D', 'E']
>>> # if you do not know there is an s.lower() method you might write the following old-wine-in-new-bottle expression
>>> ''.join([chr(ord(ch) - 65 + 97) for ch in s if ch >= 'A' and ch <= 'Z'])  
'abcde'
```

Below we demonstrate some scenarios more common in OI, such as a two-dimensional "array":

```pycon
>>> vis = [[0] * 3] * 3  # create a 3*3 all-0 array
>>> vis 
[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
>>> vis[0][0] = 1; vis  # how did it modify the other rows too?
[[1, 0, 0], [1, 0, 0], [1, 0, 0]]
>>> # let us first look at the assignment of a one-dimensional list
>>> a1 = [0, 0, 0]; a2 = a1; a3 = a1[:]  # a list can also be directly assigned to a new variable
>>> a1[0] = 1; a1  # modify list a1, seems normal
[1, 0, 0]
>>> a2  # how was a2 also changed
[1, 0, 0]
>>> a3  # a3 is unchanged
[0, 0, 0]
>>> id(a1) == id(a2) and id(a1) != id(a3)  # the built-in function id() gives the "identity value" of an object, analogous to an address; the same address means it is one object
True
>>> vis2 = vis[:]  # copy a two-dimensional list
>>> vis[0][1] = 2; vis  # vis will be modified in bulk
>>> [[1, 2, 0], [1, 2, 0], [1, 2, 0]]
>>> vis2  # but vis2 is a slice copy and yet was also changed
>>> [[1, 2, 0], [1, 2, 0], [1, 2, 0]]
>>> id(vis) != id(vis2)  # vis and vis2 are not one object
True
>>> # although vis2 is not a reference to vis, the corresponding rows in it all point to the same object
>>> [id(vis[i]) == id(vis2[i]) for i in range(3)]
[True, True, True]
>>> # look back at the two-dimensional list itself
>>> [id(x) for x in vis]  # the specific numbers are different from here but the three values must be the same, indicating they are three identical objects
[139760373248192, 139760373248192, 139760373248192]
```

Actually there is an important fact: assignment in Python only passes references rather than creating new values; you can create variables of different types and assign them to new variables, and verify that the identity values of the two are the same; it is just that until now we have only introduced the mutable type of list, and when assigning a new value to an immutable type such as a number or string, a new object is actually created, so the two variables before and after do not interfere with each other. But a list is a mutable type, so when we modify an element of one list, the other list is also modified because it points to the same object. Creating a two-dimensional array is a similar situation; in the example, creating a two-dimensional list with multiplication is equivalent to repeating the one-dimensional list `[0]*3` 3 times, so operations involving one of the lists will simultaneously affect the other two lists. Even more unfortunately, when assigning a two-dimensional list to another variable, even if we use slicing to copy, it is only a "shallow copy", and the elements in it still point to the same object; to solve this problem we need to use [`deepcopy`](https://docs.python.org/3/library/copy.html) in the standard library, or try to avoid assigning the whole two-dimensional list. Fortunately, avoiding creating duplicate lists when creating a two-dimensional list is relatively simple; just use a "list comprehension":

```pycon
>>> vis1 = [[0] * 3 for _ in range(3)]  # setting the unused loop counter variable to an underscore _ is a convention
>>> # but in the REPL _ by default refers to the result output by the previous expression, so a double underscore can also be used
>>> vis1
[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
>>> [id(x) for x in vis1]  # the specific numbers are different from here but the three values must be different, indicating they are three different objects
[139685508981248, 139685508981568, 139685508981184]
>>> vis1[0][0] = 1
[[1, 0, 0], [0, 0, 0], [0, 0, 0]]
>>> a2[0][0] = 10  # access and assign a two-dimensional array
```

We introduced list comprehensions before covering the usage of loops; this is because Python is a highly dynamic interpreted language, so its program running has a lot of extra overhead. In particular, **for loops run extremely slowly in Python**. Therefore, when using Python, if you want to obtain high performance, try to use list comprehensions, or built-in functions such as `filter`, `map` to directly operate on the whole sequence to avoid loops; of course this still depends on the specific problem.

#### Using NumPy

??? note "What is NumPy"
    [NumPy](https://numpy.org/) is a famous Python scientific computing library that provides high-performance numerical and matrix operations. When testing algorithm prototypes, we can use NumPy to avoid hand-writing algorithms such as sorting, finding extrema, etc. The core data structure of NumPy is `ndarray`, i.e. the n-dimensional array, which is stored contiguously in memory and is fixed-length. In addition, the core of NumPy is written in C, so the operation efficiency is very high. However, note that it is not part of the standard library; it can be installed using `pip install numpy`, but it is not guaranteed to be available in an OI exam environment (see [Python versions](#python-versions-provided-by-some-platforms) at the beginning of the article).

The following code will introduce how to use NumPy to build multidimensional arrays and access them.

```pycon
>>> import numpy as np  # please search for the meaning and usage of import on your own
>>> np.empty(3) # create an empty array with capacity 3, note it is not initialized to 0
array([0.00000000e+000, 0.00000000e+000, 2.01191014e+180])
>>> np.zeros((3, 3)) # create a 3*3 array and initialize it to 0
array([[0., 0., 0.],
       [0., 0., 0.],
       [0., 0., 0.]])
>>> a1 = np.zeros((3, 3), dtype=int) # create a 3×3 integer array
>>> a1[0][0] = 1 # access and assign
>>> a1[0, 0] = 1 # more friendly syntax
>>> a1.shape # the shape of the array
(3, 3)

>>> a1[:2, :2] # take the submatrix formed by the first two rows and first two columns, no copy
array([[1, 0],
       [0, 0]])

>>> a1[:, [0, 2]] # get the 1st and 3rd columns, no copy
array([[1, 0],
       [0, 0],
       [0, 0]])
>>> np.max(a1) # get the maximum value of the array
1
>>> a1.flatten() # flatten the array
array([1, 0, 0, 0, 0, 0, 0, 0, 0])

>>> np.sort(a1, axis = 1) # sort the array along the row direction, return the sorted result
array([[0, 0, 1],
       [0, 0, 0],
       [0, 0, 0]])
>>> a1.sort(axis = 1) # sort the array in place along the row direction
```

#### Using `array`

[`array`](https://docs.python.org/zh-cn/3/library/array.html) is an efficient numerical array provided by the Python standard library, which can compactly represent an array of basic type values, but does not support array nesting, and is rarely seen being used; here we just mention it in passing.

Unless otherwise specified, "array" in the following text generally refers to "list".

### [Input/output](https://docs.python.org/zh-cn/3/tutorial/inputoutput.html)

Input/output in Python is mainly done through the built-in functions `input()` and `print()`. This has been introduced earlier; below we introduce advanced usage.

#### Formatted output

Algorithm competitions usually only involve basic numerical and string output; `print()` is basically sufficient, and only when it involves the number of digits of a floating-point number do we need to use formatted string output. There are three methods for formatting: the first and most old-fashioned method is to use the `printf()`-style `%` operator; another is to use the [`format` function](https://docs.python.org/3/library/string.html#formatstrings); the third is the [f-string](https://docs.python.org/zh-cn/3/tutorial/inputoutput.html#formatted-string-literals) newly added in Python 3.6, which is the most concise, but there is no guarantee that the Python version in the exam is new enough. For detailed and rich explanations, refer to [this web page](https://www.python-course.eu/python3_formatted_output.php); although it is more recommended to use the `format()` method, to obtain an experience close to C, below we only demonstrate the old-fashioned method similar to `printf()`:

```pycon
>>> pi = 3.1415926; print('%.4f' % pi)   # the format is %[flags][width][.precision]type
3.1416
>>> '%.4f - %8f = %d' % (pi, 0.1416, 3)  # multiple arguments on the right are wrapped in (), which is actually a "tuple" as we will see later
'3.1416 - 0.141600 = 3'
```

#### The `split()` function

The behavior of the `input()` function is close to `getline()` in C++, i.e. it reads a whole line as a string, and there is no newline character at the end; but in algorithm competitions, a common input form is multiple values input on one line, so we need to use the string's `split()` method combined with a list comprehension to obtain a list storing numeric types; below we take inputting n numbers and finding the average as an example to demonstrate the method of inputting n numbers to obtain an "array":

```pycon
>>> s = input('Please enter a string of numbers: '); s  # when debugging yourself, you can pass a string to input() as a prompt
Please enter a string of numbers: 1 2 3 4 5 6
'1 2 3 4 5 6'
>>> a = s.split(); a
['1', '2', '3', '4', '5', '6']
>>> a = [int(x) for x in a]; a
[1, 2, 3, 4, 5, 6]
>>> # the above input process can be written in one line a = [int(x) for x in input().split()]
>>> sum(a) / len(a)  # sum() is a built-in function
3.5
```

Sometimes a problem inputs a fixed few numbers per line, such as the start point, end point, and weight of an edge; if we only use the method mentioned above, we can only read the array each time and then assign values according to the subscript; at this time we can use Python's "unpacking" feature to assign multiple variables at once:

```pycon
>>> u, v, w = [int(x) for x in input().split()]
1 2 4
>>> print(u,v,w)
1 2 4
```

Problems often encounter the case of inputting N lines, but we have not yet covered the most basic loop statement; but Python's powerful sequence operations can handle multi-line input without using loops; below we assume reading the start point, end point, and weight of each edge into three arrays respectively:

```pycon
>>> N = 4; mat = [[int(x) for x in input().split()] for i in range(N)]
1 3 3 
1 4 1 
2 3 4 
3 4 1 
>>> mat  # first read a two-dimensional array by rows
[[1, 3, 3], [1, 4, 1], [2, 3, 4], [3, 4, 1]]
>>> u, v, w = map(list, zip(*mat))   
# * unpacks mat to get the multiple inner lists
# zip() aggregates the corresponding elements in multiple lists into tuples, obtaining an iterator
# map(list, iterable) converts the elements in the sequence (here tuples) into lists
>>> print(u, v, w)  # directly unpack the iterator obtained by map(), assigning to u, v, w respectively
[1, 1, 2, 3] [3, 4, 3, 4] [3, 1, 4, 1]
```

The above program is actually equivalent to first reading an N-row 3-column matrix, then transposing it into a 3-row N-column matrix, i.e. the outer list nests 3 lists, and finally assigns the 3 lists representing the start point, end point, and weight to u, v, w respectively. The built-in function [`zip()`](https://docs.python.org/zh-cn/3/library/functions.html#zip) can concatenate the corresponding elements in multiple equal-length sequences within a "tuple" to obtain a new sequence. And `map()` is actually an operation of functional programming; it applies a given function to the elements of the sequence produced by `zip()`, and here it uses `list()` to turn tuples into lists. You can practice using `*` and [`zip()`](https://docs.python.org/zh-cn/3/library/functions.html#zip), [`map()`](https://docs.python.org/zh-cn/3/library/functions.html#map) on your own to understand their meanings. Note that in Python 3, `zip()` and `map()` no longer create and return lists but return iterators; here we do not explain the similarities and differences between them for now; you can consider that an iterator can produce each element in a list, and wrapping the iterator with `list()` can generate a list.

#### [File reading and writing](https://docs.python.org/3/reference/compound_stmts.html#the-with-statement)

The Python built-in function [`open()`](https://docs.python.org/3/library/functions.html#open) is used for file reading and writing; to prevent the file from not being closed normally due to an error during reading and writing, here we only introduce the safe reading and writing method using the [`with`](https://docs.python.org/3/reference/compound_stmts.html#the-with-statement) statement:

```python
a = []
with open("in.txt") as f:
    N = int(f.readline())  # read the N on the first line
    a[len(a) :] = [[int(x) for x in f.readline().split()] for i in range(N)]

with open("out.txt", "w") as f:
    f.write("1\n")
```

There are many functions about file reading and writing, applicable to different scenarios respectively; since OI contests do not yet support the use of Python, we omit it here.

### [Control flow](https://docs.python.org/zh-cn/3/tutorial/controlflow.html)

Although we have learned many features of Python, the Python code we have shown so far is all single-line statements, which masks a major difference in code style between Python and C: first, Python does not use `{}` but uses indentation to represent block structures; if the indentation is not aligned it will directly report an error, and if tab and space are mixed it will also report an error; second, at the place where a block structure begins, such as the end of the line of an `if` or `for` statement, there must be a colon `:`. This helps the readability of the code, but you may also miss the free experience of C; after all, having to manually align due to lost indentation when copy-pasting is very annoying.

#### Loop structures

List comprehensions can efficiently complete batch operations within one line, but sometimes we have already been overly deliberate in order to compress lines; in many scenarios we can still only use loop structures, so let us again take reading multi-line data as an example to show how loops in Python are written:

```python
# please note that starting from now we no longer use the REPL, please copy the multi-line data yourself
u, v, w = ([] for i in range(3))  # multi-variable assignment
for i in range(4):  # here we assume inputting 4 lines of data
    _u, _v, _w = [int(x) for x in input().split()]
    u.append(_u), v.append(_v), w.append(_w)
    # cannot perform operations like cin >> u[i] >> v[i] >> w[i], because it must exceed the current length of the list
    # of course you can choose to initialize an all-0 list of length MAXN, but you need to remember the real length and delete the extra elements
print(u, v, w)
```

Note that the for loop in Python is quite different from C/C++; its function is similar to the [range-based loop](./new.md#range-based-for-loop) introduced in C++11; it essentially iterates over the elements in a sequence, for example writing a loop to traverse array subscripts requires iterating `range(len(lst))`, rather than really defining start and termination conditions, so it is not as flexible to use as C/C++.

Below we use a while loop to show how to input when the number of lines is uncertain:

```python
u, v, w = [], [], []  # multi-variable assignment, actually the same as above
s = input()  # note that in Python an assignment statement cannot be placed in a conditional expression
while s:  # cannot do while(!scanf()) like C
    # use slice concatenation to avoid append(), note the list comprehension nests a list again
    u[len(u) :], v[len(v) :], w[len(w) :] = [[int(x)] for x in s.split()]
    s = input()
# after Python 3.8 introduced the walrus operator, you can save two lines, but the exam environment likely does not support it
while s := input():
    u[len(u) :], v[len(v) :], w[len(w) :] = [[int(x)] for x in s.split()]
print(u, v, w)
```

#### Selection structures

They are largely the same as C/C++; some formal differences are all shown in the example below; in addition, note that assignment operators are not allowed in conditional expressions (Python 3.8 and above can use [`:=`](https://www.python.org/dev/peps/pep-0572/)), and there is [no switch statement](https://docs.python.org/zh-cn/3/faq/design.html#why-isn-t-there-a-switch-or-case-statement-in-python).

```python
# no parentheses on either side of the conditional expression
if 4 >= 3 > 2 and 3 != 5 == 5 != 7:
    print("relational operators can be used consecutively")
    x = None or [] or -2
    print("&&  ||  !", "and  or  not (Chinese)", "and or not", sep="\n")
    print("using and/or well can save lines")
    if not x:
        print("a negative number is also True, this statement is not executed")
    elif x & 1:
        print("use elif instead of else if\n" "bit operators are close to C, even&1 gives 0, this statement is not executed")
    else:
        print("there is also a ternary operator") if x else print("note the structure")
```

#### Exception handling

Although C++ has [try blocks](https://zh.cppreference.com/w/cpp/language/try_catch) for exception handling, they are generally never used in competitions; while in Python the [EAFP](https://docs.python.org/zh-cn/3/glossary.html#term-eafp) style is common, so the code may extensively use [`try-except`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#the-try-statement) statements, which will also be used when introducing the `dict` structure below; here we show:

```python
s = "OI-wiki"
pat = "NOIP"
x = s.find(pat)  # find() returns -1 if not found
try:
    y = s.index(pat)  # index() throws an error if not found
    print(y)  # this line is skipped
except ValueError:
    print("not found")
    try:
        print(y)  # at this time y is not defined, so it throws an error again
    except NameError as e:
        print("cannot output y")
        print("reason:", e)
```

### Built-in containers

Python has many powerful container types built in; only by using them proficiently and understanding their characteristics can Python truly have a place in algorithm competitions; besides the `list` (list) introduced in detail above, there are also the types `tuple` (tuple), [`dict`](https://docs.python.org/zh-cn/3/library/stdtypes.html#mapping-types-dict) (dictionary), and `set` (set).

A tuple can be simply understood as an immutable list, but we still need to note the connotation of "immutable": if a certain element in the tuple is a mutable type such as a list, then we can still modify the value of that list, because what is stored in the tuple is a reference to the list, so the tuple itself has not changed. The advantage of tuples is that the overhead is relatively small and they are "[hashable](https://docs.python.org/zh-cn/3/glossary.html)", the latter being very useful when creating dictionaries and sets.

```python
tup = tuple([[1, 2], 4])  # obtain a tuple from a list
# equivalent to tup = ([1,2], 4)
tup[0].append(3)
print(tup)
a, b = 0, "I-Wiki"  # multi-variable assignment is actually tuple unpacking
print(id(a), id(b))
b, a = a, b
print(id(a), id(b))  # you should see that the id values of a, b are now swapped
# this further shows that in Python, a variable is more like a name, and assignment just makes it refer to an object
```

A dictionary is like [`map`](./csl/associative-container.md#map) in the C++ STL (please distinguish it from the built-in function [`map()`](https://docs.python.org/zh-cn/3/library/functions.html#map) in Python) used to store key-value pairs, in a form similar to [JSON](https://docs.python.org/3/library/json.html), but in JSON the keys must be strings wrapped in double quotes, while a dictionary is more flexible and powerful; any hashable object can be used as a key of a dictionary. Note that the characteristics of dictionaries have changed considerably after several Python version updates, including the order of elements in them, etc.; please explore on your own.

```python
dic = {"key": "value"}  # basic form
dic = {chr(i): i for i in range(65, 91)}  # mapping of uppercase letters to the corresponding ASCII code, note the phrasing
dic = dict(zip([chr(i) for i in range(65, 91)], range(65, 91)))  # same effect as above
dic = {dic[k]: k for k in dic}  # reverse the key-value pairs, for k in dic iterates over its keys
dic = {v: k for k, v in dic.items()}  # same function as the above line, dic.items() stores a single key-value pair as a tuple
dic = {
    k: v for k, v in sorted(dic.items(), key=lambda x: -x[1])
}  # sort the dictionary by value in reverse, using a lambda expression

print(dic["A"])  # return the item in dic with 'A' as the key, here the value is 65
dic["a"] = 97  # set d[key] to value, if key was not in the dictionary this is a direct insertion
if "b" in dic:  # LBYL (Look Before You Leap) style
    print(dic["b"])  # if the dictionary does not have this key it will error, so check first
else:
    dic["b"] = 98

# classic scenario: counting occurrences
# a new key does not exist in the original dictionary, requiring additional handling
try:  # EAFP (Easier to Ask for Forgiveness than Permission) style
    cnter[key] += 1
except KeyError:
    cnter[key] = 1
```

A set is like [`set`](./csl/associative-container.md#set) in the C++ STL; it does not save repeated elements, and can be regarded as a dictionary that saves only keys. Note that both sets and dictionaries are wrapped in `{}`, but using `{}` alone creates an empty dictionary rather than an empty set; here we no longer give an example.

### Writing functions

Defining a function in Python does not require specifying parameter types and return value types, which invisibly reduces the amount of code for OI contestants.

```python
def add(a, b):
    return a + b  # the advantage of dynamic typing, a and b can also be strings


def add_no_swap(a, b):
    print("in func #1:", id(a), id(b))
    a += b
    b, a = a, b
    print("in func #2:", id(a), id(b))  # a, b are already swapped
    return a, b  # return multiple values, actually returning a tuple, which can be received by unpacking


lst1 = [1, 2]
lst2 = [3, 4]
print("outside func #1:", id(lst1), id(lst2))
add_no_swap(lst1, lst2)
# outside the function lst1, lst2 are not swapped
print("outside func #2:", id(lst1), id(lst2))
# but the values have indeed changed
print(lst1, lst2)
```

#### Default parameters

The parameters of functions in Python are very flexible, with keyword parameters, variadic parameters, etc., but these features are not very useful in algorithm competitions; here we only introduce default parameters, because C++ also has default parameters, and using default parameters in Python is very likely to encounter a pitfall. For example, the following code.

```python
def append_to(element, to=[]):
    to.append(element)
    return to


lst1 = append_to(12)
lst2 = append_to(42)
print(lst1, lst2)

# you might think the output is [12] [42]
# but the running result is actually [12, 42] [12, 42]
```

The reason for the above running result is that the value of a default parameter is only assigned once when the function is defined; for mutable objects (such as lists, dictionaries, sets), all calls will share the same object, and `lst1` and `lst2` actually both point to the same default list object in memory. Therefore, after the second call, the content of this shared list is modified to `[12, 42]`. So the value of a function's default parameter should be set to an immutable object; using `None` as a placeholder is a best practice:

```python
def append_to(element, to=None):
    if to is None:
        to = []
    to.append(element)
    return to


lst1 = append_to(12)
lst2 = append_to(42)
print(lst1, lst2)

# the running result is [12] [42]
```

#### Type annotations

Python is a dynamically type-checked language that handles types in a flexible but implicit way; the Python interpreter only checks whether the types are correct at runtime, and allows changing variable types at runtime; as the saying goes "dynamic typing is fun for a while, code refactoring is a cremation", and some errors in a program may only be exposed at runtime:

```pycon
>>> if False:
...     1 + "two"  # This line never runs, so no TypeError is raised
... else:
...     1 + 2
...
3

>>> 1 + "two"  # Now this is type checked, and a TypeError is raised
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

After Python 3.5, type annotations were introduced, allowing setting the types of function parameters and return values, but they are only a hint and have no actual restriction effect; a static checking tool is needed to rule out this kind of error (such as [PyCharm](https://www.jetbrains.com/pycharm/) and [Mypy](http://mypy-lang.org/)), so it seems somewhat useless; for OIers it is even more just something to know about; we can set type annotations for a function's parameters and return value in the following way:

```python
def headline(
    text,  # type: str
    width=80,  # type: int
    fill_char="-",  # type: str
):  # type: (...) -> str
    return f"{text.title()}".center(width, fill_char)


print(headline("type comments work", width=40))
```

Besides function parameters, variables can also be type-annotated; you can view all type annotations in a function by calling `__annotations__`. Variable type annotations give Python the nature of a static language, i.e. separating declaration from assignment:

```pycon
>>> nothing: str
>>> nothing
NameError: name 'nothing' is not defined

>>> __annotations__
{'nothing': <class 'str'>}
```

## Decorators

A decorator is a function that accepts a function or method as its only parameter and returns a new function or method, which integrates the decorated function or method and comes with some additional functionality. In short, we can increase the functionality of a function without modifying the function code. For related knowledge, refer to the [official documentation](https://docs.python.org/3/glossary.html#term-decorator).

Some decorators are very practical in competitions, such as [`lru_cache`](https://docs.python.org/3/library/functools.html#functools.lru_cache), which can automatically add memoization ability to a function, and is very practical in recursive algorithms:

`@lru_cache(maxsize=128,typed=False)`

-   There are 2 parameters passed in: `maxsize` and `typed`; if not passed, the default value of `maxsize` is 128, and the default value of `typed` is `False`.
-   Among them, the `maxsize` parameter represents the capacity of the LRU cache, i.e. the maximum number of cacheable results of the decorated method. If this parameter value is 128, it means the decorated method can cache at most 128 return results; if `maxsize` is passed in as `None`, it means an infinite number of results can be cached.
-   If `typed` is set to `True`, function arguments of different types will be cached separately; for example, `f(3)` and `f(3.0)` will be cached twice.

The following is an example of using `lru_cache` to optimize computing the Fibonacci sequence:

```python
@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)
```

## Commonly used built-in libraries

Here we introduce some built-in libraries that may be used when writing algorithms; for specific usage you can search on your own or read the [official documentation](https://docs.python.org/3/library/index.html).

| Library name | Purpose |
| ------------------------------------------------------------------- | -------------- |
| [`array`](https://docs.python.org/3/library/array.html) | fixed-length array |
| [`argparse`](https://docs.python.org/3/library/argparse.html) | command-line argument processing |
| [`bisect`](https://docs.python.org/3/library/bisect.html) | binary search |
| [`collections`](https://docs.python.org/3/library/collections.html) | data structures such as ordered dictionary, double-ended queue, etc. |
| [`fractions`](https://docs.python.org/3/library/fractions.html) | rational numbers |
| [`heapq`](https://docs.python.org/3/library/heapq.html) | heap-based priority queue |
| [`io`](https://docs.python.org/3/library/io.html) | file streams, memory streams |
| [`itertools`](https://docs.python.org/3/library/itertools.html) | iterators |
| [`math`](https://docs.python.org/3/library/math.html) | math functions |
| [`os.path`](https://docs.python.org/3/library/os.html) | system paths, etc. |
| [`random`](https://docs.python.org/3/library/random.html) | random numbers |
| [`re`](https://docs.python.org/3/library/re.html) | regular expressions |
| [`struct`](https://docs.python.org/3/library/struct.html) | convert structs and binary data |
| [`sys`](https://docs.python.org/3/library/sys.html) | system information |

## Comparing C++ and Python from an example problem

??? note "[Example problem Luogu P4779 [Template] Single-source shortest path (standard version)](https://www.luogu.com.cn/problem/P4779)"
    Given a graph with $n(1 \leq n \leq 10^5)$ points and $m(1 \leq m \leq 2\times 10^5)$ directed edges with non-negative weights, please compute the distance from $s$ to each point. The data guarantees that any point can be reached from $s$.

### Declaring constants

=== "C++"
    ```cpp
    #include <cstdio>
    #include <cstring>
    #include <queue>
    #include <vector>
    using namespace std;
    constexpr int N = 1e5 + 5, M = 2e5 + 5;
    ```

=== "Python"
    ```python
    try:  # import the priority queue module
        import Queue as pq  # python version < 3.0
    except ImportError:
        import queue as pq  # python3.*
    
    N = int(1e5 + 5)
    M = int(2e5 + 5)
    INF = 0x3F3F3F3F
    ```

### Declaring the forward-star struct and other variables

=== "C++"
    ```cpp
    struct qxx {
      int nex, t, v;
    };
    
    qxx e[M];
    int h[N], cnt;
    
    void add_path(int f, int t, int v) { e[++cnt] = qxx{h[f], t, v}, h[f] = cnt; }
    
    using pii = pair<int, int>;
    priority_queue<pii, vector<pii>, greater<pii>> q;
    int dist[N];
    ```

=== "Python"
    ```python
    class qxx:  # forward-star class (struct)
        def __init__(self):
            self.nex = 0
            self.t = 0
            self.v = 0
    
    
    e = [qxx() for i in range(M)]  # linked list
    h = [0 for i in range(N)]
    cnt = 0
    
    dist = [INF for i in range(N)]
    q = pq.PriorityQueue()  # define a priority queue, by default a min-heap on the first element
    
    
    def add_path(f, t, v):  # add an edge in the forward star
        # if you want to modify a global variable, you must use global to declare it
        global cnt, e, h
        # output statement for debugging, use a tuple for multiple variables
        # print("add_path(%d,%d,%d)" % (f,t,v))
        cnt += 1
        e[cnt].nex = h[f]
        e[cnt].t = t
        e[cnt].v = v
        h[f] = cnt
    ```

### Dijkstra algorithm

=== "C++"
    ```cpp
    void dijkstra(int s) {
      memset(dist, 0x3f, sizeof(dist));
      dist[s] = 0, q.push(make_pair(0, s));
      while (q.size()) {
        pii u = q.top();
        q.pop();
        if (dist[u.second] < u.first) continue;
        for (int i = h[u.second]; i; i = e[i].nex) {
          const int &v = e[i].t, &w = e[i].v;
          if (dist[v] <= dist[u.second] + w) continue;
          dist[v] = dist[u.second] + w;
          q.push(make_pair(dist[v], v));
        }
      }
    }
    ```

=== "Python"
    ```python
    def nextedgeid(u):  # a generator, can be used in a for loop
        i = h[u]
        while i:
            yield i
            i = e[i].nex
    
    
    def dijkstra(s):
        dist[s] = 0
        q.put((0, s))
        while not q.empty():
            u = q.get()  # the get function also deletes the corresponding element in the heap
            if dist[u[1]] < u[0]:
                continue
            for i in nextedgeid(u[1]):
                v = e[i].t
                w = e[i].v
                if dist[v] <= dist[u[1]] + w:
                    continue
                dist[v] = dist[u[1]] + w
                q.put((dist[v], v))
    ```

### Main function

=== "C++"
    ```cpp
    int n, m, s;
    
    int main() {
      scanf("%d%d%d", &n, &m, &s);
      for (int i = 1; i <= m; i++) {
        int u, v, w;
        scanf("%d%d%d", &u, &v, &w);
        add_path(u, v, w);
      }
      dijkstra(s);
      for (int i = 1; i <= n; i++) printf("%d ", dist[i]);
      return 0;
    }
    ```

=== "Python"
    ```python
    if __name__ == "__main__":
        # read multiple integers on one line. note it reads the whole line
        n, m, s = map(int, input().split())
        for i in range(m):
            u, v, w = map(int, input().split())
            add_path(u, v, w)
    
        dijkstra(s)
    
        for i in range(1, n + 1):
            print(dist[i], end=" ")
    
        print()
    ```

### Complete code

=== "C++"
    ```cpp
    #include <cstdio>
    #include <cstring>
    #include <queue>
    #include <vector>
    using namespace std;
    constexpr int N = 1e5 + 5, M = 2e5 + 5;
    
    struct qxx {
      int nex, t, v;
    };
    
    qxx e[M];
    int h[N], cnt;
    
    void add_path(int f, int t, int v) { e[++cnt] = qxx{h[f], t, v}, h[f] = cnt; }
    
    using pii = pair<int, int>;
    priority_queue<pii, vector<pii>, greater<pii>> q;
    int dist[N];
    
    void dijkstra(int s) {
      memset(dist, 0x3f, sizeof(dist));
      dist[s] = 0, q.push(make_pair(0, s));
      while (q.size()) {
        pii u = q.top();
        q.pop();
        if (dist[u.second] < u.first) continue;
        for (int i = h[u.second]; i; i = e[i].nex) {
          const int &v = e[i].t, &w = e[i].v;
          if (dist[v] <= dist[u.second] + w) continue;
          dist[v] = dist[u.second] + w;
          q.push(make_pair(dist[v], v));
        }
      }
    }
    
    int n, m, s;
    
    int main() {
      scanf("%d%d%d", &n, &m, &s);
      for (int i = 1; i <= m; i++) {
        int u, v, w;
        scanf("%d%d%d", &u, &v, &w);
        add_path(u, v, w);
      }
      dijkstra(s);
      for (int i = 1; i <= n; i++) printf("%d ", dist[i]);
      return 0;
    }
    ```

=== "Python"
    ```python
    try:  # import the priority queue module
        import Queue as pq  # python version < 3.0
    except ImportError:
        import queue as pq  # python3.*
    
    N = int(1e5 + 5)
    M = int(2e5 + 5)
    INF = 0x3F3F3F3F
    
    
    class qxx:  # forward-star class (struct)
        def __init__(self):
            self.nex = 0
            self.t = 0
            self.v = 0
    
    
    e = [qxx() for i in range(M)]  # linked list
    h = [0 for i in range(N)]
    cnt = 0
    
    dist = [INF for i in range(N)]
    q = pq.PriorityQueue()  # define a priority queue, by default a min-heap on the first element
    
    
    def add_path(f, t, v):  # add an edge in the forward star
        # if you want to modify a global variable, you must use global to declare it
        global cnt, e, h
        # output statement for debugging, use a tuple for multiple variables
        # print("add_path(%d,%d,%d)" % (f,t,v))
        cnt += 1
        e[cnt].nex = h[f]
        e[cnt].t = t
        e[cnt].v = v
        h[f] = cnt
    
    
    def nextedgeid(u):  # a generator, can be used in a for loop
        i = h[u]
        while i:
            yield i
            i = e[i].nex
    
    
    def dijkstra(s):
        dist[s] = 0
        q.put((0, s))
        while not q.empty():
            u = q.get()
            if dist[u[1]] < u[0]:
                continue
            for i in nextedgeid(u[1]):
                v = e[i].t
                w = e[i].v
                if dist[v] <= dist[u[1]] + w:
                    continue
                dist[v] = dist[u[1]] + w
                q.put((dist[v], v))
    
    
    # if you directly run this Python code (not a module call or anything) then execute the command
    if __name__ == "__main__":
        # read multiple integers on one line. note it reads the whole line
        n, m, s = map(int, input().split())
        for i in range(m):
            u, v, w = map(int, input().split())
            add_path(u, v, w)
    
        dijkstra(s)
    
        for i in range(1, n + 1):
            # both output syntaxes can be used
            print("{}".format(dist[i]), end=" ")
            # print("%d" % dist[i],end=' ')
    
        print()  # newline at the end
    ```

## Reference documents

1.  [Python Documentation](https://www.python.org/doc/)
2.  [Python official Chinese tutorial](https://docs.python.org/zh-cn/3/tutorial/)
3.  [Learn Python3 In Y Minutes](https://learnxinyminutes.com/docs/python3/)
4.  [Real Python Tutorials](https://realpython.com/)
5.  [Liao Xuefeng's Python tutorial](https://www.liaoxuefeng.com/wiki/1016959663602400/)
6.  [GeeksforGeeks: Python Tutorials](https://www.geeksforgeeks.org/python-programming-language/)

## References and notes

[^ref1]: [2. Python interpreter — Python 3 documentation](https://docs.python.org/zh-cn/3/tutorial/interpreter.html#id1)

[^ref2]: [Unicode guide — Python 3 documentation](https://docs.python.org/zh-cn/3/howto/unicode.html#the-string-type)
