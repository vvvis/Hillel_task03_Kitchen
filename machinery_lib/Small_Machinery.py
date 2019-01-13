class CoffeeMachine:
    water_tank_cups = 0
    coffee_tank_cups = 0
    milk_tank_cups = 0
    power = 'off'

    def power_switch(self, switch):
        if switch not in ["on", "off"]:
            raise Exception('"power" parameter allowed status is "on" or "off"')
        else:
            self.power = switch

    def add_water(self, water):
        if type(water) != int or water < 0:
            raise Exception('"water" parameter should be int')
        else:
            self.water_tank_cups

    def add_coffee(self, coffee):
        if type(coffee) != int or coffee < 0:
            raise Exception('"coffee" parameter should be int')
        else:
            self.water_tank_cups += coffee

    def add_milk(self, milk):
        if type(milk) != int or milk < 0:
            raise Exception('"milk" parameter should be int')
        else:
            self.water_tank_cups += milk

    def get_water_tank_status (self):
        return str(self.water_tank_cups) + ' cups of water resource remaining\n'

    def get_coffee_tank_status (self):
        return str(self.coffee_tank_cups) + ' cups of coffee resource remaining\n'

    def get_milk_tank_status (self):
        return str(self.milk_tank_cups) + ' cups of milk resource remaining\n'

    def get_power_status (self):
        return 'Coffee machine is ' + self.power + "\n"

    def brew_espresso(self):

        if self.coffee_tank_cups == 0 or self.water_tank_cups == 0:
            raise Exception ('Refill coffee or water tank!\n' + self.coffee_tank_status() + self.water_tank_status())
        else:
            self.coffee_tank_cups -= 1
            self.water_tank_cups -= 1
            print('Espresso is ready!\n')


