def recursive_function(i):
    # 100번째 출력 시에 종료 - 종료 조건
    if i == 100:
        return
    print(i, '번째 재귀 함수가', i + 1, '번째 재귀 함수 호출')
    recursive_function(i + 1)
    print(i, '번째 재귀 함수 종료')

recursive_function(1)