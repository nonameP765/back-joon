a, b = map(int, input().split(' '))
l = list()
for i in range(a):
    l.append(list(map(int, input().split(' '))))

# dp할 배열 생성
success = [[None for i in range(b)] for j in range(a)]


def s(i, j):
    # 이부분도 중요함 여길 안막으면 종점에 가서도 역으로 재탐색함(이거도 애매했음)
    if i == a - 1 and j == b - 1:
        return 1
    # 이미 탐색 됬다면(None 이 아니니까) 그냥 리턴
    if success[i][j] is not None:
        return success[i][j]

    # 탐색 시작시 초기화
    success[i][j] = 0

    # 상하좌우 전부로 움직일 수 있음(이거때문에 계속 틀림)
    if j < b - 1 and l[i][j] > l[i][j + 1]:
        success[i][j] += s(i, j + 1)
    if j > 0 and l[i][j] > l[i][j - 1]:
        success[i][j] += s(i, j - 1)
    if i < a - 1 and l[i][j] > l[i + 1][j]:
        success[i][j] += s(i + 1, j)
    if i > 0 and l[i][j] > l[i - 1][j]:
        success[i][j] += s(i - 1, j)

    return success[i][j]


print(s(0, 0))
