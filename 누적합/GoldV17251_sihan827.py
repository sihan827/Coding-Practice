import sys

N = int(sys.stdin.readline())
str_list = list(map(int, sys.stdin.readline().split()))
# 최댓값이 무조건 이기기 때문에 최댓값의 인덱스가 중요
str_max = max(str_list) # O(N)
str_min = min(str_list) # O(N)
if str_max == str_min: 
    print("X")
else:
    max_idx = []
    for i in range(N): # O(N)
        if str_list[i] == str_max:
            max_idx.append(i)

    if len(max_idx) == 1:
        red_win = N - max_idx[0] - 1
        blue_win = max_idx[0]
    # 최댓값이 여러 개일 경우 양쪽 끝에 가까운 두 개 말고 나머지 사이는 다 무승부임
    # 양쪽 끝에 가까운 인덱스만 고려
    else:
        red_win = N - max_idx[-1] - 1
        blue_win = max_idx[0]

    if red_win > blue_win:
        print("R")
    elif red_win < blue_win:
        print("B")
    else:
        print("X")