"""
COMP.CS.100 mölkky
Tekijä: Enna Augustin
Opiskelijanumero: 050235634
"""

class Player:
    def __init__(self, nimi):
        self.__nimi = nimi
        self.__points = 0
        self.__win = 50
        self.__heitto = 0
        self.__hits = 0

    def get_name(self):
        return self.__nimi


    def add_points(self, points):
        """
        ytugihiojdrytfuygihujk
        :param points: vhbjnkmluyi
        :return: ytuyiuhojgvuhjbknl
        """
        pisteet = int(self.__points + points)
        self.__heitto += 1

        if points > 0:
            self.__hits += 1

        if pisteet > 50:
            print(self.__nimi, "gets penalty points!")
            self.__points = 25


        elif pisteet >= 40 and pisteet <= 49:
            print(f"{self.__nimi} needs only {50-pisteet} points. It's better "
                  f"to avoid knocking down the pins with higher points.")
            self.__points += points

        elif pisteet < 50:
            self.__points += points

        elif pisteet == 50:
            self.__points += points
            return self.__win

    def get_points(self):
        """
        trdytfughkjdytfuygj
        :return: xfcgvhjbkjncgvhjbj
        """
        return self.__points

    def has_won(self):
        """
        etsrdytfughkjdytfuyghkj
        :return: tfuygihjklöluhjklk
        """
        if self.__points == 50:
            return self.__win

    def keskiarvo(self):
        """
        tryugihdrytfugihij
        :return: tryugiuhjk
        """
        kk = self.__points / (self.__heitto)
        return kk


    def osumaprosentti(self):
        """
        trdyfugihjdytfugihijok
        :return: rytuhbijnklmxfcgvhb
        """
        if self.__heitto > 0:
            return round(self.__hits / self.__heitto * 100,1)
        else:
            return 0.0


def main():
    # Here we define two variables which are the objects initiated from the
    # class Player. This is how the constructor of the class Player
    # (the method that is named __init__) is called!

    player1 = Player("Matti")
    player2 = Player("Teppo")

    throw = 1
    while True:

        # if throw is an even number
        if throw % 2 == 0:
            in_turn = player1

        # else throw is an odd number
        else:
            in_turn = player2

        pts = int(input("Enter the score of player " + in_turn.get_name() +
                        " of throw " + str(throw) + ": "))

        pisteet = in_turn.get_points() + pts

        in_turn.add_points(pts)


        if pts > in_turn.keskiarvo():
            if pisteet <= 50:
                print("Cheers " + in_turn.get_name() + "!")


        if in_turn.has_won():
            print("Game over! The winner is " + in_turn.get_name() + "!")
            return

        print("")
        print("Scoreboard after throw " + str(throw) + ":")
        print(player1.get_name() + ":", player1.get_points(), "p,", "hit percentage", player1.osumaprosentti())
        print(player2.get_name() + ":", player2.get_points(), "p,", "hit percentage", player2.osumaprosentti())
        print("")

        throw += 1


if __name__ == "__main__":
    main()
