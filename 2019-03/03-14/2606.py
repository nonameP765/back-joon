N = int(input())
M = int(input())

graph = {i: list() for i in range(1, N + 1)}

for _ in range(M):
    a, b = map(int, input().split(' '))
    # 양방향임 이거때문에 몇번 재채점함
    graph[a].append(b)
    graph[b].append(a)

check = {i: False for i in range(1, N + 1)}

# bfs 구현 이게 왜 최단거리?
# 플로이드 와샬 쓰면 n^3인데..
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
