"""
COMP.CS.100 Hymiöt
Tekijä: Enna Augustin
Opiskelijanumero: 050235634
"""
def main(syöte) :
    syöte = input("How do you feel? (1-10) ")
    feel = int(syöte)
    if feel < 1 or feel > 10:
        print("Bad input!")
    elif feel < 4 and feel > 1:
        print("A suitable smiley would be :-(")
    elif feel == 10:
        print("A suitable smiley would be :-D")
    elif feel == 1:
        print("A suitable smiley would be :'(")
    else:
        if feel > 7:
            print("A suitable smiley would be :-)")
        else:
         print("A suitable smiley would be :-|")


main(1)
