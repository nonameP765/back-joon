a = int(input())

dp = [0, 1, 2]

for i in range(2, a):
    dp.append((dp[i] + dp[i-1]) % 10007)

print(dp[a])


