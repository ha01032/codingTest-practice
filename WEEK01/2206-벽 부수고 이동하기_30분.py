'''
벽을 만날때만 부수는 형태로 바꿔야함..(시간복잡도)
'''
import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int,input().strip().split())

MAP = []

for y in range(N):
    MAP.append(list(map(int,input().strip())))

#bfs 준비
dy = [1,-1,0,0]
dx = [0,0,1,-1]
def inMAP(y,x): return 0<=y<N and 0<=x<M

#bfs 초기화
dq = deque([])
time = [[[0]*2 for _ in range(M)] for _ in range(N)]
dq.append((0,0,0))
time[0][0][0] = 1
arrive = False

#bfs 시작
while dq:
    y,x,c = dq.popleft()
    currTime = time[y][x][c]
    if y==N-1 and x==M-1:
        print(currTime)
        arrive = True
        break
    for i in range(4):
        nextY = y+dy[i]
        nextX = x+dx[i]
        if inMAP(nextY, nextX) and not time[nextY][nextX][c]:
            #만약 벽인데, 아직 벽 안부쉈으면
            if MAP[nextY][nextX] == 1 and not c and not time[nextY][nextX][1]:
                dq.append((nextY, nextX, 1))
                time[nextY][nextX][1] = currTime+1
            #벽아니고 지나갈때
            if MAP[nextY][nextX] == 0:
                dq.append((nextY, nextX, c))
                time[nextY][nextX][c] = currTime+1
if not arrive: print(-1)
