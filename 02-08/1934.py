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
visited = [r]
to_visit = [r]

while to_visit:
    now = to_visit.pop()
    for i in (set(graph[now])-set(visited)):
        visited.append(i)
        to_visit.append(i)
        break
for i in visited:
    print(i, end=' ')
print()
# bfs
visited = [False for i in range(d)]
visited[r-1] = True
to_visit = [r]

while to_visit:
    now = to_visit.pop(0)
    print(now, end=' ')
    for i in graph[now]:
        if not visited[i - 1]:
            visited[i - 1] = True
            to_visit.append(i)
