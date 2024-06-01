from collections import defaultdict
from collections import deque
import sys

input = sys.stdin

N, M = map(int, input.readline().split())
graph = defaultdict(lambda: [])

for _ in range(M):
    fr, to = map(int, input.readline().split())
    fr, to = to, fr
    graph[fr].append(to)

# 시작노드로부터 갈 수 있는 모든 노드 개수가 가장 큰 시작노드 찾는 문제
check = [0]

# bfs로 해결
# dfs는 재귀제한 너무심함
for i in range(1, N+1):
    visited = [False] * (N+1)
    cnt = 1
    que = deque()
    que.append(i)
    visited[i] = True
    while que:
        s = que.popleft()
        for t in graph[s]:
            if not visited[t]:
                visited[t] = True
                que.append(t)
                cnt += 1
    check.append(cnt)

max_hack = max(check)
answer = []

for i in range(1, N+1):
    if check[i] == max_hack:
        answer.append(i)

print(*answer)