def solution(s):
    s = s.split(" ")
    ans = []
    print(s)
    for i in enumerate(s):
        temp = list(i[1])
        for alpha in range(len(temp)):
            if alpha % 2 == 0:
                temp[alpha] = temp[alpha].upper()
            else:
                temp[alpha] = temp[alpha].lower()
        ans.append("".join(temp)) 
    return " ".join(ans)