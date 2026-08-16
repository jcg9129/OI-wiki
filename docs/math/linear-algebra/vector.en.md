Before this article, let us specially explain a translation-related issue. For historical reasons, the mathematics discipline and the physics discipline translate the word "vector" differently.

In the physics discipline, it is generally translated as "矢量" (shǐliàng), and is contrasted with the word "标量" (scalar). In the mathematics discipline, it is generally translated as "向量" (xiàngliàng). Other such translation differences include "本征" vs. "特征" (eigen), "幺正" vs. "酉" (unitary), and so on.

**OI Wiki** is mainly oriented toward engineering-related disciplines such as computer science, which are closer to the mathematics discipline, so it adopts the term "向量".

## Definition and related concepts

**Vector**: a quantity that has both magnitude and direction is called a vector. The vectors studied in mathematics are **free vectors**, i.e. vectors whose starting point and endpoint can be translated arbitrarily as long as their magnitude and direction are not changed. Denoted $\vec a$ or $\boldsymbol{a}$.

**Directed segment**: a segment with a direction is called a directed segment. A directed segment has three elements: **starting point, direction, length**; knowing the three elements, the endpoint is uniquely determined. A directed segment is generally used to represent a vector.

**Modulus of a vector**: the length of the directed segment $\overrightarrow{AB}$ is called the modulus of the vector, i.e. the magnitude of this vector. Denoted $|\overrightarrow{AB}|$ or $|\boldsymbol{a}|$.

**Zero vector**: a vector with modulus $0$. The direction of the zero vector is arbitrary. Denoted $\vec 0$ or $\boldsymbol{0}$.

**Unit vector**: a vector with modulus $1$ is called the unit vector in that direction. Generally denoted $\vec e$ or $\boldsymbol{e}$.

**Parallel vectors**: two **nonzero** vectors with the same or opposite directions. Denoted $\boldsymbol a\parallel \boldsymbol b$. For multiple mutually parallel vectors, one can draw any line parallel to these vectors, and then any group of parallel vectors can be translated to the same line, so parallel vectors are also called **collinear vectors**.

**Equal vectors**: vectors with equal moduli and the same direction.

**Opposite vectors**: vectors with equal moduli and opposite directions.

**Angle between vectors**: given two nonzero vectors $\boldsymbol a,\boldsymbol b$, draw $\overrightarrow{OA}=\boldsymbol a,\overrightarrow{OB}=\boldsymbol b$; then $\theta=\angle AOB$ is the angle between the vector $\boldsymbol a$ and the vector $\boldsymbol b$. Denoted $\langle \boldsymbol a,\boldsymbol b\rangle$. Obviously, when $\theta=0$ the two vectors are in the same direction, when $\theta=\pi$ the two vectors are in opposite directions, and when $\theta=\frac{\pi}{2}$ the two vectors are perpendicular, denoted $\boldsymbol a\perp \boldsymbol b$; and it is stipulated that $\theta \in [0,\pi]$.

Note that plane vectors have directionality, and two vectors cannot be compared in magnitude (but the moduli of two vectors can be compared). However, two vectors can be equal.

## Linear operations of vectors

### Addition and subtraction of vectors

After defining a kind of quantity, one hopes to give it operations. The operations of vectors can be analogous to the operations of numbers, and one can also study the operations of vectors from the perspective of physics.

By analogy with the concept of displacement in physics, if a person walks from $A$ through $B$ to $C$, then the displacement they undergo is $\overrightarrow{AB}+\overrightarrow{BC}$, which is in fact equivalent to this person walking directly from $A$ to $C$, i.e. $\overrightarrow{AB}+\overrightarrow{BC}=\overrightarrow{AC}$.

Note that the rule for the composition of forces—the parallelogram rule—can likewise be regarded as the addition of some vectors.

Let us organize the rules of vector addition:

