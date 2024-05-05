import sys

N = int(sys.stdin.readline())
# 다이나믹 프로그래밍 문제
# 같은 색깔을 연속적으로 선택할 수 없음을 고려
# 색깔이 여러 개이므로 2차원 dp 배열 사용
rgb_cost = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[0, 0, 0] for _ in range(N)]

dp[0][0], dp[0][1], dp[0][2] = rgb_cost[0][0], rgb_cost[0][1], rgb_cost[0][2]

for i in range(1, N):
    dp[i][0] = min(dp[i-1][1] + rgb_cost[i][0], dp[i-1][2] + rgb_cost[i][0])
    dp[i][1] = min(dp[i-1][0] + rgb_cost[i][1], dp[i-1][2] + rgb_cost[i][1])
    dp[i][2] = min(dp[i-1][0] + rgb_cost[i][2], dp[i-1][1] + rgb_cost[i][2])

print(min(dp[N-1][0], dp[N-1][1], dp[N-1][2]))