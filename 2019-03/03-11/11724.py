c, n = map(int, input().split(' '))
graph = {i: list() for i in range(1, c + 1)}

for i in range(n):
    a, b = map(int, input().split(' '))
    graph[a].append(b)
    graph[b].append(a)

visited = [False for i in range(c + 1)]
count = 0


for j in range(1, c + 1):
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