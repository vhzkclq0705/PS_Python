# LEVEL 3

from collections import deque

def solution(begin, target, words):
    ans = 0
    q = deque()
    q.append([begin, 0])
    visited = [False] * len(words)

    while q:
        word, depth = q.popleft()

        if word == target:
            ans = depth
            break

        for i in range(len(words)):
            cnt = 0
            if not visited[i]:
                for j in range(len(word)):
                    if word[j] != words[i][j]:
                        cnt += 1
                
                if cnt == 1:
                    visited[i] = True
                    q.append([words[i], depth + 1])
        
    return ans

begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
print(solution(begin, target, words))

begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log"]
print(solution(begin, target, words))