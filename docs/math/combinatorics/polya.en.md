author: Wajov, Early0v0, Enter-tainer, Great-designer, iamtwz, Ir1d, MegaOwIer, mgt, StudyingFather, Tiphereth-A, warzone-oier, Xeonacid, c-forrest

Prerequisites: [Permutations and arrangements](../permutation.md)

## Introduction

The Pólya enumeration theorem is usually used to solve some counting problems involving "essentially different" objects.

???+ info "This article may involve content related to group theory"
    This article may involve content related to group theory. This article gives simple explanations of the group-theory concepts involved, so as to facilitate understanding and application of the Pólya enumeration theorem for readers unfamiliar with the relevant content. For rigorous statements and discussions of group theory, please refer to chapters such as [Basic concepts of abstract algebra](../algebra/basic.md) and [Group theory](../algebra/group-theory.md).

??? info "\"Symmetry group\", \"symmetric group\", and \"permutation group\""
    In this article it is unavoidable to use the names of these three kinds of groups simultaneously. Although this may easily cause confusion, they do refer to different concepts. Given a geometric structure, the symmetry operations on it refer to the geometric transformations that make it coincide with itself, and the symmetry group is the set of these symmetry operations. The symmetric group is the set of all permutations on a given set. The permutation group is a subgroup of the symmetric group, i.e. a group formed by some (not necessarily all) permutations. The following text explains how to represent the symmetry group of a given geometric structure in the form of a permutation group, and use it for counting problems.

## Burnside's lemma

