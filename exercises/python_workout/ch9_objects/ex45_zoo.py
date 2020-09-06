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

    def animals_by_color(self, color: str) -> List[animals.Animal]:
        return [each_animal
                for each_cage in self.all_cages
                for each_animal in each_cage.caged_beasts
                if each_animal.color.lower() == color.lower()]

    def animals_by_legs(self, num_of_legs: int) -> List[animals.Animal]:
        return [each_animal
                for each_cage in self.all_cages
                for each_animal in each_cage.caged_beasts
                if each_animal.number_of_legs == num_of_legs]

    def number_of_legs(self) -> int:
        return sum(each_animal.number_of_legs
                   for each_cage in self.all_cages
                   for each_animal in each_cage.caged_beasts)

    def __repr__(self):
        return '\n'.join(str(each_cage) for each_cage in self.all_cages)


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
