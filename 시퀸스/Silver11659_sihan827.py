N, M = map(int, input().split())
nums = list(map(int, input().split()))

# 구간합을 위한 원소별 합리스트 구현
# sum 사용하면 시간초과터짐
sums = [0]
cnt = 0

for i in range(N):
    cnt += nums[i]
    sums.append(cnt)

for _ in range(M):
    start, end = map(int, input().split())
    start, end = start - 1, end
    # 원소별 합리스트 활용하여 구간합 계산
    print(sums[end] - sums[start])
