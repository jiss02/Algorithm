def solution(array, commands):
    answer = []
    temp = []
    for one in commands:
        temp = array[one[0]-1:one[1]] 
        answer.append(sorted(temp)[one[2]-1])
    return answer