from machinery_lib.Kitchen import *

kitchen = Kitchen()
hint = '''
    ----------------------------------------------------------
    |                                                        |
    |    Welcome to SMART KITCHEN 9000!                      |
    | Please, tell your desire, master!                      |
    | Possible commands:                                     |
    |   1) latte - Tasty latte for master!                   |
    |   2) espresso - Strong espresso for master!            |
    |   3) barista_switch - Toggle barista power switch      |
    |   4) barista_milk - Refill milk                        |
    |   5) barista_water - Refill water                      |
    |   6) barista_coffee - refill coffee                    |
    |   7) hint - get list of commands of SMART KITCHEN 9000 |
    |   8) exit - Pretty self-explanatory :P                 |
    ----------------------------------------------------------
    '''
print(hint)
command_list = ['latte', 'espresso', 'barista_switch', 'barista_milk', 'barista_water',
                'barista_coffee', 'hint', 'exit']
while True:
    try:
        user_input = input()
        if user_input not in command_list:
            raise Exception('Sorry, Mater! I am not of understanding! Maybe "hint" command would help?')
        if user_input == 'latte':
            kitchen.brew_latte()
        if user_input == 'espresso':
            kitchen.brew_espresso()
        if user_input == 'barista_switch':
            kitchen.barista_power_switch()
        if user_input == 'barista_milk':
            print('How much, Master?')
            try:
                cups = int(input())
                kitchen.barista_add_milk(int(cups))
            except Exception as e:
                print('Master! I need a number amount to refill!')
        if user_input == 'barista_water':
            print('How much, Master?')
            try:
                cups = int(input())
                kitchen.barista_add_water(int(cups))
            except Exception as e:
                print('Master! I need a number amount to refill!')
        if user_input == 'barista_coffee':
            print('How much, Master?')
            try:
                cups = int(input())
                kitchen.barista_add_coffee(int(cups))
            except Exception as e:
                print('Master! I need a number amount to refill!')
        if user_input == 'hint':
            print(hint)
        if user_input == 'exit':
            print('Bye, master!')
            break
    except Exception as e:
        print(e)
