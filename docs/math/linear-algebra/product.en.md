This article introduces simple operations between vectors.

Before this article, let us specially explain a translation-related issue. For historical reasons, the mathematics discipline and the physics discipline have all sorts of translations for the two words "inner product" and "outer product".

In the physics discipline, they are generally translated as "标积" (scalar product) and "矢积" (vector product), indicating that the operation results are a scalar and a vector. The high-school mathematics textbook also adopts this free-translation approach with "数量积" (scalar product) and "向量积" (vector product).

In the mathematics discipline, they can also usually be translated as "内积" (inner product) and "外积" (outer product), which are literal translations of the two nouns. "点乘" (dot product) and "叉乘" (cross product) are colloquial names derived from the operation symbols, and these colloquial names are also very common.

In the "dot product" operation, the dot symbol of the operation is often omitted; in linear algebra it is even directly regarded as matrix multiplication, without writing the dot symbol.

## Inner product

The concept of the inner product **applies to vectors of any dimension**.

### Definition

The inner product has different but equivalent ways of definition; below we introduce some of them.

#### Geometric definition

In $n$-dimensional Euclidean space $\mathbf{R}^n$, given two vectors $\boldsymbol{a}, \boldsymbol{b}$ whose angle is $\theta$, then:

$$
\boldsymbol{a} \cdot \boldsymbol{b} = |\boldsymbol{a}| |\boldsymbol{b}| \cos \theta
$$

is the **inner product** of these two vectors, also called the **dot product** or **scalar product**. Here $|\boldsymbol{b}|\cos \theta$ is called the projection of $\boldsymbol{b}$ in the direction of $\boldsymbol{a}$. The geometric meaning of the inner product is: the inner product $\boldsymbol{a} \cdot \boldsymbol{b}$ equals the product of the modulus of $\boldsymbol{a}$ and the projection of $\boldsymbol{b}$ in the direction of $\boldsymbol{a}$.

#### Algebraic definition

In $n$-dimensional Euclidean space $\mathbf{R}^n$, given two vectors $\boldsymbol{a} = (a_1, a_2, \dots, a_n), \boldsymbol{b} = (b_1, b_2, \dots, b_n)$, then:

$$
\boldsymbol{a} \cdot \boldsymbol{b} = \sum_{i = 1}^{n} a_i b_i
$$

is the **inner product** of these two vectors, also called the **dot product** or **scalar product**. The geometric definition and algebraic definition of the inner product are equivalent in Euclidean space, and the latter is more convenient to use.

When no confusion arises, the dot of the inner product can be omitted. If there is a superscript $2$ at the upper-right of a vector, it denotes the abbreviation for the inner product of the vector with itself, i.e. **the square of the modulus of the vector**, with the modulus notation omitted. This superscript $2$ cannot be understood as the square of the vector, because the result of a vector inner product is a scalar, and there is no inner product of any number of vectors other than $2$. Similarly, the square of the square of the modulus of a vector cannot be abbreviated with a superscript $4$, but must regard the result of the superscript $2$ as a whole, and so on.

### Properties

One can find that the result obtained by the inner product is a scalar; its special feature is that it is a bilinear operation that is linear in each of the two vectors separately. Specifically, the inner product satisfies:

$$
\begin{aligned}
(\boldsymbol{a} + \boldsymbol{b}) \cdot \boldsymbol{c} &= \boldsymbol{a} \cdot \boldsymbol{c} + \boldsymbol{b} \cdot \boldsymbol{c} \\
\boldsymbol{a} \cdot (\boldsymbol{b} + \boldsymbol{c}) &= \boldsymbol{a} \cdot \boldsymbol{b} + \boldsymbol{a} \cdot \boldsymbol{c} \\
(\lambda \boldsymbol{a}) \cdot \boldsymbol{b} &= \lambda (\boldsymbol{a} \cdot \boldsymbol{b}) \\
\boldsymbol{a} \cdot (\lambda \boldsymbol{b}) &= \lambda (\boldsymbol{a} \cdot \boldsymbol{b})
\end{aligned}
$$

