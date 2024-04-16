import heapq

X = int(input())
sticks = []
# 가장 작은 막대를 고른다하여 힙 자료구조 생각
heapq.heappush(sticks, 64)

while sum(sticks) > X:
    st = heapq.heappop(sticks)
    heapq.heappush(sticks, st / 2)
    if sum(sticks) < X:
        heapq.heappush(sticks, st / 2)

# 다 자른 막대들의 수 출력
print(len(sticks))

########################################################
# 문제의 실제 의도는 비트마스킹
# 2로 나누는 문제는 비트 관련 문제인지 생각
# X를 2진수로 표현했을 때 1의 개수와 동일
print(str(bin(X)).count('1'))