from heapq import heappush, heappop

V, E = map(int, input().split(' '))

K = int(input())

graph = {i: list() for i in range(1, V + 1)}

for i in range(E):
    u, v, w = map(int, input().split(' '))
    graph[u].append((v, w))

check = {i: 'INF' for i in range(1, V + 1)}
check[K] = 0
pq = list()
heappush(pq, (0, K))

while pq:
    w, now = heappop(pq)

    if check[now] is not 'INF' and check[now] < w:
        continue

    for i, w in graph[now]:
        nc = w + check[now]
        if check[i] is 'INF' or nc < check[i]:
            check[i] = nc
            heappush(pq, (nc, i))

for i in range(1, V + 1):
    print(check[i])
