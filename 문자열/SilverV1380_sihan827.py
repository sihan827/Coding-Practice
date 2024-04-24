import sys

scene = 1
while(True):
    N = int(sys.stdin.readline())
    if N == 0:
        break
    names = [""] * (N+1)
    for i in range(1, N+1):
        name = sys.stdin.readline().rstrip()
        names[i] = name
    # 딕셔너리에 이름 있으면 지우고 없으면 추가
    ear_dict = {}
    for _ in range(2 * N - 1):
        num, _ = sys.stdin.readline().split()
        num = int(num)
        if names[num] in ear_dict:
            del ear_dict[names[num]]
        else:
            ear_dict[names[num]] = num
    # 하나 남은 이름 출력
    print(scene, list(ear_dict.keys())[0]) 
    scene += 1