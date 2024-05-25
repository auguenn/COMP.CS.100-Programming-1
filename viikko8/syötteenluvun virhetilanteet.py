"""
COMP.CS.100 syötteenluvun virhetilanteet
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


def read_input(fraasi):
    """kyselee kaikkea kivaa
    :param: str muuttuja
    jeejee
    """

    do_the_loop = True

    while do_the_loop:

        muuttuja = input(fraasi)

        try:
            mm = int(muuttuja)
            while mm <= 0:
                muuttuja = input(fraasi)
                mm = int(muuttuja)
            return mm

        except ValueError:
            continue


def main():
    width = read_input("Enter the width of a frame: ")
    height = read_input("Enter the height of a frame: ")
    mark = str(input("Enter a print mark: "))

    print()
    print_box(width, height, mark)



if __name__ == "__main__":
    main()