The inner product also satisfies commutativity, i.e.:

$$
\boldsymbol{a} \cdot \boldsymbol{b} = \boldsymbol{b} \cdot \boldsymbol{a}
$$

### Applications

Below we introduce some common applications of the inner product operation.

1.  Determining that two vectors are perpendicular:

    $$
    \boldsymbol{a} \perp \boldsymbol{b} \iff \boldsymbol{a} \cdot \boldsymbol{b} = 0
    $$

    That is, the inner product of two mutually perpendicular vectors is $0$; the inner product of a vector with the zero vector is $0$. If one uses the inner product being zero as the definition of perpendicularity, then one can conclude that the zero vector is perpendicular to any vector.

2.  Determining that two vectors are collinear:

    $$
    \exists\lambda \in \mathbf{R} (\boldsymbol{a} = \lambda \boldsymbol{b}) \iff |\boldsymbol{a} \cdot \boldsymbol{b}| = |\boldsymbol{a}| |\boldsymbol{b}|
    $$

3.  Computing the modulus of a vector:

    $$
    |\boldsymbol a| = \sqrt{\boldsymbol{a} \cdot \boldsymbol{a}}
    $$

4.  Computing the angle between two vectors:

    $$
    \theta = \arccos \frac{\boldsymbol{a} \cdot \boldsymbol{b}}{|\boldsymbol a| |\boldsymbol b|}
    $$

## Second- and third-order determinants

Second- and third-order determinants can be specially defined as relatively simple cases of the determinant. In the last part of calculus, the field theory part, Green's formula uses the second-order determinant, Gauss's formula uses the dot product, and Stokes's formula uses the third-order determinant.

A second-order determinant can be regarded as a four-variable function, defined as:

$$
\begin{vmatrix}
    a & b \\
    c & d
\end{vmatrix}=ad-bc
$$

A third-order determinant can be regarded as a nine-variable function, defined as:

$$
\begin{vmatrix}
    a & b & c \\
    d & e & f \\
    g & h & i
\end{vmatrix}=aei+dhc+gbf-ahf-dbi-gec
$$

A special memory method is to use the "diagonal rule"; the diagonal rule only applies to second- and third-order determinants.

Special note: A fourth-order determinant has 24 terms after expansion, and the sign of the anti-diagonal term is positive. If one forcibly applies the "diagonal rule" of the third-order determinant, not only is the number of terms insufficient, but the sign of the anti-diagonal term is also incorrect, so the "diagonal rule" of the third-order determinant does not apply to determinants of higher order, and determinants of higher order are also not suitable for computation by direct expansion.

## Outer product

The outer product is an **operation unique to three-dimensional vectors**.

In physics, three-dimensional vectors are by default vectors related to spatial position and are uniformly denoted in bold. However, four-dimensional vectors related to relativity in physics are not denoted in bold, but use special notation and subscripts.

In linear algebra, all vectors are denoted in bold, and because it is troublesome, and most operations in linear algebra are operations of vectors and matrices, it is hard to cause ambiguity, so when writing by hand the vector notation can be omitted.

### Definition

The outer product has different but equivalent ways of definition; below we introduce some of them.

#### Geometric definition

In three-dimensional Euclidean space $\mathbf{R}^3$, the outer product of vectors $\boldsymbol{a}, \boldsymbol{b}$ is defined as a vector, denoted $\boldsymbol{a} \times \boldsymbol{b}$, whose modulus and direction are defined as follows:

1.  $|\boldsymbol{a} \times \boldsymbol{b}| = |\boldsymbol{a}| |\boldsymbol{b}| \sin \langle \boldsymbol{a}, \boldsymbol{b} \rangle$;
2.  $\boldsymbol{a} \times \boldsymbol{b}$ is perpendicular to both $\boldsymbol{a}, \boldsymbol{b}$, and the directions of $\boldsymbol{a}, \boldsymbol{b}, \boldsymbol{a} \times \boldsymbol{b}$ conform to the right-hand rule.

