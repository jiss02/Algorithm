def solution(s):
    answer = True
    arr = "abcdefghijklmnopqrstuvwzy"
    if (len(s) == 4 or len(s) == 6):
        for i in s.lower():
            if i in arr:
                answer = False
    else:
        answer = False

    return answer