########################################################################
##
## CS 101 Lab
## Program 5
## Zack Bright
## zmbrfq@umkc.edu
##
## PROBLEM : The library want to design a new library card system. We need to build a program for the verification of the card number
##
## ALGORITHM : 
##      The card number has a few different specific parts. WE will need to check each part of the card to make sure it matches to what it should be. 
##      Once we have checked each character in the number we need to calculate the check digit and confirm the last index matches our calculation.
##      To do this, we will seperate the card number checks into various functions and then bring them all together in the main program.
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################
import string


def character_value(char : str) -> int:
    ''' Returns 0 for A, 1 for B, etc. '''
    char = char.upper()
    char_num = string.ascii_uppercase.index(char)
    return char_num

def get_check_digit(idnumber : str) -> int:
    ''' Returns the check digit for the name and sid. '''
    check_digit = -1
    sum = 0
    # Calculates first half of sum of card number through letters
    for i in range(0,5):
        value = int(character_value(idnumber[i]))
        value_times_index = value * (i + 1)
        sum += int(value_times_index)
    #  Calculates number part of card
    for i in range(5,10):
        value = int(idnumber[i])
        value_times_index = value * (i + 1)
        sum += int(value_times_index)

    # returns the check digit value based on given calculation
    check_digit = sum % 10
    return check_digit

def is_valid(idnumber : str) -> tuple:
    ''' returns 2 values bool and a string with errors if bool is False '''
    # checks length of string for 10 entries
    if len(idnumber) != 10:
        return False, 'The length of the number given must be 10'
    # confirms first five entries are letters
    for i in idnumber[0:5]:
        if i.isdigit():
            val = (idnumber[int(i)])
            i = int(i)-1
            message = 'The first 5 characters must be A-Z, the invalid character is at ' + str(i) +  ' is ' + val
            return False, message
    # checks last 3 digits are numbers
    for i in idnumber[7:10]:
        if i.isdigit() == False:
            index = idnumber.index(i)
            val = idnumber[index]
            message = 'The last 3 characters must be 0-9, the invalid character is at ' + str(index + 5) + ' is ' + val
            return False, message
    # checks for valid school
    if idnumber[5] != '1' and idnumber[5] != '2' and idnumber[5] != '3':
        return False, "The sixth character must be 1 2 or 3"
    # checks for valid grade
    if idnumber[6] != '1' and idnumber[6] != '2' and idnumber[6] != '3' and idnumber[6] != '4':
        return False, "The seventh character must be 1 2 3 or 4"
    # checks last digit against calculated check digit value
    if int(idnumber[9]) != int(get_check_digit(idnumber)):
        message = 'Check digit ' + idnumber[9] +  ' does not match calculated value ' + str(get_check_digit(idnumber))
        return False, message
    # if passes all tests, it is a valid card so True
    return True, ''

# I think this funtion is obsolete but I'm too scared to comment it out and possibly mess up my syntax again
def verify_check_digit(idnumber : str) -> tuple:
    ''' returns True if the check digit is valid, False if not '''
    if int(idnumber[9]) == get_check_digit(idnumber):
        return True
    else:
        return False
# returns school name based on value entered
def get_school(idnumber : str) -> str:
    ''' Returns the school the 5th index or 6th character is for. '''
    if idnumber[5] == '1':
        return 'School of Computing and Engineering SCE'
    elif idnumber[5] == '2':
        return 'School of Law'
    elif idnumber[5] == '3':
        return 'College of Arts and Sciences'
    else:
        return 'Invalid School'
# returns grade based on value entered
def get_grade(idnumber : str) -> str:
    '''Returns the grade for index 6'''
    if idnumber[6] == '1':
        return 'Freshman'
    elif idnumber[6] == '2':
        return 'Sophomore'
    elif idnumber[6] == '3':
        return 'Junior'
    elif idnumber[6] == '4':
        return 'Senior'
    else:
        return 'Invalid Grade'

if __name__ == "__main__":

    print("{:^60}".format("Linda Hall"))
    print("{:^60}".format("Library Card Check"))
    print("="*60)

    while True:

        print()
        card_num = input("Enter Libary Card.  Hit Enter to Exit ==> ").upper().strip()
        if card_num == "":
            break
        result, error = is_valid(card_num) #verify_check_digit(card_num)
        if result == True:
            print("Library card is valid.")
            print("The card belongs to a student in {}".format(get_school(card_num)))
            print("The card belongs to a {}".format(get_grade(card_num)))
        else:
            print("Libary card is invalid.")
            print(error)