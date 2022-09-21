# Level 1

def solution(sizes):
    return max(max(w) for w in sizes) * max(min(h) for h in sizes)

sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
print(solution(sizes))