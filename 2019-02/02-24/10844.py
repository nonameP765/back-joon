a = int(input())


dp = [None, [1 for i in range(10)]]

for i in range(2, a + 1):
    tmp = [dp[i - 1][1]]

    for j in range(1, 9):
        tmp.append(dp[i - 1][j - 1] + dp[i - 1][j + 1])

    tmp.append(dp[i - 1][8])
    dp.append(tmp)

print(sum(dp[a][1:])%1000000000)
