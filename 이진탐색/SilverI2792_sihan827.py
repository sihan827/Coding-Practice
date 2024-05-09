import sys
input = sys.stdin

N, M = map(int, input.readline().split())
gems = []

for _ in range(M):
    gems.append(int(input.readline()))

# mid는 한 사람이 가지는 보석의 수
# mid가 작을수록 질투심이 최솟값
# 기준값은 mid를 통해 계산한 사람 수가 N보다 크냐 많냐의 차이
# -> N보다 크면 mid보다 커야 하고 아니면 mid보다 작아야 함
high = max(gems)
low = 1

while low <= high:
    mid = (low + high) // 2
    total = 0
    for gem in gems:
        # 단순히 보석의 수를 mid로 나누어 사람 수 계산
        total += gem // mid
        # 나머지가 0이 아니면 남은 수 또한 한 사람에게 부여됨
        # -> 1 더하기
        if gem % mid:
            total += 1
    
    # 이렇게 계산된 사람 수가 N보다 크면 mid 늘리기
    if total > N:
        low = mid + 1
    # 사람 수가 N보다 작거나 같으면 해당 mid값을 질투값으로 저장하고 다시 탐색
    else:
        ans = mid
        high = mid - 1

print(ans)