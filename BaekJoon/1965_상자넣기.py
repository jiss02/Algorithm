N = int(input())
array = list(map(int, input().split(" ")))

dp = [0] * N
for i in range(0, N):
    dp[i] = 1
    for j in range(0, i):
        if(array[i] > array[j] and dp[j] + 1 > dp[i]):
            dp[i] = dp[j] + 1
print(max(dp))



    