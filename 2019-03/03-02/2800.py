s = input()

c = list()


# 스택과 dfs를 동시에 사용
def dfs(now, index, stack):
    # 입력수열 이상으로 탐색하면 종료
    if len(s) == index:
        # 입력수열이랑 똑같으면 그냥 넘김, 완벽한수열이 아닐떄도 넘김
        if s == now or len(stack) != 0:
            return
        # 만약 중복이 아니면 추가
        if not now in c:
            c.append(now)
            return
    # 탐색한 문자가 ( 이면
    elif s[index] == '(':
        # ( 추가하고 스택에 1 추가해서 넘기고
        dfs(now + s[index], index + 1, stack + [1])
        # ( 추가 안하고 스택에 0 추가해서 넘김
        dfs(now, index + 1, stack + [0])
    # 탐색한 문자가 ) 이면
    elif s[index] == ')':
        # 스택 길이가 없을땐 불가능수열로 판단
        if len(stack) == 0:
            return
        # 바로 전 스택이 0이면
        if stack[-1] == 0:
            # 이번 탐색을 추가를 안함
            dfs(now, index + 1, stack[:-1])
        # 바로 전 스택이 1이면
        if stack[-1] == 1:
            # 이번 탐색을 추가함
            dfs(now + s[index], index + 1, stack[:-1])
    else:
        # 다른 문자열이면 평범하게 넘김
        dfs(now + s[index], index + 1, stack)


dfs('', 0, [])
c.sort()
print('\n'.join(c))
