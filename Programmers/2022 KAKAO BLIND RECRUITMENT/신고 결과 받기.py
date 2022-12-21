# LEVEL 1

from collections import defaultdict

def solution(id_list, report, k):
    answer = []
    report = list(set(report))
    users = defaultdict(list)
    cnt = defaultdict(int)

    for repo in report:
        a, b = map(str, repo.split())
        users[a].append(b)
        cnt[b] += 1
    
    for id in id_list:
        res = 0
        for user in users[id]:
            if cnt[user] >= k:
                res += 1
        answer.append(res)

    return answer

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2
print(solution(id_list, report, k))

id_list = ["con", "ryan"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 3
print(solution(id_list, report, k))