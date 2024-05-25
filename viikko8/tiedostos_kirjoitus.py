"""
COMP.CS.100 tiedostot_kirjoitus
Tekijä: Enna Augustin
Opiskelijanumero: 050235634
"""

def main():

    filename = input("Enter the name of the file: ")

    try:
        file = open(filename, mode="w")
    except OSError:
        print(f"Writing the file {filename} was not successful.")
        return

    print("Enter rows of text. Quit by entering an empty row.")

    list = []
    while True:
        text_line = input()
        list.append(text_line)

        if text_line == "":
            break


        for i in range(0, len(list)):
            a = len(list)
        print(f"{a} {text_line}", file=file)


    file.close()

    print(f"File {filename} has been written.")

main()