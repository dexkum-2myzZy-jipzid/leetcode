from typing import List, Tuple, Optional, Set
from math import inf
import heapq

Edge = Tuple[int, int, float]  # (u, v, w)


def bellman_ford(n: int, edges: List[Edge], src: int):
    """
    Standard Bellman-Ford.
    - Supports negative weights.
    - Detects negative cycles reachable from src.
    Returns:
        dist: List[float]  shortest distances from src (inf if unreachable)
        parent: List[int]  predecessor array for path reconstruction (-1 if none)
        has_negative_cycle: bool  whether a reachable negative cycle exists
    """
    dist = [inf] * n
    parent = [-1] * n
    dist[src] = 0.0

    # V-1 relaxation rounds
    for _ in range(n - 1):
        updated = False
        for u, v, w in edges:
            if dist[u] != inf and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parent[v] = u
                updated = True
        if not updated:
            break

    # One more pass to detect a reachable negative cycle
    has_negative_cycle = False
    for u, v, w in edges:
        if dist[u] != inf and dist[u] + w < dist[v]:
            has_negative_cycle = True
            break

    return dist, parent, has_negative_cycle


def floyd_warshall(
    n: int,
    edges: List[Tuple[int, int, int]],
    directed: bool = True,
) -> Tuple[List[List[int]], List[List[Optional[int]]], Set[int]]:
    """
    Floyd-Warshall with path reconstruction.
      - n: number of nodes (0..n-1)
      - edges: list of (u, v, w)
      - directed: treat edges as directed if True
    Returns (dist, nxt, neg_cycle_nodes):
      - dist[i][j]: shortest distance from i to j (inf if unreachable)
      - nxt[i][j]: next node after i on a shortest path to j (None if no path)
      - neg_cycle_nodes: nodes i with dist[i][i] < 0 (on a negative cycle)
    """
    # Initialize distance and next matrices
    dist: List[List[int]] = [[inf for _ in range(n)] for _ in range(n)]
    nxt: List[List[Optional[int]]] = [[None for _ in range(n)] for _ in range(n)]

    for i in range(n):
        dist[i][i] = 0
        nxt[i][i] = i

    # Load edges
    for u, v, w in edges:
        if w < dist[u][v]:
            dist[u][v] = w
            nxt[u][v] = v
        if not directed and w < dist[v][u]:
            dist[v][u] = w
            nxt[v][u] = u

    # Main DP
    for k in range(n):
        for i in range(n):
            if dist[i][k] == inf:
                continue
            for j in range(n):
                if dist[k][j] == inf:
                    continue
                new_dist = dist[i][k] + dist[k][j]
                if new_dist < dist[i][j]:
                    dist[i][j] = new_dist
                    nxt[i][j] = nxt[i][k]

    # Negative cycle detection (simple)
    neg_cycle_nodes: Set[int] = {i for i in range(n) if dist[i][i] < 0}

    return dist, nxt, neg_cycle_nodes


# MST
def mst_kruskal(n, edges):
    """
    n: 节点数，节点编号为 [0..n-1]
    edges: 列表 [(w, u, v)], 已0-index
    返回: 最小总成本；若不连通，返回 -1
    """
    dsu = DSU(n)
    cost, taken = 0, 0
    for w, u, v in sorted(edges):
        if dsu.union(u, v):
            cost += w
            taken += 1
            if taken == n - 1:
                return cost
    return -1


def mst_prim_adj(n, adj):
    """
    n: 节点数
    adj: 邻接表, adj[u] = [(w, v), ...]
    返回: 最小总成本；若不连通，返回 -1
    """
    visited = [False] * n
    pq = [(0, 0)]  # (边权, 目标点)
    cost, count = 0, 0
    while pq and count < n:
        w, v = heapq.heappop(pq)
        if visited[v]:
            continue
        visited[v] = True
        cost += w
        count += 1
        for w2, to in adj[v]:
            if not visited[to]:
                heapq.heappush(pq, (w2, to))
    return cost if count == n else -1