Noting the modulus of the outer product, and associating with the triangle area formula $S=\frac{1}{2}ab\sin C$, one can find that the geometric meaning of the outer product is: **$|\boldsymbol{a} \times \boldsymbol{b}|$ is the area of the parallelogram with $\boldsymbol{a}, \boldsymbol{b}$ as adjacent sides**.

#### Algebraic definition

In three-dimensional Euclidean space $\mathbf{R}^3$, the outer product of vectors $\boldsymbol{a} = (x_1, y_1, z_1), \boldsymbol{b} = (x_2, y_2, z_2)$ is defined as a vector $\boldsymbol{c}$, denoted $\boldsymbol{c} = \boldsymbol{a} \times \boldsymbol{b}$, whose result can be represented using a third-order determinant:

$$
\begin{vmatrix}
    \boldsymbol{i} & \boldsymbol{j} & \boldsymbol{k} \\
    x_1 & y_1 & z_1  \\
    x_2 & y_2 & z_2
\end{vmatrix}
$$

where $\boldsymbol{i}, \boldsymbol{j}, \boldsymbol{k}$ denote the unit vectors pointing in the directions of the coordinate axes $x, y, z$, written at the corresponding coordinate positions. Expanding gives

$$
\begin{aligned}
\boldsymbol{c} &= \boldsymbol{a} \times \boldsymbol{b} \\
&= (y_1z_2 - y_2z_1)\boldsymbol{i} + (z_1x_2 - z_2x_1)\boldsymbol{j} + (x_1y_2 - x_2y_1)\boldsymbol{k} \\
&= (y_1z_2 - y_2z_1, z_1x_2 - z_2x_1, x_1y_2 - x_2y_1)
\end{aligned}
$$

### Properties

1.  The outer product is a bilinear operation that is linear in each of the two vectors separately. Specifically, the outer product satisfies:

    $$
    \begin{aligned}
    (\boldsymbol{a} + \boldsymbol{b}) \times \boldsymbol{c} &= \boldsymbol{a} \times \boldsymbol{c} + \boldsymbol{b} \times \boldsymbol{c} \\
    \boldsymbol{a} \times (\boldsymbol{b} + \boldsymbol{c}) &= \boldsymbol{a} \times \boldsymbol{b} + \boldsymbol{a} \times \boldsymbol{c} \\
    (\lambda \boldsymbol{a}) \times \boldsymbol{b} &= \lambda (\boldsymbol{a} \times \boldsymbol{b}) \\
    \boldsymbol{a} \times (\lambda \boldsymbol{b}) &= \lambda (\boldsymbol{a} \times \boldsymbol{b})
    \end{aligned}
    $$

    The first two rows of properties can also be called the distributive law, i.e. the outer product satisfies the multiplicative distributive law over vector addition.

2.  The outer product satisfies anti-commutativity, i.e.:

    $$
    \boldsymbol a \times \boldsymbol b=-\boldsymbol b \times \boldsymbol a
    $$

3.  According to the geometric definitions of the inner product and outer product above:

    $$
    \begin{aligned}
    |\boldsymbol a \times \boldsymbol b| &= |\boldsymbol a| |\boldsymbol b| \sin \langle \boldsymbol a, \boldsymbol b \rangle \\
    \boldsymbol a \cdot \boldsymbol b &= |\boldsymbol a| |\boldsymbol b| \cos \theta \\
    &= |\boldsymbol a| |\boldsymbol b| \cos \langle \boldsymbol a, \boldsymbol b\rangle
    \end{aligned}
    $$

    one can write the identity:

    $$
    (\boldsymbol a\times \boldsymbol b) \cdot (\boldsymbol a\times \boldsymbol b) = |\boldsymbol a|^2 |\boldsymbol b|^2-{(\boldsymbol a \cdot \boldsymbol b)}^2
    $$

