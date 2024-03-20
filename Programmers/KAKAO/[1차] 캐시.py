# LEVEL 2

def solution(cacheSize, cities):
    answer = 0
    cache = []
    
    if not cacheSize:
        return 5 * len(cities)
    
    for city in cities:
        city = city.upper()
        if city not in cache:
            answer += 5
            if len(cache) == cacheSize:
                cache.pop(0)
        else:
            answer += 1
            cache.remove(city)
        cache.append(city)
    
    return answer