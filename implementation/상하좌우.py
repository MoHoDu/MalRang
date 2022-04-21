# n 입력받기
n = int(input())
# plan 공백 구분해서 입력받기
plans = input().split()

x, y = 1, 1 # x, y의 초기 위치 설정
# 이동 타입 지정
types = ["L", "R", "U", "D"]
# 타입의 인덱스에 맞게 각 타입에 따라 이동하는 x축 y축 값 설정
move_x = [0, 0, -1, 1]
move_y = [-1, 1, 0, 0]

for plan in plans :
    for idx in range(len(types)) :
        # 해당 plan과 같은 타입의 인덱스 값으로 x, y를 이동
        if plan == types[idx] :
            next_x = x + move_x[idx]
            next_y = y + move_y[idx]

    # 만약 지도 밖으로 넘어가면 무시
    if next_x < 1 or next_y < 1 or next_x > n or next_y > n :
        continue
    
    x, y = next_x, next_y # 새로운 위치로 x, y를 이동

print(x, y) # 답 출력