import heapq

input = open("input.txt", "r")

N = int(input.readline())
# 힙으로 정렬
sort_hq = []

for _ in range(N):
    word = input.readline().rstrip()
    # 우선순위가 단어길이이므로 튜플에 (길이, 단어) 순으로 넣어서 푸시
    heapq.heappush(sort_hq, (len(word), word))

prev = ""
while sort_hq:
    # 하나씩 팝해가면서 확인
    _, curr = heapq.heappop(sort_hq)
    # 만약 이전 단어와 동일하면 스킵
    if curr == prev:
        continue
    else:
        print(curr)
    prev = curr