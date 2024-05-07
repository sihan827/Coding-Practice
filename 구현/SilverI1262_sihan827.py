N, R1, C1, R2, C2 = map(int, input().split())

# 마름모 타일 크기배열이 40000개이면 메모리 박살
# 따라서 미리 배열 생성은 불가능
al = list("abcdefghijklmnopqrstuvwxyz")
edge = 2 * N -1

# 가운데 알파벳인 a로부터 행+열 거리가 동일할 시 모두 같은 알파벳임을 이용
for i in range(R1, R2+1):
    for j in range(C1, C2+1):
        # 단위 타일로 하기 위해 한 변 길이로 나머지 계산
        i = i % edge
        j = j % edge
        # 거리 계산
        dist = abs(N-1-i) + abs(N-1-j)
        # 만약 최대 거리를 벗어나면 .를 출력
        if dist > N-1:
            print(".", end="")
        # 아닐 시 알파벳 출력
        # 알파벳은 z 이후 순환하므로 전체 알파벳 길이로 나머지 구하기
        else:
            print(al[dist % 26], end="")
    # 한 행 끝날 시 개행
    print("")