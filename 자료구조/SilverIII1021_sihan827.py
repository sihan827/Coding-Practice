import sys

input = sys.stdin

N, M = map(int, input.readline().split())
nums = list(map(int, input.readline().split()))
que = [i for i in range(1, N+1)]

cal_cnt = 0

for n in nums:
    idx = que.index(n)
    if len(que) % 2 == 0:
        check_idx = len(que) // 2
    else:
        check_idx = len(que) // 2 + 1
    # 꺼낼 원소의 현재 위치가 중간보다 왼쪽에 있으면 2번연산, 오른쪽에 있으면 3번연산
    # 연산 수행한 후 큐를 계속 업데이트
    # 연산을 모두 더하기
    if idx < check_idx:
        cal_cnt += idx
    else:
        cal_cnt += len(que) - idx
    que = que[idx+1:] + que[:idx]

print(cal_cnt)