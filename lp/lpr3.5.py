#Prim's Minimal Spanning Tree Algorithm
import heapq   # Used for priority queue (min-heap)

# Function to implement Prim's Algorithm
def prim(n, graph):

    # 🔹 Step 1: Create visited array (to track included vertices)
    visited = [False] * n

    # 🔹 Step 2: Min-heap to store (weight, vertex)
    # Start from vertex 0 with weight 0
    min_heap = [(0, 0)]

    # 🔹 Step 3: Initialize total cost of MST
    total_cost = 0

    # 🔹 Step 4: Loop until heap is empty
    while min_heap:

        # Extract minimum weight edge
        weight, u = heapq.heappop(min_heap)

        # 🔹 Step 5: Skip if already visited
        if visited[u]:
            continue

        # 🔹 Step 6: Mark current vertex as visited
        visited[u] = True

        # 🔹 Step 7: Add weight to total cost
        total_cost += weight

        # 🔹 Step 8: Traverse all adjacent vertices
        for v, w in graph[u]:

            # If neighbor is not visited
            if not visited[v]:
                # Push edge into heap
                heapq.heappush(min_heap, (w, v))

    # 🔹 Step 9: Return total cost of MST
    return total_cost


# 🔹 User Input
n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

# Create adjacency list
graph = [[] for _ in range(n)]

print("Enter edges (u v weight):")
for _ in range(e):
    u, v, w = map(int, input().split())

    # Since graph is undirected, add both sides
    graph[u].append((v, w))
    graph[v].append((u, w))


# 🔹 Call Prim's Algorithm
cost = prim(n, graph)

# 🔹 Output result
print("Minimum Cost of MST:", cost)
