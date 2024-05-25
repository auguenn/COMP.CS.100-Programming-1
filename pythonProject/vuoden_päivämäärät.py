"""
COMP.CS.100 Vuoden päivämäärät
Tekijä: Enna Augustin
Opiskelijanumero: 050235634
"""

def main() :
    kuukausi = 0
    päivä = 1

    for kuukausi in range(0,12):
        kuukausi += 1
        päivä += 1
        perjantai = päivä + 6
        if kuukausi == 2:
            for päivä in range(1,29):
                print(päivä, ".", kuukausi, ".", sep="")
        elif kuukausi == 4 or kuukausi == 6 or kuukausi == 9 or kuukausi == 11:
            for päivä in range(1,31):
                print(päivä, ".", kuukausi, ".", sep="")
        else:
            for päivä in range(1,32):
                print(päivä, ".", kuukausi, ".", sep="")


main()