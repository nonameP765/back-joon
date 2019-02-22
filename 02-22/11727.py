a = int(input())

dp = [0, 1, 3, 5]

for i in range(3, a):
    dp.append((dp[i] + dp[i-1] * 2) % 10007)

print(dp[a])


