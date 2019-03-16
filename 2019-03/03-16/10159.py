from heapq import heappush, heappop

INF = 1e9

N = int(input())
M = int(input())

# 작은쪽 저장
graph1 = {i: list() for i in range(1, N + 1)}
# 큰쪽 저장
graph2 = {i: list() for i in range(1, N + 1)}

for _ in range(M):
    a, b = map(int, input().split(' '))
    graph1[a].append(b)
    graph2[b].append(a)


def search(p0):
    hq = list()
    visited = {i: False for i in range(1, N + 1)}
    heappush(hq, p0)
    # 작은쪽 쭉 탐색
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
    # 큰쪽 쭉 탐색
    while hq:
        now = heappop(hq)
        if visited[now]:
            continue
        visited[now] = True
        for nxt in graph2[now]:
            if not visited[nxt]:
                heappush(hq, nxt)
    re = 0
    # 방문을 못했으면 카운팅
    for i in range(1, N + 1):
        if not visited[i]:
            re += 1

    return re


for i in range(1, N + 1):
    print(search(i))
