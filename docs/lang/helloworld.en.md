disqus:

## Environment configuration

If a worker wants to do his work well, he must first sharpen his tools.

### Integrated development environment

An IDE is relatively simple to operate; generally, beginner players choose an IDE to write code. The most common one in competitions is [Dev-C++](../tools/editor/devcpp.md) (if the exam environment is a Windows system, this IDE is generally also provided).

### Compiler

#### Windows

It is recommended to use the GNU compiler. You need to go to [MinGW Distro](https://nuwen.net/mingw.html) to download MinGW and install it. In addition, under Windows you can also choose the [Microsoft Visual C++ compiler](https://docs.microsoft.com/en-us/cpp/build/projects-and-build-systems-cpp); you need to go to the [Visual Studio page](https://visualstudio.microsoft.com/downloads/#build-tools-for-visual-studio-2019) to download and install it.

#### macOS

Execute in the terminal:

```bash
xcode-select --install
```

#### Linux

Use `g++ -v` to check whether `g++` has been installed.

You can install it with the following command:

```bash
sudo apt update && sudo apt install g++
```

#### Compiling code on the command line

After becoming proficient, some players will also use the more flexible command line to compile code, so that they do not depend on an IDE, but use their own familiar text editor to write code.

```bash
g++ test.cpp -o test -lm
```

`g++` is the compiler for the C++ language (the compiler for the C language is `gcc`), `-o` is used to specify the file name of the executable file, and the compilation option `-lm` is used to link the math library `libm`, so that code using `math.h` can compile and run normally.

Note: C++ programs can compile and run normally without `-lm`. The C++ compilation options of past NOI/NOIP exam questions all carry `-lm`, so it is added here as well.

## The first piece of code

Let us begin the journey of getting started with C++ through such an example program~

Note: Please pay attention to turning on the English input method before writing.

C++ language

```cpp
#include <iostream>  // include the header file

int main() {                     // define the main function
  std::cout << "Hello, world!";  // use the cout function in the standard namespace
  return 0;  // return 0, ending the main function. The compiler generally adds this line automatically, and it can generally be omitted
}
```

C language

```c
#include <stdio.h>  // include the header file

int main() {                // define the main function
  printf("Hello, world!");  // output Hello, world!
  return 0;                 // return 0, ending the main function
}
```

Note: The C language is only for reference here; C++ is basically compatible with the C language, and has many new features that can make contestants get twice the result with half the effort on the field. For details, see [Differences between C++ and other commonly used languages](./cpp-other-langs.md)
