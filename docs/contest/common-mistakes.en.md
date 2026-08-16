author: Estrella-Explore, H-J-Granger, orzAtalod, ksyx, Ir1d, Chrogeek, Enter-tainer, yiyangit, shuzhouliu, broken-paint, CarvingAn

This page mainly lists some mistakes that many people frequently make in contests.

## Errors caused by different environments

-   Using the `%I64d` format specifier with `scanf` or `printf` may cause input/output format errors under Linux.

## Errors that cause CE

These errors are mostly lexical, syntactic, and semantic errors; their causes are relatively simple, and the difficulty of fixing them is low.

Examples:

-   Spelling errors such as writing `int main()` as `int mian()`.

-   Forgetting to write the semicolon after finishing a `struct` or `class`.

-   Declaring an array too large, using an illegal function (such as multithreading) (on an OJ), or declaring but not defining a function—these cause link errors.

-   Mismatched function argument types.

    -   Example: passing one `int`-type argument and one `long long`-type argument when using the `max` function from the `<algorithm>` header.

        ```cpp
        // query is a custom function that returns long long
        printf("%lld\n", max(0, query(1, 1, n, l, r));

        // error    no instance of overloaded function "std::max" matches the argument list
        ```

-   Skipping the initialization of some local variables when using `goto` and `switch-case`.

## Errors that do not cause CE but cause a Warning

Programs written with these errors can pass compilation, but will most likely produce wrong runtime results. These errors are pointed out by the compiler when compiling with the `-W{warningtype}` parameter.

-   Confusing the assignment operator `=` with the comparison operator `==`.

    -   Example:

        ```cpp
        std::srand(std::time(nullptr));
        int n = std::rand();
        if (n = 1)
          printf("Yes");
        else
          printf("No");

        // no matter what random value n gets, the output is definitely Yes
        // warning    incorrect operator: constant assignment performed in a Boolean context. Consider using "==" instead.
        ```

    -   If you really want to use `=` in a statement where `==` should be used (such as `while (foo = bar)`) but do not want to receive the Warning, you can use **double parentheses**: `while ((foo = bar))`.

-   Errors caused by operator precedence.

    -   Example:

        ```cpp
        // wrong
        // std::cout << (1 << 1 + 1);
        // correct
        std::cout << ((1 << 1) + 1);

        // warning    "<<": check operator precedence for a possible error; use parentheses to clarify precedence
        ```

-   Using the `static` modifier incorrectly.

-   Not adding the address-of operator `&` when reading with `scanf`.

-   Argument types not matching the format specifiers when using `scanf` or `printf`.

-   Using bit operations and the logical operator `==` together without adding parentheses.
    -   Example: `(x >> j) & 3 == 2`

-   `int` literal overflow.

    -   Example: `long long x = 0x7f7f7f7f7f7f7f7f`, `1<<62`.

-   Uninitialized local variables.

    ???+ note "What happens with an uninitialized variable"
        Original: <https://loj.ac/d/3679> by @hly1204
        
        For example, if we declare an `int a;` in C++ without initializing it, one may sometimes think `a` is a "random" (in fact possibly not truly random) value, or one may think it is a fixed value, but that is actually not the case.
        
        In simple test code
        
        <https://wandbox.org/permlink/T2uiVe4n9Hg4EyWT>
        
        the code is:
        
        ```cpp
        #include <iostream>
        
        int main() {
          int a;
          std::cout << std::boolalpha << (a < 0 || a == 0 || a > 0);
          return 0;
        }
        ```
        
        With optimization enabled on some compilers and environments, its output is false.
        
        If you are interested, you can read <https://www.ralfj.de/blog/2019/07/14/uninit.html>; although it experiments with Rust, the essence is the same.

-   A local variable having the same name as a global variable, causing the global variable to be accidentally shadowed. (Enabling `-Wshadow` can check for this kind of error.)

-   Output errors caused by operator overloading.
    -   Example:

        ```cpp
        // intention: the first << is the overloaded operator, meaning output; the second << is the
        // shift operator, meaning shifting 1 left by 1 bit. But because parentheses were forgotten, the
        // compiler treats the second << as an output operator too, leading to output different from
        // expected. wrong: std::cout << 1 << 1; correct:
        std::cout << (1 << 1);
        ```

## Errors that cause neither CE nor a Warning

These errors cannot be found by the compiler and can only be discovered by oneself.

### Errors that cause WA

-   Not clearing arrays after processing one dataset and before reading the next.

-   Input optimization not handling negative numbers.

