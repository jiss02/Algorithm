def big(n):
    if len(n) <= 1:
        return n
    sen = ''
    pivot = n[len(n)//2]
    less, equal, larger = [],[],[]
    for i in range(0,len(n)):
        num = n[i]
        if sen + str(num) + str(pivot) < sen + str(pivot) + str(num):
            less.append(num)
        elif sen + str(num) + str(pivot) > sen + str(pivot) + str(num):
            larger.append(num)
        else:
            equal.append(num)
    return big(less) + equal + big(larger)

def solution(n):
    answer = ''
    if sum(n) == 0:
        return '0'
    temp = big(n)
    while temp:
        answer += str(temp.pop())
        
    return answer