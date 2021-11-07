import time
import math
a = input("(c)lasic or (a)lternative operations?: ")
if a == "k":
    ac = input("first: ")
    co = input("*,/,+,-: ")
    bc = input("second: ")
    if co == "*":
        mulkis = float(ac) * float(bc)
        print(mulkis)
        time.sleep(10)
    elif co == "/":
        devkis = float(ac) / float(bc)
        print(devkis)
        time.sleep(10)
    elif co == "+":
        plukis = float(ac) + float(bc)
        print(plukis)
        time.sleep(10)
    elif co == "-":
        minkis = float(ac) - float(bc)
        print(minkis)
        time.sleep(10)
elif a == "a":
    aa = input("first: ")
    ao = input("to the power of(2) or squere root(v)?: ")
    if ao == "v":
        straa = float(aa)
        squerkis = math.sqrt(straa)
        print(squerkis)
        time.sleep(10)
    elif ao == "2":
        topwrkis = float(aa) * float(aa)
        print(topwrkis)
        time.sleep(10)
