a, b = map(int, input().split(' '))

visited = [False for i in range(100002)]
q = [a]

count = 0

while q:
    if b in q:
        print(count)
        break
    l = len(q)
    for _ in range(l):
        now = q.pop(0)
        if now * 2 < 100001 and not visited[now * 2]:
            q.append(now * 2)
            visited[now * 2] = True
        if now + 1 <= 100001 and not visited[now + 1]:
            q.append(now + 1)
            visited[now + 1] = True

        if 0 <= now - 1 and not visited[now - 1]:
            q.append(now - 1)
            visited[now - 1] = True
    count += 1




