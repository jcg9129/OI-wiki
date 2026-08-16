author: Ir1d, cqnuljs, akakw1, MingqiHuang, Chrogeek, henrytbtrue, Planet6174, StudyingFather

## The concept of a file

A file is a collection of related data gathered together according to a specific purpose. C/C++ regards each file as an ordered byte stream, and each file ends with an **end-of-file marker** (EOF); if you want to operate on a file, the program should first open the file, and each time a file is opened (please remember to close the opened file), this file is associated with a stream, where the stream is actually a byte sequence.

C/C++ divides files into text files and binary files. A text file is a simple text file (key point); in addition, a binary file is a special-format file or an executable code file, etc.

## Steps for operating on a file

1. Open the file, point the file pointer to the file, and decide the type of file to open;  
2. Perform read and write operations on the file (the operations mainly used in competitions; some other operations are not written for now);  
3. After finishing using the file, close the file.

## The `freopen` function

### Function introduction

The function is used to redirect a specified input/output stream to a file in a specified way; it is contained in the header file `stdio.h (cstdio)`. This function can change the input/output environment without changing the original appearance of the code, but when using it, we should ensure that the stream is reliable.

The function mainly has three ways: read, write, and append.

### Command format

```cpp
FILE* freopen(const char* filename, const char* mode, FILE* stream);
```

### Parameter explanation

-   `filename`: the name of the file to open
-   `mode`: the mode of opening the file, indicating the file access permission
-   `stream`: the file pointer, usually using a standard file stream (`stdin/stdout`) or the standard error output stream (`stderr`)
-   Return value: the file pointer, pointing to the opened file

### File opening formats (optional reading)

-   `r`: open the file in read-only mode, the file must exist, only allows reading data **(commonly used)**
-   `r+`: open the file in read/write mode, the file must exist, allows reading/writing data
-   `rb`: open a binary file in read-only mode, the file must exist, only allows reading data
-   `rb+`: open a binary file in read/write mode, the file must exist, allows reading/writing data
-   `rt+`: open a text file in read/write mode, allows reading/writing data
-   `w`: open the file in write-only mode, if the file does not exist a new file is created, otherwise the content is cleared, only allows writing data **(commonly used)**
-   `w+`: open the file in read/write mode, if the file does not exist a new file is created, otherwise the content is cleared, allows reading/writing data
-   `wb`: open a binary file in write-only mode, if the file does not exist a new file is created, otherwise the content is cleared, only allows writing data
-   `wb+`: open a binary file in read/write mode, if the file does not exist a new file is created, otherwise the content is cleared, allows reading/writing data
-   `a`: open the file in write-only mode, if the file does not exist a new file is created, the written data will be appended at the end of the file (the EOF marker is retained)
-   `a+`: open the file in read/write mode, if the file does not exist a new file is created, the written data will be appended at the end of the file (the EOF marker is not retained)
-   `at+`: open a text file in read/write mode, the written data will be appended at the end of the file
-   `ab+`: open a binary file in read/write mode, the written data will be appended at the end of the file

### Usage

Read file content:

```cpp
freopen("data.in", "r", stdin);
// data.in is the name of the file to read; it should be placed in the same directory as the executable file
```

Output to a file:

```cpp
freopen("data.out", "w", stdout);
// data.out is the file name of the output file, in the same directory as the executable file
```

Close the standard input/output stream

```cpp
fclose(stdin);
fclose(stdout);
```

??? note "Note"
    Functions such as `printf/scanf/cin/cout` use `stdin/stdout` by default; after redirecting `stdin/stdout`, these functions will input/output to the redirected file.

### Template

```cpp
#include <cstdio>
#include <iostream>

int main(void) {
  freopen("data.in", "r", stdin);
  freopen("data.out", "w", stdout);
  /*
  the code in between does not need to change; just directly use cin and cout
  */
  fclose(stdin);
  fclose(stdout);
  return 0;
}
```

## The `fopen` function (optional reading)

The function is roughly the same as `freopen`; the function will open the specified file and return a pointer to the opened file.

### Function prototype

```cpp
FILE* fopen(const char* path, const char* mode)
```

The meanings of the parameters are the same as `freopen`.

### Available read/write functions (basic)

-   `fread/fwrite`
-   `fgetc/fputc`
-   `fscanf/fprintf`
-   `fgets/fputs`

### Usage

```cpp
FILE *in, *out;  // define file pointers
in = fopen("data.in", "r");
out = fopen("data.out", "w");
/*
do what you want to do
*/
fclose(in);
fclose(out);
```

## C++'s `ifstream/ofstream` file input/output streams

### Usage

Read file content:

```cpp
ifstream fin("data.in");
// data.in is the relative or absolute location of the file to read
```

Output to a file:

```cpp
ofstream fout("data.out");
// data.out is the relative or absolute location of the output file
```

Close the standard input/output stream

```cpp
fin.close();
fout.close();
```

### Template

```cpp
#include <fstream>
using namespace std;  // both types are in the std namespace

ifstream fin("data.in");
ofstream fout("data.out");

int main(void) {
  /*
  in the code in between, just change cin to fin and cout to fout
  */
  fin.close();
  fout.close();
  return 0;
}
```

## References

1.  Informatics Olympiad Complete Guide
