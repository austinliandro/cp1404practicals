"""
CP1404/CP5632 Practical
Finding color code
Emails
Estimate: 20 minutes
Actual:   25 minutes
"""


def main():
    mail_to_name = {}
    mail = input(f"Emails:")
    while mail != "":
        name = convert_mail_to_name(mail)
        verified_name = input(f"Is your name {name} (Y/n)").lower()
        if verified_name != "y" and verified_name != "":
            name = input(f"Name:")
        mail_to_name[mail] = name
        mail = input(f"Emails:")
    for mail, name in mail_to_name.items():
        print(f"{name} ({mail})")


def convert_mail_to_name(mail):
    """Get the name for provided email"""
    name_part = mail.split("@")[0]
    parts = name_part.split(".")
    name = " ".join(parts).title()
    return name


main()