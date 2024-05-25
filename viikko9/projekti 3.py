"""
COMP.CS.100 kurssirekisteri
Tekijä: Enna Augustin
Opiskelijanumero: 050235634

Ohjelma, johon talletetaan tiedostosta yliopiston kursseja. Kaikkien kurssien
luettelo voidaan tulostaa tai voidaan rajata pelkästään yhden oppiaineen
kursseihin ja tulostaa nämä. Voidaan myös lisätä ja poistaa kursseja
luettelosta. Voidaan myös selvittää, kuinka monta opintopistettä on mahdollista
saada yhden oppiaineen kursseista yhteensä.
"""


def lisäys(informaatio, oppiaine, kurssi, pisteet):
    """
    Lisää kurssiluetteloon oppiaineen, kurssin ja opintopisteet. Jos oppiaine
    on jo olemassa, lisää kyseiseen oppiaineeseen kurssin ja sen opintopisteet.

    :param informaatio: dict, sanakirja, jossa avaimina oppiaineet ja
    hyötykuormana toinen sanakirja, jossa avaimina kurssien nimet ja
    hyötykuormana opintopisteet.
    :param oppiaine: str, alkuperäisen sanakirjan avain
    :param kurssi: str, alkuperäisen sanakirjan hyötykuorma-sanakirjan avain
    :param pisteet: int, alkuperäisen sanakirjan hyötykuorma-sanakirjan
    hyötykuorma
    :return: dict, uusi sanakirja, johon lisätty uutena hyötykuormana uusi
     oppiaine-kurssi -pari
    """

    # Tarkistaa onko oppiaine alkuperäisessä sanakirjassa
    if oppiaine in informaatio:
        print(f"Added course {kurssi} to department {oppiaine}")

    elif oppiaine not in informaatio:
        # Luodaan uudelle oppiaineelle tyhjä sanakirja, johon lisätään avaimena
        # kyseisen oppiaineen kurssi ja hyötykuormana opintopisteet
        informaatio[oppiaine] = {}
        print(f"Added department {oppiaine} with course {kurssi}")

    # Lisätään alkuperäiseen sanakirjaan (luetteloon) uusi oppiaine ja siihen
    # liitetty kurssi sekä opintopisteet.
    informaatio[oppiaine][kurssi] = pisteet



def opintopisteet(informaatio, oppiaine):
    """
    Laskee käyttäjän syöttämän oppiaineen kaikkien kurssien opintopisteet
    yhteen

    :param informaatio: dict, sanakirja, jossa avaimina oppiaineet ja
    hyötykuormana toinen sanakirja, jossa avaimina kurssien nimet ja
    hyötykuormana opintopisteet.
    :param oppiaine: str, alkuperäisen sanakirjan avain
    :return: str, kysytty oppiaine; int, oppiaineen opintopisteiden yhteissumma
    """

    # Tarkistaa onko oppiaine sanakirjassa
    if oppiaine not in informaatio:
        print("Department not found!")
        return

    if oppiaine in informaatio:
        summa = 0
        # Laskee oppiaineen kurssien opintopisteet yhteen
        for kurssi in sorted(informaatio[oppiaine]):
            summa += int(informaatio[oppiaine][kurssi])
        print(f"Department {oppiaine} has to offer {summa} cr.")



def poisto(informaatio, oppiaine, kurssi):
    """
    Poistaa alkuperäisestä sanakirjasta oppiaineen tai oppiaineen sisällä
    olevan kurssin riippuen käyttäjän antamasta syötteestä

    :param informaatio: dict, sanakirja, jossa avaimina oppiaineet ja
    hyötykuormana toinen sanakirja, jossa avaimina kurssien nimet ja
    hyötykuormana opintopisteet.
    :param oppiaine: str, alkuperäisen sanakirjan avain
    :param kurssi: str, alkuperäisen sanakirjan hyötykuorma-sanakirjan avain
    :return: dict, uusi sanakirja, josta poistettu käyttäjän syötteestä
     riippuen joko kokonainen avain (oppiaine) tai sitten hyötykuorman sisältä
     avain (kurssi).
    """

    # Tarkistaa onko oppiaine sanakirjassa
    if oppiaine not in informaatio:
        print(f"Department {oppiaine} not found!")

    elif oppiaine in informaatio:
        # Tarkistaa onko kurssi oppiaineessa
        if kurssi in informaatio[oppiaine]:
            # Poistaa olemassaolevan kurssin
            del informaatio[oppiaine][kurssi]
            print(f"Department {oppiaine} course {kurssi} removed.")
        elif kurssi not in oppiaine:
            print(f"Course {kurssi} from {oppiaine} not found!")
        else:
            # Poistaa olemassaolevan oppiaineen
            del informaatio[oppiaine]
            print(f"Department {oppiaine} removed.")



