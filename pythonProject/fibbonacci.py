"""
COMP.CS.100 fibbonacci
Tekijä: Enna Augustin
Opiskelijanumero: 050235634
"""

def main() :
    a = 1
    b = 1

    numbers = int(input("How many Fibonacci numbers do you want? "))
    if numbers == 1:
        print("1.", a)
    else:
        print("1.", a)
        print("2.", b)

        for i in range(2,numbers):
            c = a+b
            a = b
            b = c
            print(i+1, end="")
            print(".", c)






main()