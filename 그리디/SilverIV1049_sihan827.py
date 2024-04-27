import heapq
import sys

N, M = map(int, sys.stdin.readline().split())
six_list = []
one_list = []

# 힙으로 각 최솟값 가져오기
for _ in range(M):
    six, one = map(int, sys.stdin.readline().split())
    heapq.heappush(six_list, six)
    heapq.heappush(one_list, one)

min_six = heapq.heappop(six_list)
min_one = heapq.heappop(one_list)

# 줄 계산 시 하나만 살 때, 세트로 살 때 고려하여 최솟값 출력
print(min(min_one * N, min_six * (N // 6) + min(min_six, (N % 6) * min_one)))