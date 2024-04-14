"""
CP1404 - Programming 2
Taxi Simulation
Name: Austin Liandro
Start from: 8.50 pm  - 4/14/2024
"""

from cp1404practicals.prac_09.taxi import Taxi
from cp1404practicals.prac_09.silver_service_taxi import SilverServiceTaxi


MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    bill_to_date = 0.0
    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != 'Q':
        if choice == 'C':
            print("Taxis available:")
            number_to_taxi = display_taxis(taxis)
            idx_choice = int(input("Choose taxi: "))
            if idx_choice not in number_to_taxi:
                print("Invalid taxi choice.")
            else:
                current_taxi = number_to_taxi[idx_choice]

        elif choice == 'D':
            if current_taxi:
                drive_distance = int(input("Drive how far? "))
                current_taxi.start_fare()
                current_taxi.drive(drive_distance)
                print(f"Your {current_taxi.name} trip cost you ${current_taxi.get_fare():.2f}")
                bill_to_date += current_taxi.get_fare()
            else:
                print("You need to choose a taxi before you can drive")

        else:
            print("Invalid option.")
        print(f"Bill to date: ${bill_to_date:.2f}")
        print(MENU)
        choice = input(">>> ").upper()
    print(f"Total trip cost: ${bill_to_date:.2f}")
    display_taxis(taxis)


def display_taxis(taxis):
    """Display the taxis with assigned numbers and their information."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")
    return {i: taxi for i, taxi in enumerate(taxis)}


main()