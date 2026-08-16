author: Ir1d, HeRaNO, Chrogeek, abc1763613206, mxdyzmx

## Definition of an angle

In primary or middle school one has learned the **static definition** of an angle: the figure formed by two rays with a common endpoint is called an angle.

But this definition limits the angle to $[0, 360^\circ]$, which brings certain difficulties to deeper study, and there are also other problems it cannot explain clearly, such as: what does rotating $720^\circ$ mean?

In high-school mathematics, the **dynamic definition** of an angle is discussed: the figure formed by a ray in a plane rotating about its endpoint from one position to another is called an angle.

The starting position is called the **initial side**, and the ending position is called the **terminal side**. And it is stipulated that:

-   an angle formed by rotating **counterclockwise** is called a **positive angle**, and its angular measure is positive;
-   an angle formed by rotating **clockwise** is called a **negative angle**, and its angular measure is negative;
-   an angle in which the terminal side has not rotated at all relative to the initial side is called a **zero angle**, and its angular measure is $0^\circ$.

This pushes the concept of an angle to **arbitrary angles**.

???+ note "Note"
    The initial and terminal sides of a zero angle coincide, but not all angles whose initial and terminal sides coincide are zero angles, such as angles that are multiples of $360^\circ$.

## Radian measure

In practical applications there is often conversion from angles to various parameters, and using radian measure to describe angles can reduce the use of coefficients. So next, we introduce **radian measure**:

The central angle subtended by an arc whose length equals the radius is called an angle of $1$ radian, denoted by the symbol $\text{rad}$, read as: radian.

According to the earlier stipulation, the radian measure of a positive angle is positive, that of a negative angle is negative, and that of a zero angle is $0$; if the arc subtended by the central angle $\alpha$ of a circle with radius $r$ has length $l$, then:

$$
|\alpha|=\dfrac{l}{r}
$$

Using this formula one can also write the formulas for arc length and sector area, which are omitted here.

Thus, the radian measure of a $360^\circ$ angle is $2\pi$; with this correspondence, one can convert between angular measure and radian measure:

$$
k \operatorname{rad} = \frac{\pi}{180^\circ} n^\circ
$$

Consider an angle, and rotate its terminal side one more full turn, or even multiple turns, with the initial side fixed; then the terminal side position is always the same. These angles are called angles with the same terminal side.

The set of angles with the same terminal side as the angle $\alpha$ is easily obtained, being $\{\varphi \mid \varphi = \alpha + 2k\pi, k \in \mathbf{Z}\}$.

This can be understood as: continually adding a full turn to the side of this angle keeps the terminal side position unchanged.

???+ note "The two mathematical constants $\pi$ and $\tau$"
    Currently there are some views in the Western mathematical community that the "true circumference ratio" should be $2\pi$, and this value is denoted by the Greek letter $\tau$. Supporters of the new circumference ratio choose to celebrate the "true" pi day on June 28.
    
    For example, under radian measure, a full angle is $2\pi$, and directly dividing $2\pi$ equally gives equal divisions of the full angle. As another example, the combination $2\pi$ appears frequently in complex analysis, and so on.
    
    To conform to the conventions established in various regions of China, **OI Wiki** uses the parameter $\pi$ to denote the circumference ratio.

???+ note "Conventional way of writing pi in programming"
    In C/C++, one generally takes $\pi$ to be `acos(-1)`, as only this value is the floating-point number closest to $\pi$. The $\pi$ written using `acos(-1)` or `4 * atan(1)` is $3.14159265358979310000$.
    
    Using other values, such as `acos(-1.0/2.0)`, `acos(1.0/2.0)`, `asin(1.0/2.0)`, etc., the $\pi$ written is $3.14159265358979360000$, which is then not the floating-point number closest to $\pi$.
    
    If you can memorize it, you can also directly write $3.1415926535897932$.

## Plane rectangular coordinate system

Two number lines in the same plane that are perpendicular to each other and have a common origin form a plane rectangular coordinate system (Rectangular Coordinates).

