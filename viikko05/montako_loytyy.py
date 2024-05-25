"""
COMP.CS.100 montako löytyy?
Tekijä: Enna Augustin
Opiskelijanumero: 050235634
"""

def input_to_list(count):
    """
    vnhhkjköl-mnklmtherth
    thejtrjtyjj
    :return: rhehtrjyjtjyt
    """
    list = []
    print(f"Enter {count} numbers: ")
    for i in range(1, count+1):
        num = int(input())
        list.append(num)
    return list

def main():
    """
    vjmhk,kglekjtlkhtrh
    :return:
    """
    count = int(input("How many numbers do you want to process: "))
    list = input_to_list(count)
    luku = int(input("Enter the number to be searched: "))

    if luku in list:
        print(luku, "shows up", list.count(luku), "times among the numbers "
                                                      "you have entered.")
    if luku not in list:
        print(luku, "is not among the numbers you have entered.")

if __name__ == "__main__":
    main()