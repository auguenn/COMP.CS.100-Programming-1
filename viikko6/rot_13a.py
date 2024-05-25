"""
COMP.CS.100 rot_13a
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




