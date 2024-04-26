import sys

N, M = map(int, sys.stdin.readline().split())
board = []
for _ in range(N):
    board.append(list(sys.stdin.readline().rstrip()))

b_board = [list("BWBWBWBW"), list("WBWBWBWB")] * 4
w_board = [list("WBWBWBWB"), list("BWBWBWBW")] * 4
min_paint = float("inf")

# 브루트포스로 탐색하는 방법밖에 없다고함
# 시간복잡도 대략 O(N*M*64)
# 생각보다 오래 걸리지 않음
for row_start in range(N-7):
    for col_start in range(M-7):
        b_paint = 0
        w_paint = 0
        for i in range(row_start, row_start+8):
            for j in range(col_start, col_start+8):
                if board[i][j] != b_board[row_start-i][col_start-j]:
                    b_paint += 1
                if board[i][j] != w_board[row_start-i][col_start-j]:
                    w_paint += 1
        min_paint = min([min_paint, b_paint, w_paint])

print(min_paint)