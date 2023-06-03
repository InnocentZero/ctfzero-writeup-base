#!/usr/bin/python3

string = input("Enter encrypted string:\n")

for i in range(1, 26):
    decrypt = ""
    for j in string:
        decrypt += chr(ord("a") + (ord(j) - ord("a") + i) % 26)
    print("shift: " + str(i) + " decrypted string: " + decrypt)
