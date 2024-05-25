"""
COMP.CS.100 järjestetty alimerkkijono
Tekijä: Enna Augustin
Opiskelijanumero: 050235634
"""
list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "å", "ä", "ö"]

def longest_substring_in_order(text):
    """
    gykjhoiljklöj.ml
    :param text: yfghfhvujhmb
    :return: hgvbghnbfkyuhjvfyuhj
    """
    r = ''
    c = ''
    for char in text:
        if (c == ''):
            c = char
        elif (c[-1] <= char):
            c += char
        elif (c[-1] > char):
            if (len(r) < len(c)):
                r = c
                c = char
            else:
                c = char
    if (len(c) > len(r)):
        r = c
    return r
