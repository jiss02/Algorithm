N = 1
M = 13
S = "OOIOIOIOIIOII"
pattern = "IO" * N + "I"

def get_pi(pattern):
    length = len(pattern)
    pi = [0] * length;
    j = 0
    for i in range(1, length):
        while(j > 0 and pattern[i] != pattern[j]):
            j = pi[j-1]
        if(pattern[i] == pattern[j]):
            j += 1
            pi[i] = j
    return pi

def KMP(S, M, pattern):
    pi = get_pi(pattern)
    p_len = len(pattern)
    j, count = 0, 0
    for i in range(0, M):
        while(j > 0 and pattern[j] != S[i]):
            j = pi[j - 1]
        if(pattern[j] == S[i]):
            if(j == p_len - 1):
                count += 1
                j = pi[j]
            else:
                j += 1
    return count

print(KMP(S, M, pattern))

