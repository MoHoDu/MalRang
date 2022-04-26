# start point를 입력받기
start = input()

# start point의 좌표를 설정하기
x = int(ord(start[0])) - int(ord('a')) + 1
y = int(start[1])

# 나이트가 이동할 수 있는 8가지의 방법 정의하기
steps = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

count = 0
# 8가지의 방법에 대해서 각각 이동 가능한지 판단하기
for step in steps:
    next_x = x + step[0]
    next_y = y + step[1]
    # 이동 가능할 시에 count += 1
    if (next_x >= 1 and next_x <= 8 and next_y >= 1 and next_y <= 8 ):
        count += 1

print(count) # 답 출력