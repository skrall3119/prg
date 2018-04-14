# Superclass "Furniture"


class Furniture:

    def __init__(self, category, material, length, width, height, price):
        self.__category = category
        self.__material = material
        self.__length = length
        self.__width = width
        self.__height = height
        self.__price = price

    def set_category(self, category):
        self.__category = category

    def set_material(self, material):
        self.__material = material

    def set_length(self, length):
        self.__length = length

    def set_width(self, width):
        self.__width = width

    def set_height(self, height):
        self.__height = height

    def set_price(self, price):
        self.__price = price

    def get_category(self):
        return self.__category

    def get_material(self):
        return self.__material

    def get_length(self):
        return self.__length

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def get_price(self):
        return self.__price

    def __str__(self):
        line = "This is a " + self.__material + " " + self.__category + " with dimensions " + str(self.__length) + "ft by " + str(self.__width) + "ft by " + str(self.__height) + "ft which costs ${:0,.2f}".format(self.__price)
        return line


class Desk(Furniture):

    def __init__(self, category, material, length, width, height, price, number_of_drawers, location_of_drawers):

        Furniture.__init__(self, category, material, length, width, height, price)

        self.__number_of_drawers = number_of_drawers
        self.__location_of_drawers = location_of_drawers

    def set_number_of_drawers(self, number_of_drawers):
        self.__number_of_drawers = number_of_drawers

    def set_location_of_drawers(self, location_of_drawers):
        self.__location_of_drawers = location_of_drawers

    def get_number_of_drawers(self):
        return self.__number_of_drawers

    def get_location_of_drawers(self):
        return self.__location_of_drawers

    def __str__(self):
        line = "This is a " + str(self.__number_of_drawers) + "-drawer " + self.get_material() + " " + self.get_category() + " with dimensions " + str(self.get_length()) + "ft by " + str(self.get_width()) + "ft by " + str(self.get_height()) + "ft with drawers on the " + self.__location_of_drawers + " side which costs ${:0,.2f}".format(self.get_price())
        return line
