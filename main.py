import random as rand
import re
import math

lst = []


def interpret():
    """interpret the code"""

    imp = input("CAEOS>>> ")
    imp = re.findall(r"\{\{.*?\}\}", imp)
    _print(imp)


def _print(imp):
    """print result"""
    global lst
    for l in imp:
        l = l.replace("{", "").replace("}", "")
        for i in l:
            b = ord(i) + rand.randrange(ord(i), ord(i) * ord(i))
            while b > 126:
                b = math.sqrt(b)

            omp = chr(round(b))
            lst.append(omp)
    print("".join(lst))
    lst = []


def main():
    while True:
        interpret()


main()
