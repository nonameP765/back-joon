V, E = map(int, input().split(' '))

K = int(input())

graph = {i: dict() for i in range(1, V + 1)}

for i in range(E):
    u, v, w = map(int, input().split(' '))
    graph[u][v] = w

check = {i: 'INF' for i in range(1, V + 1)}
visited = [i for i in range(1, V + 1)]
check[K] = 0

while True:
    mi_num = None
    mi = None
    for i in range(len(visited)):
        if check[visited[i]] is not 'INF':
            if not mi:
                mi_num = i
                mi = check[visited[i]]
            if mi_num >= check[visited[i]]:
                mi_num = i
                mi = check[visited[i]]

    if mi_num is None:
        break
    now = visited[mi_num]
    visited.pop(mi_num)

    for i in graph[now].keys():
        if check[i] is 'INF':
            check[i] = graph[now][i] + check[now]
        else:
            check[i] = min(graph[now][i] + check[now], check[i])

for i in range(1, V + 1):
    print(check[i])
