"""
COMP.CS.100 Virhetilanteet ohjelmoinnissa
Tekijä: Enna Augustin
Opiskelijanumero: 050235634
"""
"""
The price of a single ride bus ticket in Tampere
and surrounding areas on Aug 23rd, 2020.

The rules used by the program are:

  -----  -------
   Age    Price
  -----  -------
   >24     2.04
  17-24    1.47
   7-16    1.02
   0-6     0.00

Limited usefulness, the actual rules are more complex.
"""

def main(age):
    string = input("Please, enter your age: ")
    age = int(string)
    if age <= 24 and age >= 17:
        ticket_price1 = 1.47
        print("Your ride will cost:", ticket_price1)
    elif age <= 16 and age >= 7:
        ticket_price2 = 1.02
        print("Your ride will cost:", ticket_price2)
    elif age < 7:
        ticket_price3 = 0.00
        print("Your ride will cost:", ticket_price3)
    else:
        ticket_price4 = 2.04
        print("Your ride will cost:", ticket_price4)


main(20)


