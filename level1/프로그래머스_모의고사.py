def solution(a):
    answer = []
    score = [0] * 3
    one = [1,2,3,4,5]
    one += one * (len(a)//5)
    two = [2,1,2,3,2,4,2,5]
    two += two  * (len(a)//8)
    three = [3,3,1,1,2,2,4,4,5,5]
    three +=  three  * (len(a)//10) 
    
    for ans,i, j, k in zip(a,one, two, three):
        if ans == i:
            score[0] += 1
        if ans == j:
            score[1] += 1
        if ans == k:
            score[2] += 1
    
    top = max(score)
    answer = [i+1 for i,j in enumerate(score) if j == top]

    return answer