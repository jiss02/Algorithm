import collections
def solution(s, n):
    alpha = collections.deque(sorted("qazwsxedcrfvtgbyhnujmiklop"))
    ualpha = collections.deque(sorted("qazwsxedcrfvtgbyhnujmiklop".upper()))
    answer = [" "] * len(s)
    for i in range(len(s)):
        if s[i] != " ":
            if s[i] in alpha:
                temp = alpha.index(s[i])
                alpha.rotate(-n)
                answer[i] = alpha[temp]
            elif s[i] in ualpha:
                temp = ualpha.index(s[i])
                ualpha.rotate(-n)
                answer[i] = ualpha[temp]
    return "".join(answer)