# N, M을 공백으로 구분하여 입력받기
N, M = map(int, input().split())

# 캐릭터 위치를 공백으로 구분해서 x 값, y 값, 방향 값 입력받기
x, y, d = map(int, input().split())

# 맵 데이터를 한 줄씩 공백으로 구분해서 입력받기
map_data = []
for i in range(N):
    map_data.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향마다의 x, y 이동 값 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 현재 위치를 방문한 위치로 처리
map_data[x][y] = 2

# 왼쪽으로 회전 정의
def turn_left() :
    global d
    d = (d + 3) % 4

count = 1
count_turn = 0
# 시뮬레이션 시작
while True:
    # 1. 왼쪽으로 회전
    turn_left()
    next_x = x + dx[d]
    next_y = y + dy[d]
    # 전방 타일이 육지고, 방문한 적이 없다면 이동
    if (map_data[next_x][next_y] == 0):
        x = next_x
        y = next_y
        # 이동 후에 현 위치를 방문한 위치로 처리
        map_data[x][y] = 2
        # 이동 타일 갯수 + 1
        count += 1
        count_turn = 0
        continue
    else:
        # 그렇지 않다면 회전수만 + 1
        count_turn += 1
    # 만약 회전수가 4번(동서남북으로 다 돌아본 경우)인 경우
    if count_turn == 4:
        next_x = x - dx[d]
        next_y = y - dy[d]
        # 뒤 타일이 바다인 경우 프로그램 종료
        if (map_data[next_x][next_y] == 1):
            break
        # 뒤 타일이 육지인 경우 이동한 뒤 회전수 = 0
        else :
            x = next_x
            y = next_y
        count_turn = 0

print(count) # 답 출력