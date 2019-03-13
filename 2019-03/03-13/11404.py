n = int(input())
m = int(input())

INF = 1e9

graph = {i: {j: INF for j in range(1, n + 1)} for i in range(1, n + 1)}

for _ in range(m):
    a, b, c = map(int, input().split(' '))

    if graph[a].get(b, False):
        graph[a][b] = min(graph[a][b], c)
    else:
        graph[a][b] = c


for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            print(0, end=' ')
        else:
            print(graph[i][j] if graph[i][j] != INF else 0, end=' ')
    print()
