"""
COMP.CS.100 tulostuksen muotoilu
Tekijä: Enna Augustin
Opiskelijanumero: 050235634
"""


def main():
    for i in range(1, 11):
        for j in range(1, 11):
            print("%4d" % (i*j), end='')
        print()

main()