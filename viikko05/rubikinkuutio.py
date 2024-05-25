"""
COMP.CS.100 rubikinkuutio
Tekijä: Enna Augustin
Opiskelijanumero: 050235634
"""

def score():
    """
    bke,kgjerölkhrtöhltyrthl
    r,rglkjhötlköelht
    :return: kkjehgieolökrth
    """
    pass

def main():
    ajat = []
    for i in range(1, 6):
        time = float(input(f"Enter the time for performance {i}: "))
        ajat.append(time)
        i += 1
    ajat.remove(max(ajat))
    ajat.remove(min(ajat))
    sum = ajat[0] + ajat[1] + ajat[2]
    ka = sum / len(ajat)
    print(f"The official competition score is {ka:.2f} seconds.")

main()