4.  The outer product satisfies the Jacobi identity:

    $$
    \boldsymbol a \times (\boldsymbol b \times \boldsymbol c) + \boldsymbol b \times (\boldsymbol c \times \boldsymbol a) + \boldsymbol c \times (\boldsymbol a \times \boldsymbol b) = \boldsymbol 0
    $$

### Applications

Below we introduce some common applications of the outer product operation.

1.  Determining whether two vectors are collinear:

    $$
    \exists\lambda \in \mathbf{R} (\boldsymbol{a} = \lambda \boldsymbol{b}) \iff \boldsymbol{a} \times \boldsymbol{b} = \boldsymbol{0}
    $$

    That is, the outer product of two collinear three-dimensional vectors is $\boldsymbol 0$; the outer product of a three-dimensional vector with itself is $\boldsymbol 0$; the outer product of a three-dimensional vector with the zero vector is $\boldsymbol 0$. If one uses the outer product being zero as the definition of two vectors being collinear, then one can conclude that the zero vector is collinear with any vector.

2.  Computing the area of the parallelogram spanned by two vectors:

    $$
    S \langle \boldsymbol a, \boldsymbol b \rangle = |\boldsymbol a \times \boldsymbol b|
    $$

#### The case of two-dimensional vectors

For two-dimensional vectors, one cannot compute the outer product, but one can still compute the area of the parallelogram spanned by two vectors:

Denote $\boldsymbol{a} = (m, n), \boldsymbol{b} = (p, q)$; extend the plane rectangular coordinate system to a space rectangular coordinate system, with the original plane located on the $xOy$ plane of the new coordinate system, and the original coordinates $(m, n)$ and $(p, q)$ becoming $(m, n, 0)$ and $(p, q, 0)$.

Then the outer product of the two vectors is $(0, 0, mq - np)$, so the area of the parallelogram is $|mq - np|$, which can be regarded as the absolute value of the result of the second-order determinant operation.

In this case, according to the right-hand rule and the sign of the $z$-coordinate, one can infer the direction of $\boldsymbol b$ relative to $\boldsymbol a$: if it is in the counterclockwise direction then the $z$-coordinate is positive, and conversely negative, abbreviated as **clockwise negative, counterclockwise positive**.

## Scalar triple product

Like the outer product, the scalar triple product of vectors is an **operation unique to three-dimensional vectors**.

### Definition

Let $\boldsymbol a, \boldsymbol b, \boldsymbol c$ be three vectors in three-dimensional space; then $(\boldsymbol a \times \boldsymbol b) \cdot \boldsymbol c$ is called the scalar triple product of the three vectors $\boldsymbol a, \boldsymbol b, \boldsymbol c$, denoted $[\boldsymbol a \boldsymbol b \boldsymbol c]$ or $(\boldsymbol a, \boldsymbol b, \boldsymbol c)$ or $(\boldsymbol a \boldsymbol b \boldsymbol c)$ or $\det(\boldsymbol a, \boldsymbol b, \boldsymbol c)$. The geometric meaning of the absolute value of the scalar triple product $|(\boldsymbol a \times \boldsymbol b) \cdot \boldsymbol c|$ represents the volume of the parallelepiped with $\boldsymbol a, \boldsymbol b, \boldsymbol c$ as edges.

The scalar triple product of vectors can be represented using a third-order determinant:

$$
\begin{aligned}
(\boldsymbol a \times \boldsymbol b) \cdot \boldsymbol c &= \det(\boldsymbol a, \boldsymbol b, \boldsymbol c) \\
&= \begin{vmatrix}
    a_x & b_x & c_x \\
    a_y & b_y & c_y \\
    a_z & b_z & c_z
\end{vmatrix} \\
&= a_x b_y c_z + a_y b_z c_x + a_z b_x c_y - a_z b_y c_x -a _y b_x c_z - a_x b_z c_y
\end{aligned}
$$

