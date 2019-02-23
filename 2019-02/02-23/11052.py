a = int(input())
l = list(map(int, input().split(' ')))\

dp = [0, l[0]]

for i in range(2, a + 1):
    dp.append(max([dp[z] + dp[i - z] for z in range(1, i)] + [l[i - 1]]))

print(dp[-1])
