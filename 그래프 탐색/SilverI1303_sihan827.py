from collections import deque
import sys

input = sys.stdin

M, N = map(int, input.readline().split())
arr = []
visited = [[False] * M for _ in range(N)]
power_W = 0
power_B = 0

for _ in range(N):
    arr.append(list(input.readline().rstrip()))

# 너비우선탐색문제
# 너비우선탐색으로 시작 지점부터 인접한 같은 군사들을 세기
# 이미 방문한 경우는 세지 않음
def bfs(sr, sc):
    global power_W, power_B, visited, arr
    if visited[sr][sc]:
        return
    que = deque()
    que.append((sr, sc))
    adj = 1
    visited[sr][sc] = True
    while que:
        r, c = que.popleft()
        for dr, dc in zip([0, 0, 1, -1], [1, -1, 0, 0]):
            nr, nc = r + dr, c + dc
            if nr < 0 or nc < 0 or nr >= N or nc >= M:
                continue
            if visited[nr][nc]:
                continue
            if arr[r][c] == arr[nr][nc]:
                adj += 1
                visited[nr][nc] = True
                que.append((nr, nc))
    # 인접한 군사 수로 전투력 계산 
    if arr[sr][sc] == 'W': power_W += adj ** 2
    else: power_B += adj ** 2

# 모든 좌표에 대해 너비우선탐색 시행
for i in range(N):
    for j in range(M):
        bfs(i, j)

print(power_W, power_B)