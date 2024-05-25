"""
COMP.CS.100 liukulukujen vertailu
Tekijä: Enna Augustin
Opiskelijanumero: 050235634
"""

EPSILON = 0.000000001
def compare_floats(a,b,EPSILON):
    """ jejjejejejejjje
    :param: floats laskeelaskeeelaskeee
    jgiukhlikjjwhfohfdöoeifjw.
    :return: floats kmwegwkuf,wkfwekfw
    """
    return float(abs(a - b)) < EPSILON



def main():
    a = float(input("a: "))
    b = float(input("b: "))
    if compare_floats(a,b,EPSILON):
        print(True)
    else:
        print(False)
    compare_floats(a,b,EPSILON)

main()