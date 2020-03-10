def solution(citations):
    citations = sorted(citations)
    if sum(citations) == 0: return 0
    if sum(citations)/len(citations) == citations[0]: return citations[0]
    for idx in range(0, len(citations)):
        if citations[idx] > len(citations[idx+1:]):
            return len(citations[idx:])
