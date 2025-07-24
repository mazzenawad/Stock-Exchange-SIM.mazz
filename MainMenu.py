#MainMenu

import os

def MainMenu():
    while True:
        print('1. Create an account')
        print('2. Make a stock bidding')
        print('3. Make a stock asking')
        print('4. Exit the Program')
        try:
            selection = int(input('Select Option: '))
        except ValueError:
            print('Invalid input. Please enter a number from 1 to 4.')
            continue

        if selection == 1:
            os.system('python create_account.py')
        elif selection == 2:
            os.system('python bidding_.py')
        elif selection == 3:
            os.system('python asking_.py')
        elif selection == 4:
            print('Terminating program.')
            break
        else:
            print('Invalid entry. Please select a valid option.')

MainMenu()