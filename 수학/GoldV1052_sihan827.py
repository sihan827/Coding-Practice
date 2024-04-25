import sys

n, k = map(int, sys.stdin.readline().split())
# 2진수로 표현하여 1의 개수가 병의 개수 -> 1의 개수가 k보다 작거나 같도록 물병을 계속 구매
count = 0
while bin(n).count('1') > k:
    n += 1
    count += 1

print(count)