def binary_search(element, some_list):
    start = 0
    end = len(some_list)
    
    while start <= end:
        mid = (start + end) // 2
        if some_list[mid] == element:
            return mid
        elif some_list[mid] < element:
            start = mid + 1
        else:
            end = mid - 1
    return None
    
print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))
