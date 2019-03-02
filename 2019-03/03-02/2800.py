s = input()

c = list()


def dfs(now, index, stack):
    if len(s) == index:
        if s == now or len(stack) != 0:
            return
        if not now in c:
            c.append(now)
            return
    elif s[index] == '(':
        dfs(now + s[index], index + 1, stack + [1])
        dfs(now, index + 1, stack + [0])
    elif s[index] == ')':
        if len(stack) == 0:
            return
        if stack[-1] == 0:
            dfs(now, index + 1, stack[:-1])
        if stack[-1] == 1:
            dfs(now + s[index], index + 1, stack[:-1])
    else:
        dfs(now + s[index], index + 1, stack)


dfs('', 0, [])
c.sort()
print('\n'.join(c))