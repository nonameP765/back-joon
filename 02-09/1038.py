c = int(input())

# 9까진 그냥 입력값이 답(이거때문에 1시간 낭비함)
if c < 10:
    print(c)
# 1022번째 9876543210이후 감소하는 수는 없음
elif 1023 <= c:
    print(-1)
else:
    # 지금 몇번쨰 탐색인지
    count = 9
    # 현재 숫자
    num = 10
    # 거듭제곱된 10의 배수들 미리 저장
    w = [10 ** i for i in range(10)]
    while True:
        # 따로 지금 수 저장
        now = num
        # 1의자리수
        first = now % 10

        # 연속이 끝나는 자리수
        digit = 0

        while True:
            # 연속이 끝나면 탈출
            if now % 10 != first + digit:
                break
            # 10씩 나누며 연속되는지 확인
            digit += 1
            now //= 10
        # 탐색횟수 +1
        count += 1
        # 입력값이랑 횟수랑 같으면 출력
        if count == c:
            print(num)
            break
        # 연속이 안된경운 그냥 1더하면 됨
        if digit <= 1:
            num += 1
        # 연속인 경우
        else:
            # 맨 앞자리가 9라면 자리수 변경이 일어남
            if num // w[digit - 1] == 9:
                num = 0
                # ex) 자리수 3인경우의 최소인 감소하는 수는 210
                for i in range(digit + 1):
                    num += i * (10 ** i)
            # 아닌경우
            else:
                # ex) 여기서 num이 76321 이라면
                # digit = 3 이고
                # digit - 1 번째 자리수, 100의자리수를 1 더해주고 그 및 자리수를 최소로 채움
                # 76321 + 100 -> 76400 + 10 -> 76410
                num = num + w[digit - 1] - num % w[digit - 1]
                for i in range(digit - 1):
                    num += i * (10 ** i)
