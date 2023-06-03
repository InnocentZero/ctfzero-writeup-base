#!/usr/bin/python3
file1 = open("trashhed", "r")

lines = file1.readlines()

flag = ""

for line in lines:
    val = [int(x) for x in line.split(" ")]
    flag += chr(val[0] ^ val[1])

print(flag)
