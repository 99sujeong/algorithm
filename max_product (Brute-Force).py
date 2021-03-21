def max_product(left_cards, right_cards):
    max = 0
    for i in range(len(left_cards)):
        #print(left_cards[i])
        for j in range(len(right_cards)):
            result = left_cards[i]*right_cards[j]
            if result > max:
                max = result
    return max
    
# 테스트
print(max_product([1, 6, 5], [4, 2, 3]))
print(max_product([1, -9, 3, 4], [2, 8, 3, 1]))
print(max_product([-1, -7, 3], [-4, 3, 6]))
