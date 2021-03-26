def trapping_rain(buildings):
    high = max(buildings) - 1
    total = 0
    
    for i in range(len(buildings)-1):
        if buildings[0] == 0:
            if buildings[i] > buildings[i+1]:
                total += (buildings[i] - buildings[i+1])
        else:
            total += (high - buildings[i])

    return total 
    
# 테스트
print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
