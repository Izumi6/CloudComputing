
#Dijkstra's 

import heapq   # For priority queue

# Function for Dijkstra Algorithm
def dijkstra(graph, source):

    n = len(graph)

    # 🔹 Step 1: Initialize distances
    dist = [float('inf')] * n
    dist[source] = 0

    # 🔹 Step 2: Min heap (distance, node)
    pq = [(0, source)]

    # 🔹 Step 3: Process nodes
    while pq:

        current_dist, u = heapq.heappop(pq)

        # 🔹 Step 4: Check neighbors
        for v, weight in graph[u]:

            # If shorter path found
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight

                # Push updated distance
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
    graph[v].append((u, w))   # Remove for directed graph

source = int(input("Enter source vertex: "))

# 🔹 Call function
distances = dijkstra(graph, source)

# 🔹 Output
print("\nShortest distances from source:")
for i in range(n):
    print(f"Distance to {i} =", distances[i])
