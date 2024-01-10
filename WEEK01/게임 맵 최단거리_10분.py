'''
0,0부터 (N-1, N-1)로 가는 bfs로 풀어보자
'''
from collections import deque

def solution(maps):
    N = len(maps)  
    M = len(maps[0])
    #BFS 준비
    dy = [1,-1,0,0]
    dx = [0,0,1,-1]
    def inMAP(y,x): return 0<=y<N and 0<=x<M
    #BFS전 초기화
    dq = deque([])
    time = [[0]*M for _ in range(N)]
    dq.append((0,0))
    time[0][0] = 1
    #BFS 시작
    
    while dq:
        y, x = dq.popleft()
        currTime = time[y][x] + 1
        for i in range(4):
            adjY = y + dy[i]
            adjX = x + dx[i]
            if inMAP(adjY,adjX) and not time[adjY][adjX]:
                if maps[adjY][adjX]:
                    if adjY==N-1 and adjX==M-1: 
                        return currTime
                    dq.append((adjY, adjX))
                    time[adjY][adjX] = currTime
    return -1
