def solution(arr, d):
    a = []
    for i in arr:
        if i % d == 0:
            a.append(i)
    if a == []:
        a.append(-1)
    return sorted(a)