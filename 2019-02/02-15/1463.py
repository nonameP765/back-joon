l = [[int(input())]]
# 전에 나왔던건 기록할 필요가 없음
his = set()

# 1이 나올때까지 돌림
while l[-1].count(1) == 0:
    tmp = list()
    for i in l[-1]:
        # 2로 나누어지고 예전에 나온적없으면 넣고
        if i % 2 == 0:
            n = i // 2
            if not n in his:
                his.add(n)
                tmp.append(n)
        # 3으로 나누어지고 예전에 나온적없으면 넣고
        if i % 3 == 0:
            n = i // 3
            if not n in his:
                his.add(n)
                tmp.append(n)
        # -1한 값이 예전에 나온적없으면 넣고
        if not i-1 in his:
            his.add(i-1)
            tmp.append(i-1)
    l.append(tmp)

print(len(l)-1)

