"""
COMP.CS.100 tiedostot_lukeminen
Tekijä: Enna Augustin
Opiskelijanumero: 050235634
"""

def main():

    filename = input("Enter the name of the file: ")

    try:
        file = open(filename, mode="r")
    except OSError:
        print(f"Error: opening the file '{filename}' failed!")
        return

    line_count = 0
    for file_line in file:
        file_line = file_line.rstrip()
        if file_line != "\n":
            line_count += 1
        print(line_count, file_line)

    file.close()

main()