-   The bit width of the data type used is insufficient, causing overflow.
    -   Such as the scenario described by the saying "Three years of OI come to nothing; forget `long long` and meet your ancestors." A contestant loses points because they did not use `long long` in the right place (defining an integer as `long long`), leading to a wrong answer.

-   When storing a graph, node numbering starts from 0, but the two endpoints of the edges given in the problem are numbered from 1, and forgetting to subtract 1 when reading.

-   Typing the greater-than/less-than sign wrong or reversed.

-   Mixing the two kinds of IO, `scanf/printf` and `std::cin/std::cout`, after executing `ios::sync_with_stdio(false);`, causing input/output to be jumbled.

    -   Example:

        ```cpp
        // this example illustrates the consequence of mixing the two IO methods after turning off
        // synchronization with stdio
        // it is recommended to single-step through it to observe the effect
        #include <cstdio>
        #include <iostream>

        int main() {
          // after turning off synchronization, cin/cout use independent buffers instead of
          // synchronizing output to the scanf/printf buffer, thereby reducing IO time
          std::ios::sync_with_stdio(false);
          // under cout, when using '\n' for a newline, content is buffered and not output immediately
          std::cout << "a\n";
          // printf's '\n' flushes printf's buffer, causing the output to be misaligned
          printf("b\n");
          std::cout << "c\n";
          // cout's buffer is only output when the program ends
          return 0;
        }
        ```

-   Errors caused by macro expansion without adding parentheses.

    -   Example: the value returned by this macro is not $4^2 = 16$ but $2+2\times 2+2 = 8$.

        ```cpp
        #define square(x) x* x
        printf("%d", square(2 + 2));
        ```

