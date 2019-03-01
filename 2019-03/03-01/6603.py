# 깊이 위주 서치
def dfs(lis, index):
    # 남은 배열의 길이가 6번을 채울정도로 길지 않으면
    if 6 - len(lis) > len(a) - index:
        return
    # 만약 길이가 6이면
    if len(lis) == 6:
        print(' '.join(lis))
        return
    # 배열 복사
    tmp = lis[:]
    tmp.append(a[index])
    # 현재값 추가해서 넘기고
    dfs(tmp, index + 1)
    # 현재값 안추가해서 넘기고
    dfs(lis, index + 1)


while True:
    # .join을 쓰기 위해 문자열로서 처리
    a = input().split(' ')
    if a[0] == '0':
        break
    dfs([], 1)
    print()
