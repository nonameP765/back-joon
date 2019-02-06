# 파도반 수열을 재귀로 구현
def pa_do_ban(p0):
    if p0 <= 3:
        return 1
    return pa_do_ban(p0 - 2) + pa_do_ban(p0 - 3)


for i in range(int(input())):
    print(pa_do_ban(int(input())))

