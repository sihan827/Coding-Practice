import sys

N, M = map(int, sys.stdin.readline().split())

A = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
B = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]

def flip(row, col, arr):
    for i in range(row, row+3):
        for j in range(col, col+3):
            arr[i][j] = 0 if arr[i][j] else 1

cnt = 0

# 단순히 좌표 순회해서 좌표 다를 때 단위로 바꿔주기->그리디
for i in range(N-2):
    for j in range(M-2):
        if A[i][j] != B[i][j]:
            flip(i, j, A)
            cnt += 1

if A == B:
    print(cnt)
else:
    print(-1)