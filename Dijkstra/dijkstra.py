import sys

def dijkstra(graph, start):
    num_vertices = len(graph)
    visited = [False] * num_vertices
    distance = [sys.maxsize] * num_vertices
    previous = [-1] * num_vertices  # Luu dinh truoc do trong duong di
    distance[start] = 0

    for _ in range(num_vertices):
        # Chon dinh chua duoc tham va co khoang cach nho nhat
        min_dist = sys.maxsize
        u = -1
        for v in range(num_vertices):
            if not visited[v] and distance[v] < min_dist:
                min_dist = distance[v]
                u = v

        visited[u] = True

        # Cap nhat khoang cach den cac dinh ke
        for v in range(num_vertices):
            if graph[u][v] != 99 and not visited[v]:
                if distance[u] + graph[u][v] < distance[v]:
                    distance[v] = distance[u] + graph[u][v]
                    previous[v] = u  # Luu vet duong di

    return distance, previous

def reconstruct_path(previous, target):
    path = []
    while target != -1:
        path.insert(0, target)
        target = previous[target]
    return path

# Ma tran ke (99 la vo cuc)
# graph = [
#     [0, 7, 9, 99, 99, 14],   # a
#     [7, 0, 10, 15, 99, 99],  # b
#     [9, 10, 0, 11, 99, 2],   # c
#     [99, 15, 11, 0, 6, 99],  # d
#     [99, 99, 99, 6, 0, 9],   # e
#     [14, 99, 2, 99, 9, 0]    # f
# ]
graph = [
[0,	4,	99,	99,	99,	99,	99,	9,	99,	10],
[4,	0,	8,	99,	99,	99,	99,	99,	99,	5],
[99,	8,	0,	15,	99,	99,	99,	99,	12,	99],
[99,	99,	15,	0,	7,	99,	99,	99,	99,	99],
[99,	99,	99,	7,	0,	3,	99,	99,	4,	99],
[99,	99,	99,	99,	3,	0,	6,	99,	8,	99],
[99,	99,	99,	99,	99,	6,	0,	2,	2,	1],
[9,	99,	99,	99,	99,	99,	2,	0,	99,	6],
[99,	99,	12,	99,	4,	8,	2,	99,	0,	3],
[10,	5,	99,	99,	99,	99,	1,	6,	3,	0]
]

# vertices = ['a', 'b', 'c', 'd', 'e', 'f']
vertices = ['a', 'b', 'c', 'd', 'e', 'f','g','h','i','j']
start_vertex = 0  # Dinh a

# Thuc hien Dijkstra
distances, previous = dijkstra(graph, start_vertex)

# Hien thi ket qua
print(f"Duong di ngan nhat tu dinh '{vertices[start_vertex]}' den cac dinh:")
for i in range(len(vertices)):
    if i == start_vertex:
        continue
    path_indices = reconstruct_path(previous, i)
    path_names = ' -> '.join(vertices[j] for j in path_indices)
    print(f"  {vertices[start_vertex]} -> {vertices[i]} = {distances[i]:<2} | Duong di: {path_names}")
