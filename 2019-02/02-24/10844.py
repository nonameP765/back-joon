a = int(input())

# dp용 배열 생성
dp = [None, [1 for i in range(10)]]

# 자리수마다 입력값까지 dp를 생성
for i in range(2, a + 1):
    # 0으로 시작하는 경우는 이전 결과의 0 + 1 값이 이전됨
    tmp = [dp[i - 1][1]]

    # 1~8으로 시작하는 경우는 이전 결과의 i + 1 값과 i - 1 값의 합이 이전됨
    for j in range(1, 9):
        tmp.append(dp[i - 1][j - 1] + dp[i - 1][j + 1])

    # 9로 시작하는 경우는 이전 결과의 9 - 1 값이 이전됨
    tmp.append(dp[i - 1][8])
    dp.append(tmp)

# 0으로 시작하는 수는 없으므로 1번쨰 값부터 끝까지 계산
print(sum(dp[a][1:]) % 1000000000)
