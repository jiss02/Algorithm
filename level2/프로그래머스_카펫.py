def solution(brown, red):
    red_num = [(red, 1)]
    for i in range(red//2,0,-1):
        if red % i == 0:
            if i < red // i: continue
            red_num.append((i, red // i))
    for big, small in red_num:
        if (brown-(small*2)) % (big+2) == 0:
            return [big+2, (brown + red) // (big+2)]
    return -1
