import sys

datetimes = sys.stdin.readline().split()
month = datetimes[0]
day = int(datetimes[1][:-1])
year = int(datetimes[2])
hour, minute = map(int, datetimes[3].split(":"))

months = ['None', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
month = months.index(month)

def yoon(year):
    if not year % 400:
        return True
    if year % 100 and not year % 4:
        return True
    return False

days = [0, 31, 29 if yoon(year) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# 해당년도 전체일수와 현재일수 구해서 이걸로 시간 계산한 후 나눠서 percentage 구하기
total_days = sum(days)
cur_days = sum(days[:month]) + day - 1

print((cur_days * 24 * 60 + hour * 60 + minute) / (total_days * 24 * 60) * 100)