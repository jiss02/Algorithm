def solution(p, l):
    ans = 0
    top = max(p)
    while 1:
        o = p.pop(0)
        if top == o:
            ans += 1
            if l == 0:
                break
            else:
                l -= 1
            top = max(p)
        else:
            p.append(o)
            if l == 0:
                l = len(p) - 1
            else:
                 l -= 1   
    return ans