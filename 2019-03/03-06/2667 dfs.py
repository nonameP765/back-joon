c = int(input())
l = [list(map(int, input())) for i in range(c)]

# dfs용 방문확인배열
visited = [[False for j in range(c)] for i in range(c)]

# 결과값 저장용
result = list()
for i in range(c):
    for j in range(c):
        # 2중 반복문으로 방문하지 않은 모든 점을 방문함
        # 만약 방문하지 않고, 집이 있다면
        if not visited[j][i] and l[j][i] == 1:
            # 현재 카운트
            count = 0
            # 스택으로 dfs탐색 시작
            stack = [(i, j)]
            while stack:
                a, b = stack.pop()
                # 방문하지 않았다면
                if not visited[b][a]:
                    # 집 개수 1 증가
                    count += 1
                    # 위아래좌우 값이 1인경우 스택에 추가
                    if 0 < a and l[b][a - 1] == 1:
                        stack.append((a - 1, b))
                    if 0 < b and l[b - 1][a] == 1:
                        stack.append((a, b - 1))
                    if a < c - 1 and l[b][a + 1] == 1:
                        stack.append((a + 1, b))
                    if b < c - 1 and l[b + 1][a] == 1:
                        stack.append((a, b + 1))
                    visited[b][a] = True
            result.append(count)
            visited[j][i] = True

result.sort()
print(len(result))
for i in result:
    print(i)
