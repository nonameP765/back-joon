node_list = dict()
parent = dict()
c = int(input())

# 그래프 제작
for i in range(c):
    node_list[i + 1] = list()
for i in range(c - 1):
    a, b = input().split(' ')
    node_list[int(a)].append(int(b))
    node_list[int(b)].append(int(a))

# 지나간건 True 안지나간건 False
visited = [False for i in range(c)]
# 1부터 지나감
to_visit = [1]

while to_visit:
    # dfs로 구현하기 위해 맨뒤의 값을 사출
    now = to_visit.pop()
    # 그 값과 연결된 자식+부모를 반복문으로 돔
    for i in node_list[now]:
        # 방문 안한게 걸리면 방문
        if not visited[i-1]:
            # 자식과 부모 저장
            parent[i] = now
            visited[i-1] = True
            to_visit.append(i)

# 출~력
for i in range(2, c + 1):
    print(parent[i])
