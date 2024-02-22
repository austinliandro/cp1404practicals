"""
display menu
get choice
while choice != <quit option>
    if choice == <first option>
        <do first task>
    else if choice == <second option>
        <do second task>
    ...
    else if choice == <n-th option>
        <do n-th task>
    else
        display invalid input error message
    display menu
    get choice
<do final thing, if needed>
"""

MENU = "(G)et valid score\n" \
       "(P)rint Result\n" \
       "(S)how stars\n" \
       "(Q)uit"


def main():
    print(MENU)
    choice = input(">>>").upper()
    score = 0
    while choice != 'Q':
        if choice == 'G':
            score = get_score()
            print("Thankyou!")
        elif choice == 'P':
            if score != 0:
                result = determine_score(score)
                print(f"Your result is: {result}")
            else:
                print("No score entered.")
        elif choice == 'S':
            if choice != 0:
                for i in range(score):
                    print("*", end=' ')
                print()
            else:
                print("No score entered.")
        else:
            print("Invalid input")
        print(MENU)
        choice = input(">>>").upper()
    print("Farewell")


def determine_score(score):
    if score >= 90:
        message = "Excellent!"
    elif score >= 50:
        message = "Passable."
    else:
        message = "Bad"
    return message


def get_score():
    score = int(input("Enter score (1-100): "))
    while score < 0 or score > 100:
        print("Invalid number. Please Try again.")
        score = int(input("Enter score (1-100): "))
    return score


main()