"""
COMP.CS.100 tuote
Tekijä: Enna Augustin
Opiskelijanumero: 050235634
"""


class Product:
    """
    This class defines a simplified product for sale in a store.
    """
    def __init__(self, product_name, price, sale=0):
        """
        fuygiuhiojpokhlkjöäghlkjölkä
        :param product_name: tfyghuiopoiåghjlkölä
        :param price: vhhjlköä
        :param sale_percentage:tfuygihuoijofghufuyguhlj
        """
        self.__name = product_name
        self.__price = price
        self.__sale = sale

    def get_price(self):
        """
        tdfygyhkjtfdyhkj
        tydfuygiuhilkjöl
        :return: fxcyghhjklydgtfj
        """
        if self.__sale != 0:
            x = (100 - self.__sale) / 100
            sale_price = x * self.__price
            return sale_price
        else:
            return self.__price

    def set_sale_percentage(self, sale):
        """
        ytfyjgkhljöfxcghvjbknlydfghkjlö
        :param sale_percentage: tsrdtyfyugiuhijo
        :return: fxcghvjbknlmlydfgfkjl
        """


        self.__sale = sale



    def printout(self):
        """
        fygkhjlköcgvjhbknlmö,ö
        :return: tfuygihijköoptfuygiuhjlök
        """

        print(self.__name)
        print(f"  price: {self.__price:.2f}")
        print(f"  sale%: {self.__sale:.2f}")



def main():

    test_products = {
        "milk":   1.00,
        "sushi": 12.95,
    }

    for product_name in test_products:
        print("=" * 20)
        print(f"TESTING: {product_name}")
        print("=" * 20)


        prod = Product(product_name, test_products[product_name])

        prod.printout()
        print(f"Normal price: {prod.get_price():.2f}")

        print("-" * 20)

        prod.set_sale_percentage(10.0)
        prod.printout()
        print(f"Sale price: {prod.get_price():.2f}")

        print("-" * 20)

        prod.set_sale_percentage(25.0)
        prod.printout()
        print(f"Sale price: {prod.get_price():.2f}")

        print("-" * 20)





if __name__ == "__main__":
    main()