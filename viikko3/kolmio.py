"""
COMP.CS.100 kolmio
Tekijä: Enna Augustin
Opiskelijanumero: 050235634
"""

from math import sqrt

def area(a, b, c):
    """laskee pinta-alaaa
    :param result: float
    """
    result = float(sqrt(((a + b + c) * 0.5) * (((a + b + c) * 0.5) - a) * (((a + b + c) * 0.5) - b) * (((a + b + c) * 0.5) - c)))
    return result

def main():
    a = float(input("Enter the length of the first side: "))
    b = float(input("Enter the length of the second side: "))
    c = float(input("Enter the length of the third side: "))
    print(f"The triangle's area is {area(a, b, c):.1f}")


if __name__ == "__main__":
    main()