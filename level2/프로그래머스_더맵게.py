import heapq

def solution(scov, K):
    heapq.heapify(scov)
    count = 0
    while len(scov) > 1:
        pop = heapq.heappop(scov)
        if pop < K:
            mix = pop + (heapq.heappop(scov) * 2)
            heapq.heappush(scov, mix)
            count += 1
    
        
    return count if scov[0] >= K else -1