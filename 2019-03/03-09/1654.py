c, n = map(int, input().split(' '))
l = [int(input()) for i in range(c)]
l.sort()

# 1 이하로 자르면 큰일남 100% 런타임에러가 이 이유
left = 1
right = l[-1]
re = 0
# 이분탐색 시작
while left <= right:
    mid = (left + right) // 2
    su = 0
    # 현재 mid값으로 나눈 값 합
    for i in l:
        su += i // mid

    # 만약 자른 수가 원하는 수보다 많으면
    if n <= su:
        # 출력용 값 저장
        re = mid
        left = mid + 1
    else:
        right = mid - 1

print(re)
