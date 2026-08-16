author: Anguei, sshwy, Xeonacid, Ir1d, MonkeyOliver, hsfzLZH1

Node splitting is a graph-theory modeling idea, commonly used in [network flow](./flow.md) to handle problems of **node weights or node flow limits**, and also commonly used in **layered graphs**.

## Maximum flow with flow limits on nodes

If we convert nodes into edges, then this problem can be solved by applying the template.

We consider converting a node with a flow limit into the following form: a part composed of two nodes $u,v$ and an edge $\left\langle u,v \right\rangle$. Among them, node $u$ receives all the edges starting from other points in the original graph and arriving at this point in the original graph, and node $v$ leads out all the edges starting from this point in the original graph and reaching other points in the original graph. The flow limit of edge $\left\langle u,v \right\rangle$ is the flow limit of this point in the original graph, and then applying the template can solve this problem. This is the basic idea of node splitting.

If the original graph is like this:

![](./images/node.svg)

The graph after node splitting looks like this:

![](./images/node-split.svg)

## Layered graph shortest path

Layered graph shortest path, such as: there are $k$ times of passing through a path at zero cost, find the total minimum cost. For this kind of problem, we can adopt DP-related ideas, letting $\text{dis}_{i, j}$ denote the shortest path currently from the start point, node $i$, after using $j$ times of free-passage privilege. Obviously, the $\text{dis}$ array can be transferred like this:

$\text{dis}_{i, j} = \min\{\min\{\text{dis}_{from, j - 1}\}, \min\{\text{dis}_{from,j} + w\}\}$

Among them, $from$ denotes the parent node of $i$, and $w$ denotes the edge weight of the currently walked edge. When $j - 1 \geq k$, $\text{dis}_{from, j}$=$\infty$.

In fact, this DP is equivalent to splitting each node into $k+1$ nodes, each new node representing the original-graph node reached after using a different number of free passages. In other words, each node $u_i$ denotes reaching node $u$ after using $i$ times of free-passage privilege.

??? note "[「JLOI2011」Flight route](https://www.luogu.com.cn/problem/P4568)"
    Problem statement: There is an undirected graph with $n$ points and $m$ edges; you can choose $k$ roads to pass through at zero cost; find the minimum cost from $s$ to $t$.
    
    Reference core code:
    
    ```cpp
    struct State {    // node struct of the priority queue
      int v, w, cnt;  // cnt denotes how many times the free-passage privilege has been used
    
      State() {}
    
      State(int v, int w, int cnt) : v(v), w(w), cnt(cnt) {}
    
      bool operator<(const State &rhs) const { return w > rhs.w; }
    };
    
    void dijkstra() {
      memset(dis, 0x3f, sizeof dis);
      dis[s][0] = 0;
      pq.push(State(s, 0, 0));  // no need to use free passage to reach the start point, distance is zero
      while (!pq.empty()) {
        const State top = pq.top();
        pq.pop();
        int u = top.v, nowCnt = top.cnt;
        if (done[u][nowCnt]) continue;
        done[u][nowCnt] = true;
        for (int i = head[u]; i; i = edge[i].next) {
          int v = edge[i].v, w = edge[i].w;
          if (nowCnt < k && dis[v][nowCnt + 1] > dis[u][nowCnt]) {  // can pass for free
            dis[v][nowCnt + 1] = dis[u][nowCnt];
            pq.push(State(v, dis[v][nowCnt + 1], nowCnt + 1));
          }
          if (dis[v][nowCnt] > dis[u][nowCnt] + w) {  // cannot pass for free
            dis[v][nowCnt] = dis[u][nowCnt] + w;
            pq.push(State(v, dis[v][nowCnt], nowCnt));
          }
        }
      }
    }
    
    int main() {
      n = read(), m = read(), k = read();
      // the author is used to numbering from 1 to n, but this problem is from 0 to n - 1, so we need to handle it
      s = read() + 1, t = read() + 1;
      while (m--) {
        int u = read() + 1, v = read() + 1, w = read();
        add(u, v, w), add(v, u, w);  // this problem has bidirectional edges
      }
      dijkstra();
      int ans = std::numeric_limits<int>::max();  // ans takes the int maximum value as the initial value
      for (int i = 0; i <= k; ++i)
        ans = std::min(ans, dis[t][i]);  // take the optimal value over all cases of reaching the end point
      println(ans);
    }
    ```
