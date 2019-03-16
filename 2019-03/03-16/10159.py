from heapq import heappush, heappop

INF = 1e9

N = int(input())
M = int(input())

graph1 = {i: list() for i in range(1, N + 1)}
graph2 = {i: list() for i in range(1, N + 1)}

for _ in range(M):
    a, b = map(int, input().split(' '))
    graph1[a].append(b)
    graph2[b].append(a)


def search(p0):
    hq = list()
    visited = {i: False for i in range(1, N + 1)}
    heappush(hq, p0)

    while hq:
        now = heappop(hq)
        if visited[now]:
            continue
        visited[now] = True
        for nxt in graph1[now]:
            if not visited[nxt]:
                heappush(hq, nxt)

    heappush(hq, p0)
    visited[p0] = False
    while hq:
        now = heappop(hq)
        if visited[now]:
            continue
        visited[now] = True
        for nxt in graph2[now]:
            if not visited[nxt]:
                heappush(hq, nxt)
    re = 0
    for i in range(1, N + 1):
        if not visited[i]:
            re += 1

    return re


for i in range(1, N + 1):
    print(search(i))
