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




def solution(n):
    answer = []
    def dfs(n, src, tgt, inter):
        if n==1:
            answer.append([src,tgt])
        else:
            dfs(n-1, src, inter, tgt)
            answer.append([src,tgt])
            dfs(n-1, inter, tgt, src)    
    dfs(n, 1, 3, 2)
    return answer
    
    
