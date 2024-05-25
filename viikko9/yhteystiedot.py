"""
COMP.CS.100 yhteystiedot
Tekijä: Enna Augustin
Opiskelijanumero: 050235634
"""
def read_file(filename):
    """
    ydtfuygiuhiljutfygiuhil
    fuygkjlögvhjbkljö
    hyughjklöguhlkjöä
    giuhojoköäpl
    :return: dfyguhjuiofdyguhjlköl
    """
    file = open(filename, mode='r')
    contacts = {}
    for row in file:
        key, name, phone, email, skype = row.rstrip().split(";")
        contacts[key] = {}
        contacts[key]["name"] = name
        contacts[key]["phone"] = phone
        contacts[key]["email"] = email
        contacts[key]["skype"] = skype

    file.close()
    return contacts

