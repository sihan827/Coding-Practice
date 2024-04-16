from math import sqrt, floor

TC = int(input())

# 수열 규칙 문제
# 이동횟수를 기준으로 거리, 이동방법, 이동거리 최댓값 나열 시 규칙 확인
# 1     1       1                       1
# 2     2       1 1                     1
# 3     4       1 2 1                   2
# 4     6       1 2 2 1                 2
# 5     9       1 2 3 2 1               3
# 6     12      1 2 3 3 2 1             3
# 7     16      1 2 3 4 3 2 1           4
# 8     20      1 2 3 4 4 3 2 1         4
# 9     25      1 2 3 4 5 4 3 2 1       5
# 10    30      1 2 3 4 5 5 4 3 2 1     5

for _ in range(TC):
    X, Y = map(int, input().split())
    Y -= X
    X = 0
    dist = Y - X

    max_step = floor(sqrt(dist))
    if sqrt(dist) == max_step:
        cnt = max_step * 2 - 1
    elif dist <= max_step ** 2 + max_step:
        cnt = max_step * 2
    else:
        cnt = max_step * 2 + 1

    print(cnt)