"""
COMP.CS.100 Old macdonald
Tekijä: Enna Augustin
Opiskelijanumero: 050235634
"""
"""
COMP.CS.100 Programming 1
Template Song: Old MacDonald
"""

def print_verse(animal, sound):
    """tulostaa eläimen ja äänen"""
    a = str(animal)
    b = str(sound)
    print("Old MACDONALD had a farm")
    print("E-I-E-I-O")
    print("And on his farm he had a", animal)
    print("E-I-E-I-O")
    print("With a", sound, sound, "here")
    print("And a", sound, sound, "there")
    print("Here a", sound, end="")
    print(",", "there a", sound)
    print("Everywhere a", sound, sound)
    print("Old MacDonald had a farm")
    print("E-I-E-I-O")

def main():
    print_verse("cow", "moo")
    print()
    print_verse("pig", "oink")
    print()
    print_verse("duck", "quack")
    print()
    print_verse("horse", "neigh")
    print()
    print_verse("lamb", "baa")

main()


