"""
COMP.CS.100 bussi
Tekijä: Enna Augustin
Opiskelijanumero: 050235634
"""


def main():
    """
    jhmgkjh,
    gbjghlhj.ljköyjt
    grejgltg
    :return: rkhgklktrh
    """
    aikataulu = [630, 1015, 1415, 1620, 1720, 2000]
    time = int(input("Enter the time (as an integer): "))
    lenght = len(aikataulu)
    i = 0
    print("The next buses leave:")
    if time <= 630:
        print(aikataulu[0])
        print(aikataulu[1])
        print(aikataulu[2])
    elif time > 630 and time <= 1015:
        print(aikataulu[1])
        print(aikataulu[2])
        print(aikataulu[3])
    elif time > 1015 and time <= 1415:
        print(aikataulu[2])
        print(aikataulu[3])
        print(aikataulu[4])
    elif time > 1415 and time <= 1620:
        print(aikataulu[3])
        print(aikataulu[4])
        print(aikataulu[5])
    elif time > 1620 and time <= 1720:
        print(aikataulu[4])
        print(aikataulu[5])
        print(aikataulu[0])
    elif time > 1720 and time <= 2000:
        print(aikataulu[5])
        print(aikataulu[0])
        print(aikataulu[1])
    elif time >= 2000:
        print(aikataulu[0])
        print(aikataulu[1])
        print(aikataulu[2])




main()