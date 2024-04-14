"""
CP1404 - Programming 2
Band Class
Name: Austin Liandro
"""


class Band:
    """Band class"""

    def __init__(self, name=""):
        """Construct a band with a name and empty instrument Musician"""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of a Band"""
        return f"{self.name} ({','.join(str(musician) for musician in self.musicians)})"

    def __repr__(self):
        """Return a string representation of a Band, showing the variables"""
        return str(vars(self))

    def add(self, musician):
        """Add an instrument to musician's collection."""
        self.musicians.append(musician)

    def play(self):
        """Play the music"""
        return '\n'.join(musician.play() for musician in self.musicians)