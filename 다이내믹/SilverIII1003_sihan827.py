import sys
input = sys.stdin

T = int(input.readline())

# 탑다운으로 풀기엔 시간 너무오래걸림->바텀업으로 0, 1의 수를 점점 누적
for _ in range(T):
    N = int(input.readline())
    dp = [[0, 0] for _ in range(N+1)]
    dp[0][0], dp[0][1] = 1, 0
    # N = 0일 경우의 예외처리 주의
    if N > 0: dp[1][0], dp[1][1] = 0, 1

    for i in range(2, N+1):
        dp[i][0], dp[i][1] = dp[i-2][0] + dp[i-1][0], dp[i-2][1] + dp[i-1][1]

    print(dp[N][0], dp[N][1]) 