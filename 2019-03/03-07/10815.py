l_len = int(input())
l = list(map(int, input().split(' ')))
l.sort()


# 이분 탐색
def search(h):
    # 맨 왼쪽은 0
    left = 0
    # 맨 오른쪽은 끝값
    right = l_len - 1
    # 중간
    mid = (left + right) // 2
    result = 0
    while True:
        # 만약 중간값이 구할 값이면
        if l[mid] == h:
            # 1 리턴
            result = 1
            break
        # 만약 중간값이 구해야하는 값보다 작으면
        elif l[mid] < h:
            # 중간 + 1을 왼쪽으로
            left = mid + 1
        # 만약 중간값이 구해야하는 값보다 크면
        elif l[mid] > h:
            # 중간 - 1을 오른쪽으로
            right = mid - 1
        # 중간값 갱신
        mid = (left + right) // 2
        # 반목문 탈출
        if left > right:
            break

    return result


input()
for i in map(int, input().split(' ')):
    print(search(i), end=' ')
