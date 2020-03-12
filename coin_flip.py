## Project: Games of Chance
## Author: Daniel Xiang
## Version: 1.0
## Since: 2020-02-12

import random as r
import time as t
from games import Game
from utils import validate_input, wait_msg

# Flip a coin, guess "heads" or "tails"
class CoinFlip(Game):
    def __init__(self, name='Flip A Coin!'):
        super().__init__(name)

    # Override
    def execute(self, balance):
        print('------------------------------------------------------------------------', end='')   
        while True:
            super().welcome(self.name, balance)
            inpt = input('Please enter the amount of money you want to bet (default is 10.00): ')
            bet = validate_input(inpt, 'bet', balance=balance)
            if bet == 'quit': break

            inpt = input('Please enter your guess ("heads" or "tails"): ')
            guess = validate_input(inpt, 'coin_guess')
            if guess == 'quit': break

            num = r.randint(0, 1)
            outcome = ''
            win = None

            # Let user know it's executing
            wait_msg('Flipping', 5, 0.7)

            if num == 0: outcome = 'heads'
            else: outcome = 'tails'
            print("It's " + outcome + '!')
            t.sleep(1)

            if outcome == guess: win = True     
            else: win = False
            balance += super().get_result(win, bet)

        print('------------------------------------------------------------------------')
        return balance