Usually, the two number lines are placed in the horizontal position and the vertical position respectively, taking the rightward and upward directions as the positive directions of the two number lines respectively. The horizontal number line is called the $x$-axis or horizontal axis, the vertical number line is called the $y$-axis or vertical axis, the $x$-axis and $y$-axis are collectively called the coordinate axes, and their common origin $O$ is called the origin of the plane rectangular coordinate system; a plane rectangular coordinate system with point $O$ as the origin is denoted the plane rectangular coordinate system $xOy$.

The $x$-axis and $y$-axis divide the coordinate plane into four quadrants; the upper-right part is called the first quadrant, and the other three parts are called the second, third, and fourth quadrants in counterclockwise order. The quadrants are bounded by the number lines; the points on the horizontal axis, the vertical axis, and the origin are not in any quadrant. In general, the $x$-axis and $y$-axis take the same unit length, but in special cases, they can also take different unit lengths.

### Describing positions in the plane rectangular coordinate system

In the plane rectangular coordinate system, for any point in the plane, there is a unique ordered pair of numbers (i.e. the coordinates of the point) corresponding to it; conversely, for any ordered pair of numbers, there is a unique point in the plane corresponding to it.

For any point $C$ in the plane, draw perpendiculars from point $C$ to the $x$-axis and $y$-axis respectively; the corresponding points $a, b$ of the feet of the perpendiculars on the $x$-axis and $y$-axis are called the horizontal coordinate (abscissa) and vertical coordinate (ordinate) of point $C$ respectively, and the ordered pair $(a, b)$ is called the rectangular coordinates of point $C$. A point in different quadrants or on the coordinate axes has different coordinates.

## Plane polar coordinate system

Consider a practical situation, such as navigation, saying "point $B$ is in the direction of $30^\circ$ east of north from point $A$, at a distance of $100$ meters", rather than "establish a plane rectangular coordinate system with $A$ as the origin, $B(50,50\sqrt 3)$".

Thus:

1.  Choose a fixed point $O$ in the plane, called the **pole**;
2.  Draw a ray $Ox$ from the pole, called the **polar axis**;
3.  Choose a unit length (usually $1$ in mathematical problems), an angular unit (usually radians) and its positive direction (usually counterclockwise);

then the **polar coordinate system** is established.

### Describing positions in the polar coordinate system

Let $A$ be a point in the plane.

-   The distance $|OA|$ between the pole $O$ and $A$ is called the **polar radius**, denoted $\rho$;
-   The angle $\angle xOA$ with the polar axis as the initial side and $OA$ as the terminal side is called the **polar angle**, denoted $\varphi$;

then the ordered pair $(\rho,\varphi)$ is the **polar coordinates** of $A$.

By the definition of angles with the same terminal side, $(\rho,\varphi)$ and $(\rho,\varphi + 2k\pi)\ (k\in \mathbf{Z})$ in fact represent the same point. In particular, the polar coordinates of the pole are $(0,\varphi)\ (\varphi \in \mathbf{R})$, so the polar-coordinate representation of a point in the plane has infinitely many forms.

If we stipulate $\rho \ge 0,0 \le \varphi < 2\pi$, then except for the pole, other points in the plane can be represented by a unique ordered pair $(\rho,\varphi)$, and the point represented by the polar coordinates $(\rho,\varphi)$ is uniquely determined.

### Mutual conversion between the plane rectangular coordinate system and the polar coordinate system

Of course, sometimes it is somewhat inconvenient to study figures in the polar coordinate system. To transfer to the rectangular coordinate system for study, there are conversion formulas. The rectangular coordinates $(x,y)$ of the point $A(\rho,\varphi)$ can be represented as follows:

$$
\begin{aligned}
x &= \rho \cos \varphi \\
y &= \rho \sin \varphi
\end{aligned}
$$

Further, we know:

$$
\begin{aligned}
\rho^2 &= x^2 + y^2\\
\tan \varphi &= \frac{y}{x}\ \ \ \ (x\not =0)
\end{aligned}
$$

So we have $\rho = \sqrt{x^2+y^2}$.

