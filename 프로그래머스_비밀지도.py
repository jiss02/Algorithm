def solution(n, arr1, arr2):
    bits = []
    for one, two in zip(arr1, arr2):
        bit = bin(one | two)
        bit = bit[2:].zfill(n)
        bits.append(bit.replace("0"," ").replace("1","#"))
    return bits