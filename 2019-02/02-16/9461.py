# 7번쨰 이상부터 i-1, i-5의 합이라는 규칙이 있다.
# log 변수에 값을 저장해가며 계산한다.
log = [1, 1, 1, 2, 2, 3]

for i in range(int(input())):
    n = int(input())
    # 만약 아직 탐색되지 않은 곳이면 만듦
    for j in range(len(log), n+1):
        log.append(log[j-5] + log[j-1])
    print(log[n-1])
