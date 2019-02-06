c = 0
for i in range(int(input()), 0, -1):
    if i < 100:
        c += 1
    elif i // 100 - i % 100 // 10 == i % 100 // 10 - i % 10:
        c += 1

print(c)
