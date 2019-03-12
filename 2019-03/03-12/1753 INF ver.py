from heapq import heappush, heappop
from sys import stdin, stdout
input = stdin.readline
print = stdout.write

INF = 1e9
V, E = map(int, input().split())
K = int(input()) - 1
check = [INF for i in range(V)]
graph = [[] for i in range(V)]
for i in range(E):
    u, v, w = map(int, input().split())
    graph[u - 1].append([v - 1, w])

hq = []
heappush(hq, (0, K))
check[K] = 0
while hq:
    w, now = heappop(hq)
    if check[now] < w:
        continue
    for i, w2 in graph[now]:
        w2 += w
        if w2 < check[i]:
            check[i] = w2
            heappush(hq, (w2, i))

for i in range(V):
    print("%d\n" % check[i] if check[i] != INF else 'INF\n')
