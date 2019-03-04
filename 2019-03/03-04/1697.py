a, b = map(int, input().split(' '))

# 카운터 저장용
visited = [-1 for i in range(100002)]
# 첫번째 카운터는 0
visited[a] = 0
# 큐에 넣기
q = [a]


while q:
    # 앞쪽 값을 뺴옴
    now = q.pop(0)
    # 결과값이랑 같으면 출력
    if now == b:
        print(visited[now])
        break
    # 지금값에 2배한게 한계를 안넘으면
    if now * 2 < 100001:
        # 만약 탐색된적이 없다면
        if visited[now * 2] == -1:
            # 카운터를 저장
            visited[now * 2] = visited[now] + 1
            # 큐에 삽입
            q.append(now * 2)
        # 탐색되었었다면
        else:
            # 카운터가 적은쪽을 넣음
            visited[now * 2] = min(visited[now] + 1, visited[now * 2])
    # 지금값에 +1 한게 한계를 안넘으면 위와같이
    if now + 1 <= 100001:
        if visited[now + 1] == -1:
            visited[now + 1] = visited[now] + 1
            q.append(now + 1)
        else:
            visited[now + 1] = min(visited[now] + 1, visited[now + 1])
    # 지금값에 -1 한게 음수가 안되면 위와같이
    if 0 <= now - 1:
        if visited[now - 1] == -1:
            visited[now - 1] = visited[now] + 1
            q.append(now - 1)
        else:
            visited[now - 1] = min(visited[now] + 1, visited[now - 1])





