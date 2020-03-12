## Project: Games of Chance
## Author: Daniel Xiang
## Version: 1.0
## Since: 2020-02-12

import time as t
from utils import check_balance

# Game template
class Game: 
    def __init__(self, name):
        """
        param name: str (Game name)
        """
        self.name = name

    def welcome(self, msg, balance):
        """Print out welcome message"""
        check_balance(balance)
        print('\n●●●●● Welcome to【{}】●●●●●'.format(self.name))
        print('Your current balance is ${:.2f}'.format(balance))
        print('(You can go back to main menu by typing "quit", or exit the program by typing "exit".)')

    def execute(self, balance):
        """Execute the game. Return user's current balance.""" 
        return 0

    def get_result(self, win, bet, payout=1):
        """
        param win: bool (Does user win or lose),
        param payout: int 
        || Return A real number inidicatig money gain (+) or loss (-) given 'win' and 'bet'.
        """
        money = 0
        if win is None:
            print('There is a tie. Nobody wins.')
            t.sleep(2)
            return money

        if win: 
            money = bet * payout
            print('Congrats! You win!')
            t.sleep(1)
            print('You won ${:.2f}!'.format(money))
            t.sleep(2)
            return money

        money = -bet * payout
        print('Awww... You lose.')
        t.sleep(1)
        print('You lose ${:.2f}.'.format(-money))
        t.sleep(2)
        return money
