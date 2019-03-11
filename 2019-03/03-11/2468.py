c = int(input())

l = [list(map(int, input().split(' '))) for i in range(c)]

# 0부터 최대값까지 탐색해보기 위해 구함
m = 0
for i in range(c):
    for j in range(c):
        m = max(m, l[i][j])

# 결과값
mx = 0

# 0부터 최대값까지 탐색
for k in range(m + 1):
    visited = [[False for j in range(c)] for i in range(c)]
    n = 0
    for i in range(c):
        for j in range(c):
            if not visited[i][j]:
                # 만약 탐색중인 수보다 크면 DFS
                if l[i][j] > k:
                    stack = [(i, j)]
                    # 대피소? 영역 1씩 추가
                    n += 1
                    while stack:
                        a, b = stack.pop()
                        visited[a][b] = True
                        if a > 0 and not visited[a - 1][b] and l[a - 1][b] > k:
                            stack.append((a - 1, b))
                        if b > 0 and not visited[a][b - 1] and l[a][b - 1] > k:
                            stack.append((a, b - 1))
                        if a < c - 1 and not visited[a + 1][b] and l[a + 1][b] > k:
                            stack.append((a + 1, b))
                        if b < c - 1 and not visited[a][b + 1] and l[a][b + 1] > k:
                            stack.append((a, b + 1))

                else:
                    visited[i][j] = True

    mx = max(mx, n)

print(mx)
