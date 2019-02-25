a = int(input())

# dp용 배열
dp = [None, [1, 1]]

for i in range(2, a + 1):
    # 0으로 시작할떈 다음에 1로시작해도 되고 0으로 시작하도 되고
    # 1로 시작할땐 0으로만 시작해야함
    dp.append([sum(dp[i - 1]), dp[i - 1][0]])

# 이친수는 1로 시작하므로 1번쨰 배열값만 출력
print(dp[a][1])