1.  **Triangle rule of vector addition**: if the vectors to be summed are connected head to tail in sequence, then the sum of these vectors points from the starting point of the first vector to the endpoint of the last vector;
2.  **Parallelogram rule of vector addition**: if the two vectors to be summed **share a starting point**, then their sum vector is the diagonal of the parallelogram with these two vectors as adjacent sides, with the starting point being the common starting point of the two vectors, and the direction along the diagonal of the parallelogram.

In this way, vector addition acquires a geometric meaning. And one can verify that vector addition satisfies **commutativity and associativity**.

Because the subtraction of real numbers can be written in the form of adding the opposite number, consider writing this way when doing subtraction of vectors as well. That is: $\boldsymbol a-\boldsymbol b=\boldsymbol a+(-\boldsymbol b)$.

In this way, considering vectors that share a starting point, drawing their difference according to the parallelogram rule, after translation one can find that **the "difference vector of vectors sharing a starting point" is the directed segment from the "subtrahend vector" pointing to the "minuend vector"**. This is also the geometric meaning of vector subtraction.

Sometimes there are two points $A,B$, and one wants to know $\overrightarrow{AB}$; one can use the subtraction operation $\overrightarrow{AB}=\overrightarrow{OB}-\overrightarrow{OA}$ to obtain it.

### Scalar multiplication of vectors

The "product of a real number $\lambda$ and a vector $\boldsymbol a$" is stipulated to be a vector; this operation is the **scalar multiplication operation** of vectors, denoted $\lambda \boldsymbol a$, and its length and direction are stipulated as follows:

1.  $|\lambda \boldsymbol a|=|\lambda||\boldsymbol a|$;
2.  When $\lambda >0$, $\lambda\boldsymbol a$ is in the same direction as $\boldsymbol a$; when $\lambda =0$, $\lambda \boldsymbol a=\boldsymbol 0$; when $\lambda<0$, $\lambda \boldsymbol a$ is in the opposite direction to $\boldsymbol a$.

According to the definition of scalar multiplication, one can verify the following operation laws:

$$
\begin{aligned}
\lambda(\mu \boldsymbol a)&=(\lambda \mu)\boldsymbol a\\
(\lambda+\mu)\boldsymbol a&=\lambda \boldsymbol a+\mu \boldsymbol a\\
\lambda(\boldsymbol a+\boldsymbol b)&=\lambda \boldsymbol a+\lambda \boldsymbol b
\end{aligned}
$$

In particular:

$$
\begin{gathered}
(-\lambda)\boldsymbol a=-(\lambda \boldsymbol a)=-\lambda(\boldsymbol a)\\
\lambda(\boldsymbol a-\boldsymbol b)=\lambda \boldsymbol a-\lambda \boldsymbol b
\end{gathered}
$$

### Determining that two vectors are collinear

Two **nonzero** vectors $\boldsymbol a$ and $\boldsymbol b$ are collinear $\iff$ there is a unique real number $\lambda$ such that $\boldsymbol b=\lambda \boldsymbol a$.

Proof: By the definition of scalar multiplication, for a **nonzero** vector $\boldsymbol a$, if there exists a real number $\lambda$ such that $\boldsymbol b=\lambda \boldsymbol a$, then $\boldsymbol a \parallel \boldsymbol b$.

Conversely, if $\boldsymbol a\parallel \boldsymbol b$, $\boldsymbol a \not = \boldsymbol 0$, and $|\boldsymbol b|=\mu |\boldsymbol a|$, then when $\boldsymbol a$ and $\boldsymbol b$ are in the same direction, $\boldsymbol b=\mu \boldsymbol a$, and when they are in opposite directions $\boldsymbol b=-\mu \boldsymbol a$.

Finally, the addition, subtraction, and scalar multiplication of vectors are collectively called the linear operations of vectors.

## The fundamental theorem of plane vectors and coordinate representation

### Fundamental theorem of plane vectors

Statement of the theorem: If two vectors $\boldsymbol{e_1},\boldsymbol{e_2}$ are not collinear, then there exists a unique real pair $(x,y)$ such that any vector $\boldsymbol p$ coplanar with $\boldsymbol{e_1},\boldsymbol{e_2}$ satisfies $\mathbf p=x\boldsymbol{e_1}+y\boldsymbol{e_2}$.

