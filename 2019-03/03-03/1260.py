d, c, r = map(int, input().split(' '))


graph = dict()
for i in range(1, d+1):
    graph[i] = list()

for i in range(c):
    a, b = map(int, input().split(' '))
    graph[a].append(b)
    graph[b].append(a)

for i in range(d):
    graph[i+1].sort()

# dfs
stack = [r]
visited = [False for i in range(d + 1)]

while stack:
    now = stack.pop()
    if not visited[now]:
        visited[now] = True
        print(now, end=' ')
    tmp = graph[now][:]
    tmp.sort(reverse=True)
    for i in tmp:
        if not visited[i]:
            stack.append(i)

print()
# bfs
q = [r]
visited = [False for i in range(d + 1)]

while q:
    now = q.pop(0)
    if not visited[now]:
        visited[now] = True
        print(now, end=' ')
    tmp = graph[now][:]
    tmp.sort()
    for i in tmp:
        if not visited[i]:
            q.append(i)