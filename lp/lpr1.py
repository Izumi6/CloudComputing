
class Graph:
    
    def __init__(self):
        self.graph = {}   

  
    def add_edge(self, u, v):
        
        if u not in self.graph:
            self.graph[u] = []

        if v not in self.graph:
            self.graph[v] = []

        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self, node, visited):
        
        visited.add(node)         
        print(node, end=" ")    

     
        for neighbor in self.graph[node]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)  

   
    def bfs(self, start):
        
        visited = set()  
        queue = []        

        visited.add(start)    
        queue.append(start)   

        while queue:
            node = queue.pop(0)   
            print(node, end=" ")  

            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)   
                    queue.append(neighbor) 




g = Graph()   

edges = int(input("Enter number of edges: "))

print("Enter edges (u v):")

for _ in range(edges):
    u, v = input().split()
    g.add_edge(u, v)   

start = input("Enter starting node: ")

print("\nDFS Traversal:")
visited = set()
g.dfs(start, visited)

print("\nBFS Traversal:")
g.bfs(start)
