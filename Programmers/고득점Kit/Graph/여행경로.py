# LEVEL 3

from collections import defaultdict

def solution(tickets):
    ans = []
    stack = ["ICN"]
    graph = defaultdict(list)

    for departure, arrival in tickets:
        graph[departure].append(arrival)
    
    for departure in graph.keys():
        graph[departure].sort(reverse=True)
    
    while stack:
        top = stack.pop()

        if top not in graph or not graph[top]:
            ans.append(top)
        else:
            stack.append(top)
            stack.append(graph[top].pop())

    return ans[::-1]

tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
print(solution(tickets))

tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
print(solution(tickets))

tickets = [["ICN", "A"], ["ICN", "B"], ["B", "ICN"]]
print(solution(tickets))