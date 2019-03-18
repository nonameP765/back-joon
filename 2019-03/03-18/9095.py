dp = [1, 2, 4]

for _ in range(int(input())):
    n = int(input())

    for i in range(len(dp) - 1, n - 1):
        dp.append(dp[i] + dp[i - 1] + dp[i - 2])

    print(dp[n - 1])
