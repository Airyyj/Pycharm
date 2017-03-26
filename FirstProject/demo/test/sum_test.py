# -*- coding: utf-8 -*-

def sum_test(baseNum,growthRate,time):

    if time == 1:
        return baseNum
    else:
        return baseNum * (1+growthRate)**(time-1)




baseNum = 713.78

growthRate = 0.0115

time = 241

print sum_test(baseNum,growthRate,time)