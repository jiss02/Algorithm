N = 10

array = [1 ,100 ,2 ,50 ,60 ,3 ,5 ,6 ,7 ,8]
dp = [0] * N

dp[0] = array[0]

for i in range(1, N):
    for j in range(0,i):
        if(array[i] > array[j] and dp[j] + array[i] > dp[i]):
            dp[i] = dp[j] + array[i]

print(max(dp))