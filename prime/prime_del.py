# 숫자를 지우는 에라토스테네스의 체
from datetime import datetime
from math import sqrt

def sieve(N) :
    ns = list(range(2, N + 1)) 
    # 1은 소수가 아니면서 합성수도 아니기 때문에 제외
    for i in range(2, int(sqrt(N)) + 1) :
    # 루트 N까지 하는 이유
    # 2의 배수부터 차례로 제거할텐데.. 
    # 루트 100인 10보다 큰 11까지 배수들을 제거한다고 할때
    # 11 * 2(3,4,5,6,7,8,9,10)은 이미 2,3,4,5,6,7,8,9,10
    # 의 배수로 제거되었기 때문에 11 * 11부터 제거를 해야되는데
    # 11 * 11 자체가 이미 100을 넘기기 때문에 할 필요가 없음 
    # 그래서 루트 100인 10까지의 배수들만 제거해도 됨
    # int를 하는 이유는 소수점자리를 빼기 위해서고, +1을 한 이유는
    # 루트 N의 값까지 포함시켜야 하기 때문이다
        for j in range(len(ns) - 1, 1, -1) :
        # 거꾸로 제거하는 이유는 배수를 제거하고 나서
        # 뒤에 값들을 다시 복사해서 앞으로 당기는데에 드는 시간을
        # 감축하기 위함
        # len(ns) - 1인 이유는 인덱스 시작이 0이기 때문이고,
        # 1까지로 해야 ns[0], ns[1]인 2,3을 포함하지 않기 
        # 때문이다 (어차피 소수라서 계속 0, 1번째 인덱스에 있음)
            if ns[j] % i == 0 and ns[j] > i :
            # 나누어 떨어지지만, 나누는 값과 같은 수는 제외 
            # 소수인데 지워지는 것을 방지 
                ns.pop(j)
    return ns

start_time = datetime.now()
result = sieve(1000000)
print(max(result))
end_time = datetime.now()
print(end_time - start_time)
# 좋은 방법이지만, 4의 배수 역시 2의 배수인데 다시 파악하는 등
# 상당히 비효율적인 부분이 있었음
# 그런 연속적인 과정에서 계속 % 연산을 하는 것에서 시간이 더 소요
# --> while로 해결해보자

def sieveWhile(N) :
    ns = list(range(2, N + 1))
    i = 0
    while ns[i] * ns[i] <= N :
        for j in range(len(ns) - 1, 1, -1) :
            if ns[j] % ns[i] == 0 and ns[j] > ns[i] :
                ns.pop(j)
        i += 1
    return ns

start_time = datetime.now()
result = sieveWhile(1000000)
print(max(result))
end_time = datetime.now()
print(end_time - start_time)
# 연산 횟수는 줄였지만, 숫자를 제거한 뒤에 -1이 적용된 ns의 길이로 
# 배열을 계속 생성하고 값을 복사해서 배열에 당겨서 다시 넣는 연산이
# 계속되고 있음