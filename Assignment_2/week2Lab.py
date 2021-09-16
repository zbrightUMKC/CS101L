########################################################################
##
## CS 101 Lab Week 2
## Program 2
## Zack Bright
## zmbrfq@umkc.edu
##
## PROBLEM : We need to build a program that calculates a student's grade given the weights of the different coursework i.e. Labs, Lab Exams, Attendance
##
## ALGORITHM : (Labs * 0.7) + (Lab Exams * 0.2) + (Attendance * 0.1)
##
##
## ERROR HANDLING:
##      If any score less than zero or greater than 100 is entered,
##      the program will set negative values to 0 and values greaater than 100 to 100, and print out a message to inform the user.
##
## OTHER COMMENTS:
##      I'm not sure if this is the correct way to format everything, hopefully you will correct me if this isn't what you were looking for.
##
########################################################################

print('**** Welcome to the LAB grade calculator! ****\n')

# Get all necessary inputs and correct out of range answers as necessary
name = input('Who are we calculating grades for? ==> ')
print()

# Gets input for lab and adjusts score if above 100 or below 0
labs = float(input('Enter the Labs grade? ==> '))
if labs > 100:
    labs = 100
    print('You lab value should have been 100 or less. It has been changed to 100.')
if labs < 0:
    labs = 0
    print('You lab value should have been zero or greater. It has been changed to zero.')
print()

# Gets input for exams and adjusts score if above 100 or below 0
exams = float(input('Enter the EXAMS grade? ==> '))
if exams > 100:
    exams = 100
    print('You exam value should have been 100 or less. It has been changed to 100.')
if exams < 0:
    exams = 0
    print('You exam value should have been zero or greater. It has been changed to zero.')
print()

# Gets input for attendance and adjusts score if above 100 or below 0
attendance = float(input('Enter the Attendance grade? ==> '))
if attendance > 100:
    attendance = 100
    print('You attendance value should have been 100 or less. It has been changed to 100.')
if attendance < 0:
    attendance = 0
    print('You attendance value should have been zero or greater. It has been changed to zero.')
print()

# Use algorithm to claculate grade
grade = ( (labs * 0.7) + (exams * 0.2) + (attendance * 0.1) )

# Use If-Else statement to assign a letter grade
if grade >= 90:
    letter_grade = 'A'
elif grade >= 80:
    letter_grade = 'B'
elif grade >= 70:
    letter_grade = 'C'
elif grade >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F'

# Output result
print('The weighted grade for', name,'is', grade)
print(name,'has a letter grade of', letter_grade)
print()
print('**** Thanks for using the Lab grade calculator ****')
