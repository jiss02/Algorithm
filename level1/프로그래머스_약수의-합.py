def solution(n):

    arr = [n]
    for i in range(1,n//2+1):
        if n % i == 0:
            arr.append(i)
    return sum(arr)