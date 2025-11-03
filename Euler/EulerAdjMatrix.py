from collections import defaultdict

class Euler:
    def __init__(self, V):
        self.V = V
        self.adj = defaultdict(list)

    # Them canh cho do thi vo huong
    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    # DFS de kiem tra lien thong
    def dfs(self, v, visited):
        visited[v] = True
        for nei in self.adj[v]:
            if not visited[nei]:
                self.dfs(nei, visited)

    # Kiem tra do thi co lien thong khong (bo qua cac dinh bac 0)
    def is_connected(self):
        visited = [False] * self.V

        # Tim dinh dau tien co bac > 0
        start = -1
        for i in range(self.V):
            if len(self.adj[i]) > 0:
                start = i
                break

        # Neu khong co canh nao thi coi la lien thong
        if start == -1:
            return True

        self.dfs(start, visited)

        # Neu co dinh co bac > 0 nhung chua duoc tham => khong lien thong
        for i in range(self.V):
            if len(self.adj[i]) > 0 and not visited[i]:
                return False

        return True

    # 0 = khong co Euler
    # 1 = Euler Path
    # 2 = Euler Circuit
    def find_eulerian_type(self):
        if not self.is_connected():
            return 0

        odd = sum(1 for v in range(self.V) if len(self.adj[v]) % 2 == 1)

        if odd == 0:
            return 2   # Circuit
        if odd == 2:
            return 1   # Path
        return 0

    # Thuat toan Hierholzer
    def find_eulerian_path_or_circuit(self):
        # Tao ban sao danh sach ke
        Eg = {u: self.adj[u][:] for u in range(self.V)}

        stack = []
        path = []

        # Chon dinh bat dau
        start = 0
        for i in range(self.V):
            if len(Eg[i]) % 2 == 1:
                start = i
                break

        stack.append(start)

        # Hierholzer
        while stack:
            v = stack[-1]
            if Eg[v]:
                u = Eg[v].pop()
                Eg[u].remove(v)
                stack.append(u)
            else:
                path.append(stack.pop())

        return path

def read_graph_from_adj_matrix(filename):
    with open(filename, "r") as f:
        lines = f.read().strip().splitlines()

    V = int(lines[0].strip())       # so dinh
    matrix = []

    # Doc dung V dong ma tran
    for line in lines[1:1+V]:
        row = list(map(int, line.split()))
        if len(row) != V:
            raise ValueError("Moi dong ma tran phai co dung V so.")
        matrix.append(row)

    g = Euler(V)

    for i in range(V):
        for j in range(i+1, V):
            if matrix[i][j] != 0:   # co canh
                g.add_edge(i, j)

    return g

if __name__ == "__main__":
    filename = "EulerInputMatrix.txt"
    graph = read_graph_from_adj_matrix(filename)

    etype = graph.find_eulerian_type()

    if etype == 0:
        print("Do thi KHONG co Euler Path hoac Euler Circuit.")
    else:
        path = graph.find_eulerian_path_or_circuit()

        if etype == 1:
            print("Eulerian Path:")
        else:
            print("Eulerian Circuit:")

        print(" -> ".join(map(str, path)))


