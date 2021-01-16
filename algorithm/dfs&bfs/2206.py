from collections import deque

n, m = map(int, input().split())

graph = [list(map(int, input())) for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
third = [[[-1]*2 for _ in range(m) ] for _ in range(n)] #거리를 담는다

def bfs():
    q = deque()
    q.append([0,0,0])
    third[0][0][0] = 1
    while q:
        x, y, z = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny] == 0 and third[nx][ny][z] == -1: #벽 안 뿌숨
                    third[nx][ny][z] = third[x][y][z] +1
                    q.append([nx, ny, z])
                elif z == 0 and graph[nx][ny] == 1 and third[nx][ny][z+1] == -1:
                    third[nx][ny][z+1] = third[x][y][z] +1
                    q.append([nx, ny, z+1])


bfs()

ans1, ans2 = third[n-1][m-1][0], third[n-1][m-1][1]

if ans1 == -1 and ans2 != -1:
    print(ans2)
elif ans1 != -1 and ans2 == -1:
    print(ans1)
else:
    print(min(ans1, ans2))