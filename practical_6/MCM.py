# Matrix Chain Multiplication using Dynamic Programming

n = int(input("Enter number of matrices: "))

# Create dimension array
p = []

print("Enter", n + 1, "dimensions:")

for i in range(n + 1):
    value = int(input(f"Dimension {i + 1}: "))
    p.append(value)

# DP table
dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

# length = number of matrices in the chain
for length in range(2, n + 1):

    for i in range(1, n - length + 2):

        j = i + length - 1

        dp[i][j] = float('inf')

        # Try every possible split
        for k in range(i, j):

            cost = (
                dp[i][k]
                + dp[k + 1][j]
                + p[i - 1] * p[k] * p[j]
            )

            if cost < dp[i][j]:
                dp[i][j] = cost

print()
print("Minimum number of scalar multiplications =", dp[1][n])
