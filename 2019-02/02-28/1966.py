for i in range(int(input())):
    a, b = map(int, input().split(' '))
    # 프린터 큐
    q = [i for i in range(a)]
    # 랭킹 큐
    r = list(map(int, input().split(' ')))

    n = 0
    while True:
        # 랭킹이 높은놈일때
        if max(r) == r[0]:
            # 프린터 카운트 올라가고
            n += 1
            # 랭킹을 없애고
            r.pop(0)
            # 프린터가 입력값이랑 같으면 출력
            if b == q.pop(0):
                print(n)
                break
        # 랭킹이 높지 않을때
        else:
            # 둘 다 뒤로 넘김
            r.append(r.pop(0))
            q.append(q.pop(0))
