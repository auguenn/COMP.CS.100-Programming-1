"""
COMP.CS.100 projekti 1
Tekijä: Enna Augustin
Opiskelijanumero: 050235634
"""

def main():
    months = int(input("Enter the number of months: "))
    repetition_counter = 1
    sum = 0
    credits = 1

    # laskee keskiarvon annetuiden kuukausien ajalta
    while repetition_counter <= months:
        previous_months_credits = credits
        credits = int(input(f"Enter the number of credits in month {repetition_counter}: "))
        repetition_counter += 1
        sum += credits
        point_average = sum / (repetition_counter-1)

        # ehto kahden kuukauden opiskelutauolle
        if previous_months_credits == 0 and credits == 0:
            print()
            print("You did have too many study breaks!")
            return

    print()

    # ehdot keskiarvoille
    if point_average >= 5:
        print(f"You are a full time student and your monthly credit point average is {point_average:.1f}.")
    elif point_average < 5:
         print(f"Your monthly credit point average {point_average:.1f} does not classify you as a full time student.")

main()