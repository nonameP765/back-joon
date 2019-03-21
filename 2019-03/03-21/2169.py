N, M = map(int, input().split())

dp = list()
ma = list()

dp.append([0 for i in range(M)])

for _ in range(N):
    ma.append(list(map(int, input().split())))


dp = list()

tmp = [ma[0][0]]
for i in range(M - 1):
    tmp.append(tmp[i] + ma[0][i + 1])

dp.append(tmp)

for i in range(1, N):
    tmp = [dp[i - 1][j] + ma[i][j] for j in range(M)]
    tmp1 = [tmp[0]]
    for j in range(M - 1):
        tmp1.append(max(tmp1[j] + ma[i][j + 1], tmp[j + 1]))
    tmp2 = [0] * (M - 1) + [tmp[-1]]
    for j in range(M - 1, 0, -1):
        tmp2[j - 1] = max(tmp2[j] + ma[i][j - 1], tmp[j - 1])
    for j in range(M):
        tmp[j] = max(tmp1[j], tmp2[j])
    dp.append(tmp)

print(dp[-1][-1])