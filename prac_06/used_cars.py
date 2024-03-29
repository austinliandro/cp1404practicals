"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
Estimate: 10 minutes
Actual:   10 minutes
"""

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    limo = Car("Limo", 100)
    limo.add_fuel(20)
    print(limo.fuel)
    limo.drive(115)
    print(limo)

    my_car = Car("My car", 180)
    my_car.drive(30)
    print(f"fuel: {my_car.fuel}")
    print(my_car)


main()