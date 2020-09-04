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
            if len(self.contents) < Bowl.MAX_SCOOPS:
                self.contents.append(a_scoop)


if __name__ == '__main__':
    scoop1 = Scoop('Chocolate')
    scoop2 = Scoop('Coffee')
    scoop3 = Scoop('Rum Raisin')
    scoop4 = Scoop('Butter Pecan')

    my_bowl = Bowl()

    my_bowl.add_scoop(scoop1, scoop2)
    my_bowl.add_scoop(scoop3)
    my_bowl.add_scoop(scoop4)

    print('My bowl has...')
    print(my_bowl)
