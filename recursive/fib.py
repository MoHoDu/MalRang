def fib(num):
    if num <= 1:
        return num
    return fib(num - 1) + fib(num - 2)

result = fib(4)
print(result)

# fib(4)
# fib(3) + f(2)
# f(2) + f(1) + f(1) + f(0)
# f(1) + f(0) + f(1) + f(1) + f(0)
# 1 + 0 + 1 + 1 + 0 = 3

# fib(2) => fib(1) + fib(0)을 한 번 구했음에도
# 계속 반복적으로 계산하는 단점
# 이를 해결하기 위해 다이다믹 프로그래밍을 씀