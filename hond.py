class Hond:

    # Constructor
    def __init__(self, naam, leeftijd):
        self.naam = naam
        self.leeftijd = leeftijd

    def __str__(self):
        return f"{self.naam} is {self.leeftijd} jaar oud."