There are so many plane vectors; how can one use as few quantities as possible to represent all plane vectors?

Using only one vector to represent all vectors is obviously impossible; at most one can represent the vectors on some line.

Adding one more vector, representing with two **non-collinear** vectors (two collinear vectors can here be regarded as the same vector), one can decompose any plane vector onto the directions of these two vectors.

Two non-collinear vectors in the same plane are called a **basis**. If the basis vectors are mutually perpendicular, then the decomposition is an **orthogonal decomposition** of the vector.

### Coordinate representation of plane vectors

If we take unit vectors $i,j$ with the same directions as the horizontal and vertical axes as a basis, then by the fundamental theorem of plane vectors, all vectors in the plane correspond one-to-one with ordered real pairs $(x,y)$.

And ordered real pairs $(x,y)$ correspond one-to-one with points on the plane rectangular coordinate system, so drawing $\overrightarrow{OP}=\boldsymbol p$, the endpoint $P(x,y)$ is also uniquely determined. Since the objects of study are free vectors, one can freely translate the starting point, and in this way, in the plane rectangular coordinate system, every vector can be uniquely represented by an ordered real pair.

## Coordinate operations of plane vectors

### Linear operations of plane vectors

From the linear operations of plane vectors one can derive their coordinate operations; the main method is to express all coordinates in terms of the basis, then combine them using the operation laws, and afterward express the coordinate form of the operation result.

If two vectors $\boldsymbol a=(m,n)$, $\boldsymbol b=(p,q)$, then:

$$
\begin{aligned}
\boldsymbol a+\boldsymbol b&=(m+p,n+q)\\
\boldsymbol a-\boldsymbol b&=(m-p,n-q)\\
k\boldsymbol a&=(km,kn)
\end{aligned}
$$

### Finding the coordinate representation of a vector

Given two points $A(a,b),B(c,d)$, it is easy to prove $\overrightarrow{AB}=(c-a,d-b)$.

### Translating a point

Sometimes one needs to translate a point $P$ by some unit length along a certain direction; combining the direction and distance to translate into a vector, one uses the triangle rule of vector addition to add this vector to $\overrightarrow{OP}$, and the endpoint of the resulting vector is the point after translation.

### Determining that three points are collinear

If three points $A,B,C$ are collinear, then $\overrightarrow{OB}=\lambda \overrightarrow{OA}+(1-\lambda)\overrightarrow{OC}$.

### Extension of determining that three points are collinear

In triangle $ABC$, if $D$ is the $n$-division point of $BC$ ($n\ BD=k\ DC$), then: $\overrightarrow{AD}=\frac{n}{k+n}\overrightarrow{AB}+\frac{k}{k+n}\overrightarrow{AC}$

## Extension in three-dimensional space (solid geometry / space vectors)

In space, everything described in the above part holds. Furthermore:

### Fundamental theorem of space vectors

Statement of the theorem: If three vectors $\boldsymbol{e_1},\boldsymbol{e_2},\boldsymbol{e_3}$ are not coplanar, then there exists a unique real triple $(x,y,z)$ such that any vector $\boldsymbol p$ in space satisfies $\mathbf p=x\boldsymbol{e_1}+y\boldsymbol{e_2}+z\boldsymbol{e_3}$.
According to the fundamental theorem of space vectors, we can likewise use three mutually perpendicular basis vectors $\boldsymbol{e_1},\boldsymbol{e_2},\boldsymbol{e_3}$ as an orthogonal basis, establish a **space rectangular coordinate system**, and use a triple $(x,y,z)$ as coordinates to represent a space vector.

### Fundamental theorem of coplanar vectors

