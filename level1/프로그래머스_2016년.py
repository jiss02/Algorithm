def solution(a, b):
    
    date = [31,29,31,30,31,30,31,31,30,31,30,31]
    day = ["FRI", "SAT","SUN", "MON", "TUE", "WED","THU"]
    
    i = 0
    total = 0
    

    while i < a-1:
        total += date[i]
        i += 1
        
    total += b - 1
    result = total % 7
    
    answer = day[result]
    
    return answer