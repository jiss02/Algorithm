from collections import defaultdict

def make_dictionary(n, array):
    graph =  defaultdict(list)
    for i in range(n):
        for j in range(n):
            if array[i][j] == 1:
                graph[i] += [j]
        graph[i] = set(graph[i])
    return graph

def dfs(graph, start):
    visited = []
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(graph[node] - set(visited))
    return visited

def solution(n, computers):
    net = 0
    start = 0
    visited = []
    graph = make_dictionary(n, computers)
    while len(visited) != n:
        if start not in visited:
            visited += dfs(graph, start)
            net += 1
        start += 1
    return net