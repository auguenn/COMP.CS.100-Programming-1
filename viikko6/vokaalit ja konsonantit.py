"""
COMP.CS.100 vokaalit ja konsonantit
Tekijä: Enna Augustin
Opiskelijanumero: 050235634
"""

def main():
    """
    jmhjhknmnfgkjeg
    gjergkuhjrgr
    :return: hbjkhkejrg
    """
    vokaali = []
    word = str(input("Enter a word: "))

    for j in range(len(word)):
        if word[j] == "a" or word[j] == "e" or word[j] == "i" or\
                word[j] == "o" or word[j] == "u" or word[j] == "y":
            vokaali.append(word[j])


    if word == "":
        word = str(input("Enter a word: "))

    vow = len(vokaali)
    con = len(word) - vow

    print(f"The word \"{word}\" contains ", end="")
    print(f"{vow} vowels and {con} consonants.")


main()