"""
COMP.CS.100 Vaihtorahat
Tekijä: Enna Augustin
Opiskelijanumero: 050235634
"""
def main() :
    price = int(input("Purchase price: "))
    money = int(input("Paid amount of money: "))
    change = money - price
    change10 = change // 10
    change5 = int((change % 10) / 5)
    change2 = int(((change % 10) - change5 * 5) // 2)
    change1 = int(((change % 10) - change5 * 5) - change2 * 2)
    if price >= money:
        print("No change")
    elif change10 <= 0 and change5 <= 0 and change2 <= 0:
        print("Offer change:")
        print(change1, "one-euro coins")
    elif change10 <= 0 and change2 <= 0 and change1 <= 0:
        print("Offer change:")
        print(change5, "five-euro notes")
    elif change5 <= 0 and change2 <= 0 and change1 <= 0:
        print("Offer change:")
        print(change10, "ten-euro notes")
    elif change10 <= 0 and change5 <= 0 and change1 <= 0:
        print("Offer change:")
        print(change2, "two-euro coins")
    elif change10 <= 0 and change5 <= 0:
        print("Offer change:")
        print(change2, "two-euro coins")
        print(change1, "one-euro coins")
    elif change10 <= 0 and change2 <= 0:
        print("Offer change:")
        print(change5, "five-euro notes")
        print(change1, "one-euro coins")
    elif change10 <= 0 and change1 <= 0:
        print("Offer change:")
        print(change5, "five-euro notes")
        print(change2, "two-euro coins")
    elif change5 <= 0 and change2 <= 0:
        print("Offer change:")
        print(change10, "ten-euro notes")
        print(change1, "one-euro coins")
    elif change5 <= 0 and change1 <= 0:
        print("Offer change:")
        print(change10, "ten-euro notes")
        print(change2, "two-euro coins")
    elif change1 <= 0 and change2 <= 0:
        print("Offer change:")
        print(change10, "ten-euro notes")
        print(change5, "five-euro notes")
    elif change10 <= 0:
        print("Offer change:")
        print(change5, "five-euro notes")
        print(change2, "two-euro coins")
        print(change1, "one-euro coins")
    elif change5 <= 0:
        print("Offer change:")
        print(change10, "ten-euro notes")
        print(change2, "two-euro coins")
        print(change1, "one-euro coins")
    elif change2 <= 0:
        print("Offer change:")
        print(change10, "ten-euro notes")
        print(change5, "five-euro notes")
        print(change1, "one-euro coins")
    elif change1 <= 0:
        print("Offer change:")
        print(change10, "ten-euro notes")
        print(change5, "five-euro notes")
        print(change2, "two-euro coins")
    else:
        print("Offer change:")
        print(change10, "ten-euro notes")
        print(change5, "five-euro notes")
        print(change2, "two-euro coins")
        print(change1, "one-euro coins")

main()



