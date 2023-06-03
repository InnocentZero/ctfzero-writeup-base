#! /usr/bin/python3
from string import ascii_lowercase

num = 0

for i in ascii_lowercase:
    num = num ^ ord(i)

print(num)
