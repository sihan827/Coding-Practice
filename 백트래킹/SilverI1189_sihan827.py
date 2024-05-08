import copy
import sys

input = sys.stdin

R, C, K = map(int, input.readline().split())
graph = []
for _ in range(R):
    graph.append(list(input.readline().rstrip()))
visited = [[False] * C for _ in range(R)]
length = []

def dfs(sr, sc, visited, l=1):
    global graph, length
    if sr < 0 or sc < 0 or sr >= R or sc >= C:
        return
    if graph[sr][sc] == 'T':
        return
    if not visited[sr][sc]:
        # 깊이우선탐색
        # 백트래킹으로 돌아갈 때 방문노드를 미방문으로 돌리는 것이 중요
        # 이러한 방법이 생각나지 않아 단순히 visited를 깊은복사로 사용하였으나
        # 이는 메모리에서 큰 손실 야기
        # 네 방향 정의해서 탐색 전 방문하고 탐색 후 방문상태 초기화
        # 또한 미리 정의된 그래프만 가지고 방문을 표현할 수 있는지도 고려해야함
        visited[sr][sc] = True
        dfs(sr+1, sc, copy.deepcopy(visited), l+1)
        dfs(sr-1, sc, copy.deepcopy(visited), l+1)
        dfs(sr, sc+1, copy.deepcopy(visited), l+1)
        dfs(sr, sc-1, copy.deepcopy(visited), l+1)
        if sr == 0 and sc == C-1:
            length.append(l)

dfs(R-1, 0, visited)
print(length.count(K))