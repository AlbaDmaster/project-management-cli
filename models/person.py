class Person:
    """
    Base class representing a person.
    """

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name