"""
COMP.CS.100 rot_13b
Tekijä: Enna Augustin
Opiskelijanumero: 050235634
"""

def read_message():
    """
    rytfuyguhgkhlj
    :return: xycvgkhl
    """
    lista = []
    viesti = input()  # kysytään eka
    while viesti != "":  # ei tyhjä
        lista.append(viesti)  # lisätään listaan
        viesti = input()  # kysytään uusi
    return lista


def main():
    print("Enter text rows to the message. Quit by entering an empty row.")
    lista = read_message()


    print("The same, shouting:")
    for i in range(0, len(lista)):
        a = lista[i]
        print(a.upper())


if __name__ == "__main__":
    main()