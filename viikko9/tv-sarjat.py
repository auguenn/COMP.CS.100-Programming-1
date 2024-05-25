"""
COMP.CS.100 tv-sarjat
Tekijä: Enna Augustin
Opiskelijanumero: 050235634
"""
def read_file(filename):
    """
    Reads and saves the series and their genres from the file.
    """

    sanakirja = {}

    try:
        file = open(filename, mode="r")

        for row in file:
            name, genres = row.rstrip().split(";")
            genres = genres.split(",")

            for rivi in genres:
                if rivi in sanakirja:
                    sanakirja[rivi].append(name)
                else:
                    sanakirja[rivi]=[name]

        file.close()
        return sanakirja

    except ValueError:
        print("Error: rows were not in the format name;genres.")
        return None

    except IOError:
        print("Error: the file could not be read.")
        return None


def main():
    filename = input("Enter the name of the file: ")

    genre_data = read_file(filename)
    gt = sorted(genre_data)
    b = ", ".join(gt)

    print(f"Available genres are: {b}")

    do_the_loop = True

    while do_the_loop:

        genre = input("> ")

        try:
            if genre == "exit":
                return

            a = sorted(genre_data[genre])
            for genre in a:
                print(genre)

        except KeyError:
            continue


if __name__ == "__main__":
    main()
