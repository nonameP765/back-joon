from heapq import heappush, heappop

INF = 1e9

N, M = map(int, input().split(' '))

graph = {i: list() for i in range(1, N + 1)}

for _ in range(M):
    a, b = map(int, input().split(' '))
    graph[a].append(b)
    graph[b].append(a)


def search(start):
    hq = list()
    check = {i: INF for i in range(1, N + 1)}
    heappush(hq, (0, start))
    while hq:
        w, now = heappop(hq)
        if check[now] < w:
            continue
        for nxt in graph[now]:
            w2 = w + 1
            if w2 < check[nxt]:
                check[nxt] = w2
                heappush(hq, (w2, nxt))
    c = 0
    for i in range(1, N + 1):
        if i == start:
            continue
        c += check[i]
    return c


min_num = 1
min = search(1)
for i in range(2, N + 1):
    if min > search(i):
        min_num = i
        min = search(i)

print(min_num)