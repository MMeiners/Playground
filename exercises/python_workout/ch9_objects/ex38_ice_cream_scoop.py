# Problem: create a class to hold scoops of ice cream flavors, create some scoops, then read them back out
# Input: ice cream flavor strings
# Output: flavor attributes

class Scoop:
    def __init__(self, flavor: str):
        self.flavor = flavor

    def __repr__(self):
        return f'Scoop of {self.flavor}'


if __name__ == '__main__':
    bowl_of_ice_cream = [Scoop(flavor) for flavor in ('Chocolate', 'Vanilla', 'Mint')]

    for each_scoop in bowl_of_ice_cream:
        print(each_scoop.flavor)
