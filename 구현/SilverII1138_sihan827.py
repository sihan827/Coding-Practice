N = int(input())
pre_num = list(map(int, input().split()))

answer = []
## 키가 큰사람부터 배치해야 작은사람은 큰사람의 개수를 측정 가능하므로 키가 큰 순으로 배치
for i in reversed(range(1, N+1)):
    if i == N:
        answer.append(i)
    else:
        # 위치 찾아서 삽입
        answer.insert(pre_num[i-1], i)

print(*answer)