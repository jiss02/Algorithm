def solution(dartResult):
    stageNumber = ''
    stack = []
    for i in dartResult:
        if i.isnumeric():
            stageNumber += i
            continue
        elif i == 'S':
            stack.append(int(stageNumber))
        elif i == 'D':
            stack.append(int(stageNumber)**2)
        elif i == 'T':
            stack.append(int(stageNumber)**3)
        elif i == '*':
            if len(stack) > 1:
                stack[-2] *= 2
            stack[-1] *= 2
        elif i == '#':
            stack[-1] *= -1
        stageNumber = ''
    return sum(stack)
