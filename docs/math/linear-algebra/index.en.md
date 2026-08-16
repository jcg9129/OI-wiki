author: codewasp942

??? tip "Tip"
    This article has little connection with the other articles under the "linear algebra" category. But the author believes that discussing the essence of linear algebra, tracing the origins and connections of the concepts, and giving the reader a preliminary but systematic understanding of linear algebra, does have its necessity.

As early as thousands of years ago, the ancients applied systems of linear equations to solve problems, and today, linear algebra is still widely applied.

Linear algebra originates from people's observations. People found that many objects have similar properties, for example:

-   Forces can be decomposed and composed.

-   For any $k,x_0$, $k \sin (x-x_0)$ can be decomposed into $k_1\sin x + k_2\cos x$.

These properties are related to the **scaling**, **decomposition**, **superposition**, etc. of the objects described. Linear algebra abstracts these properties from concrete objects and studies them as an independent discipline. In OI, knowledge of linear algebra can be used directly to solve problems, and can also be used to optimize algorithms, data structures, etc. For example:

-   Using tree decomposition to maintain a linear basis to find the maximum XOR sum on a chain

-   Using the matrix-tree theorem to convert the problem of counting spanning trees of a graph into finding the determinant of a matrix

-   Using matrix fast exponentiation to optimize recurrences
