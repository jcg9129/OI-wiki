author: StudyingFather, NachtgeistW, countercurrent-time, Ir1d, H-J-Granger, Chrogeek, sshwy, Suyun514, hsfzLZH1, CBW2007, Xeonacid, kawa-yoiko, Konano

In competitive programming, there are many varied types of problems.

## Traditional problems

**Traditional problems** are the relatively common problem type in competitive programming today.

Contestants need to submit source code; the judging system uses some pre-prepared input data and corresponding output data as test points[^note1], compiles the source code submitted by the contestant[^note2], has the contestant's program read the input data, and determines whether the contestant's program is correct by comparing the contestant's output with the pre-prepared output. This judging method is called **black-box judging**[^note3].

For a test point, a time limit and space limit are often also set.

The time limit refers to the limit on the program's running time[^note4]. The running time of the contestant's program on a single test point cannot exceed the given time limit.

The space limit refers to the limit on the amount of memory the program uses. The maximum space occupied by the contestant's program while running cannot exceed the given space limit.

After the program finishes running normally, the contestant's output is compared with the test point's output. This comparison generally filters out the trailing newline at the end of the file and trailing spaces at the ends of lines, and then does a full-text comparison. For certain special problems, a [Special Judge](../tools/special-judge.md) is used for the comparison.

After this process ends, the judging system gives different **judging results**[^note5] according to the program's running state:

-   Accepted (AC): the contestant's program is accepted.
-   Compile Error (CE): the contestant's program cannot compile normally.
-   Wrong Answer (WA): the contestant's program finishes normally, but the contestant's program's output does not match the test point's output.
-   Presentation Error (PE): the contestant's program finishes normally, but the format does not meet the requirements[^note6].
-   Runtime Error (RE): the contestant's program finishes abnormally (the return value when the contestant's program exits is nonzero).
-   Time Limit Exceeded (TLE): the running time of the contestant's program exceeds the given time limit.
-   Memory Limit Exceeded (MLE): the maximum space occupied by the contestant's program exceeds the given space limit.
-   Output Limit Exceeded (OLE): the amount of content output by the contestant's program exceeds the maximum limit.

In ICPC events, your program must achieve the AC status on all test points of a problem to be considered as passing that problem. In OI events, achieving the AC status on a single test point earns the score of that test point[^note7].

## Answer-submission problems

**Answer-submission problems** are problems where you directly submit the answer. This type of problem generally provides input files and requires submitting an archive, a folder, or plain files containing `XXX1.out`, `XXX2.out`, `XXX3.out`…`XXXn.out`.

After the answer is submitted, the judging system compares the answer files with the standard answer, and gives a certain score according to the quality of the contestant's answer and the degree of task completion.

Because answer-submission problems do not require running a source program, they have no time or space limit.

There are generally two methods for doing this kind of problem:

-   Doing it by hand. This method is simple and crude, but is helpless against large data.
-   Writing a program to obtain the answer files.

## Interactive problems

**Interactive problems** are problems where the contestant's program needs to interact with the judging program to complete the task. One common situation is that the contestant's program issues a query to the judging program and gets its feedback. The judging program may restrict the contestant's queries, or adjust its response strategy to increase the number of queries as much as possible, which also brings more variation to the problem.

For a more detailed explanation of interactive problems, see [Interactive problems](./interaction.md).

There are mainly the following two interaction methods. Although they differ considerably in technical terms, they have no real difference in the essence of the algorithm being examined.

### STDIO interaction

