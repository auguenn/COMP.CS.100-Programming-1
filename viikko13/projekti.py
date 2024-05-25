"""
COMP.CS.100 projekti 5
Tekijä: Enna Augustin
Opiskelijanumero: 050235634
"""

from tkinter import *
import random

MAHDOLLISET_KIRJAIMET = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                         'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
                         'W', 'X', 'Y', 'Z', 'Å', 'Ä', 'Ö']

class Hangman:
    def __init__(self):
        self.__pääikkuna = Tk()
        self.__pääikkuna.title("Hirsipuu <3")


        self.__arvaukset = []
        self.__sana_arvattu = False

        self.__sallitut_epäonnistumiset = 10

        self.__toivotus = Label(self.__pääikkuna)
        self.__syöte_label = Label(self.__pääikkuna, text= 'arvaa kirjain')
        self.__syöte = Entry()
        self.__pelaa = Button(self.__pääikkuna, text='arvaa', background = 'purple', foreground = 'black', command=self.pelaa)
        self.__lopeta = Button(self.__pääikkuna, text='lopeta', background = 'black', foreground = 'pink', command=self.lopeta)

        self.__toivotus.grid(row=0, column=2)
        self.__syöte_label.grid(row=2, column=2)
        self.__syöte.grid(row=2, column=3)
        self.__pelaa.grid(row=2, column=4)
        self.__lopeta.grid(row=6, column=5)


    def pelaa(self, pelialusta):

        while self.__sallitut_epäonnistumiset > 0:
            arvaus = self.__syöte.upper()

        if self.is_invalid_letter(user_input):
            print('¡The input is not a letter!')
            continue
            # Check if the letter is not already guessed
        if user_input in self.game_progress:
            print('You already have guessed that letter')
            continue

        if user_input in self.word_to_guess:
            indexes = self.find_indexes(user_input)
            self.update_progress(user_input, indexes)
            # If there is no letter to find in the word
            if self.game_progress.count('_') == 0:
                print('\n¡Yay! You win!')
                print('The word is: {0}'.format(self.word_to_guess))
                quit()
        else:
            self.failed_attempts += 1
        print("\n¡OMG! You lost!")

    def käynnistys(self):
        self.__pääikkuna.mainloop()

    def lopeta(self):
        self.__pääikkuna.destroy()


def get_word(sanalista):
    etsitty_sana = random.choice(sanalista)
    return etsitty_sana.upper()

def avaa_tiedosto():

    try:
        file = open("sanat", mode="r")

        sanalista = []

        for row in file:
            sana = row.rstrip()
            if sana not in sanalista:
                sanalista.append(sana)

        file.close()
        return sanalista

    except IOError:
        print("Error: the file could not be read.")
        return None



def main():
    sanalista = avaa_tiedosto()
    etsitty_sana = get_word(sanalista)
    luo_pelialusta(etsitty_sana)
    hirsipuu = Hangman()
    hirsipuu.käynnistys()


if __name__ == "__main__":
    main()