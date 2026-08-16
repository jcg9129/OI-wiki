author: inclyc

The commonly used programming language in the OI community is C++. Since we use this language, we are destined to deal with the compiler and the language standard. As is well known, C++ is very chaotic and evil; this article aims to give practical compiler-related knowledge, sufficient for competition use.

## Introduction to compiler optimization

### What is optimization (Optimization)

According to the [as-if rule](https://en.cppreference.com/w/cpp/language/as_if) (The as-if Rule), improvements are made to the program's running speed and the size of the program executable file while keeping the semantics unchanged.

<!-- ### 开优化的比赛有哪些？ -->

<!-- TODO: 开 O2 的比赛 -->

## Common compiler optimizations

### Constant folding (Constant Folding)

Constant folding, also called constant propagation (Constant Propagation): if an expression can be determined to be a constant, then before its next definition (Definition), constant propagation can be performed.

```cpp
int x = 1;
int y = x;  // x = 1, => y = 1
x = 3;
int z = 2 * y;   // z => 2 * y = 2 * 1 = 2
int y2 = x * 2;  // x = 3, => y2 = 6
```

This piece of code can be converted at compile time into:

```cpp
int x = 1;
int y = 1;
x = 3;
int z = 2;
int y2 = 6;
```

Example: <https://godbolt.org/z/oEfY35TTd>

### Dead code elimination (Deadcode Elimination)

As the name implies, it means that a piece of code that is not used will be deleted.

```cpp
int test() {
  int a = 233;
  int b = a * 2;
  int c = 234;
  return c;
}
```

Will be converted to

```cpp
int test() { return 234; }
```

Note that this code first performs constant folding, so that the return value can be determined to be 234, and a, b are inactive variables, so they are deleted.

### Loop rotate (Loop Rotate)

Convert a loop from the "for" form to the "do-while" form, with an additional condition judgment in front. This transformation mainly prepares for other transformations.

```cpp
for (int i = 0; i < n; ++i) {
  auto v = *p;
  use(v);
}
```

Transformed into

```cpp
if (0 < n) {
  do {
    auto v = *p;
    use(v);
    ++i;
  } while (i < n);
}
```

### Loop invariant code motion (Loop Invariant Code Motion)

Based on alias analysis (Alias Analysis), code in the loop that is proved to be invariant (may contain memory access, load/store, so it depends on alias analysis) is moved out of the loop body, so that there is less code inside the loop body.

```cpp
for (int i = 0; i < n; ++i) {
  auto v = *p;
  use(v);
}
```

This code, intuitively, can be hoisted to:

```cpp
auto v = *p;
for (int i = 0; i < n; ++i) {
  use(v);
}
```

But in fact, if `n <= 0`, this loop will never be entered, but we execute one extra instruction (which may have side effects!). Therefore, the loop is usually rotated to the do-while form, so that it is convenient to insert a "loop guard". After that, loop invariant code motion is performed.

```cpp
if (0 < n) {  // loop guard
  auto v = *p;
  do {
    use(v);
    ++i;
  } while (i < n);
}
```

### Loop unroll (Loop Unroll)

A loop contains the loop body and various branch statements, requiring modern CPUs to perform certain branch prediction. Directly unroll the loop, exchanging a certain amount of code size for running time.

```cpp
for (int i = 0; i < 3; i++) {
  a[i] = i;
}
```

Transformed into:

```cpp
a[0] = 0;
a[1] = 1;
a[2] = 2;
```

### Loop unswitching (Loop Unswitching)

Loop unswitching moves the conditional expression in the loop outside the loop, then places two loops in each of the two external conditions, which can increase the possibility of loop vectorization and parallelization (usually simple loops are more easily vectorized).

```cpp
// clang-format off
void before(int x) {
  for(;/* i in some range */;) {
    /* A */;
    if (/* condition */ x % 2) {
      /* B */;
    }
    /* C */;
  }
}

void after(int x) {
  if (/* condition */ x % 2) {
    for(;/* i in some range */;) {
      /* A */;
      /* B */; // directly execute B, without the loop judgment
      /* C */;
    }
  } else {
     for(;/* i in some range */;) {
      /* A */; 
               // do not execute B
      /* C */;
    }
  }
}
```

### Code layout optimizations (Code Layout Optimizations)

When a program executes, the executed paths can be divided into cold and hot paths (cold/hot path). CPU jump execution, in the vast majority of cases, is not as fast as direct sequential execution; the latter is usually called "fallthrough" by compiler authors. Correspondingly, code that is frequently executed is called hot code, and the opposite is called cold code. In OI code, if there is a section that is a special-case boundary condition in a loop, or exception handling, or similar logic, then this part of the code is cold code.

A basic block (Basic Block) is the basic structure of control flow; a procedure (Procedure) is composed of several basic blocks, forming a directed graph. In the process of generating an executable file, the compiler needs to arrange a layout for placing the basic blocks (Layout), and how to arrange the layout is the focus of this optimization.

In principle, we should prefer to place hot code together and separate cold code. The reason is that this can better utilize the instruction cache, and the locality of hot code will be better.

```cpp
// clang-format off
int hotpath; // <-- hot!
if (/* boundary condition */ false) {
    // <-- cold!
}
int hotpath_again;  // <-- hot!
```

#### Basic block placement (Basic Block Placement)

We use labels to express a kind of "pseudo machine code"; this C++ program has two ways of translation:

???+ note "Layout 1"
    ```cpp
    // clang-format off
    hotblock1:
        Stmts; // <-- hot!
        if (/* boundary condition does not hold */ true)
            goto hotblock2; // happens frequently! ------+
    coldblock:                           /*   |   */
        Stmt; // <- cold                      |
        Stmt; // <- cold                      |
        Stmt; // <- cold                      |  crosses a large number of instructions, expensive!
        Stmt; // <- cold                      |
        Stmt; // <- cold                      |
        Stmt; // <- cold                      |
        Stmt; // <- cold                      |
    hotblock2:                          /*    |   */
        Stmts; // <- hot!           <----------+
    ```

Another layout is:

???+ note "Layout 2"
    ```cpp
    // clang-format off
    hotblock1:
        Stmts; // <-- hot!
        if (/* boundary condition */ false)
            goto coldblock; // rarely happens
    hotblock2:                         /*   |  low cost!  */
        Stmts; // <- hot!  <-----------------+
    coldblock:
        Stmt; // <- cold
        Stmt; // <- cold
        Stmt; // <- cold
        Stmt; // <- cold
        Stmt; // <- cold
    ```

We see that in the latter layout, the two hot code blocks are placed together, and the execution efficiency is better.

To tell the compiler whether a branch is easily executed, we can use C++20 `[[likely]]` and `[[unlikely]]`: <https://en.cppreference.com/w/cpp/language/attributes/likely>

If the competition does not adopt a standard above C++20, then we can use `__builtin_expect` (GNU Extension).

```cpp
#define likely(x) __builtin_expect(!!(x), 1)
#define unlikely(x) __builtin_expect(!!(x), 0)

if (unlikely(/* some boundary condition check */ false)) {
  // cold code
}
```

#### Hot cold splitting (Hot Cold Splitting)

A procedure (Procedure) contains both cold and hot paths, and the cold code is relatively long; a better practice is to make the cold code a function call rather than blocking the hot path. This also reminds us not to be clever and make all functions `inline`. Cold code hinders execution speed much more than a function call.

???+ note "Bad code layout"
    ```cpp
    // clang-format off
    void foo() {
          // clang-format off
    hotblock1:
        Stmts; // <-- hot!
        if (/* boundary condition does not hold */ true)
            goto hotblock2; // happens frequently! ------+
    coldblock:                           /*   |   */
        Stmt; // <- cold                      |
        Stmt; // <- cold                      |
        Stmt; // <- cold                      |  crosses a large number of instructions, expensive!
        Stmt; // <- cold                      |
        Stmt; // <- cold                      |
        Stmt; // <- cold                      |
        Stmt; // <- cold                      |
    hotblock2:                          /*    |   */
        Stmts; // <- hot!           <----------+
    }
    ```

???+ note "Good code layout"
    ```cpp
    // clang-format off
    void foo() {
    hotblock1:
      Stmts;  // <-- hot!
      if (/* boundary condition */ false)
        coldBlock();  // separate out the cold code, making the hot path more cache-friendly
    hotblock2:
      Stmts;  // <- hot!
    }
    
    void coldBlock() {
      Stmt;  // <- cold
      Stmt;  // <- cold
      Stmt;  // <- cold
      Stmt;  // <- cold
      Stmt;  // <- cold
      Stmt;  // <- cold
      Stmt;  // <- cold
    }
    ```

Hot cold splitting is actually the reverse operation of function inlining (Function Inlining); the existence of this optimization suggests that function inlining does not necessarily make the program run faster. If the inlined code is even cold code, it will instead make the program run slower! Some compilers have a compilation option for forced inlining, but it is not recommended to use. The compiler internally has a static analysis process that computes the probability of each basic block and branch, as well as a cost model related to a function call, to decide whether to inline; deciding whether to inline yourself is not necessarily better than the compiler's decision.

In fact, without additional information, the compiler usually assumes that the probability of a branch jumping and not jumping is the same, and uses this as a basis to propagate the coldness/hotness of each control flow path. Part of PGO (Profile Guided Optimization) is to obtain the real-environment program branch probabilities through several performance tests and experiments; this information can make the code layout more excellent.

### Function inlining (Function Inlining)

A function call usually needs to pass parameters through registers and the stack, and both the caller and the callee need to save a certain register state; this process is usually called the calling convention. A function call therefore causes some time loss, and an inline function means writing the function directly in the caller procedure, without performing a real function call.

```cpp
int add(int x) { return x + 1; }

int foo() {
  int a = 1;
  a = add(a);
}
```

`add()` can be inlined into `foo()`:

```cpp
int foo() {
  int a = 1;
  a = a + 1;  // <-- the function body of add(), without parameter passing
}
```

#### `always_inline`, `__force_inline`

<https://clang.llvm.org/docs/AttributeReference.html#always-inline-force-inline>

Some compilers provide a way to manually inline function calls, adding `__attribute__((always_inline))` before the function. Using it this way is not necessarily faster than a function call; the compiler at this time trusts that the programmer has good enough judgment.

### Tail call optimization (Tail Call Optimization)

When a function call is located at the tail position of the function body, this kind of function call is called a tail call (Tail Call). For this special form of call, some special optimizations can be performed. The vast majority of architectures have a Frame Pointer (a.k.a FP) and a Stack Pointer (a.k.a SP), maintaining the call frame (Frame) of the function; and if the call is located at the tail of the function, then we can not retain the call record of the outer function, and directly replace it with the inner function.

#### Using jump instructions instead of function calls

Under the vast majority of architectures, a function call needs to save the current program counter `$pc` position, save several caller saved registers, in order to return to the scene. And a tail call does not need this process, and will be directly translated into a jump instruction, because tail recursion never returns to the position where the function ran.

A simple example: <https://godbolt.org/z/e7b1safaW>

```cpp
int test(int a);

int tailCall(int x) { return test(x); }
```

```nasm
tailCall(int):                           ; @tailCall(int)
        jmp     test(int)@PLT                    ; TAILCALL
```

#### Automatic tail recursion rewriting

If the tail call of a function is itself, then this function is tail-recursive. Broadly speaking, if indirect recursion (recursion jointly formed by two or more functions) forms recursion, and all are tail calls, it also belongs to the category of tail recursion. Tail recursion can be optimized by the compiler into a non-recursive form, reducing extra stack overhead and function call cost. Many algorithm competition contestants are keen on writing non-recursive code; without optimization this can greatly optimize the constant factor of the code, however if optimization is enabled, the quality of the binary generated by recursive code is no different from hand-written code.

```cpp
int fac(int n) {
  if (n < 2) return 1;
  return /* use */ n * fac(n - 1); /* uses the variable n, cannot directly do tail recursion optimization! */
}
```

Note that this function is not tail-recursive, but can be rewritten as:

```cpp
int fac(int acc, int n) {
  if (n < 2) return acc;
  return fac(acc * n, n - 1);
}
```

The new code is tail-recursive.

Modern compilers can automatically complete this process for you; if your code has a chance to be rewritten as tail recursion, then the compiler can recognize this form and then complete the rewriting.

#### Tail recursion elimination -Rpass=tailcallelim

Since the function is already tail-recursive, then we can directly delete the recursive statement, and through certain static analysis, directly convert the function into a non-recursive form. Here we do not go into detail about how compiler authors achieve this; from actual experience, for the vast majority of OI code, if there is a recursive version and a non-recursive version, then this code can generally be automatically optimized into the non-recursive version. Here we give the reader some specific examples:

???+ note "[GCD](https://godbolt.org/z/8Wb6WEnzv)"
    ```cpp
    int gcd(int a, int b) { return b ? gcd(b, a % b) : a; }
    ```

???+ note "[Fibonacci sequence](https://godbolt.org/z/4enof6Wcb)"
    ```cpp
    // expand the fib(n - 2) term
    // fib(n - 1) cannot be transformed into non-recursive; the optimized code is still exponential
    int fib(int n) {
      if (n < 2) return 1;
      return fib(n - 1) + fib(n - 2);
    }
    ```

???+ note "[Factorial](https://godbolt.org/z/n64e75xrf)"
    ```cpp
    // expand into a scalar loop, then perform automatic vectorization; the generated code is SIMD
    unsigned fac(unsigned n) {
      if (n < 2) return 1;
      return n * fac(n - 1);
    }
    ```

The optimized assembly of these functions is completely the same as the non-recursive version; the recursion will be directly eliminated. For OI contestants, you can confidently write the recursive version of various algorithms under O2, and there will be no difference from the non-recursive version. If the function you write itself cannot be rewritten into a non-recursive form, then the compiler is powerless.

### Strength reduction (Strength Reduction)

A common compiler optimization. The simplest example is `x * 2` becoming `x << 1`; the second way of writing is quite common in OI. The compiler will automatically do similar optimizations; when the optimization switch is turned on, `x * 2` and `x << 1` are completely equivalent. Strength reduction (Strength Reduction) converts high-cost instructions into low-cost instructions.

#### Scalar operator transformation

##### Shift instead of multiplication

```cpp
int a;
a = x * 2;   // bad!
a = x << 1;  // good!
```

Note that signed and unsigned numbers have obvious differences at the level of shifting and promotion. The sign bit has special handling during shifting, including two types: arithmetic shift and logical shift. This is prominent when writing binary search / segment trees that contain a large number of divide-by-two operations; signed integer division cannot be directly optimized into a one-step right shift operation.

```cpp
int l, r;
/* codes */
int mid = (l + r) / 2; /* if the compiler cannot assume l, r are non-negative, it will generate worse code */
                       // cannot be optimized into
                       // mid = (l + r) >> 1
                       // counterexample:
                       // mid = -127
                       // mid / 2 = -63
                       // mid >> 1 = -64
```

```cpp
int mid = (l + r);
int sign = mid >> 31; /* logical right shift, get the sign bit */
mid += sign;
mid >>= 1; /* arithmetic right shift */
```

Feasible solutions:

-   Use `unsigned l, r;`; subscripts should be unsigned in the first place
-   Use shifting in the source code

##### Multiplication instead of division

```cpp
int x = a / 3;
```

This process can be transformed into `x = a * 0x55555556 >> 32`; for specifics, see [this Zhihu answer](https://zhuanlan.zhihu.com/p/151038723) or the [original paper](https://dl.acm.org/doi/10.1145/773473.178249).

#### Induction variable strength reduction (IndVars)

The compiler automatically recognizes the induction variables in a loop and converts related high-cost procedures into low-cost ones.

```cpp
int a = 0;
for (int i = 1; i < 10; i++) {
  a = 3 * i;  // bad!
  a = a + 3;  // good!
}
```

Here directly using `a = 3 * i` is very common in OI, and the compiler can automatically analyze the equivalent transformation to `a = a + 3`, using the cheaper addition instead of multiplication. Analyzing the iteration process of loop variables is called SCEV (Scalar Evolution).

SCEV can also optimize some loops:

```cpp
int test(int n) {
  int ans = 1;
  for (int i = 0; i < n; i++) {
    ans += i * (i + 1);
  }
  return ans;
}
```

This function will be optimized into an $O(1)$ formula summation, see <https://godbolt.org/z/ET8d89vvK>. This behavior currently only appears in LLVM-based compilers; the GCC compiler is more conservative.

```nasm
test(int):                               # @test(int)
        test    edi, edi
        jle     .LBB0_1
        lea     eax, [rdi - 1]
        lea     ecx, [rdi - 2]
        imul    rcx, rax
        lea     eax, [rdi - 3]
        imul    rax, rcx
        shr     rax
        imul    eax, eax, 1431655766
        and     ecx, -2
        lea     eax, [rax + 2*rcx]
        lea     eax, [rax + 2*rdi]
        dec     eax
        ret
.LBB0_1:
        mov     eax, 1
        ret
```

### Auto-vectorization (Auto-Vectorization)

Single instruction stream, multiple data streams is a good way to provide single-core parallelism. Using this kind of instruction, we can utilize the CPU's SIMD registers, which are wider than general-purpose registers, for example putting 4 integers at once and then computing. OI contestants do not need to understand the details of auto-vectorization; generally speaking, the Clang compiler does more aggressive auto-vectorization than GCC:

```cpp
// https://godbolt.org/z/h1hx5sWoE
void test(int *a, int *b, int n) {
  for (int i = 0; i < n; i++) {
    a[i] += b[i];
  }
}
```

#### `__restrict` type specifier (GNU, MSVC)

The regions corresponding to two arbitrary pointers may overlap (overlap); at this time we need to special-case whether vector code can be used. The figure below shows an example of pointer overlap:

![](./images/overlap.png)

`__restrict`, as a convention, makes the compiler assume that the memory regions pointed to by two pointers never overlap.

```cpp
void test(int* __restrict a, int* __restrict b, int n) {
  for (int i = 0; i < n; i++) {
    a[i] += b[i];
  }
}
```

`__restrict` is not part of the C++ standard, but all major compilers can use it. This keyword affects the code generation quality of auto-vectorization, and can be used in extreme constant-factor-optimization situations.

## Common language misuses related to compiler optimization

### inline - inlining

Function inlining is usually automatically completed by the compiler under O2. The `inline` in a struct definition is completely redundant; if the competition you are preparing for enables O2 optimization, then there is no need to declare it as inline at all. If O2 is not enabled, using `inline` will not make the compiler really inline.

The `inline` keyword in modern C++ is regarded as a semantic behavior related to linkage and exported symbols, rather than doing function inlining.

### register - fake register suggestion

Modern compilers will directly ignore your `register` keyword; the register allocation you think of is generally not as smart as the compiler directly running the register allocation algorithm. This keyword was deprecated in C++11 and removed in C++17[^p0001r1].

<https://en.cppreference.com/w/cpp/keyword/register>

## Undefined Behavior and compiler optimization

The compiler can consider that a C++ program has no [undefined behavior](https://en.cppreference.com/w/cpp/language/ub) (undefined behavior, UB), so when compiling a program with UB, the compiler may produce unexpected results. At the same time, the compiler can also perform more aggressive and free optimizations under the assumption that there is no UB.

Common UB includes:

1.  [Signed overflow](https://users.cs.utah.edu/~regehr/papers/overflow12.pdf);
2.  Using uninitialized variables;
3.  Out-of-bounds access;
4.  Null pointer dereference;
5.  Side-effect-free infinite loops.

Other UB and examples can be understood in detail through the extended reading.

### Signed overflow

```cpp
int f(int x) { return x * 2 / 2; }
```

The compiler can assume that the program has no signed overflow behavior, so this function may be optimized to

```cpp
int f(int x) { return x; }
```

Examples: <https://godbolt.org/z/WKv3W5hvM>, <https://godbolt.org/z/qqE9nxP1j>.

This assumption can be disabled through the [`-fwrapv`](https://gcc.gnu.org/onlinedocs/gcc-13.2.0/gcc/Code-Gen-Options.html#index-fwrapv) option. Examples: <https://godbolt.org/z/5x3K5KGnr>, <https://godbolt.org/z/4r4a4EzMW>.

### Using uninitialized variables

```cpp
int f(int x) {
  int a;
  if (x)  // either x nonzero or UB
    a = 42;
  return a;
}
```

The compiler can assume that the program has no behavior of using uninitialized variables, so `a` must be initialized, so this function may be optimized to

```cpp
int f(int) { return 42; }
```

Examples: <https://godbolt.org/z/8WYMYYjdG>, <https://godbolt.org/z/qvGd1nvv9>.

### Out-of-bounds access

```cpp
int table[4] = {};

bool exists_in_table(int v) {
  // return true in one of the first 4 iterations or UB due to out-of-bounds
  // access
  for (int i = 0; i <= 4; i++)
    if (table[i] == v) return true;
  return false;
}
```

The compiler can assume that the program has no out-of-bounds access behavior, so this function must return before out-of-bounds access occurs, so this function may be optimized to

```cpp
bool exists_in_table(int) { return true; }
```

Example: <https://godbolt.org/z/xfePeYsE3>.

### Null pointer dereference

```cpp
int f(int* p) {
  int x = *p;
  if (!p)
    return x;  // Either UB above or this branch is never taken
  else
    return 0;
}
```

The compiler can assume that the program has no null pointer dereference behavior, so `!p` is always `false`, so this function may be optimized to

```cpp
int f(int*) { return 0; }
```

Examples: <https://godbolt.org/z/GY1jvsrb5>, <https://godbolt.org/z/4ronPsnxf>.

### Side-effect-free infinite loop

???+ note "Verify Fermat's Last Theorem"
    From [Fermat's Last Theorem](https://en.wikipedia.org/wiki/Fermat%27s_Last_Theorem), we know that the indeterminate equation $a^3=b^3+c^3$ has no positive integer solutions. The following program tries to enumerate the integers in $[1,1000]$ to verify whether this equation holds; if it returns `true`, then it means a set of integer solutions has been found in the range $[1,1000]$, so Fermat's Last Theorem does not hold.
    
    ```cpp
    #include <iostream>
    
    bool fermat() {
      const int max_value = 1000;
    
      // Endless loop with no side effects is UB
      for (int a = 1, b = 1, c = 1; true;) {
        if (((a * a * a) == ((b * b * b) + (c * c * c))))
          return true;  // disproved :()
        a++;
        if (a > max_value) {
          a = 1;
          b++;
        }
        if (b > max_value) {
          b = 1;
          c++;
        }
        if (c > max_value) c = 1;
      }
    
      return false;  // not disproved
    }
    
    int main() {
      std::cout << "Fermat's Last Theorem ";
      fermat() ? std::cout << "has been disproved!\n"
               : std::cout << "has not been disproved.\n";
    }
    ```

The compiler can assume that the program has no side-effect-free infinite loop, so it considers that the for loop in the `fermat()` function must terminate at some moment and return `true`, and finally the program may output:

```text
Fermat's Last Theorem has been disproved!
```

Examples: <https://godbolt.org/z/d834MK7bz>, <https://godbolt.org/z/Eov9nsKqf>.

## Sanitizer

Sanity guarantor. Checks at runtime whether your program has undefined behavior, array out-of-bounds, null pointers, and so on.
In local debug mode, it is recommended to enable some sanitizers, which can greatly shorten your Debug time. These sanitizers are developed by Google, and the vast majority can be used in GCC and Clang. Sanitizers are more mature in LLVM, so it is recommended that contestants use the Clang compiler locally for related debugging.

### Address Sanitizer -fsanitize=address

<https://clang.llvm.org/docs/AddressSanitizer.html>

Both GCC and Clang support this Sanitizer. It includes the following check items:

-   Out-of-bounds
-   Use-after-free
-   Use-after-return
-   Double-free
-   Memory-leaks
-   Use-after-scope

Applying this check will make your program about 2x slower.

### Undefined Behavior Sanitizer -fsanitize=undefined

<https://clang.llvm.org/docs/UndefinedBehaviorSanitizer.html>

Undefined Behavior Sanitizer (a.k.a UBSan) is used to check for undefined behavior in the code. Both GCC and Clang support this Sanitizer. It automatically checks whether your program has undefined behavior. UBSan's check items include:

-   Shift overflow, for example a 32-bit integer left-shifted by 72 bits
-   Signed integer overflow
-   Floating-point conversion to integer data overflow

UBSan's check items are optional; for the impact on the program, refer to the provided web address.

## Miscellaneous

### Compiler Explorer

Observe the behavior and assembly code of various compilers here: <https://godbolt.org>

## Extended reading

1.  [The LLVM Project Blog: What Every C Programmer Should Know About Undefined Behavior #1/3](https://blog.llvm.org/2011/05/what-every-c-programmer-should-know.html)
2.  [The LLVM Project Blog: What Every C Programmer Should Know About Undefined Behavior #2/3](https://blog.llvm.org/2011/05/what-every-c-programmer-should-know_14.html)
3.  [The LLVM Project Blog: What Every C Programmer Should Know About Undefined Behavior #3/3](https://blog.llvm.org/2011/05/what-every-c-programmer-should-know_21.html)

## References and notes

[^p0001r1]: [Remove Deprecated Use of the register Keyword (open-std.org)](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2015/p0001r1.html)
