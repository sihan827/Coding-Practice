import sys

N = int(sys.stdin.readline())
arr = []

## 백트래킹으로 가능한 모든 경우의 수 탐색
## 현재 자릿수보다 작은 자릿수만 뒤에 붙을 수 있음을 이용
def backtrack(num, prev):
    global arr
    if num < 0: return
    arr.append(prev)
    for i in range(num):
        backtrack(num-i-1, int(str(prev)+str(num-i-1)))

for i in range(10):
    backtrack(i, i)

if len(arr) <= N:
    print(-1)
else:
    # 마지막에 정렬해서 N번째 출력
    arr.sort()
    print(arr[N])