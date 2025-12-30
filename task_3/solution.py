import networkx as nx
import heapq

# Create a basic weighted graph
G = nx.Graph(name="Basic Weighted Graph")
G.add_nodes_from(["A", "B", "C", "D", "E", "F"])
edges = [
    ("A", "B", 4),
    ("A", "C", 2),
    ("B", "C", 1),
    ("B", "D", 5),
    ("C", "D", 8),
    ("C", "E", 10),
    ("D", "E", 2),
    ("D", "F", 6),
    ("E", "F", 3),
]
for u, v, w in edges:
    G.add_edge(u, v, weight=w)


def dijkstra(G: nx.Graph, start: str) -> dict[str, float]:
    dist = {node: float("inf") for node in G.nodes}
    dist[start] = 0

    pq = [(0, start)]  # (distance, node)

    while pq:
        cur_d, u = heapq.heappop(pq)
        if cur_d != dist[u]:
            continue

        for v in G.neighbors(u):
            w = G[u][v].get("weight", 1)
            new_d = cur_d + w
            if new_d < dist[v]:
                dist[v] = new_d
                heapq.heappush(pq, (new_d, v))

    return dist


if __name__ == "__main__":
    print("===", G.graph.get("name", "Graph"), "===")
    start = "A"
    dist = dijkstra(G, start)
    for node in dist:
        print(f"{start}->{node}: {dist[node]}")
