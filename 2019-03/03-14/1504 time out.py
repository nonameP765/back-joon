from heapq import heappop, heappush

INF = 1e9

N, E = map(int, input().split(' '))

graph = {i: {j: INF for j in range(1, N + 1)} for i in range(1, N + 1)}

for i in range(E):
    a, b, c = map(int, input().split(' '))
    if graph[a].get(b, False):
        graph[a][b] = min(c, graph[a][b])
    else:
        graph[a][b] = c
    if graph[b].get(a, False):
        graph[b][a] = min(c, graph[b][a])
    else:
        graph[b][a] = c

m1, m2 = map(int, input().split(' '))


for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            graph[i][j] = min(graph[i][j], graph[k][j] + graph[i][k])

print(min(graph[1][m1] + graph[m1][m2] + graph[m2][N],
          graph[1][m2] + graph[m2][m1] + graph[m1][N]))
