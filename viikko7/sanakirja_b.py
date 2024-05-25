"""
COMP.CS.100 lisäominaisuuksia turistisanakirjaan 1
Tekijä: Enna Augustin
Opiskelijanumero: 050235634
"""

def main():
    english_spanish = {"hey": "hola", "thanks": "gracias", "home": "casa"}

    print("Dictionary contents:")
    a = sorted(english_spanish)
    print(", ".join(a))

    while True:

        command = input("[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: ")

        if command == "W":
            word = input("Enter the word to be translated: ")
            if word in english_spanish:
                print(f"{word} in Spanish is {english_spanish[word]}")
            else:
                print("The word", word, "could not be found from the dictionary.")

        elif command == "A":

            word2 = input("Give the word to be added in English: ")
            esp = input("Give the word to be added in Spanish: ")
            english_spanish[word2] = esp

            print("Dictionary contents:")
            a = sorted(english_spanish)
            print(", ".join(a))

        elif command == "R":
            word3 = input("Give the word to be removed: ")
            if word3 not in english_spanish:
                print("The word", word3, "could not be found from the dictionary.")
            else:
                del english_spanish[word3]

        elif command == "P":
            for eng in sorted(english_spanish):
                print(eng,english_spanish[eng])

        elif command == "T":
            translated_text = ""
            text = input("Enter the text to be translated into Spanish: ")
            lause = text.split(" ")
            print("The text, translated by the dictionary:")
            for i in range(len(lause)):
                if lause[i] in english_spanish:
                    translated_text += english_spanish[lause[i]] + " "
                else:
                    translated_text += lause[i] + " "
            print(translated_text)

        elif command == "Q":
            print("Adios!")
            return

        else:
            print("Unknown command, enter W, A, R, P, T or Q!")

if __name__ == "__main__":
    main()

