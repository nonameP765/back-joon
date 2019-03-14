from heapq import heappop, heappush

INF = 1e9

N, E = map(int, input().split(' '))

graph = {i: dict() for i in range(1, N + 1)}

for i in range(E):
    a, b, c = map(int, input().split(' '))
    if graph[a].get(b, False):
        graph[a][b] = min(c, graph[a][b])
    else:
        graph[a][b] = c
    if graph[b].get(a, False):
        graph[b][a] = min(c, graph[b][a])
    else:
        graph[b][a] = c

m1, m2 = map(int, input().split(' '))

# 우선순위 큐 탐색 구현
def hq_search(start, end):
    # 자기로 가는건 무조건 0
    if start == end:
        return 0
    check = {i: INF for i in range(1, N + 1)}
    hq = list()
    heappush(hq, (0, start))
    
    while hq:
        w, now = heappop(hq)

        if now == end:
            break
        if check[now] < w:
            continue

        for nxt in graph[now].keys():
            w2 = graph[now][nxt] + w
            if w2 < check[nxt]:
                check[nxt] = w2
                heappush(hq, (w2, nxt))
    
    return check[end]

# 시작 -> 거치는곳1 -> 거치는곳2 -> 마지막 과
# 시작 -> 거치는곳2 -> 거치는곳1 -> 마지막 을 비교해서
# 작은쪽을 출력하고, 경우의수가 없어서 INF먹어버린 경우는 -1 출력
re = min(hq_search(1, m1) + hq_search(m1, m2) + hq_search(m2, N),
          hq_search(1, m2) + hq_search(m2, m1) + hq_search(m1, N))
print(-1 if re >= INF else re)
        
        
    
