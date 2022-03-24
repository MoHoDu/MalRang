# max(memo[i][j-1], memo[i-1][j])
seq1 = "ABCDCBA"
seq2 = "DCABDC"

memo = [[0] * len(seq1) for i in range(len(seq2))]

# memo = [[0] * len(seq1)] * len(seq2)
# 위처럼 하면 *가 배열 복사가 아닌 배열의 주소를 복사
# 하는 것이기 때문에 값이 수정되면 해당 주소를 복사한
# 모든 부분이 바뀌게 된다

for i in range(len(seq2)):
    for j in range(len(seq1)):
        seq2i = seq2[i]
        seq1j = seq1[j]
        if i == 0 and j == 0 and seq2i == seq1j:
            memo[i][j] = 1
        elif i == 0 and j == 0 and seq2i != seq1j:
            memo[i][j] = 0
        elif i == 0 and j > 0 and seq2i == seq1j:
            memo[i][j] = memo[i][j - 1] + 1
        elif i == 0 and j > 0 and seq2i != seq1j:
            memo[i][j] = memo[i][j - 1]
        elif i > 0 and j == 0 and seq2i == seq1j:
            memo[i][j] = memo[i - 1][j] + 1
        elif i > 0 and j == 0 and seq2i != seq1j:
            memo[i][j] = memo[i - 1][j]
        elif i > 0 and j > 0 and seq2i == seq1j:
            memo[i][j] = max(memo[i][j-1], memo[i-1][j]) + 1
        elif i > 0 and j > 0 and seq2i != seq1j:
            memo[i][j] = max(memo[i][j-1], memo[i-1][j])

result = memo[-1][-1]
print(result)