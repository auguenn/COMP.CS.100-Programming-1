"""
COMP.CS.100 murtolukulaskin
Tekijä: Enna Augustin
Opiskelijanumero: 050235634
"""


class Fraction:
    """
    This class represents one single fraction that consists of
    numerator (osoittaja) and denominator (nimittäjä).
    """

    def __init__(self, numerator, denominator):
        """
        Constructor. Checks that the numerator and denominator are of
        correct type and initializes them.

        :param numerator: int, fraction's numerator
        :param denominator: int, fraction's denominator
        """

        # isinstance is a standard function which can be used to check if
        # a value is an object of a certain class.  Remember, in Python
        # all the data types are implemented as classes.
        # ``isinstance(a, b´´) means more or less the same as ``type(a) is b´´
        # So, the following test checks that both parameters are ints as
        # they should be in a valid fraction.
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError

        # Denominator can't be zero, not in mathematics, and not here either.
        elif denominator == 0:
            raise ValueError

        self.__numerator = numerator
        self.__denominator = denominator

    def return_string(self):
        """
        :returns: str, a string-presentation of the fraction in the format
                       numerator/denominator.
        """

        if self.__numerator * self.__denominator < 0:
            sign = "-"

        else:
            sign = ""

        return f"{sign}{abs(self.__numerator)}/{abs(self.__denominator)}"

    def simplify(self):
        """
        ygiuhijlökäkjlkölö
        :param a: kjnlkm-,_
        :param b: jknöml,äö.ä-
        :return: cgvhbkjnlmöl,ö.ä
        """
        c = greatest_common_divisor(self.__numerator,self.__denominator)
        a = self.__numerator // c
        b = self.__denominator // c
        self.__numerator = a
        self.__denominator = b

    def complement(self):
        """
        gcvhjbknkuhbkjnlm
        :return: gfghkjlcgjhkjhk
        """
        if self.__numerator < 0 and self.__denominator > 0:
            a = -1 * self.__numerator
            b= self.__denominator
        elif self.__denominator > 0 and self.__numerator > 0:
            a = -1 * self.__numerator
            b = self.__denominator
        elif self.__numerator > 0 and self.__denominator < 0:
            a = self.__numerator
            b = -1 * self.__denominator

        return Fraction(a,b)

    def reciprocal(self):
        """
        gfxchvjbknlhjbkj
        :return: cghbkjknlmvhjbmn
        """
        a = self.__denominator
        b = self.__numerator

        return Fraction(a,b)

    def get_denominator(self):
        """
        yfuguhklkjhgkjnkl
        :return: uhkjlö,öhbkjnlm
        """
        return self.__denominator

    def get_numerator(self):
        """
        tyfyugihojhgkjhkljölk
        :return: hgjklölkbhjnlml,
        """
        return self.__numerator

    def multiply(self,frac):
        """
        dryguihojfghkjklöl
        :param frac: fuygiuhijlöokhkjlöl
        :return: tfyguhiljfgjkl
        """
        denominator = self.__denominator * frac.get_denominator()
        numerator = self.__numerator * frac.get_numerator()
        return Fraction(numerator,denominator)

    def divide(self,frac):
        """
        cghvjhbknlmhjkjnl
        :param frac: cgvhjbknl
        :return: cghvjbknl
        """
        b = self.__denominator * frac.get_numerator()
        a = self.__numerator * frac.get_denominator()
        return Fraction(a,b)

    def add(self,frac):
        """
        ytfyugkhgjhvbknkkjbkn
        :param frac: ghjklghkjl
        :return: cghvjbknhkjlj
        """
        nume = (self.__numerator * frac.get_denominator()) + (
                frac.get_numerator() * self.__denominator)
        deno = self.__denominator * frac.get_denominator()
        return Fraction(nume,deno)

    def deduct(self,frac):
        """
        ytfyugiuhiljgjhkl
        :param frac: gfhkjlöiguhikjlö
        :return: vhbjlknmlkjn
        """
        nume = (self.__numerator * frac.get_denominator()) - (
                    frac.get_numerator() * self.__denominator)
        deno = self.__denominator * frac.get_denominator()
        return Fraction(nume, deno)

    def __lt__(self, frac):
        """
        fcghjklökhbjn.m,-l.,-
        :param frac: gvhbkjnlmö,
        :return: gjvhbkjnklm
        """
        deno = self.__denominator * frac.get_denominator()
        if (self.__numerator * frac.get_denominator())/deno < (frac.__numerator * self.__denominator)/deno:
            return True
        return False

    def gt(self, frac):
        """
        fyugiuhiljöklölhkbjnlmöl
        :param frac: cfghvjhbkjknlm
        :return: cghvjbknlml
        """
        deno = self.__denominator * frac.get_denominator()
        if (self.__numerator * frac.get_denominator()) / deno > (
                frac.__numerator * self.__denominator) / deno:
            return True
        return False

    def __str__(self):
        """
        fchgkjlövkhbjlknml
        :return: giuhijöokäkjbljölkäö
        """
        return self.return_string()

