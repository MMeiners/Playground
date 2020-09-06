# Problem: create a base animal class, and four subclasses able to print out their species, # of legs, and color
# Input: instantiate a few animal child classes
# Output: string representation of each animal

class Animal:
    def __init__(self, color, number_of_legs):
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


if __name__ == '__main__':
    animals = [Sheep('White'), Sheep('Brown'), Wolf('Black'), Parrot('Red'), Snake('Green')]

    for animal in animals:
        print(animal)
