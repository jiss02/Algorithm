from collections import Counter

def solution(N, stages):
    answer = {}
    for i in range(1,N+1):
        answer[i] = 0
    stages = sorted(stages)
    countList = Counter(stages)
    
    for k in range(1, N+1):
        try:
            passIdx = stages.index(k)
            arrivePlayers = stages[passIdx:]
            fail = countList[k]/len(arrivePlayers)
            answer[k] = fail
        except ValueError:
            pass
        
    answer = sorted(answer.items(), key=(lambda x:x[1]),reverse=True)
    answer = [x[0] for x in answer]
    
    return answer