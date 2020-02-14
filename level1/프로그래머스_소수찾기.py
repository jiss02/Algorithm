def solution(n):
    num = [0,0] + [1] * (n-1)
    
    for i in range(2,n+1):
        if num[i]:
            for j in range(i*2, n+1, i):          
                num[j] = 0

    return sum(num)