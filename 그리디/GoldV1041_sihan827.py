from itertools import combinations
import heapq
import sys

N = int(sys.stdin.readline())
A, B, C, D, E, F = map(int, sys.stdin.readline().split())
values = ['A', 'B', 'C', 'D', 'E', 'F']
val_dict = {'A': A, 'B': B, 'C': C, 'D': D, 'E': E, 'F': F}

# 가운데 (N-2)^2개들은 그냥 한면이므로 최솟값 쓰기 -> val * (N-2) ** 2 * 5
# 1층 꼭지점 4개는 두면만 보이므로 이어진 2면이 최소인 값 쓰기 -> val * 4
# 모서리 N-2개들은 두면 최소인 것 그냥 사용 -> val * (N-2) * 8
# 1층 모서리는 한면만 보이기 -> val * (N-2) * 4
# 윗층 꼭지점 4개는 세면이 보이므로 세면의 값이 최소인 조합 뽑기 -> val * 4

## 면 한개
min_1 = min(val_dict.values())

## 면 두개
pick_2 = list(combinations(values, 2))
pick_2.remove(('A', 'F'))
pick_2.remove(('B', 'E'))
pick_2.remove(('C', 'D'))

hq = []

for val in pick_2:
    v = [val_dict[i] for i in val]
    heapq.heappush(hq, sum(v))
min_2 = heapq.heappop(hq)

## 면 세개
pick_3 = list(combinations(values, 3))
del_list = []
for i in range(len(pick_3)):
    if 'A' in pick_3[i] and 'F' in pick_3[i]:
        del_list.append(pick_3[i])
    elif 'B' in pick_3[i] and 'E' in pick_3[i]:
        del_list.append(pick_3[i])
    elif 'C' in pick_3[i] and 'D' in pick_3[i]:
        del_list.append(pick_3[i])

for val in del_list:
    pick_3.remove(val)

hq = []
for val in pick_3:
    v = [val_dict[i] for i in val]
    heapq.heappush(hq, sum(v))
min_3 = heapq.heappop(hq)

# 모든 면의 합 계산
if N == 1:
    print(sum(val_dict.values()) - max(val_dict.values()))
else:
    print(min_1 * ((N-2) ** 2 * 5 + (N - 2) * 4) + min_2 * ((N - 2) * 8 + 4) + min_3 * 4)