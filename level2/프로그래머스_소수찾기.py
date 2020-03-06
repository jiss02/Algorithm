import itertools 

def permutation(arr, length):
    result = []
    for i in range(1, length+1):
        per = list(map(''.join, itertools.permutations(arr, i)))
        result.append(per)
    return result

def solution(numbers):
    perNumbers = permutation(numbers, len(numbers))
    perNumbers = list(map(int, sum(perNumbers, [])))
    perNumbers = list(set(perNumbers))

    if 0 in perNumbers:
        perNumbers.remove(0)
    if 1 in perNumbers:
        perNumbers.remove(1)
        
    flag = [True] * len(perNumbers)
    for idx in range(0, len(perNumbers)):
        mid = int(perNumbers[idx]/2) + 1
        for check in range(2, mid):
            if perNumbers[idx] % check == 0 :
                flag[idx] = False
                break
        
    return sum(flag)