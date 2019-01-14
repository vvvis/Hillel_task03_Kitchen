class CoffeeMachine:

    def __init__(self):
        self.water_tank_cups=0
        self.coffee_tank_cups = 0
        self.milk_tank_cups = 0
        self.power = 'off'

    def power_switch(self):
        if self.power == "on":
            self.power = "off"
        else:
            self.power = "on"

    def add_water(self, water):
        if type(water) != int or water < 0:
            raise Exception('"water" parameter should be int')
        else:
            self.water_tank_cups += water

    def add_coffee(self, coffee):
        if type(coffee) != int or coffee < 0:
            raise Exception('"coffee" parameter should be int')
        else:
            self.coffee_tank_cups += coffee

    def add_milk(self, milk):
        if type(milk) != int or milk < 0:
            raise Exception('"milk" parameter should be int')
        else:
            self.milk_tank_cups += milk

    def get_water_tank_status(self):
        return str(self.water_tank_cups) + ' cups of water resource remaining.\n'

    def get_coffee_tank_status(self):
        return str(self.coffee_tank_cups) + ' cups of coffee resource remaining.\n'

    def get_milk_tank_status(self):
        return str(self.milk_tank_cups) + ' cups of milk resource remaining.\n'

    def get_power_status (self):
        return 'Coffee machine is ' + self.power + "\n"

    def brew_espresso(self):
        if self.power == "off":
            raise Exception('Coffee Machine is turned OFF! Please, start the machine!\n')
        elif self.coffee_tank_cups == 0:
            raise Exception('Refill coffee tank!\n')
        elif self.water_tank_cups == 0:
            raise Exception('Refill water tank!\n')
        else:
            self.coffee_tank_cups -= 1
            self.water_tank_cups -= 1
            print('Espresso is ready!\n')

    def brew_latte(self):
        if self.power == "off":
            raise Exception('Coffee Machine is turned OFF! Please, start the machine!\n')
        elif self.coffee_tank_cups == 0:
            raise Exception('Refill coffee tank!\n')
        elif self.water_tank_cups == 0:
            raise Exception('Refill water tank!\n')
        elif self.milk_tank_cups == 0:
            raise Exception('Refill milk tank!\n')
        else:
            self.coffee_tank_cups -= 1
            self.water_tank_cups -= 1
            self.milk_tank_cups -= 1
            print('Latte is ready!\n')