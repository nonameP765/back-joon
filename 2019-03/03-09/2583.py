h, w, c = map(int, input().split(' '))
l = [[0 for j in range(w)]for i in range(h)]
visited = [[False for j in range(w)]for i in range(h)]

# 2차원 배열 생성 솔직히 위아래 뒤집혀도 상관없음
for i in range(c):
    w1, h1, w2, h2 = map(int, input().split(' '))
    for j in range(h1, h2):
        for k in range(w1, w2):
            l[j][k] = 1

re = list()

for j in range(h):
    for i in range(w):
        if not visited[j][i]:
            # 0을 기준으로 탐색
            if l[j][i] == 0:
                count = 0
                stack = [(j, i)]
                while stack:

                    j, i = stack.pop()
                    if not visited[j][i]:
                        visited[j][i] = True
                        count += 1
                        if j > 0 and not visited[j - 1][i] and l[j - 1][i] == 0:
                            stack.append((j - 1, i))
                        if i > 0 and not visited[j][i - 1] and l[j][i - 1] == 0:
                            stack.append((j, i - 1))
                        if j < h - 1 and not visited[j + 1][i] and l[j + 1][i] == 0:
                            stack.append((j + 1, i))
                        if i < w - 1 and not visited[j][i + 1] and l[j][i + 1] == 0:
                            stack.append((j, i + 1))

                re.append(count)
            visited[j][i] = True

re.sort()
print(len(re))
for i in re:
    print(i, end=' ')
