a = int(input())

dp = [None, [1, 1]]

for i in range(2, a + 1):
    dp.append([sum(dp[i - 1]), dp[i - 1][0]])

print(dp[a][1])
