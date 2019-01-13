from .Small_Machinery import *


class Kitchen:
    coffee_machine = CoffeeMachine

    def add_water(coffee_machine, water):
        try:
            return coffee_machine.coffee_machine.add_water(coffee_machine,water)
            print(self.machine.get_water_tank_status())
        except Exception as e:
            print(e)

