"""
COMP.CS.100 Laivanupotus-projekti
Tekijä: Enna Augustin
Opiskelijanumero: 050235634

Ohjelma, jolla voidaan pelata laivanupotusta. Eri alustyypit ja niiden
sijaintien koordinaatit saadaan tiedostosta.
"""

#Määritellään kaikki mahdolliset arvot x- ja y-koordinaateille
MAHDOLLISET_KOORDINAATIT_Y = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
MAHDOLLISET_KOORDINAATIT_X = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]


class Ship:
    """
    Tämä luokka edustaa yhtä laivaa. Laiva koostuu alustyypistä ja sen
    koordinaateista.
    """

    def __init__(self, alustyyppi, koordinaatit):
        """
        Rakentaja, alustaa laivat sen parametrien mukaan

        :param alustyyppi: str, alustyypin nimi
        :param koordinaatit: list, lista kyseisen aluksen koordinaateista.
        """
        self.__alustyyppi = alustyyppi
        self.__koordinaatit = koordinaatit

        # Muodostetaan tyhjä lista, johon voidaan lisätä koordinaatti aina kun
        # laivaan onnistutaan ampumaan
        self.__osutut = []

        # Alussa laiva on pinnalla
        self.__uponnut = False



    def get_shot(self, pelilauta, laukaus_koordinaatti):
        """
        Lisää pelilautaan ammutun koordinaatin, jos sitä ei ole aiemmin
        pelilautaan lisätty (eli kyseiseen kohtaan ei olla ammuttu).

        :param pelilauta: list, sen hetkinen pelilauta,
        joka koostuu listasta listan sisällä eli matriisista
        :param laukaus_koordinaatti: str, käyttäjän antamat koordinaatit
        laukaukselle tiettyyn kohtaan pelilaudalla syötteestä
        :return: list, päivitetty pelilauta laukauksen omalla merkinnällä
        varustettuna
        """

        # Muodostetaan laukauksen koordinaatista lista, jolloin saadaan
        # eroteltua x- ja y-koordinaatit
        laukaus = list(laukaus_koordinaatti)
        x = muunnokset(laukaus_koordinaatti)
        y = int(laukaus[1])


        # Tarkistetaan aina laukauksen kohdalla, onko kyseinen koordinaatti
        # laivan sijaintikoordinaateissa
        if laukaus_koordinaatti.upper() in self.__koordinaatit:
            # Jos on, lisätään osumakoordinaatti listaan ja lisätään
            # pelilaudalle kyseiseen kohtaan "X"
            self.__osutut.append(laukaus_koordinaatti)
            pelilauta[y][x] = "X"

        elif laukaus_koordinaatti.upper() not in self.__koordinaatit:
            # Jos ei ole, ja kyseinen kohta on 'tyhjä' eli pelkkä välilyönti
            # lisätään kyseiseen kohtaan "*"
            if pelilauta[y][x] == " ":
                pelilauta[y][x] = "*"



    def has_sunk(self):
        """
        Tutkii onko kyseinen alus uponnut kokonaan eli, onko sen kaikkiin
        koordinaatteihin osuttu

        :return: bool, totuusarvo sille onko alus uponnut. Jos on, niin
        totuusarvo on True, muuten False.
        """
        # Laiva on uponnut, jos sen koordinaattien lista on yhtä pitkä kuin
        # osuttujen laukausten lista
        if len(self.__osutut) == len(self.__koordinaatit):
            # Muutetaan tällöin uppoamisen totuusarvo
            self.__uponnut = True
            print(f"You sank a {self.__alustyyppi}!")
            return self.__uponnut



    def muunna_koordinaatit(self, pelilauta):
        """
        Jos laiva on uponnut, muuntaa kaikki kyseisen laivan koordinaatit
        kyseisen laivan nimen ensimmäiseksi kirjaimeksi pelilaudalle.

        :param pelilauta: list, kyseisen hetken pelilauta
        (matriisi eli lista listassa)
        :return: list, päivitetty pelilauta, jossa laivan koordinaatit on
        korvattu alustyypin alkukirjaimella
        """
        if self.__uponnut == True:
            # Muodostetaan alustyypin nimestä lista kirjaimia, joista saadaan
            # poimittua ensimmäinen kirjain tulostuksia varten
            a = list(self.__alustyyppi)
            b = str(a[0])

            for koordinaatti in self.__koordinaatit:
                # Muodostetaan eri koordinaateista erilliset listat, jotta
                # saadaan jokaisen koordinaatin kirjainosa erilleen
                # numero-osasta
                koordinaatti_lista = list(koordinaatti)

                for i in koordinaatti_lista:
                    x = muunnokset(koordinaatti_lista)
                    y = int(koordinaatti_lista[1])
                    # Muokataan kyseisen upotetun laivan koordinaatit
                    # alustyypin ensimmäiseksi kirjaimeksi
                    pelilauta[y][x] = b.upper()



