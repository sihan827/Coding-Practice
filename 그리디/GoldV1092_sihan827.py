import sys

input = sys.stdin.readline
N = int(input())
crane = list(map(int, input().split()))
crane.sort(reverse=True)
M = int(input())
box = list(map(int, input().split()))
box.sort(reverse=True)

if crane[0] < box[0]:
    print(-1)
else:
    minute = 0
    # 박스에 상자 없을때까지
    while len(box) > 0:
        # 크레인에 박스 할당될때마다 박스 지워주기
        for i in range(len(crane)):
            for j in range(len(box)):
                if crane[i] >= box[j]:
                    del box[j]
                    break
        # 라운드 끝날때마다 1분씩 추가
        minute += 1
    print(minute)