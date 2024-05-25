"""
COMP.CS.100 pistekirjanpito a
Tekijä: Enna Augustin
Opiskelijanumero: 050235634
"""

def main():
    scores = {}
    file_name = input("Enter the name of the score file: ")

    file =open(file_name, mode='r')
    for file_line in file:
        file_line = file_line.rstrip()
        name, score = file_line.split()
        number = int(score)

        if name not in scores:
            scores[name] = number
        elif name in scores:
            scores[name] += number

    print("Contestant score:")
    for a in sorted(scores):
        print(f"{a} {scores[a]}")

    file.close()


main()