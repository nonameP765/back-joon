c = int(input())
h = int(input())

left = 1
right = h

while right >= left:
    count = 0
    mid = (left + right) // 2
    # 최소 높이만큼 더하기
    for i in range(1, c + 1):
        count += min(mid // i, c)
    if count < h:
        left = mid + 1
    else:
        r = mid
        right = mid - 1

print(r)
