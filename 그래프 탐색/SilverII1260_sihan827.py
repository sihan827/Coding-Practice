from collections import deque
from collections import defaultdict
import sys

input = sys.stdin

N, M, start = map(int, input.readline().split())
graph = defaultdict(lambda: [])

# defaultdict 기반 그래프 생성
for _ in range(M):
    fr, to = map(int, input.readline().split())
    if fr in graph:
        graph[fr].append(to)
    else:
        graph[fr] = [to]
    if to in graph:
        graph[to].append(fr)
    else:
        graph[to] = [fr]

# 작은 노드부터 방문이므로 각 연결노드 오름차순 정렬
for k in graph:
    graph[k].sort()

dfs_result = []
bfs_result = []

# 재귀기반 dfs 구현
def dfs(s, visited):
    global dfs_result
    visited[s] = True
    dfs_result.append(s)
    for t in graph[s]:
        if visited[t]:
            continue
        else:
            dfs(t, visited)
            #break

# 큐 기반 bfs 구현
def bfs(s, visited):
    global bfs_result
    que = deque()

    que.append(s)
    visited[s] = True

    while que:
        n = que.popleft()
        bfs_result.append(n)
        for t in graph[n]:
            if visited[t]:
                continue
            else:
                visited[t] = True
                que.append(t)


# 탐색 수행
visited = [False] * (N+1)
dfs(start, visited)
visited = [False] * (N+1)
bfs(start, visited)

print(*dfs_result)
print(*bfs_result)