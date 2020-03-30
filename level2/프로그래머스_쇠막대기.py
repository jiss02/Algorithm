def solution(arrangement):
    answer = 0
    stack = []
    
    for token in arrangement:
        if token == "(":
            stack.append(token)
            tail = token
        else:
            if tail == "(":
                stack.pop()
                answer += len(stack)
                tail = token
            else:
                stack.pop()
                answer += 1
    
    return answer