But $\tan\varphi$ with the same $\dfrac{y}{x}$ has two possible values of $\varphi$; in this case one also needs to determine the direction according to the values of $x, y$. Specifically, define the function:

$$
\operatorname{atan2}(y, x) = \begin{cases}
\arctan(\frac{y}{x}) & \text{if } x > 0 \\
\arctan(\frac{y}{x}) + \pi & \text{if } y \ge 0, x < 0 \\
\arctan(\frac{y}{x}) - \pi & \text{if } y < 0, x < 0 \\
\pi/2 & \text{if } y > 0, x = 0 \\
-\pi/2 & \text{if } y < 0, x = 0 \\
\text{any} & \text{if } y = 0, x = 0
\end{cases}
$$

then $\varphi = \operatorname{atan2}(y, x)$. Note that the range of the above function is $(-\pi, \pi]$.

In the `<math.h>` or `<cmath>` library of C/C++, [this function](https://en.cppreference.com/w/cpp/numeric/math/atan2) is defined; just call `atan2(y, x)`.

## Space rectangular coordinate system

Establish a space rectangular coordinate system using the following method:

1.  Choose a point $O$ in space;
2.  Through point $O$, draw three mutually perpendicular number lines $\overrightarrow{Ox}, \overrightarrow{Oy}, \overrightarrow{Oz}$, called the $x$-axis (horizontal axis), $y$-axis (vertical axis), and $z$-axis (upright axis) respectively, collectively called the coordinate axes; their positive directions conform to the right-hand rule, i.e. gripping the $z$-axis with the right hand, when the four fingers of the right hand turn from the positive direction of the $x$-axis by an angle toward the positive direction of the $y$-axis, the thumb points in the positive direction of the $z$-axis;
3.  Set the length unit on each axis, usually all set to $1$.

This forms a space rectangular coordinate system, called the space rectangular coordinate system $O-xyz$. The fixed point $O$ is called the origin of this coordinate system.

Any two coordinate axes determine a plane, so three mutually perpendicular planes can be determined, collectively called the coordinate planes. Among them, the coordinate plane determined by the $x$-axis and the $y$-axis is called the $xOy$ plane, and similarly there are the $yOz$ plane and the $zOx$ plane. The three coordinate planes divide space into eight parts, each part called an octant.

### Describing positions in the space rectangular coordinate system

After fixing the space rectangular coordinate system $O-xyz$, one can establish a one-to-one correspondence between points in space and triples.

Let point $M$ be a point in space; through point $M$, draw planes perpendicular to the $x$-axis, $y$-axis, and $z$-axis respectively. Let the intersection points of the three planes with the $x$-axis, $y$-axis, and $z$-axis be $P, Q, R$ in order; points $P, Q, R$ are called the projections of point $M$ on the $x$-axis, $y$-axis, and $z$-axis respectively. Let the coordinates of points $P, Q, R$ on the $x$-axis, $y$-axis, and $z$-axis be $x, y, z$ in order; then point $M$ determines a triple $(x, y, z)$.

Conversely, if a triple $(x, y, z)$ is given, one can take the point $P$ with coordinate $x$ on the $x$-axis, the point $Q$ with coordinate $y$ on the $y$-axis, and the point $R$ with coordinate $z$ on the $z$-axis, then draw through points $P, Q, R$ three planes perpendicular to the $x$-axis, $y$-axis, and $z$-axis respectively; they intersect at a point $M$ in space, and point $M$ is the point determined by the triple $(x, y, z)$.

In this way, a one-to-one correspondence is established between a point $M$ in space and a triple $(x, y, z)$. The triple $(x, y, z)$ is called the coordinates of point $M$, denoted $M(x, y, z)$, where $x$ is called the horizontal coordinate, $y$ the vertical coordinate, and $z$ the upright coordinate.

## Space cylindrical coordinate system

The space cylindrical coordinate system is a way of extending polar coordinates to three dimensions: starting from the polar coordinate system applied in planar work, then adding, through the pole $O$, a $z$-axis perpendicular to that plane, pointing upward.

To find the point described by the cylindrical coordinates $(\rho, \varphi, z)$, one can first handle $\rho$ and $\varphi$ in the polar coordinate system, then move "up" or "down" along the $z$-axis according to the $z$-coordinate.

### Mutual conversion between the cylindrical coordinate system and the space rectangular coordinate system

The value of $z$ is the same under the two coordinate systems.

For the mutual conversion between $(x,y)$ and $(\rho, \varphi)$, see [Mutual conversion between the plane rectangular coordinate system and the polar coordinate system](#mutual-conversion-between-the-plane-rectangular-coordinate-system-and-the-polar-coordinate-system) above.

## Space spherical coordinate system

Spherical coordinates can be determined by the following method:

1.  Stand at the origin, facing the direction of the horizontal polar axis; the direction of the vertical axis is from the feet toward the head;
2.  Raise the arm upward, pointing in the direction of the vertical polar axis;
3.  Rotate counterclockwise by an angle $\varphi$;
4.  Rotate the arm downward by an angle $\vartheta$, with the arm pointing in the direction specified by $\varphi$ and $\vartheta$;
5.  Displace a distance $r$ from the origin along that direction.

This reaches the point described by the spherical coordinates $(r,\vartheta,\varphi)$. Here $\vartheta$ is called the **zenith angle**, and $\varphi$ is called the **azimuth angle**.

???+ warning "Warning"
    For various reasons, some places use $\phi$ to denote the zenith angle and $\theta$ to denote the azimuth angle. Please be sure to note this when reading articles that involve the spherical coordinate system.
    
    At the same time, when writing an article, if the spherical coordinate system is used, it is recommended to declare clearly in advance which symbols are used to denote the zenith angle and the azimuth angle.

### Mutual conversion between the cylindrical coordinate system and the spherical coordinate system

The value of $\varphi$ is the same under the two coordinate systems.

From the cylindrical coordinate system to the spherical coordinate system:

$$
\begin{aligned}
r &= \sqrt{\rho^2 + z^2} \\
\vartheta &= \begin{cases}
\arctan\left(\frac{\rho}{z}\right) & \text{if }z > 0 \\
\pi/2 & \text{if }z = 0, \rho \not= 0 \\
\arctan\left(\frac{\rho}{z}\right) + \pi & \text{if }z < 0 \\
\end{cases}
\end{aligned}
$$

Note that for the point $(0,0,0)$ in the cylindrical coordinate system, the $\vartheta$ of its spherical coordinates is undefined.

From the spherical coordinate system to the cylindrical coordinate system:

$$
\begin{aligned}
\rho &= r \sin \vartheta \\
z &= r \cos \vartheta
\end{aligned}
$$

### Mutual conversion between the space rectangular coordinate system and the spherical coordinate system

One can use, in combination, [Mutual conversion between the plane rectangular coordinate system and the polar coordinate system](#mutual-conversion-between-the-plane-rectangular-coordinate-system-and-the-polar-coordinate-system) above and [Mutual conversion between the cylindrical coordinate system and the spherical coordinate system](#mutual-conversion-between-the-cylindrical-coordinate-system-and-the-spherical-coordinate-system) above, or directly use the following formulas:

From the space rectangular coordinate system to the spherical coordinate system:

$$
\begin{aligned}
r &= \sqrt{x^2 + y^2 + z^2} \\
\vartheta &= \arccos\left(\frac{z}{\sqrt{x^2 + y^2 + z^2}}\right) \\
\varphi &= \operatorname{atan2}(y, x)
\end{aligned}
$$

where the definition of $\operatorname{atan2}$ is given in [Mutual conversion between the plane rectangular coordinate system and the polar coordinate system](#mutual-conversion-between-the-plane-rectangular-coordinate-system-and-the-polar-coordinate-system).

Note that for the point $(0,0,0)$ in the space rectangular coordinate system, the values of $\vartheta$ and $\varphi$ of its spherical coordinates are undefined.

From the spherical coordinate system to the space rectangular coordinate system:

$$
\begin{aligned}
x &= r \sin \vartheta \cos \varphi \\
y &= r \sin \vartheta \sin \varphi \\
z &= r \cos \vartheta
\end{aligned}
$$
