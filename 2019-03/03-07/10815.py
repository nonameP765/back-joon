l_len = int(input())
l = list(map(int, input().split(' ')))
l.sort()


def search(h):
    left = 0
    right = l_len - 1
    mid = (left + right) // 2
    result = 0
    while True:
        if l[mid] == h:
            result = 1
            break
        elif l[mid] < h:
            left = mid + 1
        elif l[mid] > h:
            right = mid - 1
        mid = (left + right) // 2
        if left > right:
            break

    return result

input()
for i in map(int, input().split(' ')):
    print(search(i), end=' ')