import math

x = int(input())
# 1부터 n까지의 합이 x와 가깝도록 하는 n을 루트로 간단하게 근사
n =  math.floor(math.sqrt(2 * x))

# 정확한 범위를 구하기 위해 반복문으로 n 조금씩 빼주기
while (n ** 2 + n) // 2 >= x:
    n -= 1

# 분수 순서 계산
xtop = x - (n ** 2 + n) // 2

# n이 홀수이면 분모가 1부터 시작
if (n+1) % 2:
    print(str(n+1-xtop+1) + '/' + str(xtop))
# n이 짝수이면 분자가 1부터 시작
else:
    print(str(xtop) + '/' + str(n+1-xtop+1))