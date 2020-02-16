def solution(arr1, arr2):
    answer = []
    temp = []
    for i, j in zip(arr1, arr2):
        temp = [ one+two for one, two in zip(i,j)]
        answer.append(temp)
    return answer