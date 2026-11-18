n = int(input("Enter number of vertices: "))
INF = 99999
dist = []

print("Enter adjacency matrix (use 99999 for no edge):")
for i in range(n):
    dist.append(list(map(int, input().split())))

for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j],
                             dist[i][k] + dist[k][j])

print("Shortest distance matrix:")
for row in dist:
    print(*row)
