# LEVEL 2

from collections import deque

def solution(people, limit):
    ans = 0
    people = deque(sorted(people))

    while len(people) > 1:
        if people[0] + people[-1] <= limit:
            people.pop()
            people.popleft()
        else:
            people.pop()
        ans += 1
    
    if people:
        ans += 1
    
    return ans

people = [70, 50, 80, 50]
print(solution(people, 100))

people = [70, 80, 50]
print(solution(people, 100))