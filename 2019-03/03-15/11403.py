c = int(input())

graph = [list(map(int, input().split(' '))) for _ in range(c)]

for k in range(c):
    for i in range(c):
        for j in range(c):
            graph[i][j] = 1 if graph[i][j] == 1 or graph[i][k] == graph[k][j] == 1 else 0

for i in range(c):
    for j in range(c):
        print(graph[i][j], end=' ')
    print()