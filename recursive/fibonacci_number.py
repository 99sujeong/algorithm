# n번째 피보나치 수를 리턴
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-2) + fib(n-1)

# 테스트: fib(1)부터 fib(10)까지 출력
for i in range(1, 11):
    print(fib(i))