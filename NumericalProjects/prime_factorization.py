'''
 Prime Factorization -- Find the prime factors of a number if any

 Following approach is used:

 1. For a given number, divide with 2 until there is a remainder
 2. The number left would be odd, so start dividing by odd numbers
 starting with 3 until square root of the main number since the factors keep repeating after square root.
 3. If number is not divisible until square root of itself, then that number is also a prime factor.
'''
__author__ = 'https://github.com/dhillonfarms'

import math

def get_prime_factors(num):
    output=str(num)+"-"
    while (num%2 == 0):
        output=output+str(2)+" * "
        num = num/2
    for i in range (3, int(math.sqrt(num))+1, 2):
        while (num%i)==0:
            output = output+str(i) + " * "
            num = num/i
    if (int(num) != 1):
        output = output+str(int(num)) + " * "
    if output.split("-")[1].rstrip()[:-1]:
        print("The number {} can be represented with prime factors as {}".format(output.split("-")[0], output.split("-")[1].rstrip()[:-1]))
    else:
        print("The number {} has no prime factors".format(num))

def check_if_prime(num):
    if num == 2 or num == 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    else:
        check = 0
        for n in range(5, int(math.sqrt(num)+1)):
            if num % n == 0:
                check = 1
                break
        return check == 0



get_prime_factors(68)
get_prime_factors(100)
get_prime_factors(315)
get_prime_factors(99)

print(check_if_prime(2))
print(check_if_prime(5))
print(check_if_prime(4))
print(check_if_prime(57))