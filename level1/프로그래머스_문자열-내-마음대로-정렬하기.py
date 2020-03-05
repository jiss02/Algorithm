import operator
def solution(s, n):
    a = {}

    for i in s:
        a[i] = i[n]

    a = sorted(a.items(),key=operator.itemgetter(1,0))

    return list([i[0] for i in a ])