### Properties

1.  The scalar triple product is linear in each of the three vectors separately; specifically:

    $$
    \begin{aligned}
    \det(\lambda\boldsymbol{u} + \mu\boldsymbol{v}, \boldsymbol{b}, \boldsymbol{c}) &= \lambda\det(\boldsymbol{u}, \boldsymbol{b}, \boldsymbol{c}) + \mu\det(\boldsymbol{v}, \boldsymbol{b}, \boldsymbol{c}) \\
    \det(\boldsymbol{a}, \lambda\boldsymbol{u} + \mu\boldsymbol{v}, \boldsymbol{c}) &= \lambda\det(\boldsymbol{a}, \boldsymbol{u}, \boldsymbol{c}) + \mu\det(\boldsymbol{a}, \boldsymbol{v}, \boldsymbol{c}) \\
    \det(\boldsymbol{a}, \boldsymbol{b}, \lambda\boldsymbol{u} + \mu\boldsymbol{v}) &= \lambda\det(\boldsymbol{a}, \boldsymbol{b}, \boldsymbol{u}) + \mu\det(\boldsymbol{a}, \boldsymbol{b}, \boldsymbol{v})
    \end{aligned}
    $$

2.  The scalar triple product has antisymmetry; swapping the positions of two vectors turns the scalar triple product into its negative, so:

    $$
    \det(\boldsymbol a, \boldsymbol b, \boldsymbol c) = \det(\boldsymbol b, \boldsymbol c, \boldsymbol a) = \det(\boldsymbol c, \boldsymbol a, \boldsymbol b) = -\det(\boldsymbol b, \boldsymbol a, \boldsymbol c) = -\det(\boldsymbol a, \boldsymbol c, \boldsymbol b)= -\det(\boldsymbol c, \boldsymbol b, \boldsymbol a)
    $$

    From this one can also obtain the following relationship between the inner product and outer product:

    $$
    (\boldsymbol a \times \boldsymbol b) \cdot \boldsymbol c = \boldsymbol a \cdot (\boldsymbol b \times \boldsymbol c)
    $$

### Applications

The scalar triple product of vectors has the following common applications.

1.  Computing the volume of a tetrahedron $ABCD$:

    $$
    V=\frac{1}{6}\left|\det(\overrightarrow{AB}, \overrightarrow{AC}, \overrightarrow{AD})\right|
    $$

2.  Determining whether $\boldsymbol a, \boldsymbol b, \boldsymbol c$ are coplanar;

    The necessary and sufficient condition for three three-dimensional vectors $\boldsymbol a, \boldsymbol b, \boldsymbol c$ to be coplanar is $\det(\boldsymbol a, \boldsymbol b, \boldsymbol c)=0$.

3.  Determining the chirality of the coordinate system formed by $\boldsymbol a, \boldsymbol b, \boldsymbol c$;

    Whether the sign of the scalar triple product $\det(\boldsymbol a, \boldsymbol b, \boldsymbol c)$ is positive or negative depends on whether the angle formed by $\boldsymbol a \times \boldsymbol b$ and $\boldsymbol c$ is acute or obtuse, i.e. whether it points to the same side or the opposite side of the plane spanned by $\boldsymbol a$ and $\boldsymbol b$, which is equivalent to whether the three vectors $\boldsymbol a, \boldsymbol b, \boldsymbol c$ in order form a right-handed or left-handed system. Specifically:

    -   $\det(\boldsymbol a, \boldsymbol b, \boldsymbol c) < 0$ is equivalent to $\boldsymbol a, \boldsymbol b, \boldsymbol c$ in order forming a left-handed system;
    -   $\det(\boldsymbol a, \boldsymbol b, \boldsymbol c) > 0$ is equivalent to $\boldsymbol a, \boldsymbol b, \boldsymbol c$ in order forming a right-handed system.

## Vector triple product

