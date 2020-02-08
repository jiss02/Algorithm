def solution(n):
    ans = ''

    while n:
        m = n % 3
        n = n // 3
        ans = "412"[m] + ans
        if m == 0:      
            n -= 1

    return ans