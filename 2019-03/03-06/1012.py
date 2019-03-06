for _ in range(int(input())):
    w, h, n = map(int, input().split(' '))
    l = [[0 for j in range(w)] for i in range(h)]
    visited = [[False for j in range(w)] for i in range(h)]
    for i in range(n):
        a, b = map(int, input().split(' '))
        l[b][a] = 1
    count = 0
    for i in range(h):
        for j in range(w):
            if not visited[i][j] and l[i][j] == 1:
                count += 1
                stack = [(i, j)]
                while stack:
                    a, b = stack.pop()
                    if not visited[a][b]:
                        if 0 < a and l[a - 1][b] == 1:
                            stack.append((a - 1, b))
                        if 0 < b and l[a][b - 1] == 1:
                            stack.append((a, b - 1))
                        if a < h - 1 and l[a + 1][b] == 1:
                            stack.append((a + 1, b))
                        if b < w - 1 and l[a][b + 1] == 1:
                            stack.append((a, b + 1))
                        visited[a][b] = True
                visited[i][j] = True
    print(count)