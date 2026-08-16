In mathematical logic, boolean algebra is a branch of algebra. In elementary algebra the values of variables are numbers, and the main operators it studies are addition, multiplication, exponentiation, and the inverse operations of these three. In boolean algebra, the values of variables are only **true** and **false** (usually denoted $1$ and $0$), and the main operators it studies are conjunction (AND, $\land$), disjunction (OR, $\lor$), and negation (NOT, $\lnot$). Just as elementary algebra is a form for describing numerical operations, boolean algebra is a form for describing logical operations.

## Boolean function

???+ abstract "Definition"
    A **boolean function** is a function of the form $f:\mathbf{B}^k\to \mathbf{B}$, where $\mathbf{B}=\{0,1\}$ is the **boolean domain** and the non-negative integer $k$ is the **arity** of this boolean function. A boolean function with $k=1$ is a unary function, and so on. When $k=0$, we consider the function to degenerate into a constant in $\mathbf{B}$.

We generally study only unary and binary boolean functions. Unless otherwise stated, the boolean functions below are limited to the unary and binary cases.

Besides the general way of expressing a function, we can also represent a boolean function with a **truth table**, a **logic gate**, or a [Venn diagram](https://en.wikipedia.org/wiki/Venn_diagram).

???+ abstract "Truth table"
    For a boolean function, we enumerate all cases of its input, and list the inputs and the corresponding outputs into a table; this table is called a truth table.

An $n$-ary boolean function can also be represented by a **propositional formula** containing $n$ variables; propositional formulas $p$ and $q$ are **logically equivalent** if and only if they describe the same boolean function, denoted $p\iff q$.

The following are some common boolean functions, which we will also collectively call **logical connectives** or **logical operators**:

| Name (mathematical logic) | Other names | Notation |
| -------------------------------------------------- | -------------------- | -------------------------------- |
| Truth (tautology) | | $\top$ |
| Falsity (contradiction) | | $\bot$ |
| Proposition | Itself | $A$ |
| Negation | NOT | $\lnot A$ |
| Conjunction | AND | $A \land B$ |
| Disjunction | OR | $A \lor B$ |
| Non-conjunction | NAND, Sheffer stroke | $A \bar{\land} B$, $A\uparrow B$ |
| Non-disjunction | NOR | $A \bar{\lor} B$, $A\downarrow B$ |
| | Exclusive-OR (XOR) | $A \oplus B$ |
| | Exclusive-NOR | $A \odot B$ |
| Material implication[^note1] | | $A \to B$ |
| Material nonimplication[^note1] | | $A \nrightarrow B$ |
| Converse implication[^note1] | | $A \gets B$ |
| Converse nonimplication[^note1] | | $A \nleftarrow B$ |
| Biconditional, equivalence[^note1][^note2] | | $A \leftrightarrow B$ |
| Non-equivalence[^note1][^note3] | | $A \nleftrightarrow B$ |

The corresponding truth table (From [Wikipedia](https://commons.wikimedia.org/wiki/File:Logical_connectives_table.svg)):

![](./images/logical-connectives-table.svg)

The corresponding Venn diagram and [Hasse diagram](./order-theory.md#偏序集的可视化表示hasse-图) (with the set containment relation $\subseteq$ as the partial order, From [Wikipedia](https://en.wikipedia.org/wiki/File:Logical_connectives_Hasse_diagram.svg)):

![](./images/logical-connectives-hasse-diagram.svg)

Since an $n$-ary boolean function has $2^n$ possible inputs, there are $2\uparrow (2\uparrow n)$ $n$-ary boolean functions, where $\uparrow$ is the Knuth up-arrow.

We call a combination of logical operators a **logical expression**.

If we regard $\mathbf{B}$ as a [residue class](./number-theory/basic.md#congruence-classes-and-residue-systems) modulo $2$, then XOR is equivalent to addition modulo $2$, and AND is equivalent to multiplication modulo $2$, so we sometimes also use $\mathbf{Z}_2$ to denote the boolean domain.

### Precedence

Unary logical operators have higher precedence than binary logical operators, i.e. $\lnot$ has higher precedence than $\land$, $\lor$, $\oplus$, etc.

The precedence among binary logical operators has various conventions; some references consider $\land$, $\lor$, $\oplus$ to have higher precedence than $\to$, $\gets$, $\leftrightarrow$, while others hold the opposite view. So when using them it is recommended to add more parentheses to make the order clear.

For the convention in C++, see the [C++ operator precedence table](../lang/op.md#c-operator-precedence-table).

### Sole sufficient operators and functionally complete operator sets

In fact, we can express all the other logical operators using just NAND or NOR, and CPUs are built based on this. However, since the four logical operators **AND, OR, NOT, XOR** have nicer properties, we generally use only these four functions when studying boolean algebra.

??? example "How to express the other logical operators using NAND and NOR respectively"
    We have
    
    -   $\lnot p=p\bar{\land} p=p\bar{\lor} p$,
    -   $p\land q=(p\bar{\land}q)\bar{\land}(p\bar{\land}q)=(p\bar{\lor}p)\bar{\lor}(q\bar{\lor}q)$,
    -   $p\lor q=(p\bar{\land}p)\bar{\land}(q\bar{\land}q)=(p\bar{\lor}q)\bar{\lor}(p\bar{\lor}q)$,
    -   $p\to q=p\bar{\land} (q\bar{\land} q)=((p\bar{\lor}p)\bar{\lor}q)\bar{\lor}((p\bar{\lor}p)\bar{\lor}q)$.
    
    In addition,
    
    -   $p=\lnot\lnot p$,
    -   $p\nleftrightarrow q=p\oplus q=(p\lor q)\land\lnot (p\land q)$,
    -   $p\leftrightarrow q=p\odot q=\lnot(p\oplus q)$,
    -   $p\nrightarrow q=\lnot(p\to q)$,
    -   $p\gets q=q\to p$,
    -   $p\nleftarrow q=\lnot(p\gets q)$.

Can we describe all the logical operators using a specified set of logical operators? This leads to the definition of a functionally complete operator set.

???+ abstract "Definition"
    For a given set of logical operators, if all the logical operators can be described using only the functions in this set, then the set is called a **functionally complete operator set**. In particular, if all the logical operators can be described using just one logical operator, then that operator is called a **sole sufficient operator** or a **Sheffer function**.
    
    If removing any one element from a functionally complete operator set makes it unable to describe all the logical operators, then the set is called a **minimal functionally complete operator set**.

It can be proved that among the logical operators only $\bar{\land}$ and $\bar{\lor}$ are sole sufficient operators.

The following are common minimal functionally complete operator sets[^vaughan1942complete]:

-   $\{\bar{\land}\}$, $\{\bar{\lor}\}$,
-   $\{\land,\lnot\}$, $\{\lor,\lnot\}$, $\{\gets,\lnot\}$, $\{\to,\lnot\}$, $\{\nleftarrow,\lnot\}$, $\{\nrightarrow,\lnot\}$,
-   $\{\gets,\bot\}$, $\{\to,\bot\}$, $\{\nleftarrow,\top\}$, $\{\nrightarrow,\top\}$,
-   $\{\gets,\nleftarrow\}$, $\{\to,\nleftarrow\}$, $\{\gets,\nrightarrow\}$, $\{\to,\nrightarrow\}$,
-   $\{\gets,\nleftrightarrow\}$, $\{\to,\nleftrightarrow\}$, $\{\nleftarrow,\leftrightarrow\}$, $\{\nrightarrow,\leftrightarrow\}$,
-   $\{\lor,\leftrightarrow,\bot\}$, $\{\lor,\leftrightarrow,\nleftrightarrow\}$, $\{\lor,\nleftrightarrow,\top\}$,
-   $\{\land,\leftrightarrow,\bot\}$, $\{\land,\leftrightarrow,\nleftrightarrow\}$, $\{\land,\nleftrightarrow,\top\}$.

### Properties

First are properties related to algebraic structure:

-   Both AND and OR form a [commutative monoid](./algebra/basic.md#groups) over $\mathbf{B}$. That is, both the AND operation and the OR operation have commutativity, associativity, and an identity ($x\land 1=x\lor 0=x$).
-   Both XOR and XNOR form a [group](./algebra/basic.md#groups) over $\mathbf{B}$. That is, both the XOR operation and the XNOR operation have commutativity, associativity, an identity ($x\oplus 0=x\odot 1=x$), and an inverse ($x\oplus x=0$, $x\odot x=1$).
-   Neither NAND nor NOR has associativity, so they do not form a semigroup.

For $\land$ and $\lor$, we have

-   Distributive laws:
    -   $a\land(b\diamond c)=(a\land b)\diamond (a\land c)$, where $\diamond$ can be $\land$, $\lor$, $\oplus$,
    -   $a\lor(b\diamond c)=(a\lor b)\diamond (a\lor c)$, where $\diamond$ can be $\land$, $\lor$, $\odot$.
-   **Idempotence** law: $x\land x=x$, $x\lor x=x$.
-   Monotonicity: $a\to b\iff(a\land c)\to(b\land c)$, $a\to b\iff(a\lor c)\to(b\lor c)$.
-   **Absorption** law: $x\land(x\lor y)=x\lor(x\land y)=x$.
-   Relation with "$\to$":
    -   $a \lor b \iff (\lnot a \to b) \land (\lnot b \to a)$,
    -   $a \land b \iff \lnot((a \to \lnot b) \lor (b \to \lnot a))$.

???+ abstract "Monotonicity of a boolean function"
    For a boolean function $f(x_1,\dots,x_n)$ and two elements $(a_1,\dots,a_n),(b_1,\dots,b_n)$ in $\mathbf{B}^n$, if whenever $a_i\leq b_i,~~\forall i=1,\dots,n$ it always holds that $f(a_1,\dots,a_n)\leq f(b_1,\dots,b_n)$, then this boolean function is said to be monotone.

We also have the following properties:

-   **Law of excluded middle**: $p\lor\lnot p$ is a tautology.
-   $\lnot p\iff p\to\bot$.
-   Double negation / **involution** law of $\lnot$: $\lnot\lnot x=x$.
-   Involution law of $\oplus$, $\odot$: $x\oplus y\oplus y=x$, $x\odot y\odot y=x$.
-   De Morgan's laws: $\lnot(p\land q)=\lnot p\lor \lnot q$, $\lnot(p\lor q)=\lnot p\land \lnot q$.

## Standardization of logical expressions

Based on the above properties, we can perform certain equivalent transformations on a logical expression to make it conform to a specific normal form, which can be used in automated theorem proving. Common standardized normal forms include **conjunctive normal form** (CNF), **disjunctive normal form** (DNF), and **algebraic normal form** (ANF).

???+ abstract "Conjunctive normal form and disjunctive normal form"
    We make the following recursive definition:
    
    1.  **Literal**: for a variable $x$, $x$ and $\lnot x$ are literals.
    2.  Subformula:
        -   a literal is a subformula,
        -   if $A$ is a literal and $B$ is a subformula, then $A\lor B$ is a subformula.
    3.  Conjunctive normal form:
        -   if $A$ is a subformula, then $(A)$ is a conjunctive normal form,
        -   if $A$ is a subformula and $B$ is a conjunctive normal form, then $(A)\land B$ is a conjunctive normal form.
    
    Similarly, swapping $\land$ and $\lor$ in the above definition gives the definition of disjunctive normal form.

For example, the following logical expressions are all disjunctive normal forms:

-   $(A\land\lnot B)\lor(C\land D\land\lnot E)$,
-   $(A\land B)\lor (C)$,
-   $(A\land B)$,
-   $(A)$.

The following logical expressions are all conjunctive normal forms:

-   $(\lnot A\lor\lnot B\lor C)\land(\lor D\lor\lnot E)$,
-   $(A\lor B)\land (C)$,
-   $(A\lor B)$,
-   $(A)$.

The following logical expressions are neither conjunctive normal forms nor disjunctive normal forms:

-   $\lnot(A\land B)$,
-   $A\land (B\lor (C\land D))$.

We can transform any logical expression containing only the $\lnot$, $\land$, $\lor$ operations into DNF through the following steps:

$$
\begin{array}{rcccl}
    \lnot\lnot x &&\mapsto&& x,\\
    \lnot(x\lor y) &&\mapsto&& \lnot x\land \lnot y,\\
    \lnot(x\land y) &&\mapsto&& \lnot x\lor \lnot y,\\
    x\land(y\lor z) &&\mapsto&& (x\land y)\lor (x\land z),\\
    (x\lor y)\land z &&\mapsto&& (x\land z)\lor (y\land z).
\end{array}
$$

To obtain the CNF of an expression $X$, one only needs to obtain the DNF of $\lnot X$, then negate it and apply De Morgan's laws.

???+ abstract "Algebraic normal form"
    First, we define subformulas by the following recursive definition:
    
    -   a variable $x$ is a subformula,
    -   if $A$ is a subformula and $x$ is a variable, then $x\land A$ is a subformula.
    
    Then a logical expression satisfying one of the following three forms is an algebraic normal form:
    
    1.  $1$, $0$,
    2.  the XOR of several inequivalent subformulas, such as $a\oplus b\oplus(a\land b)\oplus(a\land b\land c)$,
    3.  the XOR of several inequivalent subformulas with a single $1$, such as $1\oplus a\oplus b\oplus(a\land b)\oplus(a\land b\land c)$.

Note that algebraic normal forms correspond one-to-one with polynomials over $\mathbf{Z}_2$, so an algebraic normal form is also called a **Zhegalkin polynomial**.

We can transform any logical expression containing only the $\lnot$, $\land$, $\lor$, $\oplus$ operations into ANF through the following steps:

1.  $\oplus$: expand directly, such as $(1\oplus x)\oplus(1\oplus x\oplus y)=1\oplus x\oplus 1\oplus x\oplus y=y$,
2.  $\land$: expand using the distributive law, such as $x\land(1\oplus x\oplus y)=(x\land 1)\oplus (x\land x)\oplus (x\land y)=x\oplus (x\land y)$,
3.  $\lnot$: replace $\lnot x$ with $1\oplus x$, such as $\lnot(1\oplus x\oplus y)=1\oplus 1\oplus x\oplus y=x\oplus y$,
4.  $\lor$: replace $x\lor y$ with $1\oplus((1\oplus x)\land(1\oplus y))$ or $x\oplus y\oplus (x\land y)$, such as $(1\oplus x)\lor(1\oplus x\oplus y)=1\oplus((1\oplus 1\oplus x)\land(1\oplus 1\oplus x\oplus y))=1\oplus x\oplus(x\land y)$.

## References and notes

1.  [Boolean algebra - Wikipedia](https://en.wikipedia.org/wiki/Boolean_algebra)
2.  [Boolean function - Wikipedia](https://en.wikipedia.org/wiki/Boolean_function)
3.  [Logical connective - Wikipedia](https://en.wikipedia.org/wiki/Logical_connective)
4.  [Disjunctive normal form - Wikipedia](https://en.wikipedia.org/wiki/Disjunctive_normal_form)
5.  [Zhegalkin polynomial - Wikipedia](https://en.wikipedia.org/wiki/Zhegalkin_polynomial)

[^note1]: When used for propositional deduction, one should use double-lined long arrows, such as $A\implies B$, $A\impliedby B$, $A\iff B$, etc.

[^note2]: Equivalent to XNOR.

[^note3]: Equivalent to XOR.

[^vaughan1942complete]: Vaughan, H. E. (1942). Complete sets of logical functions. *Transactions of the American Mathematical Society 51*: 117–32.
