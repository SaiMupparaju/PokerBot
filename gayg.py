from math import ceil


def func(day1: (int, int, int), day2:(int, int, int)):
    pass



def calc_yearDif(y1, y2):
    #num divisble by 4s in a year
    numLeapDays = int((y2 - y1 + (y1%4))/4)
    numLeapDays += 1 if (y1%4==0) else 0
    return 365*(y2-y1) + numLeapDays

def calc_year_Dif(y1, m1, y2, m2):