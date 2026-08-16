This page mainly introduces the basic knowledge related to network flow.

## Overview

A network refers to a special directed graph $G=(V,E)$; its difference from a general directed graph is that it has capacities and source/sink points.

-   Each edge $(u, v)$ in $E$ has a weight called capacity, denoted $c(u, v)$. When $(u,v)\notin E$, we can assume $c(u,v)=0$.

-   There are two special points in $V$: the source $s$ and the sink $t$ ($s \neq t$).

For a network $G=(V, E)$, a flow is a function from the edge set $E$ to the set of integers or reals, satisfying the following properties.

1.  Capacity constraint: for each edge, the flow passing through that edge does not exceed the capacity of that edge, i.e. $0 \leq f(u,v) \leq c(u,v)$;
2.  Flow conservation: except for the source and sink, the net flow of any node $u$ is $0$. Here, we define the net flow of $u$ as $f(u) = \sum_{x \in V} f(u, x) - \sum_{x \in V} f(x, u)$.

For a network $G = (V, E)$ and a flow $f$ on it, we define the flow value $|f|$ of $f$ as the net flow $f(s)$ of $s$. As a corollary of flow conservation, this also equals the negation $-f(t)$ of the net flow of $t$.

For a network $G = (V, E)$, if $\{S, T\}$ is a partition of $V$ (i.e. $S \cup T = V$ and $S \cap T = \varnothing$) satisfying $s \in S, t \in T$, then we call $\{S, T\}$ an $s$-$t$ cut of $G$. We define the capacity of the $s$-$t$ cut $\{S, T\}$ as $||S, T|| = \sum_{u \in S} \sum_{v \in T} c(u, v)$.

## Common problems

Common network-flow problems include but are not limited to the following types of problems.

-   Maximum flow problem: for a network $G = (V, E)$, assign a flow to each edge to obtain a suitable flow $f$, making the flow value of $f$ as large as possible. At this point we call $f$ a maximum flow of $G$.
-   Minimum cut problem: for a network $G = (V, E)$, find a suitable $s$-$t$ cut $\{S, T\}$, making the total capacity of $\{S, T\}$ as small as possible. At this point we call the total capacity of $\{S, T\}$ the minimum cut of $G$.
-   Minimum-cost maximum-flow problem: on a network $G = (V, E)$, give each edge a weight $w(u, v)$, called the cost, meaning the cost of a unit flow passing through $(u, v)$. Among all possible maximum flows of $G$, we call the one with the smallest total cost the minimum-cost maximum flow.

We will introduce them in detail in later chapters.

## Example problems: the 24 network-flow problems

The 24 network-flow problems are a problem list widely circulated on the Chinese Internet ([LibreOJ](https://loj.ac/problems/tag/30)/[Luogu](https://www.luogu.com.cn/problem/list?tag=332)), which existed at least around 2010. This problem list introduces some classic techniques for modeling other problems as network-flow problems. Due to the limitations of the era, these problems are not necessarily the most representative network-flow problems, but are still worth a read for readers aspiring to algorithm competitions.
