## Project: Games of Chance
## Author: Daniel Xiang
## Version: 1.0
## Since: 2020-02-12

import sys
import time as t

from utils import validate_input, check_balance
from coin_flip import CoinFlip
from cho_han import ChoHan
from play_cards import PlayCards
from roulette import Roulette

# Main method
def main():
    # User's money
    money = 100.00

    # All the games available
    games = {1:'Flip a Coin!', 2:'Cho-Han', 3:'Poker Game', 4:'Mini Roulette'}

    # Welcome message
    print('\n★☆★☆★☆ Welcome to Games of Chance ★☆★☆★☆')
    print('You have $100 to start!')
    print('(You can exit the program at any time by entering "exit".)')

    while True:
        check_balance(money)

        # Print out main menu
        print('【Main Menu】')
        print('Your current balance is ${:.2f}'.format(money))
        print('(You can exit the program at any time by entering "exit".)')
        print('The current available games are:')
        for index in games:
            print('   {}. {}'.format(index, games[index]))

        # Prompt the user to select a game
        inpt = input('Please make your selection by entering the index of the game: ')
        selection = validate_input(inpt, 'game', num_games=len(games))
        if selection == 'quit': return

        # Execute the selected game
        if games[selection] == 'Flip a Coin!':
            cf = CoinFlip()
            money = cf.execute(money)
        elif games[selection] == 'Cho-Han':
            chohan = ChoHan()
            money = chohan.execute(money)
        elif games[selection] == 'Poker Game':
            poker = PlayCards()
            money = poker.execute(money)
        elif games[selection] == 'Mini Roulette':
            roulette = Roulette()
            money = roulette.execute(money)


# Program entry point
if __name__ == '__main__':
	main()
