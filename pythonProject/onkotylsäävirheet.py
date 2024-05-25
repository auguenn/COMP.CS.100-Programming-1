"""
COMP.CS.100 Onko tylsää?
Tekijä: Enna Augustin
Opiskelijanumero: 050235634
"""
def main():

    read_words = True

    while read_words:
        word = str(input("Answer Y or N: "))
        if word == "n" or word == "N" or word == "y" or word == "Y":
            read_words = False
            print("You answered", word)
        else:
            print("Incorrect entry.")





main()




