l = [[int(input())]]
his = set()

while l[-1].count(1) == 0:
    tmp = list()
    for i in l[-1]:
        if i % 2 == 0:
            n = i // 2
            if not n in his:
                his.add(n)
                tmp.append(n)
        if i % 3 == 0:
            n = i // 3
            if not n in his:
                his.add(n)
                tmp.append(n)
        if not i-1 in his:
            his.add(i-1)
            tmp.append(i-1)
    l.append(tmp)

print(len(l)-1)

