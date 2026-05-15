#Kruskal's Minimal Spanning Tree Algorithm
# Function to find parent (root) of a node
def find(parent, i):
    # If node is its own parent, return it
    if parent[i] == i:
        return i
    # Otherwise, recursively find root
    return find(parent, parent[i])


# Function to perform union of two sets
def union(parent, x, y):
    # Connect root of one node to another
    parent[x] = y


# Kruskal's Algorithm function
def kruskal(n, edges):

    # 🔹 Step 1: Sort edges by weight (ascending)
    edges.sort(key=lambda x: x[2])

    # 🔹 Step 2: Initialize parent array
    parent = [i for i in range(n)]

    mst = []           # To store MST edges
    total_cost = 0     # To store total weight

    # 🔹 Step 3: Process each edge
    for u, v, w in edges:

        # Find root of both vertices
        root_u = find(parent, u)
        root_v = find(parent, v)

        # 🔹 Step 4: Check for cycle
        if root_u != root_v:

            # Add edge to MST
            mst.append((u, v, w))
            total_cost += w

            # Perform union
            union(parent, root_u, root_v)

    # 🔹 Step 5: Return MST and cost
    return mst, total_cost


# 🔹 User Input
n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

edges = []
print("Enter edges (u v weight):")

for _ in range(e):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))


# 🔹 Call Kruskal's Algorithm
mst, cost = kruskal(n, edges)

# 🔹 Output
print("\nEdges in MST:")
for u, v, w in mst:
    print(u, "-", v, "=", w)

print("Total Cost of MST:", cost) 
