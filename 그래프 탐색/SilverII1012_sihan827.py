import sys

## 중요: 기본 재귀횟수 1000인데 그래프가 2500까지의 크기를 가짐
## 따라서 재귀횟수 수정 요망
## 또는 BFS로 풀기
## 아래 풀이는 DFS
sys.setrecursionlimit(2500)
input = sys.stdin
T = int(input.readline())

## dfs 함수
## 상하좌우로 1 붙어 있는 것을 DFS 탐색한 후 방문처리하기
def dfs(graph, row, col, n, m):
    if row < 0 or col < 0 or row >= n or col >= m:
        return False
    if graph[row][col] != 1:
        return False
    else:
        graph[row][col] = 2
        dfs(graph, row+1, col, n, m)
        dfs(graph, row-1, col, n, m)
        dfs(graph, row, col+1, n, m)
        dfs(graph, row, col-1, n, m)
        return True

for _ in range(T):
    cnt = 0
    M, N, K = map(int, input.readline().split())
    field = [[0]*M for _ in range(N)]
    for _ in range(K):
        c, r = map(int, input.readline().split())
        field[r][c] = 1

    ## 방문하지 않고 1인 경우
    ## DFS로 주변 1 다 방문처리 한 후
    ## 벌레 하나 추가
    for i in range(N):
        for j in range(M):
            if dfs(field, i, j, N, M):
                cnt += 1
    
    print(cnt)