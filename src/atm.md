# ATM

Brute force the pin. On linux it can be done with 

```bash
for i in $(seq 1 10000); do ./atm.out "$i"; done | grep -v "Wrong"
```

You can install Windows Subsystem for Linux [using these steps](https://www.kali.org/docs/wsl/wsl-preparations/). This gives you access to most Linux command line options.
