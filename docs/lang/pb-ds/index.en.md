author: HeRaNO, Xeonacid, saffahyjp

The full name of the pb\_ds library is Policy-Based Data Structures.

The pb\_ds library encapsulates many data structures, such as hash tables, balanced binary trees, tries (Trie trees), heaps (priority queues), etc.

Just like `vector`, `set`, `map`, its components all conform to the relevant STL interface specifications. Some (such as the priority queue) contain all the functionality of the corresponding component in STL, but have more functionality than STL.

pb\_ds can only be used under compilers that use libstdc++ as the standard library.

You can use `begin()` and `end()` to obtain an `iterator` to traverse.

You can `increase_key`, `decrease_key`, and delete a single element.

Since the main content of the pb\_ds library is in the `__gnu_pbds` namespace starting with an underscore, its compliance in NOI series activities had not been determined for a long time. On September 1, 2021, according to [《Supplementary explanation on the restriction of programming language use in NOI series activities》](https://www.noi.cn/xw/2021-09-01/735729.shtml), library functions or macros starting with an underscore are allowed (except for library functions and macros with explicitly prohibited operations), so the compliance of using the pb\_ds library in NOI series activities now has a documentary basis.

**Reference: [《The application of C++'s pb\_ds library in OI》](https://github.com/OI-Wiki/libs/blob/master/lang/pb-ds/C%2B%2B的pb_ds库在OI中的应用.pdf)**
