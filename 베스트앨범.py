def solution(genres, plays):
    answer = []
    playsDict = {}
    sumDict = {}
    for idx, genre in enumerate(genres):
        if not genre in playsDict: 
            playsDict[genre] = []
            sumDict[genre] = 0
        playsDict[genre].append((idx, plays[idx]))
        sumDict[genre] += plays[idx]
    for genre,v in sorted(sumDict.items(), key=lambda x: -x[1]):
        for i, p in sorted(playsDict[genre], key=lambda x: -x[1])[:2]:
            answer.append(i)
    return answer
