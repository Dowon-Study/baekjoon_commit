
n = int(input())

answer = [[0] * n for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

x = 0
y = 0
direction = 0
count = 1

while count <= n*n:
    answer[x][y] = count
    count += 1
    
    nx =  x + dx[direction]
    ny = y + dy[direction]
    
    if nx < 0 or ny < 0 or nx >= n or ny >= n or answer[nx][ny] != 0:
        direction = (direction + 1) % 4 
        nx = x + dx[direction]
        ny = y + dy[direction]
    
    x = nx
    y = ny

print(answer)
