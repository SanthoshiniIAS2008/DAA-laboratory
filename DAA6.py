import sys

def matrix_chain_order(p):
    n = len(p) - 1

    # Cost table
    m = [[0] * n for _ in range(n)]

    # Split table
    s = [[0] * n for _ in range(n)]

    # DP computation
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            m[i][j] = sys.maxsize

            for k in range(i, j):
                cost = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j + 1]

                if cost < m[i][j]:
                    m[i][j] = cost
                    s[i][j] = k

    return m, s


# Function to print optimal parenthesization
def print_parenthesis(s, i, j):
    if i == j:
        return f"A{i+1}"

    k = s[i][j]
    left = print_parenthesis(s, i, k)
    right = print_parenthesis(s, k + 1, j)

    return f"({left} x {right})"


# ---------------- Driver Code ----------------

n = int(input("Enter number of matrices: "))

dimensions = []
for i in range(n):
    r, c = map(int, input(f"Enter rows and columns of A{i+1}: ").split())

    if i == 0:
        dimensions.append(r)
    dimensions.append(c)

m, s = matrix_chain_order(dimensions)

print("\nMatrix Dimensions:")
for i in range(n):
    print(f"A{i+1}: {dimensions[i]} x {dimensions[i+1]}")

print("\nMinimum scalar multiplications:", m[0][n - 1])

print("Optimal parenthesization:", print_parenthesis(s, 0, n - 1))

print("\nDP Cost Table m[i][j]:")

print("      ", end="")
for i in range(n):
    print(f"A{i+1:>6}", end="")
print()

for i in range(n):
    print(f"A{i+1:<4}", end="")
    for j in range(n):
        if j < i:
            print(f"{'---':>7}", end="")
        else:
            print(f"{m[i][j]:>7}", end="")
    print()