If there exist two non-collinear vectors $\boldsymbol{x},\boldsymbol{y}$, then the necessary and sufficient condition for a vector $\boldsymbol{p}$ to be coplanar with $\boldsymbol{x},\boldsymbol{y}$ is that there exists a unique real pair $(a,b)$ such that $\boldsymbol{p}=a\boldsymbol{x}+b\boldsymbol{y}$.

### Direction vector

The direction of a line in space is represented by a nonzero vector parallel to that line, and this vector is called a direction vector of this line. The position of a line in space is **completely determined** by a point it passes through in space and one of its direction vectors.

Note that lines in a plane also have direction vectors.

For a line in **space**, its direction vector can be found as follows:

-   If there are $A(x_1,y_1,z_1),B(x_2,y_2,z_2)$, then a direction vector of the line containing $AB$ is $\boldsymbol{s}=(x_2-x_1,y_2-y_1,z_2-z_1)$.

-   If a plane **perpendicular** to the required line is known, and the general equation of this plane is $ax+by+cz+d=0$, then a direction vector of the line perpendicular to this plane is $\boldsymbol{s}=(a,b,c)$, and this direction vector is also **a normal vector** of this plane.

### Normal vector

For a face $ABCD$, its normal vector $\boldsymbol{n}$ is perpendicular to this face.

Computation method: take any two lines $\overrightarrow{AB},\overrightarrow{AD}$ in the face such that $\overrightarrow{AB} \cdot \boldsymbol{n}=\boldsymbol{0}$ and $\overrightarrow{AD} \cdot \boldsymbol{n}=\boldsymbol{0}$, and compute using the coordinate method.

## Vectors and matrices

In linear algebra, a linear transformation can be represented by a matrix. Let $T$ denote a linear transformation mapping $\mathbf R^n$ to $\mathbf R^m$, and $\mathbf x$ denote an $n$-dimensional column vector; then there exists an $m\times n$ matrix $A$ such that

$$
T(\mathbf x)=A\mathbf x.
$$

The matrix $A$ is called the transformation matrix of the linear transformation $T$. In algorithmic problems, in general the linear transformation is performed in the same dimension, so $A$ is a square matrix. In this way, the problem of a linear transformation of a vector can be transformed into a matrix multiplication problem.

Next we explore three transformations relatively common in competitions and their corresponding transformation matrices: scaling transformation (transformation matrix denoted $S$), rotation transformation (transformation matrix denoted $R$), and translation transformation (transformation matrix denoted $T$).

### Scaling transformation

For an $n$-dimensional column vector $\boldsymbol a$, scale each of its dimensions by factors of $v_1,v_2,\ldots,v_n$. It is easy to find that the transformation matrix $R$ of the scaling operation is the $n\times n$ diagonal matrix, i.e. $S=\operatorname{diag}\{v_1,v_2,\ldots,v_n\}$.

### Rotation transformation

The rotation of a vector is a relatively complex operation; we limit ourselves to discussing the two-dimensional and three-dimensional cases.

#### Rotating a vector about a point

For rotating a vector about a point, one generally means rotating the vector about the origin. For rotating a point about another point $P$, one can use a translation transformation to place point $P$ at the origin, perform the vector rotation, and then translate the coordinate system back to the original position. Let the transformation matrix of the translation operation be $T$ and the transformation matrix of the rotation-about-origin operation be $R$; then the transformation matrix of the whole process is $TRT^{-1}$. By the geometric meaning, $T^{-1}$ must exist.

For two-dimensional space, let $\boldsymbol a=(x,y)$, with inclination angle $\theta$ and length $l=\sqrt{x^2+y^2}$. Then $x=l\cos \theta,y=l\sin\theta$. Rotating it counterclockwise about the origin by an angle $\alpha$ gives the vector $\boldsymbol b=(l\cos(\theta+\alpha),l\sin(\theta+\alpha))$.

![](./images/vector-rotation.svg)

By trigonometric identity transformations,

$$
\boldsymbol{b}=(l(\cos\theta\cos\alpha-\sin\theta\sin\alpha),l(\sin\theta\cos\alpha+\cos\theta\sin\alpha))
$$

