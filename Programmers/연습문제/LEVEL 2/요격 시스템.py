# LEVEL 2

def solution(targets):
    targets.sort(key=lambda x: x[1])
    now = -1
    ans = 0

    for s, e in targets:
        if s >= now:
            ans += 1
            now = e

    return ans