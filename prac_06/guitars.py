"""
CP1404/CP5632 Practical - Client code to use the Guitar  class.
Estimate: 20 minutes
Actual:   30 minutes
"""
from prac_06.guitar import Guitar


def main():
    guitars = []
    print("My guitars!")
    get_guitar_details(guitars)

    print("\n... snip ...")
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    display_guitars(guitars)


def display_guitars(guitars):
    """Display the Guitar information"""
    print("There are my guitar:")
    if guitars:
        for i, guitar in enumerate(guitars, 1):
            vintage_string = " (vintage)" if guitar.is_vintage else ""
            print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")
    else:
        print("No guitars :( Quick, go and buy one!")


def get_guitar_details(guitars):
    """Get the guitar information"""
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        added_guitar = Guitar(name, year, cost)
        guitars.append(added_guitar)
        print(added_guitar, "added.")
        name = input("Name: ")


main()