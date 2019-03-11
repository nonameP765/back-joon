c = int(input())

l = [list(map(int, input().split(' '))) for i in range(c)]

l2 = set()
mi = l[0][0]
ma = l[0][0]
m = 0
for i in range(c):
    for j in range(c):
        m = max(m, l[i][j])

l2 = range
mx = 0
mx_num = 0


for k in range(m + 1):
    visited = [[False for j in range(c)] for i in range(c)]
    n = 0
    for i in range(c):
        for j in range(c):
            if not visited[i][j]:
                if l[i][j] > k:
                    stack = [(i, j)]
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
