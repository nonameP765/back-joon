V, E = map(int, input().split(' '))

K = int(input())

graph = {i: dict() for i in range(1, V + 1)}

for i in range(E):
    u, v, w = map(int, input().split(' '))
    graph[u][v] = w

check = {i: 'INF' for i in range(1, V + 1)}
visited = [i for i in range(1, V + 1)]
check[K] = 0
pq = [(K, 0)]

while pq:
    print(pq)
    now, w = pq.pop(0)

    if check[now] is not None and check[now] < w:
        continue

    for i in graph[now].keys():
        nc = graph[now][i] + check[now]
        if check[i] is 'INF' or nc < check[i]:
            check[i] = nc
            pq.append((i, check[i]))

for i in range(1, V + 1):
    print(check[i])
