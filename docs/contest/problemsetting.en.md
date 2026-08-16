author: ouuan, Henry-ZHR, StudyingFather, ChungZH, xyf007, Cryflmind, oierlinch, xk2013awa

## Preparation before setting problems

### Have a certain level

On one hand, when setting problems by oneself, it is hard to set problems harder than one's own level; a certain OI level helps in coming up with higher-quality ideas and thinking of good solutions. On the other hand, OI level to some extent represents OI seniority, and contestants who have seen more problems also have their own views on what makes a "good problem".

### Hold a serious and responsible attitude

Problems are set for others to do; more than showing off oneself, it is about serving others. Competitive programming is a competition among contestants, not a contest between the problem setter and the solvers. Therefore, setting problems should not aim to stump contestants (of course, appropriate anti-AK measures and good discrimination are also very important), but should let contestants gain something in the contest. Spending enough time and energy to learn how to set problems and setting them seriously and responsibly is very important.

### Be prepared to spend a lot of time

If you want to set problems seriously, you will inevitably spend a lot of time. Without mental preparation, it may lead to hasty contest preparation and substandard quality, and you may also regret afterward that you did not spend the time on learning. But setting problems can also bring many good memories; if you are truly interested in setting problems and are fully mentally prepared, the gains from setting problems can make up for the time spent.

### Read the content of this article carefully

This article introduces the entire problem-setting process from two aspects: how to set problems and how to set them well. For those who want to set problems, reading this article carefully will surely be greatly beneficial.

## Problem content

To set a problem, the idea—that is, the essential content of the problem—is the soul of the problem and the first step of setting it.

### Sources of ideas

1.  Inspired by an existing problem (but you cannot copy it wholesale or strengthen it meaninglessly, such as moving a sequence problem onto a cactus).
2.  Inspired by a topic you have learned (but you cannot patch together topics with no connection).
3.  Inspired by life/games (but be careful not to turn a game into a big simulation problem).
4.  For no known reason, you just thought of a problem.

### What kinds of ideas are bad

#### About duplicate problems

Duplicate problems can be roughly divided into three kinds: completely identical, almost identical, and same-solution.

-   Completely identical: the AC code of one problem can AC another problem.
-   Almost identical: modifying the AC code of one problem into the AC code of another can be done by someone who does not know how to solve that problem.
-   Same-solution: the core idea and approach are the same, but there are differences in the code implementation and in less crucial details.

These three kinds of duplicate problems are in a containment relationship from bottom to top.

The following situations should not occur:

1.  Setting a duplicate problem while knowing there is an "almost identical" duplicate.
2.  Setting an "almost identical" duplicate because you did not use a search engine and were unaware of the duplicate.
3.  Setting a duplicate when a "same-solution" duplicate is widely known (such as an NOIP or NOI problem).
4.  Having a "same-solution" duplicate appear in a non-giveaway problem of a selective exam.

The following situations are best avoided:

1.  Setting a duplicate problem while knowing there is at least a "same-solution" duplicate.
2.  Setting a "same-solution" duplicate because you did not use a search engine and were unaware of the duplicate.
3.  Setting an "almost identical" duplicate under any circumstances.

Exceptions where the requirements can be relaxed:

1.  In-school mock contests.
2.  Mock contests aimed at topic-specific training.
3.  Contests of lower difficulty, or problems positioned as giveaways.

#### About "toxic" problems

A "toxic problem" is a very vague and subjective concept; here we merely cite some predecessors' discussions on this, adding some of our own understanding. This topic is very open; everyone is welcome to share their views.

> A good problem should not be two problems stitched together; a good problem has its own idea—and it should highlight this idea without too much packaging.
>
> A good problem should be novel. A truly good problem is a good problem that can inspire people to come up with new good problems.
>
> ——[vfk, "The Origin of the UOJ Spirit"][1]

