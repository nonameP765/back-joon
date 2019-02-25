a = int(input())

dp = [None, [1 for i in range(10)]]

for i in range(2, a + 1):
    dp.append([sum(dp[i - 1][z:]) for z in range(10)])

print(sum(dp[a]) % 10007)