import sys

N = sys.stdin.readline().rstrip()
answer = ""

cnt = 0
check = True
# 문자열 길이 최대 50이므로 그냥 반복문으로 가능
# 사전순이므로 항상 AAAA를 먼저 넣고 남는 곳에 BB를 채운다는 느낌
# 즉 그리디 알고리즘
for i in N:
    if i == 'X': 
        cnt += 1
    else: 
        if cnt % 4 == 2 or cnt % 4 == 0:
            if cnt == 2: answer += "BB"
            elif cnt == 0: pass
            else:
                answer += "AAAA" * (cnt // 4) + "BB" * (cnt % 4 // 2)
            answer += "."
        else:
            check = False
            break
        cnt = 0

# 마지막에 점이 아닐 시 처리를 안해서 따로 해줌
if N[-1] != ".":
    if cnt % 4 == 2 or cnt % 4 == 0:
        if cnt == 2: answer += "BB"
        elif cnt == 0: pass
        else:
            answer += "AAAA" * (cnt // 4) + "BB" * (cnt % 4 // 2)
    else:
        check = False

print(answer) if check else print(-1)