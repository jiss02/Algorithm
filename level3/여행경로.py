from collections import defaultdict

def solution(tickets):
    # 객체 생성
    route = defaultdict(list)
    for start, dest in tickets:
        route[start].extend([dest])
    for i in route:
        route[i].sort(reverse=True)
    print(route)
    # 초기화
    stack, best = ["ICN"], []
    # dfs
    while stack:
        node = stack[-1]
        if node not in route or route[node] == [] :
            best.append(stack.pop())
            route[node] = route[node][:-1]
        else:
            stack.append(route[node][-1])
            route[node] = route[node][:-1]
    return best[::-1]