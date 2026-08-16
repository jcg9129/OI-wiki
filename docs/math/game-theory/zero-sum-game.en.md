Prerequisites: [Introduction to game theory](./intro.md)

This article discusses (two-player) [zero-sum games](./intro.md#zero-sumnon-zero-sum-games).

In a zero-sum game, the sum of the two players' payoffs is always zero, and one party's gain necessarily means the other party's loss. A zero-sum game can be regarded as a special case of a constant-sum game. However, any constant-sum game can be equivalently transformed into a zero-sum game by adding or subtracting a constant to one party's payoffs as a whole, so we only need to discuss zero-sum games.

The zero-sum games commonly seen in competitive programming can roughly be divided into two classes: sequential zero-sum games and simultaneous zero-sum games.

## Sequential zero-sum games

In a sequential zero-sum game, the two players act in turn until the game terminates.

In a sequential zero-sum game, the players' payoff functions exhibit a recursive structure. The game positions $S$ can be divided into three classes, namely terminal positions $S_0$, positions where player $1$ acts $S_1$, and positions where player $2$ acts $S_2$. Suppose at a terminal position $s\in S_0$, player $1$'s payoff is $v(s)$, and correspondingly player $2$'s payoff is $-v(s)$. Therefore, when it is player $2$'s turn to act, maximizing their payoff is equivalent to minimizing player $1$'s payoff. From this, assuming both parties adopt optimal strategies, the maximum payoff $V(s)$ that player $1$ can obtain at position $s\in S$ satisfies the following recurrence relation:

$$
V(s) = \begin{cases}
v(s), & s \in S_0,\\
\max_{t\in s} V(t), & s\in S_1,\\
\min_{t\in s} V(t), & s\in S_2.
\end{cases}
$$

Here, $t\in s$ means $t$ is a successor position of $s$. This is the [minimax idea](../../search/alpha-beta.md#minimax-算法).

When applying this algorithm to actual problems, there are usually the following specific methods:

-   If the number of positions involved in the game is small, one can directly brute-force implement this algorithm.

-   If the number of positions involved in the game is relatively large and there is no special structure, one can consider [Alpha–Beta pruning](../../search/alpha-beta.md#alphabeta-剪枝) combined with other search-pruning algorithms.

-   If a single position in the game is often a successor position of multiple positions, to avoid repeated searching, one can consider memoized search or other dynamic-programming algorithms.

-   If a player's final payoff in the game is the sum of the payoffs of all actions before the end, one can appropriately optimize the modeling method. Specifically, suppose that when reaching the end $s\in S_0$, the action sequences of players $i=1,2$ are $\{a^{(i)}_j\}_{j=1}^{k_i}$ respectively, the payoff corresponding to an action $a$ is $w(a)$, and player $1$'s payoff function is

    $$
    v(s) = \sum_{j=1}^{k_1}w(a_j^{(1)}) - \sum_{j=1}^{k_2}w(a_j^{(2)}).
    $$

    Then, one can let $\tilde V(s)$ be the maximum score the current player can obtain in the game after position $s\in S$. For the initial state $s_0$, we have $V(s_0)=\tilde V(s_0)$, so finding $\tilde V(\cdot)$ suffices to solve the original problem. For $\tilde V(\cdot)$, we have the following recurrence relation:

    $$
    \tilde V(s) = \begin{cases}
    0, & s \in S_0, \\
    \max_{t\in s} w(a_{s\to t}) - \tilde V(t), & s\in S_1\cup S_2.
    \end{cases}
    $$

    Here, $a_{s\to t}$ denotes an action that can transition the state from $s$ to $t$; if there are multiple such actions, take the one with the highest payoff $w(a)$.

-   All impartial combinatorial games are sequential zero-sum games; one only needs to set the payoffs of the winner and loser in the game to $+1$ and $-1$ respectively. In this case, the recurrence relation of the payoff function $V(\cdot)$ is in fact the [lemma](./impartial-game.md#the-game-graph-and-states) for determining winning states and losing states.

    This kind of problem also has a common variant, namely finding the minimum number of rounds the winner needs and the maximum number of rounds the loser can hold out. To this end, one only needs to note that when doing BFS starting from the terminal states and determining winning states and losing states according to the lemma, recording the round number the BFS has reached when determining a winning state or a losing state gives the required number of rounds. This is because determining a winning state only requires that one successor state be a losing state, and it is always transitioned from the losing state with the smallest round number among the successor states; while determining a losing state requires all successor states to be winning states, and it is always transitioned from the winning state with the largest round number among the successor states.

    This method can likewise be generalized to general [games on directed graphs](./impartial-game.md#games-on-directed-graphs).

### Example problem

???+ example "[Codeforces 794 E. Choosing Carrot](https://codeforces.com/problemset/problem/794/E)"
    There is a sequence ${a_i}$ of length $n$. Two players $1$ and $2$ alternately take away a number from either end of the sequence, until only the last number remains in the sequence. Player $1$'s goal is to maximize this last remaining number, and player $2$'s goal is to minimize it. Before the game formally begins, player $1$ can also first perform $k$ actions. Assume both players adopt optimal strategies throughout. For each $k = 0,1,2,\cdots,n-1$, find the last remaining number when the game ends. Here, $1 \le n \le 3\times 10^5$.

??? note "Solution"
    Because no matter how the two parties take numbers, the remaining part of the sequence is always a complete interval. So, the position in the game can be described only by the interval $[l,r]$ and the currently acting player $i=1,2$, and can be solved using a dynamic-programming algorithm. Let $f(l,r,i)$ be the last remaining number in the game when the position is described by $(l,r,i)$. From the earlier analysis, when $l < r$, this function satisfies the state transition equation:
    
    $$
    \begin{aligned}
    f(l,r,1) &= \max\{f(l+1,r,2),f(l,r-1,2)\},\\
    f(l,r,2) &= \min\{f(l+1,r,1),f(l,r-1,1)\}.
    \end{aligned}
    $$
    
    The terminal condition is $f(l,l,1)=f(l,l,2) = a_l$. Based on this, one can find the function values of all possible positions in $\Theta(n^2)$ time. For each $k$, the answer is
    
    $$
    g(k) = \max f(l,r,1) \text{ subject to } r - l + 1 = k.
    $$
    
    This algorithm cannot pass the data range set by the original problem, so one needs to consider optimizing the transitions. There are many processing methods here; this article provides only one of them.
    
    Regard the state transition equation as an operation on the sequence as a whole. The two transition equations respectively represent taking the maximum and minimum of adjacent numbers to obtain a new sequence; call them the "maximization operation" and the "minimization operation" respectively. Each operation decreases the length of the sequence by one. There are a total of $(n-d+1)$ results corresponding to all intervals of length $d$, which is equivalent to the sequence obtained by performing $(d-1)$ operations on the sequence. In addition, to obtain the result $f(l,r,1)$, one needs to ensure that the last operation is a maximization operation. Therefore, the end of these operation sequences is always a maximization operation.
    
    Consider the change two consecutive operations bring to the sequence. Suppose one first does a minimization operation, then a maximization operation. In this case, the sequence $a_1,a_2,a_3$ becomes
    
    $$
    \max\{\min\{a_1,a_2\},\min\{a_2,a_3\}\}.
    $$
    
    Enumerating all possible size relationships among the three numbers $a_1,a_2,a_3$, one can see that except for the case $a_1 < a_2$ and $a_2 > a_3$ (i.e. $a_2$ is a strict maximum), this expression is always equal to $a_2$. That is, if a sequence has no strict maximum point, then the only effect of two consecutive operations on it is deleting one number from each end of the sequence. This obviously greatly simplifies the transition. The only remaining problem is: how to ensure the sequence has no strict maximum point? In fact, as long as one does a maximization operation on the sequence, one can ensure there is no strict maximum point. Therefore, the results of all even numbers of operations can be obtained by pairwise deleting the endpoint numbers from the sequence obtained by performing two operations on the initial sequence; the results of all odd numbers of operations can be obtained by pairwise deleting the endpoint numbers from the sequence obtained by performing one operation on the initial sequence.
    
    Since the complete operation on the sequence needs to be performed at most $3$ times, and the subsequent tallying of the answer only needs $2$ traversals, the total time complexity of this algorithm is $\Theta(n)$.

??? note "Reference code"
    ```cpp
    --8<-- "docs/math/code/zero-sum-game/zero-sum-game-1.cpp"
    ```

### Exercises

-   [Luogu P2734 \[USACO3.3\] 游戏 A Game](https://www.luogu.com.cn/problem/P2734)
-   [Luogu P4576 \[CQOI2013\] 棋盘游戏](https://www.luogu.com.cn/problem/P4576)
-   [Luogu P7097 \[yLOI2020\] 牵丝戏](https://www.luogu.com.cn/problem/P7097)
-   [Codeforces 388 C. Fox and Card Game](https://codeforces.com/problemset/problem/388/C)
-   [Codeforces 794 E. Choosing Carrot](https://codeforces.com/problemset/problem/794/E)
-   [Codeforces 1628 D2. Game on Sum (Hard Version)](https://codeforces.com/problemset/problem/1628/D2)
-   [Luogu P3210 \[HNOI2010\] 取石头游戏](https://www.luogu.com.cn/problem/P3210)

## Simultaneous zero-sum games

In a simultaneous zero-sum game, the two players act simultaneously.

Simultaneous zero-sum games are usually represented by a payoff matrix. Suppose the action set of player $i=1,2$ is $A_i$, and when players $i=1,2$ take actions $a_i\in A_i$ respectively, the two players' payoffs are $v(a_1,a_2)$ and $-v(a_1,a_2)$ respectively.

???+ example "Example"
    Consider the rock-paper-scissors game. Suppose a win scores $1$ point, a loss scores $-1$ point, and a tie scores $0$ points. Then, the two players' payoffs in the game can be represented as
    
    $$
    \begin{pmatrix}
    0,0 & 1,-1 & -1,1 \\
    -1,1 & 0,0 & 1,-1 \\
    1,-1 & -1,1 & 0,0
    \end{pmatrix}.
    $$
    
    A general two-player simultaneous game can also be represented in a similar form, so it is also called a [bimatrix game](https://en.wikipedia.org/wiki/Bimatrix_game). For a zero-sum game, since player $1$'s payoff matrix and player $2$'s payoff matrix are negatives of each other, one can consider only player $1$'s payoff matrix:
    
    $$
    V = (v(a_1,a_2))_{(a_1,a_2)\in A_1\times A_2} = \begin{pmatrix}
    0 & 1 & -1 \\
    -1 & 0 & 1 \\
    1 & -1 & 0
    \end{pmatrix}.
    $$

The problem to be solved is: given the payoff matrix $V = (v(a_1,a_2))_{(a_1,a_2)\in A_1\times A_2}$, how does one find the two players' optimal strategies and maximum payoffs?

### Mixed strategies

Compared with sequential zero-sum games, the roles of the two players in a simultaneous game are symmetric. But, since we have already solved sequential zero-sum games, one may consider the sequential version of the simultaneous game. For example, if we assume player $1$ acts first and player $2$ acts afterward, then, by the earlier discussion, player $1$'s payoff at the end of the game will be given by

$$
w_-=\max_{a_1\in A_1}\min_{a_2\in A_2} v(a_1,a_2).
$$

Since player $1$'s action is unidirectionally transparent to player $2$, this should be the worst result player $1$ can obtain. Symmetrically, if we assume player $2$ acts first, then player $1$'s payoff will be given by

$$
w_+ = \min_{a_2\in A_2}\max_{a_1\in A_1} v(a_1,a_2).
$$

Since player $2$'s action is unidirectionally transparent to player $1$, this should be the best result player $1$ can obtain. Player $1$ should expect that, when actually playing the game, the payoff they can obtain $w\in[w_-,w_+]$. Although the inequality $w_-\le w_+$ always holds (for the proof see the [weak duality theorem](../linear-programming.md#duality-principle)), since equality does not necessarily hold, using only the analytical means of sequential games, in general there is no way to uniquely determine the game result.

???+ example "Example (continued)"
    In the rock-paper-scissors game, if there is an order to the moves, then the first mover necessarily loses and the second mover necessarily wins. Converted to mathematical language, this is the following inequality:
    
    $$
    w_- = -1 \le +1 = w_+.
    $$
    
    In this case, $w_-\neq w_+$ does not hold.

The above analysis process omits a key factor of the simultaneous game, namely that a player cannot accurately predict the opponent's action. Formally, this means both parties can adopt some random strategy. This idea does not hold in the context of sequential games, because no matter how the first mover randomly chooses an action, the second mover can always accurately observe this action and respond in a targeted way. But for a simultaneous game, the strategic ambiguity introduced by a random strategy makes it impossible for the opponent to effectively target one's own action.

???+ example "Example (continued)"
    In the rock-paper-scissors game, if player $1$ chooses one of the three actions scissors, rock, paper uniformly at random, then, depending on player $2$'s action, the payoffs player $1$ may obtain are
    
    $$
    \dfrac{1}{3}(0,1,-1)^T + \dfrac{1}{3}(-1,0,1)^T + \dfrac{1}{3}(1,-1,0)^T = (0,0,0)^T.
    $$
    
    In this case, no matter how player $2$ chooses an action, player $1$'s expected payoff is always $0$. This is obviously better than deterministically choosing a single action.

From this, we introduce the concept of a mixed strategy.

???+ abstract "Mixed strategy"
    In a simultaneous game, a **mixed strategy** of player $i$, called a **strategy** for short, is a function $s_i:A_i\to[0,1]$ satisfying $\sum_{a_i\in A_i}s_i(a_i)=1$. That is, a strategy $s_i$ is a probability distribution over player $i$'s action set $A_i$. The set of all mixed strategies of player $i$ is denoted $S_i=\Delta(A_i)$, where $\Delta(A_i)$ denotes the set of all probability distributions over $A_i$. If $s_i$ is a degenerate probability distribution, i.e. there exists $a\in A_i$ such that $s_i(a)=1$, then the strategy $s_i$ is also called a **pure strategy**.

The payoff of a mixed strategy is the expectation of the payoffs of the individual actions:

$$
v(s_1,s_2) = \sum_{a_1\in A_1}\sum_{a_2\in A_2}s_1(a_1)s_2(a_2)v(a_1,a_2).
$$

Regarding a single action as the corresponding pure strategy, one can embed the action set $A_i$ into the (mixed) strategy set $S_i$, and the $v(s_1,s_2)$ defined above can be regarded as extending $v(a_1,a_2)$ from $A_1\times A_2$ to $S_1\times S_2$.

### von Neumann's theorem

After introducing mixed strategies, the results obtained by the maximin idea and the minimax idea are consistent, and from this the result of a simultaneous zero-sum game is also uniquely determined.

???+ note "Theorem (von Neumann)"
    In a simultaneous zero-sum game allowing mixed strategies, if both parties adopt optimal strategies, then player $1$'s maximum payoff is
    
    $$
    w = \max_{s_1\in S_1}\min_{s_2\in S_2} v(s_1,s_2) = \min_{s_2\in S_2}\max_{s_1\in S_1} v(s_1,s_2),
    $$
    
    and player $2$'s maximum payoff is $-w$.

??? note "Proof"
    Let $w = \max_{s_1\in S_1}\min_{s_2\in S_2} v(s_1,s_2)$. Consider the inner minimization problem; because $v(s_1,s_2)=\sum_{a_2\in A_2}s_2(a_2)v(s_1,a_2)$, we have $\max_{s_2\in S_2}v(s_1,s_2)=\max_{a_2\in A_2}v(s_1,a_2)$, and the optimal solution of the former is the pure strategy corresponding to the optimal solution of the latter. Therefore, $w = \max_{s_1\in S_1}\min_{a_2\in A_2} v(s_1,a_2)$. Furthermore, introducing an auxiliary variable $u$, the problem can be rewritten as
    
    $$
    w = \max_{s_1\in S_1} u \text{ subject to }u \le \min_{a_2\in A_2} v(s_1,a_2).
    $$
    
    Because this constraint is equivalent to $u\le v(s_1,a_2)$ holding for all $a_2\in A_2$. Finally, introducing the definition of the mixed strategy $s_1$ and the expression of the payoff function $v(s_1,a_2)$, the original problem is equivalent to the [linear programming problem](../linear-programming.md)
    
    $$
    (P) \qquad
    \begin{aligned}
    w = \max_{u,s_1}\; & u\\
    \text{subject to }& \sum_{a_1\in A_1}s_1(a_1)v(a_1,a_2) \ge u,~\forall a_2\in A_2,\\
    & \sum_{a_1\in A_1}s_1(a_1) = 1,\\
    & s_1(a_1) \ge 0,~\forall a_1\in A_1.
    \end{aligned}
    $$
    
    This problem is obviously feasible, and the optimal solution has a solution. By the [duality principle](../linear-programming.md#duality-principle), its optimal solution equals the optimal solution of the dual problem:
    
    $$
    (D) \qquad
    \begin{aligned}
    w = \min_{t,s_2}\; & t\\
    \text{subject to }&\sum_{a_2\in A_2}s_2(a_2)v(a_1,a_2) \le t,~\forall a_1\in A_1,\\
    &\sum_{a_2\in A_2}s_2(a_2) = 1,\\
    &s_2(a_2)\ge 0,~\forall a_2\in A_2.
    \end{aligned}
    $$
    
    Repeating the earlier steps, this problem is equivalent to $\min_{s_2\in A_2}\min_{s_1\in S_1}v(s_1,s_2)$. The theorem is proved.

This result is precisely the [Nash equilibrium](https://en.wikipedia.org/wiki/Nash_equilibrium) of this game. That is, assuming both parties choose the optimal strategy in the equilibrium, then no player can strictly benefit from deviating from the equilibrium strategy.

### Transforming into a linear programming problem

The proof of von Neumann's theorem also points out the method for solving a simultaneous zero-sum game. Let $n$ and $m$ be the numbers of actions players $1$ and $2$ can take respectively. Given player $1$'s payoff matrix $V\in\mathbf R^{n\times m}$, one can solve the following linear programming problem:

$$
\begin{aligned}
w = \max_{(u,s)\in\mathbf R\times\mathbf R^n}\; & u\\
\text{subject to }& V^Ts \ge u\mathbf 1,\\
& \mathbf 1^Ts = 1,\\
& s \ge 0.
\end{aligned}
$$

This is a linear programming problem of size $\Theta(n+m)$, which can be efficiently solved with the [simplex method](../simplex.md). The optimal solution $s$ obtained by the algorithm is player $1$'s optimal (mixed) strategy. To find player $2$'s optimal strategy, one only needs to obtain the dual variables (i.e. shadow prices) of the optimal solution of this problem from the simplex tableau.

### Exercises

-   [Luogu P4232 无意识之外的捉迷藏](https://www.luogu.com.cn/problem/P4232)

## References and notes

-   [Zero-sum game - Wikipedia](https://en.wikipedia.org/wiki/Zero-sum_game)
-   [Minimax theorem - Wikipedia](https://en.wikipedia.org/wiki/Minimax_theorem)
