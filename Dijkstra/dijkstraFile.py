import sys

def read_graph_from_file(filename):
    graph = []
    with open(filename, "r") as f:
        lines = f.read().strip().splitlines()

        n = int(lines[0])  # so dinh
        for line in lines[1:1+n]:
            row = list(map(int, line.split()))
            graph.append(row)
#         for i in range (n):		#Doi xung qua duong cheo chinh
#             for j in range (n):
#                 graph[j][i]=graph[i][j]

    return graph


def dijkstra(graph, start):
    num_vertices = len(graph)
    visited = [False] * num_vertices
    distance = [sys.maxsize] * num_vertices
    previous = [-1] * num_vertices
    distance[start] = 0

    for _ in range(num_vertices):
        min_dist = sys.maxsize
        u = -1
        for v in range(num_vertices):
            if not visited[v] and distance[v] < min_dist:
                min_dist = distance[v]
                u = v
        visited[u] = True
        for v in range(num_vertices):
            if graph[u][v] != 99 and not visited[v]:
                if distance[u] + graph[u][v] < distance[v]:
                    distance[v] = distance[u] + graph[u][v]		#update distance
                    previous[v] = u
    return distance, previous

def reconstruct_path(previous, target):
    path = []
    while target != -1:
        path.insert(0, target)
        target = previous[target]
    return path

filename = "dijkstraInput.txt"
# filename = input("Input file name e.g (dijkstraInput.txt): ")
graph = read_graph_from_file(filename)
for i in graph:
    print(i, end=' ')
    print()
# tao ten cac dinh: a, b, c, ...
vertices = [chr(ord('0') + i) for i in range(len(graph))]

start_vertex = 0  # bat dau tu dinh 'a'

distances, previous = dijkstra(graph, start_vertex)



print(f"Duong di ngan nhat tu dinh '{vertices[start_vertex]}' den cac dinh:")
for i in range(len(vertices)):
    if i == start_vertex:
        continue
    path_indices = reconstruct_path(previous, i)
    path_names = " -> ".join(vertices[j] for j in path_indices)
    print(f"  {vertices[start_vertex]} -> {vertices[i]} = {distances[i]:<2} | Duong di: {path_names}")
