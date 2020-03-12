## Project: Games of Chance
## Author: Daniel Xiang
## Version: 1.0
## Since: 2020-02-12

import random as r
import time as t
from games import Game
from utils import validate_input, wait_msg

# Rollling two dices, guess their sum is even or odd
class ChoHan(Game):
    def __init__(self, name='Cho-Han'):
        super().__init__(name)

    # Override
    def execute(self, balance):
        print('------------------------------------------------------------------------', end='')
        while True:
            super().welcome(self.name, balance)
            inpt = input('Please enter the amount of money you want to bet (default is 10.00): ')
            bet = validate_input(inpt, 'bet', balance=balance)
            if bet == 'quit': break

            inpt = input('Please enter your guess ("odd" or "even"): ')
            guess = validate_input(inpt, 'odd_or_even')
            if guess == 'quit': break

            outcome = ''
            win = None

            # Let user know it's executing
            wait_msg('Rolling dies', 5, 0.4)

            die1 = r.randint(1,6)
            die2 = r.randint(1,6)
            die_sum = die1 + die2
            if die_sum % 2 == 0: outcome = 'even'
            else: outcome = 'odd'

            print('\nDice #1: {}'.format(die1))
            t.sleep(1.5)
            print('Dice #2: {}'.format(die2))
            t.sleep(1.5)
            print('The sum: {}, which is {}!'.format(die_sum, outcome))
            t.sleep(1.5)

            if outcome == guess: win = True     
            else: win = False
            balance += super().get_result(win, bet)
        
        print('------------------------------------------------------------------------')
        return balance
