def solution(arr):
    ans = []
    for i in range(1,len(arr)):
        if arr[i] != arr[i-1]:
            ans.append(arr[i-1])
    ans.append(arr[len(arr)-1])
    return ans