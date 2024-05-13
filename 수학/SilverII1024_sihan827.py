N, L = map(int, input().split())


while L <= 100:
    tmp = 0
    result = []
    # 등차수열 합 공식을 이용해 시작 항의 값을 대략 추정
    start = int((2 * N + L - L ** 2) / (2 * L))
    end = start + L - 1

    # 시작 항이 음수이면 시작 항을 0으로 조정
    if start < 0:
        start += abs(start)
        end += abs(start)
    
    # 반복문으로 모든 항을 계산, 합도 계산
    for i in range(start, end+1):
        result.append(i)
        tmp += i

    # 계산한 항의 합이 입력과 동일 시 반복문 탈출
    if tmp == N:
        break
    # 아닐 시 초기화하고 수열의 항을 하나 추가
    else:
        tmp = 0
        result = []
        L += 1
        # 수열 항의 수 제한인 100을 넘을 시 -1만 남기고 반복문 탈출
        if L > 100:
            result.append(-1)
            break

# 결과 출력
print(*result)