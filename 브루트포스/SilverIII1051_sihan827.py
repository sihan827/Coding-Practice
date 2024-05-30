import sys
input = sys.stdin

N, M = map(int, input.readline().split())
rect = []

for _ in range(N):
    rect.append(list(map(int, list(input.readline().rstrip()))))

# 정사각형 최대길이는 직사각형 변 중 가장 짧은 길이
start = min(N, M)
max_leng = 0

# 정사각형 최대길이부터 짧은 길이까지 브루트포스로 탐색
for leng in reversed(range(1, start+1)):
    for i in range(N):
        for j in range(M):
            # 인덱스 초과 처리
            if i+leng-1 >= N or j+leng-1 >= M:
                continue
            # 정사각형 조건 만족시 값 비교하여 교체
            if rect[i][j] == rect[i+leng-1][j] and rect[i][j] == rect[i][j+leng-1] and rect[i][j] == rect[i+leng-1][j+leng-1]:
                max_leng = max(max_leng, leng ** 2)


print(max_leng)