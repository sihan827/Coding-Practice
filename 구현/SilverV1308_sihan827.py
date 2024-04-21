days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

sy, sm, sd = map(int, input().split())
ey, em, ed = map(int, input().split())

def check_yoon(year):
    if year % 400 == 0:
        return True
    if year % 100 != 0 and year % 4 == 0:
        return True
    return False

if ey - sy == 1000 and sm == em and ed >= sd:
    print('gg')
elif ey - sy == 1000 and em > sm:
    print('gg')
elif ey - sy > 1000:
    print('gg')
else:
    start_days = 0
    for i in range(1, sy):
        if check_yoon(i):
            start_days += 366
        else:
            start_days += 365

    start_days += sum(days[:sm])
    start_days += sd

    if check_yoon(sy) and sm > 2:
        start_days += 1

    end_days = 0
    for i in range(1, ey):
        if check_yoon(i):
            end_days += 366
        else:
            end_days += 365

    end_days += sum(days[:em])
    end_days += ed

    if check_yoon(ey) and em > 2:
        end_days += 1

    print('D-' + str(end_days - start_days))