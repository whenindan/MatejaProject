from Bank import Bank
from Player import Player
from Tile import Tile
# TODO: MAKE THIS A CHILD CLASS OF TILES 
class StreetTile(Tile):
    """
    Represents a property in the Monopoly game.
    """
    

    """Initialize a property"""

    def __init__(self, name, price, mortgage_value, pos, rent, color_group):
        self.name = name
        self.owner = Bank
        self.price = price
        self.mortgage_value = mortgage_value
        self.is_mortgaged = False
        self.pos = pos
        self.house_count = 0
        self.hotel_count = 0
        self.rent = rent
        self.color_group = color_group
        super().__init__()
    # set the owner to a Player object
    def setOwner(self, Player):
        self.owner = Player

    def addHouse(self):
        while self.house_count <= 4:
            self.house_count += 1

    def getWorth(self):
        # worth of a property if it has 1, 2, 3, or 4 houses
        # brown & light blue: $50/house
        # purple & orange: $100/house
        # red & yellow: $150/house
        # green & blue: $200/house
        if self.house_count != 0:
            if self.color_group == 'brown' or self.color_group == 'light blue':
                return self.price + self.house_count * 50 / 2
            elif self.color_group == 'purple' or self.color_group == 'orange':
                return self.price + self.house_count * 100 / 2
            elif self.color_group == 'red' or self.color_group == 'yellow':
                return self.price + self.house_count * 150 / 2
            else:
                return self.price + self.house_count * 200 / 2

        # worth of a property if it has 1 hotel (cost of 1 hotel = 1 house)
        elif self.house_count == 0 and self.hotel_count == 1:
            if self.color_group == 'brown' or self.color_group == 'light blue':
                return self.price + (self.house_count + 1) * 50 / 2
            elif self.color_group == 'purple' or self.color_group == 'orange':
                return self.price + (self.house_count + 1) * 100 / 2
            elif self.color_group == 'red' or self.color_group == 'yellow':
                return self.price + (self.house_count + 1) * 150 / 2
            else:
                return self.price + (self.house_count + 1) * 200 / 2

        # worth of a property if it has 0 house and 0 hotel
        else:
            return self.price

    def sellHouse(self):
        if self.house_count >= 1 and self.hotel_count <= 4:
            self.house_count -= 1

    def addHotel(self):
        if self.house_count == 4:
            self.hotel_count = 1
            self.house_count = 0

    def sellHotel(self):
        self.hotel_count = 0

    def mortgage(self):
        if self.house_count == 0 and self.hotel_count == 0:
            self.is_mortgaged = True

    def unMortgage(self):
        self.is_mortgaged = False

    def calcRent(self):
        if self.hotel_count == 0:
            return self.rent[self.house_count]
        elif self.hotel_count == 1:
            return self.rent[-1]