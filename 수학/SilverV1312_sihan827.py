A, B, N = map(int, input().split())
## 파이썬 정수 데이터타입은 크기가 무제한이므로 단순히 정수계산에서는 무식한 방법 사용 가능
## 부동소수점은 데이터타입 범위가 8바이트 제한이 있으므로 불가능
print(int(10 ** N * A // B ) % 10)