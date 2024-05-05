L, R = map(int, input().split())

L_digit = len(str(L))
R_digit = len(str(R))

# 자릿수 다르면 8이 들어가지 않는 경우 무조건 존재
if L_digit != R_digit:
    print(0)
# 자릿수 같으면 앞자리부터 비교하여 8이 아닐때까지 비교->8이면 카운트
else:
    digit = 10 ** (L_digit - 1)
    L_digits = []
    R_digits = []
    while digit >= 1:
        L_digits.append(L // digit)
        R_digits.append(R // digit)
        L = L % digit
        R = R % digit
        digit = digit // 10
    
    cnt = 0
    for i, j in zip(L_digits, R_digits):
        if i == j: 
            if i == 8:
                cnt += 1
        else:
            break
    
    print(cnt)