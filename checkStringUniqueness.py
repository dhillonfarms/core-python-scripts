"""
Given a string,determine if it is compreised of all unique characters.
For example, the string 'abcde' has all unique characters and should return True.
The string 'aabcde' contains duplicate characters and should return false.
"""
__author__='https://github.com/dhillonfarms'

from collections import Counter

# Method 1
def check_uniqueness_counter(s1):
    for v in Counter(s1).values():
        if v > 1:
            return False
    return True

# Method 2
def check_uniqueness_string(s1):
    for s in range(len(s1)):
        if s1[s] in (s1[s+1:]):
            return False
    return True

s1 = 'abcde'
s2 = 'abcda'

print(check_uniqueness_counter(s1))
print(check_uniqueness_string(s1))

print(check_uniqueness_counter(s2))
print(check_uniqueness_string(s2))