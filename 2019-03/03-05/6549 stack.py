while True:
    l = list(map(int, input().split(' ')))
    n = l[0]
    # 0이면 탈출
    if n == 0:
        break
    l = l[1:]
    mx = 0
    stack = [0]
    # 전체 탐색
    for i in range(1, n):
        # 스텍이 비어있지 않고, 탐색할 곳이 지금보다 클때
        while len(stack) != 0 and l[stack[-1]] > l[i]:
            # 맨 위의 값 출력
            tmp = stack.pop()
            # 만약 출력하고 스택이 비면
            if len(stack) != 0:
                w = i - stack[-1] - 1
            else:
                w = i
            # 넓이 비교
            mx = max(mx, l[tmp] * w)
        stack.append(i)
    # 트리거 전에 끝나면 끝쪽 처리
    while len(stack) != 0:
        tmp = stack.pop()
        if len(stack) != 0:
            w = n - stack[-1] - 1
        else:
            w = n
        mx = max(mx, l[tmp] * w)

    print(mx)
