# Problem: create a bowl class to hold the scoops from ex38 and try it out
# Input: scoops of ice cream flavors
# Output: contents of the bowl object after adding scoops

from ch9_objects.ex38_ice_cream_scoop import Scoop


class Bowl:
    MAX_SCOOPS = 3

    def __init__(self):
        self.contents = []

    def __repr__(self):
        return '\n'.join(str(scoop) for scoop in self.contents)

    def add_scoop(self, *scoops: Scoop):
        """ Add a scoop to the bowl """

        for a_scoop in scoops:
            if len(self.contents) < self.MAX_SCOOPS:
                self.contents.append(a_scoop)


class BigBowl(Bowl):
    MAX_SCOOPS = 5  # override


if __name__ == '__main__':
    scoop1 = Scoop('Chocolate')
    scoop2 = Scoop('Coffee')
    scoop3 = Scoop('Rum Raisin')
    scoop4 = Scoop('Butter Pecan')
    scoop5 = Scoop('Vanilla')

    my_bowl = Bowl()
    my_big_bowl = BigBowl()

    my_bowl.add_scoop(scoop1, scoop2)
    my_bowl.add_scoop(scoop3)
    my_bowl.add_scoop(scoop4, scoop5)

    my_big_bowl.add_scoop(scoop1, scoop2, scoop3, scoop4)
    my_big_bowl.add_scoop(scoop5, scoop1, scoop2)

    print('My bowl has...')
    print(my_bowl)

    print('\n\nMy big bowl has...')
    print(my_big_bowl)
