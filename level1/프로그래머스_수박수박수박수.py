def solution(n):
    answer = ''
    soo = ["수","박"]
    answer += "".join(soo*(n//2)) + (n%2)*soo[0]
    return answer