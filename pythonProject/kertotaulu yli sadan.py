"""
COMP.CS.100 kertotaulu yli sadan
Tekijä: Enna Augustin
Opiskelijanumero: 050235634
"""
def main() :

    num = 101
    num = int(input("Choose a number: "))

    for i in range(1, 101):
        print(i, "*", num, "=", num * i)
        while num * i > 100:
            return


main()