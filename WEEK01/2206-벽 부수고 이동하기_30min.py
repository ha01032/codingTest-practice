import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int,input().strip().split())

MAP = []
WALL = []

for y in range(N):
    MAP.append(list(map(int, input().strip().split())))
    for x in range(M):
        if MAP[y][x] == 1: WALL.append((y,x))


arrive = False
minTime = N*M
#하나씩 벽 부수기
for y,x in WALL:
    WALL[y][x] = 0
    
    #BFS 준비..
    dq = deque([])
    
    time = [[0]*M for _ in range(N)]
    dy = [1,-1,0,0]
    dx = [0,0,1,-1]
    def inMAP(y,x): return 0<=y<N and 0<=x<M

    dq.append((0,0))
    time[0][0] = 1

    while dq:
        currY, currX = dq.popleft()
        currTime = time[currY][currX]

        for i in range(4):
            nextY = currY + dy[i]
            nextX = currX + dx[i]
            if inMAP(nextY, nextX) and MAP[nextY][nextX] != 1:
                if not time[nextY][nextX]:
                    if nextY == N-1 and nextX == M-1:
                        arrive = True
                        if minTime > currTime+1: minTime = currTime+1
                        break
                    time[nextY][nextX] = currTime + 1
                    dq.append((nextY, nextX))
    WALL[y][x] = 1
print(minTime)
