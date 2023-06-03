#!/usr/bin/python3

from string import ascii_letters


def vigenere_decode(key, encryption):
    decrypt = ""
    key = key.lower()
    encryption = encryption.lower()
    for i in range(len(encryption)):
        if encryption[i] in ascii_letters:
            decrypt += chr(
                (ord(encryption[i]) - ord(key[i % len(key)])) % 26 + ord("a")
            )
        else:
            decrypt += encryption[i]
    return decrypt


print(vigenere_decode("lemon", "LXFOPVEFRNHR"))