def greatest_common_divisor(a, b):
    """
    Euclidean algorithm. Returns the greatest common
    divisor (suurin yhteinen tekijä).  When both the numerator
    and the denominator is divided by their greatest common divisor,
    the result will be the most reduced version of the fraction in question.
    """

    while b != 0:
        a, b = b, a % b

    return a

def main():

    dict = {}
    while True:
        syöte = input("> ")

        if syöte == "add":
            luku = input("Enter a fraction in the form integer/integer: ")
            nimi = input("Enter a name: ")
            ml = luku.split("/")
            dict[nimi] = Fraction(int(ml[0]),int(ml[1]))


        elif syöte == "print":
            name = input("Enter a name: ")
            if name in dict:
                print(f"{name} = {dict[name]}")
            else:
                print(f"Name {name} was not found")

        elif syöte == "list":
            if dict == "":
                continue
            else:
                for i in sorted(dict):
                    print(f"{i} = {dict[i]}")

        elif syöte == "*":
            eka = input("1st operand: ")
            if eka not in dict:
                print(f"Name {eka} was not found")
                continue
            else:
                if Fraction:
                    num1 = dict[eka].get_numerator()
                    den1 = dict[eka].get_denominator()
                else:
                    ek = dict[eka].split("/")
                    num1 = int(ek[0])
                    den1 = int(ek[1])
            toka = input("2nd operand: ")
            if toka not in dict:
                print(f"Name {toka} was not found")
                continue
            else:
                if Fraction:
                    num2 = dict[toka].get_numerator()
                    den2 = dict[toka].get_denominator()
                else:
                    tk = dict[toka].split("/")
                    num2 = int(tk[0])
                    den2 = int(tk[1])
            denominator = den1 * den2
            numerator = num1 * num2
            f = numerator/denominator
            print(f"{dict[eka]} * {dict[toka]} = {num1*num2}/{den1*den2}")
            c = greatest_common_divisor(numerator, denominator)
            a = numerator // c
            b = denominator // c
            print(f"simplified {a}/{b}")

        elif syöte == "file":
            filename = input("Enter the name of the file: ")
            try:
                file = open(filename, mode="r")
                for file_line in file:
                    tunnus = file_line.split("=")
                    filenumbers = tunnus[1].split("/")
                    if tunnus[0].isalpha() and filenumbers[0].isnumeric() and filenumbers[0].isnumeric():
                        dict[tunnus[0]] = Fraction(int(filenumbers[0]),int(filenumbers[1]))
                    else:
                        raise FileNotFoundError

            except FileNotFoundError:
                print("Error: the file cannot be read.")


        elif syöte == "quit":
            print("Bye bye!")
            return

        else:
            print("Unknown command!")
            continue


main()