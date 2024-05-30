from collections import Counter


alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
name = input().rstrip()

cnt = dict(Counter(name))
mid = ""

# 홀수개 카운트체크
tmp = 0
for c in cnt.keys():
    if cnt[c] % 2 != 0:
        tmp += 1
        mid += c

# 홀수 카운트가 1개 초과 시 팰린드롬 불가
if tmp > 1:
    print("I'm Sorry Hansoo")
else:
    pen = ""
    # 반개만 추가 후 반전
    for al in alphabet:
        if al in cnt:
            pen += al * (cnt[al] // 2)
    
    final_pen = pen + mid + pen[::-1]

    print(final_pen)