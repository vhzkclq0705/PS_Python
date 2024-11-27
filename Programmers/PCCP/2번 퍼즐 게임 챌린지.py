# Programmers
# Lv.2 - 퍼즐 게임 챌린지

def solution(diffs, times, limit):
    start, end = min(diffs), max(diffs)
    level = 0
    
    while start <= end:
        mid = (start + end) // 2
        total = 0
        
        for i in range(len(diffs)):
            time_prev = times[i - 1] if i else 0
            total += (diffs[i] - mid) * (times[i] + time_prev) + times[i] if diffs[i] > mid else times[i]
            
        if total <= limit:
            level = mid
            end = mid - 1
        else:
            start = mid + 1

    return level