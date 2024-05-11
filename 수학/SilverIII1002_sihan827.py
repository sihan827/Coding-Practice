import sys

input = sys.stdin

T = int(input.readline())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input.readline().split())
    # 두 점이 일치할 때
    if x1 == x2 and y1 == y2:
        ## 반지름의 크기가 일치할 때: 무한개
        if r1 == r2:
            print(-1)
        ## 반지름의 크기가 일치하지 않을 때: 0개
        else:
            print(0)
    # 두 점이 일치하지 않을 때
    else:
        ## 두 점 사이의 거리가 두 반지름의 합보다 클 때: 0개
        if (x1 - x2) ** 2 + (y1 - y2) ** 2 > (r1 + r2) ** 2:
            print(0)
        ## 두 점 사이의 거리가 두 반지름의 합과 동일할 때: 1개
        elif (x1 - x2) ** 2 + (y1 - y2) ** 2 == (r1 + r2) ** 2:
            print(1)
        ## 두 점 사이의 거리가 두 반지름의 합보다 작을 때
        else:
            r_short, r_long = (r2, r1) if r1 > r2 else (r1, r2)
            ### 두 점 사이의 거리 + r_short > r_long: 2개
            if ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5 + r_short > r_long:
                print(2)
            ### 두 점 사이의 거리 + r_short = r_long: 1개  
            elif ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5 + r_short == r_long:
                print(1)
            ### 두 점 사이의 거리 + r_short > r_long: 0개 
            else:
                print(0)