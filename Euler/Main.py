from Euler import Euler

def read_graph_from_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        V = int(lines[0])
        graph = Euler(V)
        for line in lines[1:]:
            u, v = map(int, line.strip().split())
            graph.add_edge(u, v)
    return graph

# ======= MAIN =======
if __name__ == "__main__":
    graph = read_graph_from_file("EulerInput.txt")
    etype = graph.find_eulerian_type()
    if etype == 0:
        print("Do thi KHONG co duong di hoac chu trinh Euler.")
    elif etype == 1:
        print("Do thi co duong di Euler:")
        path = graph.find_eulerian_path_or_circuit()
        print(" -> ".join(map(str, path)))
    else:
        print("Do thi co chu trinh Euler:")
        path = graph.find_eulerian_path_or_circuit()
        print(" -> ".join(map(str, path)))

# 5
# 0 1
# 1 2
# 2 0
# 1 3
# 3 4
# 1 4
# 

# 5
# 0 1
# 0 2
# 1 2
# 2 3
# 3 4
# 4 0

# 8
# 0 1
# 0 7
# 1 2
# 1 6 
# 1 7
# 2 3
# 3 4
# 3 6
# 3 7
# 4 5
# 5 6
# 6 7