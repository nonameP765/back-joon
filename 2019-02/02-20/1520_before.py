a, b = map(int, input().split(' '))
l = list()
for i in range(a):
    l.append(list(map(int, input().split(' '))))

# dp할 배열 만들기
success = [[None for i in range(b)] for j in range(a)]
# success 내 값을 사용해서 종점을 미리 표시
success[-1][-1] = 1


def s(i, j):
    # 첫번쨰 탐색이고, 종점이 아닐때
    if success[i][j] is None and not (i == a - 1 and j == b - 1):
        success[i][j] = 0

        # 상하좌우 탐색
        if j < b - 1 and l[i][j] > l[i][j + 1]:
            # 탐색
            s(i, j + 1)
            # 한 뒤에 저장된 결과값을 지금에 더함
            success[i][j] += success[i][j + 1]
        if i < a - 1 and l[i][j] > l[i + 1][j]:
            s(i + 1, j)
            success[i][j] += success[i + 1][j]
        if i > 0 and l[i][j] > l[i - 1][j]:
            s(i - 1, j)
            success[i][j] += success[i - 1][j]
        if j > 0 and l[i][j] > l[i][j - 1]:
            s(i, j - 1)
            success[i][j] += success[i][j - 1]


s(0, 0)
print(success[0][0])
