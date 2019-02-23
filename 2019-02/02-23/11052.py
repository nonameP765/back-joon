a = int(input())
l = list(map(int, input().split(' ')))\

dp = [0, l[0]]

for i in range(2, a + 1):
    dp.append(max([dp[z+1] + dp[i - z - 1] for z in range(i//2)] + [l[i - 1]]))

print(dp[-1])
