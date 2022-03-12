def is_prime(n) :
    for i in range(2, n) :
        if n % i == 0 :
            return False
    return True

print(is_prime(11))

# 아주 기본적인 소수 구하기 프로그램
# n-1까지 선형적으로 계속 나누어서 떨어지는지 판단
# 시간이 상당히 오래 걸림 