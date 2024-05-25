"""
COMP.CS.100 Onko tylsää 3
Tekijä: Enna Augustin
Opiskelijanumero: 050235634
"""

def main():

    read_words = True

    while read_words:
        word = str(input("Bored? (y/n) "))
        if word == "y" or word =="Y":
            read_words = False
            print("Well, let's stop this, then.")
        elif word == "n" or word == "N":
            read_words = True
        else:
            print("Incorrect entry.")


main()