N, M, K = map(int, input().split( ))

data = list(map(int, input().split()))

data.sort()
first = data[N - 1]
second = data[N - 2]

count_first = (M // (K + 1)) * K + (M % (K + 1))
count_secound = M - count_first
result = (first * count_first) + (second * count_secound)

print(result)