def muunnokset(laukaus_koordinaatti):
    """
    Muuntaa ammutun koordinaatin kirjainosan numeromuotoon, jotta
    koordinaattiin saadaan asetettua merkki get_shot -metodissa

    :param laukaus: list, kyseinen laukaus listamuodossa, jossa kirjainosa ja
    numero-osa eriteltyinä listan eri arvoiksi
    :return: int, koordinaatin kirjainosa muutettuna sanakirjan avulla
    vastaavaksi numeroksi.
    """
    # Koordinaatin kirjainosa on listan ensimmäinen alkio
    kirjainosa = laukaus_koordinaatti[0]

    # Kirjaimia vastaavat numeroarvot
    muunnokset = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6,
                  "H": 7, "I": 8, "J": 9}

    # Etsitään sanakirjasta kyseistä kirjainosaa vastaava lukuarvo ja
    # palautetaan se
    return muunnokset[kirjainosa.upper()]



def create_board():
    """
    Luo listan listan sisällä eli matrisin. Tämä toimii pelilautana pelille.

    :return: list, tyhjä matriisi, eli pelilauta
    """
    # Luodaan ensin yksi tyhjä lista pelilaudalle
    pelilauta = []


    for rivi in range(10):
        # Lisätään jokaiselle riville oma listansa, jolloin saadaan aikaan
        # matriisi
        pelilauta.append([])
        for sarake in range(10):
            # Lisätään välilyönnit 'arvoiksi' edellä lisättyihin 'sisälistoihi'
            # jotta pelilauta pysyy siistin näköisenä
            pelilauta[rivi].append(' ')

    return pelilauta



def print_board(pelilauta):
    """
    Tulostaa sen hetkisen pelilaudan

    :param pelilauta: list, matriisi
    :return: str, siististi asemoitu pelilauta, johon tehty mahdolliset
    päivitykset
    """
    # Alkuun ja loppuun tulostetaan sarakkeita vastaavat kirjaimet
    # Nämä edustavat samalla x-koordinaatteja
    print("  A B C D E F G H I J ")

    for i in range(10):
        # Muodostetaan edellisessä funktiossa luoduista 'sisälistoista'
        # siististi asettuva merkkijono
        j = " ".join(pelilauta[i])
        # Tulostetaan pelilaudan sen hetkiset tiedot rivinumeroiden (i) kanssa
        print(f"{i} {j} {i}")

    print("  A B C D E F G H I J ")



def read_file(tiedosto_nimi):
    """
    Lukee käyttäjältä saadun tiedoston ja muodostaa oikean muotoisesta
    tiedostosta listan eri laiva-olioista

    :param tiedosto_nimi: str, käyttäjän syötteestä saatu nimi avattavalle
    tiedostolle
    :return: list, lista eri laiva-oloista, joilla omat "alustyypit" ja
    koordinaatit
    """

    try:

        tiedosto = open(tiedosto_nimi, mode='r')

        # Luodaan tyhjä lista, johon lisätään tiedostosta saatavat laiva-oliot
        laiva_oliot = []

        # Luodaan tyhjä lista, johon lisätään kaikkien laiva-olioiden
        # koordinaatit virhetarkastelua varten
        kaikki_koordinaatit = []


        for tiedosto_rivi in tiedosto:
            # Erotellaan laivatyyppi sen koordinaateista
            laivat = tiedosto_rivi.rstrip().split(";")
            alustyyppi = laivat[0]
            koordinaatit = laivat[1:]
            # Luodaan olio ja lisätään se olioille tarkoitettuun listaan
            olio = Ship(alustyyppi, koordinaatit)
            laiva_oliot.append(olio)


            for i in koordinaatit:
                # Tarkastetaan, onko laivan koordinaatti jo kaikkien
                # koordinaattien listassa ja jos ei ole, niin lisätään
                # koordinaatti sinne
                if i not in kaikki_koordinaatit:
                    kaikki_koordinaatit.append(i)
                else:
                    # Virhetulostus, jos tiedoston laivoilla on yhteisiä
                    # koordinaatteja eli ne olisivat pelilaudalla päällekkäin,
                    # jolloin ohjelman suoritus päättyy
                    print("There are overlapping ships in the input file!")
                    return False


        for j in kaikki_koordinaatit:
            # Muodostetaan jokaisesta koordinaatista oma listansa, jotta
            # voidaan tarkastaa koordinaattien sopivuus pelilaudalle
            eri_koordinaatit_laivoille = list(j)
            y = eri_koordinaatit_laivoille[0]
            z = eri_koordinaatit_laivoille[1:]
            # Yhdistetään listan loppupään arvot, jolloin saadaan
            # x-koordinaatin arvo
            x = "".join(z)

            # Virhetuloste, jos edes yksi y- tai x-koordinaatti ei toteuta
            # koordinaateille asetettuja ehtoja
            # Tällöin ohjleman suoritus päättyy
            if y.upper() not in MAHDOLLISET_KOORDINAATIT_X or x not in\
                    MAHDOLLISET_KOORDINAATIT_Y:
                print("Error in ship coordinates!")
                return False
            else:
                continue


    # Vikailmoitus, jos tiedoston avaaminen ei onnistu tai sitä ei ole olemassa
    # Tällöin ohjelman suoritus päättyy
    except OSError:
        print("File can not be read!")
        return False

    return laiva_oliot



