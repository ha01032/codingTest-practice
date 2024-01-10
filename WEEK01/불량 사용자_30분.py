'''
<코드입력전 로직 생각>
banned_id와 user_id를 각각 비교해서(2중for문),
    개수같은지 체크 > 한글자씩 별은 그냥 continue, 글자는 같은지 확인
각각의 banned_id에 대한 인접리스트를 만들어준다.
이 인접리스트를 이용해서 깊이 우선탐색을 하며,
visited는 비트마스크를 활용.
깊이가 banned_id 배열의 크기만큼 들어갔을때, 비트마스크를 배열에 담아주고
그 배열을 set으로 만들어서 길이를 리턴한다.
'''
def solution(user_id, banned_id):
    #banned_id와 user_id비교
    banNum = len(banned_id)
    banList = [[] for _ in range(banNum)]
    
    for banIdx, ban in enumerate(banned_id):
        for usrIdx, usr in enumerate(user_id):
            if len(ban) == len(usr):
                isContain = True
                for i in range(len(ban)):
                    if ban[i] == '*': continue
                    if ban[i] != usr[i]: 
                        isContain = False
                        break
                if isContain: banList[banIdx].append(usrIdx)
    
    answerList = []
    def dfs(depth, visited):
        if depth == banNum:
            answerList.append(visited)
            return
        for banUsrIdx in banList[depth]:
            if visited & (1 << banUsrIdx): continue
            dfs(depth+1, (1 << banUsrIdx) | visited)
    dfs(0, 0)
    return len(set(answerList))
