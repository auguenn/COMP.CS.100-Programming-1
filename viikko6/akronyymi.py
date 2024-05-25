"""
COMP.CS.100 akronyymi
Tekijä: Enna Augustin
Opiskelijanumero: 050235634
"""

def create_an_acronym(s):
    """
    yugkhjkjknll
    :param s: gjhk
    :return: rydtfygjk
    """
    return ''.join(word[0] for word in s.upper().split())
