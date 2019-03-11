c, n = map(int, input().split(' '))
# 그래프 제작
graph = {i: list() for i in range(1, c + 1)}

for i in range(n):
    a, b = map(int, input().split(' '))
    graph[a].append(b)
    graph[b].append(a)

visited = [False for i in range(c + 1)]
count = 0

# 모든 정점을 순환
for j in range(1, c + 1):
    # 물론 방문하지 않은 경우만
    if not visited[j]:
        stack = [j]

        while stack:
            now = stack.pop()
            visited[now] = True

            for i in graph[now]:
                if not visited[i]:
                    stack.append(i)

        count += 1

print(count)