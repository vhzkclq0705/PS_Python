# LEVEL 2

def solution(sequence, k):
    answer = []
    left, right = 0, 0
    total = sequence[0]
    
    while left <= right:
        if total == k:
            if not answer:
                answer.append([left, right])
            else:
                print(answer)
                if answer[1] - answer[0] > right - left:
                    answer = [left, right]
        
        if total < k and right < len(sequence) - 1:
            right += 1
            total += sequence[right]
        else:
            total -= sequence[left]
            left += 1
            
    return answer

sequence = [1, 2, 3, 4, 5]
k = 7
print(solution(sequence, k))

sequence = [1, 1, 1, 2, 3, 4, 5]
k = 5
print(solution(sequence, k))

sequence = [2, 2, 2, 2, 2]
k = 6
print(solution(sequence, k))