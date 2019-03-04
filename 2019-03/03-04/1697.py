a, b = map(int, input().split(' '))

visited = [-1 for i in range(100002)]
visited[a] = 0
q = [a]

if a == b:
    print(0)
else:
    while q:
        now = q.pop(0)
        if now == b:
            print(visited[now])
            break
        if now * 2 < 100001:
            if visited[now * 2] == -1:
                visited[now * 2] = visited[now] + 1
                q.append(now * 2)
            else:
                visited[now * 2] = min(visited[now] + 1, visited[now * 2])
        if now + 1 <= 100001:
            if visited[now + 1] == -1:
                visited[now + 1] = visited[now] + 1
                q.append(now + 1)
            else:
                visited[now + 1] = min(visited[now] + 1, visited[now + 1])
        if 0 <= now - 1:
            if visited[now - 1] == -1:
                visited[now - 1] = visited[now] + 1
                q.append(now - 1)
            else:
                visited[now - 1] = min(visited[now] + 1, visited[now - 1])





