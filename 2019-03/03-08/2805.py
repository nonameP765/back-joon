c, r = map(int, input().split(' '))
l = list(map(int, input().split(' ')))
l.sort()

# 나무의 길이는 0부터
left = 0
# 최고로 큰 나무까지 가능하다
right = l[-1]
re = 0
while left <= right:
    mid = (left + right) // 2
    count = 0
    # 탐색하는 중간값을 기준으로 나무를 자르고 저장
    for i in l:
        if i > mid:
            count += i - mid
    if count == r:
        re = mid
        break
    elif count < r:
        right = mid - 1
    elif count > r:
        re = mid
        left = mid + 1

print(re)