'''
Get values of pi upto nth digit using:
    1. Gregory-Leibniz series where pi =  (4/1) - (4/3) + (4/5) - (4/7) + (4/9) - (4/11) + (4/13) - (4/15) ...
    2. Nilkantha series where pi = pi = 3 + 4/(2*3*4) - 4/(4*5*6) + 4/(6*7*8) - 4/(8*9*10) + 4/(10*11*12) - 4/(12*13*14)

Use timeit module to compare performance of both series
'''
__author__ = 'https://github.com/dhillonfarms'

from decimal import Decimal
import timeit
import math

def get_pi_gregory_leibniz_series(iterationCount):
    if iterationCount < 10000:
        print("The number you entered is very low, setting it to default minimum value of 10000 iterations.")
        iterationCount = 10000
    sum_pi = Decimal(4/1)
    minus_sum = Decimal(0)
    plus_sum = Decimal(0)
    plus_minus_check = 1
    if iterationCount % 2 != 0:
        iterationCount = iterationCount + 1
    for n in range(3, iterationCount, 2):
        if plus_minus_check  == 0:
            plus_sum = plus_sum + Decimal((4 / n))
            plus_minus_check = 1
        else:
            minus_sum = minus_sum + Decimal((4/n))
            plus_minus_check = 0
    return sum_pi+plus_sum-minus_sum

def get_pi_nilkantha_series(iterationCount):
    sum_pi = Decimal(3/1)
    minus_sum = Decimal(0)
    plus_sum = Decimal(0)
    plus_minus_check = 0
    for n in range(2, iterationCount, 2):
        if plus_minus_check  == 0:
            plus_sum = plus_sum + Decimal((4 / (n*(n+1)*(n+2))))
            plus_minus_check = 1
        else:
            minus_sum = minus_sum + Decimal((4 / (n*(n+1)*(n+2))))
            plus_minus_check = 0
    return sum_pi+plus_sum-minus_sum

# Defining
num = 25000

pi_gl = get_pi_gregory_leibniz_series(num)
pi_nl = get_pi_nilkantha_series(num)
print("Direct value of pi is: {}\n".format(Decimal(math.pi)))
print("Value of pi upto {} decimal points using Gregory Leibniz series is: {}\n".format(
    num, pi_gl))
print("Value of pi upto {} decimal points using Nilkantha series is: {}\n".format(
    num, pi_nl))



print("Gregory Leibniz performance (milliseconds): {}\n".format(
    timeit.timeit('get_pi_gregory_leibniz_series(num)', 'from __main__ import get_pi_gregory_leibniz_series, num', number=100)*1000))
print("Nilkantha performance (milliseconds): {}".format(
    timeit.timeit('get_pi_nilkantha_series(num)', 'from __main__ import get_pi_nilkantha_series, num', number=100)*1000))
