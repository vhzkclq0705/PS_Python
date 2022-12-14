# LEVEL 2

def solution(numbers, target):
    graph = [0]

    for num in numbers:
        tmp = []
        for i in graph:
            tmp.append(i + num)
            tmp.append(i - num)
        graph = tmp

    return graph.count(target)

numbers = [1, 1, 1, 1, 1]
target = 3
print(solution(numbers, target))

numbers = [4, 1, 2, 1]
target = 4
print(solution(numbers, target))