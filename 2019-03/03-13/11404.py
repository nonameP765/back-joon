n = int(input())
m = int(input())

INF = 1e9

# 그래프
graph = {i: {j: INF for j in range(1, n + 1)} for i in range(1, n + 1)}

for _ in range(m):
    a, b, c = map(int, input().split(' '))

    # 똑같은 간선인 길이가 더 길어버리기~
    if graph[a].get(b, False):
        graph[a][b] = min(graph[a][b], c)
    else:
        graph[a][b] = c


# 3중 반복문으로 간선 체크
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        # 만약 자신이면 0
        if i == j:
            print(0, end=' ')
        else:
            print(graph[i][j] if graph[i][j] != INF else 0, end=' ')
    print()
