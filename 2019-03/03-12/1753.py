from heapq import heappush, heappop

V, E = map(int, input().split(' '))

K = int(input())

graph = {i: list() for i in range(1, V + 1)}

for i in range(E):
    u, v, w = map(int, input().split(' '))
    graph[u].append((v, w))

# 무한대를 이렇게 구현해보았다.
check = {i: 'INF' for i in range(1, V + 1)}
check[K] = 0
pq = list()
heappush(pq, (0, K))

# 우선순위 큐를 활용
while pq:
    w, now = heappop(pq)

    # 만약 지금까지 합해진 길이보다 기록된 길이가 짧으면 스킵
    if check[now] is not 'INF' and check[now] < w:
        continue

    for i, w in graph[now]:
        # 지금까지 기록된거 + 앞으로 진행할것이 이미 기록되어있는것보다 적으면
        nc = w + check[now]
        if check[i] is 'INF' or nc < check[i]:
            check[i] = nc
            # 새로이 큐에 추가
            heappush(pq, (nc, i))

for i in range(1, V + 1):
    print(check[i])