STDIO interaction (standard I/O interaction) is the interaction method of online platforms such as Codeforces and AtCoder, and is also the standard in ICPC-series events. Codeforces provides a more concise [explanation (in English)](https://codeforces.com/blog/entry/45307).

???+ note "Example [LOJ #559 "LibreOJ Round #9" ZQC's Maze](https://loj.ac/problem/559)"
    Please note the content added at the very bottom.
    
    This problem is an interactive problem.
    
    You, located in a dark maze made up of $n \times m$ cells, need to walk to the maze's exit to complete the maze challenge.
    
    At the start, you are located at the maze's start, i.e. at $(1,1)$, facing right, and the exit is located at $(n,m)$. Any two cells of the maze are connected, and there is only a unique path; the length between two adjacent (i.e. 4-connected: up, down, left, right) cells is one unit length. There may be a wall between two adjacent cells; the wall thickness is very small relative to a cell and is roughly negligible. The boundary of the maze all has walls, and every wall is connected to the boundary. The maze is completely dark, meaning you cannot obtain any information other than $(n,m)$.
    
    To try not to get lost in the dark, each time you advance you can only start from the current cell, follow the left or right wall, touch the wall with your left or right hand, and advance, making the hand touching the wall move exactly one unit length. Note that if the left or right wall does not exist, you cannot advance in that direction.
    
    Being in the dark too long will make you afraid, so you need to get out of the maze as early as possible. If you do not get out of the maze within the limited number of steps, the challenge will fail.

For this type of problem, the contestant just needs to write the query to standard output as usual, **flush the output buffer**, and then read the result from standard input. Only after the contestant's program flushes the output buffer can the judging program (called the interactor) connected to it via a pipe immediately receive this data. In C/C++, `fflush(stdout)` and `std::cout << std::flush` can achieve this operation (using `std::cout << std::endl` for a newline also automatically flushes the buffer, but `std::cout << '\n'` does not); in Pascal it is `flush(output)`.

### Grader interaction

The Grader interaction method is common in international OI events such as IOI and APIO (especially in CMS-platform competitions).

???+ note "Example [UOJ #206 【APIO2016】Gap](https://uoj.ac/problem/206)"
    There are $N$ strictly increasing non-negative integers $a_1,a_2,\cdots,a_N (0\leq a_1<a2<\cdots<a_N\leq 10^{18})$. You need to find the maximum value among $a_{i+1}−a_i (0\leq i\leq N−1)$.
    
    Your program cannot directly read in this integer sequence, but you can query information about the sequence through given functions. For details about the query functions, refer to the implementation-details section below according to the language you use.
    
    You need to implement a function that returns the maximum value among $a_{i+1}−a_i (0\leq i\leq N−1)$.

For this type of problem, the contestant just needs to write a specific function to complete some task, which interacts by calling several given helper functions. To make it convenient for the contestant to test locally, the problem distributes a header file and a reference judging program `grader.cpp` (for Pascal, a library `graderlib`); the contestant compiles their own program together with `grader.cpp` to get an executable.

```sh
g++ grader.cpp my_solution.cpp -o my_solution -Wall -O2
./my_solution   # run the program
```

The compiled program behaves similarly to a traditional-problem program. It opens fixed files, reads data in a fixed format, calls the function written by the contestant, and displays the result and some information (such as the number of queries and the correctness of the answer) on standard output.

During actual judging, the contestant's program is compiled with a different `grader.cpp`. This `grader.cpp` calls the function written by the contestant in a similar way and records its score. Generally, all global symbols of this version of `grader.cpp` are set to `static`, i.e. it cannot be cracked via name-conflict tricks, and any attempt to break the grader's restrictions results in disqualification.

### Differences

An obvious advantage of STDIO interaction is that it can support any programming language, but the time cost of input/output can easily become a bottleneck in problem design, sometimes making it impossible to distinguish the time-efficiency differences between programs; Grader interaction is exactly the opposite—because the overhead of a function call is small, it can often allow queries on the order of $10^6$, but the language restriction is its shortcoming.

If you design a problem or hold a contest yourself, you need to weigh and compare the two carefully.

## Communication problems

**Communication problems** are problems where two contestant programs need to communicate and cooperate to complete some task. The first program receives the problem's input and produces some output; the second program's input is related to the first's output (sometimes passed verbatim as a parameter, sometimes processed by the judging side), and it needs to produce the problem's solution.

Examples of communication problems include: [UOJ #178 New Year's Congratulatory Telegram](https://uoj.ac/problem/178), [#454 【UER #8】Snowball Fight](https://uoj.ac/problem/454), etc.

Local testing methods are many and varied due to different problem settings; common forms include:

-   Manual input
-   Writing a helper program to convert the first program's output into the second program's input
-   Connecting the two programs' standard input/output with a bidirectional pipe

Since judging platforms have limited support for communication problems, so far communication problems are only common in the IOI series and contests held by a few online platforms such as UOJ. It remains a field yet to be explored.

## Function-completion problems

**Function-completion problems** are problems where the contestant needs to complete a program. It can be understood as an interactive problem in which the problem provides the contestant's code and requires writing helper functions.

There are usually the following forms:

-   Given a program, being told where the code block to complete will be embedded.
-   No program is given, and the input information is passed as parameters of the function to be submitted.

This kind of problem is more common on [LeetCode](https://leetcode.com/) and [PTA - PinTia](https://pintia.cn/problem-sets).

## Other types

???+ note "Example [Quine](https://loj.ac/problem/4)"
    Write a program that can output its own source code.
    
    The code must contain at least ten visible characters.

The problem is classic, but it is hard to accomplish on the vast majority of OJs.

??? note "Reference code"
    **Note**: the source code does not include the first line below (i.e. `// clang-format off`).
    
    ```cpp
    // clang-format off
    #include<cstdio>
    
    char *s={"#include<cstdio>%cchar *s={%c%s%c};%cint main(){printf(s,10,34,s,34,10);return 0;}"};
    
    int main(){printf(s,10,34,s,34,10);return 0;}
    ```

## References and notes

[^note1]: Because of technical and resource limitations, a problem's test points in most cases cannot cover all data satisfying the data range.

[^note2]: For an interpreted language like Python, the interpreter directly interprets and runs the program.

[^note3]: In fact, the implementation of a judging system is far more complex than this; here we have only roughly introduced the judging process of a judging system.

[^note4]: To be precise, it is generally the program's user-mode time.

[^note5]: The judging results here mostly also apply to other types of problems.

[^note6]: Most judging systems classify the PE status as part of the WA status.

[^note7]: Some test points may have partial credit; the contestant can earn a certain proportion of the score when completing part of a test point's task, or when the contestant's output is correct but not optimal enough.
