def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(grid, start, goal):
    
    open_list = [start]     
    visited = set()         

    g_cost = {start: 0}    
    parent = {}             

    while open_list:
        
        current = open_list[0]
        for node in open_list:
            if g_cost[node] + heuristic(node, goal) < g_cost[current] + heuristic(current, goal):
                current = node

        if current == goal:
            path = []
            while current in parent:
                path.append(current)
                current = parent[current]
            path.append(start)
            path.reverse()
            return path

        open_list.remove(current)
        visited.add(current)

        x, y = current
        neighbors = [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]

        for n in neighbors:
            r, c = n

            if r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0]) and grid[r][c] == 0:
                
                if n in visited:
                    continue

                new_cost = g_cost[current] + 1

                if n not in open_list:
                    open_list.append(n)
                elif new_cost >= g_cost.get(n, 999):
                    continue

                g_cost[n] = new_cost
                parent[n] = current

    return None

grid = [
    [0, 0, 0],
    [1, 0, 1],
    [0, 0, 0]
]

start = (0, 0)
goal = (2, 2)

path = a_star(grid, start, goal)

print("Path:", path)
