author: H-J-Granger, Ir1d, ChungZH, Marcythm, StudyingFather, billchenchina, Suyun514, Psycho7, greyqz, Xeonacid, partychicken

This page mainly lists some little tricks used in contests.

## Exploiting locality

Locality means that a program tends to reference data items near other recently referenced data items, or the recently referenced data items themselves. Locality is divided into temporal locality and spatial locality.

For details, see content such as [Loop unrolling](../lang/optimizations.md#loop-unroll-loop-unroll) and [Code layout optimizations](../lang/optimizations.md#code-layout-optimizations-code-layout-optimizations).

## Loop macro definitions

The following code can be simplified using a macro definition:

```cpp
for (int i = 0; i < N; i++) {
  // loop body omitted
}

// simplified using a macro
#define f(x, y, z) for (int x = (y), __ = (z); x < __; ++x)

// then, when writing loop code, it can be simplified to `f(i, 0, N)`. For example:
// a is a STL container
f(i, 0, a.size()) { ... }
```

In addition, here is a rather useful macro definition:

```cpp
#define _rep(i, a, b) for (int i = (a); i <= (b); ++i)
```

## Making good use of namespaces

Using namespaces makes a program more readable and easier to debug.

??? note "Example: NOI 2018 Dragon-Slaying Warrior"
    ```cpp
    // NOI 2018 Dragon-Slaying Warrior, 40-point partial-credit code
    #include <algorithm>
    #include <cmath>
    #include <cstring>
    #include <iostream>
    using namespace std;
    long long n, m, a[100005], p[100005], aw[100005], atk[100005];
    
    namespace one_game {
    // variables can actually also be declared inside a namespace
    void solve() {
      for (int y = 0;; y++)
        if ((a[1] + p[1] * y) % atk[1] == 0) {
          cout << (a[1] + p[1] * y) / atk[1] << endl;
          return;
        }
    }
    }  // namespace one_game
    
    namespace p_1 {
    void solve() {
      if (atk[1] == 1) {  // solve 1-2
        sort(a + 1, a + n + 1);
        cout << a[n] << endl;
        return;
      } else if (m == 1) {  // solve 3-4
        long long k = atk[1], kt = ceil(a[1] * 1.0 / k);
        for (int i = 2; i <= n; i++)
          k = aw[i - 1], kt = max(kt, (long long)ceil(a[i] * 1.0 / k));
        cout << k << endl;
      }
    }
    }  // namespace p_1
    
    int main() {
      int T;
      cin >> T;
      while (T--) {
        memset(a, 0, sizeof(a));
        memset(p, 0, sizeof(p));
        memset(aw, 0, sizeof(aw));
        memset(atk, 0, sizeof(atk));
        cin >> n >> m;
        for (int i = 1; i <= n; i++) cin >> a[i];
        for (int i = 1; i <= n; i++) cin >> p[i];
        for (int i = 1; i <= n; i++) cin >> aw[i];
        for (int i = 1; i <= m; i++) cin >> atk[i];
        if (n == 1 && m == 1)
          one_game::solve();  // solve 8-13
        else if (p[1] == 1)
          p_1::solve();  // solve 1-4 or 14-15
        else
          cout << -1 << endl;
      }
      return 0;
    }
    ```

## Using macros for debugging

When testing locally, programmers often need to add some debugging statements. But when they need to submit to an OJ, to keep the output of the debugging statements from affecting the system's judgment of the program's output, they have to delete them all, which is time-consuming. In this case, one can save time by defining macros. The rough program framework is like this:

```cpp
#define DEBUG
#ifdef DEBUG
// do something when DEBUG is defined
#endif
// or
#ifndef DEBUG
// do something when DEBUG isn't defined
#endif
```

`#ifdef` checks whether the program has the corresponding identifier defined by `#define`; if it is defined, it executes the statements that follow. `#ifndef`, on the other hand, executes the statements that follow when the corresponding identifier is not defined.

This way, you only need to write the debugging code inside `#ifdef DEBUG` and the actual submission code inside `#ifndef DEBUG` to conveniently do local testing. When submitting the program, you only need to comment out the `#define DEBUG` line. You can also not define the identifier in the program, but instead define the `DEBUG` identifier at compile time via the `-DDEBUG` compilation option. This way you don't need to modify the program when submitting.

Many OJs enable the `-DONLINE_JUDGE` compilation option; making good use of this feature can save a lot of time.

## Diff-testing (duipai)

Diff-testing is a method of checking or debugging that verifies a program's correctness by comparing the outputs of two programs. You can compare your own program's output with another program's output to determine whether your program is correct.

The diff-testing process must be run many times, so it needs to be automated via a batch method.

Specifically, diff-testing requires one [data generator](../tools/testlib/generator.md) and two programs whose output results are to be compared.

Each time the data generator runs, it writes the generated data into the input file; the two programs read the data via redirection and write their output into designated files; finally, the `fc` command under Windows (the `diff` command under Linux) is used to compare the files to verify the program's correctness. If a program is found to be wrong, you can directly use the just-generated data to debug.

The rough framework of a diff-testing program is as follows:

```cpp
#include <cstdio>
#include <cstdlib>

int main() {
  // For Windows
  // do not use file I/O when diff-testing
  // of course, this program can also be rewritten in batch form
  while (true) {
    system("gen > test.in");  // the data generator writes the generated data into the input file
    system("test1.exe < test.in > a.out");  // get the output of program 1
    system("test2.exe < test.in > b.out");  // get the output of program 2
    if (system("fc a.out b.out")) {
      // this statement compares the input and output
      // fc returns 0 when the outputs are consistent, otherwise it means there are differences
      system("pause");  // convenient for viewing the differences
      return 0;
      // this input data is already stored in the test.in file and can be used directly for debugging
    }
  }
}
```

## Memory pools

When dynamically allocating memory, frequent use of `new`/`malloc` takes up a lot of time and space, and even generates a large amount of memory fragmentation that lowers the program's performance, possibly turning an otherwise correct program into TLE/MLE.

At such times you need the "memory pool" technique: before actually using memory, first request an allocation of a certain amount of memory as a reserve. When a dynamic allocation is needed, simply allocate a block from the reserve memory.

In most OI problems, you can precompute the maximum memory needed and request the allocation all at once.

Example:

```cpp
// dynamically allocate an array of 32-bit signed integers:
int* newarr(int sz) {
  static int pool[MAXN], *allocp = pool;
  return allocp += sz, allocp - sz;
}

// code for dynamic node allocation in a segment tree:
Node* newnode() {
  static Node pool[MAXN << 1], *allocp = pool - 1;
  return ++allocp;
}
```

## References

[Luogu Daily #86](https://studyingfather.blog.luogu.org/some-coding-tips-for-oiers)

*Classic Introduction to Algorithm Competitions: Exercises and Solutions*
