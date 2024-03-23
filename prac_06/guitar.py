"""CP1404/CP5632 Practical
Guitar class """

CURRENT_YEAR = 2013
VINTAGE_AGE = 50


class Guitar:
    """Guitar class storing guitar information"""

    def __init__(self, name, year, cost,):
        """Initialise a Guitar."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return the guitar information string"""
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self):
        """Calculate the age of the guitar"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if the guitar vintage or not"""
        return self.get_age() >= VINTAGE_AGE