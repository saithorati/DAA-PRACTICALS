def prim(graph, n, start):
    visited = [False] * n
    visited[start] = True
    total = 0

    for _ in range(n - 1):
        minimum = float('inf')
        u = -1
        v = -1

        for i in range(n):
            if visited[i]:
                for j in range(n):
                    if graph[i][j] > 0 and not visited[j]:
                        if graph[i][j] < minimum:
                            minimum = graph[i][j]
                            u = i
                            v = j

        if v == -1:
            print("MST is not possible")
            return

        print(u, "-", v, ":", minimum)
        visited[v] = True
        total += minimum

    print("Minimum cost:", total)


n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

graph = [[0] * n for _ in range(n)]

for _ in range(e):
    u = int(input("Enter first vertex: "))
    v = int(input("Enter second vertex: "))
    w = int(input("Enter weight: "))
    graph[u][v] = w
    graph[v][u] = w

start = int(input("Enter starting vertex: "))

prim(graph, n, start)
