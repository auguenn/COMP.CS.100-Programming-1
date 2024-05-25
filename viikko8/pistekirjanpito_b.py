"""
COMP.CS.100 pistekirjanpito b
Tekijä: Enna Augustin
Opiskelijanumero: 050235634
"""

def main():
    scores = {}
    file_name = input("Enter the name of the score file: ")

    try:
        file =open(file_name, mode='r')
    except OSError:
        print("There was an error in reading the file.")
        return

    for file_line in file:
        file_line = file_line.rstrip()
        try:
            name, score = file_line.split()
        except ValueError:
            print("There was an erroneous line in the file:")
            print(file_line)
            return

        try:
            number = int(score)
        except ValueError:
            print("There was an erroneous score in the file:")
            print(score)
            return

        if name not in scores:
            scores[name] = number
        elif name in scores:
            scores[name] += number

    print("Contestant score:")
    for a in sorted(scores):
        print(f"{a} {scores[a]}")

    file.close()


main()