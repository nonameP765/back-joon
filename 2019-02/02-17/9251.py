b = input()
a = input()
lcs = [[0 for i in b]]
now = 0
for i in range(len(a)):
    tmp = [0 for z in b]

    for j in range(len(b)):

        if a[i] == b[j]:
            # 맨 앞이 아니면 왼쪽 위에 있는 값에 +1
            if not j == 0:
                tmp[j] = lcs[i][j-1] + 1
            # 맨 앞이면 그냥 1
            else:
                tmp[j] = 1
        else:
            # 맨 앞이 아니면 위 왼쪽 비교
            if not j == 0:
                tmp[j] = tmp[j - 1] if tmp[j - 1] > lcs[i][j] else lcs[i][j]
            # 맨 앞이면 위쪽
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
        # 문자도 같고 숫자도 탐색중이라면
        if lcs[r][i] == now and a[r] == b[i]:
            c = i - 1
            count += 1
            now -= 1
            break
    # 열 탐색 됬으면 한칸 올라감
    r -= 1
    if r == -1 or c == -1:
        break

print(count)

