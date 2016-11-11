# addrflipper
flips byte address and pads a '\x' to each for little endian exploits
eg: 41424344 => \x44\x43\x42\x41
    AABBCCDD => \xDD\xCC\xBB\xAA

# usage
./addrflipper.py 41424344

you can also import retaddr(addr) function to your exploit script and use it as part of it

# screens
![alt scree](https://snag.gy/Ml29jC.jpg)
-
![alt scree](https://snag.gy/6jVtkM.jpg)

# run online
[run on the cloud](https://repl.it/EVOR/1)
