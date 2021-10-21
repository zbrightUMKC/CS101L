########################################################################
##
## CS 101 Lab
## Program 7
## Zack Bright
## zmbrfq@umkc.edu
##
## PROBLEM : We are tasked with building a program that can search through a vehicle data file and return the data of cars above a certain mpg threshold
##
## ALGORITHM : 
##      The main problem here is to read through the text file, and writing only the specific information that we want. To do this, I need to read each line
##      from the input file as a list using readlines(). Once I have a list of lines, I can go through each element to change the delimiter and turn the string
##      into a list. Once each line from the original file is stored as a list of lists, I can remove the elements I don't need from each nested list. Once each
##      nested list contains only the inforamtion I want, I can go through each nested list and format the information into a string and write it to the output.
## 
## ERROR HANDLING:
##      There are a lot of potential places for input errors in this program. I have set an exception handler for each potential error that could happen.
##      The program should never crash due to bad input.
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################
def get_input_file():
    '''This function asks the user for a file name to look through for car data. Will repeatedly ask until valid file name is entered'''
    while True:
        try: # Checks to make sure the input file actually exists
            in_file = input('Enter the name of the input vehicle file ==>  ')
            f = open(in_file, 'r')
            f.close()
            break # If the file name is valid end the loop
        except FileNotFoundError:
            print("There was a File Not Found Error with", in_file)
        except ValueError:
            print("There was a Value Error with", in_file)
        except TypeError:
            print("There was a Type Error with", in_file)
        except OSError:
            print("There was an OS Error with", in_file) # If it doesn't print error message to get input again
        except IOError:
            print("There was an IO Error with", in_file)
    return in_file

def get_mpg_threshold():
    '''This function will prompt the user to enter a MPG threshold for car data in the output. Will continue to ask until value 0-100 is entered'''
    while True:
        try:
            mpg = int(input('Enter the minimum mpg ==>  '))
            if mpg > 0 and mpg <= 100: # If the input meets the requirements end the loop
                break
            elif mpg < 0:
                print('Fuel economy must be greater than 0')
            elif mpg > 100:
                print('Fuel economy must be less than 100')
        except (ValueError, TypeError):
            print('You must enter a number 0-100')
    return mpg

def get_output_file():
    '''This function asks the user for a file name to output the results of get_car_data() to. Will repeatedly ask until valid file name is entered'''
    while True:
        try:
            out_file = input('Enter the name of the output vehicle file ==>  ')
            f = open(out_file, 'w') # Will create an output file if the one you enter doesn't exist, so name just has to have legal syntax
            f.close()
            break
        except FileNotFoundError:
            print("There was a File Not Found Error with", out_file)
        except ValueError:
            print("There was a Value Error with", out_file)
        except TypeError:
            print("There was a Type Error with", out_file)
        except OSError:
            print("There was an OS Error with", out_file)
        except IOError:
            print("There was an IO Error with", out_file)
    return out_file

def format_data(answers_list):
    '''Takes a list [year, make, model, mpg] and formats the data as requested. The year, make, model are left justified 40 spaces,
    and the mpg is right justified 10 spaces. Returns a string that can then be easily written to a file'''
    string1 = str(answers_list[0])
    string2 = str(answers_list[1])
    string3 = str(answers_list[2])
    str123 = string1 + ' ' + string2 + ' ' + string3
    str123 = str123.ljust(40)
    string4 = str(answers_list[3])
    string4 = string4.rjust(10)
    string5 = str123 + string4
    return string5

def get_car_data(in_file,out_file,mpg):
    '''Reads through the in_file and writes the list [year, make, model, combined mpg] of cars above the mpg threshold into the out_file'''
    open_in = open(in_file, 'r')
    open_out = open(out_file, 'w')

    spam = open_in.readlines()

    for i in range(1,len(spam)):
        #This loop goes through the list of lines from the text file and refines it to show us only the desired output
        spam[i] = spam[i].replace("\t", ',')
        spam[i] = spam[i].strip()
        spam[i] = spam[i].split(',') # Turns each line on the original file into a list we can iterate through more easily
        # Here we remove all elements except year, make, model, and combined mpg
        del spam[i][9],spam[i][8], spam[i][6], spam[i][5], spam[i][4], spam[i][3]
        
        # This try block catches bad data entries for the combined mpg field. Will print a message to the screen if a certain car's data cannot be displayed
        try:
            if float(spam[i][3]) >= mpg:
                car_info = format_data(spam[i])
                open_out.write('{}\n'.format(car_info))
                #print('{}\n'.format(car_info))
        except (TypeError, ValueError):
            print('Could not convert value',str(spam[i][3]),'for vehicle', str(spam[i][0]), str(spam[i][1]), str(spam[i][2]))
    
    open_in.close()
    open_out.close()



###MAIN###

# Get the minimum mpg threshold for data to retrieve and write to the output file
mpg = get_mpg_threshold()
print()

# Get the name of the vehicle information file to read through
in_file = (get_input_file())
print()

# Get the name of the output file to write the desired information to
out_file = (get_output_file())
print()

# Put all the information we have gotten from our user together to produce the result
get_car_data(in_file, out_file, mpg) 
