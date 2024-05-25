"""
COMP.CS.100 parasetamoli
Tekijä: Enna Augustin
Opiskelijanumero: 050235634
"""
def calculate_dose(weight, time, total_dose_24):
    """hassunhauska kommentti jossa
    kerrotaan kaikkea kivaaaaa
    """
    total_dose = weight * 15
    if time < 6:
        return 0 * weight * 15
    elif total_dose > 4000 - total_dose_24:
        return 4000 - total_dose_24
    elif total_dose_24 >= 4000:
        return 0 * weight * 15
    return total_dose


def main():
    weight = int(input("Patient's weight (kg): "))
    time = int(input("How much time has passed from the previous dose (full hours): "))
    total_dose_24 = int(input("The total dose for the last 24 hours (mg): "))
    print(f"The amount of Parasetamol to give to the patient: {calculate_dose(weight, time, total_dose_24)}")

    calculate_dose(weight, time, total_dose_24)

    # calculate_dose assumes parameters to be of type int
    # and they should be passed in the order: weight, time, total_doze_24
    # (or more like the automated tests assume this)


if __name__ == "__main__":
  main()
