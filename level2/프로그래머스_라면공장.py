import heapq

def solution(stock, dates, supplies, k):
    h = []
    count = 0
    idx = 0
    while stock < k:
        for i in range(idx, len(dates)):
            if stock < dates[i]:
                break
            else:
                heapq.heappush(h,(-supplies[i], supplies[i]))
                idx += 1

        stock += heapq.heappop(h)[1]
        count += 1
    return count