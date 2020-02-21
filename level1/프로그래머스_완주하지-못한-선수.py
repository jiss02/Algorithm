import collections
def solution(participant, completion):
    answer = collections.Counter(participant)-collections.Counter(completion)
    answer = list(answer.keys())
    return answer[0]