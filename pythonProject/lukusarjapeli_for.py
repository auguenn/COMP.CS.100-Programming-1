"""
COMP.CS.100 Lukusarjapeli_for
Tekijä: Enna Augustin
Opiskelijanumero: 050235634
"""
def main() :
    x = int(input("How many numbers would you like to have? "))
    for i in range(1, x + 1) :
        if i % 3 == 0 and i % 7 == 0:
            print("zip boing")
        elif i % 3 == 0:
            print("zip")
        elif i % 7 == 0:
            print("boing")
        else:
            print(i)



main()