from math import sqrt, pi
import sys

a, b, h = map(int, sys.stdin.readline().split())

if a == b:
    print(-1)
else:
    if a > b:
        tmp = a
        a = b
        b = tmp
    # 피타고라스 정리와 변의 비를 이용
    x = a * h / (b - a)
    a_cr = sqrt(x**2 + a**2)
    b_cr = sqrt((x + h)**2 + b**2)
    print((b_cr ** 2 - a_cr ** 2) * pi)