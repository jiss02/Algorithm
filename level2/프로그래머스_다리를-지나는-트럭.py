def solution(b, w, t):
    stack = [0]*b
    ans = 0
    
    while stack:
        stack.pop(0)
        if (sum(stack) + t[0]) <= w:
        	truck = t.pop(0)
        	stack.append(truck)
        else:
        	stack.append(0)
        ans += 1
    return ans