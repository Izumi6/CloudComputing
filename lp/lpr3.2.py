#	Kruskal's Algorithm

def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, x, y):
    parent[x] = y


def kruskal(n, edges):
    edges.sort(key=lambda x: x[2])

    parent = [i for i in range(n)]
    mst = []
    total_cost = 0

    for u, v, w in edges:
        root_u = find(parent, u)
        root_v = find(parent, v)

        if root_u != root_v:
            mst.append((u, v, w))
            total_cost += w
            union(parent, root_u, root_v)

    return mst, total_cost


n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

edges = []
for _ in range(e):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))

mst, cost = kruskal(n, edges)

print("Edges in MST:")
for u, v, w in mst:
    print(u, "-", v, "=", w)

print("Total Cost of MST:", cost)

