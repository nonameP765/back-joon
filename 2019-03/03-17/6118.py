from heapq import heappop, heappush

INF = 1e9

N, M = map(int, input().split(' '))

graph = {i: list() for i in range(1, N + 1)}

for _ in range(M):
    a, b = map(int, input().split(' '))
    heappush(graph[a], b)
    heappush(graph[b], a)

check = {i: INF for i in range(1, N + 1)}

hq = list()
heappush(hq, (0, 1))

mx = 0
mxn = 0
mxc = set()
while hq:
    w, now = heappop(hq)

    if check[now] <= w:
        continue

    check[now] = w

    if w > mx:
        mx = w
        mxn = now
        mxc = set()

    if w == mx:
        mxc.add(now)

    for nxt in graph[now]:
        if check[nxt] > w + 1:
            heappush(hq, (w + 1, nxt))

print(mxn, mx, len(mxc))