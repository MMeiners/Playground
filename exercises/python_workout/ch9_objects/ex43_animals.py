# Problem: create a base animal class, and four subclasses able to print out their species, # of legs, and color
# EDIT: for ex44 adding a cage class
# Input: instantiate a few animal child classes
# Output: string representation of each animal

from typing import List


class Animal:
    def __init__(self, color: str, number_of_legs: int):
        self.color = color
        self.number_of_legs = number_of_legs

    def __repr__(self):
        return f'A {self.color} {self.__class__.__name__}, {self.number_of_legs} legs '


class Wolf(Animal):
    def __init__(self, color):
        super().__init__(color, 4)


class Sheep(Animal):
    def __init__(self, color):
        super().__init__(color, 4)


class Snake(Animal):
    def __init__(self, color):
        super().__init__(color, 0)


class Parrot(Animal):
    def __init__(self, color):
        super().__init__(color, 2)


class Cage:
    def __init__(self, cage_id: int):
        self.cage_id = cage_id
        self.caged_beasts: List[Animal] = []

    def add_animals(self, *animals_to_add):
        for beast in animals_to_add:
            self.caged_beasts.append(beast)

    def __repr__(self):
        report_header = f'Cage id {self.cage_id} contains\n'
        report_rows = '\n'.join((f'\t{beast}' for beast in self.caged_beasts))
        return report_header + report_rows


if __name__ == '__main__':
    animals = [Sheep('White'), Sheep('Brown'), Wolf('Black'), Parrot('Red'), Snake('Green')]

    cage1 = Cage(1)
    cage2 = Cage(2)

    cage1.add_animals(*animals[0:3])
    cage2.add_animals(*animals[3:])

    print(cage1)
    print(cage2)
