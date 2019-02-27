stack = list()

n = input()
i = 0
stick = 0

result = 0

while True:
    if n[i:i + 2] == '()':
        result += stick
        i += 2
    elif n[i] == '(':
        stick += 1
        result += 1
        stack.append(0)
        i += 1
    elif n[i] == ')':
        stick -= 1
        stack.pop()
        i += 1

    if i == len(n):
        break

print(result)
