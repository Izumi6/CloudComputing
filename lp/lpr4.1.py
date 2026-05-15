# Graph Coloring using Branch and Bound + Backtracking

def is_safe(graph, colors, node, color):
    for neighbor in graph[node]:
        if colors[neighbor] == color:
            return False
    return True


def solve(graph, m, colors, node, n):
    if node == n:
        return True

    for color in range(1, m + 1):
        if is_safe(graph, colors, node, color):
            colors[node] = color

            if solve(graph, m, colors, node + 1, n):
                return True

            colors[node] = 0  # Backtrack

    return False


def graph_coloring(n, edges, m):
    graph = [[] for _ in range(n)]

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    colors = [0] * n

    if solve(graph, m, colors, 0, n):
        return colors
    else:
        return None


# --- User Input ---
n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

edges = []
print("Enter edges (u v):")
for _ in range(e):
    u, v = map(int, input().split())
    edges.append((u, v))

m = int(input("Enter number of colors: "))

# --- Solve ---
color_names = ["Red", "Green", "Blue", "Yellow", "Orange"]

result = graph_coloring(n, edges, m)

if result:
    print("\nSolution Found!")
    print("-" * 25)
    for i in range(n):
        name = color_names[result[i] - 1] if result[i] <= len(color_names) else f"Color {result[i]}"
        print(f"  Vertex {i} --> {name}")
    print("-" * 25)
else:
    print(f"\nNo solution possible with {m} colors.")
