a, b = map(int, input().split(' '))
l = list(map(int, input().split(' ')))

c = 0


# 깊이 위주 서치
def dfs(now, index):
    global c
    # 배열 길이보다 더 텀색할순 없으니
    if index == a:
        return
    # 만약 합이 제시된것과 같으면
    if now + l[index] == b:
        # 카운터 추가
        c += 1

    # 현재값에서 서치된곳의 값을 합치고 넘기고
    dfs(now + l[index], index + 1)
    # 현재값에서 서치된곳의 값을 안 합치고 넘기고
    dfs(now, index + 1)


dfs(0, 0)

print(c)
