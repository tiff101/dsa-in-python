# as supplement to the random activity generator
# we about to bulk these activities out!

class Ternary:
    BOTH = 2
    TRUE = 1
    FALSE = 0


class Activity:
    def __init__(self, name, is_indoor: Ternary, is_solo: Ternary):
        """
        :param name: title of activity
        :param is_indoor: ternary to represent indoor, outdoor or both
        :param is_solo: ternary to represent solo, multiple people or both
        """
        self.name = name
        self.is_indoor = is_indoor
        self.is_solo = is_solo


class Food:
    def __init__(self, name, flavour_type, price, effort, meal_type, is_cooked):
        self.name = name
        self.flavour_type = flavour_type    # one of savoury, sweet
        self.price = price  # on a scale of 1 (ultra cheap) - 5 (expensive / unpredictable)
        self.effort = effort  # another scale
        self.meal_type = meal_type  # [snack, meal, dessert]
        self.is_cooked = is_cooked   # [cooked, takeaway (bought)]