def main():

    # Kysytään käyttäjältä nimeä, sille tiedostolle, josta laivojen nimet ja
    # koordinaatit halutaan avata
    tiedosto_nimi = input("Enter file name: ")

    # Avataan tiedosto ja katsotaan funktion kautta, onko siinä virheitä
    # ohjelman toiminnan kannalta
    laivat = read_file(tiedosto_nimi)
    if not laivat:
        return

    print()
    pelilauta = create_board()


    while True:

        # Tulostetaan pelilautaa ja kysytään käyttäjältä koordinaatteja, joihin
        # ammutaan niin kauan, että kaikki laivat on upotettu pelilaudalta tai
        # käyttäjä syöttää lopettamisen komennon
        print_board(pelilauta)
        print()


        syöte = input("Enter place to shoot (q to quit): ")


        # Lopetuksen komento
        if syöte == "Q" or syöte == "q":
            print("Aborting game!")
            return

        # Virhetulostus, jos käyttäjän antama syöte ei ole oikean pituinen eli
        # ei ole muotoa XY
        elif len(syöte) != 2:
            print("Invalid command!")
            print()
            continue

        # Virhetulostus, jos käyttäjä antaa tyhjän syötteen
        # Tälle oma tarkastelu, koska edellinen tarkastelu ei ymmärrä tyhjää
        # syötettä pituudeksi 0
        elif syöte == "":
            print("Invalid command!")
            print()
            continue

        # Muutetaan syöte listaksi, jotta päästään tarkastelemaan koordinaatin
        # oikeellisuutta pelin kannalta
        laukaus_koordinaatit = list(syöte)
        x = laukaus_koordinaatit[0]
        y = laukaus_koordinaatit[1]


        # Virhetulostus, jos koordinaateista muodostettu lista ei ole muotoa
        # ['X', 'Y']
        # Tämä tuloste on olemassa, koska muuten ohjelma alkaa herjaamaan
        # erroria vääränmuotoisen syötteen kohdalla, vaikka samankaltainen
        # tarkastelu onkin tehty jo aikaisemmin :)
        if len(laukaus_koordinaatit) < 2:
            print("Invalid command!")
            print()
            continue

        # Tarkistetaan onko annettu x-koordinaatti pelilaudalle mahdollisissa
        # x-koordinaateissa
        elif x.upper() not in MAHDOLLISET_KOORDINAATIT_X:
            print("Invalid command!")
            print()
            continue

        # Tarkistetaan onko annettu y-koordinaatti pelilaudalle mahdollisissa
        # y-koordinaateissa
        elif y not in MAHDOLLISET_KOORDINAATIT_Y:
            print("Invalid command!")
            print()
            continue

        # Muutetaan koordinaatit vielä int-muotoon, jotta voidaan tehdä
        # viimeinen virhetarkastelu
        x = muunnokset(syöte)
        y = int(laukaus_koordinaatit[1])

        # Virhetuloste, jos syötteessä annettu koordinaatti on pelilaudalla jo
        # täynnä eli jos siihen on jo ammuttu aikaisemmin
        if pelilauta[y][x] != " ":
            print("Location has already been shot at!")
            print()
            continue


        else:
            # Tukitaan jokaista laiva-oliota kyseiset oliot sisältävässä
            # listassa
            for ship in laivat:
                ship.get_shot(pelilauta, syöte)

                # Jos laiva on uponnut muunnetaan sen koordinattien merkit
                # laivatyypin ensimmäiseksi kirjaimeksi ja sitten poistetaan
                # kyseinen laiva laiva-oloit sisältävästä listasta
                if ship.has_sunk():
                    ship.muunna_koordinaatit(pelilauta)
                    laivat.remove(ship)



        #Peli loppuu, kun kaikki laiva-oliot on poistettu kyseiset oliot
        # sisältävästä listasta eli, kun lista on tyhjä
        if len(laivat) == 0:
            print()
            print_board(pelilauta)
            print()
            print("Congratulations! You sank all enemy ships.")
            return

        print()


if __name__ == "__main__":
    main()


