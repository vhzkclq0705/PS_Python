# Level 2

def solution(citations):
    citations.sort(reverse = True)

    for i in range(len(citations)):
        if i >= citations[i]:
            return i
    
    return len(citations)

c = [3, 0, 6, 1, 5]
print(solution(c))