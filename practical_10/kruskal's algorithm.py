def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])
    return parent[i]


n = int(input("Enter vertices: "))
e = int(input("Enter edges: "))
edges = []

for _ in range(e):
    u, v, w = map(int, input("Enter u v weight: ").split())
    edges.append((w, u, v))

edges.sort()
parent = list(range(n))
total = 0

print("MST edges:")
for w, u, v in edges:
    a = find(parent, u)
    b = find(parent, v)

    if a != b:
        parent[a] = b
        print(u, "-", v, ":", w)
        total += w

if len({find(parent, i) for i in range(n)}) == 1:
    print("Minimum cost:", total)
else:
    print("MST is not possible")
