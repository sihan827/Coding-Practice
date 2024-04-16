TC = int(input())

# m개의 다리 중 n개 선택
# mCn
def fact(N):
    if not N:
        return 1
    res = 1
    for i in range(1, N+1):
        res *= i
    return res

for _ in range(TC):
    n, m = map(int, input().split())
    # int형으로 출력되야 하는 것 주의
    print(fact(m) // (fact(m-n)*fact(n)))