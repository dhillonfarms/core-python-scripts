# Calculate factorial for a number
__author__ = 'https://github.com/dhillonfarms'

# Using regular loops to calculate factorial
def get_factorial_loop(num):
    factorial_result = 1
    if num < 0:
        print("Factorial can only be calculated for positive integers!!")
    elif num == 0:
        print (factorial_result)
    else:
        for n in range (num-1, 0, -1):
            factorial_result *= n
        print (factorial_result)

# Using recursion to calculate factorial
def get_factorial_recursion(num):
    if num < 0:
        return "Factorial can only be calculated for positive integers!!"
    elif num == 0 or num == 1:
        return 1
    else:
        return (num-1) * get_factorial_recursion(num-1)



get_factorial_loop(0)
get_factorial_loop(-1)
get_factorial_loop(6)

print(get_factorial_recursion(0))
print(get_factorial_recursion(-1))
print(get_factorial_recursion(6))