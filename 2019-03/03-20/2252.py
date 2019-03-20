N, M = map(int, input().split())

graph = {i: {j: 0 for j in (1, N + 1)} for i in (1, N + 1)}
count = {i: 0 for i in (1, N + 1)}

for _ in M:
    a, b = map(int, input().split())
    graph[a][b] = True
    count += b

queue = list()
for i in range(1, N + 1):
    if count[i] == 0:
        queue.append(i)

for _ in range(N):
    now = queue.pop(0)

