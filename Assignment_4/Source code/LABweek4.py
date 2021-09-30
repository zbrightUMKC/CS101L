########################################################################
##
## CS 101 Lab
## Program 4
## Zack Bright
## zmbrfq@umkc.edu
##
## PROBLEM : We have been given an incomplete program that plays a slots-like game. Our job is to write the functions that will make the program run
##
## ALGORITHM : 
##      1. The program has a pretty much set up structure, I just need to write the definitions of the functions so that it works properly. 
##         The functions have been set up so that the program runs in an infinite loop, since many of the functions just return True at the moment.
##         First thing I need to do is write the functions so that the program can at least not go infinitely, after that I will look to make sure the logic
##         is all correct, and I am getting the results desired. Once all the functions have been appropriately defined, the program should run the slots game.
##         Note: There are some minor changes and additions that need to be made to the main code to make the final print message display the correct values.
##
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################

import random


def play_again() -> bool:
    ''' Asks the user if they want to play again, returns False if N or NO, and True if Y or YES.  Keeps asking until they respond yes '''
    '''play = input('Do you want to play again? ==> ')
    playCheck = ['y', 'n', 'yes', 'no']
    while play not in playCheck:
        play = input('Do you want to play again? ==> ')
        if play.lower() == 'n' or 'no':
            return False
        else:
            return True'''

    while True:
        play = input('Do you want to play again? ==> ')
        if play.lower() == 'y' or play.lower() == 'yes':
            return True
        elif play.lower() == 'n' or play.lower() == 'no':
            return False
        print('You must enter Y/YES/N/NO to continue. Please try again')

        
     
def get_wager(bank : int) -> int:
    ''' Asks the user for a wager chip amount.  Continues to ask if they result is <= 0 or greater than the amount they have '''

    bet = int(input('How many chips do you want to wager? ==> '))
    while True:

        if bet > bank:
            print('The wager amount cannot be greater than how much you have.', bank)
            bet = int(input('How many chips do you want to wager? ==> '))
        if bet < 0:
            print('The wager amount must be greater than 0. Please enter again')
            bet = int(input('How many chips do you want to wager? ==> '))
        if bet <= bank and bet > 0:
            return bet
                

def get_slot_results() -> tuple:
    ''' Returns the result of the slot pull '''
    slot1 = random.randint(1,10)
    slot2 = random.randint(1,10)
    slot3 = random.randint(1,10)

    return slot1, slot2, slot3

def get_matches(reela, reelb, reelc) -> int:
    if reela == reelb and reelb == reelc:
        return 3
    if reela == reelb or reelb == reelc or reela == reelc:
        return 2
    else:
        return 0

def get_bank() -> int:
    ''' Returns how many chips the user wants to play with.  Loops until a value greater than 0 and less than 101 '''
    bank = int(input('How many chips do you want to start with? ==> '))
    while True:
        if bank < 0:
            print('Too low a value, you can only choose 1 - 100 chips')
            bank = int(input('How many chips do you want to start with? ==> '))
        if bank > 100:
            print('Too high a value, you can only choose 1 - 100 chips')
            bank = int(input('How many chips do you want to start with? ==> '))
        if bank > 0 and bank <= 100:
            return bank


def get_payout(wager, matches):
    ''' Returns how much the payout is.. 10 times the wager if 3 matched, 3 times the wager if 2 match, and negative wager if 0 match '''

    if matches == 3:
        return wager * 10
    if matches == 2:
        return wager * 3
    else:
        return wager * -1     


if __name__ == "__main__":

    playing = True
    while playing:

        bank = get_bank()
        bank_start = bank
        bank_max = 0
        count = 0

        while bank > 0: 
            
            wager = get_wager(bank)

            reel1, reel2, reel3 = get_slot_results()

            if bank_max < bank:
                bank_max = bank

            matches = get_matches(reel1, reel2, reel3)
            payout = get_payout(wager, matches)
            bank = bank + payout
            count +=1

            print("Your spin", reel1, reel2, reel3)
            print("You matched", matches, "reels")
            print("You won/lost", payout)
            print("Current bank", bank)
            print()
           
        print("You lost all", bank_start, "in", count, "spins")
        print("The most chips you had was", bank_max)
        playing = play_again()