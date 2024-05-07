import sys

input = sys.stdin

A = int(input.readline())
B = int(input.readline())

A, B = A if len(str(A)) > len(str(B)) else B, B if len(str(A)) > len(str(B)) else A

# 최악의 경우는 안 맞물리는 경우-> 두 기어의 길이의 합이 됨
min_gear = len(str(A)) + len(str(B))

# 기어가 맞물렸을 때 4이면 서로 맞물리지 않은 것이므로 이 경우만 제외해주고 길이 짧은대로 업데이트 해주면 됨
for i in range(len(str(A))):
    result = 10 ** i * B + A
    if '4' not in str(result):
        min_gear = min(min_gear, len(str(result)))

for i in range(len(str(B))):
    result = 10 ** i * A + B
    if '4' not in str(result):
        min_gear = min(min_gear, len(str(result)))

print(min_gear)