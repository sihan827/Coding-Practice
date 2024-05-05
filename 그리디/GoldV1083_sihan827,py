N = int(input())
arr = list(map(int, input().split()))
S = int(input())

# 버블소트에 그리디를 추가한 문제: 정렬알고리즘을 항상 잘 알고있어야 한다
for i in range(N):
    if not S:
        break
    max_val = max(arr[i:i+S+1])
    max_idx = arr.index(max_val)
    while max_idx != i and S:
        arr[max_idx], arr[max_idx-1] = arr[max_idx-1], arr[max_idx]
        max_idx -= 1
        S -= 1
print(*arr)