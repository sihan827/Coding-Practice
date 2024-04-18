import heapq

word = input().rstrip()
# 힙으로 정렬
word_hq = []

# brute force로 모든 경우 다 구해서 힙에 푸시
for i in range(1, len(word)):
    for j in range(i+1, len(word)):
        str_1 = word[:i]
        str_2 = word[i:j]
        str_3 = word[j:]
        new_word = str_1[::-1] + str_2[::-1] + str_3[::-1]
        heapq.heappush(word_hq, new_word)

# 최상위 항목 팝
print(heapq.heappop(word_hq))