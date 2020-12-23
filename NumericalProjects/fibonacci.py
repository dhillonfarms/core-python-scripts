"""
Discussing various approaches for generating fibonacci sequences

Using Python timeit module to find most efficient approach

"""

__author__ = 'https://github.com/dhillonfarms'

import timeit

# Using classic loop approach to get fibonacci series
def get_fibonacci_classic(num):
    a = 1
    b = 1
    output = []
    for n in range(num):
        output.append(a)
        c = a+b
        a = b
        b = c
    return output

# Using generators to get fibonacci series
def get_fibonacci_generators(num):
    a = 1
    b = 1
    for n in range(num):
        yield a
        c = a + b
        a = b
        b = c

# Using recursion to get fibonacci series
def get_fibonacci_recursion(num):
    # This method will return the nth element of fibonacci series
    if num == 0 or num == 1:
        return num
    else:
        return get_fibonacci_recursion(num-1)+get_fibonacci_recursion(num-2)

# Using memonization to get fibonacci series
store_fibonacci = {}
def get_fibonacci_memonization(num):
    if num == 0 or num == 1:
        store_fibonacci[num] = num
    if num not in store_fibonacci.keys():
        store_fibonacci[num] = get_fibonacci_memonization(num-1)+get_fibonacci_memonization(num-2)
    return store_fibonacci[num]

num = 20

print(get_fibonacci_recursion(10))
print(get_fibonacci_generators(10))
print(get_fibonacci_classic(10))
print(get_fibonacci_memonization(10))


print(timeit.timeit('get_fibonacci_classic(num)', 'from __main__ import get_fibonacci_classic, num', number=10000)*1000)
print(timeit.timeit('get_fibonacci_generators(num)', 'from __main__ import get_fibonacci_generators, num', number=10000)*1000)
print(timeit.timeit('get_fibonacci_recursion(num)', 'from __main__ import get_fibonacci_recursion, num', number=10000)*1000)