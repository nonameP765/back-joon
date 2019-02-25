a = int(input())

# dp용 배열
dp = [None, [1 for i in range(10)]]

for i in range(2, a + 1):
    # 높은 index의 값을 다 더해서 저장
    dp.append([sum(dp[i - 1][z:]) for z in range(10)])

print(sum(dp[a]) % 10007)