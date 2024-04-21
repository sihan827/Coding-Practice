N, M = map(int, input().split())
table = []
answer = -1

def is_sqrt(S):
    S = int(S)
    return int(S ** 0.5) ** 2 == S

for _ in range(N):
    table.append(list(input().rstrip()))

for i in range(N): # 가능한 row 경우
    for j in range(M): # 가능한 column 경우 
        for row_d in range(-N, N): # row 공차
            for col_d in range(-M, M): # column 공차
                num = ""
                x, y = i, j
                if row_d == 0 and col_d == 0: # row, column 공차 0인 경우는 모두 제외
                    continue
                while 0 <= x < N and 0 <= y < M: # row, column 범위 안에 있을 때
                    num += table[x][y]
                    if is_sqrt(num): # 제곱수이면 최대인가 판단
                        answer = max(answer, int(num))
                    # 공차 더해주기
                    x += row_d
                    y += col_d

print(answer)