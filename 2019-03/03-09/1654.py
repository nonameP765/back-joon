c, n = map(int, input().split(' '))
l = [int(input()) for i in range(c)]
l.sort()

left = 1
right = l[-1]
re = 0
while left <= right:
    mid = (left + right) // 2
    su = 0
    for i in l:
        su += i // mid

    if n <= su:
        re = mid
        left = mid + 1
    else:
        right = mid - 1

print(re)
