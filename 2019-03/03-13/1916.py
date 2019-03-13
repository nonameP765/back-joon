from heapq import heappush, heappop

N = int(input())
M = int(input())

INF = 1e9

graph = {i: dict() for i in range(1, N + 1)}

for _ in range(M):
    n1, n2, n3 = map(int, input().split(' '))
    if graph[n1].get(n2, False):
        graph[n1][n2] = min(graph[n1][n2], n3)
    else:
        graph[n1][n2] = n3

start, end = map(int, input().split(' '))
check = {i: INF for i in range(1, N + 1)}
hq = list()
heappush(hq, (0, start))

while hq:
    w, now = heappop(hq)
    if now == end:
        break
    if check[now] < w:
        continue
    for i in graph[now].keys():
        w2 = graph[now][i] + w
        if w2 < check[i]:
            check[i] = w2
            heappush(hq, (w2, i))

print(check[end])