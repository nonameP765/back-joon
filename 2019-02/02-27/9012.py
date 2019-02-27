for i in range(int(input())):
    s = input()
    stack = list()
    yes = True
    for j in range(len(s)):
        if j == 0:
            if s[0] == '(':
                stack.append(1)
            elif s[0] == ')':
                yes = False
                break
        else:
            if s[j] == '(':
                stack.append(1)

            elif s[j] == ')':
                if len(stack) == 0:
                    yes = False
                    break
                elif stack[-1] == 1:
                    stack.pop()
                else:
                    yes = False
                    break
    if yes and len(stack) == 0:
        print('YES')
    else:
        print('NO')

