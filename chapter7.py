"""
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section that explain the required code
    Your file should compile error free
    Submit your completed file
"""

# TODO 7.2 Lists
# Create a list of days of the week, assign it to the variable days, remove """ """ to test
days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
print(days)

# Create a list with 5 items, set them all to 0, use the Repetition Operator ( * )
numbers = [0] * 5

# print the contents of your days list using the for operator
for d in days:
    print(d)

# print the list item that holds the value Saturday from the days list by using it's index
print(days[5])

# set the size variable to hold the length of the list days using the len function
size = len(days)
# concatenate the two following lists together, storing the value in list3 - remove the """ """ to test

list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6, 8, 10]
list3 = list1 + list2
print(list3)

# TODO 7.3 List Slicing
# Slice the list days to select from Monday through Friday, inclusive, and assign the new list to work_days
# print work_days

work_days = days[:5]
print(work_days)

# TODO 7.4 Finding items in Lists with the in Operator
# test to see if "Tue" is in the list days, print yes, Tue is in the list or no, Tue is not in the list
day = "tue"
if day in days:
    print('Tue is in the list')
else:
    print('Tue is not in the list.')

# TODO 7.5 List Methods and Useful Built-in Functions
# Complete the following code to append the last three months of the year to the list months. Remove
# the """   """ to test, and print the contents of months

months = list(["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept"])
months.append('october')
months.append('november')
months.append('december')
print(months)

# get the index of "May" from the months list and print it on screen
print(months.index('May'))
# sort list3 from the 7.2 exercise and print the results on screen
list3.sort()
print(list3)
# reverse the order of list 3
list3.reverse()
# delete the number 5 from list 3 and print the list(remeber we reversed the list)
del list3[5]
# print the maximum item from list 3
print(max(list3))

# TODO 7.6 Copying Lists
# copy the list months to the variable months_of_the_year
# print the values in months_of_the_year

months_of_the_year = [] + months
print(months_of_the_year)
# TODO 7.7 Processing lists
# total the values in list3 and print the results
total = 0
count = 0
for number in list3:
    total += number
    count = count + 1
print(total)
# get the average of values in list 3 and print the results
average = total/len(list3)
print(count)
# open the file states in read mode, read the contents of the file into the list states_list and print the
# contents of states_list on screen
states_file = open('states.txt', 'r')
line = states_file.readline()
states_list = []
while line != '':
    states_list.append(line)
    line = states_file.readline()
for d in states_list:
    print(d)
states_file.close()

# TODO 7.8 Two-Dimensional Lists
# Create a two dimensional list that has the months of the year and the days in each month during a non leap year
# print the contents of the list
months1 = [["Jan", 31], ["Feb", 28], ["Mar", 31], ["Apr", 30], ["May", 31], ["June", 30], ["July", 31], ["Aug", 31], ["Sept", 30], ['October', 31], ['November', 30], ['December', 31]]
for d in months1:
    print(d)
# print just the values for index 3,0 and 3,1
print(months1[3][0])
print(months1[3][1])
# TODO 7.9 Tuples
# convert the months list to a tuple
month_tuple = tuple(months1)
