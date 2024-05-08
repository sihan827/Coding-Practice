from collections import defaultdict, deque
import sys

input = sys.stdin

N, M = map(int, input.readline().split())

# 그래프의 인접행렬을 딕셔너리나 리스트 자료구조로 표현하는 것이 중요
graph = defaultdict(lambda: {})
for _ in range(N-1):
    fr, to, dist = map(int, input.readline().split())
    graph[fr][to] = dist
    graph[to][fr] = dist


# 그래프에서 두 노드 사이의 거리 구할 땐 너비 우선 탐색 사용
def bfs(start, find):
    global graph
    que = deque()
    que.append((start, 0))
    visited = [False] * (N+1)
    visited[start] = True

    while que:
        node, dist = que.popleft()
        # 끝 노드 찾았으면 해당 거리 출력
        if node == find:
            return dist
        
        # 아니면 인접 노드 중 방문하지 않은 노드에 방문하여 거리 누적
        for n in graph[node]:
            if not visited[n]:
                visited[n] = True
                que.append((n, dist + graph[node][n]))

for _ in range(M):
    fr, to = map(int, input.readline().split())
    print(bfs(fr, to))