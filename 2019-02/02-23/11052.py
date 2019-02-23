a = int(input())
l = list(map(int, input().split(' ')))

# dp용 배열
dp = [0, l[0]]

for i in range(2, a + 1):
    # 이전까지의 계산결과를 dp에 저장하고
    # l[i] 와 (여기선 한칸씩 앞으로 되있으니까 i - 1로 코딩)
    # dp[1] + dp[i - 1], dp[2] + dp[i - 2].... 을 비교해서 가장 큰걸 dp[i]로 넣는다.
    dp.append(max([dp[z+1] + dp[i - z - 1] for z in range(i//2)] + [l[i - 1]]))
print(dp[-1])
