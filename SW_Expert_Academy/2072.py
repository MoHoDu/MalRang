T = int(input())

for i in range(T):
    numbers = map(int, input().split())

    answer = 0
    for number in numbers:
        if number % 2 == 1:
            answer += number
    print(f'#{i+1} {answer}')
