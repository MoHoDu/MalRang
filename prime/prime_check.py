# 숫자를 지우지 않는 에라토스테네스의 체 
from datetime import datetime
def sieve(N) :
    ns = list(range(2, N + 1))
    check = [True] * len(ns)
    
    i = 0
    while ns[i] * ns[i] <= N :
        if check[i] :
        # check의 값이 True라면, 아직 걸러지지 않은 수이므로
        # 소수 판별이 필요 
            for j in range(ns[i] + i, len(ns), ns[i]) :
            # ns[i]만큼 점프하면서 ns[i]의 배수들에 해당하는 인덱스 값의
            # check[해당 인덱스]를 False로 바꿀 것임
            # ns[i] + i 인덱스부터 시작하는 이유는..
            # ns[i]인덱스는 자기 자신이므로 빼야지 소수를 지우는 실수를 하지
            # 않기 때문으로, ns[i] 인덱스를 처음에 한번 건너뛰면 ns[i] * 2
            # 값부터 저절로 시작하게 됨
                check[j] = False
        i += 1
        
    primes = []
    for i in range(len(check)) :
        if check[i] :
            primes.append(ns[i])
    return primes

start_time = datetime.now()
N = 1000000
res = sieve(N)
end_time = datetime.now()
print(len(res), max(res))
print(end_time - start_time)