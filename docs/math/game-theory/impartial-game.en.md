author: cutekibry, woruo27, tinjyu, 2008verser, Backl1ght, billchenchina, Enter-tainer, FFjet, Ir1d, Molmin, orzAtalod, ouuan, SaMiiKaaaa, SamZhangQingChuan, Tiphereth-A, chu-yuehan

Prerequisites: [Introduction to game theory](./intro.md)

This article discusses [impartial combinatorial games](./intro.md#impartial-combinatorial-games).

Among impartial combinatorial games, the most basic and important is the normal Nim game. The Sprague–Grundy theorem states that all impartial combinatorial games with normal rules are equivalent to a single-pile Nim game. From this, one can develop the concepts of the Sprague–Grundy function and the Nim number, which completely characterize an impartial combinatorial game with normal rules. Therefore, this article first establishes the conclusions of the normal Nim game and the Sprague–Grundy theory. Subsequently, this article discusses some impartial combinatorial games commonly seen in competitive programming.

Finally, this article briefly discusses the misère Nim game. Misère games are much more complex than normal games, and rarely appear in competitive programming. Unless otherwise stated, the games mentioned in this article are by default normal impartial combinatorial games.

???+ info "\"State\", \"position\", and \"game\""
    This article uses these three terms interchangeably. In game theory, the state of a game usually includes all information possibly relevant to the game up to a certain moment. In general, the state of a game usually includes both players' past actions, the realized values of random variables, the contents of both players' known information, etc. The position of a game is relatively not a standard term in game theory, usually referring to the situation faced by both players at a certain moment of the game, such as the positions of the pieces in a board game. Only for impartial combinatorial games (or more generally zero-sum, deterministic, perfect-information games), since the game involves no randomness, and the players' future action sets and payoff functions are independent of the historical path leading to the current position (i.e. the previous behaviors of both parties), the state and the position of the game are no different, and both can be regarded as a node in the game graph. Since a game can always be described by its initial position, the word "position" is sometimes used directly to refer to the game itself.

## Nim game

The rules of the Nim game are very simple:

???+ abstract "Nim game"
    There are $n$ piles of stones in total, with the $i$-th pile having $a_i$ stones. Two players alternately take away any number of stones from any one pile, but cannot take none. The player who takes away the last stone wins.

It is easy to verify that the Nim game is an impartial combinatorial game with normal rules.

???+ example "Example"
    Let us give an example. Currently, there are $3$ piles of stones, with numbers of stones $2,5,4$ respectively. Then one can take away the $2$ items in the $1$st pile, and the position becomes $0, 5, 4$; or take away the $4$ items in the $2$nd pile, and the position becomes $2, 1, 4$. If at some moment the position becomes $0, 0, 5$, and A takes away the $5$ items in the $3$rd pile, i.e. takes away the last item, then A wins.

### The game graph and states

In the Nim game, the possible changes of positions can be described by a game graph.

Treating each possible state as a node in the graph, and connecting a state to its successor states (i.e. states reachable via one operation) with edges, one obtains a directed acyclic graph, which is the game graph. The graph is acyclic because in the Nim game, each operation strictly decreases the total number of stones.

???+ example "Example"
    For example, for a Nim game whose initial position has $3$ piles of stones with numbers $1,1,2$ respectively, one can draw the following game graph:
    
    ![Example of a game graph](./images/nim.svg)
    
    As will be mentioned shortly, the red nodes in the graph represent winning states, and the black nodes represent losing states.

Since the Nim game is an impartial combinatorial game, whether a player has a winning strategy depends only on the current state of the game and is independent of the player's identity. Therefore, all states can be divided into (first-player) **winning states** and (first-player) **losing states**, denoted the $\mathcal N$ state and the $\mathcal P$ state respectively[^n-vs-p]. This definition applies to all impartial combinatorial games.

Through the following lemma, one can inductively label all states as winning states and losing states:<a id="np-lem"></a>

???+ note "Lemma"
    In an impartial combinatorial game with normal rules,
    
    1.  a state with no successor state is a losing state $\mathcal P$,
    2.  a state is a winning state $\mathcal N$ if and only if at least one of its successor states is a losing state $\mathcal P$,
    3.  a state is a losing state $\mathcal P$ if and only if all of its successor states are winning states $\mathcal N$.

??? note "Proof"
    For the first, if the player currently has no available action, then the player has already lost the game.
    
    For the second, if this state has at least one successor state that is a losing state, then the player can move to that losing state; at this point, the opponent faces a first-player-losing state, and the player themselves wins.
    
    For the third, if there is no successor state that is a losing state, then no matter what, the player can only move to a winning state; at this point, the opponent faces a first-player-winning state, and the player themselves loses the game.

In all impartial combinatorial games, the game graph is a directed acyclic graph. So, through these three properties, one can, after drawing the game graph, compute in $O(|V|+|E|)$ time whether each state is a winning state or a losing state. Here, $|V|$ is the number of states in the game graph, and $|E|$ is the number of edges, i.e. the total number of actions all states can take.

This lemma can be generalized to misère games and to the case where the directed graph may have cycles. For the relevant discussion, see the section [games on directed graphs](#games-on-directed-graphs).

### Nim sum

Let us continue examining the Nim game.

By drawing the game graph, one can determine in $\Omega(\prod_{i=1}^na_i)$ time whether a certain position is a first-player win. But the complexity of doing so is too high to be applied in practice. In fact, one can find that whether a state of the Nim game is a first-player win is related only to the Nim sum of the numbers of stones in the current position.

???+ abstract "Nim sum"
    The **Nim sum** of the natural numbers $a_1,a_2,\cdots,a_n$ is defined as $a_1\oplus a_2\oplus\cdots\oplus a_n$.

The so-called Nim sum is the [XOR operation](../bit.md#bit-operations).

???+ note "Theorem"
    In the Nim game, the state $(a_1,a_2,\cdots,a_n)$ is a losing state $\mathcal P$ if and only if the Nim sum
    
    $$
    a_1\oplus a_2\oplus\cdots\oplus a_n = 0.
    $$

??? note "Proof"
    Apply induction over all possible states:
    
    1.  If $a_i=0$ holds for all $i=1,\cdots,n$, this state has no successor state, and the Nim sum equals $0$, so the proposition holds.
    2.  If $k = a_1\oplus a_2\oplus\cdots\oplus a_n\neq 0$, then we need to prove that this state is a winning state. That is, we need to construct a legal move such that the successor state is a losing state; by the induction hypothesis, we only need to prove that the successor state satisfies $a'_1\oplus a'_2\oplus\cdots\oplus a'_n=0$. Using the property of the Nim sum (i.e. XOR), this is equivalent to saying that there exists a pile of stones from which taking away some stones from $a_i$ can yield $a_i\oplus k$, i.e. $a_i>a_i\oplus k$.
    
        In fact, let the highest $1$ in the binary representation of $k$ be at bit $d$. Then there must exist some $a_i$ whose $d$-th binary bit is $1$. For the corresponding pile of stones, we must have $a_i>a_i\oplus k$, because bit $d$ of $a_i\oplus k$ is $0$, and the higher bits are the same as $a_i$.
    3.  If $a_1\oplus a_2\oplus\cdots\oplus a_n= 0$, then we need to prove that this state is a losing state. By the induction hypothesis, we only need to prove that the Nim sums of all its successor states are not $0$. This is inevitable: any legal move that changes $a_i$ to $a'_i\neq a_i$ necessarily makes the Nim sum become $a'_i\oplus a_i\neq 0$.

From this, one can determine in $O(n)$ time whether a state of the Nim game is a first-player-winning state.

## Sprague–Grundy theory

The Sprague–Grundy theory states that all impartial combinatorial games are equivalent to a single-pile Nim game. The main scenario in which this conclusion is applied is when a game is composed of multiple mutually independent subgames. In this case, the state determination of the game can be completed by computing the Nim sum of the SG function values of the subgames. If the game itself does not have such a structure, then determining winning states and losing states only requires applying the [lemma](#np-lem) from the earlier game-graph section.

### Notation for games

It has already been explained that all impartial combinatorial games can be described by drawing a game graph. Since in a game graph, the property of each state is determined only by its successor states, a state $S$ in the game graph can be represented by the set of its successor states.

???+ example "Example (continued)"
    Taking the game graph above as an example, one can obtain the following state representations:
    
    $$
    \begin{aligned}
    S_{0,0,0} &= \{\},\\
    S_{0,1,0} &= \{S_{0,0,0}\} = \{\{\}\},\\
    S_{0,0,1} &= \{S_{0,0,0}\} = \{\{\}\},\\
    S_{0,0,2} &= \{S_{0,0,0},S_{0,0,1}\} = \{\{\},\{\{\}\}\},\\
    S_{0,1,1} &= \{S_{0,0,0},S_{0,1,0},S_{0,0,1}\} = \{\{\},\{\{\}\}\},\\
    S_{0,1,2} &= \{S_{0,0,2},S_{0,1,0},S_{0,1,1}\} = \{\{\{\}\},\{\{\},\{\{\}\}\}\}.
    \end{aligned}
    $$
    
    Here, $S_{0,1,0}=S_{0,0,1}$, $S_{0,0,2}=S_{0,1,1}$.

A game can be represented by its initial state.

Although the representation of an impartial game may be quite complex, the single-pile Nim game is relatively much simpler. With only one pile of stones and number of stones $n$, it can be represented as

$$
*0 = \{\},~*n = \{*m : m<n,~m\in\mathbf N\} = \{*0,*1,\cdots,*(n-1)\}.
$$

Here, the notation $*n$ denotes (the initial state of) the single-pile Nim game with number of stones $n$.

???+ example "Example (continued)"
    Using this notation, the states in the above example can be simply represented as
    
    $$
    S_{0,0,0} = *0,~
    S_{0,1,0} = S_{0,0,1} = *1,~
    S_{0,0,2} = S_{0,1,1} = *2,~
    S_{0,1,2} = \{*1, *2\}.
    $$

In the subsequent discussion, the notation $T\in S$ should be understood as: state $T$ is a successor state of state $S$.

### Sum and equivalence of games

The equivalence relation of games depends on the concept of the sum[^more-sums] of games.

???+ note "Sum of games"
    The **sum** of games $G$ and $H$, also called the **combined game**, denoted $G+H$, is the game
    
    $$
    G + H = \{g + H : g \in G\} \cup \{G + h : h \in H\}.
    $$

The sum of games can be understood as a game composed of two subgames that are played simultaneously and do not interfere with each other; at each step the player can and must choose exactly one of the subgames to move one step in, and the game ends when neither subgame can be moved. The concept of the sum of games can be generalized to any number of games, and satisfies associativity and commutativity—that is, the result of combining multiple games is independent of both the order of combination and the order of the games. The Nim game is the sum of multiple single-pile Nim games.

One observation is that although in single-pile Nim games, except for the case of no stones, all are first-player-winning states, these different single-pile Nim games, when combined with other single-pile Nim games, give different games. For example, the game $*n$ can only give a losing game when combined with another $*n$; combined with all other games $*n'\neq *n$, the resulting game is a winning game.

The inspiration this observation brings is that one can study the properties of a game by examining its sums with other games. This leads to the concept of the equivalence of games.

???+ abstract "Equivalence relation of games"
    If for all games $H$, the games $G_1+H$ and $G_2+H$ are both in a losing state or both in a winning state, then the games $G_1$ and $G_2$ are said to be **equivalent**, denoted $G_1\approx G_2$.

It is easy to verify that $\approx$ defined this way is indeed an [equivalence relation](../order-theory.md#二元关系) on all impartial games.

### Sprague–Grundy function

The analysis of the Nim game shows that different single-pile Nim games are not equivalent to one another. But all impartial games are equivalent to some single-pile Nim game. From this, one can assign a number to each impartial game, which is the Sprague–Grundy function.

To prove these conclusions, we first need to establish two lemmas about the equivalence relation of games. First, combining a losing game with any game gives a game equivalent to the original game.

???+ note "Lemma 1"
    For a game $G$ and any losing game $A\in\mathcal P$, we have $G\approx G + A$.

??? note "Proof"
    By definition, we only need to prove that $G+H\approx G+A+H$ holds for any game $H$.
    
    If the game $G+H$ has a winning strategy, then the game $G+A+H$ also has a winning strategy. If the opponent makes a move in the subgame $A$, make a move to restore it to a losing state; otherwise, move according to the winning strategy in the game $G+H$. This is sure to guarantee eventual victory.
    
    If the game $G+H$ is a losing game, then the game $G+A+H$ is likewise a losing game. Because no matter whether the move this round is in the subgame $G+H$ or the subgame $A$, the opponent can restore the corresponding subgame to a losing state next round. Eventually, the first player is sure to be unable to win.

Second, two games are equivalent if and only if their sum is a losing game. This lemma provides a method for proving that two games are equivalent.

<a id="sg-lem-2"></a>

???+ note "Lemma 2"
    Games $G$ and $G'$ are equivalent if and only if $G+G'\in\mathcal P$ is a losing game.

??? note "Proof"
    If games $G$ and $G'$ are equivalent, then $G+G'$ and $G+G$ are simultaneously winning or simultaneously losing, and the game $G+G$ is a losing game. This is because, for any operation by the first player, the second player can take the same action in the other subgame, and in the end the first player is sure to be unable to move.
    
    Conversely, if $G+G'$ is a losing game, then by Lemma 1, $G\approx G+(G+G') = (G+G)+G' \approx G'$.

Using these lemmas, one can obtain the following theorem:

???+ note "Theorem (Sprague–Grundy)"
    For any (finite) impartial game $G$, there exists $n\in\mathbf N$ such that $G\approx *n$ holds.

??? note "Proof"
    To prove the conclusion of the theorem, one can apply mathematical induction. Let the game $G = \{G_1,G_2,\cdots,G_k\}$. By the induction hypothesis, there exist $n_1,n_2,\cdots,n_k$ such that $G_i\approx *n_i$; then, one can examine the game
    
    $$
    G' = \{*n_1,*n_2,\cdots,*n_k\}.
    $$
    
    What we will prove is $G'\approx *m$, where $m=\operatorname{mex}\{n_1,n_2,\cdots,n_k\}$ is the smallest natural number not appearing in the set.
    
    In the first step, we need to show $G\approx G'$. By [Lemma 2](#sg-lem-2), we only need to prove that the game $G+G'$ is a losing game. Without loss of generality, assume $G\neq *0$. If the first player chooses $G_i$, then the second player can choose $*n_i$; conversely, if the first player chooses $*n_i$, the second player can choose $G_i$. In any case, after these two operations, the game becomes $G_i+*n_i$, which by Lemma 2 and $G_i\approx *n_i$ is a losing game. This proves $G\approx G'$.
    
    In the second step, we need to show $G'\approx*m$. By [Lemma 2](#sg-lem-2), we only need to prove that $G'+*m$ is a losing game. Without loss of generality, assume $G'\neq *0$. If the first player chooses $*n_i\in *m$, then by the definition of $m$, the second player can choose $*n_i\in G'$, changing the game position to $*n_i + *n_i\in\mathcal P$, a first-player loss. If the first player chooses $*n_i\in G'$ with $n_i<m$, then the second player can choose $*n_i\in *m$, and the game position likewise becomes $*n_i+*n_i\in\mathcal P$, a first-player loss. Finally, if the first player chooses $*n_i\in G'$ with $n_i>m$, then the second player can choose $*m\in *n_i$, and the game position becomes $*m+*m\in\mathcal P$, a first-player loss. This proves $G'\approx *m$.
    
    By the transitivity of the equivalence relation, $G\approx *m$. This completes the induction, proving that all games $G$ are equivalent to a single-pile Nim game.

This conclusion shows that one can assign to each impartial game $G$ a natural number $n$ such that $G\approx *n$.

???+ abstract "Nim number"
    The **Nim number** (nimber) corresponding to an impartial game $G$ is the unique natural number $n$ such that $G\approx *n$ holds.

This function mapping impartial games to Nim numbers is called the **Sprague–Grundy function**, or **SG function** for short, denoted $\operatorname{SG}(\cdot)$. Since the state of each impartial game is another impartial game, one can compute the corresponding Nim number, also called the corresponding SG function value, for each state of an impartial game.

According to the proof process of the theorem in this section, the Sprague–Grundy function can be computed recursively as follows:

???+ note "Corollary"
    The Sprague–Grundy function value $\operatorname{SG}(x)$ corresponding to a state $x$ in an impartial game $G$ satisfies
    
    $$
    \operatorname{SG}(x) = \operatorname{mex}\{\operatorname{SG}(x'): x'\in x\}.
    $$
    
    Here, $\operatorname{mex}(A):=\min\{n\in\mathbf N:n\notin A\}$ is the smallest natural number not appearing in the set $A$.

That is, the SG function value of a state equals the $\operatorname{mex}$ value of the SG function values of all its successor states.

Using the SG function value (i.e. the Nim number), one can determine whether a state is a first-player-winning state.

???+ note "Corollary"
    A state $x$ in an impartial game $G$ is a first-player-winning state if and only if $\operatorname{SG}(x)\neq 0$.

Finally, the SG function value of the sum of games is the Nim sum (i.e. XOR) of the SG function values of the subgames.

???+ note "Theorem (Sprague–Grundy)"
    For impartial games $G_1,G_2,\cdots,G_n$, we have
    
    $$
    \operatorname{SG}(G_1+ G_2+\cdots + G_n) = \operatorname{SG}(G_1)\oplus \operatorname{SG}(G_2)\oplus\cdots\oplus\operatorname{SG}(G_n).
    $$

??? note "Proof"
    Because $*a_1+ *a_2 + \cdots + *a_n$ is precisely the Nim game with numbers of stones $(a_1,a_2,\cdots,a_n)$, by the conclusion of the Nim game, the game
    
    $$
    *a_1+ *a_2 + \cdots + *a_n + *(a_1\oplus a_2\oplus\cdots\oplus a_n)
    $$
    
    is a first-player loss. By [Lemma 2](#sg-lem-2), we have
    
    $$
    *a_1+ *a_2 + \cdots + *a_n \approx *(a_1\oplus a_2\oplus\cdots\oplus a_n).
    $$
    
    So, we have
    
    $$
    \operatorname{SG}(*a_1 + *a_2 + \cdots + *a_n) = a_1\oplus a_2\oplus\cdots\oplus a_n.
    $$
    
    Let $a_i=\operatorname{SG}(G_i)$; then $G_i\approx *a_i$, so using the algebraic properties of $\approx$, we have
    
    $$
    (G_1+ G_2+\cdots + G_n) + (*a_1 + *a_2 + \cdots + *a_n) = \sum_{i=1}^n(G_i+*a_i) \in\mathcal P.
    $$
    
    So, we have
    
    $$
    \begin{aligned}
    \operatorname{SG}(G_1+ G_2+\cdots + G_n) &= \operatorname{SG}(*a_1 + *a_2 + \cdots + *a_n) \\
    &= a_1\oplus a_2\oplus \cdots \oplus a_n \\
    &= \operatorname{SG}(G_1)\oplus \operatorname{SG}(G_2)\oplus\cdots\oplus\operatorname{SG}(G_n).
    \end{aligned}
    $$

Using this theorem, one can greatly simplify the computation when computing the SG function value of the sum of games.

From this, one can summarize the computation method for SG function values:

-   For multiple independent games, one can compute their SG function values separately, then take the Nim sum;
-   For a single game, the SG function value of each state is the $\operatorname{mex}$ value of the SG function values of all its successor states;
-   In particular, the SG function value of a terminal state (i.e. a state with no successor state) is $\operatorname{mex}\varnothing = 0$.

### Nim numbers

All impartial games correspond uniquely to a Nim number. The set of (finite) Nim numbers is precisely the set of natural numbers $\mathbf N$. But its algebraic properties are different from those of the set of natural numbers. Specifically, on Nim numbers one can define two operations, the Nim sum $\oplus$ and the Nim product $\otimes$:

???+ abstract "Operations on Nim numbers"
    For Nim numbers $a,b$, one can define:
    
    -   the Nim sum $a\oplus b=\operatorname{mex}(\{a'\oplus b:a'<a,~a'\in\mathbf N\}\cup\{a\oplus b':b'<b,~b'\in\mathbf N\})$,
    -   the Nim product $a\otimes b=\operatorname{mex}(\{(a'\otimes b)\oplus(a\otimes b')\oplus(a'\otimes b'):a'<a,~b'<b,~a',b'\in\mathbf N\})$.

All Nim numbers under the operations $\oplus$ and $\otimes$ form a [field](../algebra/basic.md#fields) of characteristic $2$. Moreover, these operations and their inverse operations are closed for the first $2^{2^n}$ Nim numbers; this gives a series of [finite fields](../algebra/field-theory.md#finite-field) $\mathbf F_{2^{2^n}}$ of size $2^{2^n}$.

## Common impartial games

Although the Sprague–Grundy theory completely solves the problem of impartial games, when handling actual impartial games, directly applying the Sprague–Grundy theorem is still not efficient. For example, in the Nim game, the complexity of brute-force computation of the Sprague–Grundy value is exponential. Therefore, one often needs to guess the conclusion of a specific impartial game by tabulating.

This section lists some common impartial games and their conclusions. When stating the conclusions, this section only gives the criteria for determining winning and losing states. As for the winning strategy, it is to perform an appropriate operation such that the position left to the opponent is exactly a losing state. Since variants of these games frequently appear in competitive programming, mastering the proof process of each game's conclusion is also important.

???+ info "Proof method for the conclusions in this section"
    The proofs of the conclusions in this section are all verificational. For a game, the conclusion describes its first-player-losing states and first-player-winning states. In the proof, one only needs to verify that starting from a first-player-losing state, one can only reach first-player-winning states; and starting from a first-player-winning state, one can always reach at least one first-player-losing state. To rewrite these proofs as rigorous proofs, one needs to establish the game graph and then apply mathematical induction to the states on the game graph, and these verification steps are the inductive part of it.

### Bachet's game

Compared with the single-pile Nim game, Bachet's game limits the number of stones that can be taken each time.

???+ abstract "Bachet's game"
    There is a pile of stones, $n$ in total. Two players alternately take away at least $1$ and at most $k$ stones. The player who takes away the last stone wins.

For this, we have the following conclusion:

???+ note "Theorem"
    The first player loses if and only if $n\equiv 0\pmod {k+1}$.

??? note "Proof 1"
    When $n\not\equiv 0\pmod {k+1}$, as long as one takes away $n\bmod{(k+1)}\in[1,k]$ stones, one can guarantee that the opponent is in a losing state. Therefore, this is a first-player-winning state.
    
    Conversely, when $n\equiv 0\pmod {k+1}$, then either there is no choice, or after taking away $k'$ stones oneself, the opponent can immediately take away $k+1-k'$ stones, returning oneself to a losing state.

??? note "Proof 2"
    As an application of the Sprague–Grundy theorem, one can compute $f(n)$ as the SG function value of the position corresponding to only $n$ stones remaining.
    
    For $n\le k$, one can inductively prove $f(n)=n$. This is the same as the single-pile Nim game, because the limit on the number of stones taken does not come into play. For $n>k$, one can prove $f(n)=n\bmod{(k+1)}$, so we have
    
    $$
    f(n) = \operatorname{mex}\{f(n-k),f(n-k+1),\cdots,f(n-1)\}.
    $$
    
    This ranges over all residues modulo $k+1$ except $n\bmod{(k+1)}$. Therefore, $f(n) = n\bmod{(k+1)}$.

### Moore's Nim-k game

Compared with the Nim game, Moore's Nim-$k$ game allows taking stones from $k$ piles at once.

???+ abstract "Moore's Nim-$k$ game"
    There are $n$ piles of stones in total, with the $i$-th pile having $a_i$ stones. Two players alternately take away any number of stones from at least $1$ and at most $k$ piles, but cannot take none. The player who takes away the last stone wins.

For this, we have the following conclusion:

???+ note "Theorem"
    Represent the number of stones in each pile as a binary number, and for each bit $d$, count how many piles have a $1$ in the $d$-th bit of their number of stones, and compute the residue of this count modulo $(k+1)$. If for every bit this residue equals $0$, then the first player loses; otherwise, the first player wins.

??? note "Proof"
    Following the proof of the conclusion of the Nim game, this conclusion is easily proved. Let $d$ be the highest binary bit whose residue is not $0$, with corresponding residue $k'\le k$. Then, the winning strategy is: among the piles whose number of stones has a $1$ in the $d$-th binary bit, choose $k$ piles, and choose the numbers of stones to remove such that in the opponent's position, the residue of every bit is $0$. The only thing that needs to be explained is that the choice of the number of stones taken at the end is always feasible.
    
    In fact, as long as one selects $k'$ piles of stones and takes away $2^d$ stones from each, one can make the residue of the $d$-th bit in the result become $0$. For the residues of the lower bits, distribute these residues arbitrarily among some pile.

### Staircase Nim game

The staircase Nim game is a bit more complex; it allows stones to be moved between adjacent piles.

???+ abstract "Staircase Nim game"
    There are $n$ piles of stones in total, with the $i$-th pile having $a_i$ stones. Two players alternately operate; each operation is either taking away any number of stones from the $1$st pile, or moving any number of stones from the $i>1$-th pile to the $i-1$-th pile, but one cannot do nothing. The player who takes away the last stone wins.

For this, we have the following conclusion:

???+ note "Theorem"
    The first player loses if and only if the Nim sum of the numbers of stones in the odd piles $a_1\oplus a_3\oplus\cdots\oplus a_{n-1+(n\bmod 2)}=0$.

??? note "Proof"
    When any player moves stones from an even pile to an odd pile, the opponent can continue to move these stones to the next even pile (or remove them), so such a move does not affect the position of the odd piles. In this case, each odd pile moving down to the adjacent even pile (or removing) can be regarded as an independent single-pile Nim game. By the conclusion of the Sprague–Grundy theorem on the sum of games, the SG function value of the staircase Nim game is the Nim sum of the SG function values of these subgames. This gives the above conclusion.

### Fibonacci Nim game

The Fibonacci Nim game is similar to Bachet's game, with only one pile of stones and a limit on the number taken each time. Unlike Bachet's game, in the Fibonacci Nim game the limit on the number taken each time is dynamic.

???+ abstract "Fibonacci Nim game"
    There is a pile of stones, $n$ in total. Two players alternately take stones. The first player to act is not limited in the number of stones taken, but cannot take all the stones; subsequently, the number of stones taken each time may not exceed twice the number of stones taken last time (referring to the opponent's turn). The number of stones taken each time may not be $0$. The player who takes away the last stone wins.

For this, we have the following conclusion:

???+ note "Theorem"
    At the start of the game, the first player loses if and only if the number of stones $n$ is a [Fibonacci number](../combinatorics/fibonacci.md).

??? note "Proof"
    Let $q$ be the quota of the number of stones that can be removed in the current position. Then, in the first round, $q=n-1$; and in the subsequent rounds, $q$ is twice the number of stones removed last time (by the opponent). Consider the [Fibonacci coding](../combinatorics/fibonacci.md#fibonacci-coding) of the remaining number of stones $n$, i.e. uniquely decomposing $n$ into a sum of a series of non-adjacent positive Fibonacci numbers. What needs to be proved is that the current state is a winning state if and only if $q$ is greater than or equal to the smallest Fibonacci number in the decomposition of $n$.
    
    The winning strategy is: if possible, remove all remaining stones; otherwise, remove the smallest Fibonacci number in the decomposition. Since in the decomposition, the second-smallest Fibonacci number is necessarily strictly greater than twice the smallest Fibonacci number, as long as the current round in a winning state cannot take all the stones, the opponent in the next round also cannot take the second-smallest Fibonacci number (i.e. the smallest Fibonacci number in the next round), and the opponent is sure to be in a losing state.
    
    Conversely, if one is currently in a losing state, then let the number taken this time be $k$; it is necessarily strictly less than the smallest Fibonacci number $F$ in the current decomposition. Suppose the smallest Fibonacci number in the next round is $F'$; it is necessarily also the smallest Fibonacci number in the decomposition corresponding to $F - k$. Let $F'=F''+F'''$ with $F''>F'''$, that is, $F''',F'',F'$ are three consecutive terms in the Fibonacci sequence. If $k<F''$, then when using Fibonacci coding to compute $k + (F-k)$, no carry is needed, and one naturally cannot obtain $F$. So, we must have $k\ge F''$. This shows that the quota of the next round $2k>F''+F'''=F'$, a winning state.

### Wythoff's game

Wythoff's game allows removing from multiple piles of stones simultaneously, but requires removing the same number of stones from each pile.

???+ abstract "Wythoff's game"
    There are two piles of stones, with $a_1$ and $a_2$ stones respectively. Two players alternately take stones from one pile or both piles, cannot take none, but require that when taking stones from both piles, the number of stones taken must be the same. The player who takes away the last stone wins.

For this, we have the following conclusion:

???+ note "Theorem"
    Without loss of generality, suppose $a_1\le a_2$; then the first player loses if and only if $a_1 = \lfloor(a_2-a_1)\phi\rfloor$, where $\phi=(\sqrt{5}+1)/2$ is the golden ratio.

To prove this conclusion, we need the following lemma:

???+ abstract "Beatty sequence"
    Let $r > 1$ be an irrational number. The Beatty sequence it generates is $\mathcal B_r = \{\lfloor kr\rfloor : k \in\mathbf N_+\}$.

???+ note "Rayleigh's theorem"
    Let $r,s > 1$ be two irrational numbers with $\dfrac{1}{r}+\dfrac{1}{s}=1$. Then the sequences $\mathcal B_r$ and $\mathcal B_s$ form a partition of the set of positive integers $\mathbf N_+$. In this case, they are also called complementary Beatty sequences.

??? note "Proof"
    Let $\mathcal A_r=\{kr:k\in\mathbf N_+\}$. Consider sorting the elements in the set $\mathcal A=\mathcal A_r\cup\mathcal A_\ell$ to obtain the sequence $\{a_i\}_{i\in\mathbf N_+}$. What needs to be proved is that $i=\lfloor a_i\rfloor$ holds for all $i\in\mathbf N_+$, which gives that $\mathcal B_r\cup\mathcal B_s$ is a partition of the set of positive integers $\mathbf N_+$.
    
    First, prove that there are no repeated elements in the sequence. Suppose not; there exist $k,\ell\in\mathbf N_+$ such that $kr=\ell s$ holds. Then, we have
    
    $$
    \dfrac{\ell}{k} = \dfrac{r}{s} = r - 1.
    $$
    
    But the left side of the equation is rational and the right side is irrational, a contradiction. Therefore, the numbers in the sequence are all distinct.
    
    Then, prove that there are exactly $\lfloor a_i\rfloor$ numbers in the set $\mathcal A$ less than or equal to $a_i$. Without loss of generality, suppose $a_i\in\mathcal A_r$, i.e. $a_i=kr$; then counting the elements in the sets $\mathcal A_r$ and $\mathcal A_\ell$ respectively, there are exactly
    
    $$
    k + \left\lfloor\dfrac{kr}{s}\right\rfloor = k + \lfloor k(r-1)\rfloor = \lfloor kr\rfloor = \lfloor a_i\rfloor
    $$
    
    positive integers less than or equal to $a_i$. Furthermore, since the sequence $\{a_i\}$ is strictly increasing, there are exactly $i$ numbers less than or equal to $a_i$. This gives $i=\lfloor a_i\rfloor$.

From this, one can obtain the proof of the aforementioned conclusion.

??? note "Proof of the conclusion of Wythoff's game"
    For all first-player-losing states $(a_1,a_2)$ with $a_1 < a_2$, letting $k = a_2 - a_1 \in\mathbf N_+$, we have $a_1=\lfloor k\phi\rfloor$ and $a_2=\lfloor k(\phi+1)\rfloor$. Since $\phi$ is the golden ratio, $\dfrac{1}{\phi}+\dfrac{1}{\phi+1}=1$. By Rayleigh's theorem, the sequences $\{\lfloor k\phi\rfloor\}$ and $\lfloor k(\phi+1)\rfloor$ form a partition of the set of positive integers $\mathbf N_+$. This in fact shows that among all first-player-losing states $(a_1,a_2)$ with $a_1 < a_2$, the components $a_1$ and $a_2$ range over all positive integers exactly once, and their difference $a_2-a_1$ also ranges over all positive integers exactly once.
    
    Since in Wythoff's game a legal operation either keeps one of the components unchanged or keeps the difference of the components unchanged, starting from a first-player-losing state, one indeed cannot reach another first-player-losing state via a legal operation. Conversely, for any first-player-winning state $(a_1,a_2)$, without loss of generality suppose $a_1\le a_2$, and let $k=a_2-a_1$. If $a_1>\lfloor k\phi\rfloor$, then the first player can take $(a_1 - \lfloor k\phi\rfloor)$ from both piles, changing the position to a losing state. Conversely, by the conclusion of the previous paragraph, for this $a_1$ there must exist a unique losing state $(a_1,a_2')$. Furthermore, if $a_1 > a_2'$, obviously $a_2' < a_2$; otherwise, if $a_1 < a_2'$, then one can take $k'=a_2'-a_1$ such that $a_1=\lfloor k'\phi\rfloor$, and also $a_1 < \lfloor k\phi\rfloor$, so $k' < k$, hence $a_2'=a_1 + k' < a_1+k = a_2$. So, as long as $a_1 < \lfloor k\phi\rfloor$, we must have $a_2' < a_2$, and the first player only needs to take $(a_2-a'_2)$ stones from the second pile to change the position to a losing state.

### Coin-turning games

Coin-turning games are also a class of common impartial combinatorial games.

???+ abstract "Coin-turning game"
    Let $(S,\preceq)$ be a [well-founded poset](../order-theory.md), and let the map $f:S\rightarrow\mathcal P\mathcal PS$ satisfy that for all $s\in S$ the set $f(s)$ is non-empty, that for $T\in f(s)$ we have $s\in T$, and that for all $t\in T$ we have $t\preceq s$. Each element of the set $S$ has a coin, which may be heads up or tails up. Players act in turn, choosing a heads-up coin $s$ and a set $T\in f(s)$, and turning over all coins in the set $T$. The player who turns all coins to tails up wins.

The coin-turning game is in fact a large class of games. Depending on the choice of the specific poset $S$ and the map $f$, the specific form of the coin-turning game also varies. In the game description, the condition that the map $f$ needs to satisfy is saying that in the set $T$ of coins the player chooses to turn over each time, there must exist a heads-up coin $s$ such that all elements in the set $T$ are ordered before $s$. This guarantees that the game can terminate after finitely many steps.

???+ example "Examples"
    1.  Let $S=\{1,2,\cdots,n\}$ and $f(s)=\{\{t,s\}:t \le s\}$. This is equivalent to saying that there is a row of $n$ coins, and each time one turns over a heads-up coin and can choose a coin to its left to turn over.
    2.  Let $S=\{1,2,\cdots,n\}$ and $f(s)=\{[t,s]:t \le s\}$. This is equivalent to saying that there is a row of $n$ coins, and each time one turns over a consecutive segment of coins, but must ensure that the rightmost of these coins is heads up before turning.
    3.  Let $S=\{1,2,\cdots,n\}^2$ and $f(s)=\{\{s\}\}$. This is equivalent to saying that there are $n$ rows and $n$ columns of coins, and each time one can only turn over one heads-up coin.
    4.  Let $S$ be the set of nodes of a rooted tree, and $f(s)$ be the set of all subsets, containing $s$ itself, of the set of nodes on the path from vertex $s$ to the tree root. This is equivalent to saying that there is a rooted tree, with a coin placed at each node, and each time one turns over a heads-up coin and can choose to turn over the coins at some of its ancestor nodes.

Although there are many kinds of coin-turning games, the ideas for solving them are consistent. For a coin-turning game $(S,f)$, let $G_s$ be the position in which only the coin at element $s$ is heads up. These positions are called basic positions. Then, any position $G$ can be regarded as the sum of the games corresponding to these basic positions. That is, the following conclusion holds:

???+ note "Theorem"
    For a coin-turning game $(S,f)$ and a position $G$, let the set of positions of the heads-up coins in it be $H(G)\subseteq S$. Then, the SG function value of the position $G$ is
    
    $$
    \operatorname{SG}(G) = \bigoplus_{s\in H(G)}\operatorname{SG}(G_s).
    $$

??? note "Proof"
    Consider a related game: in a position $G'$, each element of the set $S$ has some stones placed on it; when a player acts each time, they can take away one stone at $s$, choose a set $T\in f(s)$, and place one stone on each element in the set $T\setminus\{s\}$. For this kind of game, one can still define basic positions $G'_s$, i.e. the position with only one stone placed at position $s$. In this kind of game, each position is the sum of the basic positions corresponding to all its stones. This is because as long as one associates a newly placed stone with the stone that was taken away, one can associate each stone appearing during the game with the various stones in the initial position, and then the subgame processes corresponding to different stones of the initial position do not interfere with one another, so the whole game can be regarded as the sum of these subgames. Since the SG values of the basic positions corresponding to stones at the same position are the same, using the property of the XOR value, the SG value of the position $G'$ is determined only by the parity of the number of stones in each pile, and is independent of the specific number. Therefore, for a game position $G'$, if we denote the set of positions with an odd number of stones as $H(G')$, then the analysis of this paragraph can be summarized in the formula:
    
    $$
    \operatorname{SG}(G') = \bigoplus_{s\in H(G')} \operatorname{SG}(G'_s).
    $$
    
    From this, below we only need to establish the equivalence of the game $G'$ and the game $G$ to prove the formula in the theorem.
    
    What needs to be explained is that for the position $G'$ of the new game and the position $G$ of the coin-turning game, as long as the positions with an odd number of stones in $G'$ are the same as the positions where coins are heads up in $G$, then $G'$ and $G$ are equivalent. By [Lemma 2 of the Sprague–Grundy theorem](#sg-lem-2), this is equivalent to proving that the position $G+G'$ is a losing state. The second player's winning strategy is simple: if the first player chooses to take away a stone at $s$ and there is more than one stone there, then the second player directly imitates the first player's behavior; otherwise, the second player chooses the same $s$ and $T\in f(s)$ as the first player, but chooses a different subgame from the first player, i.e. if the first player takes a stone the second player takes a coin, and if the first player takes a coin the second player turns a stone. Since no matter what operation the first player makes, the second player can continue to operate and ensure that the positions with an odd number of stones in the residual position are the same as the positions where coins are heads up. In this way, the game must end when the first player has no legal operation, so the first player loses. The theorem is thereby proved.

Using this conclusion, to determine whether a certain position is a win, one only needs to compute the SG function values of the basic positions corresponding to all heads-up coins in it, then take the Nim sum. The SG function values of these basic positions are also not hard to compute, because their successor positions are already given by the map $f$, and the SG values of the successor positions can be computed inductively:

$$
\operatorname{SG}(G_s) = \operatorname{mex}\limits_{T\in f(s)}\bigoplus_{t\in T\setminus\{s\}}\operatorname{SG}(G_t).
$$

This amounts to providing a recurrence formula for the SG function values of the basic positions.

### Bipartite graph game

Prerequisite: [maximum matching of a bipartite graph](../../graph/graph-matching/bigraph-match.md)

At the end of this section, we discuss the bipartite graph game. Although this game is often called the bipartite graph game, its description and the proof of its conclusion are independent of the structure of the bipartite graph, so its conclusion in fact holds for general undirected graphs. But the maximum matching of a general graph is relatively complex, so this conclusion often appears in problems about bipartite graphs.

???+ abstract "Bipartite graph game"
    Two players act in turn. The position faced by each player is composed of an undirected graph $G=(V,E)$ and one of its vertices $v\in V$. In a player's turn, if the current position is $(G,v)$, then the player must choose a vertex $u$ adjacent to $v$. Then, vertex $v$ and all its incident edges are deleted from the graph $G$, giving the residual graph $G'$. The new position is $(G',u)$, handed to the next player. If at the start of some player's turn, the current vertex $v$ has no adjacent vertex in the graph (i.e. no legal choice exists), then this player cannot act and thereby loses the game.

For this, we have the following conclusion:

???+ note "Theorem"
    The first player wins if and only if vertex $v$ is a maximum-matching key point of the graph $G$, that is, in all maximum matchings of the graph $G$, vertex $v$ is a matched point.

??? note "Proof"
    First, suppose vertex $v$ is a maximum-matching key point of the graph $G$. Let a maximum matching of $G$ be $M$. In this case, the first player can move the position to the vertex $u$ matched with vertex $v$ in $M$. Since vertex $v$ appears in all maximum matchings of the graph $G$, the size of the maximum matching of the residual graph $G'$ is at most $|M|-1$; and removing the edge $(v,v)$ from $M$ gives a matching $M'$ of size $|M|-1$ of the graph $G'$: combining these two points, we know that $M'$ is a maximum matching of the graph $G'$. But in the position the second player faces, vertex $u$ is not a matched point of the matching $M'$. Therefore, the second player must be in a losing state.
    
    Conversely, suppose there exists a maximum matching $M$ such that $v$ is an unmatched point. Since $M$ is a maximum matching, the vertices adjacent to vertex $v$ must be matched points; otherwise, one could add the edge between them to $M$, obtaining a larger matching. Therefore, no matter what the first player chooses, the second player is in a winning state.

For the algorithm to find the maximum-matching key points of a bipartite graph, see the [maximum matching of a bipartite graph page](../../graph/graph-matching/bigraph-match.md#最大匹配关键点).

In addition, the bipartite graph game also has a variant:

???+ abstract "Variant of the bipartite graph game"
    Let $G=(V,E)$ be an undirected graph, with a stone placed on each vertex of the graph. Two players alternately act, taking away stones. At the start of the game, the first player can take away any stone; in subsequent rounds, the vertex from which each player takes a stone must be adjacent to the vertex from which the opponent took a stone in the previous round. The first player unable to take a stone loses the game.

Obviously, this variant amounts to letting the first player choose the initial position in the aforementioned bipartite graph game, and then starting the bipartite graph game from the second player. Therefore, in this variant, the first player loses if and only if every vertex is a maximum-matching key point, i.e. the graph $G$ has a [perfect matching](../../graph/graph-matching/graph-match.md#定义).

## Misère Nim game

This section discusses the solution of the misère Nim game.

???+ abstract "Nim game"
    There are $n$ piles of stones in total, with the $i$-th pile having $a_i$ stones. Two players alternately take away any number of stones from any one pile, but cannot take none. The player who takes away the last stone loses.

For this, we have the following conclusion:

???+ note "Theorem"
    In the misère Nim game, the state $(a_1,a_2,\cdots,a_n)$ is a losing state $\mathcal P$ if and only if
    
    1.  there exists $i$ such that $a_i>1$, and the Nim sum $a_1\oplus a_2\oplus\cdots\oplus a_n=0$, or
    2.  for all $i$ we have $a_i\le 1$, and the number of remaining non-empty piles is odd.

??? note "Proof"
    Since being unable to operate is a first-player-winning state $\mathcal N$, one can inductively prove that if every pile has only one stone, then an odd number of piles corresponds to a first-player-losing state $\mathcal N$, and an even number of piles corresponds to a first-player-winning state $\mathcal N$.
    
    Next, consider the case where some piles of stones have a number strictly greater than $1$.
    
    Case A: If only one pile of stones has a number strictly greater than $1$, then in this case the Nim sum is definitely not $0$. Moreover, since the first player can choose to transfer to a position where the number of stones in all piles is no more than $1$, and can control the parity of the number of remaining non-empty piles. Therefore, this is a first-player-winning state $\mathcal N$.
    
    Case B: Now, more than one pile of stones has a number strictly greater than $1$; then, no matter what operation, in the next position there is at least one pile of stones with a number strictly greater than $1$. By the induction hypothesis, in the next position, a first-player loss corresponds to a Nim sum of zero, and a first-player win corresponds to a Nim sum not zero. This is exactly the same as the induction hypothesis of the normal Nim game. Therefore, repeating the argument of the Nim game, one can know that the current position likewise conforms to the conclusion that a Nim sum of zero corresponds to a first-player-losing state.

## Games on directed graphs

The impartial combinatorial games discussed in this article require that the same position cannot appear twice, and there is no possibility of a tie. Therefore, the corresponding game graph is always a directed acyclic graph. This section relaxes this restriction and discusses how to determine, on a general directed graph, whether each state is a first-player win, a first-player loss, or a tie.

The rules of games on directed graphs are broadly the same as those of other impartial combinatorial games: starting from the initial state, alternately move one step along an edge of the directed graph until there is nowhere to go. Depending on whether the game is under normal rules or misère rules, the last player unable to move is respectively the loser and the winner. In such a game, the win/loss situation of each state has three possibilities in total: first-player win, first-player loss, tie. In a tie, the game never terminates. Although a bit more complex, the [lemma](#np-lem) about losing states and winning states still holds, and the remaining states are tie states:

-   A state is a first-player win if and only if one of its successor states is a losing state;
-   If a state has successor states, then it is a first-player loss if and only if all its successor states are winning states;
-   If a state cannot be classified as a winning state or a losing state, then it is a tie state.

To classify all states into these three states, one only needs to use an idea similar to [topological sorting](../../graph/topo.md):

1.  During initialization, record the out-degree of all states, push all states with out-degree zero into a queue, and set them as losing states or winning states depending on whether the game is under normal rules or misère rules.
2.  Pop the state at the front of the queue. If it is a losing state, set the predecessor states as winning states; otherwise, the current state is a winning state, decrement the out-degree of all its predecessor states by one, and set the predecessor states with out-degree zero as losing states. Push the predecessor states that can be determined as winning or losing states into the queue.
3.  The algorithm terminates when the queue is empty. States not yet determined as winning or losing states are all tie states.

This algorithm can classify all states in $O(|V|+|E|)$ time.

## Example problems

This section discusses some typical example problems.

???+ example "[Luogu P2148 \[SDOI2009\] E&D](https://www.luogu.com.cn/problem/P2148)"
    There are $2n$ piles of stones. For $k=1,2,\cdots,n$, piles $2k-1$ and $2k$ are divided into a group. Two players alternately operate; each time one chooses a group of piles, removes one of the piles, and divides the other pile into two non-empty piles, placing them at the two positions where this group of piles is. If all piles have only one stone, the current player has no legal operation and loses the game. Given the number of stones in each pile $\{a_i\}_{i=1}^{2n}$, determine whether it is a first-player-winning state.

??? note "Solution"
    Obviously, the games of different groups of piles are mutually independent, so as long as one computes the SG function value of each group's game, one can compute the SG value of the whole game and then determine whether it is a winning state. The key is how to compute the SG function value of each group of piles. This is not easy. A common idea for solving this kind of game-theory problem is tabulating. Let the SG value when the numbers of stones in a group of piles are $(i,j)$ respectively be $f(i,j)$. Then, writing a brute-force tabulating program gives the following result:
    
    ```text
    0 1 0 2 0 1 0 3 0 1 0 2 0 1 0 4 
    1 1 2 2 1 1 3 3 1 1 2 2 1 1 4 4
    0 2 0 2 0 3 0 3 0 2 0 2 0 4 0 4
    2 2 2 2 3 3 3 3 2 2 2 2 4 4 4 4
    0 1 0 3 0 1 0 3 0 1 0 4 0 1 0 4
    1 1 3 3 1 1 3 3 1 1 4 4 1 1 4 4
    0 3 0 3 0 3 0 3 0 4 0 4 0 4 0 4
    3 3 3 3 3 3 3 3 4 4 4 4 4 4 4 4
    0 1 0 2 0 1 0 4 0 1 0 2 0 1 0 4
    1 1 2 2 1 1 4 4 1 1 2 2 1 1 4 4
    0 2 0 2 0 4 0 4 0 2 0 2 0 4 0 4
    2 2 2 2 4 4 4 4 2 2 2 2 4 4 4 4
    0 1 0 4 0 1 0 4 0 1 0 4 0 1 0 4
    1 1 4 4 1 1 4 4 1 1 4 4 1 1 4 4
    0 4 0 4 0 4 0 4 0 4 0 4 0 4 0 4
    4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
    ```
    
    This table is very regular. There is a simple observation: the table is divided into several $2\times 2$ matrices, and the upper-left corner is always $0$, while the other three values are always the same. So, one may compress this table, compressing each $2\times 2$ matrix into that common value other than the upper-left corner:
    
    ```text
    1 2 1 3 1 2 1 4 
    2 2 3 3 2 2 4 4 
    1 3 1 3 1 4 1 4 
    3 3 3 3 4 4 4 4 
    1 2 1 4 1 2 1 4 
    2 2 4 4 2 2 4 4 
    1 4 1 4 1 4 1 4 
    4 4 4 4 4 4 4 4 
    ```
    
    One can find that this compressed table is the value at the corresponding position of the previous complete table plus one. The problem is in fact solved. With indices starting from $0$, the value $g(i,j)$ at position $(i,j)$ in the table can be given by the following recurrence formula:
    
    $$
    g(i,j) =
    \begin{cases}
    0, & \text{if }2\mid i\text{ and }2\mid j,\\
    g(\lfloor i/2\rfloor,\lfloor j/2\rfloor)+1,& \text{otherwise}.
    \end{cases}
    $$
    
    The required SG function $f(i,j)=g(i-1,j-1)$. Using this recurrence formula, the algorithm can find the value of $f(i,j)$ in $O(\log\min\{i,j\})$ time.
    
    Of course, by simple induction one can obtain that $g(i,j)$ is in fact the minimum number of times one repeatedly divides both $i$ and $j$ by $2$ to obtain two even numbers. In other words, it is the number of trailing $1$s in the bitwise OR of $i$ and $j$. From this, one can also directly use `__builtin_ctz(~(i | j))` to compute this value.
    
    In this kind of problem, as long as one obtains the SG function expression by tabulating and observing, it is easily proved by induction, so the key to solving the problem is obtaining these conclusions in some form rather than deriving them. For example, once the conclusion is known, the recurrence relation in this problem can be proved by induction as follows. Let $S_k$ be the set of SG values of the positions obtainable by dividing $k$ stones into two non-empty piles; then $f(i,j) = \operatorname{mex}(S_i \cup S_j)$. Therefore, $S_k$ has the recurrence relation:
    
    $$
    S_k = \{\operatorname{mex}(S_i \cup S_j) : i + j = k,~i,j\in\mathbf N_+\}.
    $$
    
    What needs to be proved is that $d\in S_k$ if and only if bit $d$ (the lowest bit being bit $0$) in the binary representation of $(k-1)$ is $1$.
    
    Use mathematical induction. The induction base $S_1=\varnothing$ obviously holds. Suppose the proposition holds for all positive integers less than $k$. Then, $d\in S_k$ if and only if there exist $i,j\in\mathbf N_+$ such that $i+j=k$ and at least one of the two numbers $(i-1)$ and $(j-1)$ has a $1$ in some bit $d' < d$, and both have $0$ in bit $d$. Obviously, such a split exists if and only if, considering only bits $0\sim d$, i.e. modulo $2^{d+1}$, the value of $(k-1)=(i-1)+(j-1)+1$ falls in the range $[2^d,2^{d+1}-1)$. This condition is equivalent to bit $d$ of $(k-1)$ being $1$. From this, the induction step holds. The original proposition is proved.

??? note "Reference code"
    ```cpp
    --8<-- "docs/math/code/impartial-game/impartial-game-1.cpp"
    ```

???+ example "[Luogu P5675 \[GZOI2017\] 取石子游戏](https://www.luogu.com.cn/problem/P5675)"
    There are $n$ piles of stones, with the $i$-th pile having $a_i$. Two people play the Nim game. Now, one can arbitrarily designate some piles of stones as the initial position, and designate one of the piles such that the first player must take stones from it in the first round, but cannot designate the number of stones taken. Ask how many designation ways make the first player unable to win. The data satisfy $n,a_i\le 200$.

??? note "Solution"
    For this kind of problem, one needs to use the conclusions of common games, combined with knowledge of other parts, to solve it. Suppose the first player is designated to take from the $i$-th pile, and the Nim sum of the numbers of all designated piles is $v$; then the first player cannot win if and only if $a_i \le a_i\oplus v$, that is, the number of stones $a_i$ in the $i$-th pile does not exceed the Nim sum $a_i\oplus v$ of the numbers of the remaining piles other than the $i$-th. Since the data range is very small, directly enumerate the pile designated for the first round; when enumerating up to the $i$-th pile, for each of the remaining piles chosen or not, the number of ways to obtain different Nim sums can be computed via DP, and one sums up the part of the finally obtained number of ways that is greater than or equal to $a_i$.

??? note "Reference code"
    ```cpp
    --8<-- "docs/math/code/impartial-game/impartial-game-2.cpp"
    ```

???+ example "[Luogu P2599 \[ZJOI2009\] 取石子游戏](https://www.luogu.com.cn/problem/P2599)"
    There are $n$ piles of stones, with the $i$-th pile having $a_i$. Two people alternately take stones; each time one can only choose one of the leftmost or rightmost two piles and take away any number of stones, but cannot take none. The player who takes away the last stone wins. Ask whether the first player wins.

??? note "Solution"
    Since in this problem there are no mutually independent subgames, this problem in principle only uses the [lemma for determining losing and winning states](#the-game-graph-and-states). Let us start analyzing from the simplest case. When $n\le 2$, it is the Nim game. When $n \ge 3$, the problem becomes complex. But since the operable piles can only be the piles at the two ends, let their numbers of stones be $x$ and $y$ respectively. Furthermore, let $f(x,y)$ be the indicator function of a first-player-winning state, i.e. $f(x,y)=1$ when the first player wins, and $f(x,y)=0$ otherwise. It is easy to find that the value of $f(x,y)$ satisfies the recurrence relation: $f(x,y)=0$ if and only if for all $s < x$ and $t < y$ we have $f(x,t)=f(s,y)=1$. The recurrence base is at $x=0$ or $y=0$; in this case, the game already has fewer than $n$ piles of stones, and one needs to further consider the number of the middle piles. Therefore, one may temporarily assume that $f(x,0)$ and $f(0,y)$ are known, and consider how to deduce all values of $f(x,y)$ from their values. This is not difficult. Consider an infinitely large matrix with index set $\mathbf N\times\mathbf N$; finding $f(x,y)$ amounts to filling in $0$s and $1$s in it, and the condition to satisfy is that each row and each column has at most one $0$, and if no $0$ has appeared in the previous positions of the same row or column, this position must be $0$. The position of the $0$ in each row in fact defines a function from the row number $x$ to the column number $y$. After trying a few examples (i.e. tabulating), one can find that if the unique $x$ making $f(x,0)=0$ is $x_0$, and the unique $y$ making $f(0,y)=0$ is $y_0$, then, for any $x$, the $y$ making $f(x,y)=0$ hold is
    
    $$
    y = \begin{cases}
    0, & x = x_0,\\
    x - 1, & x_0 < x < y_0,\\
    x + 1, & y_0 < x < x_0,\\
    x, & \text{otherwise}.
    \end{cases}
    $$
    
    That is, as long as one knows $x_0$ and $y_0$, one can compute the value of any $f(x,y)$ in $O(1)$ time and determine whether the current state is a first-player-winning state. And $x_0$ and $y_0$ can be computed recursively. For example, $x_0$ is the unique solution making $f(x,0)=0$, but at the same time, the value of $f(x,0)$ can be computed by removing the rightmost pile and considering only the remaining $n-1$ piles; that is, considering only the first $n-1$ piles, one can likewise compute an $f_{1,n-1}(x,y)$, and then obviously $f(x,0)=f_{1,n-1}(x,a_{n-1})$; similarly, after removing the leftmost pile and computing $f_{2,n}(x,y)$, one obtains $f(0,y)=f_{2,n}(a_1,y)$. Of course, the computation of the inner functions $f_{1,n-1}(x,y)$ and $f_{2,n}(x,y)$ depends on even more inner functions. This is typical [interval DP](../../dp/interval.md). Each layer only needs to maintain the $x_0$ and $y_0$ of the corresponding function.

??? note "Reference code"
    ```cpp
    --8<-- "docs/math/code/impartial-game/impartial-game-3.cpp"
    ```

## Exercises

First are some template problems. They are simple applications of the conclusions of this page:

-   [Luogu P2197 【模板】Nim 游戏](https://www.luogu.com.cn/problem/P2197)
-   [Luogu P2252 \[SHOI2002\] 取石子游戏](https://www.luogu.com.cn/problem/P2252)
-   [Luogu P2594 \[ZJOI2009\] 染色游戏](https://www.luogu.com.cn/problem/P2594)
-   [Luogu P3185 \[HNOI2007\] 分裂游戏](https://www.luogu.com.cn/problem/P3185)
-   [Luogu P3480 \[POI 2009\] KAM-Pebbles](https://www.luogu.com.cn/problem/P3480)
-   [Luogu P4101 \[HEOI2014\] 人人尽说江南好](https://www.luogu.com.cn/problem/P4101)
-   [Luogu P4279 \[SHOI2008\] 小约翰的游戏](https://www.luogu.com.cn/problem/P4279)
-   [Luogu P6487 \[COCI 2010/2011 #4\] HRPA](https://www.luogu.com.cn/problem/P6487)
-   [Luogu P6560 \[SBCOI2020\] 时光的流逝](https://www.luogu.com.cn/problem/P6560)
-   [Luogu P7589 黑白棋（2021 CoE-II B）](https://www.luogu.com.cn/problem/P7589)
-   [AtCoder Regular Contest 168 B - Arbitrary Nim](https://atcoder.jp/contests/arc168/tasks/arc168_b)

Then are some problems that are more thought-provoking or more comprehensive:

-   [Luogu P2490 \[SDOI2011\] 黑白棋](https://www.luogu.com.cn/problem/P2490)
-   [Luogu P3179 \[HAOI2015\] 数组游戏](https://www.luogu.com.cn/problem/P3179)
-   [Luogu P5363 \[SDOI2019\] 移动金币](https://www.luogu.com.cn/problem/P5363)
-   [Luogu P5970 \[POI 2016\] Nim z utrudnieniem](https://www.luogu.com.cn/problem/P5970)
-   [Luogu P6791 \[SNOI2020\] 取石子](https://www.luogu.com.cn/problem/P6791)
-   [Luogu P7864「EVOI-RD1」摘叶子](https://www.luogu.com.cn/problem/P7864)
-   [Luogu P8347「Wdoi-6」另一侧的月](https://www.luogu.com.cn/problem/P8347)
-   [AtCoder Grand Contest 002 E - Candy Piles](https://atcoder.jp/contests/agc002/tasks/agc002_e)
-   [AtCoder Grand Contest 010 F - Tree Game](https://atcoder.jp/contests/agc010/tasks/agc010_f)
-   [AtCoder Grand Contest 017 D - Game on Tree](https://atcoder.jp/contests/agc017/tasks/agc017_d)
-   [AtCoder Beginner Contest 278 G - Generalized Subtraction Game](https://atcoder.jp/contests/abc278/tasks/abc278_g)
-   [SPOJ COT3 - Combat on a tree](https://www.spoj.com/problems/COT3/)
-   [Codeforces 494 E. Sharti](https://codeforces.com/problemset/problem/494/E)
-   [Codeforces 1149 E. Election Promises](https://www.luogu.com.cn/problem/CF1149E)
-   [Codeforces 1451 F. Nullify The Matrix](https://codeforces.com/problemset/problem/1451/F)
-   [Codeforces 1704 F. Colouring Game](https://codeforces.com/problemset/problem/1704/F)

Finally are some bipartite graph game problems. Since they require some bipartite matching algorithms, they are listed separately:

-   [Luogu P4136 谁能赢呢？](https://www.luogu.com.cn/problem/P4136)
-   [Luogu P4617 \[COCI 2017/2018 #5\] Planinarenje](https://www.luogu.com.cn/problem/P4617)
-   [Luogu P4055 \[JSOI2009\] 游戏](https://www.luogu.com.cn/problem/P4055)
-   [Luogu P1971 \[NOI2011\] 兔兔与蛋蛋游戏](https://www.luogu.com.cn/problem/P1971)
-   [Codeforces 1147 F. Zigzag Game](https://codeforces.com/problemset/problem/1147/F)

## References and notes

-   [(Reprint) Nim Game Theory (Complete Collection) by exponent - cnblogs](http://www.cnblogs.com/exponent/articles/2141477.html)
-   [\[Combinatorial Games and Game Theory\]【Study Notes】by Candy? - cnblogs](https://www.cnblogs.com/candy99/p/6548836.html)
-   [Nim - Wikipedia](https://en.wikipedia.org/wiki/Nim)
-   [Sprague–Grundy theorem - Wikipedia](https://en.wikipedia.org/wiki/Sprague%E2%80%93Grundy_theorem)
-   [Nimber - Wikipedia](https://en.wikipedia.org/wiki/Nimber)
-   [Beatty Sequence - Wikipedia](https://en.wikipedia.org/wiki/Beatty_sequence)
-   [Games on arbitrary graphs - CP Algorithms](https://cp-algorithms.com/game_theory/games_on_graphs.html)
-   [Algorithm Study Notes (74): Bipartite Graph Game by Pecco - Zhihu](https://zhuanlan.zhihu.com/p/359334008)
-   Conway, John H. On numbers and games. AK Peters/CRC Press, 2000.
-   Berlekamp, Elwyn R., John H. Conway, and Richard K. Guy. Winning ways for your mathematical plays, volume 1-4. AK Peters/CRC Press, 2001-2004.

[^n-vs-p]: The two names "$\mathcal N$ state" and "$\mathcal P$ state" respectively stand for "Next player wins" and "Previous player wins".
