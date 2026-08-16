author: Tiphereth-A, ShaoChenHeng, Enter-tainer, ksyx, c-forrest, StudyingFather, H-J-Granger, iamtwz, imp2002, Ir1d, kenlig, LeBronGod, Marcythm, MegaOwIer, NachtgeistW, ouuan, Patchouliys, Soohti, TianKong-y, sun2snow

## Introduction

Probability DP is used to solve probability problems and expectation problems; it is recommended to first have some understanding of the content of [probability & expectation](../math/probability/exp-var.md). Generally, solving a probability problem requires a forward loop, while solving an expectation problem uses a reverse loop. If the defined state-transition equation has an aftereffect problem, we also need to use [Gaussian elimination](../math/numerical/gauss.md) to optimize. Probability DP is also examined in combination with other knowledge, such as [bitmasking](./state.md), performing DP transitions on trees, etc.

## Probability DP

This kind of problem uses forward derivation, i.e. deriving from the initial state toward the result. Similar to general DP, the difficulty is still characterizing the state-transition equation, only that this kind of problem is wrapped in probability-theory knowledge.

### Example

???+ example "[Codeforces 148D Bag of mice](https://codeforces.com/problemset/problem/148/D)"
    A bag has $w$ white mice and $b$ black mice; the princess and the dragon take turns grabbing mice from the bag. Whoever grabs a white mouse first wins; if there are no mice left in the bag and no one has grabbed a white mouse, then the dragon wins. The princess grabs one mouse each time, and each time the dragon grabs a mouse, a mouse then runs out. Each grabbed mouse and each escaping mouse is random. The princess grabs first. Ask the probability that the princess wins.

??? note "Solution"
    Let $f_{i,j}$ be the probability that the princess wins when it is the princess's turn and the bag has $i$ white mice and $j$ black mice. Initialize the boundaries: $f_{0,j}=0$ because with no white mice left the dragon wins, and $f_{i,0}=1$ because grabbing one gives a white mouse and the princess wins.
    Consider the transition of $f_{i,j}$:
    
    -   The princess grabs a white mouse; the princess wins. The probability is $\dfrac{i}{i+j}$.
    -   The princess grabs a black mouse, the dragon grabs a white mouse; the dragon wins. The probability is $\dfrac{j}{i+j}\cdot\dfrac{i}{i+j-1}$.
    -   The princess grabs a black mouse, the dragon grabs a black mouse, a black mouse runs out; transition to $f_{i,j-3}$. The probability is $\dfrac{j}{i+j}\cdot\dfrac{j-1}{i+j-1}\cdot\dfrac{j-2}{i+j-2}$.
    -   The princess grabs a black mouse, the dragon grabs a black mouse, a white mouse runs out; transition to $f_{i-1,j-2}$. The probability is $\dfrac{j}{i+j}\cdot\dfrac{j-1}{i+j-1}\cdot\dfrac{i}{i+j-2}$.
    
    When considering the probability that the princess wins, the second case does not participate in the computation. And we must ensure the latter two cases are valid, so we also need to check the magnitudes of $i,j$: satisfying the third case requires at least 3 black mice, and satisfying the fourth case requires 1 white mouse and 2 black mice.

??? note "Reference code"
    ```cpp
    --8<-- "docs/dp/code/probability/probability_1.cpp"
    ```

### Exercises

