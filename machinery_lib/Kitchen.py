from .Small_Machinery import *


class Kitchen:

    def __init__(self):
        self.barista = CoffeeMachine()

    def barista_get_status(self):
        print(self.barista.get_water_tank_status()
              + self.barista.get_milk_tank_status()
              + self.barista.get_coffee_tank_status()
              + self.barista.get_power_status())

    def barista_power_switch(self):
        self.barista.power_switch()
        if self.barista.power == "on":
            print('YEAH! NOW WE`RE COOCKING!')
        else:
            print('OH, C`MON (x_x)!')



    def barista_add_water(self, water):
        try:
            self.barista.add_water(water)
            print('Water added! ' + self.barista.get_water_tank_status())
        except Exception as e:
            print(e)

    def barista_add_coffee(self, coffee):
        try:
            self.barista.add_coffee(coffee)
            print('Coffee Added! ' + self.barista.get_coffee_tank_status())
        except Exception as e:
            print(e)

    def barista_add_milk(self, milk):
        try:
            self.barista.add_milk(milk)
            print('Milk Added! ' + self.barista.get_milk_tank_status())
        except Exception as e:
            print(e)

    def brew_espresso(self):
        try:
            self.barista.brew_espresso()
        except Exception as e:
            print(e)

    def brew_latte(self):
        try:
            self.barista.brew_latte()
        except Exception as e:
            print(e)
