from heapq import heappop, heappush

INF = 1e9

N, M = map(int, input().split(' '))

graph = {i: list() for i in range(1, N + 1)}

for _ in range(M):
    a, b = map(int, input().split(' '))
    # 왠지 순서대로 처리해야할거 같아서 힙 썼는데 필요없...
    heappush(graph[a], b)
    heappush(graph[b], a)

check = {i: INF for i in range(1, N + 1)}

# 우선순위 큐 구현
hq = list()
heappush(hq, (0, 1))

# 높은 값
mx = 0
# 높은 위치
mxn = 0
# 높은 위치들
# 중복되지 않게 하려고 집합으로 구현
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