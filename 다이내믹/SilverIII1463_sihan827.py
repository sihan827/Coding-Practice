N = int(input())

dp = [0] * (N+1)
dp[1] = 0

# 바텀업 방식(제한이 10의 6승이므로)
# 세가지 연산을 다 비교해서 제일 작은 연산수를 저장
for i in range(2, N+1):
    dp[i] = dp[i-1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i // 2] + 1, dp[i])
    if i % 3 == 0:
        dp[i] = min(dp[i // 3] + 1, dp[i])

print(dp[N])