"""
COMP.CS.100 tehtävä
Tekijä: Enna Augustin
Opiskelijanumero: 050235634
"""

from tkinter import *


class Counter:
    """
    gjkhljövjhbklököklölÄ
    hkjlkögkjlälgkuhijlköl
    ögkhkjölö

    """
    def __init__(self):
        """
        gyiuojöokägikhjlkölgikjlöl
        ufygiuhojpokplfuygiuhiljökäplgkhjlköläö
        uighljökäölvhkbjnlml,ö
        """
        self.__pääikkuna = Tk()
        self.__counter = 0

        self.__current_value_label = Label(self.__pääikkuna, text='0')
        self.__current_value_label.pack(expand=True, fill=BOTH)

        self.__reset_button = Button(self.__pääikkuna, text='reset', command=self.reset)
        self.__reset_button.pack(side=LEFT,expand=True, fill=BOTH)

        self.__increase_button = Button(self.__pääikkuna, text='increase', command=self.increase)
        self.__increase_button.pack(side=LEFT,expand=True, fill=BOTH)

        self.__decrease_button = Button(self.__pääikkuna, text='decrease', command=self.decrease)
        self.__decrease_button.pack(side=LEFT,expand=True, fill=BOTH)

        self.__quit_button = Button(self.__pääikkuna, text='quit', command=self.quit)
        self.__quit_button.pack(side=LEFT,expand=True, fill=BOTH)

        self.__pääikkuna.mainloop()

    def reset(self):
        """
        gjhklöfgkhjklölhgkjlöläöäjklö,öä
        hkjljökä
        ökjlö
        :return: fyghjlkgfhkjlöl
        """
        self.__counter = 0
        self.__current_value_label['text'] = str(self.__counter)

    def increase(self):
        """
        fgjklögvjhbknklml,hbkjnlml
        :return: ytfughkjlöghkjlöö
        """
        self.__counter += 1
        self.__current_value_label['text'] = str(self.__counter)

    def decrease(self):
        """fghjklöfgkjlökljö,ö.ä
        tiuoiupkålåijokäl
        äökölä
        """
        self.__counter -= 1
        self.__current_value_label['text'] = str(self.__counter)

    def quit(self):
        """
        hjklöjhknlmö,ögjklö
        :return: fugyhkjlöftgyhkjlkghkjlö
        """
        self.__pääikkuna.destroy()


def main():
    # There is no need to modify the main function.
    # As a matter of fact, automated tests ignore main
    # once again.

    Counter()


if __name__ == "__main__":
    main()
