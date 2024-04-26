import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
P = [i for i in range(N)]
# A 기반으로 인덱스 정렬
P_sorted = sorted(P, key= lambda x: A[x])
# 정렬된 인덱스 기반으로 실제 P의 수열 정렬
P_sorted = sorted(P, key= lambda x: P_sorted[x])

print(*P_sorted)