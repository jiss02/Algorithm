import math
def solution(a, b):
    answer = 0
    if a == b:
        return a
    elif (b - a) % 2 == 0:
        return (a+b) * abs(b-a)/2 + (a+b)/2
    else:
        return (a+b) * math.ceil(abs(b-a)/2)

