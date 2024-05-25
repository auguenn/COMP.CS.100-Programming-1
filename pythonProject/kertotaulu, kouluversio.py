"""
COMP.CS.100 kertotaulu, kouluversio
Tekijä: Enna Augustin
Opiskelijanumero: 050235634
"""

def main():
    num = 12


    num = int(input("Choose a number: "))


    for i in range(1, 11):
        print(i, '*', num, '=', num * i)
main()