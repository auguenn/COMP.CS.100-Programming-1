"""
COMP.CS.100 lottopelejä
Tekijä: Enna Augustin
Opiskelijanumero: 050235634
"""
def factorial(n):
    """
    tdyjhgjhoilkj.k
    :param n: fujhjhgjhkujhgtth
    :return: gfhjhmghjghgygkj
    """
    fact=1
    while(n>1):
        fact=fact*n
        n=n-1
    return fact

def combinations(n,k):
    """
    hngjhkjhkjlghgjjbkerjger,gjrehlgierrerbreb
    :param n: fhjdjhehgkerjhgrkeugherj
    :param k: vbjhevberkerkgkjergfkjer
    :return: bjvnbjhebvehbvhj
    """
    num = int(factorial(n))
    den = int(factorial(k) * factorial(n-k))
    return int(num / den)


def main():
    balls = int(input("Enter the total number of lottery balls: "))
    drawn = int(input("Enter the number of the drawn balls: "))

    if balls < 0 or drawn < 0:
        print("The number of balls must be a positive number.")
    elif drawn > balls:
        print("At most the total number of balls can be drawn.")
    else:
        print(f"The probability of guessing all {drawn} balls correctly is 1/{combinations(balls,drawn)}")

main()