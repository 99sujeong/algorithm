# n의 각 자릿수의 합을 리턴
def sum_digits(n):
    '''
    if n > 10000:
        return (n // 10000) + sum_digits(n % 10000)
    elif n > 1000:
        return (n // 1000) + sum_digits(n % 1000)
    elif n > 100:
        return (n // 100) + sum_digits(n % 100)
    elif n > 10:
        return (n // 10) + sum_digits(n % 10)
    return n // 1
    '''
    if n < 10:
        return n

    return n % 10 + sum_digits(n//10)
    
# 테스트
print(sum_digits(22541))
print(sum_digits(92130))
print(sum_digits(12634))
print(sum_digits(704))
print(sum_digits(3755))
