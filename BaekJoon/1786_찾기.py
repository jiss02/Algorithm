S = "ABC ABCDAB ABCDABCDABDE"
pattern = "AB"


def get_pi(pattern):
    p_len = len(pattern)
    pi = [0] * p_len
    j = 0

    for i in range(1, p_len):
        while(j > 0 and (pattern[i] != pattern[j])):
            j = pi[j - 1]
        if(pattern[i] == pattern[j]):
            j += 1
            pi[i] = j

    return pi


def KPM(S, pattern):
    pi = get_pi(pattern)
    s_len, p_len = len(S), len(pattern)
    idx = []
    j = 0

    for i in range(0 , s_len):
        while(j > 0 and (S[i] != pattern[j])):
            j = pi[j - 1]
        if(S[i] == pattern[j]):
            if(j == p_len - 1):
                idx.append(i - j + 1)
                j = pi[j]
            else:
                j += 1
    return idx

print(KPM(S, pattern))
