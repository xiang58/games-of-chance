## Project: Games of Chance
## Author: Daniel Xiang
## Version: 1.0
## Since: 2020-02-12

import random as r
import time as t
from games import Game
from utils import validate_input, wait_msg

# Roulette simulator
class Roulette(Game):
    def __init__(self, name='Mini Roulette'):
        super().__init__(name)
        self.rules = {
            1: 'Straight up [payout 35:1] (any single number, including 0 & 00.)', 
            2: 'Odd or Even [payout 1:1] (from 1 to 36, excluding 0 and 00)',
            3: 'Red or Black [payout 1:1]\n      Red: 1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,26\n      Black: 2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35',
            4: 'High or Low [payout 1:1] (high: 19-36; low: 1-18)'
        }

    # Override
    def execute(self, balance):
        print('------------------------------------------------------------------------', end='')
        while True:
            # Welcome message & menu
            super().welcome(self.name, balance)
            print('Currently, the supported bet rules include:')
            for index in self.rules:
                print('   {}. {}'.format(index, self.rules[index]))

            # Input how user wants to bet
            inpt = input('Please select how you want to place your bet: ')
            rule = validate_input(inpt, 'roulette', num_rules=len(self.rules))
            if rule == 'quit': break

            your_bet = ''
            if rule == 1:
                inpt = input('Please enter a single number: ')
                your_bet = validate_input(inpt, 'roulette1')
                if your_bet == 'quit': break
            elif rule == 2:
                inpt = input('Please input your choice (odd/even): ')
                your_bet = validate_input(inpt, 'odd_or_even')
                if your_bet == 'quit': break
            elif rule == 3:
                inpt = input('Please input your choice (red/black): ')
                your_bet = validate_input(inpt, 'red_or_black')
                if your_bet == 'quit': break
            elif rule == 4:
                inpt = input('Please input your choice (high/low): ')
                your_bet = validate_input(inpt, 'high_or_low')
                if your_bet == 'quit': break

            # Input how much the user wants to bet
            inpt = input('Please enter the amount of money you want to bet (default is 10.00): ')
            bet = validate_input(inpt, 'bet', balance=balance, payout=35) if rule == 1 else validate_input(inpt, 'bet', balance=balance)

            # Roll the ball
            spot = r.randint(-1, 36)
            spot = '00' if spot == -1 else str(spot)
            wait_msg('Rolling the ball', 7, 0.5)
            print('The ball is on spot ' + spot + '!')
            t.sleep(1)
            print('Your bet is on "' + your_bet + '"!')
            t.sleep(1)

            # Check result
            win = None

            if rule == 1:
                if your_bet == spot: win = True
                else: win = False
                balance += super().get_result(win, bet, 35)

            elif rule == 2:
                if spot == '0' or spot == '00': win = False
                elif int(spot) % 2 != 0:
                    if your_bet == 'odd': win = True
                    else: win = False
                else:
                    if your_bet == 'even': win = True
                    else: win = False
                balance += super().get_result(win, bet)

            elif rule == 3:
                red = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,26]
                black = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
                if spot == '0' or spot == '00': win = False
                elif int(spot) in red:
                    if your_bet == 'red': win = True
                    else: win = False
                else:
                    if your_bet == 'black': win = True
                    else: win = False
                balance += super().get_result(win, bet)

            elif rule == 4:
                if spot == '0' or spot == '00': win = False
                elif int(spot) >= 19:
                    if your_bet == 'high': win = True
                    else: win = False
                else:
                    if your_bet == 'low': win = True
                    else: win = False
                balance += super().get_result(win, bet)

        print('------------------------------------------------------------------------')
        return balance
