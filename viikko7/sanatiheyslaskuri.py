"""
COMP.CS.100 sanatiheyslaskuri
Tekijä: Enna Augustin
Opiskelijanumero: 050235634
"""

def main():
    print("Enter rows of text for word counting. Empty row to quit.")
    ls = []
    str = input().lower()
    while str != "":
        ls.append(str)
        str = input().lower()

    words = " ".join(ls)
    bb = words.split()

    counts = dict()
    for word in sorted(bb):
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    for i in counts:
        print(f"{i} : {counts[i]} times")



if __name__ == "__main__":
    main()