import math

def solution(p, s):
    ans = []
    stack = []
    a = 0
    for i, j in zip(p,s):
        how = 100 - i
        ap = math.ceil(how/j)
        stack.append(ap)
        
    for i in range(0,len(stack)):
        a += 1
        if i == len(stack) - 1:
            ans.append(a)
            break            
        if stack[i] < stack[i+1]:
            ans.append(a)
            a = 0
        else:
            continue
    return ans