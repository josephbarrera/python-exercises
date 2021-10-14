#!/usr/bin/env python
# coding: utf-8

# # 1. Conditional Basics
# 
# a. prompt the user for a day of the week, print out whether the day is Monday or not

# In[1]:


today_is_Monday = True

if today_is_Monday:
    print('It\'s so Monday')
else:
    print('It\'s definitely not Monday')


# In[2]:


day = input('Please enter the day of the week')

if day.lower() in ['monday', 'mon']:
    print('Today is Monday')
else:
    print(f'Today is {day.capitalize()}')


# b. prompt the user for a day of the week, print out whether the day is a weekday or a weekend

# In[ ]:


today = 'Monday'
weekday = 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'
if today == weekday:
    print('Bummer, it\'s a weekday')
else:
    print('It\'s the weekend!')


# In[ ]:


day = input('Please enter the day of the week')

if day.lower() in ['sunday', 'saturday']:
    print("today is a weekend")
else:
    print('today is a weekday')


# c. create variables and make up values for
# - the number of hours worked in one week
# - the hourly rate
# - how much the week's paycheck will be

# In[ ]:


number_of_hours_worked = 45
hourly_rate = 50
overtime_pay = hourly_rate * 1.5
weekly_paycheck = number_of_hours_worked * hourly_rate


# In[ ]:





# Write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours

# In[ ]:


weekly_paycheck

if number_of_hours_worked <= 40:
    total_pay = hours_worked * hourly_rate
else:
    regular_pay = 40 * hourly_rate
    overtime_pay = (hours_worked - 40) * overtime_rate
    total_pay = reguar_pay + overtime_pay
    
total_pay


# # 2. Loop Basics
# a. While

# - Create an integer variable i with a value of 5
# - Create a while loop that runs so long as i is less than or equal to 15
# - Each loop iteration, output the current value of i, then increment i by one

# In[4]:


i = 5
while i <= 15:
    print(i)
    i = i + 1


# - Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line

# In[7]:


i = 0
while i <= 100:
    print(i)
    i = i + 2


# - Alter your loop to count backwards by 5's from 100 to -10

# In[5]:


i = 100
while i <= 100:
    print(i)
    i -= 5
    if i == -15:
        break


# In[ ]:


i = 100


# Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000

# In[8]:


i = 2
while i <= 1000000:
    print(i)
    i == ** 2
    if i == 1000000:
        break


# In[1]:


i = 2
while i > 1_000_000:
    print(i)
    i = i * i


# Write a loop that uses print to create the output shown below:
# 100
# 95
# 90
# 85
# 80
# 75
# 70
# 65
# 60
# 55
# 50
# 45
# 40
# 35
# 30
# 25
# 20
# 15
# 10
# 5

# In[2]:


i = 100
while i <= 100:
    print(i)
    i -= 5
    if i == 0:
        break


# # For Loops

# i. Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.
# 
# For example, if the user enters 7, your program should output:
# 
# 
# 7 x 1 = 7
# 7 x 2 = 14
# 7 x 3 = 21
# 7 x 4 = 28
# 7 x 5 = 35
# 7 x 6 = 42
# 7 x 7 = 49
# 7 x 8 = 56
# 7 x 9 = 63
# 7 x 10 = 70

# In[ ]:


for n in range(1 - 10):
    x = (n + 1) * 2
    print(x)


# In[4]:


num = input('Please enter a positive integer: ')

num = int(num)

for i in range(1, 11):
    print(f' {num} * {i} = {num * i} ')


# Create a for loop that uses print to create the output shown below.
# 
# 
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# 88888888
# 999999999

# In[5]:


for i in range(1, 10):
    print(str(i) * i)


# break and continue
# 
# Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to continue prompting the user if they enter invalid input. (Hint: use the isdigit method on strings to determine this). Use a loop and the continue statement to output all the odd numbers between 1 and 50, except for the number the user entered.
# 
# Your output should look like this:
# 
# 
# Number to skip is: 27
# 
# Here is an odd number: 1
# Here is an odd number: 3
# Here is an odd number: 5
# Here is an odd number: 7
# Here is an odd number: 9
# Here is an odd number: 11
# Here is an odd number: 13
# Here is an odd number: 15
# Here is an odd number: 17
# Here is an odd number: 19
# Here is an odd number: 21
# Here is an odd number: 23
# Here is an odd number: 25
# Yikes! Skipping number: 27
# Here is an odd number: 29
# Here is an odd number: 31
# Here is an odd number: 33
# Here is an odd number: 35
# Here is an odd number: 37
# Here is an odd number: 39
# Here is an odd number: 41
# Here is an odd number: 43
# Here is an odd number: 45
# Here is an odd number: 47
# Here is an odd number: 49

# In[10]:


num = input('Please enter an odd number between 1 and 50: ')


# isdigit= False
# > 50
# <= 0
# num % 2 == 0

while True:
    if (num.isdigit() == False
       or int(num) <= 0
       or int(num) > 50
       or int(num) % 2 == 0):
        print('Invalid Input')
        num = input('Please enter an odd number between 1 and 50: ')
    else:
        break


# 

# In[13]:




num = int(num)
print(' The number to skip is ', num)

for i in range(1, 50):
    if i % 2 == 0:
        continue
    elif i == num:
        print('Yikes, skipping this number', i)
    else:
        print('Here is an odd number', i)


# 

# In[ ]:


num = input('Please input a positive integer: ')




# 

# In[ ]:





# 

# In[ ]:





# 

# In[16]:


for i in range(1, 101):
    if i % 3 == 0:
        print('fizz')
    elif i % 5 == 0:
        print('buzz')
    else:
        print(i)


# Display a table of powers:
# - Prompt

# In[18]:


num = input('Please enter a positive interger: ')

print('Here is your table!')
print('number|squared|cubed')
print('------|-------|-----')

num = int(num)
for i in range(1, num + 1):
    print(f' {i} | {i ** 2} | {i ** 3}')


# Grades

# In[3]:



choice = 'yes'

while choice.lower() == choice:
    num = input('Please enter the numberic grade: ')
    num = int(num)
    if num >= 88:
        print('A')
    elif num >= 80:
        print('B')
    elif num >= 67:
        print('C')
    elif num >= 60:
        print('D')
    else:
        print('F')
        
    choice = input('Do you want to continue? Please enter yes or y to continue')
    if choice.lower() in ['yes', 'y']:
        continue
    else:
        break


# 

# In[11]:


books = [
    {
        'title': 'title1',
        'author': 'author1',
        'genre': 'genre1'
    },  
    {
        'title': 'title2',
        'author': 'author1',
        'genre': 'genre2'
    }
    {
        'title': 'title3',
        'author': 'author2',
        'genre': 'genre2'
    },
    {
        'title': 'title4',
        'author': 'author3',
        'genre': 'genre2'
    }
]


# In[6]:


books[3]['title']


# In[ ]:


for book in books:
    print(f' The book {book[title]})


# In[ ]:


user_input = input('Please choose a genre: ')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




