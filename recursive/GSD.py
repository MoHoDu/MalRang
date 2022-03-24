# Greatest Common Divisor

# 최대공약수 규칙
# gcd(a, a) = a
# if a < b -> gcd(a, b) = gcd(a, a + b)
# if a > b -> gcd(a, b) = gcd(a - b, b)
# gcd(a, b) = gcd(b, a)

def gcd(first, second):
    print(first, second)
    if first == second:
        return first
    elif first > second:
        return gcd(first - second, second)
    elif first < second:
        return gcd(first, second - first)
    return 1

result = gcd(196, 42)
print(result)