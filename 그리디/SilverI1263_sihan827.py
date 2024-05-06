import heapq

N = int(input())

works = []
for _ in range(N):
    t, s = map(int, input().split())
    heapq.heappush(works, (-s, t))

s, t = heapq.heappop(works)
remain = -s
heapq.heappush(works, (s, t))

while works:
    s, t = heapq.heappop(works)
    s = -s
    remain = remain - t if s > remain else s - t

print(remain if remain >= 0 else -1)