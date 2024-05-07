import sys

input = sys.stdin
N, W, L = map(int, input.readline().split())
trucks = list(map(int, input.readline().split()))
bridge = [0] * W
time = 0

# 다리를 큐처럼 생각해서 시간 지날 때마다 하나씩 popleft 해준다는 느낌으로 접근한다
# 트럭 순서가 정해져 있으므로 가능함
while True:
    if trucks:
        truck = trucks[0]
        del bridge[0]
        if sum(bridge) + truck <= L:
            bridge.append(truck)
            del trucks[0]
        else:
            bridge.append(0)
    else:
        del bridge[0]
        bridge.append(0)
    time += 1
    if len(trucks) == 0 and sum(bridge) == 0:
        break

print(time)