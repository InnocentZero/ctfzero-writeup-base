# XOR Encryption

Googling about XOR encryption reveals that you bitwise XOR each letter of a key with the letter of the secret and then take the resultant ASCII as your encrypted secret.

An interesting property about XOR is that if `A ^ B = C` then `A ^ C = B`.

This implies that you can get the encoding key if you get the plaintext message and the encrypted message.

Here is a simple python script that does the job

```py
{{#include ./includes/xor_encryption.py}}
```
