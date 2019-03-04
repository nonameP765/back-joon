a, b = map(int, input().split(' '))

# 단순 방문 확인용
visited = [False for i in range(100002)]
q = [a]

count = 0

while q:
    # 만약 지금 큐에 결과값이 있으면
    if b in q:
        print(count)
        break
    # 그냥 반복문 돌리면 실사간으로 줄어들어서..?
    l = len(q)
    # 큐 길이만큼 반복
    for _ in range(l):
        # 앞에있는 값 뺌
        now = q.pop(0)
        # 전부 한계가 안넘고 방문하지 않았다면 추가
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