Example: ["XR-1" The Conan Family](https://www.luogu.com.cn/problem/P5346), whose two halves of the solution are completely disjoint; the first half is ["Template" Tree Suffix Sorting](https://www.luogu.com.cn/problem/P5353) and the second half is a classic tree problem. Even with arbitrarily input tree vertex weights, you can still do the second part; the two parts have no connection.

> One class of OI problems is mainly mathematical: both the problem statement and the solution have the characteristics of a math problem, and the solution contains no algorithm-related topics. This class of OI problems is collectively called pure math problems.
>
> ——[Wang Tianyi, "On the Harm of Off-Topic Problems"][2]

Classic example: [NOIP2017 Xiaokai's Confusion](https://uoj.ac/problem/329)

The difference between math problems in OI and other math problems—a characteristic that reflects the essence of OI—is that math problems in OI usually focus not on **what** the answer is, but on how to **speed up** computing the answer. If a problem's focus is on "how to compute" rather than "how to compute quickly", such a math problem is generally unsuitable for OI.

> Some off-topic problems involve university physics content, leaving contestants at a loss when facing physics topics they have never encountered, creating a knowledge barrier.
>
> ——[Wang Tianyi, "On the Harm of Off-Topic Problems"][2]

Classic example: ["Tsinghua Training 2015" Polygon Goes to Sea](https://uoj.ac/problem/159)

Not just physics—OI problems should not involve too much knowledge from other subjects; if they do, a detailed explanation should be given, and knowledge from other subjects should not become a major obstacle to solving the problem.

> A good problem, regardless of difficulty, should have its own thinking difficulty, requiring contestants to think and discover some properties.
>
> The code of a good problem can be long, but it must not be made long by forced nesting or by adding conditions; it should be long naturally, making people feel that the code of this problem should be this long.
>
> ——[Wang Tianyi, "On the Harm of Off-Topic Problems"][2]

Classic examples: ["SDOI2010" Killer of the Pig Kingdom](https://loj.ac/problem/2885), ["Training Team Mutual Test 2015" Future Program · Revised](https://uoj.ac/problem/98)

In a general OI contest, thinking difficulty should account for the main part. Of course, engineering problems like those on Day 2+ of THUWC/THUSC also have their reason for existing—after all, the purpose of the experience camp, besides examining contestants' algorithm-design ability, is also engineering code and documentation-learning ability that connects to university study. But in a general OI contest, what is examined more should still be algorithm design and thinking ability.

## Problem statement

### Writing formulas with LaTeX

There are many LaTeX tutorials online, such as:

-   [Introduction to LaTeX](../tools/latex.md#图表)
-   [Complete LaTeX Formula Guide](https://www.luogu.com.cn/blog/IowaBattleship/latex-gong-shi-tai-quan)
-   [Various LaTeX Commands and Symbols](https://blog.csdn.net/anxiaoxi45/article/details/39449445)

When using it, please note the [format requirements for LaTeX formulas](../intro/format.md).

### Problem background

The problem background should be as short as possible. When the problem background is long, it should be separated from the problem description.

You must absolutely avoid the problem background seriously affecting the understanding of the problem's meaning.

When necessary, you can provide two versions: a problem description combined with the background, and a concise problem description.

### Problem description

In short, the problem description needs to be **clear and easy to understand**.

Every definition in the statement that may not be understood should be explained; concepts that are not defined should not appear out of nowhere. For example, in [CF1172D Nauuo and Portals](https://codeforces.com/problemset/problem/1172/D), you must explain in the statement what a "portal" is.

Each concept involved in the statement should be described with a single term. For example, you should not say "cost" (费用) at one point and "cost" (代价) at another.

You should not, without explanation, use a term with a meaning different from its original or common meaning. For example, you should not use "path" to refer to a single edge without explanation.

You need to ensure that your statement does not contradict itself. For example, in [CF1173A Nauuo and Votes](https://codeforces.com/problemset/problem/1173/A), "?" was not treated as a kind of "result", because the meaning of "?" is "there are more than one possible results".

You need to ensure that your statement cannot be misunderstood in a self-consistent way, even if such an interpretation is counterintuitive and no one would think that way. For example, in [CF1172D Nauuo and Portals](https://codeforces.com/problemset/problem/1172/D), the reason for tediously defining "walk into" and distinguishing it from "teleport" is to prevent this interpretation: through a portal you can reach another portal, and reaching a portal teleports you, so you would bounce back and forth repeatedly.

Reading the problem description straight through, one should be able to understand every sentence and grasp the problem's task and requirements. At least in the immediately following paragraph the confusion should be resolved, rather than only after several paragraphs, or only after reading the input/output format, or even having to guess the meaning from the samples. For example, in ["GuOJ Round #1" Cirno's Ice and Snow Banquet](https://github.com/OI-wiki/problemset/blob/master/contest/online/GuOJ/OI%20Archive%20-%20GuOJ1171.pdf), the problem's goal—"the maximum amount of water the Misty Lake can ultimately receive"—appears for the first time only in the output format, and combined with the misleading sentence "Reimu can of course quickly figure out the total cost of clearing all the streams", it more easily causes people to misread the problem's meaning, which is undesirable; the problem's goal should be stated in the problem description itself. (In this example there is also the problem of the background seriously affecting the understanding of the meaning.) The same mistake also appears in [CF1423(4)N Bubblesquare Tokens](https://codeforces.com/problemset/problem/1423/N), where the problem's goal, "friend pairs and number of tokens each of them gets on behalf of their friendship", appears for the first time only in the output format.

### Input/output format

The input/output format just needs to be clear and **complete**; there are no rigid requirements. Personally I suggest writing the input/output format by referring to CF problems; for details refer to [Notes for CF Problem Setters][3].

For the convenience of contestants, the input/output format should preferably explain the specific meaning of each variable, unless the meaning of a variable is very long and cannot be stated in one sentence (in which case you can say "see the problem description for the meaning").

Note in particular that if the output contains decimals, please use an [SPJ](#special-judge) to limit the size of the error as much as possible, rather than requiring "keep x decimal places".

"Keep x decimal places" may impose an infinite precision requirement. For example, requiring three decimal places when the actual answer is $0.0015$: then as long as an error of any size makes the computed answer smaller than $0.0015$, even if the computed answer is $0.00149999\cdots$, it will output a wrong answer.

If you cannot use an SPJ, please ensure that the precision requirement is finite—for example: please output the answer rounded to three decimal places. Let the standard answer be $ans$; the data guarantees that for any $x$ satisfying $\frac{|x-ans|}{\max(1,ans)}<10^{-9}$, its rounded result is the same as the rounded $ans$.

Some sentences you can refer to:

```latex
The first line of input contains three positive integers $n$, $m$, $k$ ($1\le n,m\le 2\cdot 10^5$, $1\le k\le 100$) — $n$ is the length of the sequence, $m$ is the number of operations, and the meaning of $k$ is given in the problem description.
```

```latex
The second line of input contains $n$ non-negative integers $a_1,a_2,\ldots,a_n$ ($1\le a_i\le 10^9$) — the sequence given by the problem.
```

```latex
The $i$-th of the next $m$ lines contains two positive integers $l_i$ and $r_i$ ($1\le l_i\le r_i\le n$), indicating that the $i$-th operation is performed on the interval $[l_i,r_i]$.
```

```latex
Each of the next $n-1$ lines contains two positive integers $u$ and $v$ ($1\le u,v\le n$), indicating that $u$ and $v$ are connected by an edge.

The data guarantees that the given edges form a tree.
```

```latex
The only line of input contains a non-empty string of lowercase English letters whose length does not exceed $10^6$.
```

```latex
The second line of input contains a real number $x$ with no more than three decimal places ($-10^6\le x\le 10^6$); the meaning is given in the problem description.
```

```latex
The output contains a real number; it is considered correct when the absolute or relative error between your output and the standard answer is less than $10^{-6}$.
```

```latex
The second line of output contains $n$ positive integers, representing the scheme you constructed — where the $i$-th number is the number of the $i$-th card you play.

If there are multiple valid answers, you may output any one of them.
```

???+ note "Generating input data with a random-number generator inside the contestant's code"
    Some problems, because the input data is too large, require the contestant to generate the data within the code via a given data generator instead of reading the data via standard input or a file, in order to prevent overly long reading times.
    
    Adopting this approach requires careful consideration, because it has many drawbacks:
    
    -   It may introduce data randomness not needed by the intended solution, or make constructing data difficult
    -   It may increase the difficulty of understanding the input format
    -   If the random-number generator is poorly encapsulated, understanding how to use the data generator itself may be difficult
    -   If a contestant does not use the language recommended by the problem setter, they may need to write their own data generator
    
    This approach is generally adopted to prevent overly long reading times, so one possible alternative is to distribute a sufficiently high-performance [input/output optimization](./io.md) template to try to keep everyone's reading time consistent, so that even a long reading time does not affect the difference in time among contestants. Another solution is to package the problem as a function-call-style (rather than IO-style) interactive problem; even if there is no interaction in the algorithm process, an interactive problem can serve to unify the reading time, and IOI adopts the scheme where all problems are interactive. But both schemes restrict the languages contestants use, and require the problem setter to manually support each language contestants are allowed to use.
    
    Returning to the root of the problem, you can also consider whether overly large input data is necessary, whether it is possible to achieve the goal with smaller input data, and whether solutions slightly worse than the intended solution's complexity need to be excluded.

### Data range

According to CF's requirements, the data range should be written in the input format, but in China the data range is often written at the end of the problem.

The easiest mistake to make in the data range is incompleteness. Every number and every string in the input should be clearly delimited. The input/output format examples given above include some correct ways to write data ranges.

Common omissions in the data range:

1.  The "integer" part of "integer" (i.e. failing to specify it is an integer).
2.  The statement only says "integer" not "positive integer", and the data range has only an upper bound with no lower bound.
3.  A string with no specified character set.
4.  A real number with no specified number of decimal places.
5.  Some variables with no given range.

You need to ensure that your reference solution can pass **any dataset** satisfying the data range stated in the problem.

???+ note "About 'the data is guaranteed to be randomly generated'"
    Some problems "guarantee that the data is randomly generated"; often such a restriction is not the optimal solution, because "randomly generated" does not clearly restrict the data, which makes it difficult to judge the specific data range and to provide hack data.
    
    Generally, "the data is guaranteed to be randomly generated" can be replaced by the data properties needed by the solution. For example, randomly generating a tree can often be replaced by restricting the tree's height.
    
    If you must guarantee that the data is randomly generated, you should specify the exact operation of the random generation. For example, whether generating a tree randomly chooses the parent node or randomly generates a Prüfer sequence.
    
    Note that a nondeterministic algorithm and an algorithm that depends on data randomness are different. The former can obtain the correct solution with high probability for any data, while the latter obtains the correct solution for most data but cannot possibly obtain it for certain specific data.

### Samples

Samples should have a certain strength, able to catch some simple errors. Someone who misread the problem's meaning should be able to discover through the samples that they misread it.

For a problem with multiple kinds of operations, each kind of operation should appear in the samples.

For a problem with multiple kinds of output (such as [CF1173A Nauuo and Votes](https://codeforces.com/problemset/problem/1173/A)), each kind of output should appear in the samples. Exception: problems where there is actually never no solution, but which require determining whether a solution exists.

### Sample explanation

The more complex and harder to understand the problem description, the more it should have a detailed sample explanation.

The simpler the problem's difficulty, the more it should have a detailed sample explanation.

A detailed sample explanation may optionally be accompanied by pictures.

Larger samples may have no sample explanation.

To accommodate the color-vision-impaired, it is best not to make color essential to understanding the sample explanation. You can use color pictures to beautify the sample explanation, but if you must use color to convey some necessary information, it is best not to have red and yellow or red and green appear together.

## Time limit, space limit, and partial credit

The purpose of the time limit and space limit is to exclude solutions with wrong complexity. (Of course, it is also to prevent overly long judging times; for example, an interactive problem with only a query-count limit and no time-complexity limit still has a time limit.)

Therefore, in principle the time limit should be chosen as the largest possible value that does not let wrong solutions pass.

Generally, the time limit should meet the following requirements:

1.  At least twice the worst-case time of std.
2.  If the contest allows Java, it should let Java pass.
3.  It should not let wrong solutions pass (except when a wrong solution really cannot be excluded, or you want to let a certain wrong solution pass).

To better let large-constant solutions pass while excluding wrong solutions, one can generally increase both the data range and the time limit. But note that sometimes the intended solution (due to cache and other unpredictable issues) has a huge constant increase when the data range increases, and then increasing the data range may not increase the time gap between the intended and wrong solutions.

In a format with partial credit, you can also, by setting graded data and slightly-smaller-range data, keep rather good wrong solutions and large-constant intended solutions from passing while letting them earn high partial credit.

Note in particular that when the data range is smaller than $5\cdot 10^5$, you should consider whether an [instruction set](https://ouuan.github.io/post/n方过百万-暴力碾标算——指令集优化的基础使用) can be used to pass.

Generally, the space limit should be set large enough, unless a solution with better space complexity is indeed very clever and worth excluding solutions with large space complexity. In that case you can consider setting partial credit with a loose space limit. It is worth noting that if you do not want to exclude solutions with large space consumption, data-structure problems generally need a large space limit.

> A good problem should have its selective nature, with sufficient discrimination. It should have at least 4 tiers of partial credit, letting beginners earn points and letting experts show their strength.
>
> ——vfk, "The Origin of the UOJ Spirit"

Partial credit generally comes in two kinds: smaller data ranges and special properties.

Smaller data ranges generally need multiple tiers; even if you cannot think of a solution of a certain complexity, you can consider giving that complexity a tier of credit. Generally, to avoid constant-factor issues, you can set a tier of partial credit at half the maximum data.

"Graded data" is best replaced by multiple tiers of partial credit.

The setting of special-property partial credit depends on the specific problem. Ideal special-property partial credit should guide contestants toward thinking of the intended solution. Unlike smaller-data-range partial credit, when you cannot think of a solution targeting a certain special property, it is best not to give that special property a tier of credit. For example, the $k=1$ tier of partial credit in ["CTS2019" Random Cube](https://loj.ac/problem/3119) was criticized by many people during the editorial, saying that this tier hindered thinking of the intended solution.

If the problem's scoring method differs from the default (such as bundling subtasks for testing in a general OI-format contest), you must state it in the statement.

It is not recommended to use the phrasing "XX% of the data satisfies XX", especially when the data range has multiple variables. For example, "$30\%$ of the data satisfies $n \le 1000$" and "$40\%$ of the data satisfies $m \le 100$" may describe the properties of $70\%$ of the data, or may describe the properties of only $40\%$ of the data. Generally, a subtask or data-range table is a better choice.

## Making data

Data generation is a necessary step in the problem-setting process and is also required for diff-testing. Mastering some data-generation techniques makes the data-making process easier and produces data of higher strength.

### Generating random data

#### Generating random numbers

Please refer to the [random functions](../misc/random.md) page.

Note in particular that when generating numbers with a value range larger than the random function's return value, please **do not** use a form like `rand() * rand()`; the random numbers generated this way are very non-uniform.

In addition, when setting problems it is recommended to use [testlib](../tools/testlib/generator.md) to make data, which guarantees that the same seed generates the same random numbers on different platforms, and the seed is automatically generated based on command-line arguments.

#### Generating a random permutation

You can use the `std::shuffle` function in the STL, in the form `std::shuffle(a, a + n, rng)`, where `rng` is a random-number generator, such as `std::mt19937 rng(std::chrono::steady_clock::now().time_since_epoch().count())`.

Please **do not** use `std::random_shuffle`; it was deprecated in C++14 and removed in C++17.

#### Generating a random interval

Common wrong method: randomly generate the left endpoint $l$ in $[1,n]$, then randomly generate the right endpoint $r$ in $[l, n]$. This way the generated interval tends to be toward the right.

A rather correct method (recommended): randomly generate two numbers in $[1, n]$, take the smaller as the left endpoint and the larger as the right endpoint.

A truly uniformly random method: generate a random number $x$ in $[0, n]$; if $x = 0$, generate another random number $y$ in $[1, n]$ and the interval is $[y, y]$; otherwise generate it by the "rather correct method".

#### Generating a random tree

The common method is to randomly choose a parent from $[1,i-1]$ for each node $i$ from $2$ to $n$. Doing so, the generated tree is not uniformly random, and its expected height is $O(\log n)$.

There is another random method: choose $i$'s parent randomly from $[i\cdot low, i\cdot high]$. If $low$ and $high$ are set appropriately, one can produce trees of relatively high strength.

The truly uniformly random method uses the [Prüfer sequence](../graph/prufer.md): first generate a random Prüfer sequence, then generate the tree from the sequence. Doing so, the tree's expected height is $O(\sqrt n)$.

Besides this, you can randomize a permutation to renumber the nodes / shuffle the order of the edges.

### Constructing data

#### Problems related to intervals

Common constructions: extremely small lengths (in particular, all single points), extremely large lengths (in particular, all the entire sequence).

#### Problems requiring factorization

Maximizing the number of prime factors with multiplicity: powers of $2$.

Maximizing the number of distinct prime factors: the product of the smallest several primes.

Maximizing the number of divisors: you can refer to the [A002182](http://oeis.org/A002182) sequence on OEIS.

#### Problems requiring the greatest common divisor

Making the two numbers whose GCD is to be computed adjacent terms of the [Fibonacci sequence](../math/combinatorics/fibonacci.md) can make Euclid's algorithm reach its worst-case time complexity.

#### Tree problems

Common constructions:

-   A chain
-   A star (chrysanthemum)
-   A complete binary tree
-   Replacing each node of a complete binary tree with a chain of length $\sqrt n$
-   A chain hung off a star
-   Single points hung off a chain
-   A tree of height $d$ with $d>1$ whose root has two children, the left subtree being a chain of length $d-1$ and the right subtree being such a tree of height $d-1$.

If you are not in the exam hall, you can also use [Tree-Generator](https://github.com/ouuan/Tree-Generator) to generate all kinds of trees.

### Generating data in bulk

The author recommends the command-line-argument + bat/sh method.

For example:

`gen.cpp`:

```cpp
#include "testlib.h"

using namespace std;

int n, m, k;
vector<int> p;

int main(int argc, char* argv[]) {
  registerGen(argc, argv, 1);

  int i;

  n = atoi(argv[1]);
  m = atoi(argv[2]);
  k = rnd.next(1, n);

  for (i = 1; i <= n; ++i) p.push_back(i);

  shuffle(p.begin(), p.end());
  // shuffle using rnd.next()

  printf("%d %d %d\n", n, m, k);
  for (i = 0; i < n; ++i) {
    printf("%d%c", p[i], " \n"[i == n - 1]);
    // using a string as an array—space in the middle, newline at the end—is a common data-making trick
  }

  return 0;
}
```

`gen_scripts.bat`:

```bat
gen 10 10 > 1.in
gen 1 1 > 2.in
gen 100 200 > 3.in
gen 2000 1000 > 4.in
gen 100000 100000 > 5.in
```

The benefit of doing this is that you only need to write one generator for different data, and you can conveniently modify the parameters of a certain test point.

### Requirements for making data

The data should include the minimum and maximum of each parameter.

The data should include various corner cases.

When using subtasks, the data (including input and output) should preferably cover the various ranges in the value range, rather than only the maximum of the data range.

To prevent special-case handling targeting a specific construction from passing, you can combine different constructions in one test point, or make most of the data a construction mixed with a small part of randomness.

The data should include all kinds of constructions, even if you do not know what wrong solution will fail on a given construction. (In a format that scores by test point, handle this as appropriate.)

Of course, if you already know a wrong solution with a correctness problem (one a normal person can think of and write out), you should exclude it as much as possible.

Note in particular that if there is a possibility of integer overflow, you must exclude solutions that overflow. In a format with partial credit, someone who does not use long long should not get a score equal to or even lower than the brute force.

If there are pretests, the pretests should be as strong as possible (while as few as possible). In other words, you need to include all known break points of the problem in the pretests (with as few datasets as possible).

If you want a small amount rather than none of FST, you should still ensure the strength of the pretests, because in an actual contest unexpected errors are very likely to occur, leading to a far higher FST count than expected.

### Data format

Here we provide some data-format requirements for input data in the usual case, which can serve as a general-case reference:

> 1.  Use the newline format of the testing environment.
> 2.  There is a newline at the end of the last line of the file, i.e. the last character of the entire file needs to be `\n`.
> 3.  There is no whitespace at the beginning or end of any line.
> 4.  No more than 1 consecutive space.

Data generated in a Windows environment usually has the newline format `\r\n`, while mainstream judging systems all run in a Linux environment, whose newline format is `\n`. If Windows-format newline data is read in a Linux environment, it may cause abnormal newline handling when reading strings, which in turn causes the program to behave differently in different environments; if output generated in a Linux environment is compared with standard output generated in a Windows environment under a Linux environment, the comparison may differ due to the different newline formats. To keep program behavior consistent, the newline format of all data must be converted to the newline format of the environment in which the program runs.

You can generally generate data with Linux-format newlines in the following ways:

1.  Generate the data directly in a Linux environment.
2.  Convert the input/output files with the [`dos2unix`](https://dos2unix.sourceforge.io/) tool, which is included in toolchains such as Cygwin and MinGW.
3.  Open the output file in binary mode and use the `\n` newline format.
4.  Write your own tool by referring to the `dos2unix.cpp` code on [this page](https://help.luogu.com.cn/manual/luogu/problem/testcase-format#附录windows-环境下造数据注意事项).

## Special Judge

[SPJ writing tutorial](../tools/special-judge.md)

Scheme-output problems and floating-point-output problems are two relatively common problem types that need an SPJ; other problems also need an SPJ as appropriate. On CF, all problems must use a testlib-based checker; for example, when a problem requires outputting several integers, use testlib's built-in ncmp checker, and the contestant may output arbitrary whitespace (either spaces or newlines).

Checkers are generally written with testlib. Since a checker must cope with all kinds of illegal output, it needs extremely strong robustness, and it is hard to write a good checker without testlib.

Two points to note when writing a checker:

1.  You need to cope with all kinds of illegal output, so please check whether each read variable is in a valid range (`readInt(minvalue, maxvalue)`). For example, when reading a variable that will be used as an array index during the check, you must check its range, otherwise it may cause an array out-of-bounds, which sometimes leads to RE and sometimes may be judged as AC.
2.  In principle, a checker should not check whitespace (i.e. you should not use `readSpace()`, `readEoln()`, `readEof()`; it is worth mentioning that testlib automatically checks whether there is extra output).

## Editorial

The goal of the editorial is for everyone expected to participate in the contest to understand it. So the requirement for the level of detail of an official editorial is higher than that of an ordinary editorial.

### About partial credit

For a problem with partial credit, you can consider writing about the partial-credit solutions in the editorial.

### About topics

The topics used in the solution should be clearly pointed out. For topics whose difficulty is comparable to the problem's difficulty, it is best to give materials for learning that topic (such as the address of a blog post).

### About definitions

Do not have concepts appear out of nowhere in the editorial.

For example, a DP editorial should clearly explain the definition of the state.

### About details

If the specific implementation details are rather clever, it is best to write them out; otherwise "see the code for details" is also acceptable. If it is "see the code for details", it is best to add some comments to the code.

### Reference solution

It is best to remove redundant parts from the reference solution. For example, some editorials keep a complete define template (to increase solving speed, containing many defines and common functions, often used in online contests such as CF), and a large part of it is unused, which is bad.

If some implementation details are not explained in detail in the editorial, it is best to add an appropriate amount of comments.

## Contest

### The problem difficulty in the contest announcement must be truthful

> Remember that authors tend to underestimate the difficulty of their problems.
>
> ——A reminder on the Codeforces PROPOSE A PROBLEM page

The problem setter is very likely to misjudge the difficulty of the problem, so if you want to write the contest difficulty in the contest announcement, you need to consider carefully, and it is best to ask people to test the problems and assess them in advance.

### Allocation of problem difficulty

In domestic-OI-like mock contests, it is often enough that the overall difficulty of the three problems is comparable to the contest difficulty.

In CF/ATC-like online contests, you need to ensure increasing difficulty as much as possible (although due to misjudgment of difficulty, this often cannot really be achieved), and avoid a large difficulty gap as much as possible. You can reduce the difficulty gap by splitting one problem into an easy and a hard problem (two subtasks), but splitting into subtasks requires careful consideration, and many people also dislike subtasks in the CF format ([Are subtasks evil?](https://codeforces.com/blog/entry/71700)) for reasons including but not limited to:

-   Due to the format, doing the easy version first and then the hard version may incur less penalty and a higher total score
-   The scoring of subtasks is often not proportional to the problem difficulty
-   Often the easy version is not a qualified problem (not interesting)
-   Often the easy version's solution does not help in thinking of the hard version's intended solution

### Allocation of problem topics

A contest should cover as broad a range of topics as possible (topic-specific training contests excepted, of course).

A classic counterexample: CTS2019, which covered many topics such as dynamic programming, expectation, combinatorial counting, the inclusion–exclusion principle, and polynomials.

> I had to pick six problems out of five; I was quite helpless too.
>
> ——The reason given by the CTS2019 problem compiler, having not received enough problem submissions

## Problem-setting platforms

### Polygon

Polygon is a very powerful multi-person collaborative problem-setting platform; it can be the first choice for multi-person collaborative problem-setting on any website (using the package feature to export to sites that do not support Polygon), and is also a good choice for solo problem-setting (especially setting problems on different devices). For how to use it, see [Introduction to Polygon](../tools/polygon.md).

### Codeforces

Codeforces is one of the most famous competitive-programming websites in the world, with relatively high-quality problems, very suitable for problem setters who have some problem-setting experience and want to further improve their level and set a high-quality set of problems. Its shortcoming is that the review speed is rather slow (generally a few months), but you can also start preparing the problems during the review period (though with the risk that a problem gets rejected and the preparation is wasted).

#### Problem-setting eligibility

-   Blue name and having participated in at least 25 rated contests;
-   Purple name and having participated in at least 15 rated contests;
-   Orange name and having participated in at least 5 rated contests;
-   Red name or black-red name.

#### Submitting a contest proposal

Once you have problem-setting eligibility, you can see the [Propose a contest/problems](http://codeforces.com/proposals/new-contest) button in the sidebar.

After clicking in, first write a contest proposal (in PROPOSE A CONTEST), then write problem proposals and add them to the contest.

Once the problems are decided, you can open the contest proposal to review (submit for review).

#### Preparing problems on Polygon

Refer to [Introduction to Polygon](../tools/polygon.md).

#### Contact with the coordinators

Contact with the coordinators has two purposes:

1.  Speed up the review.
2.  After entering the preparation stage, the coordinator provides suggestions and help.

The formal way to contact them is to submit an application in the form of a proposal in the proposal system; after the coordinator begins reviewing, discuss in the form of comments below the proposal.

In fact, if a proposal has not passed review for a long time, you can consider contacting the coordinator by private message (CF actually writes "Don't send private messages or emails to coordinators", but 300iq stated in a [comment](http://codeforces.com/blog/entry/64077#comment-478933) that you can private-message him).

### Comet OJ

[Comet OJ link](https://www.cometoj.com/)

No longer active (as of November 2021, the last contest was in January 2020).

Problem-setting application: <https://info.cometoj.com/contests/Questionnaire_IssuerInfo/>

### CodeChef

An Indian competitive-programming platform with three formats: the 10-day Long Challenge with a challenge problem, the 2.5h ICPC-like Cook-Off, and the 3h IOI-like LunchTime.

Problem-setting FAQ: <https://www.codechef.com/wiki/faq-problem-setters>

Problem-setting guide: <https://www.codechef.com/problemsetting>

### AtCoder

A Japanese competitive-programming platform; problem-setting contact: <contest@atcoder.jp>.

### UOJ & LOJ

Domestic OJs with few contests.

### Luogu

Personnel participating in problem-setting work need a certain award-certification level; after creating a contest, the person in charge submits an application in the [ticket system](https://www.luogu.com.cn/ticket).

Open-contest standard: <https://help.luogu.com.cn/rules/academic/opencontest-standard>

## References

1.  [vfk, "The Origin of the UOJ Spirit"][1]

2.  [Wang Tianyi, "On the Harm of Off-Topic Problems"][2]

3.  [Notes for CF Problem Setters][3] ([image version accessible in China](https://github.com/OI-wiki/libs/blob/master/topic/rules.jpg))

4.  [The Self-Cultivation of a CF Problem Setter][4]

This article was ported by the author from [ouuan's problem-setting standard](https://ouuan.github.io/post/ouuan-的出题规范/) with some modifications and additions.

[1]: https://vfleaking.blog.uoj.ac/blog/909 "vfk, 'The Origin of the UOJ Spirit'"

[2]: https://github.com/OI-wiki/libs/blob/master/topic/7-%E7%8E%8B%E5%A4%A9%E6%87%BF-%E8%AE%BA%E5%81%8F%E9%A2%98%E7%9A%84%E5%8D%B1%E5%AE%B3.ppt "Wang Tianyi, 'On the Harm of Off-Topic Problems'"

[3]: https://docs.google.com/document/d/e/2PACX-1vRhazTXxSdj7JEIC7dp-nOWcUFiY8bXi9lLju-k6vVMKf4IiBmweJoOAMI-ZEZxatXF08I9wMOQpMqC/pub "Notes for CF Problem Setters"

[4]: https://github.com/OI-wiki/libs/blob/master/topic/CF%E5%87%BA%E9%A2%98%E4%BA%BA%E7%9A%84%E8%87%AA%E6%88%91%E4%BF%AE%E5%85%BB.md "The Self-Cultivation of a CF Problem Setter"
