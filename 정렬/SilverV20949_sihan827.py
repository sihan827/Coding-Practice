import heapq
import math
import sys

def check_ppi(w, h):
    return math.sqrt(w ** 2 + h ** 2) / 77

N = int(sys.stdin.readline())
# 힙으로 정렬해서 하나씩 빼기
hq = []

for i in range(1, N+1):
    width, height = map(int, sys.stdin.readline().split())
    heapq.heappush(hq, (-check_ppi(width, height), i))

while hq:
    _, num = heapq.heappop(hq)
    print(num)