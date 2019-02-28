q = [i + 1 for i in range(int(input()))]

while len(q) != 1:
    q.pop(0)
    q.append(q.pop(0))

print(q[0])