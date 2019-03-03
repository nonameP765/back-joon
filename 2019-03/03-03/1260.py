d, c, r = map(int, input().split(' '))

# 그래프 만들기
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
# 스택을 활용함
stack = [r]
visited = [False for i in range(d + 1)]

while stack:
    # 맨 뒷값만 사용
    now = stack.pop()
    if not visited[now]:
        visited[now] = True
        print(now, end=' ')
    # 거꾸로 정렬해서 넣어야함
    tmp = graph[now][:]
    tmp.sort(reverse=True)
    for i in tmp:
        if not visited[i]:
            stack.append(i)

print()
# bfs
# 큐를 활용함
q = [r]
visited = [False for i in range(d + 1)]

while q:
    # 맨 앞값만 사용
    now = q.pop(0)
    if not visited[now]:
        visited[now] = True
        print(now, end=' ')
    # 정렬햇 넣어야함
    tmp = graph[now][:]
    tmp.sort()
    for i in tmp:
        if not visited[i]:
            q.append(i)
