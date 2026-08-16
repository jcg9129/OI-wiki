author: johnvp22, Ir1d

## What is `string`

`std::string` is a class provided in the standard library `<string>` (note not the `<string.h>` library in the C language); it is essentially an alias of `std::basic_string<char>`.

## Why use `string`

In the C language, string operations are provided, but strings can only be implemented through character arrays. `string`, on the other hand, is a simple class, easy to use, and is widely used in OI competitions. Moreover, compared with other STL containers, the constant factor of `string` can be considered very excellent, basically comparable to a character array.

### `string` can dynamically allocate space

Like many STL containers, `string` can dynamically allocate space, which allows us to directly use `std::cin` to input, but its speed is likewise relatively slow. This also means we do not have to worry about memory.

### `string` overloads the addition operator and comparison operators

The addition operator of `string` can directly concatenate two strings or a string and a character. Similar to `std::vector`, `string` overloads the comparison operators, likewise comparing in lexicographic order, so we can directly call `std::sort` to sort several strings.

## Usage

Below we introduce the basic operations of `string`; for details see the [C++ documentation](https://zh.cppreference.com/w/cpp/string/basic_string).

### Declaration

```cpp
std::string s;
```

### Converting to a char array

In the C language, there are also many string functions, but their parameters are all of char pointer type; for convenience of use, `string` has two member functions that can convert itself to a char pointer——`data()`/`c_str()` (before C++11, `c_str()` guarantees a null character at the end while `data()` does not; since C++11 the two behave identically[^string1]), for example:

```cpp
printf("%s", s);          // not guaranteed to compile; behavior is undefined
printf("%s", s.data());   // undefined behavior before C++11; outputs correctly since C++11
printf("%s", s.c_str());  // definitely outputs correctly
```

### Getting the length

Many functions can return the length of a string:

```cpp
printf("The length of s is %zu", s.size());
printf("The length of s is %zu", s.length());
printf("The length of s is %zu", strlen(s.c_str()));
```

???+ note "The complexity of these functions"
    The complexity of `strlen()` is definitely linearly related to the length of the string.
    
    The complexity of `size()` and `length()` was not specified in C++98, and was specified as constant complexity in C++11. But on common compilers, even in C++98, the complexity of these two functions is also constant.

???+ warning "Warning"
    The return value types of these three functions (as well as the `find` function to be mentioned below) are all `size_t` (`unsigned long`). Therefore, these return values do not support directly comparing or operating with negative numbers; it is recommended to perform a cast when needed.

### Finding the first occurrence of a certain character (string)

The `find(str,pos)` function can be used to find the first occurrence of a character/string in a string after `pos` (inclusive) (if no argument is passed to `pos`, it defaults to `0`). If it does not occur, it returns `string::npos` (defined as `-1`, but the type is still `size_t`/`unsigned long`).

Example:

```cpp
string s = "OI Wiki", t = "OI", u = "i";
int pos = 5;
printf("The character I first occurs at position %lu of s\n", s.find('I'));
printf("The character a first occurs at position %lu of s\n", s.find('a'));
printf("The character a first occurs at position %d of s\n", s.find('a'));
printf("The string t first occurs at position %lu of s\n", s.find(t));
printf("Starting from position pos in s, the string u first occurs at position %lu", s.find(u, pos));
```

Output:

```text
The character I first occurs at position 1 of s
The character a first occurs at position 18446744073709551615 of s // i.e. size_t(-1), the specific value is platform-dependent.
The character a first occurs at position -1 of s // cast to int type, it normally outputs -1
The string t first occurs at position 0 of s
Starting from position pos in s, the string u first occurs at position 6
```

### Extracting a substring

The `substr(pos, len)` function returns the string formed by extracting at most `len` characters starting from position `pos` (if the length of the suffix starting from `pos` is less than `len`, then this suffix is extracted).

Example:

```cpp
string s = "OI Wiki", t = "OI";
printf("The substring formed by at most three characters starting from the fourth position of string s is %s\n",
       s.substr(3, 3).c_str());
printf("The substring formed by at most three characters starting from the second position of string t is %s",
       t.substr(1, 3).c_str());
```

Output:

```text
The substring formed by at most three characters starting from the fourth position of string s is Wik
The substring formed by at most three characters starting from the second position of string t is I
```

### Inserting/deleting a character (string)

`insert(index,count,ch)` and `insert(index,str)` are relatively common insertion functions. They respectively represent inserting the string `ch` `count` times consecutively at `index` and inserting the string `str`.

The `erase(index,count)` function deletes `count` characters starting from position `index` of the string (inclusive) (if no argument is passed to `count`, it means deleting all characters at and after position `index`).

Example:

```cpp
string s = "OI Wiki", t = " Wiki";
char u = '!';
s.erase(2);
printf("The string obtained after deleting all characters starting from the third position of string s is %s\n", s.c_str());
s.insert(2, t);
printf("The string obtained after inserting the string t at the third position of string s is %s\n", s.c_str());
s.insert(7, 3, u);
printf("The string obtained after consecutively inserting the string u 3 times at the eighth position of string s is %s",
       s.c_str());
```

Output:

```text
The string obtained after deleting all characters starting from the third position of string s is OI
The string obtained after inserting the string t at the third position of string s is OI Wiki
The string obtained after consecutively inserting the string u 3 times at the eighth position of string s is OI Wiki!!!
```

### Replacing a character (string)

`replace(pos,count,str)` and `replace(first,last,str)` are relatively common replacement functions. They respectively represent replacing the substring of `count` characters starting from position `pos` with `str` and replacing the substring starting at `first` (inclusive) and ending at `last` (exclusive) with `str`, where `first` and `last` are both iterators.

Example:

```cpp
string s = "OI Wiki";
s.replace(2, 5, "");
printf("The string obtained after replacing positions 3~7 of string s with the empty string is %s\n", s.c_str());
s.replace(s.begin(), s.begin() + 2, "NOI");
printf("The string obtained after replacing the first two positions of string s with NOI is %s", s.c_str());
```

Output:

```text
The string obtained after replacing positions 3~7 of string s with the empty string is OI
The string obtained after replacing the first two positions of string s with NOI is NOI
```

## References and notes

[^string1]: [C++ standard draft \[basic.string\]](https://eel.is/c++draft/basic.string#general-3)
