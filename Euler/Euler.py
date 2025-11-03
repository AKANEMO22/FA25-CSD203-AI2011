from collections import defaultdict

class Euler:
    def __init__(self, V):
        self.V = V
        self.adj = defaultdict(list)

    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def dfs(self, v, visited):
        visited[v] = True
        for neighbor in self.adj[v]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited)

    def is_connected(self):
        visited = [False] * self.V

        # Tim dinh dau tien co bac > 0
        start = -1
        for i in range(self.V):
            if len(self.adj[i]) > 0:
                start = i
                break
        if start == -1:
            return True

        # DFS tu dinh co bac > 0
        self.dfs(start, visited)

        for i in range(self.V):
            if not visited[i] and len(self.adj[i]) > 0:
                return False
        return True

    def find_eulerian_type(self):
        if not self.is_connected():
            return 0  # Khong lien thong
        
        odd=0
        for v in self.adj:
            if len(self.adj[v]) % 2 != 0: # So dinh bac le
                odd+=1
        
        if odd == 0:
            return 2  # Chu trinh Euler
        elif odd == 2:
            return 1  # Duong di Euler
        else:
            return 0  # Khong co

    def find_eulerian_path_or_circuit(self):
        Eg = defaultdict(list)
        for u in self.adj:
            for v in self.adj[u]:
                Eg[u].append(v)

        stack = []
        path = []

        # Tim dinh bat dau phu hop - Dinh bac le
        start = 0
        for i in range(self.V):
            if len(Eg[i]) % 2 == 1:
                start = i
                break

        stack.append(start)
        while stack:
            v = stack[-1]
            if Eg[v]:
                u = Eg[v].pop()
                Eg[u].remove(v)
                stack.append(u)
            else:
                path.append(stack.pop())
        return path
