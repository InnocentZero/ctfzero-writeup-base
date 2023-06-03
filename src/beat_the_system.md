# Beat the System

Here is the python code that was running behind the binary

```py
import time

num = int(input("Enter a number to beat the system:"))
while num < 99999999999999999999999999999999999999999999999999999999 and num > 0:
    print("Welp, looks like you're stuck here")
    num += 0.05
    time.sleep(2)

print("Flag: ctfZero{0verruL3_T#3_$ys+3m}")
```

So this basically wanted you to overflow the integer to make it a negative number. This can be used in situations to override an entire section of code in a binary and skip crucial instructions from happening, making the binary crash.
