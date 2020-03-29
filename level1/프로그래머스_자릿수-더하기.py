def solution(n):
    ans = 0
    
    while n:
        ans += n % 10
        n = n // 10
    
    return ans