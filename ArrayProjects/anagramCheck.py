# Simple script to check whether two strings are anagrams
__author__='https://github.com/dhillonfarms'

def check_anagram(s1,s2):
    s1 = s1.replace(" ","")
    s2 = s2.replace(" ","")
    if len(s1) != len(s2):
        return False

    if sorted(s1.lower()) == sorted(s2.lower()):
        return True
    return False

s1 = "Clint Eastwood"
s2 = "old west action"

print(check_anagram(s1,s2))
