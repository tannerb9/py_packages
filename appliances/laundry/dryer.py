# from .appliances import Appliance


class Dryer:

    def __init__(self, color, heat_method):
        self.color = color
        self.heat_method = heat_method

    def dry_clothes(self, setting="low"):
        if setting != "low":
            print("Please allow 40 minutes for you clothes to come out crispy.")
        else:
            print("Please allow 40 minutes for your clothes to come out soggy.")
