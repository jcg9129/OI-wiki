This page briefly introduces the simulation approach.

## Introduction

Simulation is using a computer to simulate the operations required by the problem.

Simulation problems usually have the characteristics of a large amount of code, many operations, and complicated logic. Because of the large amount of code, it is often difficult to debug, and writing it wrong during a contest is quite a waste of time.

## Techniques

When writing simulation problems, following the suggestions below may improve your solving speed:

-   Before starting to write code, write out the process to be implemented as fully as possible on scratch paper.
-   In the code, try to modularize each part, writing it as a function, struct, or class.
-   For some concepts that may be used repeatedly, you can convert them uniformly for convenient handling: for example, if a problem gives you "YY-MM-DD hour:minute", extracting it into a function and converting it into seconds reduces conceptual confusion.
-   Debug block by block when debugging. The benefit of modularization is that you can conveniently debug a single part in isolation.
-   When writing code, keep your logic clear; do not write whatever comes to mind, but write according to the steps you put on paper.

In fact, the above steps are also very helpful when solving other types of problems.

## Detailed worked example

???+ note "[Climbing Worm](https://open.kattis.com/problems/climbingworm)"
    A worm of negligible length is at the bottom of a well $n$ inches deep. Each time it climbs up $u$ inches, but it must rest once before it can climb up again. While resting, it slides down $d$ inches. After that it repeats the process of climbing up and resting. How many times must the worm climb, at minimum, to climb out of the well? If the worm reaches exactly the top of the well after climbing, we also consider that the worm has climbed out of the well.

??? note "Solution idea"
    Simply use a program to simulate the process of the worm climbing the well. Use a loop to repeat the worm's climbing process, and break out when the climbed length exceeds or equals the depth of the well.

??? note "Reference code"
    === "C++"
        ```cpp
        --8<-- "docs/basic/code/simulate/simulate_1.cpp"
        ```
    
    === "Python"
        ```python
        --8<-- "docs/basic/code/simulate/simulate_1.py"
        ```
    
    === "Java"
        ```java
        --8<-- "docs/basic/code/simulate/simulate_1.java"
        ```

## Exercises

-   ["NOIP2014" Big Bang Theory Rock-Paper-Scissors - Universal Online Judge](https://uoj.ac/problem/15)
-   ["OpenJudge 3750" World of Warcraft](http://bailian.openjudge.cn/practice/3750/)
-   ["SDOI2010" Killer of the Pig Kingdom - LibreOJ](https://loj.ac/problem/2885)
