"""
COMP.CS.100 TGIF
Tekijä: Enna Augustin
Opiskelijanumero: 050235634
"""

def main() :
    for day in range(1,32):
        if day == 3 or day == 3 + 7 or day == 3 + 7 + 7 or day == 3 + 3 * 7 or day == 3 + 4 * 7:
            print(day, "1.", sep=".")
    for day2 in range(1,29):
        if day2 == 7 or day2 == 7 + 7 or day2 == 7 + 7 + 7 or day2 == 7 + 3 * 7 or day2 ==3 + 4 * 7:
            print(day2, "2.", sep=".")
    for day in range (1,32):
        if day == 7 or day == 7 + 7 or day == 7 + 2 * 7 or day == 7 + 3 * 7 or day == 7 + 4 * 7:
            print(day, "3.", sep=".")
    for day3 in range(1,31):
        if day3 == 4 or day3 == 4 + 7 or day3 == 4 + 2 * 7 or day3 == 4 + 3 * 7 or day3 == 4 + 4 * 7:
            print(day3, "4.", sep=".")
    for day in range(1,32):
        if day == 2 or day == 2 + 7 or day == 2 + 2 * 7 or day == 2 + 3 * 7 or day == 2 + 4 * 7:
            print(day, "5.", sep=".")
    for day3 in range(1,31):
        if day3 == 6 or day3 == 6 + 7 or day3 == 6 + 2 * 7 or day3 == 6 + 3 * 7 or day3 == 6 + 4 * 7:
            print(day3, "6.", sep=".")
    for day in range(1,32):
        if day == 4 or day == 4 + 7 or day == 4 + 2 * 7 or day == 4 + 3 * 7 or day == 4 + 4 * 7:
            print(day, "7.", sep=".")
    for day in range(1,32):
        if day == 1 or day == 1 + 7 or day == 1 + 2 * 7 or day == 1 + 3 * 7 or day == 1 + 4 * 7:
            print(day, "8.", sep=".")
    for day3 in range(1,31):
        if day3 == 5 or day3 == 5 + 7 or day3 == 5 + 2 * 7 or day3 == 5 + 3 * 7 or day3 == 5 + 4 * 7:
            print(day3, "9.", sep=".")
    for day in range(1,32):
        if day == 3 or day == 3 + 7 or day == 3 + 2 * 7 or day == 3 + 3 * 7 or day == 3 + 4 * 7:
            print(day, "10.", sep=".")
    for day3 in range(1,31):
        if day3 == 7 or day3 == 7 + 7 or day3 == 7 + 2 * 7 or day3 == 7 + 3 * 7 or day3 == 7 + 4 * 7:
            print(day3, "11.", sep=".")
    for day in range(1,32):
        if day == 5 or day == 5 + 7 or day == 5 + 2 * 7 or day == 5 + 3 * 7 or day == 5 + 4 * 7:
            print(day, "12.", sep=".")

main()