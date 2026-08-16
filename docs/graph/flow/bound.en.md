Before reading this article, please first read [maximum flow](./max-flow.md) and make sure you have mastered the maximum flow algorithm.

## Overview

Bounded network flow essentially sets an upper flow bound $c(u,v)$ and a lower flow bound $b(u,v)$ for each edge of the flow network. That is to say, a feasible flow must satisfy $b(u,v) \leq f(u,v) \leq c(u,v)$. At the same time, the flow of the remaining points except the source and sink must be balanced.

According to the problem requirements, we can use bounded network flow to solve different problems.

## Feasible flow with bounds and without source/sink

Given a source/sink-free flow network $G$. Ask whether there exists a way to calibrate the flow of each edge such that the flow of each edge satisfies the bounds and the flow of every point is balanced.

We may as well assume that each edge has already flowed $b(u,v)$ of flow, and set it as the initial flow. At the same time we add in the new graph an edge from $u$ to $v$ with flow $c(u,v) - b(u,v)$. Consider making adjustments on the new graph.

Since the maximum flow needs to satisfy the initial flow-balance condition (the maximum flow can be regarded as a bounded maximum flow with lower bound $0$), but the constructed initial flow is very likely not to satisfy initial flow balance. Suppose the initial inflow minus the initial outflow of a point is $M$.

If $M=0$, at this point the flow is balanced, and no additional edge is needed.

If $M>0$, at this point the inflow is too large, and we need to create an additional source $S'$, which connects an additional edge with flow $M$ to it.

If $M<0$, at this point the outflow is too large, and we need to create an additional sink $T'$, to which it connects an additional edge with flow $-M$.

If the additional edge is at full flow, it means the flow-balance condition of this point can be satisfied, otherwise the flow-balance condition of this point is not satisfied. (Because the flow balance in the original graph is only satisfied after the original graph plus the additional flow.)

After building the graph, run the maximum flow from $S'$ to $T'$; if all edges connected out from $S'$ are at full flow, then a feasible flow exists, otherwise it does not.

### Example problem

???+ note "[luogu P14578 【Template】Feasible Flow with Bounds and without Source/Sink](https://www.luogu.com.cn/problem/P14578)"
    A directed graph $G$ with $n$ points and $m$ directed edges, where each edge has a lower flow bound $l_i$ and an upper flow bound $r_i$.
    
    Construct a scheme such that the flow $w_i$ of each edge satisfies the flow constraint $l_i\leq w_i\leq r_i$, and each point's flow is balanced, i.e. the inflow of each point equals its outflow. Or report no solution.

??? note "Reference code"
    ```cpp
    --8<-- "docs/graph/code/flow/bound/bound_1.cpp"
    ```

## Feasible flow with bounds and with source/sink

Given a flow network $G$ with source/sink. Ask whether there exists a way to calibrate the flow of each edge such that the flow of each edge satisfies the bounds and every point except the source and sink has balanced flow.

Suppose the source is $S$ and the sink is $T$.

Then we can add an edge from $T$ to $S$ with upper bound $\infty$ and lower bound $0$ to convert it into a feasible-flow-with-bounds-and-without-source/sink problem.

If there is a solution, then the feasible flow from $S$ to $T$ equals the flow of the additional edge from $T$ to $S$.

## Maximum flow with bounds and with source/sink

Given a flow network $G$ with source/sink. Ask whether there exists a way to calibrate the flow of each edge such that the flow of each edge satisfies the bounds and every point except the source and sink has balanced flow. If it exists, ask for the maximum flow satisfying the calibration.

We find any feasible flow on the network. If no solution can be found, we can directly end.

Otherwise we consider the residual network after deleting all additional edges and make adjustments on the network.

We run the maximum flow from $S$ to $T$ once more on the residual network, and add the feasible flow and the maximum flow as the answer.

??? warning "A very error-prone problem"
    The maximum flow from $S$ to $T$ is run directly on the residual network after running the feasible flow with bounds and with source/sink.
    
    It must not be run on the original flow network.

## Minimum flow with bounds and with source/sink

Given a flow network $G$ with source/sink. Ask whether there exists a way to calibrate the flow of each edge such that the flow of each edge satisfies the bounds and every point except the source and sink has balanced flow. If it exists, ask for the minimum flow satisfying the calibration.

Similarly, we consider returning the unneeded flow in the residual network.

We find any feasible flow on the network. If no solution can be found, we can directly end.

Otherwise we consider the residual network after deleting all additional edges.

We run the maximum flow from $T$ to $S$ once more on the residual network, and subtract the maximum flow from the feasible flow as the answer.

??? note "[AHOI 2014 Side Plot](https://loj.ac/problem/2226)"
    For each plot edge from $x$ to $y$ with cost $v$, set the upper bound to $\infty$ and the lower bound to $1$.
    
    For each point, connect an edge to $T$ with edge weight $c$, upper bound $\infty$, lower bound $1$.
    
    Point $S$ is node $1$.
    
    Just run a minimum-cost feasible flow with bounds and with source/sink once.
    
    Because the minimum-cost feasible flow solution is similar to the minimum feasible flow, it is not elaborated here.
