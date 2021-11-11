def get_file_name():
    '''Asks the user for the name of a text file. Will ask until valid file name given.'''
    while True:
        try:
            file_name = input("Enter the name of the file to open ")
            text_file = open(file_name)
            text_file.close()
            break
        except FileNotFoundError:
            print("Could not open file", file_name)
            print('Please try again')
            print()
    return file_name

def clean_puncuation(file_name):
    '''Takes the name of a file, reads it. Converts the contents to a one line string of lowercase words seperated by single spaces without puncuation.'''
    words = open(file_name)
    word_string = words.read()
    word_string = word_string.replace('.',' ', -1)
    word_string = word_string.replace('!',' ', -1)
    word_string = word_string.replace('\n',' ', -1)
    word_string = word_string.replace('  ',' ', -1)
    clean_words = list(filter(lambda x: x.isalnum() or x == ' ', word_string))
    words = ''
    for i in clean_words:
        words = words + i
    words = words.replace('  ',' ', -1)
    words = words.strip(' ')
    return words.lower() 

def top_ten(clean_word_str):
    '''Takes a string of words seperated by spaces and prints the ten most frequently occuring words in the order of descending frequency. 
    If there are less than 10 unique words, the function returns however many words there are.'''
    # Build a list from the given string
    word_list = clean_word_str.split(' ')
    # Initialize an empty list
    word_count_dict = {}
    # Create a set of the words in the list, this will serve as a list of keys we can refference to build our dict above
    word_set = set(word_list)
    # Build dict of word:occurence pairs from the string given
    for i in word_set:
        word_count_dict[i] = clean_word_str.count(i)
    # Reduce the dict to only contain words with length of at least 4
    more_than_three = {}
    for i in word_count_dict:
        if len(i) > 3:
            more_than_three[i] = word_count_dict[i]
    # Sort dict by word count
    sorted_tuple = tuple(sorted(more_than_three.items(), reverse=True, key=lambda elem: elem[1]))
    # Print in desried format
    print('Most frequently used words')
    print('#         Word            Freq.')
    print('================================')
    length = 10
    if len(sorted_tuple) < 10:
        length = len(sorted_tuple)
    for i in range(length):
        print(str(i+1).ljust(9), str(sorted_tuple[i][0]).ljust(19), str(sorted_tuple[i][1]))

def only_once(clean_word_str):
    '''Takes a string of words seperated by spaces and returns the amount of words of length >3 that occur only one time in the string'''
    # All the code before the next line break, is copied from top_ten(str) to build a dict of word:occurence pairs
    word_list = clean_word_str.split(' ')
    word_count_dict = {}
    word_set = set(word_list)
    for i in word_set:
        word_count_dict[i] = clean_word_str.count(i)
    more_than_three = {}
    for i in word_count_dict:
        if len(i) > 3:
            more_than_three[i] = word_count_dict[i]
    # Once we have our dict of word:occurence pairs we can simply create a new dict and only add to it the pairs where the value == 1        
    single_occurance = {}
    for i in more_than_three:
        if more_than_three[i] == 1:
            single_occurance[i] = more_than_three[i]
    return len(single_occurance)

def total_unique_words(clean_word_str):
    '''Takes a string of words spereated by single spaces and returns the number of unique words in the string.'''
    # Convert the string of words into a list of the words greater than length 3
    word_list = clean_word_str.split(' ')
    word_list3 = []
    for i in word_list:
        if len(i) > 3:
            word_list3.append(i)
    # Convert the list to a set to get the unique word count from it's length 
    word_set = set(word_list3)
    total_unique = len(word_set)
    return total_unique

if __name__ == '__main__':
    # Get name of file to get word list from, also checks to make sure it is a valid file
    text_file = get_file_name()
    # Get rid of all puncuation, build a string that's one line of words seperated by a single space.
    words_and_spaces = clean_puncuation(text_file)
    print()
    # Print top ten occuring words, or however many of each word over 3 characters there are if less than ten words total
    top_ten(words_and_spaces)
    print()
    # Print the amount of words that occur only once
    print('There are {} words that occur only once'.format(only_once(words_and_spaces)))
    # Print amount of toal unique words
    print('There are {} unique words in the document'.format(total_unique_words(words_and_spaces)))

