#Dijkstra's Algorithm
import heapq

def dijkstra(graph, source):
    n = len(graph)
    dist = [float('inf')] * n
    dist[source] = 0

    pq = []
    heapq.heappush(pq, (0, source))

    while pq:
        current_dist, u = heapq.heappop(pq)

        for v, weight in graph[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                heapq.heappush(pq, (dist[v], v))

    return dist


# 🔹 User Input
n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

graph = [[] for _ in range(n)]

print("Enter edges (u v weight):")
for _ in range(e):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))  # remove if directed graph

source = int(input("Enter source vertex: "))

distances = dijkstra(graph, source)

print("\nShortest distances from source:")
for i in range(n):
    print(f"Distance to {i} =", distances[i])
