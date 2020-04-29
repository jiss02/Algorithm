import itertools

def check_same(check, num):
    strike, ball = (0,0)
    for i in range(3):
        if check[i] == num[i]:
            strike += 1
        if check[i] in num:
            ball += 1
    return (strike, ball-strike)
            
def solution(baseball):
    number = [str(x) for x in range(1,10)]
    allNumber = list(map(''.join, itertools.permutations(number,3)))
    for num, strike, ball in baseball:
        allNumber = [check for check in allNumber if check_same(check, str(num)) == (strike, ball)]
    return len(result)

solution([[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]])