-   [POJ3071 Football](http://poj.org/problem?id=3071)
-   [CodeForces 768D Jon and Orbs](https://codeforces.com/problemset/problem/768/D)

## Expectation DP

### Example

???+ example "[POJ2096 Collecting Bugs](http://poj.org/problem?id=2096)"
    A piece of software has $s$ subsystems and can produce $n$ kinds of bugs. Someone finds one bug per day; this bug belongs to some bug category and also to some subsystem. Each bug belongs to some subsystem with probability $\dfrac{1}{s}$ and to some bug category with probability $\dfrac{1}{n}$. Find the expected number of days to find $n$ kinds of bugs and have found bugs in all $s$ subsystems.

??? note "Solution"
    Let $f_{i,j}$ be the expected number of days to reach the goal state when $i$ bug categories and bugs of $j$ subsystems have already been found. The goal state here is finding $n$ bug categories and bugs of $s$ subsystems. Then $f_{n,s}=0$, because the goal state has already been reached and no more days are needed to find bugs, so we start the recurrence from the goal state; the answer is $f_{0,0}$.
    
    Consider the state transition of $f_{i,j}$:
    
    -   $f_{i,j}$: find a bug belonging to one of the already-found $i$ bug categories and $j$ subsystems, with probability $p_1=\dfrac{i}{n}\cdot\dfrac{j}{s}$.
    -   $f_{i,j+1}$: find a bug belonging to one of the already-found $i$ bug categories but not an already-found subsystem, with probability $p_2=\dfrac{i}{n}\cdot(1-\dfrac{j}{s})$.
    -   $f_{i+1,j}$: find a bug not belonging to an already-found bug category but to one of the $j$ subsystems, with probability $p_3=(1-\dfrac{i}{n})\cdot\dfrac{j}{s}$.
    -   $f_{i+1,j+1}$: find a bug not belonging to an already-found bug category and not an already-found subsystem, with probability $p_4=(1-\dfrac{i}{n})\cdot(1-\dfrac{j}{s})$.
    
    Then by the linearity of expectation, we can obtain the state-transition equation:
    
    $$
    \begin{aligned}
    f_{i,j} &= p_1\cdot f_{i,j}+p_2\cdot f_{i,j+1}+p_3\cdot f_{i+1,j}+p_4\cdot f_{i+1,j+1} + 1\\
    &= \dfrac{p_2\cdot f_{i,j+1}+p_3\cdot f_{i+1,j}+p_4\cdot f_{i+1,j+1}+1}{1-p_1}
    \end{aligned}
    $$

??? note "Reference code"
    ```cpp
    --8<-- "docs/dp/code/probability/probability_2.cpp"
    ```

???+ example "[「NOIP2016」Changing Classrooms](http://uoj.ac/problem/262)"
    Niuniu has classes in $n$ time slots; the $i$-th time slot is in classroom $c_i$, and can apply to switch to classroom $d_i$, with the application succeeding with probability $p_i$; at most $m$ classes can be applied to switch. After finishing the class in the $i$-th time slot, one must walk to the classroom of the $(i+1)$-th time slot; given a graph of $v$ classrooms and $e$ paths, moving consumes stamina; find which courses to apply to switch to minimize the expected total stamina consumed by moving between classrooms, i.e. find the minimum expected total distance.

??? note "Solution"
    For this undirected connected graph, first use Floyd to find the shortest paths, which brings convenience to the subsequent state transition. Taking one move as a stage (moving from the $i$-th time slot to the $(i+1)$-th time slot is one move), then each step goes to $d_i$ with probability $p_i$ (though only $m$ of all the $d_i$ can be selected) and to $c_i$ with probability $1-p_i$; find the minimum expected total distance after finishing the $n$ stages.
    
    Define $f_{i,j,0/1}$ as the minimum expected total distance at the $i$-th time slot when, including this time slot, $j$ classroom-switching opportunities have been used and this time slot switches (1) or does not switch (0) classroom; then the answer is $\min \{f_{n,i,0},f_{n,i,1}\} ,i\in[0,m]$. Note the boundaries $f_{1,0,0}=f_{1,1,1}=0$.
    
    Consider the state transition of $f_{i,j,0/1}$:
    
    -   If this stage does not switch, i.e. $f_{i,j,0}$. It may be transitioned from the previous non-switch state, which is $f_{i-1,j,0}+w_{c_{i-1},c_{i}}$, or from the previous switch state, which, analyzed with conditional and total probability, is $f_{i-1,j,1}+w_{d_{i-1},c_{i}}\cdot p_{i-1}+w_{c_{i-1},c_{i}}\cdot (1-p_{i-1})$; the state-transition equation is:
    
    $$
    \begin{aligned}
    f_{i,j,0}=min(f_{i-1,j,0}+w_{c_{i-1},c_{i}},f_{i-1,j,1}+w_{d_{i-1},c_{i}}\cdot p_{i-1}+w_{c_{i-1},c_{i}}\cdot (1-p_{i-1}))
    \end{aligned}
    $$
    
    -   If this stage switches, i.e. $f_{i,j,1}$. Similarly, it may be transitioned from the previous non-switch state or the previous switch state. Then multiply by $(1-p_i)$ when encountering the non-switch case, and by $p_i$ when encountering the switch case; just enumerate all possible cases and compute. We do not belabor the various transition cases here; through the previous stage example, the state transition here should be easy to write out.

??? note "Reference code"
    ```cpp
    --8<-- "docs/dp/code/probability/probability_3.cpp"
    ```

Comparing these two problems, we can see that whether a DP-for-expectation problem is finding a specific value or an optimization problem has some influence on the transition method the equation obtains, but whether DP for probability or DP for expectation, it always cannot do without probability knowledge and the steps of writing out and simplifying the computation formula, and the details to consider when writing the state-transition equation are similar.

### Exercises

-   [HDU3853 LOOPS](https://acm.hdu.edu.cn/showproblem.php?pid=3853)
-   [HDU4035 Maze](https://acm.hdu.edu.cn/showproblem.php?pid=4035)
-   [「SCOI2008」Bonus Stage](https://www.luogu.com.cn/problem/P2473)

## DP with aftereffect

### Example

???+ example "[CodeForces 24D Broken robot](https://codeforces.com/problemset/problem/24/D)"
    Given an $n \times m$ matrix region. A robot is initially at row $x$, column $y$; each step the robot equiprobably chooses to stay in place, move left one step, move right one step, or move down one step. If the robot is at a boundary it will not move out of the region; ask the expected number of steps for the robot to reach the last row.

??? note "Solution"
    When $m=1$, each time there is a $\dfrac{1}{2}$ probability of not moving and a $\dfrac{1}{2}$ probability of moving down one cell; the answer is $2\cdot (n-x)$.
    Let $f_{i,j}$ be the expected number of steps for the robot to reach the $n$-th row starting from row $i$, column $j$; the final state is $f_{n,j}=0$.
    Since the robot equiprobably chooses to stay in place, move left one step, move right one step, or move down one step, consider the state transition of $f_{i,j}$:
    
    -   $f_{i,1}=\dfrac{1}{3}\cdot(f_{i+1,1}+f_{i,2}+f_{i,1})+1$
    -   $f_{i,j}=\dfrac{1}{4}\cdot(f_{i,j}+f_{i,j-1}+f_{i,j+1}+f_{i+1,j})+1$
    -   $f_{i,m}=\dfrac{1}{3}\cdot(f_{i,m}+f_{i,m-1}+f_{i+1,m})+1$
    
    Between rows, since it can only move down, there is no aftereffect. Between columns it can move left and right, and cycles may arise during movement, so there is aftereffect.
    Transforming the equations gives:
    
    -   $2f_{i,1}-f_{i,2}=3+f_{i+1,1}$
    -   $3f_{i,j}-f_{i,j-1}-f_{i,j+1}=4+f_{i+1,j}$
    -   $2f_{i,m}-f_{i,m-1}=3+f_{i+1,m}$
    
    Since it is a reverse recurrence, each $f_{i+1,j}$ is known.
    Since there are $m$ columns, the right side is equivalent to an $m$-row column vector, so the left side is an $m$-by-$m$ matrix. Using the augmented matrix, it becomes an $m$-by-$(m+1)$ matrix, and then performing [Gaussian elimination](../math/numerical/gauss.md) solves the answer.

??? note "Reference code"
    ```cpp
    --8<-- "docs/dp/code/probability/probability_4.cpp"
    ```

### Exercises

-   [HDU 4418 Time Travel](https://acm.hdu.edu.cn/showproblem.php?pid=4418)
-   [「HNOI2013」Wandering](https://loj.ac/problem/2383)

## References

[kuangbin's Summary of Probability DP](https://www.cnblogs.com/kuangbin/archive/2012/10/02/2710606.html)
