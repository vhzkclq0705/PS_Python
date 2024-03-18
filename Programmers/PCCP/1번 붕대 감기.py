# LEVEL 1 / 1번 / 붕대 감기

def solution(bandage, health, attacks):
    max_health = health
    bandaging = 0
    idx = 0

    for time in range(1, attacks[-1][0] + 1):
        if time == attacks[idx][0]:
            health -= attacks[idx][1]
            bandaging = 0
            idx += 1

            if health <= 0:
                return -1
        else:
            health = min(health + bandage[1], max_health)
            bandaging += 1
            if bandaging == bandage[0]:
                health = min(health + bandage[2], max_health)
                bandaging = 0

    return health