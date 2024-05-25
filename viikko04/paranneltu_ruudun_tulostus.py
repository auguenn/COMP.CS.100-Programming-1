"""
COMP.CS.100 paranneltu ruudun tulostus
Tekijä: Enna Augustin
Opiskelijanumero: 050235634
"""
def print_box(height, width, border_mark="#", inner_mark=" "):
    """
    hjegfjehgejhvbjfhvfkvbiukvri
    :param width: bfjhrufryghrjg
    :param height: jfv3fg3fikrfkrj
    :param inner_mark: fhgefvhf3rfhj
    :param border_mark: fhjvfu3f3uj3
    :return: frhfburyfgbrgikrg4rg
    """
    i = 1
    while (i <= width):
        j = 1
        while (j <= height):
            if (i == 1 or i == width or j == 1 or j == height):
                print(border_mark, end='')
            else:
                print(inner_mark, end='')
            j = j + 1
        i = i + 1
        print()

def main():
    print_box(5, 4)
    print()
    print_box(3, 8, "*")
    print()
    print_box(5, 4, "O", "o")
    print()
    print_box(inner_mark=".", border_mark="O", height=4, width=6)




if __name__ == "__main__":
    main()