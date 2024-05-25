"""
COMP.CS.100 rot_13c
Tekijä: Enna Augustin
Opiskelijanumero: 050235634
"""
def encrypt(text):
    """
    Encrypts its parameter using ROT13 encryption technology.

    :param text: str,  string to be encrypted
    :return: str, <text> parameter encrypted using ROT13
    """

    regular_chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                       "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
                       "w", "x", "y", "z"]

    encrypted_chars = ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
                       "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i",
                       "j", "k", "l", "m"]

    # TODO: implement encryption here
    encrypted = ""

    if text.isupper():
        index = regular_chars.index(text.lower())
        encrypted += encrypted_chars[index].upper()
    elif not text in regular_chars:
        return text
    else:
        index = regular_chars.index(text)
        encrypted += encrypted_chars[index]

    return encrypted

def row_encryption(text):
    """
    uygihujokl
    :param text: tfuygihkjl
    :return: rdytfughj
    """
    sana = []
    sana.append(text)
    aa = "".join(sana)

    letter = ""
    for i in range(0,len(aa)):
        s = encrypt(aa[i])
        letter += s
        i += 1
    return letter

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


    print("ROT13:")
    for i in range(0, len(lista)):
        a = lista[i]
        print(row_encryption(a))


if __name__ == "__main__":
    main()