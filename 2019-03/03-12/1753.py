V, E = map(int, input().split(' '))

K = int(input())

graph = {i: [] for i in range(1, V + 1)}

for i in range(E):
    u, v, w = map(int, input().split(' '))
    graph[u].append((v, w))

check = {i: 'INF' for i in range(1, V + 1)}
visited = {i: False for i in range(1, V + 1)}
check[K] = 0

queue = [K]

while queue:
    now = queue.pop(0)
    visited[now] = True
    for i, w in graph[now]:
        if not visited[i]:
            queue.append(i)
            if check[i] is 'INF':
                check[i] = w + check[now]
            else:
                check[i] = min(w + check[now], check[i])

for i in range(1, V + 1):
    print(check[i])

