# Programmers
# Lv.2 - 택배 배달과 수거하기

def solution(cap, n, deliveries, pickups):
    ans = 0
    delivery = 0
    pickup = 0
    
    for i in range(n - 1, -1, -1):
        delivery += deliveries[i]
        pickup += pickups[i]
        
        while (delivery > 0 or pickup > 0):
            delivery -= cap
            pickup -= cap
            ans += (i + 1) * 2
    
    return ans