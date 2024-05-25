"""
COMP.CS.100 tehtävä
Tekijä: Enna Augustin
Opiskelijanumero: 050235634
"""
from tkinter import *
import random
import sys

words = ["MrBlake", "cat"]

sword = random.choice(words)
guesses = 10
word = ("-" * len(sword))


class Application(Frame):
    """ GUI application which can retrieve an auto number to guess. """

    def __init__(self, master):
        """ Initialize the frame. """
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """ Create button, text, and entry widgets. """

        """ Instruction Label """

        # Create instruction label for Program
        self.inst_lbl = Label(self, text="Welcome to Guess the Word!")
        self.inst_lbl.grid(row=0, column=0, columnspan=2, sticky=W)

        """ Guess Input """

        # Create label for entering Guess
        self.guess_lbl = Label(self, text="Enter your Guess:")
        self.guess_lbl.grid(row=2, column=0, sticky=W)

        # Create entry widget to accept Guess
        self.guess_ent = Entry(self)
        self.guess_ent.grid(row=2, column=1, sticky=W)

        # Create a space
        self.gap1_lbl = Label(self, text=" ")
        self.gap1_lbl.grid(row=3, column=0, sticky=W)

        """ Submit Button """

        # Creating a submit button
        self.submit_bttn = Button(self, text="Submit", command=self.reveal)
        self.submit_bttn.grid(row=6, column=0, sticky=W)

        # Create a space
        self.gap2_lbl = Label(self, text=" ")
        self.gap2_lbl.grid(row=7, column=0, sticky=W)

        """ RESET """

        # Creating a reset button
        self.reset_bttn = Button(self, text="Reset", command=self.reset)
        self.reset_bttn.grid(row=6, column=1, sticky=W)

        """ Display """

        # Create text widget to display welcome_msg
        self.display1_txt = Text(self, width=45, height=1, wrap=WORD)
        self.display1_txt.grid(row=8, column=0, columnspan=2, sticky=W)

        # Create text widget to display guess_msg
        self.display2_txt = Text(self, width=45, height=1, wrap=WORD)
        self.display2_txt.grid(row=9, column=0, columnspan=2, sticky=W)

        # Create text widget to display result_msg
        self.display3_txt = Text(self, width=45, height=2, wrap=WORD)
        self.display3_txt.grid(row=10, column=0, columnspan=2, sticky=W)

        # Create text widget to display tries_msg
        self.display4_txt = Text(self, width=45, height=2, wrap=WORD)
        self.display4_txt.grid(row=11, column=0, columnspan=2, sticky=W)

        # Create text widget to display word_msg
        self.display5_txt = Text(self, width=45, height=2, wrap=WORD)
        self.display5_txt.grid(row=12, column=0, columnspan=2, sticky=W)

    def reveal(self):
        global words
        global sword
        global word
        guesses = 10
        letter = self.guess_ent.get()
        while guesses != 0:
            for i in range(0, 1):
                word_msg = word
                tries_msg = guesses
                welcome_msg = "Welcome!"
                guess_msg = letter
                print(letter)
                for i in range(0, len(sword)):
                    if sword[i] == letter:
                        temp = i
                        word = word[:temp] + letter + word[temp + 1:]
                        word_msg = word
                    if word == sword:
                        result_msg = "Congratulations! You win!"
                    if letter not in sword:
                        guesses = guesses - 1
                        result_msg = "incorrect"
                    if guesses == 0:
                        result_msg = "G A M E  O V E R"
        # Display
        self.display1_txt.delete(0.0, END)
        self.display1_txt.insert(0.0, welcome_msg)
        self.display2_txt.delete(0.0, END)
        self.display2_txt.insert(0.0, guess_msg)
        self.display3_txt.delete(0.0, END)
        self.display3_txt.insert(0.0, result_msg)
        self.display4_txt.delete(0.0, END)
        self.display4_txt.insert(0.0, tries_msg)
        self.display5_txt.delete(0.0, END)
        self.display5_txt.insert(0.0, word)
        Tk.update(self)

    def reset(self):
        global tries
        self.display4_txt.delete(0.0, END)
        self.display3_txt.delete(0.0, END)
        self.display2_txt.delete(0.0, END)
        self.display1_txt.delete(0.0, END)


# Main manager
root = Tk()
root.title("Guessing Game")
root.geometry("300x225")
app = Application(root)