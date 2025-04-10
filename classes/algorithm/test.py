def power_2(x):
    a = 2
    a = a + a
    a = a + 3
    a = a - a
    return x*x + a


# debug mode


def cal_bmi(h, w):
    h = h/100
    bmi = w/power_2(h)
    return bmi


print(cal_bmi(165, 70))
