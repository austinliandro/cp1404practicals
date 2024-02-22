MINIMUM_CHARACTER = 0


def main():
    password = get_password()
    display_password(password)


def display_password(password):
    """ it will display the password"""
    print("Your new password is:", "*" * len(password))


def get_password():
    password = input("Enter your password: ")
    while len(password) <= MINIMUM_CHARACTER:
        print("The password doesn't meet a minimum length set by a variable. Please try again.")
        password = input("Enter your password: ")
        return password


main()
