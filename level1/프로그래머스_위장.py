from collections import defaultdict

def solution(clothes):
    clothesdict = defaultdict(lambda:0)
    for name, kind in clothes:
        clothesdict[kind] += 1
    numbers = [ x for x in clothesdict.values()]
    answer = 1
    for num in numbers:
        answer *= num + 1
    return answer - 1