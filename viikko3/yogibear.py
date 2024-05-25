"""
COMP.CS.100 yogibear
Tekijä: Enna Augustin
Opiskelijanumero: 050235634
"""
def repeat_name(name, times):
    """tulostaa karhun nimeä"""

    repetition_counter = 1

    for i in range(0, times):
        print(name,", ", name, " Bear", sep="")
        i += 1

def verse(line, name):
    """tulostaa lauseen ja nimen"""
    c = str(line)
    d = str(name)
    for i in range(1,15):
        if i == 1 or i == 3 or i == 7:
            print(line)
        elif i == 2:
            print(name,", ", name, sep="")
        elif i == 4:
            repeat_name(name, 3)
        elif i == 8:
            repeat_name(name, 1)


def main():
    verse("I know someone you don't know", "Yogi")
    print()
    verse("Yogi has a best friend too", "Boo Boo")
    print()
    verse("Yogi has a sweet girlfriend", "Cindy")



if __name__ == "__main__":
    main()