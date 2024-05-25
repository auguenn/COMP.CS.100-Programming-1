"""
COMP.CS.100 tehtävä
Tekijä: Enna Augustin
Opiskelijanumero: 050235634
"""
def main():
    """
    lnlekrlgn,g
    fhbrjkbg,erlke.jlhtrl.
    :return: rgbrbgk4rj,gj4l.h
    """
    print("Give 5 numbers:")
    five_numbers = []

    i = 0
    while i < 5:
        numbers = int(input("Next number: "))
        i += 1
        five_numbers.append(numbers)


    print("The numbers you entered, in reverse order:")

    for numbers in five_numbers[-1:-6:-1]:
        print(numbers)



main()