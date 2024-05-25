"""
COMP.CS.100 käännä nimet
Tekijä: Enna Augustin
Opiskelijanumero: 050235634
"""
def reverse_name(s):
    """
    jhkukhj
    :param s:fhnjgjhm
    :return: frntyhnyht
    """
    b = s.strip()
    if "," in b:
        a = b.split(",")
        a.reverse()
        result = " ".join(a)
        return result.strip()
    elif "," not in b:
        return str(b).strip()



