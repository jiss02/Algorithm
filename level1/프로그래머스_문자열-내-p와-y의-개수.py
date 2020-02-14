import collections
def solution(s):
    a = False
    
    arr = collections.Counter(s.lower())
    if arr["p"] == arr["y"]:
        a = True
    

    return a;