Simplifying,

$$
\boldsymbol b=(l\cos\theta\cos\alpha-l\sin\theta\sin\alpha,l\sin\theta\cos\alpha+l\cos\theta\sin\alpha)
$$

Substituting the above $x,y$ back gives

$$
\boldsymbol b=(x\cos\alpha-y\sin\alpha,y\cos\alpha+x\sin\alpha)
$$

Therefore, in two-dimensional space, the transformation matrix $R$ is

$$
R=
\begin{bmatrix}
\cos\alpha & -\sin\alpha\\
\sin\alpha & \cos\alpha
\end{bmatrix}.
$$

For three-dimensional space, the rotation of a vector requires two angular parameters, namely the zenith-angle rotation angle and the azimuth-angle rotation angle; one can use the [space spherical coordinate system](../coordinate.md#space-spherical-coordinate-system) to perform the rotation operation.

#### Rotating a vector about a line

For three-dimensional vectors, more common is rotating about a certain line. Likewise for convenience, this line passes through the origin. If the line does not pass through the origin, we can still translate the coordinate system to transform it.

Take the direction vector of the line $\boldsymbol u=(u_x,u_y,u_z)$, and suppose the three-dimensional vector is rotated counterclockwise about it by an angle $\theta$. Then the corresponding transformation matrix $R$ is[^note1]

$$
R=
\begin{bmatrix}
u_x^2 \left(1-\cos \theta\right) + \cos \theta & u_x u_y \left(1-\cos \theta\right) - u_z \sin \theta & u_x u_z \left(1-\cos \theta\right) + u_y \sin \theta \\ 
u_x u_y \left(1-\cos \theta\right) + u_z \sin \theta & u_y^2\left(1-\cos \theta\right) + \cos \theta & u_y u_z \left(1-\cos \theta\right) - u_x \sin \theta \\ 
u_x u_z \left(1-\cos \theta\right) - u_y \sin \theta & u_y u_z \left(1-\cos \theta\right) + u_x \sin \theta & u_z^2\left(1-\cos \theta\right) + \cos \theta
\end{bmatrix}.
$$

### Translation transformation

A translation transformation is not a linear transformation, but an affine transformation. But an affine transformation in $\mathbf R^n$ can still be represented by a linear transformation in $\mathbf R^{n+1}$.

Consider an $n$-dimensional vector $\boldsymbol a=(a_1,a_2, \ldots , a_n)$; now we want to translate it along the vector $\boldsymbol t=(t_1, t_2, \ldots , t_n)$. We add a dimension to the column vector $\boldsymbol a$ and set it to $1$, obtaining a new column vector $\boldsymbol a'=(a_1, a_2, \ldots , a_n, 1)$. Then the transformation matrix $T$ can be written as

$$
T=
\begin{bmatrix}
1 &   &        &   & t_1    \\
  & 1 &        &   & t_2    \\
  &   & \ddots &   & \vdots \\
  &   &        & 1 & t_n    \\
  &   &        &   & 1      \\
\end{bmatrix}.
$$

For other linear transformation matrices, by adding a column and a row to the matrix, filling everything except the bottom-right element (which is $1$) with $0$, through this method all linear transformation matrices can be converted into affine transformation matrices. For example, for two-dimensional vector rotation, the transformation matrix can become

$$
R'=
\begin{bmatrix}
\cos\alpha & -\sin\alpha & 0\\
\sin\alpha & \cos\alpha & 0\\
0 & 0 & 1
\end{bmatrix}.
$$

## A more rigorous definition of a vector

In the above, a vector was defined as a directed segment in space. But strictly speaking, a vector is more than a directed segment. To give a more rigorous definition of a vector, one first needs to define a [linear space](./vector-space.md); for the specific content, see the introduction on the [linear space](./vector-space.md) page.

[^note1]: See [Rotation matrix from axis and angle - Wikipedia](https://en.wikipedia.org/wiki/Rotation_matrix#Rotation_matrix_from_axis_and_angle)
