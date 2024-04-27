import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

# 서로 반대로 정렬해서 곱하면 그것이 최솟값이 됨
A.sort(reverse=True)
B.sort()

sum_ab = 0

for i in range(N):
    sum_ab += A[i] * B[i]

print(sum_ab)