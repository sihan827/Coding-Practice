import math

N, r, c = map(int, input().split())
r += 1
c += 1

def recur_box(r, c):
    # 최소단위 정의 (2x2)
    if r <= 2 and c <= 2:
        if r == 0 and c == 0:
            return 0
        if r == 1 and c == 1:
            return 1
        elif r == 1 and c == 2:
            return 2
        elif r == 2 and c == 1:
            return 3
        elif r == 2 and c == 2:
            return 4
    else:
        # 아닐 경우 4분면으로 구분해서 최소단위까지 재귀 실행
        tmp = max(math.log2(r), math.log2(c))
        unit = 2 ** int(tmp - 1) if tmp == int(tmp) else 2 ** int(tmp) 
        if r - unit == 0 and c - unit == 0:
            return unit ** 2 
        elif r - unit > 0 and c - unit > 0:
            return unit ** 2 * 3 + recur_box(r - unit, c - unit)
        elif r - unit > 0 and c - unit <= 0:
            return unit ** 2 * 2 + recur_box(r - unit, c) 
        elif r - unit <= 0 and c - unit > 0:
            return unit ** 2 + recur_box(r, c - unit)


print(recur_box(r, c) - 1)