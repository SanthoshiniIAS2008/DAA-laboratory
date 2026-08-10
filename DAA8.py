import math

INF = math.inf

# Cost Matrix
cost = [
    [INF, 10, 8, 9, 7],
    [10, INF, 10, 5, 6],
    [8, 10, INF, 8, 9],
    [9, 5, 8, INF, 6],
    [7, 6, 9, 6, INF]
]

cities = ["A", "B", "C", "D", "E"]

n = len(cost)

visited = [False] * n
best_cost = INF
best_path = []


def tsp(curr_city, count, curr_cost, path):
    global best_cost, best_path

    # Branch and Bound
    if curr_cost >= best_cost:
        return

    # All cities visited
    if count == n and cost[curr_city][0] != INF:
        total_cost = curr_cost + cost[curr_city][0]

        if total_cost < best_cost:
            best_cost = total_cost
            best_path = path[:] + [0]
        return

    # Try next city
    for next_city in range(n):
        if not visited[next_city] and cost[curr_city][next_city] != INF:
            visited[next_city] = True
            path.append(next_city)

            tsp(next_city,
                count + 1,
                curr_cost + cost[curr_city][next_city],
                path)

            visited[next_city] = False
            path.pop()


# Start from city A
visited[0] = True
tsp(0, 1, 0, [0])

# -------- Output --------

print("5-City TSP - Cost Matrix:\n")

print("     ", end="")
for city in cities:
    print(f"{city:>5}", end="")
print()

for i in range(n):
    print(f"{cities[i]:<5}", end="")
    for j in range(n):
        if cost[i][j] == INF:
            print(f"{'INF':>5}", end="")
        else:
            print(f"{cost[i][j]:>5}", end="")
    print()

print("\nOptimal Tour:", end=" ")

for i in range(len(best_path)):
    print(cities[best_path[i]], end="")
    if i != len(best_path) - 1:
        print(" -> ", end="")

print("\nMinimum Cost:", best_cost)

print("\nPath verification:")

total = 0
for i in range(len(best_path) - 1):
    u = best_path[i]
    v = best_path[i + 1]
    c = cost[u][v]
    total += c
    print(f"{cities[u]} -> {cities[v]}: cost = {c}")