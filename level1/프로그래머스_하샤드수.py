def solution(x):
    answer = True
    total = 0
    num = x
    while x:
        total += x % 10
        print(total)
        x = x // 10

    if num % total != 0:
        answer = False
        
    return answer