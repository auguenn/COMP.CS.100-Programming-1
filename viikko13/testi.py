"""
COMP.CS.100 tehtävä
Tekijä: Enna Augustin
Opiskelijanumero: 050235634
"""
from tkinter import *

class Käyttöliittymä:
  def __init__(self):
    self.__pääikkuna = Tk()
    self.__pääikkuna.mainloop()

def main():
  käli = Käyttöliittymä()

if __name__ == "__main__":
    main()