def tulosta_kaikki(informaatio):
    """
    Tulostaa sanakirjassa olevien kurssien nimet ja opintopisteet oppiaineiden
    mukaan aakkosjärjestyksessä

    :param informaatio: dict, sanakirja, jossa avaimina oppiaineet ja
    hyötykuormana toinen sanakirja, jossa avaimina kurssien nimet ja
    hyötykuormana opintopisteet.
    :return: str, aakkostettu luettelo oppiaineista ja niihin kuuluvista
    kursseista aakkosjärjestyksessä. Kurssien perässä kerrottu myös saatavilla
    olevat opintopisteet.
    """

    # Järjestetään oppiaineet aakkosjärjestykseen
    for oppiaine in sorted(informaatio):
        # Tulostetaan aakkostetut oppiaineet
        print(f"*{oppiaine}*")

        # Järjestetään oppiaineiden kurssit aakkosjärjetykseen
        for kurssi in sorted(informaatio[oppiaine]):
            # Tulostetaan aakkostetut kurssit oppiaineiden alle
            print(kurssi, ":", informaatio[oppiaine][kurssi], "cr")



def tulosta_oppiaine(informaatio, oppiaine):
    """
    Tulostaa käyttäjän syötteen perusteella pyydetyn oppiaineen kurssit

    :param informaatio: dict, sanakirja, jossa avaimina oppiaineet ja
    hyötykuormana toinen sanakirja, jossa avaimina kurssien nimet ja
    hyötykuormana opintopisteet.
    :param oppiaine: str, alkuperäisen sanakirjan avain
    :return: str, aakkostettu luettelo pyydetyn oppiaineen kursseista ja niiden
    opintopistetistä
    """

    # Tarkistaa onko oppiaine sanakirjassa
    if oppiaine not in informaatio:
        print("Department not found!")
        return

    # Tulostaa käyttäjän pyytämän oppiaineen
    print(f"*{oppiaine}*")

    # Järjestelee kurssit aakkosjärjestykseen
    for kurssi in sorted(informaatio[oppiaine]):
        # Tulostaa kurssit ja niiden opintopisteeet
        print(kurssi, ":", informaatio[oppiaine][kurssi], "cr")



def main():

    # Kysytään käyttäjältä tiedoston nimi
    tiedosto_nimi = input("Enter file name: ")
    print()

    try:
        tiedosto = open(tiedosto_nimi, mode="r")

        # Luodaan tyhjä sanakirja, johon lisätään oppiaineet
        informaatio = {}

        for rivi in tiedosto:
            # Erotellaan toisistaan oppiaine, kurssi ja opintopisteet
            oppiaine, kurssi, pisteet = rivi.rstrip().split(";")
            if oppiaine not in informaatio:
                # Luodaan toinen tyhjä sanakirja edellisen sanakirjan sisään,
                # johon lisätään oppiaineen kurssit ja niiden opintopisteet
                informaatio[oppiaine] = {}
            informaatio[oppiaine][kurssi] = pisteet

    # Vikailmoitus, jos tiedoston avaaminen ei onnistu tai sitä ei ole olemassa
    except OSError:
        print("Error opening file!")
        return

    # Vikailmoitus, jos tiedosto ei ole sopivaa tyyppiä ohjelmalle
    except ValueError:
        print("Error in file!")
        return

    tiedosto.close()


    while True:
        # Kysytään komentoa käyttäjältä niin kauan, että syöte on "quit"
        print("[A]dd / [C]redits / [D]elete / [P]rint all / p[R]int department"
              " / [Q]uit")
        komento = input("Enter command: ")

        if komento == "P" or komento == "p":
            print()
            tulosta_kaikki(informaatio)
            print()
            continue

        elif komento == "Q" or komento == "q":
            print("Ending program.")
            return

        # Jakaa syötteen listaksi, jolloin voidaan erottaa komento
        # määrittelevistä tiedoista
        komento = komento.split(" ")

        if komento[0] == "C" or komento[0] == "c":
            oppiaine = komento[1]
            print()
            opintopisteet(informaatio, oppiaine)
            print()
            continue

        elif komento[0] == "R" or komento[0] == "r":
            oppiaine = komento[1]
            print()
            tulosta_oppiaine(informaatio, oppiaine)
            print()
            continue

        elif komento[0] == "A" or komento[0] == "a":
            oppiaine = komento[1]
            kurssi = komento[2:-1]
            kurssi = " ".join(kurssi)
            pisteet = komento[-1]
            if kurssi == "":
                print()
                # Virhetilanteen tuloste tähän väliin, koska muuten tulostaa
                # virhettä väärin
                print("Invalid command!")
                print()
                continue
            print()
            lisäys(informaatio, oppiaine, kurssi, pisteet)
            print()
            continue

        elif komento[0] == "D" or komento[0] == "d":
            oppiaine = komento[1]
            kurssi = komento[2:]
            # Yhdistetään loppukomennon osat yhteen, jolloin saadaan selville
            # kurssin kokonimi
            kurssi = " ".join(kurssi)
            print()
            poisto(informaatio, oppiaine, kurssi)
            print()

        else:
            print()
            # Virheellisen komennon tuloste
            print("Invalid command!")
            print()
            continue



main()