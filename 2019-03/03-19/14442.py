N, M, K = map(int, input().split(' '))

INF = 1e9

ma = list()
for _ in range(N):
    ma.append(list(map(int, input())))

check = [[{i: INF for i in range(K + 1)} for _2 in range(M)] for _ in range(N)]
visited = [[{i: False for i in range(K + 1)} for _2 in range(M)] for _ in range(N)]

check[0][0][K] = 1

stack = [(0, 0)]

while stack:
    i, j = stack.pop(0)

    for k in range(K + 1):

        w = check[i][j][k]
        if w == INF:
            continue

        if visited[i][j][k]:
            continue

        visited[i][j][k] = True
        if i > 0:
            if ma[i - 1][j] == 1 and k > 0:
                if w + 1 < check[i - 1][j][k - 1]:
                    check[i - 1][j][k - 1] = w + 1
                    stack.append((i - 1, j))
            elif ma[i - 1][j] == 0:
                if w + 1 < check[i - 1][j][k]:
                    check[i - 1][j][k] = w + 1
                    stack.append((i - 1, j))
        if j > 0:
            if ma[i][j - 1] == 1 and k > 0:
                if w + 1 < check[i][j - 1][k - 1]:
                    check[i][j - 1][k - 1] = w + 1
                    stack.append((i, j - 1))
            elif ma[i][j - 1] == 0:
                if w + 1 < check[i][j - 1][k]:
                    check[i][j - 1][k] = w + 1
                    stack.append((i, j - 1))
        if i < N - 1:
            if ma[i + 1][j] == 1 and k > 0:
                if w + 1 < check[i + 1][j][k - 1]:
                    check[i + 1][j][k - 1] = w + 1
                    stack.append((i + 1, j))
            elif ma[i + 1][j] == 0:
                if w + 1 < check[i + 1][j][k]:
                    check[i + 1][j][k] = w + 1
                    stack.append((i + 1, j))
        if j < M - 1:
            if ma[i][j + 1] == 1 and k > 0:
                if w + 1 < check[i][j + 1][k - 1]:
                    check[i][j + 1][k - 1] = w + 1
                    stack.append((i, j + 1))
            elif ma[i][j + 1] == 0:
                if w + 1 < check[i][j + 1][k]:
                    check[i][j + 1][k] = w + 1
                stack.append((i, j + 1))

a = min(check[N - 1][M - 1].values())

print(-1 if a == INF else a)
