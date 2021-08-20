#상하좌우
x,y = 1, 1 #시작 위치가 (1,1)
n = int(input())
plans = input().split()

#L, R, U, D에 따른 이동 방향
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move = ['L','R','U','D']

for i in plans:
    for j in range(len(move)):
        if i == move[j]:
            nx = x +dx[j]
            ny = y +dy[j]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny
print(x,y)
