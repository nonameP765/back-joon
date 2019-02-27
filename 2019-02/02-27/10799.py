stack = list()

n = input()
i = 0
stick = 0

result = 0

while True:
    # 만약 바로 괄호가 성립하면 지금 스틱 개수만큼 조각개수에 추가
    if n[i:i + 2] == '()':
        result += stick
        # 두개를 넘어가야 하기 떄문에 +2
        i += 2
    # 만약 스틱의 시작이면
    elif n[i] == '(':
        # 스틱 개수에 1 더하고
        stick += 1
        # 조각에 스틱 처음부분이 더해지고
        result += 1
        # 스틱 시작부분을 스택에 추가
        stack.append(0)
        i += 1
    # 스틱의 끝이면
    elif n[i] == ')':
        # 스틱 개수 하나 줄어듬
        stick -= 1
        # 스틱 스택에서 제거
        stack.pop()
        i += 1

    if i == len(n):
        break

print(result)