Related reading: [Burnside's lemma](../algebra/group-theory.md#burnsides-lemma)

The Pólya enumeration theorem is an application and generalization of Burnside's lemma. Before introducing the Pólya enumeration theorem, we first briefly review the content of Burnside's lemma.

To summarize a general pattern, first consider a simple example.

???+ example "Necklace coloring"
    Now there is a necklace of four beads in total; each bead can be red or blue. Compute how many essentially different necklaces there are. (If the results of two colorings can coincide by rotating the necklace, they are considered the same.)

??? example "Solution and analysis"
    This problem is simple enough to be solved by enumeration. There are $4$ beads in total, each of which can be colored in $2$ colors, so the total number of possible colorings of the necklace is $2^4=16$. Grouping together those that can be obtained from one another by rotation, there are $6$ groups in total, as shown in the figure below. (Here, the encoding of a single coloring represents the colors colored clockwise starting from the bead at the lower-left corner, $B$ denotes blue, $R$ denotes red; colorings assigned to the same group have the same background color.)
    
    ![Necklace coloring](../images/necklaces.svg)
    
    From this example, one can see that to compute the number of essentially different colorings, the key is actually to know how many different colorings correspond to each essentially-identical coloring. That is, to figure out the size of each group in the figure above.
    
    Colorings that can be assigned to the same group are those that can be transformed into one another by rotation operations. There are $4$ ways of rotation in total, i.e.
    
    $$
    G=\{r_0,r_1,r_2,r_3\},
    $$
    
    denoting rotation by $0,1,2,3$ times respectively. Rotating $0$ times is staying in place.
    
    First look at the group in which the coloring $RRBB$ lies. Applying these four operations to it, we respectively obtain
    
    $$
    RRBB, RBBR, BBRR, BRRB.
    $$
    
    The four colorings are mutually distinct, so this group has $4$ elements.
    
    Next look at the group in which the coloring $BRBR$ lies. Applying the same four operations to it, we respectively obtain
    
    $$
    BRBR, RBRB, BRBR, RBRB.
    $$
    
    In this case, the result of rotating twice is the same as the result of not rotating, and the result of rotating three times is the same as rotating once. So this group has $2$ elements.
    
    Now look at the groups in which the colorings $BBBB$ and $RRRR$ lie. Applying the four operations to them, the results are all themselves. Therefore, each group has only $1$ element.
    
    If we use $x$ to denote a coloring and $Gx$ to denote the set of color encodings obtainable after operating on the coloring $x$, then from the above example one can summarize a pattern, namely that the effect of the operations of $G$ on $x$ has a certain "periodicity".
    
    Let $|G|$ denote the total number of operations; this "periodicity" of the effect means that if there are $m$ different operations in $G$ that transform the coloring $x$ to itself, then the results of $x$ under these operations repeat $m$ times. Therefore, the coloring $x$ has a total of $|G|/m$ different results under these operations, which is also the size of the group in which $x$ lies.
    
    In this example, because only rotating zero times $r_0$ can transform $RRBB$ to itself, the size of the group it lies in equals $4/1=4$; and both rotating zero times $r_0$ and twice $r_2$ can transform $BRBR$ to itself, so the size of the group it lies in equals $4/2=2$; no matter how many times we rotate, we can transform $BBBB$ to itself, so the size of the group it lies in is $4/4=1$.
    
    In the following description, we use $G_x$ to denote the number of operations that can transform $x$ to itself, so $|G_x|$ is the $m$ above. In this case, the size of the group in which $X$ lies is $|G|/|G_x|$. To compute the number of groups of colorings, one only needs to exhaust all possible colorings $x\in X$, and assign weight $1/|Gx|$ to a coloring $x$ whose group size is $|Gx|$; then the number of groups can be expressed as
    
    $$
    |X/G|=\sum_{x\in X}\frac{1}{|Gx|}=\sum_{x\in X}\frac{|G_x|}{|G|}.
    $$
    
    The form of this expression is not convenient for application now. Let $gx$ be the result of applying operation $g\in G$ to a coloring $x\in X$; then the set $G_x$ described above is $\{g\in G:gx=x\}$, so swapping the summation order gives
    
    $$
    \begin{aligned}
    \sum_{x\in X}|G_x| 
    &=\sum_{x\in X}|\{g\in G:gx=x\}|\\
    &=\sum_{x\in X}\sum_{g\in G}[gx=x]\\
    &=\sum_{g\in G}\sum_{x\in X}[gx=x]\\
    &=\sum_{g\in G}|\{x\in X:gx=x\}|\\
    &=\sum_{g\in G}|X^g|.
    \end{aligned}
    $$
    
    where $[\cdot]$ is the Iverson bracket. In the result of swapping the summation signs, $X^g=\{x\in X:gx=x\}$ refers to the set of colorings $x$ that remain unchanged under operation $g$. In short, it is the set of fixed points of operation $g$.
    
    After these discussions, we can now write the number of groups as
    
    $$
    |X/G|=\frac{1}{|G|}\sum_{g\in G}|X^g|.
    $$
    
    That is, the number of groups is the average number of fixed points of the various rotation operations.
    
    As an application of this result, let us again compute the number of necklace colorings. The fixed points of these rotation operations can be listed as follows.
    
    |  Operation  |          Fixed points          |
    | :---: | :-----------------------: |
    | $r_0$ |            $X$            |
    | $r_1$ |      $\{BBBB,RRRR\}$      |
    | $r_2$ | $\{BBBB,BRBR,RBRB,RRRR\}$ |
    | $r_3$ |      $\{BBBB,RRRR\}$      |
    
    Therefore, the number of groups equals
    
    $$
    \frac{16+2+4+2}{4} = 6.
    $$
    
    This gives the earlier result.

From this example, one can induce a general result for solving this kind of counting problem. For convenience of discussion, the scenario considered in this article is the coloring problem; of course it can also be applied to other scenarios, and corresponding examples will be provided at the end of the article.

The coloring problem says: given some structure, coloring each of its vertices yields different colorings. This structure has some symmetry that makes seemingly different colorings transformable into one another after a series of symmetry operations. These mutually-transformable colorings are called essentially the same. The problem is to find the number of essentially different colorings.

According to the analysis in the example, to solve such a problem, we first need to discuss what symmetry operations the given structure has. The set $G$ of these symmetry operations is called the symmetry group of the given structure. In practical applications, most of the time there is no need to understand the definition of a group; one only needs to be able to discuss all the symmetry operations without repetition or omission. Later in this article we analyze the structure of several common symmetry groups, where the definition of a group is explained.

The set of all colorings is denoted $X$, and a single coloring in it is denoted $x$. The result of operation $g\in G$ acting on a coloring $x\in X$ is $gx$. Then all results obtainable by acting on a coloring $x$ via some operation form $Gx=\{gx:g\in G\}$, called the orbit of $x$ under the action of the group $G$. Different colorings in the same orbit are precisely the so-called "essentially the same" in this kind of problem. Therefore, the number of all essentially different colorings is equivalent to the number of distinct orbits.

The analysis in the example can be generalized to the general case.

???+ note "Burnside's lemma"
    Given the action of a group $G$ on a set $X$, the number of all distinct orbits
    
    $$
    |X/G|=\frac{1}{|G|}\sum_{g\in G}|X^g|.
    $$
    
    Here, $X^g=\{x\in X:gx=x\}$ is the set of fixed points under the action of $g\in G$.

Its proof almost directly copies the analysis in the example above. But the example used the observation that the result of the action of the group $G$ on a single element $x$ has some "periodicity", so the number of these periodic repetitions equals the number of operations that can transform $x$ to itself. This observation is correct in the general case, but because the structure of the group $G$ may be very complex, its "periodicity" is not necessarily as direct as presented in the example. To state this observation rigorously requires the [orbit-stabilizer theorem](../algebra/group-theory.md#stabilizer) from group theory.

In applications, as long as one can list all the symmetry operations and give the number of fixed points corresponding to each symmetry operation, the corresponding counting problem can be solved. The following is a slightly more complex application.

???+ example "Cube coloring"
    Coloring a cube with three colors, find the number of essentially different schemes (two schemes that are the same after a spatial rotation are regarded as the same).

??? example "Solution"
    Because a cube has $6$ faces and each face has $3$ coloring methods, there are $3^6$ colorings in total, i.e. $|X|=3^6$. Denote the symmetry group of the cube by $G$.
    
    ![](../images/cube.svg)
    
    Next we need to analyze all the operations in $G$; they can be divided into the following classes (for convenience, the six faces of the cube are called front, back, top, bottom, left, right):
    
    -   Fixed: i.e. the identity transformation; because all direct colorings are unchanged under the identity transformation, its corresponding $|X^g|=3^6$;
    -   $90^\circ$ rotation about the axis connecting the centers of two opposite faces: there are $3$ choices of opposite faces and $2$ choices of rotation direction, so this class has $6$ permutations in total. Assuming the axis connecting the centers of the front and back faces is chosen, the colors of the top, bottom, left, right faces must be the same to keep it unchanged after rotation. In this case, there are $3$ independently colorable regions, so its corresponding $|X^g|=3^3$;
    -   $180^\circ$ rotation about the axis connecting the centers of two opposite faces: there are $3$ choices of opposite faces, and the choice of rotation direction has no effect, so this class has $3$ permutations in total. Assuming the axis connecting the centers of the front and back faces is chosen, the colors of the top and bottom faces must be the same and the colors of the left and right faces must be the same to keep it unchanged after rotation. In this case, there are $4$ independently colorable regions, so its corresponding $|X^g|=3^4$;
    -   $180^\circ$ rotation about the axis connecting the midpoints of two opposite edges: there are $6$ choices of opposite edges, and the rotation direction still has no effect on the permutation, so this class has $6$ permutations in total. Assuming the boundary of the front and top faces and the boundary of the bottom and back faces are chosen as opposite edges, then the colors of the front and top faces must be the same, the colors of the bottom and back faces must be the same, and the colors of the left and right faces must be the same to keep it unchanged after rotation. In this case, there are $3$ independently colorable regions, so its corresponding $|X^g|=3^3$;
    -   $120^\circ$ rotation about the axis connecting two opposite vertices: there are $4$ choices of opposite vertices and $2$ choices of rotation direction, so this class has $8$ permutations in total. Assuming the upper-right corner of the front and the lower-left corner of the back are chosen as opposite vertices, then the colors of the front, top, right faces must be the same and the colors of the back, bottom, left faces must be the same to keep it unchanged after rotation. In this case, there are $2$ independently colorable regions, so its corresponding $|X^g|=3^2$.
    
    Therefore, the number of all essentially different colorings is
    
    $$
    \frac{1\times3^6+6\times3^3+3\times3^4+6\times3^3+8\times3^2}{1+6+3+6+8}=57.
    $$

## Pólya enumeration theorem

In the statement of Burnside's lemma, the property that the set $X$ is all colorings on some structure was not used. In fact, the scope of application of Burnside's lemma is not limited to coloring-counting problems. For coloring-counting problems, the Pólya enumeration theorem provides a more precise computation method. It can be regarded as an application of the general Burnside's lemma to coloring-counting problems.

Compared with Burnside's lemma, the improvement of the Pólya enumeration theorem is that it provides a specific computation method for the fixed-point set size $|X^g|$ in coloring-counting problems.

This can be seen intuitively from the cube-coloring example above. For the various symmetry operations of the cube, the size of its fixed-point set is always of the form $m^{c(g)}$, where $m$ is the number of colors and $c(g)$ is the number of independently colorable regions under operation $g$. This observation also holds in the general case, but one needs to further clarify how to compute the value of $c(g)$ for a given $g$.

Choosing a coloring for some structure, expressed in mathematical language, is choosing a map $f:X\rightarrow C$ from the set $X$ of colorable objects of this structure (such as beads in a necklace, faces of a cube, etc.) to the color set $C$. Therefore, the set of colorings is $C^X$. The symmetry group $G$ of this structure acts on the structure, and naturally acts on the set $X$ as well. Such a symmetry operation always corresponds to a bijection on the set $X$, i.e. a **permutation**.[^perm-group]

Now analyze the structure of the fixed-point set $(C^X)^g$. Given $g$, viewed as a permutation on $X$, by analogy with the analysis in the example, one can see that if a position $x$ in $X$ can be moved to a position $y$ after finitely many repetitions of operation $g$, then, as a fixed point $f\in (C^X)^g$, it must satisfy $f(x)=f(y)$. In the language of orbits from the previous section, because positions $x$ and $y$ are in the same orbit of the action[^g-act] of operation $g$, they need to be colored the same color. In the language of permutations, in the [cycle decomposition](../permutation.md#轮换表示) of the permutation $g$, positions $x$ and $y$ are in the same cycle, so they need to be colored the same color. Different cycles in the cycle decomposition need not be colored the same and can be colored independently, so in this case the number of independently colorable regions is $c(g)$, i.e. the number of cycles in the cycle decomposition of $g$.

From this, the number of fixed points of operation $g$ is $|C|^{c(g)}$. Substituting this conclusion into Burnside's lemma gives the unweighted version of the **Pólya enumeration theorem**.

???+ note "Pólya enumeration theorem (unweighted version)"
    Given the action of a group $G$ on a set $X$ and a color set $C$, the number of different colorings
    
    $$
    |C^X/G|=\frac{1}{|G|}\sum_{g\in G}m^{c(g)},
    $$
    
    Here, $m$ is the number of colors, and $c(g)$ is the number of cycles in the cycle decomposition of the permutation representation of the element $g\in G$.

??? info "On the meaning of the group $G$"
    Here there is a slight abuse of notation. If the group $G$ acts on $X$, then the group action on the coloring set $C^X$ needs to be redefined; no distinction is made here.

As a simple application of the Pólya enumeration theorem, below we again use the Pólya enumeration theorem to compute the earlier example.

??? example "Another solution to the necklace-coloring problem"
    Label the four beads $1\sim 4$; then the elements of the group $G$ in the example have permutation representations as follows: (all written in cycle-decomposition form)
    
    -   rotating zero times $r_0=(1)$, $4$ cycles in total (note the omitted $1$-cycles);
    -   rotating once $r_1=(1234)$, $1$ cycle in total;
    -   rotating twice $r_2=(13)(24)$, $2$ cycles in total;
    -   rotating three times $r_3=(1432)$, $1$ cycle in total.
    
    Therefore, the number of essentially different colorings is
    
    $$
    \frac{2^4+2^1+2^2+2^1}{4}=6.
    $$

??? example "Another solution to the cube-coloring problem"
    Since the earlier analysis has essentially already given the cycle representations of the various classes of permutations, only without writing them explicitly with numeric symbols, we do not repeat the earlier analysis here. We only consider the case of $180^\circ$ rotation about the axis connecting the midpoints of opposite edges as an illustration. Numbering the six faces front, back, top, bottom, left, right as $1\sim6$ in order, the corresponding permutation in this case is $(13)(24)(56)$, so $c(g)=3$. The other types of permutations can be analyzed similarly, and the final counting expression is also entirely consistent with the above.

## Weighted-form generalization

The unweighted version of the Pólya enumeration theorem can only count all essentially different colorings, but is powerless when handling more refined problems. For example, if in the above coloring problem the number of each usable color is given, one cannot apply the above Pólya counting formula. When actually solving such problems, one needs to use Burnside's lemma again for the derivation; and summarizing these results in the form of a generating function gives the weighted version of the Pólya enumeration theorem.

???+ example "Necklace coloring (with constraints)"
    Now there is a necklace of four beads in total; each bead can be red or blue, and exactly two red beads and two blue beads are usable. Compute how many essentially different necklaces there are. (If the results of two colorings can coincide by rotating the necklace, they are considered the same.)

??? example "Solution and analysis"
    Consider using Burnside's lemma. With two red beads and two blue beads each, there are $\dbinom{4}{2}=6$ colorings in total. The symmetry group $G=\{r_0,r_1,r_2,r_3\}$ corresponds to rotating $0\sim3$ times respectively, and the analysis of their corresponding fixed-point sets is as follows:
    
    -   rotating zero times $r_0=(1)$, all $6$ colorings are fixed points;
    -   rotating once $r_1=(1234)$, a fixed point requires all beads to be colored the same, so there are no fixed points;
    -   rotating twice $r_2=(13)(24)$, there are two independently colorable regions, both of size $2$, which must be colored red and blue respectively, so the size of the fixed-point set is $2$;
    -   rotating three times $r_3=(1432)$, same as the case of rotating once, no fixed points.
    
    So, by Burnside's lemma, the number of essentially different colorings is
    
    $$
    \frac{6+0+2+0}{4}=2.
    $$

From this example one can summarize the following computation method. For problems constraining the number of different colors, one likewise needs to color the cycles of each permutation in the symmetry group, but needs to make the number of colors used in the coloring exactly equal to the given number of colors. Such combinatorial problems usually have no explicit solution; except for special cases that can be computed by [permutation and combination methods](../combinatorics/combination.md), they need to be treated as [knapsack problems](../../dp/knapsack.md) to be solved.

The answer to such counting problems can be given via generating functions. Given a permutation $g$, if its [type](../permutation.md#置换的型) is $1^{\alpha_1}2^{\alpha_2}\cdots n^{\alpha_n}$, i.e. it has $\alpha_k$ cycles of length $k$, and each cycle can be colored in one of $m$ colors, then in the generating function

$$
\prod_{k=1}^n\left(\sum_{i=1}^mx_i^k\right)^{\alpha_k}
$$

the coefficient of the monomial $x_1^{\beta_1}x_2^{\beta_2}\cdots x_m^{\beta_m}$ is the count of using the $i$-th color $\beta_i$ times. Here the combinatorial meaning of the expression $\sum_{i=1}^mx_i^k$ in parentheses is: for a cycle of length $k$, the count of the coloring method using color $i$ $k$ times is $1$, and for other cases the count is $0$; this precisely describes the requirement that all positions in the same cycle be colored consistently.

Given the generating function of the coloring count under a permutation $g$, applying Burnside's lemma to each monomial gives the essentially-different counts under various color combinations. Because the generating function is linear in each monomial, the generating function of the count of essentially different colorings is

$$
\frac1{|G|}\sum_{g\in G}\prod_{k=1}^n\left(\sum_{i=1}^mx_i^k\right)^{\alpha_k}.
$$

Expanding this expression, the coefficient of each monomial gives the count of essentially different colorings under the given color combination.

In the above process, the generating function $\sum_{i=1}^mx_i^k$ for coloring each cycle is nothing special, and can be replaced with other generating functions. Therefore, we have the following general version of the Pólya enumeration theorem.

???+ note "Cycle index of a permutation group"
    Given a permutation group $G$, the **cycle index** of the group $G$ is defined as
    
    $$
    Z_G(t_1,t_2,\cdots,t_n)=\frac{1}{|G|}\sum_{g\in G}t_1^{c_1(g)}t_2^{c_2(g)}\cdots t_n^{c_n(g)},
    $$
    
    where $c_k(g)$ is the number of cycles of length $k$ in the cycle decomposition of the permutation $g$, i.e. $1^{c_1(g)}2^{c_2(g)}\cdots n^{c_n(g)}$ is the type of the permutation $g$.

???+ note "Pólya enumeration theorem (weighted version)"
    Given the action of a group $G$ on a set $X$, where the coloring method of each point is given by the generating function $f(x_1,x_2,\cdots,x_m)$ of the count of its colorings, then the generating function of the count of essentially different colorings of the set $X$ is
    
    $$
    Z_G(f(x_1^1,x_2^1,\cdots,x_m^1),f(x_1^2,x_2^2,\cdots,x_m^2),\cdots,f(x_1^n,x_2^n,\cdots,x_m^n)),
    $$
    
    Here, $Z_G(t_1,t_2,\cdots,t_n)$ is the cycle index of the group $G$.

Here, if the generating function of the coloring of a single position is $f(x_1,x_2,\cdots,x_m)$, then the generating function of the coloring of a cycle of length $k$ is $f(x_1^k,x_2^k,\cdots,x_m^k)$. This reflects that if some coloring is a fixed point of the given permutation, then all positions in the same cycle must be colored the same color. If the generating function is evaluated at $x_i=1$, one obtains the unweighted version of the Pólya enumeration theorem above.

The statement of the theorem uses the concept of the cycle index of a permutation group. It is independent of the specific coloring problem. It describes the structure of the permutation group.

??? example "Another solution to the constrained necklace-coloring problem"
    The cycle index of the rotational symmetry group is $\dfrac14\left(t_1^4+t_2^2+2t_4\right)$, and the generating function of a single-point coloring is $r+b$, so the generating function of all colorings is
    
    $$
    \begin{aligned}
    F(r,b)&=\frac14\left((r+b)^4+(r^2+b^2)^2+2(r^4+b^4)\right)\\
    &=r^4+r^3b+2r^2b^2+rb^3+b^4.
    \end{aligned}
    $$
    
    The count sought is the coefficient of $r^2b^2$, i.e. a total of $2$ essentially different colorings. Incidentally, this expression also gives the counts under other constraints.

### Applications

The weighted version of the Pólya enumeration theorem plays an important role in combinatorial counting problems. Here we briefly discuss its applications, and a more general discussion can be found in [the symbolic method for combinatorial problems](../poly/symbolic-method.md#有限制的构造).

???+ example "Diamond necklace"
    Now there is a necklace of four identical beads in total; each bead can be set with several diamonds. If there are four diamonds, how many essentially different diamond-setting ways are there in total. (If the results of two diamond settings can coincide by rotating the necklace, they are considered the same.)

??? example "Solution and analysis"
    The symmetry group of the necklace is still the same as described earlier. Without considering the constraint on the total number of diamonds, the generating function of the diamond-setting scheme for a single position is
    
    $$
    f(x)=1+x+x^2+\cdots=\sum_{i=1}^\infty x^i=\frac{1}{1-x}.
    $$
    
    Applying the weighted version of the Pólya enumeration theorem, the generating function of all diamond-setting schemes is
    
    $$
    \begin{aligned}
    F(x)&=\frac14\left(f(x)^4+f(x^2)^2+2f(x^4)\right)\\
    &=1+x+3x^2+5x^3+10x^4+\cdots.
    \end{aligned}
    $$
    
    Therefore, the number of diamond-setting schemes sought is the coefficient of $x^4$, i.e. a total of $10$ schemes. As a verification, by enumeration one can see that they are respectively
    
    $$
    4000,3100,3010,3001,2200,2020,2110,2101,2011,1111.
    $$
    
    Here, each group of four numbers denotes the number of diamonds set on each bead.

This example shows that the problems the weighted version of the Pólya enumeration theorem can solve are far broader than coloring-counting problems. It provides a way to extend a single-point count to an essentially-different count over the entire structure. The coloring problem is only a special case of this kind of problem.

## Common symmetry groups

One of the difficulties of Pólya-counting-related problems lies in analyzing the structure of the permutation group. Here we briefly discuss the structure of common symmetry groups, and describe them using their cycle indices. It should be noted that for the symmetry group of the same structure, if the set of objects acted upon is different, the corresponding [group action](../algebra/group-theory.md#group-action) is also different, so their permutation representations are also different. For example, the action of the symmetry group of a cube on its vertices, edges, and faces corresponds respectively to the vertex permutation group, edge permutation group, and face permutation group of the cube; the numbers of vertices, edges, and faces are mutually different, so these permutation groups and the corresponding cycle indices are of course also different. So, when solving specific problems, one cannot ignore the specification of the object of the group action.

??? info "The relationship between the symmetry group and the permutation group"
    Although the two concepts are very similar, they are by no means the same object. In the language of group theory, given a symmetry group $G$ and its group action on a set $X$, the permutation representation of the group action in fact provides a homomorphism $\varphi$ from the group $G$ to the symmetric group $S_X$, and this permutation representation is often faithful in the context of combinatorial counting, i.e. $\ker\varphi=\{e\}$, so the homomorphism $\varphi$ is in fact an embedding of the group $G$ into the group $S_X$. The permutation group in the text is the image of this embedding, i.e. $\varphi(G)$, which is isomorphic to the symmetry group $G$ itself. Therefore, for the symmetry group $G$ on the same structure, if the choice of group action is inconsistent, it will be isomorphic to a different permutation group $\varphi(G)$, and thus have a different cycle index (isomorphic permutation groups do not necessarily have the same cycle index).

Given a structure, its symmetry group is the set of all operations that can transform it to itself. It must satisfy the following conditions:

-   Applying two symmetry operations to the given structure in succession can be regarded as applying another symmetry operation, i.e. the set of symmetry operations is closed under composition;
-   The composition of symmetry operations satisfies associativity;
-   There exists an identity symmetry operation, i.e. keeping the given structure unchanged is itself regarded as an operation;
-   Every operation has its inverse operation, which can cancel the effect of the given operation.

A [group](../algebra/basic.md#groups) is the abstraction of all concepts satisfying these conditions. The discussion of the structure of groups is the main research content of [group theory](../algebra/group-theory.md). The analysis here focuses mainly on symmetry groups, and the discussion of their structure mainly applies a geometric viewpoint. Here we give common examples, from which the reader should gain the common ideas for analyzing this kind of problem.

### Cyclic group

Given a regular $n$-gon, the symmetry group formed by all its rotation operations is called the cyclic group, denoted $C_n$. Denoting the operation of counterclockwise rotation by $(360/n)^\circ$ as $r$, the elements of the group $C_n$ can be written as

$$
C_n=\{e,r,r^2,\cdots,r^{n-1}\}.
$$

Here, $r^k$ refers to the result of repeating operation $r$ $k$ times, i.e. counterclockwise rotation by $(360k/n)^\circ$, and $e=r^0$ refers to the identity transformation.

Whether one considers the action of the cyclic group on the set of all vertices or all edges of the regular $n$-gon, its permutation representation is the same. Taking the set of all vertices as an example to analyze the permutation representation of the group action, its cycle index is

$$
Z(C_n)=\frac1n\sum_{d\mid n}\varphi(d)t_{d}^{n/d}.
$$

Here, $\varphi(\cdot)$ is [Euler's totient function](../number-theory/euler-totient.md) in number theory.

Counting only rotation operations, the symmetry group of a necklace of length $n$ is $C_n$.

??? note "Analysis"
    Suppose the set of vertices is denoted $\{0,1,\cdots,n-1\}$ in counterclockwise order; then $r^k(i)=i+k\bmod n$. The set of vertices in the cycle containing vertex $i$ is
    
    $$
    \{i+\ell k\bmod n:\ell\in\mathbf Z\}.
    $$
    
    Obviously, $i\equiv i+\ell k\pmod n$ if and only if
    
    $$
    \frac{n}{\gcd(k,n)}\mid\ell.
    $$
    
    This means that the length of the cycle containing any vertex $i$ is $\dfrac{n}{\gcd(k,n)}$. Therefore, the permutation $r^k$ has $\gcd(k,n)$ cycles of equal length. Consider combining like terms in the cycle-index expression; given $d\mid n$, the number of $k$ satisfying $\gcd(k,n)=n/d$ is $\varphi(d)$, and the monomials they correspond to are all of the form $t_d^{n/d}$, so we obtain the above cycle-index expression.

### Dihedral group

Given a regular $n$-gon, all its rotations and reflections about axes of symmetry also form a symmetry group, called the dihedral group, denoted $D_{2n}$. Denoting the operation of counterclockwise rotation by $(360/n)^\circ$ as $r$, and the operation of reflection along some given axis of symmetry (such as the line connecting the center and some vertex) as $s$, the operations of the group $D_{2n}$ can be written as

$$
D_{2n}=\{e,r,\cdots,r^{n-1},s,sr,\cdots,sr^{n-1}\}.
$$

Here, $r^k$ is still a rotation operation, and although $sr^k$ is rotating $k$ times first and then reflecting along the given axis of symmetry, it can equivalently be regarded as a reflection along another axis of symmetry. Therefore, the group $D_{2n}$ has $1$ identity transformation, $(n-1)$ rotation operations, and $n$ reflection operations in total. Its group action on the vertex set and the edge set also has the same permutation representation. Its cycle index is

$$
Z(D_{2n})=\frac12Z(C_n)+
\begin{cases}
\dfrac12t_1t_2^k,&n=2k+1,\\
\dfrac14\left(t_1^2t_2^{k-1}+t_2^k\right),&n=2k.
\end{cases}
$$

??? note "Analysis"
    The analysis of the set of rotation operations $r^k$ (including the identity transformation) in the group $D_{2n}$ is exactly the same as for the cyclic group $C_n$; the key lies in the analysis of the remaining reflection operations. Here we need to discuss cases according to the parity of the number of vertices $n$.
    
    When $n=2k+1$, the axes of symmetry of all reflection operations connect a vertex and the midpoint of its opposite edge, and there are $n$ such axes of symmetry in total. After each reflection operation, the vertex on the axis of symmetry remains fixed, while the other vertices are swapped in pairs, so there is $1$ fixed point ($1$-cycle) and $k$ $2$-cycles.
    
    When $n=2k$, there are two kinds of axes of symmetry. Among them, half of the axes of symmetry connect opposite vertices; reflecting along such an axis keeps the two vertices on the axis fixed while swapping the remaining vertices in pairs, so there are $2$ fixed points ($1$-cycles) and $(k-1)$ $2$-cycles. The other half of the axes of symmetry connect the midpoints of opposite edges; reflecting along such an axis swaps all vertices in pairs, so there are $k$ $2$-cycles.
    
    Based on this analysis, one can write the above cycle-index expression.

### Symmetric group

Given $n$ elements, all permutations on them form a group, called the symmetric group of degree $n$, denoted $S_n$. It describes all the symmetries these $n$ vertices can have. It is also the permutation representation of the action of these symmetry operations on the vertex set.

According to the analysis in the article [Permutations and arrangements](../permutation.md#置换的型), its cycle index is

$$
Z(S_n)=\sum_{a_1+2\alpha_2+\cdots+n\alpha_n=n}\frac{t_1^{\alpha_1}t_2^{\alpha_2}\cdots t_n^{\alpha_n}}{1^{\alpha_1}2^{\alpha_2}\cdots n^{\alpha_n}\alpha_1!\alpha_2!\cdots\alpha_n!}.
$$

Here we use the fact that the count of permutations of type $1^{\alpha_1}2^{\alpha_2}\cdots n^{\alpha_n}$ is

$$
\frac{n!}{1^{\alpha_1}2^{\alpha_2}\cdots n^{\alpha_n}\alpha_1!\alpha_2!\cdots\alpha_n!}.
$$

It satisfies the recurrence relation

$$
Z(S_n)=\frac1n\sum_{k=1}^nt_kZ(S_{n-k}),
$$

with the recurrence starting point $Z(S_0)=1$. The combinatorial meaning of this recurrence relation is that to construct a permutation of length $n$, one can first choose the length $k$ of the cycle containing point $n$, then construct on the set of the remaining $(n-k)$ vertices.

Given a complete graph with $n$ vertices, its symmetry group is precisely $S_n$. The cycle index of its action on the set of all vertices is given by the $Z(S_n)$ above. However, the permutation representation of its action on the set of all edges is not the same. For example, the size of the set is not the same; the number of all edges is $n(n-1)/2$. For the edge case, additional analysis is needed. Here we give a simple example, and the general case can be found in the exercises.

???+ example "Counting undirected simple graphs"
    Compute the number of undirected simple graphs with $4$ vertices up to isomorphism.

??? example "Solution"
    This is equivalent to coloring the complete graph with $4$ vertices with two colors, and finding the number of essentially different colorings. The symmetry group is $S_4$; now we analyze the cycle index of its edge permutation group $S_4^{(2)}$.
    
    -   identity transformation ($1$ kind): the edges also remain fixed, so the corresponding monomial is $t_1^6$;
    -   swapping two vertices ($6$ kinds): assuming $a$ and $b$ are swapped, then edge $1$ and edge $3$ remain fixed, while edge $2$ and edge $5$ are swapped and edge $4$ and edge $6$ are swapped, so the corresponding monomial is $6t_1^2t_2^2$;
    -   cycling three vertices ($8$ kinds): assuming the cycle is $(abc)$, then the edges $1,2,5$ connecting them are correspondingly cycled, and their edges $4,6,3$ to the fourth point $d$ are correspondingly cycled, so the corresponding monomial is $8t_3^2$;
    -   swapping two pairs of vertices ($3$ kinds): assuming point $a$ and point $b$ are swapped and point $c$ and point $d$ are swapped, then edge $1$ and edge $3$ remain fixed, while edge $2$ and edge $4$ are swapped and edge $5$ and edge $6$ are swapped, so the corresponding monomial is $3t_1^2t_2^2$;
    -   cycling four vertices ($6$ kinds): assuming the cycle is $(abcd)$, then the edges $1,2,3,4$ connecting adjacent vertices are correspondingly cycled, and the edges $5,6$ connecting opposite vertices are simultaneously swapped, so the corresponding monomial is $6t_2t_4$.
    
    So, the cycle index of the edge permutation group is
    
    $$
    Z(S_4^{(2)})=\dfrac{1}{24}(t_1^6+9t_1^2t_2^2+8t_3^2+6t_2t_4).
    $$
    
    By the Pólya enumeration theorem, the number of undirected simple graphs with $4$ vertices up to isomorphism is
    
    $$
    \frac{2^6+9\times 2^4+8\times 2^2+6\times 2^2}{24} = 11.
    $$

### Polyhedral groups

A polyhedral group is the symmetry group of a regular polyhedron. There are only five regular polyhedra: the regular tetrahedron, the cube, the regular octahedron, the regular dodecahedron, and the regular icosahedron. If one keeps the adjacency relations among points, edges, and faces and swaps points and faces, one obtains the dual regular polyhedron. Among them, the regular tetrahedron is dual to itself, the cube and the regular octahedron are dual, and the regular dodecahedron and the regular icosahedron are dual. Using the duality relation, one can simplify the discussion of their symmetry groups.

Counting only the rotation operations that can be carried out in three-dimensional space, there are only three kinds of their symmetry groups.

-   Tetrahedral group, i.e. the symmetry group of the regular tetrahedron:

    -   identity transformation;
    -   rotation by $120^\circ$ and $240^\circ$ about the line connecting a vertex and the center of the opposite face;
    -   rotation by $180^\circ$ about the line connecting the midpoints of opposite edges.

    A total of $1+2\times4+1\times3=12$ symmetry operations.

    The cycle indices of the corresponding permutation groups are as follows.

    -   vertex permutation group and face permutation group: $\dfrac1{12}\left(t_1^4+8t_1t_3+3t_2^2\right)$;
    -   edge permutation group: $\dfrac1{12}\left(t_1^6+8t_3^2+3t_1^2t_2^2\right)$.

-   Octahedral group, i.e. the symmetry group of the cube (and the regular octahedron):

    -   identity transformation;
    -   rotation by $120^\circ$ and $240^\circ$ about the line connecting opposite vertices;
    -   rotation by $180^\circ$ about the line connecting the midpoints of opposite edges;
    -   rotation by $90^\circ$, $180^\circ$, and $270^\circ$ about the line connecting the centers of opposite faces.

    A total of $1+2\times 4+1\times 6+3\times 3=24$ symmetry operations.

    The cycle indices of the corresponding permutation groups of the cube are as follows.

    -   vertex permutation group: $\dfrac{1}{24}\left(t_1^8+8t_1^2t_3^2+9t_2^4+6t_4^2\right)$;
    -   edge permutation group: $\dfrac{1}{24}\left(t_1^{12}+8t_3^4+6t_1^2t_2^5+6t_4^3+3t_2^6\right)$;
    -   face permutation group: $\dfrac{1}{24}\left(t_1^6+8t_3^2+6t_2^3+6t_1^2t_4+3t_1^2t_2^2\right)$.

    The permutation groups of the regular octahedron are similar, only the roles of vertices and faces are swapped.

-   Icosahedral group, i.e. the symmetry group of the regular dodecahedron (and the regular icosahedron):

    -   identity transformation;
    -   rotation by $120^\circ$ and $240^\circ$ about the line connecting opposite vertices;
    -   rotation by $180^\circ$ about the line connecting the midpoints of opposite edges;
    -   rotation by $72^\circ$, $144^\circ$, $216^\circ$, and $288^\circ$ about the line connecting the centers of opposite faces.

    A total of $1+2\times 10+1\times 15+6\times 4=60$ symmetry operations.

    The cycle indices of the corresponding permutation groups of the regular dodecahedron are as follows.

    -   vertex permutation group: $\dfrac{1}{60}\left(t_1^{20}+20t_1^2t_3^6+15t_2^{10}+24t_5^4\right)$;
    -   edge permutation group: $\dfrac{1}{60}\left(t_1^{30}+20t_3^{10}+15t_1^2t_2^{14}+24t_5^6\right)$;
    -   face permutation group: $\dfrac{1}{60}\left(t_1^{12}+20t_3^4+15t_2^6+24t_1^2t_5^2\right)$.

    The permutation groups of the regular icosahedron are similar, only the roles of vertices and faces are swapped.

The ones given here are all cycle indices of permutation groups acting on individual objects such as vertices, edges, and faces separately. If one wants to color different objects simultaneously, one needs to write the joint cycle index.

## Exercises

### Coloring problems

These problems only require analyzing the structure of the permutation group and applying the Pólya enumeration theorem.

-   [Luogu P4980 【模板】Polya 定理](https://www.luogu.com.cn/problem/P4980)
-   [Luogu P2561 \[AHOI2002\] 黑白瓷砖](https://www.luogu.com.cn/problem/P2561)
-   [TRANSP - Transposing is Fun](https://www.spoj.com/problems/TRANSP/)
-   [TRANSP2 - Transposing is Even More Fun](https://www.spoj.com/problems/TRANSP2/)
-   [Luogu P3307 \[SDOI2013\] 项链](https://www.luogu.com.cn/problem/P3307)

When the usable color combinations are constrained, one needs to find the number of ways of coloring the cycles via knapsack DP or combinatorial methods.

-   [Luogu P1446 \[HNOI2008\] Cards](https://www.luogu.com.cn/problem/P1446)
-   [UVA10601 Cubes](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1542)
-   [Luogu P4916 \[MtOI2018\] 魔力环](https://www.luogu.com.cn/problem/P4916)

### Graph enumeration

The Pólya enumeration theorem can be used for [graph enumeration](../combinatorics/graph-enumeration.md) problems; the difficulty of this kind of problem lies in enumerating the edge permutation group of the graph.

-   [SGU 282. Isomorphism](https://codeforces.com/problemsets/acmsguru/problem/99999/282)
-   [Luogu P4727 \[HNOI2009\] 图的同构计数](https://www.luogu.com.cn/problem/P4727)
-   [Luogu P4128 \[SHOI2006\] 有色图](https://www.luogu.com.cn/problem/P4128)

Another kind of graph-enumeration problem to which the Pólya enumeration theorem can be applied requires directly manipulating generating functions.

-   [LOJ 6538 烷基计数 加强版 加强版](https://loj.ac/p/6538)
-   [LOJ 6512「雅礼集训 2018」烷烃计数](https://loj.ac/p/6512)
-   [Luogu P6597 烯烃计数](https://www.luogu.com.cn/problem/P6597)
-   [Luogu P5818 \[JSOI2011\] 同分异构体计数](https://www.luogu.com.cn/problem/P5818)

## References and notes

-   [Pólya enumeration theorem - Wikipedia](https://en.wikipedia.org/wiki/P%C3%B3lya_enumeration_theorem)
-   [Notes on Pólya's Enumeration Theorem](https://www.diva-portal.org/smash/get/diva2:324594/FULLTEXT01.pdf)
-   [Cycle index - Wikipedia](https://en.wikipedia.org/wiki/Cycle_index)

[^perm-group]: Therefore, the symmetry group $G$ can be represented as a permutation group on the set $X$, i.e. a subgroup of the symmetric group $S_X$.

[^g-act]: Strictly speaking, it is the action of the subgroup $\langle g\rangle\le G$.
