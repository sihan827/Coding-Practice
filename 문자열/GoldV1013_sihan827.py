import re

TC = int(input())

for _ in range(TC):
    signal = input().rstrip()
    # 정규표현식 패턴 정의
    patt = re.compile(r'(100+1+|01)+')
    # 해당 패턴과 문자열이 전부 일치하나 체크
    if patt.fullmatch(signal):
        print('YES')
    else:
        print('NO')