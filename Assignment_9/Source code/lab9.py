import csv

def month_from_number(number):
    '''The month_from_number function takes an integer as a parameter and returns a string.
    The parameter is expected to be 1 to 12 and returns the string result for the month.'''
    months = {1 : 'January', 2 : 'February', 3: 'March', 4 : 'April', 5 : 'May', 6 : 'June', 7 : 'July', 8 : 'August', 9 : 'September', 10 : 'October', 11 : 'November', 12 : 'December'}
    if number < 1 or number > 12:
        raise ValueError('Month must be 1-12')
    else:
        month = months[number]
    return month

def read_in_file(file_name):
    '''The read_in_file function takes a filename as a string and returns a list of list of list of the contents. 
    Each sublist is a row from the file. The file is expected to be a comma separated value.'''
    list_of_crimes = [] # Initialize empty list
    file = open(file_name, encoding='utf-8') # Open file
    file_csv = csv.reader(file) # Read file contents
    for line in file_csv: # Iterate through the contents and appends data to empty list
        list_of_crimes.append(line)
    file.close() # Close file
    return list_of_crimes

def create_reported_date_dict(list_of_crimes):
    '''The create_reported_date_dict function takes a list, which is the list of lists returned from the read_in_file function above and returns a dictionary 
    where the key is a date of the year found in index 1, and the value is how many times a crime occurred on that data as read from the file.'''
    date_list = [] # Initialize empty list
    for crime in list_of_crimes[1:]: # Build list of dates that crimes have occured
        date_list.append((crime[1]))
    date_count = {} # Initialize empty dict
    for date in date_list: # Build dict of date:crime occurence pairs
        if date in date_count: # If date in dict add one to the value
            date_count[date] = date_count[date] + 1
        else: # If date not in dict, add it
            date_count[date] = 1
    return date_count

def create_reported_month_dict(list_of_crimes):
    '''The create_reported_month_dict function takes a list, which is the list of lists returned from the read_in_file function above 
    and returns a dictionary where the key is the month of the offense, and the value is how many times a crime occurred on that data as read from the file.'''
    # Initialize container objects
    date_list = []
    month_list = []
    month_count = {}
    for crime in list_of_crimes[1:]: # Build list of dates that crimes have occured
        date_list.append((crime[1]))
    for date in date_list: # From each date, save just the number for the month as a list
        month_list.append(int(date[0:2]))
    for month in month_list: # Build dict of month:crime occurence pairs
        if month in month_count: # If month in dict add one to the value
            month_count[month] = month_count[month] + 1
        else: # If month not in dict, add it
            month_count[month] = 1
    return month_count

def create_offense_dict(list_of_crimes):
    '''This function takes a list, again it is the list returned from read_in_file function 
    and returns a dictionary where the key the offense (Arson, Burglary, etc) and the value is how many times that offense occurs.'''
    offense_list = [] # Initialize empty list
    for crime in list_of_crimes[1:]: # Build list of offenses that have occured
        offense_list.append((crime[7]))
    offense_count = {} # Initialize empty dict
    for offense in offense_list: # Build dict of offense type:occurence pairs
        if offense in offense_count: # If offense in dict add one to the value
            offense_count[offense] = offense_count[offense] + 1
        else: # If offense not in dict, add it
            offense_count[offense] = 1
    return offense_count

def create_offense_by_zip(list_of_crimes): 
    '''This function takes a list, again it is the list returned from read_in_file function and returns a dictionary where the key is the offense (Arson, Burglary, etc) 
    and the value is another dictionary. This sub dictionary has a key for the zip code, and a value that is how many times this offense occurs in this zip code.'''
    # Initialize container objects
    offense_list = []
    offence_zip_dict = {}
    for crime in list_of_crimes[1:]: # Build list of offenses that have occured
        offense_list.append((crime[7]))
    for offense in offense_list: # Take each offense from the list above and set it as the key of a pair, set the value of each key as an empty dict
        offence_zip_dict[offense] = {} # {'Vehicular – Non-Injury': {}, 'Stealing – Shoplift': {}, 'Embezzlement': {}}
    for crime in list_of_crimes[1:]: # Check each crime data entry
        for offense in offence_zip_dict: # Find the offense in offense_zip_dict that matches the offense in the crime data entry
            if crime[7] == offense: 
                zipcode = crime[13] # Get value of zipcode that offense occured in
                if zipcode in offence_zip_dict[crime[7]]: # Add zipcode:occurence pair to the empty nested dict which we set as the value for the key in offence_zip_dict
                    offence_zip_dict[crime[7]][zipcode] = offence_zip_dict[crime[7]][zipcode] + 1 # If zipcode in dict add one to the value
                else:
                    offence_zip_dict[crime[7]][zipcode] = 1 # If zipcode not in dict, add it
    return offence_zip_dict

if __name__ == "__main__":
    # Get valid file name
    while True:
        try:
            file_name = input('Enter the name of the crime data file ==> ')
            file = open(file_name)
            file.close()
            break
        except FileNotFoundError:
            print('Could not find the file specified. {} does not exist'.format(file_name))
    print()
    # Get and print highest crime month 
    list_of_crimes = read_in_file(file_name)
    month_dict = create_reported_month_dict(list_of_crimes)
    highest_month_amount = 0
    for i in month_dict.items():
        if month_dict[i[0]] > highest_month_amount:
            highest_month_amount = month_dict[i[0]]
            highest_month = i[0]
    month = month_from_number(highest_month)
    print('The month with the highest number of crimes is {} with {} offenses.'.format(month, highest_month_amount))
    # Get and print highest crime offense
    offenses_dict = create_offense_dict(list_of_crimes)
    highest_offense_amount = 0
    for i in offenses_dict.items():
        if offenses_dict[i[0]] > highest_offense_amount:
            highest_offense_amount = offenses_dict[i[0]]
            highest_offense = i[0]
    print('The offense with the highest number of crimes is {} with {} offenses.'.format(highest_offense, highest_offense_amount))
    print()
    # Get offense name
    offenses_zip = create_offense_by_zip(list_of_crimes)
    while True:
        crime_name = input('Enter an offense ==> ')
        if crime_name in offenses_zip.keys():
            break
        else:
            print('Not a valid offense name, please try again.')
    print()
    # Print the number of occurences of inputted offense in each zip code they occured in 
    print('{} offenses by Zip Code'.format(crime_name))
    print('Zip Code               # Offenses')
    print('=================================')
    for k,v in offenses_zip[crime_name].items():
        print('{}                           {}'.format(k,v))