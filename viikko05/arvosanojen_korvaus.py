"""
COMP.CS.100 arvosanojen korvaus
Tekijä: Enna Augustin
Opiskelijanumero: 050235634
"""

def convert_grades(lista):
    """
    bk,j,herkgjelrkgjrlekgerkg
    grejghrgkherjgreurjhgjme
    :param grades: gergjbhrgergjuergerg
    :return: grejghrgiuregerkugh
    """
    lenght = len(lista)
    for index in range(0,lenght):
        if lista[index] == 0:
            lista[index] = 0
        elif lista[index] == 1:
            lista[index] = 6
        elif lista[index] == 2:
            lista[index] = 6
        elif lista[index] == 3:
            lista[index] = 6
        elif lista[index] == 4:
           lista[index] = 6
        elif lista[index] == 5:
            lista[index] = 6


def main():
    grades = [0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0]
    convert_grades(grades)
    print(grades)
      # Should print [0, 6, 0, 6, 0, 6, 0, 6, 0, 6, 0]


if __name__ == "__main__":
    main()