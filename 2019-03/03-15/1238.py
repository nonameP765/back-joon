from heapq import heappush, heappop

INF = 1e9

N, M, X = map(int, input().split(' '))

graph = {i: dict() for i in range(1, N + 1)}

for _ in range(M):
    a, b, c = map(int, input().split(' '))
    if graph[a].get(b, False):
        graph[a][b] = min(graph[a][b], c)
    else:
        graph[a][b] = c


# 우선순위 큐 구현
def search(start, end):
    hq = list()
    heappush(hq, (0, start))
    check = {i: INF for i in range(1, N + 1)}

    while hq:
        w, now = heappop(hq)
        if now == end:
            return check[end]
        if check[now] < w:
            continue
        for nxt in graph[now].keys():
            w2 = w + graph[now][nxt]
            if w2 < check[nxt]:
                check[nxt] = w2
                heappush(hq, (w2, nxt))


mx = 0

# i에서 X로 가는것, X에서 1에서 가는것이 왕복값
# 자신한테 가면 INF가 뜨므로 제외
for i in range(1, N + 1):
    if i == X:
        continue
    mx = max(search(i, X) + search(X, i), mx)

print(mx)
