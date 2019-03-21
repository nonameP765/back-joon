N = int(input())

li = list(map(int, input().split()))

S = int(input())

li.sort()

left = 1

right = li[-1]

re = 0


while left <= right:
    mid = (left + right) // 2
    tmp = 0
    for i in li:
        if i < mid:
            tmp += i
        else:
            tmp += mid

    if tmp <= S:
        re = mid
        left = mid + 1

    if tmp > S:
        right = mid - 1

print(re)