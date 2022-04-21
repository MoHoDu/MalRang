N, K = map(int, input().split())

result = 0
while True :
    quo = N // K
    remain = N % K
    result += remain + 1
    N = quo
    if N < K :
        break 

result += (N - 1)
print(result)