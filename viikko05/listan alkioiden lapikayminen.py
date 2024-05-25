"""
COMP.CS.100 listan alkioiden läpikäyminen
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
        if numbers > 0:
            five_numbers.append(numbers)
        i += 1

    print("The numbers you entered that were greater than zero were:")
    for numbers in five_numbers:
        print(numbers)






main()