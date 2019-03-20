from heapq import heappush, heappop

N = int(input())

graph = {i: list() for i in range(1, N + 1)}
count = {i: 0 for i in range(1, N + 1)}
time = dict()

for i in range(1, N + 1):
    inp = list(map(int, input().split()))
    time[i] = inp[0]

    for j in range(1, len(inp) - 1):
        graph[inp[j]].append(i)
        count[i] += 1


queue = list()
result = dict()
for i in range(1, N + 1):
    if count[i] == 0:
        heappush(queue, (time[i], i))

for _ in range(N):
    w, now = heappop(queue)
    result[now] = w

    for nxt in graph[now]:
        count[nxt] -= 1
        if count[nxt] == 0:
            heappush(queue,(w + time[nxt], nxt))

for i in range(1, N + 1):
    print(result[i])