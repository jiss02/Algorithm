def solution(n, lost, reserve):
    answer = 0

    student = [1] * n

    for i in reserve:
        student[i-1] += 1
    for i in lost:
        student[i-1] -= 1

    top = [i for i, j in enumerate(student) if j == 2]

    for i in top:
        if i!=0 and (student[i-1] == 0):
            student[i] -= 1
            student[i-1] += 1
        elif i!=len(student)-1 and (student[i+1] == 0) :
            student[i] -= 1
            student[i+1] += 1
        else:
            student[i] -= 1  

    return sum(student)