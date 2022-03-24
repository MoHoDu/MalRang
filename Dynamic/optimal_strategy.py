def optimal_strategy(coins):
    n = len(coins)
    dp = [[0] * n for i in range(n)]

    # 숫자가 1개만 있는 경우
    for j in range(0, n):
        dp[j][j] = (coins[j], 0)
    
    # 숫자가 2개만 있는 경우
    for j in range(0, n - 1):
        first = max(coins[j], coins[j + 1])
        second = min(coins[j], coins[j + 1])
        dp[j][j + 1] = (first, second)
    
    # 숫자가 3개 이상인 경우
    for i in range(2, n):
        for j in range(0, n - i):
            coin_left = coins[j]
            coin_right = coins[j + i]
            x = coin_left + dp[j + 1][j + i][1]
            y = coin_right + dp[j][j + i - 1][1]
            second = min(dp[j + 1][j + i][0], dp[j][j + i - 1][0])
            dp[j][j + i] = (max(x, y), second)
    
    print(dp)
    return dp[0][n - 1]


coins = [2, 7, 40, 19]
result = optimal_strategy(coins)

print(result)