"""
COMP.CS.100 projekti 2
Tekijä: Enna Augustin
Opiskelijanumero: 050235634

Ohjelma, joka laskee tietyn ajanjakson päivien lämpötilojen keskiarvon ja
mediaanin, sekä kertoo käyttäjälle mitkä päivät ovat lämpötilaltaan mediaanin
yläpuolella ja mitkä alapuolella.
"""


def lämpötilat():
    """
    kysyy käyttäjältä päivien lukumäärän ja kyseisten päivien lämpötilat
    :return: lista lämpötiloista
    """
    luvut = []
    päivät = int(input("Enter amount of days: "))

    # kysellään käyttäjältä lämpötilat pyydettyjen päivien ajalta ja lisätään
    # ne tyhjään listaan "luvut"
    for i in range(1, päivät + 1):
        lämpötilat = float(input(f"Enter day {i}. temperature in Celcius: "))
        luvut.append(lämpötilat)
        i += 1

    return luvut


def keskiarvo(luvut):
    """
    laskee lämpötilojen keskiarvon
    :param luvut: lista päivien lämpötiloista
    :return: float, lämpötilojen keskiarvo
    """

    # listan "luvut" summa jaetaan listan pituudella, jolloin saadaan
    # lämpötilojen keskiarvo
    ka = sum(luvut) / len(luvut)
    print(f"Temperature mean: {ka:.1f}C")

    return ka


def mediaani(luvut):
    """
    laskee lämpötilojen mediaanin
    :param luvut: lista päivien lämpötiloista
    :return: float, lämpötilojen mediaani
    """
    pituus = len(luvut)

    #järjestellään listan alkiot suuruusjärjestykseen mediaanin laskemista
    # varten
    lista = sorted(luvut)

    med = (sum(lista[pituus // 2 - 1:pituus // 2 + 1]) / 2.0,
                lista[pituus // 2])[pituus % 2]

    print(f"Temperature median: {med:.1f}C")

    return med if pituus else None


def luokittelu(luvut, med, ka):
    """
    luokittelee annetut päivät sen mukaan onko niiden lämpötila mediaanin ylä-
    vai alapuolella
    :param luvut: lista päivien lämpötiloista
    :param mediaani: float, lämpötilojen mediaani
    :param keskiarvo: float, lämpötilojen keskiarvo
    :return: int, kyseisen päivän järjestysnumero; float, kyseisen päivän
    lämpötila ja lämpötilan ero keskiarvoon verrattuna
    """

    print("Over or at median were: ")

    # tulostaa päivät ja lämpötilat listassa "luvut" jotka ovat suurempia tai
    # yhtäsuuria kuin mediaani
    i = 0
    while i < len(luvut):
        if luvut[i] >= med:
            print(f"Day {i + 1:2}. {luvut[i]:5.1f}C difference to mean: "
                  f"{luvut[i] - ka:5.1f}C")
        i += 1

    print()
    print("Under median were:")

    # tulostaa päivät ja lämpötilat listassa "luvut", jotka ovat pienempiä
    # kuin mediaani
    i = 0
    while i < len(luvut):
        if luvut[i] < med:
            print(f"Day {i + 1:2}. {luvut[i]:5.1f}C difference to mean: "
                  f"{luvut[i] - ka:5.1f}C")
        i += 1



def main():

    # kutsuu funktiota lämpötilat() ja liittää paluuarvon muuttujaan "luvut"
    luvut = lämpötilat()

    print()

    # kutsuu funktiota keskiarvo() ja liittää paluuarvon muuttujaan "keskiarvo"
    ka = keskiarvo(luvut)

    # kutsuu funktiota mediaani() ja liittää paluuarvon muuttujaan "mediaani
    med = mediaani(luvut)

    print()

    #kutsuu funktiota luokittelu()
    luokittelu(luvut, med, ka)


if __name__ == "__main__":
    main()