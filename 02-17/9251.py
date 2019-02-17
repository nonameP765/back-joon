b = input()
a = input()
lcs = [[0 for i in b]]
now = 0
for i in range(len(a)):
    tmp = [0 for z in b]

    for j in range(len(b)):

        if a[i] == b[j]:
            if not j == 0:
                tmp[j] = lcs[i][j-1] + 1
            else:
                tmp[j] = 1
        else:
            if not j == 0:
                tmp[j] = tmp[j - 1] if tmp[j - 1] > lcs[i][j] else lcs[i][j]
            else:
                tmp[j] = lcs[i][0]

    lcs.append(tmp)
lcs.pop(0)

# 세로
r = len(a) - 1
# 가로
c = len(b) - 1
# 탐색 횟수
count = 0
# 탐색중인 숫자
now = max(lcs[-1])
while True:
    for i in range(c, -1, -1):
        if lcs[r][i] == now and a[r] == b[i]:
            c = i - 1
            count += 1
            now -= 1
            break
    r -= 1

    if r == -1 or c == -1:
        break

print(count)

