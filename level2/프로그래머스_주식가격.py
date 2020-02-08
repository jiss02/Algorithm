def solution(p):

    secs = []
    
    for i in range(0,len(p)):
        sec = 1
        if i == len(p)-1:
            secs.append(0)
            break
        for j in range(i+1, len(p)):      
            if p[j] >= p[i]:
                sec += 1
                if j == len(p)-1:
                    sec -= 1
                    secs.append(sec)       
            else:
                secs.append(sec)
                break
                      
    return secs

# O(n^2) 보다 효율적으로 짜고싶었으나 잘 되지 않았다.