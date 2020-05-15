S1 = "This:-(is str:-(:-(ange te:-)xt."
S2 = "How are you :-) doing :-( today :-)?"
S3 = ":)"

HAPPY = ":-)"
SAD = ":-("

def EMOJI(S, HAPPY, SAD):
    result = ""
    sad, happy, j = 0, 0, 0

    for i in range(0, len(S)):
        while(j > 0 and (S[i] != HAPPY[j] and S[i] != SAD[j])):
            j = 0
        if(S[i] == HAPPY[j] or S[i] == SAD[j]):
            if(j == len(HAPPY) - 1):
                if(S[i] == "("): sad += 1
                else: happy += 1
            else:
                j += 1

    if(sad > happy):
        result = "sad"
    elif(sad < happy):
        result = "happy"
    elif(sad == 0 and happy == 0):
        result = "noun"
    else:
        result = "unsure"

    return result

print(EMOJI(S1, HAPPY, SAD))
print(EMOJI(S2, HAPPY, SAD))
print(EMOJI(S3, HAPPY, SAD))

