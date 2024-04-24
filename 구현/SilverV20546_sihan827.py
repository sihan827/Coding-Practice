import sys

m = int(sys.stdin.readline())
money = [m, m]
stock = [0, 0]

cost = list(map(int, sys.stdin.readline().split()))

asc_cnt = 0
des_cnt = 0

## 준현이 계산
for i in range(14):
    stock[0] += money[0] // cost[i]
    money[0] -= money[0] // cost[i] * cost[i]

## 성민이 계산
for i in range(1, 14):
    if cost[i-1] < cost[i]:
        asc_cnt += 1
    else:
        asc_cnt = 0 
    if cost[i-1] > cost[i]:
        des_cnt += 1
    else:
        des_cnt = 0
    if des_cnt >= 3:
        stock[1] += money[1] // cost[i]
        money[1] -= money[1] // cost[i] * cost[i]
    if asc_cnt >= 3:
        money[1] += cost[i] * stock[1]
        stock[1] = 0

jun = money[0] + stock[0] * cost[-1]
sung = money[1] + stock[1] * cost[-1]

if jun == sung:
    print('SAMESAME')
elif jun > sung:
    print('BNP')
else:
    print('TIMING')