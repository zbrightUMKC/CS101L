########################################################################
##
## CS 101 Lab
## Program 3
## Zack Bright
## zmbrfq@umkc.edu
##
## PROBLEM : We need to create a program that can guess what number the user is thinking of between 1-100 inclusive, 
##           using the results from dividing that number by 3, 5, and 7
##
## ALGORITHM : 
##      Not sure, which part of the program counts as the algorithm in this case
## 
## ERROR HANDLING:
##      Need to check each remainder of 3, 5, and 7 to make sure they are valid. 
##      I.E. If the remainder of something divided by 5 is greater than 4, there is an error in the division
##
## OTHER COMMENTS:
##      IMPORTANT ===> The remainders for something divided by x, must be at most x-1. This was how I came up with the first part of the solution.
##      The key to solving this was not creating a list of all 1-100 and narrowing it down, but instead checking all the requirements for the remainders at once
##      in a single for-loop. There is a lot of repeated code when confirming the remainder input, I think creating a function would be better here in future
##
########################################################################
# Startup message
print('Welcome to the Flarsheim Guesser!')

# Initiate some variables I will need to use later
play = 'y'
divide_by_3 = -1
divide_by_5 = -1
divide_by_7 = -1
guessed_num = -1


# Enter while loop to play game, using .lower() method to avoid case sensitivity
while play.lower() == 'y':
    print()
    print('Please think of a number between and including 1 and 100.\n')
    
    # Check for remainder when divided by 3
    divide_by_3 = int(input('What is the remainder when your number is divided by 3 ?'))
    while divide_by_3 < 0 or divide_by_3 > 2:
        if divide_by_3 < 0:
            print('The value entered must be 0 or greater')
            divide_by_3 = int(input('What is the remainder when your number is divided by 3 ?'))
        elif divide_by_3 > 2:
            print('The value entered must be less than 3')
            divide_by_3 = int(input('What is the remainder when your number is divided by 3 ?'))
    print()

    # Check for remainder when divided by 5
    divide_by_5 = int(input('What is the remainder when your number is divided by 5 ?'))
    while divide_by_5 < 0 or divide_by_5 > 4:
        if divide_by_5 < 0:
            print('The value entered must be 0 or greater')
            divide_by_5 = int(input('What is the remainder when your number is divided by 5 ?'))
        elif divide_by_5 > 4:
            print('The value entered must be less than 5')
            divide_by_5 = int(input('What is the remainder when your number is divided by 5 ?'))
    print()

    # Check for remainder when divided by 7
    divide_by_7 = int(input('What is the remainder when your number is divided by 7 ?'))
    while divide_by_7 < 0 or divide_by_7 > 6:
        if divide_by_7 < 0:
            print('The value entered must be 0 or greater')
            divide_by_7 = int(input('What is the remainder when your number is divided by 7 ?'))
        elif divide_by_7 > 6:
            print('The value entered must be less than 7')
            divide_by_7 = int(input('What is the remainder when your number is divided by 7 ?'))

    # Now we can generate a number that matches the specific remainders entered
    for i in range(0,101):
        if i % 3 == divide_by_3 and i % 5 == divide_by_5 and i % 7 == divide_by_7:
            guessed_num = i

    # Output the result
    print('Your number was',guessed_num)
    print('How amazing is that?\n')

    # While-condition check to make sure the loop is not infinitely repeating but also only accepts valid input
    play = input('Do you want to play again? Y to continue, N to quit  ==> ')
    playCheck = ['y','n']
    while play not in playCheck:
        play = input('Do you want to play again? Y to continue, N to quit  ==> ')
        if play == 'n':
            break