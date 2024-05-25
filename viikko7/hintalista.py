"""
COMP.CS.100 hintalista
Tekijä: Enna Augustin
Opiskelijanumero: 050235634
"""
PRICES = {
    "milk": 1.09, "fish": 4.56, "bread": 2.10,
    "chocolate": 2.70, "grasshopper": 13.25,
    "sushi": 19.90, "noodles": 0.97, "beans": 0.87,
    "bananas": 1.05, "Pepsi": 3.15,  "pizza": 4.15,
}


def main():
    name = input("Enter product name: ")
    b = name.strip()
    while b != "":  # ei tyhjä
        b = name.strip()
        if b in PRICES:
             print(f"The price of {b} is {PRICES[b]:.2f} e")
        elif b not in PRICES:
            print(f"Error: {b} is unknown.")
        name = input("Enter product name: ")
        b = name.strip()
    print("Bye!")


if __name__ == "__main__":
    main()
