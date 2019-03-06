c = int(input())
l = [list(map(int, input().split(' '))) for i in range(c)]

visited = [[False for j in range(c)] for i in range(c)]

stack =