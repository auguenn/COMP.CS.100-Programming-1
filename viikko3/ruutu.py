"""
COMP.CS.100 ruutu
Tekijä: Enna Augustin
Opiskelijanumero: 050235634
"""
def print_box(width, height, mark):
    """tulostaa ruudun
    width = param int
    height = param int
    mark = param str
    """
    for i in range (1,height+1):
        rivi = width * mark
        print(rivi)
        i += 1


def main():
    """kutsuu funktion print_box"""
    width = int(input("Enter the width of a frame: "))
    height = int(input("Enter the height of a frame: "))
    mark = str(input("Enter a print mark: "))

    print()
    print_box(width, height, mark)


if __name__ == "__main__":
    main()