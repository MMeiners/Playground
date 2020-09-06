# Problem: To build on ex43 and ex44, build a zoo class that can inspect the cages and report on metrics like
#          list the animals with four legs, or of a color, and total number of legs (don't ask...)
# Input: cages, animals, and report calls
# Output: report strings based on zoo contents

import ch9_objects.ex43_animals as animals
from typing import List


class Zoo:
    def __init__(self):
        self.all_cages: List[animals.Cage] = []

    def add_cages(self, *cages: animals.Cage):
        for cage in cages:
            self.all_cages.append(cage)

    def animals_by_color(self, color: str):
        same_colored_animals = []

        for cage in self.all_cages:
            same_colored_animals.extend(each_animal
                                        for each_animal in cage.caged_beasts
                                        if each_animal.color.lower() == color.lower())

        return same_colored_animals

    def animals_by_legs(self, num_of_legs: int):
        same_legged_animals = []

        for cage in self.all_cages:
            same_legged_animals.extend(each_animal
                                       for each_animal in cage.caged_beasts
                                       if each_animal.number_of_legs == num_of_legs)

        return same_legged_animals

    def number_of_legs(self):
        total_legs = 0

        for cage in self.all_cages:
            total_legs += sum(each_animal.number_of_legs for each_animal in cage.caged_beasts)

        return total_legs

    def __repr__(self):
        report = ''

        for cage in self.all_cages:
            report += str(cage)
            report += '\n'

        return report


if __name__ == '__main__':
    all_animals = [animals.Sheep('White'), animals.Sheep('Brown'),
                   animals.Wolf('White'), animals.Parrot('Red'),
                   animals.Snake('Green')]

    cage1 = animals.Cage(1)
    cage2 = animals.Cage(2)

    cage1.add_animals(*all_animals[0:3])
    cage2.add_animals(*all_animals[3:])

    my_zoo = Zoo()
    my_zoo.add_cages(cage1, cage2)

    print(my_zoo)
    print(my_zoo.animals_by_color('White'))
    print(my_zoo.animals_by_legs(4))
    print(f'Number of legs: {my_zoo.number_of_legs()}')
