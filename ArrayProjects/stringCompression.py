"""
KIRAN just saw this code*************
Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it to become 'A4B4C5D2E4'.
For this problem, you can falsely "compress" strings of single or double letters.
For instance, it is okay for 'AAB' to return 'A2B1' even though this technically takes more space.

The function should also be case sensitive, so that a string 'AAAaaa' returns 'A3a3'.

"""
__author__='https://github.com/dhillonfarms'

from collections import Counter

def compress_string(s1):
    output = ''
    for k,v in Counter(s1).items():
        output=output+k+str(v)
    print(output)

compress_string('AAAABBBBCCCCCDDEEEEaaaabbbbccdddeeeeee')
