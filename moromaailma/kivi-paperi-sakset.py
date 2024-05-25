"""
COMP.CS.100 Kivi-paperi-sakset
Tekijä: Enna Augustin
Opiskelijanumero: 050235634
"""
def main(user1) :
    user1 = input("Player 1, enter your choice (R/P/S): ")
    user2 = input("Player 2, enter your choice (R/P/S): ")
    rock = "R"
    paper = "P"
    scissors = "S"
    if user2 == paper and user1 == rock or user2 == scissors and user1 == paper:
        print("Player 2 won!")
    elif user2 == rock and user1 == scissors:
        print("Player 2 won!")
    elif user1 == paper and user2 == rock or user1 == rock and user2 == scissors:
        print("Player 1 won!")
    elif user1 == scissors and user2 == paper:
        print("Player 1 won!")
    else:
        print("It's a tie!")

main("P")