# 깊이 위주 탐색
def dfs(now, index, ns):
    n1, n2, n3, n4 = ns
    # 만약 입력값 넘어가면 탐색 종료
    if index == c:
        r.append(now)
        return
    # +
    if n1 > 0:
        dfs(now + l[index], index + 1, (n1 - 1, n2, n3, n4))
    # -
    if n2 > 0:
        dfs(now - l[index], index + 1, (n1, n2 - 1, n3, n4))
    # *
    if n3 > 0:
        dfs(now * l[index], index + 1, (n1, n2, n3 - 1, n4))
    # //
    if n4 > 0:
        # C++식 나누기를 구현
        if now < 0:
            dfs(-1 * ((-1 * now) // l[index]), index + 1, (n1, n2, n3, n4 - 1))
        else:
            dfs(now // l[index], index + 1, (n1, n2, n3, n4 - 1))


r = list()
c = int(input())
l = list(map(int, input().split(' ')))

dfs(l[0], 1, map(int, input().split(' ')))
print(max(r))
print(min(r))
