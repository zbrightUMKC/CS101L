def add_test():
    '''Asks for a score greater than zero as input and adds it to the global list tests.'''
    global tests
    while True: # Will continue to ask for input until valid number > 0 is entered
        try:
            score = float(input('Enter the new Test score 0-100 ==> '))
            if score > 0:
                break
            else:
                print('Score must be greater than 0')
                continue
        except(ValueError):
            print('Score must be a number between 0-100')
        
    tests.append(score)

def remove_test():
    '''Asks for a score as input, checks if the score is contained as an element in the global list tests, and removes it if it is.'''
    global tests
    try:
        score = float(input('Enter the Test score to remove 0-100 ==> '))
        if score < 0:
            print('Score must be greater than 0')
        if score in tests:
            tests.remove(score)
        else:
            print('Could not find that score to remove')
    except(ValueError):
        print('Score must be a number between 0-100')

def clear_tests():
    '''Resets the global variable tests to an empty list'''
    global tests
    tests = []
    return tests

def add_assignment():
    '''Asks for a score as input and adds it to the global list assignments.'''
    global assignments
    while True: # Will continue to ask for input until valid number > 0 is entered
        try:
            score = float(input('Enter the new Assignment score 0-100 ==> '))
            if score > 0:
                break
            else:
                print('Score must be greater than 0')
                continue
        except(ValueError):
            print('Score must be a number between 0-100')
        
    assignments.append(score)

def remove_assignment():
    '''Asks for a score as input, checks if the score is contained as an element in the global list assignments, and removes it if it is.'''
    global assignments
    try:
        score = float(input('Enter the Test score to remove 0-100 ==> '))
        if score < 0:
            print('Score must be greater than 0')
        if score in assignments:
            assignments.remove(score)
        else:
            print('Score could not be found')
    except(ValueError):
        print('Score must be a number between 0-100') 

def clear_assignments():
    '''Resets the global variable assignments to an empty list'''
    global assignments
    assignments = []
    return assignments

def calculate_stats(scores, score_name):
    if len(scores) > 0: # To prevent possible ZeroDivisionError when calculating mean and standard deviation
        # Calculate all the different statistics we want to display
        mean = sum(scores) / len(scores)
        max_score = max(scores)
        min_score = min(scores)
        std_factors = list(map(lambda x: (x - mean) ** 2, scores))
        std_numerator = functools.reduce(lambda x,y: x + y, std_factors) 
        if std_numerator > 0:
            std = math.sqrt((std_numerator) / len(scores))
        else:
            std = 0
        mean_str = '{:.2f}'.format(mean)
        std_str = '{:.2f}'.format(std)
        # Print the calculated stats
        print(score_name.ljust(20), str(len(scores)).ljust(10), str(min_score).ljust(10), str(max_score).ljust(10), mean_str.ljust(10), std_str.ljust(10))
    else:
        # If no scores are entered, print n/a for undefined stats
        print(score_name.ljust(20), str(len(scores)).ljust(10), 'n/a'.ljust(10), 'n/a'.ljust(10), 'n/a'.ljust(10), 'n/a'.ljust(10))

def display_scores(tests, assignments):
    '''Calculates the quantity of scores in boths lists as well as the min, max, average, and standard deviation of the scores if the length of that list is greater than 0'''
    print_display_header()
    calculate_stats(tests, 'Tests')
    calculate_stats(assignments, 'Programs')
    print()

    # This if-else statement calculates the weighted score according to the given requirements
    if (len(tests) > 0) and (len(assignments) > 0):
        test_mean = sum(tests) / len(tests)
        assignment_mean = sum(assignments) / len(assignments)
        final_grade = (test_mean * 0.6) + (assignment_mean * 0.4)
    elif (len(tests) > 0) and (len(assignments) == 0):
        test_mean = sum(tests) / len(tests)
        final_grade = (test_mean * 0.6)
    elif(len(assignments) > 0) and (len(tests) == 0):
        assignment_mean = sum(assignments) / len(assignments)
        final_grade = (assignments * 0.4)
    else:
        final_grade = 0
    print('The weighted score is       {:.2f}'.format(final_grade))

def print_menu(): 
    '''Prints the option menu'''
    print('Grade Menu'.rjust(20))
    print('1 - Add Test')
    print('2 - Remove Test')
    print('3 - Clear Tests')
    print('4 - Add Assignment')
    print('5 - Remove Assignment')
    print('6 - Clear Assignments')
    print('D - Display Scores')
    print('Q - Quit')
    print()

def print_display_header():
    '''Builds and prints the header for displaying the scores with approprate whitespaces'''
    score_type = 'Type'.ljust(21)
    score_quant = '#'.ljust(11)
    score_min = 'min'.ljust(11)
    score_max = 'max'.ljust(11)
    score_avg = 'avg'.ljust(11)
    score_std = 'std'.ljust(11)

    header = score_type + score_quant + score_min + score_max + score_avg + score_std
    print(header)
    print('=' * 69)

###MAIN###

# Import modules
import functools
import math

# Initialize lists
tests = []
assignments = []

# Loop unitl the break statement inside the nested if-else block is reached
while True:
    print()
    print_menu() # Displays menu of choices to user
    choice = input('==>  ')
    print()

    #This if-else block has a branch for each menu choice, plus a branch to catch bad input.
    if choice == '1':
        add_test()
    elif choice == '2':
        remove_test()
    elif choice == '3':
        clear_tests()
    elif choice == '4':
        add_assignment()
    elif choice == '5':
        remove_assignment()
    elif choice == '6':
        clear_assignments()
    elif choice.upper() == 'D':
        display_scores(tests, assignments)
    elif choice.upper() == 'Q':
        break
    else: # Catches bad input
        print('You must enter one of the following options: 1/2/3/4/5/6/D/Q')
