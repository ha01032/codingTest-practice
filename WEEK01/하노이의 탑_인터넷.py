answer = []
def dfs(n, x, y):
    global answer
    if n==2:
        answer.append([x,6-x-y])
        answer.append([x,y])
        answer.append([6-x-y,y])
    else:
        dfs(n-1, x, 6-x-y)
        answer.append([x,y])
        dfs(n-1, 6-x-y, y)
def solution(n):
    if n==1: return [1,3]
    dfs(n, 1, 3)
    return answer
