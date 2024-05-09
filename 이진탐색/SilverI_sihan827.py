import sys

input = sys.stdin

N, M = map(int, input.readline().split())
lectures = list(map(int, input.readline().split()))

# 탐색해야하는 변수는 블루레이의 수
# 이를 이진탐색할 것
# 최솟값은 강의 중 시간이 가장 긴 것
# 최댓값은 전체 강의의 합
low = max(lectures)
high = sum(lectures)

while low <= high:
    cnt, time = 0, 0
    mid = (low + high) // 2
    for lec in lectures:
        if time + lec > mid:
            time = 0
            cnt += 1
        time += lectures
    if time: cnt += 1
    if cnt <= M:
        high = mid - 1
    else:
        low = mid + 1

print(low)