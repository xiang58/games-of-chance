## Project: Games of Chance
## Author: Daniel Xiang
## Version: 1.0
## Since: 2020-02-12

import random as r
import time as t
from games import Game
from utils import validate_input, wait_msg

# Two players draws cards, the one who gets higher number wins
class PlayCards(Game):
    def __init__(self, name='Poker Game'):
        super().__init__(name)
        self.cards = [
            '♠A','♠2','♠3','♠4','♠5','♠6','♠7','♠8','♠9','♠10','♠J','♠Q','♠K',
            '♦A','♦2','♦3','♦4','♦5','♦6','♦7','♦8','♦9','♦10','♦J','♦Q','♦K',
            '♥A','♥2','♥3','♥4','♥5','♥6','♥7','♥8','♥9','♥10','♥J','♥Q','♥K',
            '♣A','♣2','♣3','♣4','♣5','♣6','♣7','♣8','♣9','♣10','♣J','♣Q','♣K'
        ]

    # Override
    def execute(self, balance):
        print('------------------------------------------------------------------------', end='')
        while True:
            super().welcome(self.name, balance)
            print('Note: there are no jokers in this deck of cards (total: 52 cards).')
            inpt = input('Please enter the amount of money you want to bet (default is 10.00): ')
            bet = validate_input(inpt, 'bet', balance=balance)
            if bet == 'quit': break

            print('Choose which player you want to be (Player 1 draws first, Player 2 draws next)')
            inpt = input('Enter "1" or "2": ')
            player = validate_input(inpt, 'player')
            if player == 'quit': break

            first_draw = self.cards[r.randint(0, len(self.cards)-1)]
            self.cards.remove(first_draw)
            second_draw = self.cards[r.randint(0, len(self.cards)-1)]

            # Let user know it's executing
            wait_msg('Drawing cards from a deck', 5, 0.5)

            num1 = self.parse_card(first_draw)
            num2 = self.parse_card(second_draw)
            win = None

            if player == 1:
                print("\nYou (player 1) have drawn: {}".format(first_draw))
                t.sleep(1.5)
                print('The computer (player 2) has drawn: {}'.format(second_draw))
                t.sleep(1.5)
                if num1 > num2: win = True
                elif num1 < num2: win = False
                balance += super().get_result(win, bet)
            else:
                print('\nThe computer (player 1) has drawn: {}'.format(first_draw))
                t.sleep(1.5)
                print("You (player 2) have drawn: {}".format(second_draw))
                t.sleep(1.5)
                if num1 < num2: win = True
                elif num1 > num2: win = False
                balance += super().get_result(win, bet)

        print('------------------------------------------------------------------------')
        return balance

    def parse_card(self, card):
        """
        param card: str
        || Return the corresponding number (1-13) on the card.
        """
        digit = card[-1]

        if digit.isnumeric():
            digit = int(digit)
            digit = 10 if digit == 0 else digit
        else:
            if digit == 'A': digit = 1
            elif digit == 'J': digit = 11
            elif digit == 'Q': digit = 12
            elif digit == 'K': digit = 13

        return digit
