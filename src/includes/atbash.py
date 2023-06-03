#!/usr/bin/python3

from string import ascii_lowercase as lowercase
from string import ascii_uppercase as uppercase

string = input("Enter the string: ")

decrypt = ""
for i in string:
    if i in uppercase:
        decrypt += uppercase[-1 * uppercase.index(i) - 1]
    elif i in lowercase:
        decrypt += lowercase[-1 * lowercase.index(i) - 1]

print(decrypt)
