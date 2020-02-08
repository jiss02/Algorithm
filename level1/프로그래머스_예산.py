def solution(d, budget):
    answer = 0
    c = 0
    d=sorted(d)
    for num in d:
        answer+=num
        if answer == budget:
            c += 1;
            break
        elif answer > budget:
            break
        c += 1;
    return c