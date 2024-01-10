answer = []
def dfs(n, x, y):
    global answer
    if n==1:
        answer.append([x,y])
    else:
        dfs(n-1, x, 6-x-y)
        answer.append([x,y])
        dfs(n-1, 6-x-y, y)
def solution(n):
    dfs(n, 1, 3)
    return answer
