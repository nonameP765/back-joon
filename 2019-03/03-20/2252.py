N, M = map(int, input().split())

graph = {i: list() for i in range(1, N + 1)}
count = {i: 0 for i in range(1, N + 1)}

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    count[b] += 1

queue = list()
for i in range(1, N + 1):
    if count[i] == 0:
        queue.append(i)

result = ''
for _ in range(N):
    now = queue.pop(0)
    result += str(now) + ' '
    for nxt in graph[now]:
        count[nxt] -= 1
        if count[nxt] == 0:
            queue.append(nxt)

print(result)


