def solution(n, m):
    answer = []
    temp = 1
    while 1:
        if n % 2 == 0 and m % 2 == 0:
            n, m = n // 2, m //2
            temp *= 2
        elif n % 3 == 0 and m % 3 == 0:
            n, m = n // 3, m //3
            temp *= 3
        else:
            answer.append(temp)
            temp *= n*m
            break
    answer.append(temp)
            
    return answer