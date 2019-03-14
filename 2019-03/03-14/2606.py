N = int(input())
M = int(input())

graph = {i: list() for i in range(1, N + 1)}

for _ in range(M):
    a, b = map(int, input().split(' '))
    graph[a].append(b)
    graph[b].append(a)

check = {i: False for i in range(1, N + 1)}

q = [1]
count = 0

while q:
    now = q.pop(0)
    if check[now]:
        continue
    check[now] = True
    if now != 1:
        count += 1
    for i in graph[now]:
        if not check[i]:
            q.append(i)

print(count)
