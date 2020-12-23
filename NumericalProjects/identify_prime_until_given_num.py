# Script to find prime numbers until a given number
__author__ = 'https://github.com/dhillonfarms'

import math

# Function to check whether a given number is prime
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

# Find list of all prime numbers until a given number
def identify_prime_until(num):
    if num < 2:
        return "Input must be greater than 2!"
    elif num==2:
        return [2]
    elif num==3:
        return [2, 3]
    else:
        list1 = []
        for n in range(3, num, 2):
            if check_if_prime(n):
                list1.append(n)
        if list1:
            list1.insert(0,2)
            return list1
        else:
            return "No prime numbers found"

print(identify_prime_until(2))
print(identify_prime_until(20))
print(identify_prime_until(3))
print(identify_prime_until(5))
print(identify_prime_until(50))

