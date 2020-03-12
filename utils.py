## Project: Games of Chance
## Author: Daniel Xiang
## Version: 1.0
## Since: 2020-02-12

import sys
import time as t

# Helper functions
def validate_input(inpt, tp, **kwargs):
    """
    param inpt: str (user input),
    param tp: str (input type)
    || Return modified user input given raw input 'inpt' and the type 'tp' of this input.
    """
    valid = False

    if tp == 'game': # Game selection step
        if inpt.isnumeric():
            if int(inpt) > 0 and int(inpt) <= kwargs.get('num_games'):
                valid = True 
        elif inpt.lower() == 'exit': sys.exit()

        while not valid:
            inpt = input('Invalid input. Please try again: ')
            if inpt.isnumeric():
                if int(inpt) > 0 and int(inpt) <= kwargs.get('num_games'):
                    valid = True 
            elif inpt.lower() == 'exit': sys.exit()
        
        return int(inpt)
    
    elif tp == 'bet': # How much money does the user want to bet?
        inpt = inpt.lower()
        if inpt == 'quit': return 'quit'
        if inpt == 'exit': sys.exit()
        inpt = 10.00 if inpt == '' else inpt

        bet = 0
        try: 
            bet = float(inpt)
            valid = True
        except: pass

        if bet <= 0: valid = False
        elif bet * kwargs.get('payout', 1) > kwargs.get('balance'):
            print('Not enough balance.')
            t.sleep(1)
            valid = False

        while not valid:
            inpt = input('Invalid input. Please try again: ')
            inpt = inpt.lower()
            if inpt == 'quit': return 'quit'
            if inpt == 'exit': sys.exit()
            inpt = 10.00 if inpt == '' else inpt

            bet = 0
            try: 
                bet = float(inpt)
                valid = True
            except: pass
        
            if bet <= 0: valid = False
            elif bet * kwargs.get('payout', 1) > kwargs.get('balance'):
                print('Not enough balance.')
                t.sleep(1)
                valid = False

        return bet
    
    elif tp == 'coin_guess': # User's guess ("heads" or "tails")
        if inpt.isalpha():
            inpt = inpt.lower()
            if inpt == 'heads' or inpt == 'tails':
                valid = True
            elif inpt == 'quit': return 'quit'
            elif inpt == 'exit': sys.exit()

        while not valid:
            inpt = input('Invalid input. Please try again: ')
            if inpt.isalpha():
                inpt = inpt.lower()
                if inpt == 'heads' or inpt == 'tails':
                    valid = True
                elif inpt == 'quit': return 'quit'
                elif inpt == 'exit': sys.exit()

        return inpt

    elif tp == 'odd_or_even': # User's guess ("odd" or "even")
        if inpt.isalpha():
            inpt = inpt.lower()
            if inpt == 'odd' or inpt == 'even':
                valid = True
            elif inpt == 'quit': return 'quit'
            elif inpt == 'exit': sys.exit()

        while not valid:
            inpt = input('Invalid input. Please try again: ')
            if inpt.isalpha():
                inpt = inpt.lower()
                if inpt == 'odd' or inpt == 'even':
                    valid = True
                elif inpt == 'quit': return 'quit'
                elif inpt == 'exit': sys.exit()

        return inpt

    elif tp == 'player': # Let user choose whether s/he draws card first or not
        if inpt.isnumeric():
            inpt = int(inpt)
            if inpt == 1 or inpt == 2:
                valid = True 
        elif inpt.lower() == 'exit': sys.exit()
        elif inpt.lower() == 'quit': return 'quit'

        while not valid:
            inpt = input('Invalid input. Please try again: ')
            if inpt.isnumeric():
                inpt = int(inpt)
                if inpt == 1 or inpt == 2:
                    valid = True 
            elif inpt.lower() == 'exit': sys.exit()
            elif inpt.lower() == 'quit': return 'quit'

        return inpt

    elif tp == 'roulette': # Let user choose how s/he places the bet
        if inpt.isnumeric():
            if int(inpt) > 0 and int(inpt) <= kwargs.get('num_rules'):
                valid = True 
        elif inpt.lower() == 'exit': sys.exit()
        elif inpt.lower() == 'quit': return 'quit'

        while not valid:
            inpt = input('Invalid input. Please enter the index of the bet you want to place: ')
            if inpt.isnumeric():
                if int(inpt) > 0 and int(inpt) <= kwargs.get('num_rules'):
                    valid = True 
            elif inpt.lower() == 'exit': sys.exit()
            elif inpt.lower() == 'quit': return 'quit'
        
        return int(inpt)

    elif tp == 'roulette1': # Roulette rule #1
        if inpt.isnumeric():
            if inpt == '00': return -1
            if inpt == '0' or int(inpt) > 0 and int(inpt) <= 36:
                valid = True 
        elif inpt.lower() == 'exit': sys.exit()
        elif inpt.lower() == 'quit': return 'quit'

        while not valid:
            inpt = input('Invalid input. Please enter a number among 0, 00, and 1-36: ')
            if inpt.isnumeric():
                if inpt == '00': return -1
                if inpt == '0' or int(inpt) > 0 and int(inpt) <= 36:
                    valid = True 
            elif inpt.lower() == 'exit': sys.exit()
            elif inpt.lower() == 'quit': return 'quit'
        
        return inpt

    elif tp == 'red_or_black': #Roulette rule: red or black
        if inpt.isalpha():
            inpt = inpt.lower()
            if inpt == 'red' or inpt == 'black':
                valid = True
            elif inpt == 'quit': return 'quit'
            elif inpt == 'exit': sys.exit()

        while not valid:
            inpt = input('Invalid input. Please try again: ')
            if inpt.isalpha():
                inpt = inpt.lower()
                if inpt == 'red' or inpt == 'black':
                    valid = True
                elif inpt == 'quit': return 'quit'
                elif inpt == 'exit': sys.exit()

        return inpt

    elif tp == 'high_or_low': #Roulette rule: high or low
        if inpt.isalpha():
            inpt = inpt.lower()
            if inpt == 'high' or inpt == 'low':
                valid = True
            elif inpt == 'quit': return 'quit'
            elif inpt == 'exit': sys.exit()

        while not valid:
            inpt = input('Invalid input. Please try again: ')
            if inpt.isalpha():
                inpt = inpt.lower()
                if inpt == 'high' or inpt == 'low':
                    valid = True
                elif inpt == 'quit': return 'quit'
                elif inpt == 'exit': sys.exit()

        return inpt

    else: 
        print('Invalid input type')
        return ''


def wait_msg(msg, num_dots, interval):
    """
    param msg: str,
    param num_dots: int,
    param interval: float
    || Simulates game executing process.
    """
    sys.stdout.write(msg)
    sys.stdout.flush()
    for i in range(num_dots):
        sys.stdout.write('.')
        sys.stdout.flush()
        t.sleep(interval)


def check_balance(balance):
    """
    param balance: float
    || Check if the user has any money left. If not, exit the program.
    """
    if balance == 0.00:
        print("\nAh oh! You don't have enough money to play Games of Chance!")
        print('This program will exit automatically in 5 seconds...')
        t.sleep(5)
        sys.exit()
