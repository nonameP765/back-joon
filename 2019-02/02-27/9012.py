for i in range(int(input())):
    s = input()
    stack = list()
    yes = True
    for j in range(len(s)):
        # 첫번쨰일때
        if j == 0:
            # 여는 괄호면 1 추가
            if s[0] == '(':
                stack.append(1)
            # 닫는 괄호면 NO
            elif s[0] == ')':
                yes = False
                break
        # 그 다음에
        else:
            # 여는 괄호면 1 추가
            if s[j] == '(':
                stack.append(1)
            # 닫는 괄호면 stack에 여는 괄호가 있으면 그걸 제거
            # 만약에 없으면 NO
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

