#!/usr/bin/python3


def xor(string1, string2):
    return_val = ""
    if len(string1) == len(string2):
        for i in range(len(string1)):
            return_val += chr(ord(string1[i]) ^ ord(string2[i]))
        return return_val
    return None


message = "ctfZero{not_the_key}"
encoded = "%RV($Q/^KE5iAT8-CIA%"

key = xor(message, encoded)

final_encoded = "%RV($Q/^QE5WYP$-[YK%"

print(xor(key, final_encoded))
