########################################################################
##
## CS 101 Lab
## Program 6
## Zack Bright
## zmbrfq@umkc.edu
##
## PROBLEM : We are building a program that can encode and decode Ceaser Ciphers
##
## ALGORITHM : 
##      One of the main challenenges weith this problem is making the alphabet wrap around. For example, if we are shifting all letters down by 1, Z must wrap to A
##      To accomplish this, we check the new ord() value and if it is out of range oz A-Z ascii values then we enter a loop that uses the distance from A-Z
##      to measure how the character should wrap
##
## ERROR HANDLING:
##      Any Special Error handling to be noted. 
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################

import string

def encode():
    '''This function encodes a string by shifting each letter in the word over by the inputted number. For example if the string entered is "ABC" and the number entered is 1, the encoded string is "BCD"'''
    print()
    # Get input
    code = input('Enter (brief) text to encrypt: ')
    num = int(input('Enter the number to shift the letters by: '))
    # Initialize Variables
    code = code.upper()
    value = 0
    new_value = 0
    correct_num = 0
    new_code = ''
    # Go through each character in inputted string
    for i in range(len(code)):
        if code[i] not in string.ascii_uppercase: # If the character is not a letter, assume it's a space and so it does NOT shift in the encoded word
            new_code = new_code + ' '
            continue
        # Get the ascii value for the encoded character
        value = ord(code[i]) 
        new_value = value + num
        # We need to make sure the alphabet wraps around back to A after Z. Check ascii values to be sure
        if new_value > 90:
            correct_num = new_value - 90
            new_value = 64 + correct_num
            new_code = new_code + chr(new_value)
        else:
            new_code = new_code + chr(new_value)
    # print the encoded word
    print('Encrypted:', new_code)
    print()

def decode():
    '''This function decodes a string that has been encoded by the encode() function. For example if the string entered is "BCD" and the number entered is 1, the encoded string is "ABC"'''
    print() 
    # Get input
    code = input('Enter (brief) text to decrypt: ')
    num = int(input('Enter the number to shift the letters by: '))
    # Initialize Variables
    code = code.upper()
    value = 0
    new_value = 0
    correct_num = 0
    new_code = ''
    # Go through each character in inputted string
    for i in range(len(code)):
        if code[i] not in string.ascii_uppercase: # If the character is not a letter, assume it's a space and so it does NOT shift in the encoded word
            new_code = new_code + ' '
            continue
        # Get the ascii value for the encoded character
        value = ord(code[i])
        new_value = value - num
        # We need to make sure the alphabet wraps around back to Z after A. Check ascii values to be sure
        if new_value < 65:
            correct_num = 65 - new_value
            new_value = 91 - correct_num
            new_code = new_code + chr(new_value)
        else:
            new_code = new_code + chr(new_value)
    # print the encoded word
    print('Decrypted:', new_code)
    print()

# This is where the main program begins
while True:
    print() # The selection menu prints every iteration of the loop
    print('1) Encode a string')
    print('2) Decode a string')
    print('Q) Quit')
    # get input for selection
    play = input('Enter your selection ==> ')
    # This if-else statement checks to make sure the input is a valid selection
    if play == 'Q' or play == 'q': 
        print('Have a great day')
        break
    elif play == '1': # If 1 is entered, call the encode function
        encode()
    elif play == '2': # If 2 is entered, call the decode function
        decode()
    # Prints error message with more explicit instructions if invalid input is entered.
    print('You must enter 1, 2, or Q/q to continue. Please try again')