The scalar triple product of three-dimensional vectors is a mixture of the inner product and outer product, and has cyclic symmetry. The outer product of a three-dimensional vector and a three-dimensional vector is still a three-dimensional vector, so is there a related conclusion for the outer product of outer products?

First prove a lemma.

$$
(\boldsymbol a \times \boldsymbol b)\times \boldsymbol a = (\boldsymbol a \cdot \boldsymbol a) \boldsymbol b - (\boldsymbol a \cdot \boldsymbol b) \boldsymbol a
$$

Proof: By the right-hand rule, $\boldsymbol a \times \boldsymbol b$ is perpendicular to both $\boldsymbol a$ and $\boldsymbol b$; the left side of the equation to be proved is perpendicular to $\boldsymbol a \times \boldsymbol b$, so the left side of the equation to be proved is coplanar with $\boldsymbol a$ and $\boldsymbol b$.

Therefore one can assume:

$$
(\boldsymbol a \times \boldsymbol b)\times \boldsymbol a = \lambda \boldsymbol a + \mu \boldsymbol b
$$

According to the related conclusions of the scalar triple product, taking the inner product of both sides of the above with $\boldsymbol a$ and $\boldsymbol b$ respectively:

$$
\begin{aligned}
\lambda (\boldsymbol a \cdot \boldsymbol a)+\mu (\boldsymbol a \cdot \boldsymbol b) &= 0 \\
\lambda (\boldsymbol a \cdot \boldsymbol b) + \mu (\boldsymbol b \cdot \boldsymbol b) &= \det(\boldsymbol b, \boldsymbol a \times \boldsymbol b, \boldsymbol a) \\
&= (\boldsymbol a \times \boldsymbol b) \cdot (\boldsymbol a \times \boldsymbol b)
\end{aligned}
$$

From the identity deduced earlier:

$$
(\boldsymbol a \times \boldsymbol b) \cdot (\boldsymbol a \times \boldsymbol b) = |\boldsymbol a|^2|\boldsymbol b|^2-(\boldsymbol a \cdot \boldsymbol b)^2
$$

one can solve:

$$
\begin{aligned}
\lambda &= -\boldsymbol a \cdot \boldsymbol b \\
\mu &= \boldsymbol a \cdot \boldsymbol a
\end{aligned}
$$

Q.E.D.

In the above proof it is mentioned that the vector obtained by cross-multiplying $\boldsymbol a \times \boldsymbol b$ with any vector is coplanar with $\boldsymbol a$ and $\boldsymbol b$. Next we prove the conclusion of the **vector triple product**:

$$
(\boldsymbol a\times \boldsymbol b)\times \boldsymbol c=(\boldsymbol a \cdot \boldsymbol c)\boldsymbol b - (\boldsymbol b \cdot \boldsymbol c)\boldsymbol a
$$

The above coplanarity helps in memorizing the conclusion of the vector triple product. One can see that the lemma above is a special case of the vector triple product.

Proof: Here we only need to consider the case where all three vectors are nonzero and not collinear; the other special cases are obvious.

The three-dimensional vectors $\boldsymbol a$, $\boldsymbol b$, and $\boldsymbol a \times \boldsymbol b$ are not coplanar, so one can assume:

$$
\boldsymbol c = \alpha \boldsymbol a + \beta \boldsymbol b + \gamma(\boldsymbol a \times \boldsymbol b)
$$

So:

$$
\begin{aligned}
(\boldsymbol a \times \boldsymbol b) \times \boldsymbol c &= (\boldsymbol a \times \boldsymbol b) \times (\alpha \boldsymbol a + \beta \boldsymbol b + \gamma(\boldsymbol a \times \boldsymbol b)) \\
&= \alpha(\boldsymbol a \times \boldsymbol b) \times \boldsymbol a + \beta(\boldsymbol a \times \boldsymbol b) \times \boldsymbol b
\end{aligned}
$$

According to the lemma above:

