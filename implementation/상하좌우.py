# n 입력받기
n = int(input())
# plan 공백 구분해서 입력받기
plans = input().split()

x, y = 1, 1
types = ["L", "R", "U", "D"]
move_x = [0, 0, -1, 1]
move_y = [-1, 1, 0, 0]

for plan in plans :
    for idx in range(len(types)) :
        if plan == types[idx] :
            next_x = x + move_x[idx]
            next_y = y + move_y[idx]

    if next_x < 1 or next_y < 1 or next_x > n or next_y > n :
        continue
    
    x, y = next_x, next_y

print(x, y)