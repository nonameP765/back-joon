c, r = map(int, input().split(' '))
l = list(map(int, input().split(' ')))
l.sort()

left = 0
right = l[-1]
re = 0
while left <= right:
    mid = (left + right) // 2
    count = 0
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