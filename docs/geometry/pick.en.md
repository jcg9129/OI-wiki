## Pick's theorem

Pick's theorem: given a simple polygon all of whose vertices are integer points, Pick's theorem states the relationship among its area ${\displaystyle A}$, the number of interior lattice points ${\displaystyle i}$, and the number of lattice points on the boundary ${\displaystyle b}$: ${\displaystyle A=i+{\frac {b}{2}}-1}$.

For the specific proof: [Pick's theorem](https://en.wikipedia.org/wiki/Pick%27s_theorem)

It has the following generalizations:

-   Take the area of the figure composed of lattice points as one unit. On parallelogram lattices, Pick's theorem still holds. Applied to arbitrary triangular lattices, Pick's theorem is ${\displaystyle A=2 \times i+b-2}$.
-   For a non-simple polygon ${\displaystyle P}$, Pick's theorem is ${\displaystyle A=i+{\frac {b}{2}}-\chi (P)}$, where ${\displaystyle \chi (P)}$ denotes the **Euler characteristic** of ${\displaystyle P}$.
-   High-dimensional generalization: the Ehrhart polynomial
-   Pick's theorem is equivalent to **Euler's formula** (${\displaystyle V-E+F=2}$).

## An example problem ([POJ 1265](http://poj.org/problem?id=1265))

### Problem summary

In the Cartesian coordinate system, a robot starts from an arbitrary point and makes $\textit{n}$ moves; each time it moves right by $\textit{dx}$ and up by $\textit{dy}$; finally it forms a closed simple polygon in the plane. Find the number of points on the boundary, the number of points inside the polygon, and the polygon's area.

### Solution

This problem actually uses the following three pieces of knowledge:

-   For a line segment with integer points as vertices, if both edges $\textit{dx}$ and $\textit{dy}$ are nonzero, the number of lattice points passed is $\gcd(\textit{dx}, \textit{dy}) + 1$; of course, if computing for an entire figure, the extra added point will be counted by the previous edge, so it does not need to be added. Then the number of points covered by one edge is $\gcd(\textit{dx},\textit{dy})$, where $\textit{dx},\textit{dy}$ are the number of points the segment occupies horizontally and vertically respectively. If $\textit{dx}$ or $\textit{dy}$ is $0$, then the number of covered points is $\textit{dy}$ **or** $\textit{dx}$.
-   Pick's theorem: the area of a simple polygon in the plane with integer points as vertices = number of points on the boundary / 2 + number of interior points - 1.
-   The area of any polygon equals half the sum of the cross products of the vectors formed by each pair of adjacent points and the origin, taken in order (this can also be obtained by clockwise definite integration).

??? note "Reference code"
    ```cpp
    --8<-- "docs/geometry/code/pick/pick_1.cpp"
    ```
