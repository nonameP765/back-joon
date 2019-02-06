n = input()


# 자리수 합 구하는 재귀함수
def sum_digit(p0):
    if p0 == 0:
        return 0
    return p0 % 10 + sum_digit(p0 // 10)


# 입력받은 숫자 - 자릿수 * 9 ~ 입력받은 숫자 까지 탐색
for i in range(int(n) - len(n) * 9, int(n)):
    if int(n) == i + sum_digit(i):
        print(i)
        break
else:  # 탐색된게 없으면 0
    print(0)
