N = int(input())
words = []

for _ in range(N):
    words.append(input().rstrip())

# 길이가 긴 단어들은 접두사가 될 수 없으므로 
# 최대한 이들을 포함하는 식으로 그리디 알고리즘 구성
words.sort(reverse=True, key=lambda x: len(x))
xwords = [words[0]]

for word in words[1:]:
    is_pre = False
    for xword in xwords:
        if xword.startswith(word):
            is_pre = True
            break
    if not is_pre:
        xwords.append(word)

print(len(xwords))