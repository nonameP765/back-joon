a = int(input())

# 점화식은 a[n] = a[n - 1] + a[n - 2] * 2 이다
# 새로 놓여질 블럭이 세로로 세워지면 a[n - 1]의 경우의수,
# 새로 놓여질 블럭이 앞에 블럭과 가로로 세워지면 2칸 전인 a[n - 2]의 경우의수,
# 새로 놓여질 블럭이 앞에 블럭 합쳐져 2x2가 된다면 2칸 전인 a[n - 2]의 경우의수가 된다.
dp = [0, 1, 3, 5]

for i in range(3, a):
    dp.append((dp[i] + dp[i-1] * 2) % 10007)

print(dp[a])

