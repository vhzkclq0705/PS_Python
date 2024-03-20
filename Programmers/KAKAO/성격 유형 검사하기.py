# LEVEL 1

def solution(survey, choices):
    answer = ''
    type = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}
    
    for i in range(len(survey)):
        if choices[i] < 4:
            type[survey[i][0]] += 4 - choices[i]
        elif choices[i] > 4:
            type[survey[i][1]] += choices[i] - 4
    
    answer += "R" if type["R"] >= type["T"] else "T"
    answer += "C" if type["C"] >= type["F"] else "F"
    answer += "J" if type["J"] >= type["M"] else "M"
    answer += "A" if type["A"] >= type["N"] else "N"

    return answer

survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5, 3, 2, 7, 5]
print(solution(survey, choices))

survey = ["TR", "RT", "TR"]
choices = [7, 1, 3]
print(solution(survey, choices))