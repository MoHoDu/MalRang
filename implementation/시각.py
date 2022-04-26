# N을 입력받기
N = int(input())

count = 0
for hour in range(N+1): # 시간 : 0 ~ N
    for minute in range(60): # 분 : 0 ~ 59
        for second in range(60): # 초 : 0 ~ 59
            time = f'{hour:02d}{minute:02d}{second:02d}'
            # time에 '3'이 포함되어 있으면 count += 1
            if '3' in time:
                count += 1

print(count) # 답 출력