from collections import defaultdict
import sys

N = int(input())

# 딕셔너리에 단어개수 세기
# 이전 문자랑 다른데 이미 카운트가 됐으면 연속문자열이 아닌것으로 판단
def seq_word(w: str):
    check_dict = defaultdict(int)
    check_dict[w[0]] += 1
    for i in range(1, len(w)):
        if w[i-1] != w[i] and check_dict[w[i]] > 0:
            return False
        check_dict[w[i]] += 1
    return True

cnt = 0

for _ in range(N):
    word = sys.stdin.readline().rstrip()
    if seq_word(word):
        cnt += 1

print(cnt)