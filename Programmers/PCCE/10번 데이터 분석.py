# LEVEL 1 / 10번 / 데이터 분석

def solution(data, ext, val_ext, sort_by):
    d = {"code": 0, "date": 1,"maximum": 2, "remain": 3}
    answer = [i for i in data if i[d[ext]] < val_ext]

    return sorted(answer, key=lambda x: x[d[sort_by]])