from itertools import permutations

n = int(input("Enter number of cities: "))
cost = []

print("Enter cost matrix (99999 for no route):")
for i in range(n):
    cost.append(list(map(int, input().split())))

minimum = float('inf')
best = None

for p in permutations(range(1, n)):
    path = (0,) + p + (0,)
    total = 0

    for i in range(n):
        total += cost[path[i]][path[i + 1]]

    if total < minimum:
        minimum = total
        best = path

if minimum >= 99999:
    print("Tour is not possible")
else:
    print("Minimum cost:", minimum)
    print("Best path:", *best)
