"""
COMP.CS.100 geometriset kuviot
Tekijä: Enna Augustin
Opiskelijanumero: 050235634
"""
from math import pi
from math import sqrt

def xx(muuttuja):
    """
    kbfekjrhekjgbkerjgbrkg
    :param muuttuja: hebkfjrbkrjjr
    :return: ggjhgjgkjhjk
    """
    pass

def square():
    """
    hbefkwejfkj,hrkej,gre
    :return: vjhejermhfkerjghrkejghkrje
    """
    side = float(input("Enter the length of the square's side: "))
    while side <= 0:
        side = float(input("Enter the length of the square's side: "))
    cir = 4 * side
    area = side ** 2
    print(f"The circumference is {cir:.2f}")
    print(f"The surface area is {area:.2f}")
    return side

def yy():
    """
    jhewfkejhgrekjlghlrk,gjrkth
    :return: fk,jhkler,gejrgr
    """
    pass

def retangle():
    """
    kbvvkjrelkjekjf,hekrgherkjgh,erkgre
    rgnlerjgnerk,hgrl
    :return: bdbvjhemdbvemjge
    """
    side1 = float(input("Enter the length of the rectangle's side 1: "))
    while side1 <= 0:
        side1 = float(input("Enter the length of the rectangle's side 1: "))
    side2 = float(input("Enter the length of the rectangle's side 2: "))
    while side2 <= 0:
        side2 = float(input("Enter the length of the rectangle's side 2: "))
    cir1 = side1 + side2 + side1 + side2
    area1 = side1 * side2
    print(f"The circumference is {cir1:.2f}")
    print(f"The surface area is {area1:.2f}")

def circle():
    """
    dmbnwkj,brkwjghkrjg,he,rgher,jghkrejghker
    kbekrgherkgjherlgiregke
    ghegrkgher
    :return: mhmfkwhjgkjwhkhgbghergkuerge
    """
    radius = float(input("Enter the circle's radius: "))
    while radius <= 0:
        radius = float(input("Enter the circle's radius: "))
    cir2 = 2 * pi * radius
    area2 = pi * (radius ** 2)
    print(f"The circumference is {cir2:.2f}")
    print(f"The surface area is {area2:.2f}")

def kk():
    """
    hjhmnbkejv,nelknrlenrtjk
    :return: shjwfehwgfkejghergjr
    """
    pass

def menu():
    """
    Print a menu for user to select which geometric pattern to use in calculations.
    """
    while True:
        answer = str(input("Enter the pattern's first letter or (q)uit: "))

        if answer == "s":
            square()

        elif answer == "r":
            retangle()

        elif answer == "c":
            circle()

        elif answer == "q":
            return

        else:
            print("Incorrect entry, try again!")

        # Empty row for the sake of readability.
        print()

def main():
    menu()
    print("Goodbye!")

if __name__ == "__main__":
    main()