$$
\begin{aligned}
(\boldsymbol a \times \boldsymbol b) \times \boldsymbol a &=(\boldsymbol a \cdot \boldsymbol a) \boldsymbol b - (\boldsymbol a \cdot \boldsymbol b) \boldsymbol a \\
(\boldsymbol a \times \boldsymbol b) \times \boldsymbol b
&= -(\boldsymbol b \times \boldsymbol a) \times \boldsymbol b \\
&= -(\boldsymbol b \cdot \boldsymbol b)\boldsymbol a+(\boldsymbol a \cdot \boldsymbol b) \boldsymbol b
\end{aligned}
$$

Therefore:

$$
\begin{aligned}
(\boldsymbol a \times \boldsymbol b) \times \boldsymbol c &= \alpha((\boldsymbol a \cdot \boldsymbol a)\boldsymbol b - (\boldsymbol a \cdot \boldsymbol b)\boldsymbol a) + \beta((\boldsymbol a \cdot \boldsymbol b)\boldsymbol b - (\boldsymbol b \cdot \boldsymbol b)\boldsymbol a) \\
&=(\alpha(-\boldsymbol a \cdot \boldsymbol b) + \beta(-\boldsymbol b \cdot \boldsymbol b))\boldsymbol a + (\alpha \boldsymbol a \cdot \boldsymbol a + \beta \boldsymbol a \cdot \boldsymbol b)\boldsymbol b \\
&= (\boldsymbol a \cdot \boldsymbol c) \boldsymbol b - (\boldsymbol b \cdot \boldsymbol c) \boldsymbol a
\end{aligned}
$$

Q.E.D.

According to the anti-commutativity of the outer product, one can obtain the two formulas of the vector triple product:

$$
\begin{aligned}
(\boldsymbol a\times \boldsymbol b)\times \boldsymbol c &=(\boldsymbol a \cdot \boldsymbol c)\boldsymbol b - (\boldsymbol b \cdot \boldsymbol c)\boldsymbol a \\
\boldsymbol a \times(\boldsymbol b \times \boldsymbol c) &= (\boldsymbol a \cdot \boldsymbol c)\boldsymbol b - (\boldsymbol a \cdot \boldsymbol b)\boldsymbol c
\end{aligned}
$$

One can see that the vector triple product has strict requirements on the order of operations.

With the help of the scalar triple product and the vector triple product, one can also prove Lagrange's identity.

$$
(\boldsymbol a \times \boldsymbol b) \cdot (\boldsymbol c \times \boldsymbol d)=(\boldsymbol a \cdot \boldsymbol c)(\boldsymbol b \cdot \boldsymbol d)-(\boldsymbol a \cdot \boldsymbol d)(\boldsymbol b \cdot \boldsymbol c)
$$

Proof:

$$
\begin{aligned}
(\boldsymbol a \times \boldsymbol b) \cdot (\boldsymbol c \times \boldsymbol d) &= \det(\boldsymbol c, \boldsymbol d, \boldsymbol a \times \boldsymbol b) \\
&= \det(\boldsymbol a \times \boldsymbol b, \boldsymbol c, \boldsymbol d) \\
&= ((\boldsymbol a \times \boldsymbol b)\times \boldsymbol c)\cdot \boldsymbol d \\
&= (\boldsymbol b(\boldsymbol a \cdot \boldsymbol c)- \boldsymbol a(\boldsymbol b \cdot \boldsymbol c))\cdot \boldsymbol d \\
&= (\boldsymbol a \cdot \boldsymbol c)(\boldsymbol b \cdot \boldsymbol d) - (\boldsymbol a \cdot \boldsymbol d)(\boldsymbol b \cdot \boldsymbol c)
\end{aligned}
$$

One can see that the earlier identity

$$
(\boldsymbol a \times \boldsymbol b) \cdot (\boldsymbol a \times \boldsymbol b) = |\boldsymbol a|^2|\boldsymbol b|^2 - (\boldsymbol a \cdot \boldsymbol b)^2
$$

is a special case of Lagrange's identity.
