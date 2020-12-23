# Simple script to check whether a string is a palindrome
__author__='https://github.com/dhillonfarms'

def check_if_palindrome(str1):
    if len(str1) < 1:
        return True
    else:
        if str1[0]==str1[-1]:
            return check_if_palindrome(str1[1:-1])
        else:
            return False

print(check_if_palindrome('abcde'))
print(check_if_palindrome('madam'))