-   Computation errors caused by not using `unsigned` when hashing.
    -   The right-shift operation on a negative number fills the highest bit with 1. See: [bitwise operators](../lang/op.md#bit-operators).

-   Not deleting or commenting out debug-output statements.

-   Accidentally adding a `;`.

    -   Example:

        ```cpp
        /* clang-format off */
        while (1);
            printf("OI Wiki!\n");
        ```

-   Setting a sentinel value incorrectly. For example, the `0` node of a balanced tree.

-   When using `:` to initialize variables in a class or struct constructor, the declaration order of the variables does not match the dependency relationship at initialization time.

    -   The initialization order of member variables is related to the order in which they are declared in the class, not to the order in the initializer list. See: the "Initialization order" section of [Constructors and member initializer lists](https://zh.cppreference.com/w/cpp/language/constructor).
    -   Example:

        ```cpp
        #include <iostream>

        class Foo {
         public:
          int a, b;

          // a will be initialized before b, so its value is indeterminate
          Foo(int x) : b(x), a(b + 1) {}
        };

        int main() {
          Foo bar(1, 2);
          std::cout << bar.a << ' ' << bar.b;
        }

        // possible output: -858993459 1
        ```

-   Not merging the ancestors of the two elements when merging sets in a disjoint-set union.

    -   Example:

        ```cpp
        f[a] = b;              // wrong
        f[find(a)] = find(b);  // correct
        ```

-   Using `a` (append) for writing with `freopen`.
    -   CCF's judging environment does not clear the output file; using `a` causes the previous contestant's output to also be read by the judge, triggering WA.

#### Different newline characters

???+ warning "Warning"
    In an official contest, effort is made to ensure that the environment in which contestants answer is the same as the final testing environment.
    
    The content of this section only applies to situations such as mock contests, and we also recommend that problem setters make the data conform to the [data format](problemsetting.md#data-format) as much as possible.

Different operating systems use different symbols to mark line breaks; the following are the newline characters of several commonly used systems:

-   LF (denoted by `\n`): `Unix` or `Unix`-compatible systems

-   CR+LF (denoted by `\r\n`): `Windows`

-   CR (denoted by `\r`): `Mac OS` version 9 and earlier

C/C++ uses the escape sequence `\n` for a line break, which may lead us to think that the newline character in the input must also be represented by `\n`, and to read only one character to represent the newline character, causing us not to fully read the input file.

The following are solutions:

-   Call `getchar()` multiple times until the desired character is read.

-   Read with `cin`, **which may increase the code's constant factor**.

-   Use `scanf("%s",str)` to read a string, then take `str[0]` as the read character.

-   Use `scanf(" %c",&c)` to filter out all whitespace characters.

### Errors that cause unknown results

Undefined behavior leads to unknown results, which may be WA, RE, etc. The compiler usually assumes your program has no undefined behavior, hence the situation where the code behaves inconsistently with and without O2.

-   Dividing by 0 (finding the inverse of 0).

    ???+ warning "Example"
        ```cpp
        cout << x / 0 << endl;
        ```

-   Array (index) out of bounds.

    For example:

    -   Not setting the loop's initial value correctly, causing access to the value at index -1.

    -   Not making the edge table of an undirected graph twice as large.

    -   Not allocating 4 times the space for a segment tree.

    -   Misreading the data range and typing one fewer zero.

    -   Wrongly estimating the algorithm's space complexity.

    -   When writing a segment tree, `pushup` or `pushdown` on a leaf node.

        The correct approach: do not go out of bounds; remember to check your code so that the index `x` accessed is within the defined index range.

-   A function with a return value (other than main) executes to the end without executing any return statement.

    Even if one branch has a return value while other branches do not, the result is undefined.

    You can append `-Wall` to the compilation options to check whether the compiler gives a warning about a function not returning.

-   Attempting to modify a string literal.

    ???+ warning "Example"
        ```cpp
        char *p = "OI-wiki";
        p[0] = 'o';
        p[1] = 'i';
        ```

    Attempting to modify a string literal this way causes **undefined behavior**; you should use another **appropriate** data type, such as `std::string` and `char[]`.

-   Freeing/illegally dereferencing a block of memory multiple times.

    For example:

    -   Dereferencing a pointer before initializing it.

    -   The memory region the pointer points to has already been freed.

        When using `erase`, `delete`, or `free`, be careful not to use them multiple times on the same address/object.

-   Attempting to free part of a whole block of memory allocated by `new []`.

    For example:

    ```cpp
    object *pool = new object[POOL_SIZE];

    object *pointer = pool + 10;

    // error!
    delete pointer;
    ```

    Commonly seen when, after preallocating a whole block of memory using a memory pool, one attempts to use `delete` or `free()` to free a single object obtained from the memory pool.

-   Dereferencing a null pointer / wild pointer.

    For a null pointer: you should first check for a null pointer, which can be done with `p == nullptr` or `!p`.

    For a wild pointer: you can set the pointer to `nullptr` when freeing it to avoid this.

-   Signed-number overflow.

    For example, we have an expression `x+1 > x`.

    The normal output should be `true`, but when `INT_MAX` is used as `x` the output is `false`; this is called `signed integer overflow`.

    You can use a larger data type (such as `long long` or `__int128`), or check for overflow. If no negative numbers are guaranteed, you can also use an unsigned integer type.

    Signed-integer overflow may affect compiler optimization; for example, the code:

    ```cpp
    int foo(int x) {
      if (x > x + 1) return 1;
      return 0;
    }
    ```

    may be directly optimized by the compiler into:

    ```cpp
    int foo(int x) { return 0; }
    ```

    because the compiler can assume that signed integers never overflow, so `x > x + 1` never holds.

-   Using an uninitialized variable.

    ???+ warning "Example"
        ```cpp
        int foo(int a) {
          int t; /* not initialized */
          if (/* use */ t > 3) return a;
          return 0;
        }
        ```

### Errors that cause RE

-   Not removing file operations (on some OJs).

-   Errors in the comparison function when sorting. `std::sort` requires the comparison function to be a strict weak ordering: `a<a` is `false`; if `a<b` is `true`, then `b<a` is `false`; if `a<b` is `true` and `b<c` is `true`, then `a<c` is `true`. Pay special attention to the second point.
    If the above requirements are not met, sorting will very likely RE.
    For example, when writing the parity sorting for Mo's algorithm, writing it like this is wrong:

    ```cpp
    bool operator<(const int a, const int b) {
      if (block[a.l] == block[b.l])
        return (block[a.l] & 1) ^ (a.r < b.r);
      else
        return block[a.l] < block[b.l];
    }
    ```

    In the above code, `(block[a.l]&1)^(a.r<b.r)` does not satisfy the second point of the requirements.
    Changing it to this is correct:

    ```cpp
    bool operator<(const int a, const int b) {
      if (block[a.l] == block[b.l])
        // wrong: does not satisfy the strict-weak-ordering requirement
        // return (block[a.l] & 1) ^ (a.r < b.r);
        // correct
        return (block[a.l] & 1) ? (a.r < b.r) : (a.r > b.r);
      else
        return block[a.l] < block[b.l];
    }
    ```

-   Insufficient stack space under Windows, causing a stack overflow; Windows sends the program a SIGSEGV signal, the program terminates and returns 3221225725 (i.e. 0xC00000FD, defined by NTSTATUS as `STATUS_STACK_OVERFLOW`).  
    If you use the gcc compiler, you can add the command `-Wl,--stack=SIZE` at compile time to specify the stack-space size limit, where `SIZE` is the stack-space size in bytes.

    Insufficient stack space under Linux, causing a stack overflow; Linux scribbles `head_info` around the stack heap, an operation that in the vast majority of cases causes the program to exit immediately, displaying words like `segmentation fault (core dumped)`.  
    You can use `ulimit -s SIZE` in the terminal to modify the current terminal's stack-space limit, where `SIZE` is the stack-space size in kilobytes (KB).  
    **Note that if you set the stack-space limit too large, infinite recursion may make the recursion stack too large and cause the system to crash.**

### Errors that cause TLE

-   Divide and conquer not checking the boundary, causing infinite recursion.

-   Infinite loops.

    -   Loop variable name collision.

    -   The loop direction is reversed.

-   Not marking whether a state has been visited during BFS.

-   Writing min/max using macro expansion.

    This kind of error greatly increases the program's running time and may even directly affect the code's time complexity. It is especially common when beginners write segment trees.

    A common wrong way to write it is:

    ```cpp
    #define Min(x, y) ((x) < (y) ? (x) : (y))
    #define Max(x, y) ((x) > (y) ? (x) : (y))
    ```

    Although there is no problem with correctness written this way, if you directly take the max of function return values, such as `a = Max(func1(), func2())`, and these functions take a long time to run, it will greatly affect the program's performance, because after macro expansion it is of the form `a = func1() > func2() ? func1() : func2()`, calling the function three times, one more than a normal max function. Note that if `func1()` returns a different answer each time, this way of writing `max` will also produce errors—for example, when `func1()` is `return ++a;` and `a` is a global variable.

    Example: the following code can be adversarially made $\Theta(n)$ per query, causing TLE.

    ```cpp
    #define max(x, y) ((x) > (y) ? (x) : (y))

    int query(int t, int l, int r, int ql, int qr) {
      if (ql <= l && qr >= r) {
        ++ti[t];  // record the node visit count for convenient debugging
        return vi[t];
      }

      int mid = (l + r) >> 1;
      if (mid >= qr) return query(lt(t), l, mid, ql, qr);
      if (mid < ql) return query(rt(t), mid + 1, r, ql, qr);
      return max(query(lt(t), l, mid, ql, qr), query(rt(t), mid + 1, r, ql, qr));
    }
    ```

-   Appending a character to a `std::string`-class string using the + operator.

    This kind of error creates a temporary `string` variable, and after modification assigns it back to the original variable. This kind of error cannot be optimized by the compiler, and may cause the time complexity to degrade when the data volume is large.

    Common wrong way to write it:

    ```cpp
    std::string a;
    char b = 'c';
    a = a + b;
    ```

    When this code executes, the program first creates a temporary `string` variable, then stores the value of `a` into the temporary variable, then adds the value of `b` at the end, and finally stores it back into `a`.

    From the [assembly result](https://godbolt.org/z/Eo9vn7or5), you can see that `a = a + b` calls three features of `std::__cxx11::basic_string`, namely `operator+`, `operator=`, and variable creation.

    The correct way to write it should be:

    ```cpp
    std::string a;
    char b = 'c';
    a += b;
    ```

    [This way of writing it](https://godbolt.org/z/eGh33Grf3) directly appends the character `b` to the string `a`, calling only `operator+=` once. For a more detailed performance comparison, refer to the [Benchmark](https://quick-bench.com/q/JNDGl7HgOszNG-bo7AgVc42owv4).

-   Not removing file operations (on some OJs).

-   Repeatedly executing a function whose complexity is not $O(1)$ inside a `for/while` loop. Strictly speaking, this may cause a change in time complexity.

-   Errors in the midpoint formula or termination condition when doing binary search.

### Errors that cause MLE

-   The array is too large.

    ??? note "Detailed explanation of memory-usage metrics under Linux"
        > TL;DR: If you declare a particularly large global static array during a CCF-series exam, you need to be especially careful. Because arrays declared by the program are all counted in memory usage (unlike most online judging platforms, which only count the actually-used part), in some cases this may even cause the entire problem to MLE.
        
        -   About RSS and VSZ[^ref1][^ref2]
        
            1.  VSZ (Virtual Memory Size)[^ref3]
        
                VSZ denotes the process's **virtual memory size**, the total size of the virtual address space the process can access, usually displayed in KB.
        
                Virtual memory is a logical concept and is usually much larger than the actual memory usage.
        
                Under Linux you can use the `top` command to view the composition of a process's memory usage, where the `VIRT` column represents the virtual memory it occupies.
        
                Virtual memory generally includes the address space allocated but not actually used by the process; in short, however much is requested, the virtual memory is roughly that much.
        
                Note in particular that commonly used online judging platforms usually only count physical memory usage. But **CCF's judging environment counts virtual memory**, which means that if you declare a global static large array, even if only a small part of it is used, it will occupy a large amount of space.
            2.  RSS (Resident Set Size)[^ref4]
        
                RSS denotes the **physical memory size** actually occupied by the process, i.e. the size of the page frames resident in RAM, usually displayed in KB.
        
                Likewise, you can use `top` to view a process's physical memory in the `RES` column.
        
                RSS generally includes only the part actually loaded into physical memory; that is, however much is actually used is how much it is.
        -   Analysis of memory-usage behavior
        
            Suppose the following array is declared:
        
            ```cpp
            const int SIZE = 1e8;
            int arr[SIZE];  // space occupied: 4 bytes * 100 million = 400 MB
            ```
        
            This is a static array allocated in the global data segment. This array is not explicitly initialized, so it is usually allocated in the BSS segment (if explicitly initialized (such as all 0 or another value), it is allocated in the DATA segment).
        
            -   When the array is completely unused (assuming the compiler does not optimize it away)
        
                -   Physical memory: if the array is not accessed, the demand-paging mechanism means the memory pages are not yet loaded into physical memory. Physical memory does not increase, or increases only slightly (a few metadata pages may be loaded).
                -   Virtual memory: the size of the array is counted in virtual memory (increasing by `400MB`), because the entire array's virtual address space has been allocated.
            -   When the array is partially used
        
                Suppose only a small part of the array's elements are used, for example:
        
                ```cpp
                arr[0] = 1;
                arr[999999] = 2;
                ```
        
                -   Virtual memory: virtual memory does not change, still `400MB`.
                -   Physical memory: each time an element of the array is accessed, the corresponding virtual page is loaded into physical memory. Assuming the system page size is `4KB`, each page contains $4 \text{KB} ÷ 4 \text{B} = 1024$ `int` elements. Accessing the array twice may load 2 pages, i.e. increasing physical memory by about $2 \times 4 \text{KB} = 8 \text{KB}$.
            -   When the array is used for the most part
        
                Suppose the first $50,000,000$ elements of the array are assigned:
        
                ```cpp
                for (int i = 0; i < 50000000; ++i) {
                  arr[i] = i;
                }
                ```
        
                -   Virtual memory (VSZ): VSZ is still `400MB` and does not change.
                -   Physical memory (RSS): this is contiguous access (the $50,000,000$ accessed elements are adjacent in memory address), and the number of pages that need to be loaded is $\left\lceil \dfrac{50,000,000}{1024} \right\rceil = 48,828$ pages.
        
                    Assuming each page is `4KB`, the total is $48,828 \times 4 \text{KB} \approx 190 \text{MB}$, so physical memory increases to about `190MB`.
        
                    Note: if the indices are random when assigning to the array, the physical memory usage will differ greatly from the prediction (because page loading is based on address, so random assignment loads a large number of memory pages).
        
                Brief summary: as the proportion of the accessed part increases, physical memory approaches virtual memory (assuming no page reclamation occurs).
-   Inserting too many elements into an STL container.

    -   This is often an infinite loop inside a loop that inserts elements into the STL.

    -   It may also be adversarially exploited.

### Errors that cause an excessive constant factor

-   Not defining the modulus as a constant when defining it.

    -   Example:

        ```cpp
        // int mod = 998244353;      // wrong
        const int mod = 998244353;  // correct, makes it convenient for the compiler to treat it as a constant
        ```

-   Using unnecessary recursion (tail recursion excepted).

-   Introducing a large amount of extra computation when converting recursion into iteration.

### Errors that only have an effect when the program runs locally

-   Errors that may occur with file operations:

    -   Not closing the file pointer with `fclose(fp)` during diff-testing before setting `fp = fopen()` again. This causes the process to have a large number of dangling file pointers.

    -   Not adding `.in`/`.out` to the file name in `freopen()`.

-   Forgetting to `delete` or `free` after using heap space.

## References and notes

[^ref1]: [What is RSS and VSZ in Linux memory management - Stack Overflow](https://stackoverflow.com/questions/7880784/what-is-rss-and-vsz-in-linux-memory-management)

[^ref2]: [Need explanation on Resident Set Size/Virtual Size - Stack Overflow](https://unix.stackexchange.com/questions/35129/need-explanation-on-resident-set-size-virtual-size)

[^ref3]: [Virtual memory](https://zh.wikipedia.org/wiki/%E8%99%9A%E6%8B%9F%E5%86%85%E5%AD%98)

[^ref4]: [Resident set size](https://zh.wikipedia.org/wiki/%E5%B8%B8%E9%A9%BB%E9%9B%86%E5%A4%A7%E5%B0%8F)
